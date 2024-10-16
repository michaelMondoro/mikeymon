import { writable } from "svelte/store";

const storedPage = localStorage.getItem("page");
export const currentPage = writable(storedPage);
currentPage.subscribe(value => localStorage.setItem("page", value));


const storedApiPage = localStorage.getItem("apiPageSelected")
export const ipApiSelectedPage = writable(storedApiPage);
ipApiSelectedPage.subscribe(value => localStorage.setItem("apiPageSelected", value))

const storedIPData = localStorage.getItem("ipData")
export const currentIPData = writable(storedIPData);
currentIPData.subscribe(value => localStorage.setItem("ipData", value))