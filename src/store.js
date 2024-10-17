import { writable } from "svelte/store";

export const mine = writable(true);

const storedPage = sessionStorage.getItem("page");
export const currentPage = writable(storedPage);
currentPage.subscribe(value => sessionStorage.setItem("page", value));


const storedApiPage = sessionStorage.getItem("apiPageSelected")
export const ipApiSelectedPage = writable(storedApiPage);
ipApiSelectedPage.subscribe(value => sessionStorage.setItem("apiPageSelected", value))

const storedIPData = sessionStorage.getItem("ipData")
export const currentIPData = writable(storedIPData);
currentIPData.subscribe(value => sessionStorage.setItem("ipData", value))