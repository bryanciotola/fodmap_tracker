from django.contrib import admin
from .models import FoodItem, FoodLogEntry

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'food_type', 'details']
    list_filter = ['category', 'food_type']

class FoodLogEntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'comment_summary']
    filter_horizontal = ['food_items']

    def comment_summary(self, obj):
        return obj.comments[:60]  # Display first 60 characters of comments

admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(FoodLogEntry, FoodLogEntryAdmin)
