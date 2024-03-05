
from django.urls import path
from UserApp import views

urlpatterns = [
    path('',views.home),    
    path('ShowCakes/<cid>',views.ShowCakes),
    path('ViewDetails/<id>',views.ViewDetails),
    path('Login',views.login),
    path('SignUp',views.signup),
    path('Logout',views.logout),
    path('AddToCart',views.AddToCart),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('MakePayment',views.MakePayment)

]
