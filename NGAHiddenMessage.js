// ==UserScript==
// @name         NGA hidden message auto open
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  simple but useful
// @author       GitHub: isaacveg
// @match        *://*.nga.cn/*
// @grant        none
// ==/UserScript==

var pageURLCheckTimer = setInterval (
    function () {
        if (    this.lastPathStr  !== location.pathname
            ||  this.lastQueryStr !== location.search
            ||  this.lastPathStr   === null
            ||  this.lastQueryStr  === null
           ) {
            this.lastPathStr  = location.pathname;
            this.lastQueryStr = location.search;
            gmMain ();
        }
    }
    , 1000
);

function gmMain () {
    var x = document.getElementsByName("lessernukeblk");
    for(var i=0;i<x.length;i++)
    {x[i].style.display = ""}
}

