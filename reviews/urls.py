from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('thank-you', views.ThankYouView.as_view()),
    path('reviews', views.ReviewsListView.as_view()),
    path('reviews/<int:pk>', views.UserReviewView.as_view(),name='reviews'),
]
