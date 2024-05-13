from django.db import models

class FoodItem(models.Model):
    FOOD_CHOICES = [
        ('NO', 'Do Not Eat'),
        ('LIMIT', 'Limit Intake'),
        ('FREE', 'Eat Freely')
    ]
    FOOD_TYPE_CHOICES = [
        ('DAIRY', 'Dairy'),
        ('MEAT_PROTEIN', 'Meat + Protein'),
        ('FLAVOUR', 'Flavour'),
        ('VEGGIES', 'Veggies'),
        ('FRUITS', 'Fruits'),
        ('GRAINS', 'Grains'),
        ('BEVVIES', 'Bevvies'),
        ('SWEETS', 'Sweets'),
        ('NUTS', 'Nuts'),
        ('SEEDS', 'Seeds'),
        ('SNEAKY_SNACKS', 'Sneaky Snacks'),
        ('FLOURS_STARCHES', 'Flours + Starches')
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=5, choices=FOOD_CHOICES)
    food_type = models.CharField(max_length=15, choices=FOOD_TYPE_CHOICES)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name

class FoodLogEntry(models.Model):
    date = models.DateField(auto_now_add=True)
    food_items = models.ManyToManyField(FoodItem)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f'Log Entry on {self.date}'
