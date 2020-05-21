from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'core'

urlpatterns = [
    path('ebook/create', views.create_ebook),
    path('book/create', views.create_book),
    #
    path('book/read', views.read_book),
    path('ebook/read', views.read_ebook),
    #
    path('book/update/<id>', views.update_book),
    path('ebook/update/<id>', views.update_ebook),
    #
    path('book/delete/<id>', views.delete_book),
    path('ebook/delete/<id>', views.delete_ebook),
    #
    path('book/detail/<id>', views.detail_book),
    path('ebook/detail/<id>', views.detail_ebook),
    #
    path('book/my/', views.my_book),
    path('login', views.login_user),
    path('logout/', views.logout_user),
    path('create/user', views.create_user),
    path('dev', views.dev),
    path('', RedirectView.as_view(url='book/read'))
]
