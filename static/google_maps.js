
$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initMap)

})


function initMap() {
    console.log("Initializing Map");
    var map = new google.maps.Map(document.getElementById('map-route'), {
        zoom: 7,
    });
    console.log("Map is ready");
}