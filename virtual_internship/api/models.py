from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class PerevalAdded(models.Model):
    class Meta:
        db_table = 'pereval_added'

    class Status(models.TextChoices):
        NEW = 'NEW', 'New'
        PENDING = 'PEN', 'Pending'
        ACCEPTED = 'ACT', 'Accepted'
        REJECTED = 'RJT', 'Rejected'

    date_added = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    other_titles = models.CharField(max_length=20)
    connect = models.CharField(blank=True, null=True)
    add_time = models.DateTimeField()
    winter = models.CharField(blank=True, null=True)
    summer = models.CharField(blank=True, null=True)
    autumn = models.CharField(blank=True, null=True)
    spring = models.CharField(blank=True, null=True)
    user = models.ForeignKey(to='User',
                             on_delete=models.CASCADE,
                             related_name='pereval')
    coords = models.OneToOneField(to='Coords',
                                  on_delete=models.CASCADE,
                                  related_name='pereval')
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.NEW)


class User(models.Model):
    class Meta:
        db_table = 'users'

    name = models.CharField(max_length=30)
    fam = models.CharField(max_length=30)
    otc = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)


class Coords(models.Model):
    class Meta:
        db_table = 'coords'

    latitude = models.DecimalField(max_digits=6, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    height = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])


class Images(models.Model):
    class Meta:
        db_table = 'images'

    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150)
    data = models.CharField()
    # img = models.BinaryField()
    pereval = models.ForeignKey(to='PerevalAdded',
                                on_delete=models.CASCADE,
                                related_name='images')


class PerevalAreas(models.Model):
    class Meta:
        db_table = 'pereval_areas'

    id_parent = models.ForeignKey(to='PerevalAreas',
                                  on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
