from django.contrib import admin
from .models import Company
from .models import QnA
# Register your models here.

admin.site.register(QnA)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['company']
 
admin.site.register(Company,CompanyAdmin)
