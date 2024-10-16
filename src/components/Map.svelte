<script>
    import L from 'leaflet';
    import { onMount } from 'svelte';
    import { fade } from 'svelte/transition';

    let map;
    export let data;
    onMount(() => {
        map = L.map("map",{}).setView([data.coordinates.latitude, data.coordinates.longitude], 8);
		L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
			maxZoom: 30,
			attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
		}).addTo(map);

		var marker = L.marker([data.coordinates.latitude, data.coordinates.longitude],{})
		marker.bindTooltip("<b>Location</b><br>" + data.city + ", " + data.country)
		marker.addTo(map);
    })
</script>

<svelte:head>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="" />
</svelte:head>

<div class="container" in:fade={{ duration: 1000 }}>
	<div class="mapContainer">
		<div id="map"></div>
	</div>
</div>

<style>
.container {
    width: 75%; 
    height:20em; 
    display:flex; 
    justify-content:center;
}
.mapContainer {
    width: 90%; 
    height: 100%
}
#map {
    height: 100%; 
    box-shadow: rgb(183, 179, 179) 1px 1px 7px;
}
</style>