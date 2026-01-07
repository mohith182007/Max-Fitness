// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Toggle mobile menu
    hamburger.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        hamburger.classList.toggle('active');
    });

    // Close menu when link is clicked
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        const isClickInsideMenu = navMenu.contains(event.target);
        const isClickOnHamburger = hamburger.contains(event.target);

        if (!isClickInsideMenu && !isClickOnHamburger && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            hamburger.classList.remove('active');
        }
    });

    // Plan Type Selector
    const planTypeButtons = document.querySelectorAll('.plan-type-btn');
    planTypeButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const planType = this.getAttribute('data-plan');
            
            // Remove active class from all buttons
            planTypeButtons.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            // Hide all plan grids
            document.querySelectorAll('.membership-grid').forEach(grid => {
                grid.style.display = 'none';
            });
            
            // Show selected plan grid
            document.getElementById(planType).style.display = 'grid';
        });
    });

    // Scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.8s ease-out forwards';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe facility and location cards
    const cards = document.querySelectorAll('.facility-card, .location-card, .testimonial-card, .membership-card');
    cards.forEach(card => {
        card.style.opacity = '0';
        observer.observe(card);
    });

    // Initialize EmailJS
    (function() {
        emailjs.init("94SJeKZrQ9ahy-X0p"); // Replace with your EmailJS user ID
    })();

    // Form submission with EmailJS
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const name = contactForm.querySelector('input[name="from_name"]').value;
            const email = contactForm.querySelector('input[name="from_email"]').value;
            const message = contactForm.querySelector('textarea[name="message"]').value;
            
            // Simple validation
            if (name && email && message) {
                // Show loading state
                const submitBtn = contactForm.querySelector('.submit-btn');
                const originalText = submitBtn.textContent;
                submitBtn.textContent = 'Sending...';
                submitBtn.disabled = true;

                // Send email using EmailJS
                const templateParams = {
                    from_name: name,
                    from_email: email,
                    message: message,
                    to_email: 'maxxfitnesswebsite@gmail.com',
                    reply_to: email
                };

                emailjs.send('service_jnvacog', 'template_a6lnazj', templateParams)
                    .then(function(response) {
                        console.log('Email sent successfully:', response);
                        alert('Thank you for your message! We will get back to you soon.');
                        contactForm.reset();
                    }, function(error) {
                        console.log('Failed to send email:', error);
                        // Fallback to mailto link
                        const subject = encodeURIComponent(`Contact from ${name} - Maxx Fitness Website`);
                        const body = encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`);
                        const mailtoLink = `mailto:maxxfitnesswebsite@gmail.com?subject=${subject}&body=${body}`;
                        window.open(mailtoLink);
                        alert('Opening your email client to send the message. Please send the pre-filled email.');
                    })
                    .finally(function() {
                        // Reset button state
                        submitBtn.textContent = originalText;
                        submitBtn.disabled = false;
                    });
            } else {
                alert('Please fill in all fields.');
            }
        });
    }

    // View Map buttons - Modal functionality
    const viewMapBtns = document.querySelectorAll('.view-btn');
    viewMapBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const locationCard = this.closest('.location-card');
            const locationName = locationCard.querySelector('h3').textContent;
            alert(`Opening map for ${locationName}.\n\nIn a real application, this would open a map embed or external map service.`);
        });
    });

    // Join Now buttons
    const joinBtns = document.querySelectorAll('.join-btn');
    joinBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const membershipName = this.closest('.membership-card').querySelector('h3').textContent;
            alert(`You selected the ${membershipName} plan.\n\nRedirecting to membership registration...`);
        });
    });

    // CTA Button
    const ctaBtn = document.querySelector('.cta-btn');
    if (ctaBtn) {
        ctaBtn.addEventListener('click', function() {
            document.querySelector('#contact').scrollIntoView({ behavior: 'smooth' });
        });
    }

    // Newsletter subscription
    const footerButton = document.querySelector('.footer-section:last-child button');
    if (footerButton) {
        footerButton.addEventListener('click', function(e) {
            e.preventDefault();
            const input = this.previousElementSibling;
            if (input.value) {
                alert('Thank you for subscribing to our newsletter!');
                input.value = '';
            } else {
                alert('Please enter your email address.');
            }
        });
    }

    // Add animation class on page load
    window.addEventListener('load', function() {
        document.body.style.opacity = '1';
    });

    // Navbar color change on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 5px 20px rgba(230, 57, 70, 0.3)';
        } else {
            navbar.style.boxShadow = '0 2px 10px rgba(230, 57, 70, 0.2)';
        }
    });

    // Smooth number counting in stats
    const stats = document.querySelectorAll('.stat h3');
    let hasAnimated = false;

    window.addEventListener('scroll', function() {
        if (!hasAnimated && window.scrollY > 1000) {
            stats.forEach(stat => {
                animateValue(stat);
            });
            hasAnimated = true;
        }
    });

    function animateValue(element) {
        const text = element.textContent;
        const number = parseInt(text);
        const suffix = text.replace(/[0-9]/g, '');
        const duration = 2000;
        const steps = 60;
        const stepValue = number / steps;
        let currentValue = 0;
        let currentStep = 0;

        const interval = setInterval(() => {
            currentStep++;
            currentValue = Math.floor(stepValue * currentStep);
            element.textContent = currentValue + suffix;

            if (currentStep === steps) {
                element.textContent = text;
                clearInterval(interval);
            }
        }, duration / steps);
    }
});

// Add loading animation
window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});
