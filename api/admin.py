from django.contrib import admin
from .models import Project, Category, Expense
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    """ Project Admin Costumizations """
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Expense)