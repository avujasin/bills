import django_filters
from django_filters import DateFilter

from .models import *

class BillFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="payment_date",lookup_expr='gte')
    end_date = DateFilter(field_name="payment_date",lookup_expr='lte')
    class Meta:        
        model = MonthlyBills
        fields = '__all__'
        exclude = ['date_created','user','payment_date']
        
