// ============================================
// SGD Events - Main JavaScript
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // Mobile Menu Toggle
    // ============================================
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            const icon = this.querySelector('i');
            
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }
    
    // ============================================
    // Smooth Scrolling for Anchor Links
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Only prevent default for actual anchor links (not just #)
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                
                const target = document.querySelector(href);
                if (target) {
                    const navHeight = document.querySelector('.navbar').offsetHeight;
                    const targetPosition = target.offsetTop - navHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu if open
                    if (navLinks.classList.contains('active')) {
                        navLinks.classList.remove('active');
                        mobileMenuToggle.querySelector('i').classList.remove('fa-times');
                        mobileMenuToggle.querySelector('i').classList.add('fa-bars');
                    }
                }
            }
        });
    });
    
    // ============================================
    // Location Selection
    // ============================================
    const locationItems = document.querySelectorAll('.location-item');
    
    locationItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const location = this.getAttribute('data-location');
            
            // Store selected location in localStorage
            localStorage.setItem('selectedLocation', location);
            
            // Update UI to show selected location
            const locationToggle = document.querySelector('.dropdown-toggle');
            if (locationToggle && locationToggle.textContent.includes('Location')) {
                locationToggle.innerHTML = `
                    <i class="fas fa-map-marker-alt"></i> ${location}
                    <i class="fas fa-chevron-down"></i>
                `;
            }
            
            // Show notification
            showNotification(`Location changed to ${location}`);
        });
    });        


    // Restore selected location on page load
    const savedLocation = localStorage.getItem('selectedLocation');
    if (savedLocation) {
        const locationToggle = document.querySelector('.dropdown-toggle');
        if (locationToggle && locationToggle.textContent.includes('Location')) {
            locationToggle.innerHTML = `
                <i class="fas fa-map-marker-alt"></i> ${savedLocation}
                <i class="fas fa-chevron-down"></i>
            `;
        }
    }
    
    // ============================================
    // Event Selection
    const eventItems = document.querySelectorAll('.event-item');
    
    eventItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const event = this.getAttribute('data-event');

            // Store selected event in localStorage
            localStorage.setItem('selectedEvent', event);

            // Update UI to show selected event
            const eventToggle = document.querySelector('.dropdown-toggle');
            if (eventToggle && eventToggle.textContent.includes('Event')) {
                eventToggle.innerHTML = `   
                    <i class="fas fa-star"></i> ${event}
                    <i class="fas fa-chevron-down"></i>
                `;
            }
            // Show notification
            showNotification(`Event changed to ${event}`);
        });
    });
    
    // ============================================
    // Package Card Interactions
    // ============================================
    const packageCards = document.querySelectorAll('.package-card');
    
    packageCards.forEach(card => {
        const learnMoreBtn = card.querySelector('.btn-outline');
        const bookNowBtn = card.querySelector('.btn-primary');
        
        if (learnMoreBtn) {
            learnMoreBtn.addEventListener('click', function() {
                const packageName = card.querySelector('.package-name').textContent;
                showNotification(`More details about ${packageName} coming soon!`);
            });
        }
        
        if (bookNowBtn) {
            bookNowBtn.addEventListener('click', function() {
                const packageName = card.querySelector('.package-name').textContent;
                showNotification(`Booking for ${packageName} - Contact us to proceed!`);
            });
        }
    });
    
    // ============================================
    // Category Card Interactions
    // ============================================
    const categoryCards = document.querySelectorAll('.category-card');
    
    categoryCards.forEach(card => {
        card.addEventListener('click', function() {
            const categoryName = this.querySelector('.category-name').textContent;
            showNotification(`${categoryName} category - Coming soon!`);
        });
    });
    
    // ============================================
    // Navbar Background on Scroll
    // ============================================
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.2)';
        } else {
            navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        }
    });
    
    // ============================================
    // Notification System
    // ============================================
    function showNotification(message) {
        // Remove existing notifications
        const existingNotification = document.querySelector('.notification');
        if (existingNotification) {
            existingNotification.remove();
        }
        
        // Create notification element
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.innerHTML = `
            <i class="fas fa-check-circle"></i>
            <span>${message}</span>
        `;
        
        // Add styles
        notification.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            background: linear-gradient(135deg, #d4af37, #b8941f);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
            z-index: 10000;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-weight: 600;
            animation: slideInRight 0.3s ease;
        `;
        
        document.body.appendChild(notification);
        
        // Remove after 3 seconds
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 3000);
    }
    
    // ============================================
    // Add CSS Animations for Notifications
    // ============================================
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from {
                transform: translateX(400px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(400px);
                opacity: 0;
            }
        }
        
        @media (max-width: 968px) {
            .nav-links.active {
                display: flex;
                flex-direction: column;
                position: absolute;
                top: 100%;
                left: 0;
                right: 0;
                background: linear-gradient(135deg, #2c1810 0%, #8b4513 100%);
                padding: 1rem;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
                gap: 0.5rem;
            }
            
            .nav-links.active .dropdown-menu {
                position: static;
                opacity: 1;
                visibility: visible;
                transform: translateY(0);
                margin-top: 0.5rem;
            }
        }
    `;
    document.head.appendChild(style);
    
    // ============================================
    // Image Lazy Loading
    // ============================================
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // ============================================
    // Scroll to Top Button (Optional Enhancement)
    // ============================================
    const scrollToTopBtn = document.createElement('button');
    scrollToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollToTopBtn.className = 'scroll-to-top';
    scrollToTopBtn.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #d4af37, #b8941f);
        color: white;
        border: none;
        cursor: pointer;
        display: none;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        z-index: 1000;
        transition: all 0.3s ease;
    `;
    
    document.body.appendChild(scrollToTopBtn);
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 500) {
            scrollToTopBtn.style.display = 'flex';
        } else {
            scrollToTopBtn.style.display = 'none';
        }
    });
    
    scrollToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    scrollToTopBtn.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.1)';
    });
    
    scrollToTopBtn.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
    });
    
    // ============================================
    // Form Validation & Enhancement
    // ============================================
    const contactForm = document.querySelector('.contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const name = document.querySelector('#id_name');
            const email = document.querySelector('#id_email');
            const phone = document.querySelector('#id_phone');
            
            // Basic validation
            if (name && name.value.trim() === '') {
                e.preventDefault();
                alert('Please enter your name');
                name.focus();
                return false;
            }
            
            if (email && email.value.trim() === '') {
                e.preventDefault();
                alert('Please enter your email');
                email.focus();
                return false;
            }
            
            if (phone && phone.value.trim() === '') {
                e.preventDefault();
                alert('Please enter your phone number');
                phone.focus();
                return false;
            }
            
            // Show loading state
            const submitBtn = this.querySelector('.btn-submit');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';
                submitBtn.disabled = true;
            }
        });
        
        // Auto-scroll to form if there are errors
        const alerts = document.querySelectorAll('.alert');
        if (alerts.length > 0) {
            const contactSection = document.querySelector('#contact');
            if (contactSection) {
                contactSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }
    
    // ============================================
    // Console Welcome Message
    // ============================================
    console.log('%c Welcome to SGD Events! ', 'background: #d4af37; color: #2c1810; font-size: 20px; font-weight: bold; padding: 10px;');
    console.log('%c Sree Gurudatta Events - Making your special moments unforgettable ', 'color: #8b4513; font-size: 14px;');
});
