from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'core'

urlpatterns = [
    path('book/create', views.create_book),
    path('book/read', views.read_book),
    path('book/update/<id>', views.update_book),
    path('book/delete/<id>', views.delete_book),
    path('book/detail/<id>', views.detail_book),
    path('login', views.login_user),
    path('logout/', views.logout_user),
    path('create/user', views.create_user),
    path('', RedirectView.as_view(url='book/read'))
]
