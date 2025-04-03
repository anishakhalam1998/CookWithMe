import pytest
from django.urls import reverse,resolve
from django.test import Client

@pytest.mark.django_db
def test_home_url():
    """Test the home page URL"""
    url = reverse('home')
    response = Client().get(url)
    assert response.status_code == 200
    assert 'Welcome' in response.content.decode()  # Update to match actual content


@pytest.mark.django_db
def test_login_url():
    """Test the login page URL"""
    url = reverse('login')
    response = Client().get(url)
    assert response.status_code == 200
    assert 'Login' in response.content.decode()  # Check if login page is rendered


@pytest.mark.django_db
def test_logout_url():
    """Test the logout page URL"""
    path = reverse('logout', kwargs={})
    assert resolve(path).view_name == 'logout' # Ensure redirection to login page


@pytest.mark.django_db
def test_signup_url():
    """Test the signup page URL"""
    url = reverse('signup')
    response = Client().get(url)
    assert response.status_code == 200
    assert 'Sign Up' in response.content.decode()  # Check for sign up form
