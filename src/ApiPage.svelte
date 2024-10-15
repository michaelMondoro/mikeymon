<script>
    import { fade } from "svelte/transition";

    let data;
    let ipInput;
    let error;


    async function getIP(e) {
        if (e) e.preventDefault()
        try {
            let res = await fetch(`https://mikeymon.dev/api/ip_please?ip=${ipInput ? ipInput : ''}`)
            data = await res.json()
            ipInput = undefined;
            console.log(data)
        } catch (err) {
            error = err;
            console.log(err)
        }
        
    }
</script>

<div class="container" in:fade={{ duration: 1500 }}>
    <div id="heading">
        <h3>Geo IP API <emoji>&#128640;</emoji></h3>
        <span class="subheading">get your IP info <span class="underline hover">FREE!</span></span>
    </div>
    <br>
    <form class="horizontal-flex" on:submit={getIP}>
        <input bind:value={ipInput} type="text" placeholder="ip address">
        <button>check</button>
    </form>
    
    {#if data && data.city}
        <div class="grid" in:fade={{ duration: 1500 }}>
            <h3>{data.ip} <emoji>🌎</emoji></h3>
            <span></span>
            <span>
                <h2>Location</h2>
                <h3>{data.city}, {data.country}</h3>
                <h3>({data.coordinates.longitude}, {data.coordinates.latitude})</h3>
            </span>
            <span>
                <h2>ASN Info</h2>
                <h3>{data.asn.org}</h3>
                <h3>{data.asn.number}</h3>  
            </span> 
        </div>
    
    
    {:else if data && data.error}
        <p class="error">{data.error}</p>
    {/if}

    {#if error}
        <p class="error">{error}</p>
    {/if}
    
</div>
<style>

button {
    all: unset;
    padding: .5em 1em;
    cursor: pointer;
    background-color: var(--main-color);
    color: black;
    border-radius: .3em;
    transition: all .2s;
}

button:hover {
    color: var(--main-color);
    background-color: rgba(99, 99, 99, 0);
    border-radius: .3em;
    text-decoration: underline;
}

input {
    all: unset;
    padding: .5em 1em;
    border-radius: .3em;
    border: solid var(--main-color) 1px;
    margin: 0 1em;
}

h3 {
  margin: 0em 0em;
}

h2 {
    color: var(--secondary-color);
    margin: .5em 0em;
}

.error {
    background-color: rgba(134, 0, 0, 0.586);
    border: solid rgba(134, 0, 0, 1) 1px;
    padding: 1em;
    border-radius: .3em;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 1em;
}
.horizontal-flex {
    display: flex;
}

.subheading {
  color: var(--secondary-color);
}

.underline {
  border-bottom: solid var(--secondary-color) 1px;
}
.underline:hover {
    border-color: rgb(82, 154, 254);
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>