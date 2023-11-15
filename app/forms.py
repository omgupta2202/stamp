from django import forms
from .models import *



class SearchForm(forms.Form):
    registration_no = forms.CharField(label='Registration Number', max_length=100)
    date_of_registration = forms.DateField(label='Date of Registration')
    buyer_name = forms.CharField(label="Buyer's Name", max_length=100)
    buyer_address = forms.CharField(label="Buyer's Address", widget=forms.Textarea)
    buyer_number = forms.CharField(label="Buyer's Number", max_length=20)
    seller_name = forms.CharField(label="Seller's Name", max_length=100)
    seller_address = forms.CharField(label="Seller's Address", widget=forms.Textarea)
    seller_number = forms.CharField(label="Seller's Number", max_length=20)
    ward_halka = forms.CharField(label='Ward/Patwari Halka', max_length=100)
    halka_name = forms.CharField(label='Ward/Patwari Halka Name', max_length=100)
    property_address = forms.CharField(label='Property Address', widget=forms.Textarea)
    khasra_number = forms.CharField(label='Plot No.', max_length=50)
    north = forms.CharField(label='North', max_length=50)
    south = forms.CharField(label='South', max_length=50)
    east = forms.CharField(label='East', max_length=50)
    west = forms.CharField(label='West', max_length=50)



class CaptchForm(forms.ModelForm):
    class Meta:
        model = Captch
        fields = ['take_captcha']

class CaptchaForm(forms.Form):
    username = forms.CharField(max_length=100)
    captcha = forms.CharField()


# from .forms import SearchForm

# def collect_and_save_data(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             # Process the form data and save it to the database
#             registration = Registration(
#                 registration_no=form.cleaned_data['registration_no'],
#                 date_of_registration=form.cleaned_data['date_of_registration'],
#                 buyer_name=form.cleaned_data['buyer_name'],
#                 # Add other fields as needed
#             )
#             registration.save()
#             return HttpResponse("Data has been collected and saved to the database.")
#     else:
#         form = SearchForm()
#     return render(request, 'data_collection_form.html', {'form': form})
