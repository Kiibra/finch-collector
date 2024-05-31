from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finch_index, name='finch-index'),
  path('finches/<int:finch_id>', views.finch_detail, name='finch-detail'),
  # new route used to show a form and create a finch
  path('finchess/create/', views.FinchCreate.as_view(), name='finch-create'),
    # Add the new routes below
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch-update'),
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch-delete'),
  path('finches/<int:finch_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
  # associate a toy with a finch (M:M)
  path('finches/<int:finch_id>/assoc-toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
]