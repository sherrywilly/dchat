from django.contrib import admin
from company.models import Company, Support, Worker
# Register your models here.

admin.site.register(Company)
admin.site.register(Worker)
admin.site.register(Support)
