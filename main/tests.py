from django.test import TestCase
from .models import Product, Order, OrderItem
from django.contrib.auth.models import User

# Create your tests here.

class TestStatus(TestCase):

    def test_main(self):
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('MIET FOOD', response.content.decode())

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('MIET FOOD', response.content.decode())

    def test_register(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('MIET FOOD', response.content.decode())


    def test_profile(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ваш профиль', response.content.decode())

class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='peter',
            email='petergriffin@fguy.com',
            password='petah1111')

        self.order1 = Order.objects.create(
            customer= self.user1,
            number='P100',
            complete=False
        )

        self.product1 = Product.objects.create(
            title = 'brusnichka',
            description = 'yummy',
            price = 75.0,
            amount = 100
        )

        self.product2 = Product.objects.create(
            title = 'bush',
            description = 'yes',
            price = 75.5,
            amount = 150
        )

        self.order_item1 = OrderItem.objects.create(
            product = self.product1,
            order = self.order1,
            quantity = 10
        )

        self.order_item2 = OrderItem.objects.create(
            product = self.product2,
            order = self.order1,
            quantity = 15
        )

    def test_order_str(self):
        self.assertEqual(str(self.order1), 'P100')

    def test_order_total(self):
        self.assertEqual(self.order1.get_cart_total, 1882.5)

    def test_order_items(self):
        self.assertEqual(self.order1.get_cart_items, 25)

    def test_product_str(self):
        self.assertEqual(str(self.product1), 'brusnichka')
        self.assertEqual(str(self.product2), 'bush')

    def test_order_item_str(self):
        self.assertEqual(str(self.order_item1), 'brusnichka')
        self.assertEqual(str(self.order_item2), 'bush')

    def test_prder_item_total(self):
        self.assertEqual(self.order_item1.get_total, 750.0)
        self.assertEqual(self.order_item2.get_total, 1132.5)