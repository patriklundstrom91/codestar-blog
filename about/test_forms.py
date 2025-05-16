from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Ulf',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")


    def test_form_is_invalid_name(self):
        """Test invalid name"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Name not provided but Form is valid")


    def test_form_is_invalid_email(self):
        """Test invalid email"""
        form = CollaborateForm({
            'name': 'Ulf',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="email not provided but Form is valid")


    def test_form_is_invalid_message(self):
        """Test invalid message"""
        form = CollaborateForm({
            'name': 'Ulf',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="message not provided but Form is valid")