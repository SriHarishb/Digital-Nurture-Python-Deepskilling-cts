// Request interceptor: runs before EVERY outgoing axios request, useful for
// logging, attaching auth headers, etc. Must return the (possibly modified) config.
axios.interceptors.request.use((config) => {
    console.log(`API call started: ${config.url}`);
    return config;
});



// Small wrapper around axios.get so callers don't repeat try/catch or
// `.data` unwrapping everywhere they need to fetch something.
async function apiFetch(url, params = {}) {
    const response = await axios.get(url, { params });
    return response.data;
}

async function fetchPostsByUser() {
    try {
        const posts = await apiFetch("https://jsonplaceholder.typicode.com/posts", { userId: 1 });
        console.log(`Fetched ${posts.length} posts for userId 1`);
        console.log(posts);
    } catch (error) {
        console.error("Error fetching posts by user:", error.message);
    }
}

fetchPostsByUser();