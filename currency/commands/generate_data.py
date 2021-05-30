from django.core.management.base import BaseCommand
from currency.models import Rate
import random


class Command(BaseCommand):
    help = 'Generate Random records'

    def handle(self, *args, **options):
        for index in range(100):
            Rate.object.create(
                type=random.choice(('usd', 'eur')),
                sale=index,
                buy=index + 1,
                source='monobank'
            )
            # rate = Rate(
            #     type='usd',
            #     sale=index,
            #     buy=index + 1,
            #     source='monobank'
            # )
        return Rate