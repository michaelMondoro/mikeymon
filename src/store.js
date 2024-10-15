import { writable } from "svelte/store";

const storedPage = localStorage.getItem("page");
export const currentPage = writable(storedPage);
currentPage.subscribe(value => {
    localStorage.setItem("page", value);
});