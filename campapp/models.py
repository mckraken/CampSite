from django.db import models

# Create your models here.

class CampTeam(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Camper(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team = models.ForeignKey(CampTeam, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Activity(models.Model):
    name = models.CharField(max_length=30)
    # time = models.DateTimeField(null=True)
    max_points = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class TeamScheduledActivity(models.Model):
    time = models.DateTimeField(null=True)
    team = models.ForeignKey(CampTeam, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    points = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.activity.name} {self.team.name}'

class CamperActivity(models.Model):
    camper = models.ForeignKey(Camper, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    points = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.camper.first_name} {self.camper.last_name}, {self.activity.name}'
