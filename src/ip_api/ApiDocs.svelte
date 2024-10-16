<script>
    import { ipApiSelectedPage } from "../store.js";
    import { fade } from "svelte/transition";

    let curlCommand = "curl -k https://mikeymon.dev/api/ip_please?ip=78.251.236.95";
    let apiUrl = "https://mikeymon.dev/api/ip_please/";

    function copy(e) {
        navigator.clipboard.writeText(e.target.dataset.copy);
        e.target.innerText = " copied"
    }
</script>

<div class="api" in:fade={{ duration: 1000 }}>
    <div class="docs">
        <div class="header">
            <button class="header-item" on:click={()=>ipApiSelectedPage.set("service")}><i class="fa fa-arrow-left hover icon"></i></button>
            <h3 class="header-item">API Docs</h3>
            <span class="header-item"></span>
        </div>
        <span style="color: var(--secondary-color);">keeping it simple</span>
        <div class="horizontal">
            <span class="badge green">GET</span>
            <pre class="desc">{apiUrl} <i role="button" data-copy={apiUrl} on:click={copy} class="fa fa-clipboard hover"></i></pre>
        </div>
        <h3>Parameters</h3>
        <div class="horizontal">
            <span class="badge grey">OPTIONAL</span>
            <pre class="opt">{"{ ip }"}</pre><pre class="desc">address you want to get info on i.e. {"{ 78.251.236.95 }"}</pre>
        </div>
        <h3>Example</h3>
        <hr style="width: 100%">
        <div class="horizontal">
            <span class="badge blue">REQUEST</span>
            <pre class="desc">{curlCommand}<i role="button" data-copy={curlCommand} on:click={copy} class="fa fa-clipboard hover"></i></pre>
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
    display: flex;
    justify-content: space-between;
    border-bottom-right-radius: .3em;
    border-top-right-radius: .3em;
    width: 100%;
}
.desc::-webkit-scrollbar, .opt::-webkit-scrollbar {
    display: none;
}
.horizontal {
    display: flex; 
    align-items:center;
}
.docs {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: left;
    border-radius: .1em;
    width: 75%;
    padding: .5em;
    overflow-x: hidden;
}
pre {
    font-size: large;
    padding: 1em;
    background-color: rgb(22, 22, 22);
    overflow-x: scroll;
    outline: none;
}
.opt {
    border-right: solid var(--main-color) 1px; 
    min-width: 4em;
}
.blue {
    background-color: rgb(2, 98, 195);
}
.blue:hover {
    box-shadow: rgb(0, 128, 255) 0px 0px 5px;
}
.green {
    background-color: green;
}
.green:hover {
    box-shadow: green 0px 0px 5px;
}
.grey {
    background-color: gray;
}
.grey:hover {
    box-shadow: gray 0px 0px 5px;
}
.badge {
    padding: 1em;
    border-top-left-radius: .3em;
    border-bottom-left-radius: .3em;
}
.api {
    display: flex;
    width: 100%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
}
</style>