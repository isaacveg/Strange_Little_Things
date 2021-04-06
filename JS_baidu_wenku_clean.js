// ==UserScript==
// @name         百度文库优化
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  百度文库优化
// @author       isaacveg
// @match        *://wenku.baidu.com/view/*.html
// @grant        none
// ==/UserScript==


function main(){
    var ReadAll = document.getElementsByClassName("read-all");
    if (ReadAll.length) {
        ReadAll[0].click();
    }

    var LO = document.getElementsByClassName("link-open");
    if (LO.length) {
        LO[0].click();
    }

    var ReadEnd = document.getElementsByClassName("try-end-fold-page");
    if (ReadEnd.length) {
        ReadEnd[0].style = "display:none";
    }

    var DocBtnW = document.getElementsByClassName("doc-btns-wrap");
    DocBtnW[0].style = "display:none";

    var DocInfo = document.getElementsByClassName("doc-info-right");
    DocInfo[0].style = "display:none";

    var CP = document.getElementById("color-plate");
    CP.style = "display:none";

    var PTB = document.getElementsByClassName("pure-tool-btn");
    PTB[0].style = "display:none";

    var VipCard = document.getElementsByClassName("vip-card-wrap");
    VipCard[0].style = "display:none";

    var BottomReadToolBar = document.getElementsByClassName("tool-bar-wrapper");
    BottomReadToolBar[0].style = "display:none";

    var NoCourse = document.getElementsByClassName("lazy-load");
    for(var x = 0; x<NoCourse.length;x=x+1){
        NoCourse[x].style = "display:none";
    }


    var SearchBar = document.getElementsByClassName("search-tab-content");
    SearchBar[0].style = "display:none";

    var RightBox = document.getElementsByClassName("right-box");
    RightBox[0].style = "display:none";

    var Bad = document.getElementsByClassName("ex-wrapper no-full-screen");
    Bad[0].style = "display:none";

    var BadC = document.getElementsByClassName("comment-wrapper");
    BadC[0].style = "display:none";
}

setTimeout(main,1500);
