from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import ContactForm
from .models import VenueItem, JewelleryItem, FoodItem, Favorite


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

    events = [
        'Wedding',
        'Engagement',
        'Birthday',
        'Corporate Event',
        'Anniversary',
        'Baby Shower',        
    ]
    
    context = {
        'packages': packages,
        'categories': categories,
        'locations': locations,
        'form': form,
        'events': events,
    }
    
    return render(request, 'events/home.html', context)


def venue_list(request):
    """Display all venues grouped by subcategory"""
    venues = VenueItem.objects.all()
    
    # Group by subcategory
    subcategories = {}
    for choice_value, choice_label in VenueItem.SUBCATEGORY_CHOICES:
        items = venues.filter(subcategory=choice_value)
        if items.exists():
            subcategories[choice_label] = items
    
    context = {
        'subcategories': subcategories,
        'category_name': 'Venues',
        'events': ['Wedding', 'Birthday', 'Corporate Event', 'Anniversary', 'Engagement'],
        'locations': ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Hyderabad'],
    }
    return render(request, 'events/venue_list.html', context)


def venue_detail(request, slug):
    """Display detailed view of a single venue"""
    venue = get_object_or_404(VenueItem, slug=slug)
    
    # Check if favorited (if user is logged in)
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(
            user=request.user,
            item_type='venue',
            item_id=venue.id
        ).exists()
    
    context = {
        'item': venue,
        'item_type': 'venue',
        'is_favorited': is_favorited,
        'events': ['Wedding', 'Birthday', 'Corporate Event', 'Anniversary', 'Engagement'],
        'locations': ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Hyderabad'],
    }
    return render(request, 'events/venue_detail.html', context)


def jewellery_list(request):
    """Display all jewellery items grouped by subcategory"""
    items = JewelleryItem.objects.all()
    
    # Group by subcategory
    subcategories = {}
    for choice_value, choice_label in JewelleryItem.SUBCATEGORY_CHOICES:
        category_items = items.filter(subcategory=choice_value)
        if category_items.exists():
            subcategories[choice_label] = category_items
    
    context = {
        'subcategories': subcategories,
        'category_name': 'Jewellery',
        'events': ['Wedding', 'Birthday', 'Corporate Event', 'Anniversary', 'Engagement'],
        'locations': ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Hyderabad'],
    }
    return render(request, 'events/jewellery_list.html', context)


def jewellery_detail(request, slug):
    """Display detailed view of a single jewellery item"""
    item = get_object_or_404(JewelleryItem, slug=slug)
    
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(
            user=request.user,
            item_type='jewellery',
            item_id=item.id
        ).exists()
    
    context = {
        'item': item,
        'item_type': 'jewellery',
        'is_favorited': is_favorited,
        'events': ['Wedding', 'Birthday', 'Corporate Event', 'Anniversary', 'Engagement'],
        'locations': ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Hyderabad'],
    }
    return render(request, 'events/jewellery_detail.html', context)


def food_list(request):
    """Display all food items grouped by subcategory"""
    items = FoodItem.objects.all()
    
    # Group by subcategory
    subcategories = {}
    for choice_value, choice_label in FoodItem.SUBCATEGORY_CHOICES:
        category_items = items.filter(subcategory=choice_value)
        if category_items.exists():
            subcategories[choice_label] = category_items
    
    context = {
        'subcategories': subcategories,
        'category_name': 'Food & Catering',
        'events': ['Wedding', 'Birthday', 'Corporate Event', 'Anniversary', 'Engagement'],
        'locations': ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Hyderabad'],
    }
    return render(request, 'events/food_list.html', context)


def food_detail(request, slug):
    """Display detailed view of a single food item"""
    item = get_object_or_404(FoodItem, slug=slug)
    
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(
            user=request.user,
            item_type='food',
            item_id=item.id
        ).exists()
    
    context = {
        'item': item,
        'item_type': 'food',
        'is_favorited': is_favorited,
        'events': ['Wedding', 'Birthday', 'Corporate Event', 'Anniversary', 'Engagement'],
        'locations': ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Hyderabad'],
    }
    return render(request, 'events/food_detail.html', context)


@login_required
def favorites(request):
    """Display user's favorite items"""
    user_favorites = Favorite.objects.filter(user=request.user)
    
    # Get actual items
    favorited_items = {
        'venues': [],
        'jewellery': [],
        'food': []
    }
    
    for fav in user_favorites:
        if fav.item_type == 'venue':
            try:
                item = VenueItem.objects.get(id=fav.item_id)
                favorited_items['venues'].append(item)
            except VenueItem.DoesNotExist:
                pass
        elif fav.item_type == 'jewellery':
            try:
                item = JewelleryItem.objects.get(id=fav.item_id)
                favorited_items['jewellery'].append(item)
            except JewelleryItem.DoesNotExist:
                pass
        elif fav.item_type == 'food':
            try:
                item = FoodItem.objects.get(id=fav.item_id)
                favorited_items['food'].append(item)
            except FoodItem.DoesNotExist:
                pass
    
    context = {
        'favorited_items': favorited_items,
        'events': ['Wedding', 'Birthday', 'Corporate Event', 'Anniversary', 'Engagement'],
        'locations': ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Hyderabad'],
    }
    return render(request, 'events/favorites.html', context)


@login_required
@require_POST
def toggle_favorite(request):
    """Toggle favorite status via AJAX"""
    item_type = request.POST.get('item_type')
    item_id = request.POST.get('item_id')
    
    if not item_type or not item_id:
        return JsonResponse({'success': False, 'error': 'Missing parameters'})
    
    try:
        favorite = Favorite.objects.get(
            user=request.user,
            item_type=item_type,
            item_id=item_id
        )
        favorite.delete()
        return JsonResponse({'success': True, 'favorited': False})
    except Favorite.DoesNotExist:
        Favorite.objects.create(
            user=request.user,
            item_type=item_type,
            item_id=item_id
        )
        return JsonResponse({'success': True, 'favorited': True})

def about(request):
    """About Us page view"""
    return render(request, 'events/about.html')
