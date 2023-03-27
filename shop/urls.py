from django import views
from django.urls import path
from .import views


urlpatterns=[
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cart'),
    path('<slug:c_slug>/<slug:product_slug>',views.proddetails,name='details'),
    path('search',views.search,name='search'),

]