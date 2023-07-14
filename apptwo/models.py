from django.db import models


# Create your models here.
class Rate(models.Model):
    name = models.CharField(max_length=100)
    rateing = models.CharField(max_length=100)
    feedback = models.CharField(max_length=200)
    bestrider = models.CharField(max_length=200)


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/")


class Signup(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)


class Rider(models.Model):
    Srn = models.CharField(max_length=20, unique=True)


class Passenger(models.Model):
    Srn = models.CharField(max_length=20, unique=True)


class MapVal(models.Model):
    Mapp = models.CharField(max_length=200)


class MAP(models.Model):
    # MapVal = models.JSONField()

    def create_mapping_dict():
        mapping_dict = {}
        class1_objects = Rider.objects.all()

        for obj in class1_objects:
            try:
                class2_obj = Passenger.objects.get(Srn=obj.Srn)
                mapping_dict[obj.key] = class2_obj.value
            except Passenger.DoesNotExist:
                print("No driver found")

        return mapping_dict


class FileField(models.Model):
    File = models.FileField(upload_to="downloads/")
