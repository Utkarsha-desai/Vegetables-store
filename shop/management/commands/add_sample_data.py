from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from author.models import AuthorProfile
from shop.models import Category, Product
from django.core.files import File
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Add sample data for development'

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
            {'name': 'Vegetables', 'photo_name': 'category.jpg'},
            {'name': 'Fruits', 'photo_name': 'category-1.jpg'},
            {'name': 'Juices', 'photo_name': 'category-3.jpg'},
            {'name': 'Dried', 'photo_name': 'category-4.jpg'},
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

        # Products data
        products_data = [
            {'name': 'Fresh Carrot', 'price': 418, 'details': 'Organic fresh carrots', 'photo_name': 'product-1.jpg', 'category_name': 'Vegetables'},
            {'name': 'Green Broccoli', 'price': 668, 'details': 'Healthy green broccoli', 'photo_name': 'product-2.jpg', 'category_name': 'Vegetables'},
            {'name': 'Red Tomato', 'price': 250, 'details': 'Ripe red tomatoes', 'photo_name': 'product-3.jpg', 'category_name': 'Vegetables'},
            {'name': 'Organic Spinach', 'price': 334, 'details': 'Fresh organic spinach', 'photo_name': 'product-4.jpg', 'category_name': 'Vegetables'},
            {'name': 'Yellow Bell Pepper', 'price': 501, 'details': 'Sweet yellow bell peppers', 'photo_name': 'product-5.jpg', 'category_name': 'Vegetables'},
            {'name': 'Fresh Cucumber', 'price': 334, 'details': 'Crisp and fresh cucumbers', 'photo_name': 'product-6.jpg', 'category_name': 'Vegetables'},
            {'name': 'Green Lettuce', 'price': 250, 'details': 'Fresh green lettuce leaves', 'photo_name': 'product-7.jpg', 'category_name': 'Vegetables'},
            {'name': 'Red Onion', 'price': 167, 'details': 'Sweet red onions', 'photo_name': 'product-8.jpg', 'category_name': 'Vegetables'},
            {'name': 'Potato', 'price': 84, 'details': 'Starchy potatoes', 'photo_name': 'product-9.jpg', 'category_name': 'Vegetables'},
            {'name': 'Garlic', 'price': 418, 'details': 'Aromatic garlic bulbs', 'photo_name': 'product-10.jpg', 'category_name': 'Vegetables'},
            {'name': 'Cabbage', 'price': 334, 'details': 'Crunchy cabbage heads', 'photo_name': 'product-11.jpg', 'category_name': 'Vegetables'},
            {'name': 'Eggplant', 'price': 501, 'details': 'Purple eggplants', 'photo_name': 'product-12.jpg', 'category_name': 'Vegetables'},
            {'name': 'Zucchini', 'price': 334, 'details': 'Green zucchinis', 'photo_name': 'product-1.jpg', 'category_name': 'Vegetables'},
            {'name': 'Asparagus', 'price': 585, 'details': 'Fresh asparagus spears', 'photo_name': 'product-2.jpg', 'category_name': 'Vegetables'},
            {'name': 'Cauliflower', 'price': 418, 'details': 'White cauliflower heads', 'photo_name': 'product-3.jpg', 'category_name': 'Vegetables'},
            {'name': 'Kale', 'price': 334, 'details': 'Nutritious kale leaves', 'photo_name': 'product-4.jpg', 'category_name': 'Vegetables'},
            {'name': 'Radish', 'price': 167, 'details': 'Crunchy red radishes', 'photo_name': 'product-5.jpg', 'category_name': 'Vegetables'},
            {'name': 'Beet', 'price': 250, 'details': 'Sweet beets', 'photo_name': 'product-6.jpg', 'category_name': 'Vegetables'},
            {'name': 'Mushroom', 'price': 501, 'details': 'Fresh mushrooms', 'photo_name': 'product-7.jpg', 'category_name': 'Vegetables'},
            {'name': 'Celery', 'price': 250, 'details': 'Crisp celery stalks', 'photo_name': 'product-8.jpg', 'category_name': 'Vegetables'},
            {'name': 'Sweet Potato', 'price': 334, 'details': 'Nutritious sweet potatoes', 'photo_name': 'product-9.jpg', 'category_name': 'Vegetables'},
            {'name': 'Green Beans', 'price': 418, 'details': 'Fresh green beans', 'photo_name': 'product-10.jpg', 'category_name': 'Vegetables'},
            {'name': 'Broccoli Rabe', 'price': 501, 'details': 'Bitter broccoli rabe', 'photo_name': 'product-11.jpg', 'category_name': 'Vegetables'},
            {'name': 'Artichoke', 'price': 585, 'details': 'Tender artichokes', 'photo_name': 'product-12.jpg', 'category_name': 'Vegetables'},
            {'name': 'Leek', 'price': 250, 'details': 'Mild leeks', 'photo_name': 'product-1.jpg', 'category_name': 'Vegetables'},
            # Fruits
            {'name': 'Apple', 'price': 167, 'details': 'Fresh red apples', 'photo_name': 'product-2.jpg', 'category_name': 'Fruits'},
            {'name': 'Banana', 'price': 84, 'details': 'Ripe bananas', 'photo_name': 'product-3.jpg', 'category_name': 'Fruits'},
            {'name': 'Orange', 'price': 250, 'details': 'Juicy oranges', 'photo_name': 'product-4.jpg', 'category_name': 'Fruits'},
            # Juices
            {'name': 'Carrot Juice', 'price': 334, 'details': 'Fresh carrot juice', 'photo_name': 'product-5.jpg', 'category_name': 'Juices'},
            {'name': 'Tomato Juice', 'price': 250, 'details': 'Pure tomato juice', 'photo_name': 'product-6.jpg', 'category_name': 'Juices'},
            # Dried - only vegetable-related
            {'name': 'Dried Tomatoes', 'price': 418, 'details': 'Sun-dried tomatoes', 'photo_name': 'product-7.jpg', 'category_name': 'Dried'},
            {'name': 'Dried Mushrooms', 'price': 501, 'details': 'Dried mushrooms', 'photo_name': 'product-8.jpg', 'category_name': 'Dried'},
            {'name': 'Dried Garlic', 'price': 4, 'details': 'Dried garlic flakes', 'photo_name': 'product-9.jpg', 'category_name': 'Dried'},
        ]

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
                self.stdout.write(self.style.SUCCESS(f'Created product: {prod_data["name"]}'))
            else:
                self.stdout.write(f'Product {prod_data["name"]} already exists')

        self.stdout.write(self.style.SUCCESS('Sample data added successfully'))
