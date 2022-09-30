from django.core.management.base import BaseCommand
from measurement.models import Sensor, Measurement
import random
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        sensor_list = [
            {'name': 'ДТ1', 'description': 'датчик температуры в коридоре'},
            {'name': 'ДТ2', 'description': 'датчик температуры в комнате'},
            {'name': 'ДТ3', 'description': 'датчик температуры в кухне'},
            {'name': 'ДТ4', 'description': 'датчик температуры в ванной'},
            {'name': 'ДТ5', 'description': 'датчик температуры наружного воздуха'}
        ]

        for sens in sensor_list:
            sensor = Sensor(
                name=sens['name'],
                description=sens['description'],
            )
            sensor.save()

        sensors = Sensor.objects.all()
        for sensor in sensors:
            mesures_list = [
                {'temperature': round(random.uniform(20, 22), 1),
                 'date_time': datetime.strptime('07/20/2022 8:30 AM +0300', '%m/%d/%Y %I:%M %p %z')},
                {'temperature': round(random.uniform(20, 22), 1),
                 'date_time': datetime.strptime('07/20/2022 12:30 PM +0300', '%m/%d/%Y %I:%M %p %z')},
                {'temperature': round(random.uniform(20, 22), 1),
                 'date_time': datetime.strptime('07/20/2022 4:30 PM +0300', '%m/%d/%Y %I:%M %p %z')},
                {'temperature': round(random.uniform(20, 22), 1),
                 'date_time': datetime.strptime('07/20/2022 8:30 PM +0300', '%m/%d/%Y %I:%M %p %z')}
            ]
            for measure in mesures_list:
                Measurement.objects.create(
                    sensor=sensor,
                    temperature=measure['temperature'],
                    created_at=measure['date_time']
                )

