from .import views
from django.urls import path


app_name = 'food'
urlpatterns = [
    # path('', views.index, name ='index'),
    path('', views.IndexClassView.as_view(), name ='index'),
    # path('<int:item_id>/', views.detail, name ='detail'),
    path('<int:pk>/', views.FoodDetail.as_view(), name ='detail'),
    path('item/', views.item, name = 'item'),
    path('thing/', views.thing, name = 'thing'),

    #add items(Create)
    path('add',views.create_item, name ='create_item'),
    
    #Edit items(Update)
    path('update/<int:id>',views.update_item, name ='update_item'),

    #Delete items
    path('delete/<int:id>',views.delete_item, name ='delete_item'),
]