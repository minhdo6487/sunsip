
from django.test import TestCase, RequestFactory

from .views import LoginView, RegisterView
from core.user.models import User

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    # def test_details(self):
    #     # Create an instance of a GET request.
    #     request = self.factory.post('/api/login/', {'username': 'golfer@gmail.com', 'password': '12345678',
    #                                                 'email': 'golfer@gmail.com'}, format='json')
    #     my_view = LoginView.as_view()
    #     # Test my_view() as if it were deployed at /customer/details
    #     response = my_view(request)
    #     response.render()
    #     print(response.content.decode('utf-8'))
    #     self.assertEqual(response.status_code, 200)

    def test_register(self):
        payload = {
            'username'  : 'tester@golfconnect24.com',
            'email'     : 'tester@golfconnect24.com',
            'password'  : '12345789',
            'first_name': 'tester',
            'last_name' : 'golfconnect',
        }
        payload['password_confirmation'] = payload['password']
        request = self.factory.post('/api/register/', payload, format='json')
        resp = RegisterView.as_view()(request)
        self.assertEqual(resp.status_code, 200)

        n = User.objects.filter(username=payload['username']).count()
        self.assertEqual(n, 1)
