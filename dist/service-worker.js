if(!self.define){let e,i={};const s=(s,r)=>(s=new URL(s+".js",r).href,i[s]||new Promise((i=>{if("document"in self){const e=document.createElement("script");e.src=s,e.onload=i,document.head.appendChild(e)}else e=s,importScripts(s),i()})).then((()=>{let e=i[s];if(!e)throw new Error(`Module ${s} didn’t register its module`);return e})));self.define=(r,n)=>{const l=e||("document"in self?document.currentScript.src:"")||location.href;if(i[l])return;let o={};const u=e=>s(e,l),t={module:{uri:l},exports:o,require:u};i[l]=Promise.all(r.map((e=>t[e]||u(e)))).then((e=>(n(...e),o)))}}define(["./workbox-db5fc017"],(function(e){"use strict";e.setCacheNameDetails({prefix:"child-support"}),self.addEventListener("message",(e=>{e.data&&"SKIP_WAITING"===e.data.type&&self.skipWaiting()})),e.precacheAndRoute([{url:"/css/app.c8aa742e.css",revision:null},{url:"/img/1.e2c0d40f.jpg",revision:null},{url:"/img/2.1268057f.jpg",revision:null},{url:"/img/3.17b2bd5f.jpg",revision:null},{url:"/img/logo.dd8822ea.png",revision:null},{url:"/index.html",revision:"373aedb630e808490186787700651216"},{url:"/js/app.635cee6a.js",revision:null},{url:"/js/chunk-vendors.dd6a0aa8.js",revision:null},{url:"/manifest.json",revision:"45bca75a72d9a94e9159f743789c4551"},{url:"/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"}],{})}));
//# sourceMappingURL=service-worker.js.map