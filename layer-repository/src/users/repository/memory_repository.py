from users.repository.abstract_repository import AbstractRepository
from users.repository.abstract_repository import AbstractRepositoryC
from users.model import user_model
from users.model import courses_model


class UserRepository(AbstractRepository):

    def __init__(self):
        self.users = []

    def add(self, user: user_model.User):
        self.users.append(user)

    def get(self, user_id) -> user_model.User:
        user = next((user for user in self.users if user.id == int(user_id)), None)
        return user
    
class CourseRepository(AbstractRepositoryC):

    def __init__(self):
        self.courses = []

    def add(self, course: courses_model.Course):
        self.courses.append(course)

    def get(self, course_id) -> courses_model.Course:
        course = next((course for course in self.courses if course.id == int(course_id)), None)
        return course
    

