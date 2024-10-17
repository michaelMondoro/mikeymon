<script>
    import Map from "../components/Map.svelte";
    import ApiDocs from "./ApiDocs.svelte";
    import Loader from "../components/Loader.svelte";
    import IpData from "./IpData.svelte";
    import { fade } from "svelte/transition";
    import { ipApiSelectedPage } from "../store";
    import { currentIPData } from "../store";
    import { onMount } from "svelte";
    import { get } from "svelte/store";

    let data;
    let ipInput;
    let error;
    let mine = true;
    let loading = false;
    
    onMount(() => {
        if ($currentIPData) {
            data = JSON.parse($currentIPData);
        } else {
            getIP();
        }
        if (!$ipApiSelectedPage) ipApiSelectedPage.set("service")
    })
    
    async function getIP(e) {
        if (e) e.preventDefault()
        try {   
            loading = true;
            let res = await fetch(`https://mikeymon.dev/api/ip_please?ip=${ipInput ? ipInput : ''}`)
            data = await res.json()
            mine = true;
            currentIPData.set(JSON.stringify(data))
            console.log($currentIPData)
        } catch (err) {
            error = err;
            console.log(err)
        }
        loading = false;
        
    }
</script>

<div class="container" in:fade={{ duration: 1000 }}>
    <div class="heading">
        <h3>Geo IP Service <emoji>&#128640;</emoji></h3>
        <span class="subheading">
            get some cool info about any ip address or hostname. check out the API 
            <span role="button" on:click={()=>ipApiSelectedPage.set("api")} class="hover link">here</span>
        </span>
    </div>
    {#if $ipApiSelectedPage === "service"}
        <form class="horizontal-flex" on:submit={getIP} in:fade={{ duration: 1000 }}>
            <input bind:value={ipInput} on:input={() => {mine = (ipInput.length>0) ? false : true}} type="text" placeholder="ip address">
            <button type="submit" class="submit">{mine ? "check my ip" : "search ip"}</button>
        </form>
        
        {#if loading}
            <Loader />
        {/if}
        {#if !loading && data && data.city}
            <IpData data={data} />
            <Map data={data}/>
        
        {:else if data && data.error}
            <p class="error">{data.error}</p>
        {/if}

        {#if error}
            <p class="error">{error}</p>
        {/if}
    {:else if $ipApiSelectedPage === "api"}
        <ApiDocs />
    {/if}
    
</div>
<style>

.submit {
    background-color: var(--main-color);
    color: black;
    border-radius: .3em;
}
.submit:hover {
    color: var(--main-color);
    background-color: rgba(47, 47, 47, 0);
    border-radius: 1em;
    text-decoration: underline;
}
.link {
    color: var(--main-color);
    cursor: pointer;
}
.link:hover {
    text-decoration: underline;
}

input {
    all: unset;
    padding: .5em 1em;
    border-radius: .3em;
    border: solid var(--main-color) 1px;
    margin: 0 .5em;
}

h3 {
  margin: 0em 0em;
}

.error {
    background-color: rgba(134, 0, 0, 0.586);
    border: solid rgba(134, 0, 0, 1) 1px;
    padding: 1em;
    border-radius: .3em;
}

.horizontal-flex {
    display: flex;
    margin-bottom: 1em;
}

.heading {
    text-align: center;
    margin-bottom: 1em;
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