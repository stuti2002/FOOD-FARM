from django.forms import ModelForm,forms
from django.forms.models import ALL_FIELDS
from .models import Order
import datetime
    
    
class NewOrder(ModelForm):  
    class Meta:
        model = Order
        fields = ['Your_Name','Phone_Number','Table_Number','Item_name','Total_Item', 'Address']
