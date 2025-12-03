from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser named "ahmet" if it does not exist'

    def handle(self, *args, **options):
        # Check if user 'ahmet' already exists
        if not User.objects.filter(username='ahmet').exists():
            # Create superuser 'ahmet' with email and password
            User.objects.create_superuser('ahmet', 'ahmet@example.com', 'your_password')
            self.stdout.write(
                self.style.SUCCESS("Superuser 'ahmet' successfully created!")
            )
        else:
            self.stdout.write(
                self.style.WARNING("User 'ahmet' already exists.")
            )