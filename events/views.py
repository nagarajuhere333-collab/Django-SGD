from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def home(request):
    """Homepage view with packages and categories"""
    
    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you can save to database or send email
            # For now, just show a success message
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            form = ContactForm()  # Reset form
    else:
        form = ContactForm()
    
    # Sample packages data (will come from database later)
    packages = [
        {
            'name': 'Silver Package',
            'price': '₹50,000',
            'features': [
                'Basic Venue Decoration',
                'Photography (4 hours)',
                'Basic Catering for 50 guests',
                'Mehandi Artist',
            ],
            'is_popular': False
        },
        {
            'name': 'Gold Package',
            'price': '₹1,50,000',
            'features': [
                'Premium Venue Decoration',
                'Photography & Videography (8 hours)',
                'Full Catering for 100 guests',
                'Makeup Artist & Mehandi',
                'DJ & Music',
            ],
            'is_popular': True
        },
        {
            'name': 'Platinum Package',
            'price': '₹3,00,000',
            'features': [
                'Luxury Venue Decoration',
                'Premium Photography & Videography (Full Day)',
                'Catering for 200 guests',
                'Makeup, Mehandi & Jewellary',
                'Live Band & DJ',
                'Pre-Wedding Shoot',
            ],
            'is_popular': False
        },
    ]
    
    # Categories data
    categories = [
        {'name': 'Venue', 'icon': 'fa-building', 'description': 'Beautiful venues for your special day'},
        {'name': 'Makeup', 'icon': 'fa-paint-brush', 'description': 'Professional makeup artists'},
        {'name': 'Photographers', 'icon': 'fa-camera', 'description': 'Capture your precious moments'},
        {'name': 'Mehandi', 'icon': 'fa-hand-sparkles', 'description': 'Traditional mehandi designs'},
        {'name': 'Virtual Planning', 'icon': 'fa-video', 'description': 'Plan your event online'},
        {'name': 'Jewellary', 'icon': 'fa-gem', 'description': 'Exquisite jewelry collection'},
        {'name': 'Food', 'icon': 'fa-utensils', 'description': 'Delicious catering services'},
        {'name': 'Pre Wedding Shoot', 'icon': 'fa-heart', 'description': 'Memorable pre-wedding photography'},
        {'name': 'Pandit', 'icon': 'fa-om', 'description': 'Traditional ceremony services'},
    ]
    
    # Locations for dropdown
    locations = [
        'Bangalore',
        'Mumbai',
        'Delhi',
        'Chennai',
        'Hyderabad',
        'Pune',
        'Kolkata',
    ]
    
    context = {
        'packages': packages,
        'categories': categories,
        'locations': locations,
        'form': form,
    }
    
    return render(request, 'events/home.html', context)


def about(request):
    """About Us page view"""
    return render(request, 'events/about.html')
