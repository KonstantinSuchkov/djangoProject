from django.core.management.base import BaseCommand
from authapp.models import ClientUser
from authapp.models import ClientUserProfile


class Command(BaseCommand):
    help = 'Update DB'

    def handle(self, *args, **options):
        users = ClientUser.objects.all()
        for user in users:
            users_profile = ClientUserProfile.objects.create(user=user)
            users_profile.save()
