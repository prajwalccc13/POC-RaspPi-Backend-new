from datetime import datetime
from secrets import choice
from django.db import models
from django.contrib.auth.models import User

class RawImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='prediction_images')

    def __str__(self) -> str:
        return f'{self.id} - {self.user}'


class RawImageMobile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='prediction_images')

    # def __str__(self) -> str:
    #     return f'{self.id} - {self.user}'
    


class Cure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=False)
    
    def __str__(self) -> str:
        return f'{self.name}'


class Disease(models.Model):
    ALTERNARIA_LEAF_SPOT = 'ALF'
    BLACK_ROT = 'BR'
    CABBAGE_APHID = 'CA'
    CABBAGE_LOOPER = 'CL'
    HEALTHY_LEAF = 'HL'
    DISEASE_CHOICES = [
        (ALTERNARIA_LEAF_SPOT, 'Alternaria Leaf Spot'),
        (CABBAGE_APHID, 'Cabbage Aphid'),
        (CABBAGE_LOOPER, 'Cabbage Looper'),
        (BLACK_ROT, 'Black Rot'),
        (HEALTHY_LEAF, 'Heathy Leaf')
    ]
    name = models.CharField(
        max_length=3,
        choices=DISEASE_CHOICES,
        default=ALTERNARIA_LEAF_SPOT,
        unique=True
    )

    description = models.TextField(blank=False, null=False)
    
    LOW = 0
    MINOR = 1
    MODERATE = 2
    HIGH = 3
    CRITICAL = 4
    SEVERITY_CHOICES = (
        (LOW, 'Low'),
        (MINOR, 'Minor'),
        (MODERATE, 'Moderate'),
        (HIGH, 'High'),
        (CRITICAL, 'Critical'),
    )
    severity = models.IntegerField(
        choices=SEVERITY_CHOICES,
        default=LOW
    )
    cure = models.ForeignKey(Cure, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    raw_image = models.ForeignKey(RawImage, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    datetime = models.DateTimeField (auto_now_add=True, blank = True)

    def __str__(self) -> str:
        return f'{self.user} - {self.disease}'

class ReportMobile(models.Model):
    raw_image = models.ForeignKey(RawImageMobile, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    datetime = models.DateTimeField (auto_now_add=True, blank = True)

    # def __str__(self) -> str:
    #     return f'{self.user} - {self.disease}'
