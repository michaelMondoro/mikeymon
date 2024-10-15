<script>
    import Map from "./Map.svelte";
    import { fade } from "svelte/transition";
    import Loader from "./Loader.svelte";
    
    let data;
    let ipInput;
    let error;
    let mine = true;
    let loading = false;
    
    async function getIP(e) {
        if (e) e.preventDefault()
        try {   
            loading = true;
            let res = await fetch(`https://mikeymon.dev/api/ip_please?ip=${ipInput ? ipInput : ''}`)
            data = await res.json()
            ipInput = undefined;
            mine = true;
            console.log(data)
        } catch (err) {
            error = err;
            console.log(err)
        }
        loading = false;
        
    }
</script>

<div class="container" in:fade={{ duration: 1000 }}>
    <div class="heading">
        <h3>Geo IP API <emoji>&#128640;</emoji></h3>
        <span class="subheading">get some cool info about your (or anyone else's) ip address</span>
    </div>
    <br>
    <form class="horizontal-flex" on:submit={getIP}>
        <input bind:value={ipInput} on:input={() => {mine = (ipInput.length>0) ? false : true}} type="text" placeholder="ip address">
        <button>{mine ? "check my ip" : "search ip"}</button>
    </form>
    <br>
    {#if loading}
        <Loader />
    {/if}
    {#if !loading && data && data.city}
        <div class="grid" in:fade={{ duration: 1000 }}>
            <h3>{data.ip} <emoji>🌎</emoji></h3>
            <span></span>
            <span>
                <h2>Location</h2>
                <h3>{data.city}, {data.country}</h3>
                <h3>({data.coordinates.longitude}, {data.coordinates.latitude})</h3>
            </span>
            <span>
                <h2>Info</h2>
                <h3><span class="subheading">Org:</span> {data.asn.org}</h3>
                <h3><span class="subheading">ASN #:</span> {data.asn.number}</h3>  
            </span> 
        </div>

        <br>
        <Map data={data}/>
    
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
    background-color: rgba(47, 47, 47, 0);
    border-radius: 1em;
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

.heading {
    text-align: center;
}
.subheading {
  color: var(--secondary-color);

}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>