# """
# This file (test_models.py) contains the unit tests for the models.py file.
# """
# from webappflask.models import User
#
#
# def test_new_user():
#     """
#     GIVEN a User model
#     WHEN a new User is created
#     THEN check the email, hashed_password, authenticated, and role fields are defined correctly
#     """
#     user = User('user1', 'user1@gmail.com', 'testing')
#     assert user.email == 'user1@gmail.com'
#     assert user.hashed_password != 'testing'
#     assert user.role == 'user'
#     assert user.__repr__() == '<User: user1@gmail.com>'
#     assert user.is_authenticated
#     assert user.is_active
#     assert not user.is_anonymous
#
#
# def test_new_user_with_fixture(new_user):
#     """
#     GIVEN a User model
#     WHEN a new User is created
#     THEN check the email, hashed_password, authenticated, and role fields are defined correctly
#     """
#     assert new_user.email == 'user1@gmail.com'
#     assert new_user.hashed_password != 'testing'
#     assert new_user.role == 'user'
#
#
# def test_setting_password(new_user):
#     """
#     GIVEN an existing User
#     WHEN the password for the user is set
#     THEN check the password is stored correctly and not as plaintext
#     """
#     new_user.set_password('NewPassword')
#     assert new_user.hashed_password != 'NewPassword'
#     assert new_user.is_correct_password('NewPassword')
#     assert not new_user.is_correct_password('NewPassword2')
#     assert not new_user.is_correct_password('testing')
#
#
# def test_user_id(new_user):
#     """
#     GIVEN an existing User
#     WHEN the ID of the user is defined to a value
#     THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
#     """
#     new_user.id = 17
#     assert isinstance(new_user.get_id(), str)
#     assert not isinstance(new_user.get_id(), int)
#     assert new_user.get_id() == '17'
