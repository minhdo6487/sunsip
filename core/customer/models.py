from django.db import models
import datetime

# from core.checkin.models import create_checkin
'''
    Customer Name: str(255)
    GST Registered No: str(32)
    UEN/ACRA: str(32)
    Postal Code: int
    Address: str(255)
    Country: dropdown list (Singapore, Malaysia, Indonesia, Australia, Vietnam, Cambodia, Thailand, Phillipines)
    Customer type: dropdown list (Residential, Commercial, Industrial, Governmental, N/A)
'''
SG = 'INGAPORE'
MY = 'MALAYSIA'
ID = 'INDONESIA'
AU = 'AUSTRALIA'
VN = 'VIETNAM'
KH = 'CAMBODIA'
TH = 'THAILAND'
PH = 'PHILLIPINES'

COUNTRY_LIST = (
    (SG, 'INGAPORE'),
    (MY, 'MALAYSIA'),
    (ID, 'INDONESIA'),
    (AU, 'AUSTRALIA'),
    (VN, 'VIETNAM'),
    (KH, 'CAMBODIA'),
    (TH, 'THAILAND'),
    (PH, 'PHILLIPINES'),
)

RES = '1'
COM = '2'
IND = '3'
GOV = '4'
OTHER = '5'
CUSTOMER_TYPE = (
    (RES, 'RESIDENTIAL'),
    (COM, 'COMMERCIAL'),
    (IND, 'INDUSTRIAL'),
    (GOV, 'GOVERNMENTAL'),
    (OTHER, 'N/A')
)

class Customer(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    gst_registered_no = models.CharField(max_length=100)
    uen_acra = models.IntegerField()
    postal_code = models.IntegerField()
    address = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, choices=COUNTRY_LIST, default=VN, null=False, blank=False)
    cus_type = models.CharField(max_length=100, choices=CUSTOMER_TYPE, default=OTHER, null=False, blank=False)
    created = models.DateTimeField(null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.today()
        return super(Customer, self).save(*args, **kwargs)
    '''
        should add time create and modify
    '''
    def __str__(self):
        return self.name
