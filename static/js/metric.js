
var metricModal = document.querySelector(".add-metric-modal")
var metricOpen = document.getElementById("addMetric")
var metricClose = document.getElementById("close");


    metricOpen.onclick = function(){
      // e.preventDefault();
        metricModal.style.display = "block";
        
    } 

    metricClose.onclick = function(){
      e.preventDefault();
        metricModal.style.display = "none";
        
    }

    // window.onclick = function(event) {
    //     if (event.target == metricModal) {
    //       metricModal.style.display = "none";
    //     }
    //   }
