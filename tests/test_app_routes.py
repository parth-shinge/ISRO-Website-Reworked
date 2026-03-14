from app import app as flask_app


def test_home_route_ok():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        response = client.get('/')
    assert response.status_code == 200


def test_contact_route_ok():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        response = client.get('/contact')
    assert response.status_code == 200


def test_invalid_template_returns_404():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        response = client.get('/template-does-not-exist')
    assert response.status_code == 404


def test_forgot_password_get_redirects_to_login():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        response = client.get('/forgot_password')
    assert response.status_code == 302
    assert '/login' in response.location


def test_submit_feedback_redirects_to_valid_page():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        response = client.post(
            '/submit_feedback',
            data={'name': 'Test', 'email': 'test@example.com', 'message': 'Great site'},
        )
    assert response.status_code == 302
    assert '/valid' in response.location
