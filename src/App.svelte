<script>
import { fade } from "svelte/transition";

</script>
<main>
  <div class="header" in:fade={{ delay: 250, duration: 300 }}>
    <span>
        <a class="hover" href="https://github.com/michaelMondoro" target="_blank"><i class="fa fa-github hover icon"></i></a>
        <a class="hover" href="https://www.linkedin.com/in/michael-mondoro-8b7423151/" target="_blank"><i class="fa fa-linkedin hover icon"></i></a>
    </span>
    <span></span>
  </div>
  <div class="container">
    <h2>nothing here <emoji>&#128640;</emoji></h2>
    
  </div>
</main>

  
<style>
main {
  width: 100%;
  height: 100%;
}

a {
  color: var(--main-color);
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.hover:hover {
  color: rgb(82, 154, 254);
}

.icon {
  font-size: 25px;
  padding: .5em .5em;
}

.header {
  max-height: 3em;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
