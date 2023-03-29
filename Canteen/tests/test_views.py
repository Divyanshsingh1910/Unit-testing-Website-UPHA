from django.test import TestCase, Client
from django.urls import reverse
from Canteen.models import Menu, Bill, Order
from django.contrib.auth.models import User
from Login.models import UserManager, User_class

class TestView(TestCase):

    def setUp(self):
        # Create a student user
        self.user = User_class.objects.create_user(
            username='student',
            name='Student',
            password='pass1234',
            designation='Student'
        )
        # Create some menu items
        self.item = Menu.objects.create(
            Item_Name='item',
            Price=20
        ) 

    def test_place_order_success(self):
        # Login as the student user
        self.client.login(username='student', password='pass1234')
        # Submit a POST request to place an order
        response = self.client.post(
            reverse('Student_Place_Order'),
            data={
                'submit': self.item.id,
                'quantity': 2
            }
        )
        # Check that the response status is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check that the order has been added to the database
        order = Order.objects.get(
            User_Name='student',
            Item_Name='item',
            Cart_Status=True
        )
        self.assertEqual(order.Quantity, 2)
        self.assertEqual(order.Amount, 40)
        print(order.Order_Date_Time)
        # Check that the success message is displayed
        messages = list(response.context.get('messages'))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your order has been successfully added to cart')

    def test_place_order_not_authenticated(self):
        # Submit a POST request to place an order without logging in
        response = self.client.post(
            reverse('Student_Place_Order'),
            data={
                'submit': self.item.id,
                'quantity': 2
            }
        )
        # Check that the response status is 200 OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Error.html')

    def test_place_order_not_student(self):
        # Create a non-student user
        user2 = User_class.objects.create_user(
            username='canteen_manager',
            name='Canteen Manager',
            password='pass1234',
            designation='Canteen Manager'
        )
        # Login as the non-student user
        self.client.login(username='canteen_manager', password='pass1234')
        # Submit a POST request to place an order
        response = self.client.post(
            reverse('Student_Place_Order'),
            data={
                'submit': self.item.id,
                'quantity': 2
            }
        )
        # Check that the response status is 200 OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Error.html')