<script>
    import { ipApiSelectedPage } from "./store";
    import { fade } from "svelte/transition";
</script>

<div class="api" in:fade={{ duration: 1000 }}>
    <div class="header">
        <button class="header-item" on:click={()=>ipApiSelectedPage.set("service")}><i class="fa fa-arrow-left hover icon"></i></button>
        <h3 class="header-item">API Docs</h3>
        <span class="header-item"></span>
    </div>
    <div class="docs">
        <span style="color: var(--secondary-color);">keeping it simple</span>
        <div class="horizontal">
            <span class="badge green">GET</span>
            <pre>https://mikeymon.dev/api/ip_please/</pre>
        </div>
        <h3>Parameters</h3>
        <div class="horizontal">
            <span class="badge grey">optional</span>
            <pre>{"{ ip }"}</pre><pre class="desc">address you want to get info on i.e. {"{ 78.251.236.95 }"}</pre>
        </div>
        <h3>Example</h3>
        <hr style="width: 100%">
        <div class="horizontal">
            <pre>curl -k https://mikeymon.dev/api/ip_please?ip=78.251.236.95</pre>
        </div> 
        <pre>{
`{
    "ip": "78.251.236.95",
    "city": "Paris",
    "country": "France",
    "country_code": "FR",
    "coordinates": {
    "latitude": 48.8566,
    "longitude": 2.35222
    },
    "asn": {
    "number": 12322,
    "org": "Free SAS"
    }
}
`
            }</pre>
    </div>
    
</div>

<style>
.desc {
    border-left: solid var(--main-color) 1px;
    padding: .5em;
}
.horizontal {
    display: flex; 
    align-items:center
}
.docs {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: left;
    min-width: 70%;
    padding: 1em;
    border-radius: .1em;
}
pre {
    font-size: large;
    margin: 1em;
}
.green {
    background-color: green;
}
.grey {
    background-color: gray;
}
.badge {
    padding: .5em 1em;
    border-radius: .3em;
}
.api {
    display: flex;
    flex-direction: column;
    min-width: 50%;
    justify-content: space-between;
    align-items: center;
}
</style>