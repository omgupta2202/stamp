# data_collector/models.py
from django.db import models

from django.db import models

class Details(models.Model):
    username = models.CharField(max_length=255, unique=True)  # Set username as unique
    district_registered = models.CharField(max_length=255, verbose_name='District (Where Document Was Registered)')
    district_search = models.CharField(max_length=255, verbose_name='District Being Used for Search')
    search_registered_sampada = models.BooleanField(default=False)
    financial_year = models.CharField(max_length=10, verbose_name='Financial Year')
    from_date = models.DateField(verbose_name='From Date')
    to_date = models.DateField(verbose_name='To Date')
    # district = models.CharField(max_length=255, null=True, blank=True)
    # tehsil = models.CharField(max_length=255, null=True, blank=True)
    # type_of_area = models.CharField(max_length=255, null=True, blank=True)
    # sub_area_type = models.CharField(max_length=255, null=True, blank=True)
    # ward_number_patwari_number = models.CharField(max_length=255, null=True, blank=True)
    # mohalla_colony_name_society_road = models.CharField(max_length=255, null=True, blank=True)
    khasra_number = models.CharField(max_length=255, null=True, blank=True)
    transacting_party_first_name = models.CharField(max_length=255, verbose_name='Transacting Party First Name', blank=True, null=True)
    transacting_party_middle_name = models.CharField(max_length=255, verbose_name='Transacting Party Middle Name', blank=True, null=True)
    transacting_party_last_name = models.CharField(max_length=255, verbose_name='Transacting Party Last Name', blank=True, null=True)
    transacting_party_mother_name = models.CharField(max_length=255, verbose_name='Transacting Party Mother Name', blank=True, null=True)
    transacting_party_father_name = models.CharField(max_length=255, verbose_name='Transacting Party Father Name', blank=True, null=True)
    organization_name = models.CharField(max_length=255, verbose_name='Organization Name', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Check if a record with the same username already exists
        existing_record = Details.objects.filter(username=self.username).first()
        if existing_record:
            # Update the existing record with the new data
            self.id = existing_record.id  # Preserve the existing user's ID
            super(Details, self).save(*args, **kwargs)
            
        else:
            super(Details, self).save(*args, **kwargs)

    def __str__(self):
        return f'Registration {self.id}'


class Registration(models.Model):
    registration_no = models.CharField(max_length=100)
    date_of_registration = models.DateField()
    buyer_name = models.CharField(max_length=200)
    buyer_address = models.CharField(max_length=200)  # Add fields as needed
    buyer_number = models.CharField(max_length=20)
    seller_name = models.CharField(max_length=200)
    seller_address = models.CharField(max_length=200)
    seller_number = models.CharField(max_length=20)
    ward_patwari_halka = models.CharField(max_length=100)
    ward_patwari_halka_name = models.CharField(max_length=100)
    property_address = models.CharField(max_length=200)
    plot_number = models.CharField(max_length=50)
    north = models.CharField(max_length=50)
    south = models.CharField(max_length=50)
    east = models.CharField(max_length=50)
    west = models.CharField(max_length=50)

class Captch(models.Model):
    take_captcha = models.CharField(max_length=200)
    
class District(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.name


class Tehsil(models.Model):
    name = models.CharField(max_length=150)
    state = models.ForeignKey(District, on_delete=models.PROTECT, related_name="tehsil_district")
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.name

class TypeOfArea(models.Model):
    name = models.CharField(max_length=150)
    tehsil = models.ForeignKey(Tehsil, on_delete=models.PROTECT, related_name="typeofarea_tehsil")
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.name

class SubArea(models.Model):
    name = models.CharField(max_length=150)
    typeofarea = models.ForeignKey(TypeOfArea, on_delete=models.PROTECT, related_name="subarea_typeofarea")
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.name

class WardPatwariNumber(models.Model):
    name = models.CharField(max_length=150)
    subarea = models.ForeignKey(SubArea, on_delete=models.PROTECT, related_name="ward_subarea")
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.name
    
    class Meta:
        verbose_name = 'WardPatwariNumber'
        verbose_name_plural = 'WardNumber/PatwariNumber'
    
class SocietyName(models.Model):
    name = models.CharField(max_length=150)
    ward = models.ForeignKey(WardPatwariNumber, on_delete=models.PROTECT, related_name="society_ward")
    is_active = models.BooleanField(default=True)

    def _str_(self):
        return self.name

    class Meta:
        verbose_name = 'SocietyName'
        verbose_name_plural = 'Mohalla/Colony/Society/Road'