from faker import Faker
from .models import User

fake = Faker(['ru_RU'])


def generate_user_fake_data(count):
    for _ in range(count):
        users = User.objects.create(
            username=fake.name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number()
        )
        users.save()
