from flet_demo.user import User


class Repository:
    _users = []

    def find_all(self) -> list[User]:
        return self._users

    def find(self, uid: str) -> User:
        return next(filter(lambda user: user.id == uid, self._users))

    def insert(self, user: User):
        self._users.append(user)


repository = Repository()
