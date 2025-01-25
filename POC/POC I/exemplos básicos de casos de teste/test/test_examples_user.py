import pytest
from src.examples import User

# Teste original:

# def test_create_user():
#     user = User("Iara", "123456")
#     assert user.name == "Iara"
#     assert user.password == "123456"
    
def test_create_user_valid():
    user = User("Iara", "12345678")
    assert user.name == "Iara"
    assert user.password == "12345678"

def test_create_user_invalid():
    with pytest.raises(ValueError):
        User("I", "123456")
    with pytest.raises(ValueError):
        User("Iara", "12345")

def test_update_password():
    user = User("Iara", "12345678")
    user.update_password("98765432")
    assert user.password == "98765432"

def test_delete_account():
    user = User("Iara", "12345678")
    user.delete_account()
    assert hasattr(user, "Iara") is False