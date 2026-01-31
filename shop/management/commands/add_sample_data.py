from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from author.models import AuthorProfile
from shop.models import Category, Product
from django.core.files import File
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Add sample vegetable data for the store'

    def handle(self, *args, **options):
        # Create user
        user, created = User.objects.get_or_create(username='sampleuser', defaults={'email': 'sample@example.com'})
        if created:
            user.set_password('password')
            user.save()
            self.stdout.write(self.style.SUCCESS('Created user: sampleuser'))

        # Create author
        author, created = AuthorProfile.objects.get_or_create(user=user, defaults={
            'name': 'Sample Author',
            'email': 'sample@example.com',
            'about': 'Sample author for products',
            'gender': 'male'
        })
        if created:
            src = os.path.join(settings.BASE_DIR, 'static', 'images', 'person_1.jpg')
            if os.path.exists(src):
                with open(src, 'rb') as f:
                    author.photo.save('person_1.jpg', File(f))
            author.save()
            self.stdout.write(self.style.SUCCESS('Created author: Sample Author'))

        # Create categories
        categories_data = [
            {'name': 'Leafy Greens', 'photo_name': 'category.jpg'},
            {'name': 'Root Vegetables', 'photo_name': 'category-1.jpg'},
            {'name': 'Cruciferous', 'photo_name': 'category-3.jpg'},
            {'name': 'Nightshades', 'photo_name': 'category-4.jpg'},
            {'name': 'Legumes', 'photo_name': 'category.jpg'},
            {'name': 'Alliums', 'photo_name': 'category-1.jpg'},
            {'name': 'Herbs', 'photo_name': 'category-3.jpg'},
            {'name': 'Squashes', 'photo_name': 'category-4.jpg'},
        ]
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(name=cat_data['name'])
            if created:
                src = os.path.join(settings.BASE_DIR, 'static', 'images', cat_data['photo_name'])
                if os.path.exists(src):
                    with open(src, 'rb') as f:
                        category.photo.save(cat_data['photo_name'], File(f))
                category.save()
                self.stdout.write(self.style.SUCCESS(f'Created category: {cat_data["name"]}'))
            categories[cat_data['name']] = category

        # Products data - 45 vegetables
        products_data = [
            # Leafy Greens
            {'name': 'Fresh Spinach', 'price': 120, 'details': 'Organic fresh spinach leaves, rich in iron and vitamins. Perfect for salads and smoothies.', 'photo_name': 'product-1.jpg', 'category_name': 'Leafy Greens'},
            {'name': 'Green Lettuce', 'price': 80, 'details': 'Crisp and fresh lettuce leaves, great for salads and sandwiches.', 'photo_name': 'product-2.jpg', 'category_name': 'Leafy Greens'},
            {'name': 'Kale', 'price': 150, 'details': 'Nutritious kale leaves, superfood rich in antioxidants.', 'photo_name': 'product-3.jpg', 'category_name': 'Leafy Greens'},
            {'name': 'Swiss Chard', 'price': 130, 'details': 'Colorful chard with tender leaves and crunchy stalks.', 'photo_name': 'product-4.jpg', 'category_name': 'Leafy Greens'},
            {'name': 'Arugula', 'price': 140, 'details': 'Peppery arugula leaves, perfect for gourmet salads.', 'photo_name': 'product-5.jpg', 'category_name': 'Leafy Greens'},
            {'name': 'Collard Greens', 'price': 110, 'details': 'Large, dark green leaves rich in nutrients.', 'photo_name': 'product-6.jpg', 'category_name': 'Leafy Greens'},
            
            # Root Vegetables
            {'name': 'Fresh Carrot', 'price': 60, 'details': 'Organic fresh carrots, sweet and crunchy. High in beta-carotene.', 'photo_name': 'product-7.jpg', 'category_name': 'Root Vegetables'},
            {'name': 'Potato', 'price': 40, 'details': 'Fresh potatoes, versatile for any dish.', 'photo_name': 'product-8.jpg', 'category_name': 'Root Vegetables'},
            {'name': 'Sweet Potato', 'price': 90, 'details': 'Nutritious sweet potatoes, naturally sweet and delicious.', 'photo_name': 'product-9.jpg', 'category_name': 'Root Vegetables'},
            {'name': 'Red Beet', 'price': 85, 'details': 'Fresh beets, earthy and sweet. Great for salads and juicing.', 'photo_name': 'product-10.jpg', 'category_name': 'Root Vegetables'},
            {'name': 'Radish', 'price': 55, 'details': 'Crunchy red radishes with a peppery bite.', 'photo_name': 'product-11.jpg', 'category_name': 'Root Vegetables'},
            {'name': 'Turnip', 'price': 65, 'details': 'Fresh turnips with mild, slightly sweet flavor.', 'photo_name': 'product-12.jpg', 'category_name': 'Root Vegetables'},
            {'name': 'Ginger Root', 'price': 180, 'details': 'Fresh ginger root, aromatic and spicy. Perfect for cooking and tea.', 'photo_name': 'product-1.jpg', 'category_name': 'Root Vegetables'},
            
            # Cruciferous
            {'name': 'Green Broccoli', 'price': 130, 'details': 'Healthy green broccoli florets, packed with vitamins.', 'photo_name': 'product-2.jpg', 'category_name': 'Cruciferous'},
            {'name': 'Cauliflower', 'price': 120, 'details': 'Fresh white cauliflower heads, versatile and nutritious.', 'photo_name': 'product-3.jpg', 'category_name': 'Cruciferous'},
            {'name': 'Cabbage', 'price': 50, 'details': 'Crunchy cabbage heads, great for slaws and stir-fries.', 'photo_name': 'product-4.jpg', 'category_name': 'Cruciferous'},
            {'name': 'Red Cabbage', 'price': 70, 'details': 'Vibrant red cabbage, rich in antioxidants.', 'photo_name': 'product-5.jpg', 'category_name': 'Cruciferous'},
            {'name': 'Brussels Sprouts', 'price': 160, 'details': 'Fresh Brussels sprouts, miniature cabbage-like vegetables.', 'photo_name': 'product-6.jpg', 'category_name': 'Cruciferous'},
            {'name': 'Bok Choy', 'price': 95, 'details': 'Asian leafy vegetable with tender white stems.', 'photo_name': 'product-7.jpg', 'category_name': 'Cruciferous'},
            
            # Nightshades
            {'name': 'Red Tomato', 'price': 80, 'details': 'Ripe red tomatoes, juicy and flavorful.', 'photo_name': 'product-8.jpg', 'category_name': 'Nightshades'},
            {'name': 'Cherry Tomatoes', 'price': 100, 'details': 'Sweet cherry tomatoes, perfect for snacking.', 'photo_name': 'product-9.jpg', 'category_name': 'Nightshades'},
            {'name': 'Bell Pepper Red', 'price': 120, 'details': 'Sweet red bell peppers, crisp and colorful.', 'photo_name': 'product-10.jpg', 'category_name': 'Nightshades'},
            {'name': 'Bell Pepper Yellow', 'price': 120, 'details': 'Sweet yellow bell peppers, vibrant and crunchy.', 'photo_name': 'product-11.jpg', 'category_name': 'Nightshades'},
            {'name': 'Bell Pepper Green', 'price': 100, 'details': 'Fresh green bell peppers with a mild flavor.', 'photo_name': 'product-12.jpg', 'category_name': 'Nightshades'},
            {'name': 'Eggplant', 'price': 90, 'details': 'Purple eggplants, perfect for grilling and baking.', 'photo_name': 'product-1.jpg', 'category_name': 'Nightshades'},
            {'name': 'Green Chili', 'price': 70, 'details': 'Spicy green chilies for adding heat to dishes.', 'photo_name': 'product-2.jpg', 'category_name': 'Nightshades'},
            
            # Legumes
            {'name': 'Green Beans', 'price': 110, 'details': 'Fresh green beans, tender and crisp.', 'photo_name': 'product-3.jpg', 'category_name': 'Legumes'},
            {'name': 'Snow Peas', 'price': 130, 'details': 'Sweet snow peas with edible pods.', 'photo_name': 'product-4.jpg', 'category_name': 'Legumes'},
            {'name': 'Sugar Snap Peas', 'price': 140, 'details': 'Crunchy snap peas, naturally sweet.', 'photo_name': 'product-5.jpg', 'category_name': 'Legumes'},
            
            # Alliums
            {'name': 'Red Onion', 'price': 45, 'details': 'Sweet red onions, great for salads and grilling.', 'photo_name': 'product-6.jpg', 'category_name': 'Alliums'},
            {'name': 'White Onion', 'price': 40, 'details': 'Fresh white onions with sharp flavor.', 'photo_name': 'product-7.jpg', 'category_name': 'Alliums'},
            {'name': 'Spring Onion', 'price': 60, 'details': 'Fresh spring onions with mild flavor.', 'photo_name': 'product-8.jpg', 'category_name': 'Alliums'},
            {'name': 'Garlic', 'price': 150, 'details': 'Aromatic garlic bulbs, essential for cooking.', 'photo_name': 'product-9.jpg', 'category_name': 'Alliums'},
            {'name': 'Leek', 'price': 95, 'details': 'Mild leeks with tender white stalks.', 'photo_name': 'product-10.jpg', 'category_name': 'Alliums'},
            {'name': 'Shallots', 'price': 120, 'details': 'Small shallots with delicate flavor.', 'photo_name': 'product-11.jpg', 'category_name': 'Alliums'},
            
            # Herbs
            {'name': 'Fresh Coriander', 'price': 30, 'details': 'Fresh coriander leaves, aromatic herb for garnishing.', 'photo_name': 'product-12.jpg', 'category_name': 'Herbs'},
            {'name': 'Mint Leaves', 'price': 40, 'details': 'Fresh mint leaves, refreshing and aromatic.', 'photo_name': 'product-1.jpg', 'category_name': 'Herbs'},
            {'name': 'Basil', 'price': 50, 'details': 'Fresh basil leaves with sweet aroma.', 'photo_name': 'product-2.jpg', 'category_name': 'Herbs'},
            {'name': 'Parsley', 'price': 45, 'details': 'Fresh parsley, versatile herb for many dishes.', 'photo_name': 'product-3.jpg', 'category_name': 'Herbs'},
            
            # Squashes
            {'name': 'Zucchini', 'price': 85, 'details': 'Fresh green zucchini, tender and mild.', 'photo_name': 'product-4.jpg', 'category_name': 'Squashes'},
            {'name': 'Yellow Squash', 'price': 90, 'details': 'Bright yellow squash with delicate flavor.', 'photo_name': 'product-5.jpg', 'category_name': 'Squashes'},
            {'name': 'Pumpkin', 'price': 70, 'details': 'Fresh pumpkin, sweet and versatile.', 'photo_name': 'product-6.jpg', 'category_name': 'Squashes'},
            {'name': 'Bottle Gourd', 'price': 55, 'details': 'Fresh bottle gourd, mild and healthy.', 'photo_name': 'product-7.jpg', 'category_name': 'Squashes'},
            {'name': 'Bitter Gourd', 'price': 65, 'details': 'Bitter gourd with unique taste and health benefits.', 'photo_name': 'product-8.jpg', 'category_name': 'Squashes'},
            {'name': 'Ridge Gourd', 'price': 60, 'details': 'Fresh ridge gourd with tender flesh.', 'photo_name': 'product-9.jpg', 'category_name': 'Squashes'},
        ]

        created_count = 0
        existing_count = 0

        for prod_data in products_data:
            if not Product.objects.filter(name=prod_data['name']).exists():
                product = Product(
                    name=prod_data['name'],
                    price=prod_data['price'],
                    details=prod_data['details'],
                    category=categories[prod_data['category_name']],
                    author=author
                )
                # Copy image from static to media
                src_path = os.path.join(settings.BASE_DIR, 'static', 'images', prod_data['photo_name'])
                if os.path.exists(src_path):
                    with open(src_path, 'rb') as f:
                        product.photo.save(prod_data['photo_name'], File(f), save=False)
                product.save()
                self.stdout.write(self.style.SUCCESS(f'✓ Created: {prod_data["name"]} - ₹{prod_data["price"]}'))
                created_count += 1
            else:
                existing_count += 1

        self.stdout.write(self.style.SUCCESS(f'\n{"="*60}'))
        self.stdout.write(self.style.SUCCESS(f'Products added: {created_count}'))
        self.stdout.write(self.style.WARNING(f'Already existing: {existing_count}'))
        self.stdout.write(self.style.SUCCESS(f'Total products in database: {Product.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'{"="*60}\n'))
