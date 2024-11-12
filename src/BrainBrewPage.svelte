<script>
    import { fade } from "svelte/transition";

</script>

<main class="container" in:fade={{ duration: 1000 }}>
    <div class="heading">
        <h3>BrainBrew <emoji>&#x2615;</emoji></h3>
        <span class="subheading"><u>keeping research simple</u></span>
    </div>
    <div class="container">
        <p>The world is constantly evolving with new techology that is transforming our lives on a daily basis. 
            Wouldn't it be nice to be able to keep up with these changes without having to read stacks of research papers? 
            That is exactly BrainBrew seeks to do. Updated daily with the latest published research across a variety of domains, BrainBrew distills each paper into a short, easily digestible post. 
            Users can browse by tags, or search for specific topics.</p>
        <button class="submit"><a target="_blank" href="https://brainbrew.netlify.app">Check It Out!</a></button>
        <hr>
        <img src="https://github.com/user-attachments/assets/4ad6bca1-3036-4a42-9dea-a17db7e968d0">
    </div>
</main>

<style>
hr {
    border: solid rgb(55, 55, 55) 1px;
    width: 50%;   
    margin: 1em 0em;
}
a {
    all: unset;
}
img {
    box-shadow: rgb(55, 55, 55) 1px 2px 10px;
    width: 70%;
    border-radius: 1em;
    border: solid rgb(55, 55, 55) 1px;
}
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
p {
    width: 70%;
    margin: .5em 0em;
    color: var(--secondary-color);
    word-break: break-word;
}
.horizontal-flex {
    display: flex;
    margin-bottom: 1em;
}
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.heading {
    text-align: center;
    margin-bottom: 1em;
}
.subheading {
  color: var(--secondary-color);

}
</style>