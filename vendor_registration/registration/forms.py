from django import forms
from .models import Vendor

class VendorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        # Optional fields
        self.fields['gst_no'].required = False
        self.fields['website'].required = False
        self.fields['business_description'].required = False
        self.fields['pan_document'].required = False
        self.fields['msme_certificate'].required = False
        self.fields['msme_certificate'].required = False 
        self.fields['registration_certificate'].required = False
        self.fields['bank_details'].required = True
        self.fields['pan_document'].required = True

    class Meta:
        model = Vendor
        fields = [
            'requesting_lakshya_department',
            'vendor_name', 'vendor_type', 'gst_no', 'pan_no', 'company_status', 'state',
            'banking_name', 'bank', 'ifsc', 'account_number', 'address', 'std_code_phone_no',
            'contact_person', 'city', 'contact_person_designation', 'website', 'is_msmse',
            'mobile', 'business_description', 'email', 'pin', 'registration_certificate', 'bank_details','pan_document','msme_certificate',
        ]
        labels = {
            'vendor_name': 'Name of Firm/Company',
            'vendor_type': 'Type of Firm',
            'gst_no': 'GST No',
            'pan_no': 'PAN No',
            'company_status': 'Status of Company',
            'state': 'State',
            'banking_name': 'Vendor Banking Name',
            'bank': 'Vendor Bank',
            'ifsc': 'Vendor IFSC',
            'account_number': 'Vendor Account Number',
            'address': 'Address',
            'std_code_phone_no': 'Business Contact No.',
            'contact_person': 'Name of Contact Person',
            'city': 'City',
            'fax': 'Fax',
            'contact_person_designation': 'Designation of Contact Person',
            'website': 'Website',
            'is_msmse': 'Do you have MSME (Udyam) Registration?',
            'mobile': 'Mobile Number',
            'business_description': 'Brief Description of Business',
            'email': 'Email',
            'pin': 'PIN Code',
            'registration_certificate': 'GST Rgn certificate / Co Incorporation certificate',
            'bank_details': 'Attach any of this - Cancelled cheque/Bank passbook/Account statement',
            'pan_document': 'Upload PAN Document',
            'msme_certificate': 'Upload MSME Certificate',
        }
        widgets = {
            field: forms.TextInput(attrs={'class': 'form-control'}) for field in [
                'vendor_name', 'gst_no', 'pan_no', 'banking_name', 'bank',
                'ifsc', 'account_number', 'std_code_phone_no', 'contact_person',
                'city', 'contact_person_designation', 'mobile', 'pin',
            ]
        }
        widgets.update({
            'requesting_lakshya_department': forms.Select(attrs={'class': 'form-control'}),  # ✅ Add this
            'vendor_type': forms.Select(attrs={'class': 'form-control'}),
            'company_status': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Website URL (Optional)'}),
            'is_msmse': forms.Select(choices=[('Yes', 'Yes'), ('No', 'No')], attrs={'class': 'form-control'}),
            'business_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'registration_certificate': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bank_details': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pan_document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'msme_certificate': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        })
