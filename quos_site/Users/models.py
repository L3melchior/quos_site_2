from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

###Класс ученика
class Students_class(models.Model):
    class_name = models.CharField(max_length=10)

    def __str__(self):
        return str(str(self.class_name)+" класс")

###Ученик
class Student(models.Model):
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    students_class = models.ForeignKey(Students_class,  on_delete = models.CASCADE, blank=True, null=True, default=None)


    def __str__(self):
        return str(str(self.surname) + ' ' + str(self.name))
    
###class Notification(models.Model):
###    pass
    

###Расширенный стандартный пользователь
class Profile(models.Model):
    access_choise = (
        ("Родитель","Родитель"),
        ("Учитель","Учитель"),   
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access = models.CharField(choices=access_choise,max_length=10, blank=True, default=access_choise[0][0])
    students = models.ManyToManyField(Student, blank=True)
    ###notifications = models.ManyToManyField(Notification, blank=True)
    name_user = models.CharField(max_length=50, blank=True)
    patronymic_user = models.CharField(max_length=50, blank=True)
    surname_user = models.CharField(max_length=50, blank=True)
    students_class = models.ForeignKey(Students_class,  on_delete = models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return str(str(self.user) + f" [{self.access}]")

###Сигналы для создания профиля при создании пользователя
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        is_present = Student.objects.filter(name = "None").exists()
        if is_present:
            print("в наборе есть объекты")
        else:
            print("объекты в наборе отсутствуют")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class RequestQR(models.Model):
    code_request = models.CharField(max_length=50)
    owner_request = models.CharField(max_length=100)
    child_owner = models.CharField(max_length=100)
    child_class = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    entered_at = models.CharField(max_length=100, blank=True, null=True)
    closed_at = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.owner_request
