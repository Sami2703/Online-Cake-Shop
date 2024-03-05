from django.shortcuts import render,redirect
from django.http import HttpResponse
from AdminApp.models import Cake,Category,UserInfo,MyCart,Accounts,OrderMaster
from datetime import datetime
from django.contrib import messages


def home(request):
    cats = Category.objects.all()
    cakes = Cake.objects.all()
    return render(request,"master.html",{'cats':cats,'cakes':cakes})

def ShowCakes(request,cid):
    cats = Category.objects.all()
    #We need cakes filtered based on category
    #cid is id of selected Category
    #Fetch the object of that category
    cat = Category.objects.get(id=cid)
    cakes = Cake.objects.filter(category = cat)
    return render(request,"master.html",{'cats':cats,'cakes':cakes})


def ViewDetails(request,id):
    cake = Cake.objects.get(id=id)
    cats = Category.objects.all()
    return render(request,"viewdetails.html",{"cake":cake,"cats":cats})

def login(request):
    if(request.method=="GET"):
        return render(request,"Login.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            u1 = UserInfo.objects.get(username=uname,password=pwd)
        except:
            messages.add_message(request, messages.INFO, 'Invalid Credentials')
            return redirect(login)

            #return HttpResponse("Invalid Credentials..")
        else:
            request.session["uname"]=uname
            return redirect(home)
            #return HttpResponse("Login Successful")

def signup(request):
    if(request.method=="GET"):
        return render(request,"SignUp.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        #check if user already exists
        try:
            u1 = UserInfo.objects.get(username=uname)
        except:
            #Create model object
            u1 = UserInfo(uname,pwd)
            u1.save()
            return redirect(home)
        else:
            return HttpResponse("User Already Present")
        

def AddToCart(request):
    if(request.method=="POST"):
        #Check if session is created
        if("uname" in request.session):
            #Add To cart
            qty = request.POST["qty"]
            uname = request.session["uname"]
            cakeid = request.POST["cakeid"]
            cake = Cake.objects.get(id=cakeid)
            user = UserInfo.objects.get(username = uname)
            #First check that item is not a duplicate
            try:
                cart = MyCart.objects.get(user=user,cake=cake)
            except:
                cart = MyCart()
                cart.user = user
                cart.cake = cake
                cart.qty = qty
                cart.save()
                return HttpResponse("Added to Cart..")
            else:
                return HttpResponse("Item already in cart")

        else:
            return redirect(login)


def logout(request):
    request.session.clear()
    return redirect(home)

def ShowAllCartItems(request):
    cats = Category.objects.all()
    user = UserInfo.objects.get(username = request.session["uname"])
    if(request.method == "GET"):        
        items = MyCart.objects.filter(user=user)
        total = 0
        for item in items:
            total += item.qty*item.cake.price
        
        request.session["total"] = total
        return render(request,"ShowAllCartItems.html",{"cats":cats,"items":items})
    else:
        #Check if Update button was clicked or Remove was clicked
        action = request.POST["action"]
        cakeid = request.POST["cakeid"]
        cake = Cake.objects.get(id=cakeid)
        item = MyCart.objects.get(user = user,cake=cake)            
        if(action == "Remove"):
            item.delete()
        elif(action == "Update"):
            qty = request.POST["qty"]
            item.qty = qty
            item.save()
        return redirect(ShowAllCartItems)


def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        #Check for card validity
        try:
            customer_acc = Accounts.objects.get(cardNo=cardno,cvv=cvv,expiry=expiry)
        except:
            return HttpResponse("Invalid card Details")
        else:
            #Perform transaction
            customer_acc.balance -= request.session["total"]
            owner_acc = Accounts.objects.get(cardNo='111',cvv='111',expiry='12/2030')
            owner_acc.balance+=request.session["total"]
            owner_acc.save()
            customer_acc.save()
            #Clear the cart
            order = OrderMaster()
            user = UserInfo.objects.get(username = request.session["uname"])
            items = MyCart.objects.filter(user=user)
            c_name = ""
            for item in items:
                c_name += item.cake.cakename+","
                item.delete()
            #print(c_name)
            order.user = user
            order.cake_details = c_name
            order.total_amount = request.session["total"]
            order.date_of_order = datetime.now()
            order.save()
            return HttpResponse("Payment Successful")

