import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_landing_page(client):
    """Test that the landing page renders correctly and contains footer links."""
    response = client.get('/')
    assert response.status_code == 200
    html_content = response.data.decode('utf-8')
    
    # Check that footer links are present and correct
    assert '/privacy-policy' in html_content
    assert '/terms-and-conditions' in html_content
    assert 'Privacy Policy' in html_content
    assert 'Terms and Conditions' in html_content

def test_register_page(client):
    """Test that the register page renders correctly."""
    response = client.get('/register')
    assert response.status_code == 200

def test_login_page(client):
    """Test that the login page renders correctly."""
    response = client.get('/login')
    assert response.status_code == 200

def test_privacy_policy_page(client):
    """Test that the privacy policy page renders correctly and contains expected content."""
    response = client.get('/privacy-policy')
    assert response.status_code == 200
    html_content = response.data.decode('utf-8')
    assert 'Privacy Policy' in html_content
    assert 'Information We Collect' in html_content

def test_terms_and_conditions_page(client):
    """Test that the terms and conditions page renders correctly and contains expected content."""
    response = client.get('/terms-and-conditions')
    assert response.status_code == 200
    html_content = response.data.decode('utf-8')
    assert 'Terms and Conditions' in html_content
    assert 'Acceptance of Terms' in html_content
