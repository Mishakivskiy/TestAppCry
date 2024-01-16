from django.db.models import Model, CharField, IntegerField


class Car(Model):
    brand = CharField(max_length=50)
    model = CharField(max_length=50)
    horse_power = IntegerField()
