from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout #login
from django.contrib import messages

from django.core.paginator import Paginator

from .decorators import *

from django.contrib.auth.decorators import login_required

from .forms import * #importovanje forms.py
from .filters import BillFilter
from .models import * #models.py
# Create your views here.
import datetime
from django.db.models import Sum


def ime(request, pk):
    return  HttpResponse('Pozdrav ' + pk)


@unauthenticated_user
def registerPage(request):
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                
                messages.success(request, 'Account was created for ' + username)

                return redirect ('login')

        context = {'form':form}
        return render(request, 'account/register.html', context)


@unauthenticated_user
def loginPage(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')
            
        context = {}
        return render(request, 'account/login.html', context)

@login_required(login_url='login')
def logOutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    bills = MonthlyBills.objects.all().filter(user=request.user)
    last_5_bills = bills.order_by('-id')[:5]
    today = datetime.date.today()

    this_year_f = bills.filter(payment_date__year=today.year)
    this_year = this_year_f.count()

    this_month_f = bills.filter(payment_date__month=today.month)
    this_month = this_month_f.count()

    total_bills = bills.count()

    sum_bills = bills.aggregate(total_sum = Sum('price'))

    sum_b_m = this_month_f.aggregate(total_sum = Sum('price'))
    

    sum_b_y = this_year_f.aggregate(total_sum = Sum('price'))
    

    c = Category.objects.all()
    
    context = {'total_bills':total_bills,'bills':bills,'this_year':this_year,'this_month':this_month,'c':c,'last_5_bills':last_5_bills,'sum_bills':sum_bills,'sum_b_y':sum_b_y,'sum_b_m':sum_b_m}

    return render(request, 'account/dashboard.html',context)

@login_required(login_url='login')
def createBill(request):
    
    form = BillForm()

    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            add_bill = form.save(commit=False)
            add_bill.user=request.user
            add_bill.save()
            
            return redirect('home')
    context = {'form':form}
    return render(request, 'account/bill_form.html', context)

@login_required(login_url='login')
def updateBill(request,pk):

    instance_bills = MonthlyBills.objects.get(id=pk)
    form = BillForm(instance=instance_bills)

    if request.method == 'POST':
        form = BillForm(request.POST, instance = instance_bills)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'account/bill_form.html', context)

@login_required(login_url='login')
def deleteBill(request,pk):
    bill = MonthlyBills.objects.get(id=pk)

    if request.method == 'POST':
        bill.delete()
        return redirect('home')
    context = {'bill':bill}
    return render(request, 'account/delete_bill.html', context)

@login_required(login_url='login')
def viewProfile(request):
    
    bills = MonthlyBills.objects.all().filter(user=request.user)
    

    myFilter = BillFilter(request.GET, queryset=bills)
    
    bills = myFilter.qs
    sum_bills = bills.aggregate(total_sum = Sum('price'))
    count_bills = bills.count()

    ##############paginator#########################
    paginator = Paginator(bills, 5) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    ##############paginator#########################
    
    context = {'bills':bills,'sum_bills':sum_bills,'myFilter':myFilter,'count_bills':count_bills,'page_obj':page_obj}
    return render(request, 'account/profile.html', context)

def editProfile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
        
    else:
        form = UserEditForm(instance=request.user)
        context = {'form':form}
        return render(request, 'account/edit_profile.html', context)


