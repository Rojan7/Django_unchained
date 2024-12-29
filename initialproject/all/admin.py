from django.contrib import admin
from .models import Chaivariety,Chai_Review,Store,Chai_certificate

class ChaiReviewInline(admin.TabularInline):
    model = Chai_Review
    extra = 2

class ChaivarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_variety',)
class Chai_certificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'issued_date', 'validity_date')


# Register your models here.
admin.site.register(Chaivariety,ChaivarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Chai_certificate,Chai_certificateAdmin)

