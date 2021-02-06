from django.contrib import admin
from .models import Category, Project, Study, Service, Credit

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class StudyAdmin(admin.ModelAdmin):
    pass

class ServiceAdmin(admin.ModelAdmin):
    pass

class CreditAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Credit, CreditAdmin)