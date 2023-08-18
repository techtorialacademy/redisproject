async function fetchWithoutRedis() {
    let response = await fetch('/without_redis');
    let data = await response.text();
    document.getElementById('response').innerText = data;
}

async function fetchWithRedis() {
    let response = await fetch('/with_redis');
    let data = await response.text();
    document.getElementById('response').innerText = data;
}

