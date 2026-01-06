from django.contrib import admin
from .models import (Category, SubCategory, Package, VenueItem, VenueImage,
                     JewelleryItem, JewelleryImage, FoodItem, FoodImage, Favorite)


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'created_at')
    search_fields = ('name', 'description')
    inlines = [SubCategoryInline]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)


# Venue Admin
class VenueImageInline(admin.TabularInline):
    model = VenueImage
    extra = 3


@admin.register(VenueItem)
class VenueItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'location', 'price_per_day', 'capacity')
    list_filter = ('subcategory', 'location')
    search_fields = ('name', 'location', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [VenueImageInline]


# Jewellery Admin
class JewelleryImageInline(admin.TabularInline):
    model = JewelleryImage
    extra = 3


@admin.register(JewelleryItem)
class JewelleryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'material', 'rental_price')
    list_filter = ('subcategory', 'material')
    search_fields = ('name', 'material', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [JewelleryImageInline]


# Food Admin
class FoodImageInline(admin.TabularInline):
    model = FoodImage
    extra = 3


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'cuisine_type', 'price_per_plate', 'serves')
    list_filter = ('subcategory', 'cuisine_type')
    search_fields = ('name', 'cuisine_type', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [FoodImageInline]


# Favorites Admin
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_type', 'item_id', 'created_at')
    list_filter = ('item_type', 'created_at')
    search_fields = ('user__username',)
