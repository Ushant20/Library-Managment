from django.contrib import admin
from .models import Student , Payment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'whatsapp',
        'fee_amount',
        'fee_status',
        'joining_date'
    )

    search_fields = (
        'name',
        'whatsapp',
        
    )

    list_filter = (
        'fee_status',
        'joining_date'
    )

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student',
        'amount',
        'payment_date',
    )

    search_fields = (
        'student__name',
    )

    list_filter = (
        'payment_date',
    )