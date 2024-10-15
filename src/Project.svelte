<script>
    export let title;
    export let desc;
    export let packageName;
    export let version;
    export let defaultLink=undefined;
    export let defaultImgLink=undefined;
    

    let projectLink=`https://github.com/michaelMondoro/${packageName}`
    let projectImgLink=`https://img.shields.io/badge/${packageName}-${version ? version : 'git'}-orange.svg`
    let packageLink=`https://pypi.org/project/${packageName}`
    let packageImgLink=`https://img.shields.io/badge/pypi- -blue.svg`
    let statsLink=`https://pypistats.org/packages/${packageName}`
    let statsImgLink=`https://img.shields.io/pypi/dm/${packageName}`

</script>

<div class="project">
    <h3>{title}</h3>
    <p>{desc}</p>
    <a href="{projectLink}" target="_blank">
        <img alt="{packageName}" src="{projectImgLink}">
    </a>
    {#if defaultLink}
    <a href="{defaultLink}" target="_blank">
        <img alt="{packageName}" src="{defaultImgLink}">
    </a> 
    {/if}
    <!-- for Python projects -->
    {#if version} 
    <a href="{statsLink}" target="_blank">
        <img alt="{packageName}" src="{statsImgLink}">
    </a>
    <a href="{packageLink}" target="_blank">
        <img alt="{packageName}" src="{packageImgLink}">
    </a>
    {/if}
</div>

<style>
.project {
    padding: 1em;
    max-width: 30em;
}

h3 {
    margin: 0em 0em;
}
p {
    margin: .5em 0em;
    color: var(--secondary-color);
    word-break: break-word;
}
</style>