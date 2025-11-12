document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search');
    const sortSelect = document.getElementById('sort-by');
    const trackContainer = document.getElementById('track-container');
    const paginationContainer = document.getElementById('pagination');
    const recentContainer = document.getElementById('recent-searches');

    let tracks = [];
    let currentPage = 1;
    const tracksPerPage = 10; // 2 rows x 5 tracks
    let recentSearches = [];

    // Fetch tracks from Flask endpoint
    fetch('/tracks')
        .then(res => res.json())
        .then(data => {
            tracks = data;
            displayTracks();
            setupPagination();
        });

    // Display current page tracks
    function displayTracks() {
        trackContainer.innerHTML = '';
        const start = (currentPage - 1) * tracksPerPage;
        const end = start + tracksPerPage;
        const paginatedTracks = tracks.slice(start, end);

        if (paginatedTracks.length === 0) {
            trackContainer.innerHTML = '<p>No results found.</p>';
            return;
        }

        paginatedTracks.forEach(track => {
            const card = document.createElement('div');
            card.classList.add('track-card');

            const albumCover = track.album_cover || '/static/default_cover.jpg';
            const trackName = track.song_name || 'Unknown Track';
            const artist = track.artist || 'Unknown Artist';
            const album = track.album || 'Unknown Album';
            const popularity = track.popularity !== undefined ? track.popularity : 'N/A';
            const duration = track.duration !== undefined ? track.duration : 'N/A';
            const url = track.url || '#';

            card.innerHTML = `
                <img src="${albumCover}" alt="Album cover" class="album-cover" loading="lazy">
                <h3 class="track-name">${trackName}</h3>
                <p class="artist">${artist}</p>
                <p class="album">Album: ${album}</p>
                <p class="popularity">Popularity: ${popularity}</p>
                <p class="duration">Duration: ${duration} mins</p>
                <p class="url"><a href="${url}" target="_blank">Listen on Spotify</a></p>
            `;
            trackContainer.appendChild(card);

            // Save search and redirect to track page
            card.addEventListener('click', () => {
                fetch('/save_search', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(track)
                }).then(() => {
                    saveRecentSearch(track);
                    window.location.href = `/track/${encodeURIComponent(track.song_name)}`;
                });
            });
        });

        renderRecentSearches();
    }

    // Pagination
    function setupPagination() {
        paginationContainer.innerHTML = '';
        const totalPages = Math.ceil(tracks.length / tracksPerPage);

        if (currentPage > 1) {
            const prev = document.createElement('button');
            prev.textContent = '« Prev';
            prev.addEventListener('click', () => {
                currentPage--;
                displayTracks();
                setupPagination();
            });
            paginationContainer.appendChild(prev);
        }

        for (let i = 1; i <= totalPages; i++) {
            const btn = document.createElement('button');
            btn.textContent = i;
            if (i === currentPage) btn.classList.add('active');
            btn.addEventListener('click', () => {
                currentPage = i;
                displayTracks();
                setupPagination();
            });
            paginationContainer.appendChild(btn);
        }

        if (currentPage < totalPages) {
            const next = document.createElement('button');
            next.textContent = 'Next »';
            next.addEventListener('click', () => {
                currentPage++;
                displayTracks();
                setupPagination();
            });
            paginationContainer.appendChild(next);
        }
    }

    // Debounce helper
    function debounce(func, delay) {
        let timeout;
        return function (...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), delay);
        };
    }

    // Search input
    searchInput.addEventListener('input', debounce(() => {
        const query = searchInput.value.toLowerCase();
        fetch('/tracks')
            .then(res => res.json())
            .then(data => {
                tracks = data.filter(track =>
                    (track.song_name && track.song_name.toLowerCase().includes(query)) ||
                    (track.artist && track.artist.toLowerCase().includes(query))
                );
                currentPage = 1;
                displayTracks();
                setupPagination();
            });
    }, 300));

    // Sort select
    sortSelect.addEventListener('change', () => {
        const value = sortSelect.value;
        if (value === 'popularity') tracks.sort((a, b) => (b.popularity || 0) - (a.popularity || 0));
        if (value === 'duration') tracks.sort((a, b) => (b.duration || 0) - (a.duration || 0));
        currentPage = 1;
        displayTracks();
        setupPagination();
    });

    // Recent searches
    function saveRecentSearch(track) {
        if (!track || !track.song_name) return;
        recentSearches = recentSearches.filter(t => t.song_name !== track.song_name);
        recentSearches.unshift(track);
        if (recentSearches.length > 5) recentSearches.pop();
        renderRecentSearches();
    }

    function renderRecentSearches() {
        if (!recentContainer) return;
        if (recentSearches.length === 0) {
            recentContainer.innerHTML = '<p class="no-recent">No recent searches.</p>';
            return;
        }
        recentContainer.innerHTML = recentSearches.map(track => `
            <div class="recent-item" onclick="window.location.href='/track/${encodeURIComponent(track.song_name)}'">
                <a href="${track.url}" target="_blank">${track.song_name}</a>
            </div>
        `).join('');
    }
});
