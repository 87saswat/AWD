from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "Dynamically print the name  with greeting"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Take the name from commandline argument")

    def handle(self, *args, **kwargs):
        name=kwargs['name']
        greeting = f'Hi {name}, Good morning !'

        self.stdout.write(greeting)
        #self.stdout.write(self.style.SUCCESS('greeting'))
         #self.stdout.write(self.style.WARNING('greeting'))