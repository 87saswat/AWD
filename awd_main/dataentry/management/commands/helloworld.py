from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "prints helloworld"

    def handle(self, *arags,**kwargs):
        self.stdout.write("Hello World")