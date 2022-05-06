from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail.as_view(), name='detail'),
    path('profile/', views.profile, name='profile'),
    path('employer/', views.employer, name='employer'),
    path('settings/', views.settings, name='settings'),
    path('settings/employer/', views.settingsEmployer, name='settings-employer'),
    path('posting/create/', views.createPosting, name='create-posting'),
    path('posting/delete/<int:pk>/', views.deletePosting, name='delete-posting'),
    path('posting/edit/<int:pk>/', views.editPosting, name='edit-posting'),
    path('apply/<int:pk>/', views.apply, name='apply'),
    path('postings/<slug:slug>/', views.queryPostings, name='query-postings'),
    # path('profile/<int:pk>/', views.profile, name='profile'),
    path('', views.PostingsListView, name='posting-list'),
] 