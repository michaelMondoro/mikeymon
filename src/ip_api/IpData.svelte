<script>
    import { fade } from "svelte/transition";
    import { mine } from "../store";
    export let data;

</script>

<div class="grid" in:fade={{ duration: 1000 }}>
    <h3>{data.ip} <emoji>🌎</emoji></h3>
    <span></span>
    <span>
        <h2>Location</h2>
        <h3>{data.city} {data.subdivision}, {data.country}</h3>
        <h3>({data.coordinates.longitude}, {data.coordinates.latitude})</h3>
    </span>
    <span>
        <h2>Info</h2>
        <h3><span class="subheading">Org:</span> {data.asn.org}</h3>
        <h3><span class="subheading">ASN #:</span> {data.asn.number}</h3>  
    </span> 
</div>
<br>

<style>
h2 {
    color: var(--secondary-color);
    margin: .5em 0em;
}

h3 {
  margin: 0em 0em;
}

.grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 1em;
    max-width: 70%;
    margin-bottom: 1em;
}
</style>