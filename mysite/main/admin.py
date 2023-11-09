from django.contrib import admin
from .models import Company
from .models import QnA
from .models import Question_Answer
# Register your models here.

admin.site.register(QnA)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['company']
 
admin.site.register(Company,CompanyAdmin)

admin.site.register(Question_Answer)