from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView , DetailView 
from django.views.generic.edit import FormView , CreateView

# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Have a good day!"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
    # def get_queryset(self) :
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt = 4)
    #     return data   
    
class UserReviewView(DetailView):
    template_name = "reviews/user_review.html"
    model = Review













# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
    
#     def form_valid(self, form) :
#         form.save()
#         return super().form_valid(form)
    
    
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
        
#         return render(request, "reviews/review.html", {
#             "form": form
#         })


# class UserReviewView(TemplateView):
#     template_name = "reviews/user_review.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']
#         selected_review = Review.objects.get(pk = review_id)
#         context['review'] = selected_review
#         return context


# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context['reviews'] = reviews
#         return context


# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()

#             # review = Review(
#             #     user_name = form.cleaned_data["user_name"] ,
#             #     review_text = form.cleaned_data["review_text"],
#             #     rating = form.cleaned_data["rating"]
#             # )
#             # review.save()
            
#             return HttpResponseRedirect("/thank-you")
#     else :
#         form = ReviewForm()
#     return render(request, "reviews/review.html", {
#         "form": form
#     })