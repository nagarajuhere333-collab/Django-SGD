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
    
    # Categories data with subcategories
    categories = [
        {
            'name': 'Venues',
            'icon': 'fa-building',
            'description': 'Beautiful venues for your special day',
            'image': 'https://images.unsplash.com/photo-1519167758481-83f29da8c776?w=800',
            'subcategories': [
                'Banquet Halls',
                'Marriage Gardens',
                'Wedding Resorts',
                'Kalyana Mandapams',
                'Wedding Hotels'
            ]
        },
        {
            'name': 'Photographers',
            'icon': 'fa-camera',
            'description': 'Capture your precious moments',
            'image': 'https://images.unsplash.com/photo-1606216794074-735e91aa2c92?w=800',
            'subcategories': [
                'Wedding Photography',
                'Candid Shoots',
                'Pre-Wedding',
                'Cinematography'
            ]
        },
        {
            'name': 'Makeup',
            'icon': 'fa-paint-brush',
            'description': 'Professional makeup artists',
            'image': 'https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?w=800',
            'subcategories': [
                'Bridal Makeup',
                'Family Makeup',
                'Hair Styling',
                'Mehandi Artists'
            ]
        },
        {
            'name': 'Planning & Decor',
            'icon': 'fa-palette',
            'description': 'Complete event planning services',
            'image': 'https://images.unsplash.com/photo-1511795409834-ef04bbd61622?w=800',
            'subcategories': [
                'Wedding Planners',
                'Decorators',
                'Florists',
                'Stage Design'
            ]
        },
        {
            'name': 'Catering',
            'icon': 'fa-utensils',
            'description': 'Delicious catering services',
            'image': 'https://images.unsplash.com/photo-1583939003579-730e3918a45a?w=800',
            'subcategories': [
                'Wedding Caterers',
                'Cake Makers',
                'Bar Services'
            ]
        },
        {
            'name': 'Entertainment',
            'icon': 'fa-music',
            'description': 'Music and entertainment',
            'image': 'https://images.unsplash.com/photo-1511578314322-379afb476865?w=800',
            'subcategories': [
                'DJ Services',
                'Music Bands',
                'Dancers',
                'Anchors'
            ]
        },
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
