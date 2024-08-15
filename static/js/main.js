document.querySelectorAll('pre').forEach((tag) => {
    tag.classList.add('prettyprint');
})

document.querySelectorAll('code').forEach((tag) => {
    tag.classList.add('prettyprint');
})


let emoji = document.querySelector('emoji');
emoji.addEventListener('mouseover', (e) => {
    e.target.innerHTML = "&#129327;";
})
emoji.addEventListener('mouseout', (e) => {
    e.target.innerHTML = "&#129323;";
})