from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        'vendor_name', 'vendor_type', 'requesting_lakshya_department',
        'pan_no', 'contact_person', 'mobile', 'email'
    )
    search_fields = ('vendor_name', 'pan_no', 'gst_no', 'email')
    list_filter = ('vendor_type', 'requesting_lakshya_department', 'state')
