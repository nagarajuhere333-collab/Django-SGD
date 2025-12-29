from django import forms


class ContactForm(forms.Form):
    """Contact form for event inquiries"""
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your Email'
        })
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your Phone Number'
        })
    )
    wedding_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-input',
            'type': 'date'
        })
    )
    wedding_destination = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Wedding Destination'
        })
    )
    wedding_budget = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Your Budget'
        })
    )
    
    # Function checkboxes
    FUNCTION_CHOICES = [
        ('mehendi', 'Mehendi'),
        ('sangeet', 'Sangeet'),
        ('wedding', 'Wedding'),
        ('cocktail', 'Cocktail Party'),
        ('reception', 'Reception'),
    ]
    functions = forms.MultipleChoiceField(
        choices=FUNCTION_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox'}),
        required=False
    )
    
    # Hotel category
    HOTEL_CHOICES = [
        ('5_star', '5 star'),
        ('4_star', '4 star'),
        ('3_star', '3 star'),
        ('villa', 'Villa'),
    ]
    hotel_category = forms.MultipleChoiceField(
        choices=HOTEL_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox'}),
        required=False
    )
    
    number_of_rooms = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-input',
            'placeholder': 'Number of Rooms'
        })
    )
    
    # How did you hear about us
    REFERRAL_CHOICES = [
        ('', 'Select an option'),
        ('internet', 'Internet Search'),
        ('social_media', 'Social Media'),
        ('friend', 'Friend/Family'),
        ('advertisement', 'Advertisement'),
        ('other', 'Other'),
    ]
    heard_from = forms.ChoiceField(
        choices=REFERRAL_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        required=False
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Tell us about your dream day...',
            'rows': 5
        }),
        required=False
    )
    
    # Consultation preference
    CONSULTATION_CHOICES = [
        ('yes', 'Yes, I would prefer to talk to you'),
        ('no', 'No, I would stick with email for now'),
    ]
    consultation = forms.ChoiceField(
        choices=CONSULTATION_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-radio'}),
        initial='no',
        required=False
    )
