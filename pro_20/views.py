from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from pro_20.models import customer, products, booking, Payments, Wishlist,Reviews
from django.contrib.auth import authenticate,logout
# Create your views here.
import os


def sign_in(request):
    if request.method == 'POST':
        a = request.POST['First_Name']
        b = request.POST['Last_Name']
        c = request.POST['Email']
        d = request.POST['User_Name']
        e = request.POST['Password']
        z = User(first_name=a, last_name=b, username=d, email=c)
        z.set_password(e)
        z.save()
        q = customer(First_Name=a, Last_Name=b, Email=c, User_Name=d, Password=e)
        q.save()
        return HttpResponse('data successfully saved')
    return render(request, 'usersignin.html')


def home(request):
    return render(request, 'home.html')


def user_views(request):
    q = customer.objects.all()
    return render(request,'views.html',{'p':q})


def user_login(request):
    if request.method == 'POST':
        a = request.POST['User_Name']
        b = request.POST['Password']
        q = authenticate(username=a, password=b)
        request.session['user_id'] = a
        if q is not None and q.is_superuser == 1:
            return redirect(admin_home)
        else:
            m = customer.objects.get(User_Name=a)
            print(m)
            if m.Password == b:
                if q is not None and q.is_superuser == 0:
                    return redirect(user_home)
    return render(request, 'userlogin.html')


def user_home(request):
    return render(request, 'user_home.html')


def admin_home(request):
    return render(request, 'admin_home.html')


def products_add(request):
    if request.method == 'POST':
        a = request.POST['Product_Name']
        b = request.POST['Price']
        c = request.POST['Quantity']
        d = request.FILES['Product_Image']
        print(a,b,c,d)
        q = products(Product_Name=a, Price=b, Quantity=c, Photo=d)
        q.save()

        return HttpResponse('data successfully saved')
    return render(request, 'products.html')


def products_view(request):
    q = products.objects.all()
    return render(request, 'pro_views.html', {'p': q})


def products_edit(request, id1):
    p_id = id1
    q = products.objects.get(id=p_id)
    if request.method == 'POST':
        q.Product_Name = request.POST['Product_Name']
        q.Price = request.POST['Price']
        q.Quantity = request.POST['Quantity']
        if len(request.FILES) != 0:
            if len(q.Photo) > 0:
                os.remove(q.Photo.path)
        q.Photo = request.FILES['Product_Image']

        q.save()
        return HttpResponse('data successfully updated')
    return render(request, 'edit.html', {'p': q})


def products_delete(request,id1):
    p_id = id1
    q = products.objects.get(id=p_id)
    q.delete()
    return HttpResponse('data successfully removed')


def home1(request):
    return render(request, 'home1.html')


def index(request):
    return render(request, 'index.html')


def user_view(request):
    q = products.objects.all()
    return render(request, 'user_view.html', {'p': q})


def order(request,pid,pr):
    price=pr
    uid=request.session['user_id']
    x=products.objects.get(id=pid)

    pr_name=x.Product_Name
    q = booking.objects.all()
    if request.method=='POST':
        qnty=request.POST['Quantity']
        if int(qnty) <= x.Quantity:
            total=int(qnty)*int(price)
            print(pid,uid,pr_name,qnty,total)
            z=booking(Product_Id=pid,User_id=uid,Product_Name=pr_name,Quantity=qnty,Total=total,Status="Pending")
            z.save()
            x.Quantity=int(x.Quantity)-int(qnty)
            x.save()
            return HttpResponse('Order successfully completed')
        else:
            return HttpResponse('<script>alert("insufficient quantity"),window.location="/user_view";</script>')
    return render(request,'booking.html', {'p': q})


def approve(request,oid):
    q=booking.objects.get(id=oid)
    q.Status='Approved'
    q.save()
    return HttpResponse('Order Accepted')


def reject(request,oid):
    q=booking.objects.get(id=oid)
    q.Status='rejected'
    q.save()
    return HttpResponse('Order rejected')


def logt(request):
    logout(request)
    return HttpResponse('<script>alert("logout"),window.location="/user_login";</script>')


def admin_view(request):
    q = booking.objects.all()
    return render(request, 'admin_view.html', {'p': q})


def order_view(request):
    uid=request.session['user_id']
    q = booking.objects.filter(User_id=uid)
    return render(request,'user_view_order.html',{'p':q})


def make_payment(request, id, t):
    b_id = id
    total_amount=t
    if request.method=='POST':
        q=Payments(customer_id=request.session['user_id'],booking_id=b_id,total_amount=total_amount,status='Paid')
        q.save()
        q = booking.objects.get(id=b_id)
        q.Status = "confirm"
        q.save()
        return HttpResponse("Payment success and order confirm")
    return render(request, 'payment.html', {'t': total_amount})


def wishlist(request, id):
    p_id = id
    uid = request.session['user_id']
    q = Wishlist(User_id=uid,Product_Id=p_id,Status='wishlist')
    q.save()
    return HttpResponse("wishlist")


def review(request,id):
    p_id=id
    uid = request.session['user_id']
    if request.method == 'POST':
        review = request.POST['Review']
        q= Reviews(User_id=uid,Product_Id=p_id,Review=review)
        q.save()
        return HttpResponse('<script>alert("review stored"),window.location="/user_home";</script>')
    return render(request, 'reviews.html')





