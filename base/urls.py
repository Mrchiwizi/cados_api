from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoint),
    path('advocates/', views.advocate_list, name="advocates"),
    path('company/', views.company_list),
    path('advocates/<str:username>/', views.advocate_detail),
    # path('advocates/<str:username>/', views.AdvocateDetail.as_view())

]