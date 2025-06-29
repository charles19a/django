from django.urls import path
from.import views
urlpatterns=[
    path("add",views.add,name="added"),
    path("succs",views.succ,name="succ"),
    path("cr",views.curd,name="crd"),
    path('od',views.orders,name="order"),
    path('or',views.read,name="ordetails"),
    path('ou/<int:pk>/',views.orupdate,name="orderup"),
    path('del/<int:pk>/',views.delete,name="dele"),
    path('cours',views.course,name="course"),
    path('crrea',views.reead,name="courseread"),
    path('crup/<int:pk>/',views.curupdate,name="courupdate"),
    path('de/<int:pk>/',views.deletee,name="delet"),
    path('imm',views.imupl,name='flip')
    
    

]