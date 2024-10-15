<script>
    import { fade } from "svelte/transition";
    import { fly } from "svelte/transition";
    import { quintOut } from 'svelte/easing';
    import Project from "./Project.svelte";

</script>

<div class="center" in:fade={{ delay: 200, duration: 1500 }}>
  <h2 style="border-bottom:solid var(--main-color) 1px">Projects</h2>

  <div class="content" >
      <Project
      title="EasyRSS" 
      desc="Python package for processing Atom and RSS feeds"
      packageName="easy_rss"
      version=1.2.5/>

      <Project
      title="GoogleTrendy" 
      desc="Package for browsing Google Search Trends"
      packageName="google_trendy"
      version=1.5/>   

      <Project
      title="TheWeather" 
      desc="Python package for getting weather data"
      packageName="the_weather"
      version=1.5/>   
  </div>

  <br><br>
  <div class="content" in:fade={{ delay: 400, duration: 1500 }}>
      <Project
      title="fireship.io - videos"
      desc="Extension for viewing the latest and greatest from the fireship.io YouTube"
      packageName="fireship.io_videos"
      defaultLink="https://marketplace.visualstudio.com/items?itemName=mikeymon.fireship-videos"
      defaultImgLink="https://img.shields.io/badge/fireshipio-VS Code-blue.svg"/>

      <Project
      title="InsightBrowser"
      desc="Desktop app built with Electron - providing a dashboard for users to visualize their web browsing"
      packageName="insight_browser" />

  </div>
</div>
<style>
.quote {
  height: 5em;
  display: flex;
  align-items: center;
  border-left: solid rgb(245, 245, 245) 1px;
  padding: 1em;
  transition: all .5s;
}

.center {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
.content {
  display: flex;
  justify-content: center;
  /* align-items: center; */
}

@media only screen and (max-width: 700px) {
  .content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0em 2em;
  }
}
</style>