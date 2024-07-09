// JavaScript
        document.addEventListener("DOMContentLoaded", function() {
            const navLinks = document.querySelectorAll("nav a");
            const sections = document.querySelectorAll("main section");

            function showSection(id) {
                sections.forEach(section => {
                    if (section.id === id) {
                        section.style.display = 'block';
                    } else {
                        section.style.display = 'none';
                    }
                });
            }

            navLinks.forEach(link => {
                link.addEventListener("click", function(event) {
                    event.preventDefault();
                    const targetId = this.getAttribute("href").substring(1);
                    showSection(targetId);
                });
            });

            // Initially show the home section and hide others
            showSection('home');

            // Modal handling
            const modal = document.getElementById('bookingModal');
            const closeModal = modal.querySelector('.close');
            const bookButtons = document.querySelectorAll('.book-now');
            const carNameInput = document.getElementById('carName');

            // Handle "Book Now" button click
            bookButtons.forEach(button => {
                button.addEventListener("click", function() {
                    const carName = this.getAttribute("data-car");
                    carNameInput.value = carName;
                    modal.style.display = "flex";
                });
            });

            // Handle close modal
            closeModal.addEventListener("click", function() {
                modal.style.display = "none";
            });

            // Close modal if user clicks outside the modal content
            window.addEventListener("click", function(event) {
                if (event.target === modal) {
                    modal.style.display = "none";
                }
            });

            // Submit form handling
            const bookingForm = document.getElementById("bookingForm");
            bookingForm.addEventListener("submit", function(event) {
                event.preventDefault();
                // Handle form submission here, e.g., send data to server
                console.log("Form submitted!");
                // Optionally, close the modal after submission
                modal.style.display = "none";
            });
        });
