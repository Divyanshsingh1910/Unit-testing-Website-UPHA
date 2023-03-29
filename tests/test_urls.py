from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Canteen.views import Student_Place_Order, Student_Cart, Student_Pending_Order, Student_Orders_History, Owner_New_Order, Owner_Pending_Order, Owner_Modify_Menu, Owner_Students_Bill

class TestUrls(SimpleTestCase):

    def test_Student_Place_Order(self):
        url = reverse('Student_Place_Order')
        self.assertEquals(resolve(url).func, Student_Place_Order)
    
    def test_Student_Cart(self):
        url = reverse('Student_Cart')
        self.assertEquals(resolve(url).func, Student_Cart)
    
    def test_Student_Pending_Order(self):
        url = reverse('Student_Pending_Order')
        self.assertEquals(resolve(url).func, Student_Pending_Order)
    
    def test_Student_Orders_History(self):
        url = reverse('Student_Orders_History')
        self.assertEquals(resolve(url).func, Student_Orders_History)
    
    def test_Owner_New_Order(self):
        url = reverse('Owner_New_Order')
        self.assertEquals(resolve(url).func, Owner_New_Order)
    
    def test_Owner_Pending_Order(self):
        url = reverse('Owner_Pending_Order')
        self.assertEquals(resolve(url).func, Owner_Pending_Order)
    
    def test_Owner_Modify_Menu(self):
        url = reverse('Owner_Modify_Menu')
        self.assertEquals(resolve(url).func, Owner_Modify_Menu)
    
    def test_Owner_Students_Bill(self):
        url = reverse('Owner_Students_Bill')
        self.assertEquals(resolve(url).func, Owner_Students_Bill)