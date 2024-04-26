from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    # path('articles/<slug:slug>/', views.DetailViewPage.as_view(), name="detail"),
    path('articles/', views.ListViewPage.as_view(), name="list"),
    path("category/<int:pk>/", views.category_detail, name="category_detail"),
    path('search/', views.search, name="search"),
    path("articles/<slug:slug>/", views.post_detail, name='detail'),
    path('contactus/', views.ContactUsView.as_view(), name="ContactUS"),
    path('about/', views.about_us, name="about"),
    path('like/<slug:slug>/<int:pk>/', views.like, name='like')
]
