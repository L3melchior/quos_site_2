from django.contrib import admin
from .models import Profile, Student, Students_class, RequestQR


# Первая часть

##Отображение и редактирование связанных моделей через другую связанную модель (Действительно только для ForeginKey OneToMany)
class StudentInline(admin.TabularInline):
    model = Student

class ProfileInline(admin.TabularInline):
    model = Profile

##Отображение и редактирование связанных моделей через другую связанную модель (Действительно только для ManyToMany)
class MembershipInline(admin.TabularInline):
    model = Profile.students.through
    max_num = 3


# Вторая часть
class Students_classAdmin(admin.ModelAdmin):
    inlines = [
        StudentInline,
    ]

class ProfileAdmin(admin.ModelAdmin):
    #Сортировка
    list_display = ["user","access"]
    ##Отображение и редактирование связанных моделей внутри модели
    inlines = [
        MembershipInline,
    ]

class StudentAdmin(admin.ModelAdmin):
    #Сортировка
    list_display = ["surname", "name", "students_class", ]
    ##Отображение и редактирование связанных моделей внутри модели
    inlines = [
        MembershipInline,
    ]


#Регистрация моделей
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Students_class, Students_classAdmin)
admin.site.register(RequestQR)