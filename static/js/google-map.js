
function init() {
    // Check if Google Maps API is loaded
    if (typeof google === 'undefined' || !google.maps) {
        console.error('Google Maps API not loaded. Please check your API key.');
        var mapElement = document.getElementById('map');
        if (mapElement) {
            mapElement.innerHTML = '<p style="padding: 20px; text-align: center; color: #666;">Map could not be loaded. Please try again later.</p>';
        }
        return;
    }

    try {
        // Basic options for a simple Google Map
        // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
        var myLatlng = new google.maps.LatLng(40.69847032728747, -73.9514422416687);

        var mapOptions = {
            // How zoomed in you want the map to start at (always required)
            zoom: 7,

            // The latitude and longitude to center the map (always required)
            center: myLatlng,

            // How you would like to style the map.
            scrollwheel: false,
            styles: [
                {
                    "featureType": "administrative.country",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "visibility": "simplified"
                        },
                        {
                            "hue": "#ff0000"
                        }
                    ]
                }
            ]
        };

        // Get the HTML DOM element that will contain your map
        var mapElement = document.getElementById('map');

        if (!mapElement) {
            console.error('Map element not found.');
            return;
        }

        // Create the Google Map using our element and options defined above
        var map = new google.maps.Map(mapElement, mapOptions);

        // Note: Geocoding without API key is deprecated. For production, use Places API or Geocoding API with key.
        // This is a placeholder for demonstration.
        var addresses = ['New York'];

        for (var x = 0; x < addresses.length; x++) {
            // Using HTTPS for geocoding (though still deprecated without key)
            $.getJSON('https://maps.googleapis.com/maps/api/geocode/json?address=' + encodeURIComponent(addresses[x]) + '&sensor=false', null, function (data) {
                if (data.results && data.results[0]) {
                    var p = data.results[0].geometry.location;
                    var latlng = new google.maps.LatLng(p.lat, p.lng);
                    new google.maps.Marker({
                        position: latlng,
                        map: map,
                        icon: 'images/loc.png'
                    });
                }
            }).fail(function() {
                console.warn('Geocoding failed for address: ' + addresses[x]);
            });
        }

    } catch (error) {
        console.error('Error initializing Google Map:', error);
        var mapElement = document.getElementById('map');
        if (mapElement) {
            mapElement.innerHTML = '<p style="padding: 20px; text-align: center; color: #666;">Map could not be loaded due to an error. Please try again later.</p>';
        }
    }
}

// Initialize map when window loads, but only if Google Maps is available
if (typeof google !== 'undefined' && google.maps && google.maps.event) {
    google.maps.event.addDomListener(window, 'load', init);
} else {
    // Fallback if Google Maps API loads after this script
    window.addEventListener('load', function() {
        if (typeof google !== 'undefined' && google.maps) {
            google.maps.event.addDomListener(window, 'load', init);
        } else {
            init(); // Try anyway, error handling will catch it
        }
    });
}
