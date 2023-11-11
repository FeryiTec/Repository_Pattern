import abc
from users.model import user_model
from users.model import courses_model


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, user: user_model.User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> user_model.User:
        raise NotImplementedError

class AbstractRepositoryC(abc.ABC):   
    @abc.abstractmethod
    def add(self, course: courses_model.Course):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> courses_model.Course:
        raise NotImplementedError
