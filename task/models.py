from django.db import models



class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


class Unit(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker , related_name='worker' , on_delete=models.CASCADE)



class Visit(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    unit = models.ForeignKey(Unit , related_name= 'visits', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return  str(self.date_time)