from django.contrib import admin

from .models import Category,Occupation,Job,JobCollaborator,User
# Register your models here.



class AdminCategory(Category):
    pass

admin.site.register(Category)



class AdminOccupation(Occupation):
    pass

admin.site.register(Occupation)


class AdminJob(Job):
    pass

admin.site.register(Job)



class AdminJobCollaborator(JobCollaborator):
    pass
admin.site.register(JobCollaborator)


# class AdminUser(User):
#     pass

# admin.site.register(User)