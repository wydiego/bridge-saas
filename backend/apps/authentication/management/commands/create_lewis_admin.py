from django.core.management.base import BaseCommand
from django.conf import settings
from apps.authentication.models import User

class Command(BaseCommand):
    help = 'Create Lewis admin user'

    def handle(self, *args, **options):
        lewis_config = settings.LEWIS_ADMIN
        
        if not User.objects.filter(username=lewis_config['USERNAME']).exists():
            admin_user = User.objects.create_superuser(
                username=lewis_config['USERNAME'],
                email=lewis_config['EMAIL'],
                password=lewis_config['PASSWORD'],
                first_name=lewis_config['FIRST_NAME'],
                last_name=lewis_config['LAST_NAME'],
            )
            self.stdout.write(
                self.style.SUCCESS(f'✅ Usuario admin Lewis creado: {admin_user.email}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('⚠️ Usuario Lewis ya existe')
            )
