from src.repository import UserRepository
from test.builders.user_builder import build_user, build_user_id, build_user_address


class TestUserRepository:
    def test_get_user(self, user_repository: UserRepository):
        """Test saving a user and retrieving it from the repository"""
        user_id = build_user_id()
        user = build_user(id=user_id)
        user_repository.save_user(user)
        user_stored = user_repository.get_user(user_id)

        assert user_stored is not None
        assert user_stored.id == user.id
        assert user_stored.username == user.username
        assert user_stored.email == user.email
        assert user_stored.address == user.address

    def test_get_all_users(self, user_repository: UserRepository):
        """Test saving multiple users and retrieving them from the repository"""
        user_ids = [build_user_id() for _ in range(3)]
        users = [build_user(id=user_id) for user_id in user_ids]
        for user in users:
            user_repository.save_user(user)

        users_stored = user_repository.get_all_events()
        assert len(users_stored) == 3
        assert all(user in users_stored for user in users)

    def test_get_non_existing_user(self, user_repository: UserRepository):
        """Test retrieving a non-existing user from the repository"""
        user_id = build_user_id()
        user_stored = user_repository.get_user(user_id)

        assert user_stored is None

    def test_user_full_cycloe(self, user_repository: UserRepository):
        """Test saving a user, updating email and adding address"""
        user_id = build_user_id()
        user = build_user(id=user_id)
        user_repository.save_user(user)

        new_email = "updatedemail@example.com"
        user_repository.update_email(user=user, new_email=new_email)

        address = build_user_address()
        user_repository.add_address(user=user, address=address)

        user = user_repository.get_user(user_id)
        assert user is not None
        assert user.id == user_id
        assert user.username == user.username
        assert user.email == new_email
        assert user.address == address
