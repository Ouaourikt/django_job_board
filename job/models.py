from django.db import models


JOBE_TYPE = (
    ('Full time','Full time'),
    ('Part time','Part time')
)
# Create your models here.
class job(models.Model): #table
    title = models.CharField(max_length=100) #column
    #location 
    job_type = models.CharField(max_length=15,choices=JOBE_TYPE)
    descriptione = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1) #Number
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
