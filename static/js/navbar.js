//responsive sidenav
var openMenu = document.querySelector(".menu");

openMenu.addEventListener("click", function(){
    document.querySelector(".sidebar").style.display = "inline";
})
var closeMenu = document.querySelector(".fa-times");
closeMenu.addEventListener("click", function(){
    document.querySelector(".sidebar").style.display = "none";
})


//active nav
var currentLocation = location.href;

var sidebarContainer = document.getElementById("navItems");                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

var navItems = sidebarContainer.getElementsByClassName("nav");

var navLength = navItems.length;

for(let i = 0; i< navLength; i++ ){
  if(navItems[i].href === currentLocation){
    navItems[i].className += " active"
  }
}
// navItems[i].addEventListener("click", function(){
        

// })