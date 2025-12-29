from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    """Test cases for the homepage"""
    
    def test_home_page_status_code(self):
        """Test that homepage returns 200 status"""
        response = self.client.get(reverse('events:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_uses_correct_template(self):
        """Test that homepage uses the correct template"""
        response = self.client.get(reverse('events:home'))
        self.assertTemplateUsed(response, 'events/home.html')
    
    def test_home_page_contains_packages(self):
        """Test that homepage contains packages"""
        response = self.client.get(reverse('events:home'))
        self.assertContains(response, 'Silver Package')
        self.assertContains(response, 'Gold Package')
        self.assertContains(response, 'Platinum Package')
    
    def test_home_page_contains_categories(self):
        """Test that homepage contains all categories"""
        response = self.client.get(reverse('events:home'))
        categories = ['Venue', 'Makeup', 'Photographers', 'Mehandi', 
                     'Virtual Planning', 'Jewellary', 'Food', 
                     'Pre Wedding Shoot', 'Pandit']
        
        for category in categories:
            self.assertContains(response, category)
