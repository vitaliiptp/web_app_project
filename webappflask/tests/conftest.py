import pytest
from webappflask import create_app, db
from webappflask.models import User
from webappflask.config import Config_Test


@pytest.fixture(scope='module')
def new_user():
    user = User('user1', 'user1@gmail.com', 'testing')
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config_class=Config_Test)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all(app=create_app())

    # Insert user data
    user1 = User(username='user1', email='user1@gmail.com', password='testing')
    user2 = User(username='user2', email='user2@gmail.com', password='testing')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(username='user1', email='user1@gmail.com', password='testing'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)
