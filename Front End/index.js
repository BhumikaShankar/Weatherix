// index.js

// JavaScript for slideshow functionality
document.addEventListener('DOMContentLoaded', function() {

    let slideIndex = 0;
    showSlides();

    function showSlides() {
        let i;
        let slides = document.getElementsByClassName("mySlides");
        let dots = document.getElementsByClassName("dot");
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slideIndex++;
        if (slideIndex > slides.length) { slideIndex = 1; }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].className += " active";
        setTimeout(showSlides, 2000); // Change slide every 2 seconds
    }

    // Event listener for the Predict Temperature button
    document.getElementById('predictButton').addEventListener('click', function() {
        console.log('Button clicked');  // Add this line
        // Call the Flask API to get predicted temperature
        fetch('http://localhost:5000/get_predicted_temperature')
            .then(response => response.json())
            .then(data => {
                console.log('Response:', data);  // Add this line
                // Display the predicted temperature
                const predictedTemperatureElement = document.getElementById('predictedTemperature');
                if (predictedTemperatureElement) {
                    predictedTemperatureElement.innerText = `Predicted Temperature: ${data.predicted_temperature} °C`;
                }
            })
            .catch(error => console.error('Error:', error));
    });    
});
