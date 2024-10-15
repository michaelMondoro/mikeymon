<script>
  import { onMount } from "svelte";
  import ApiPage from "./ApiPage.svelte";

let ready = false;
onMount(() => ready = true)
</script>
<main>
  <div class="header">
    <span>
        <a class="hover" href="https://github.com/michaelMondoro" target="_blank"><i class="fa fa-github hover icon"></i></a>
        <a class="hover" href="https://www.linkedin.com/in/michael-mondoro-8b7423151/" target="_blank"><i class="fa fa-linkedin hover icon"></i></a>
    </span>
    <span></span>
  </div>
  {#if ready}
    <ApiPage />
  {/if}
</main>

  
<style>
main {
  width: 100%;
  height: 100%;
}

a {
  color: var(--main-color);
}

.header {
  max-height: 3em;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
