from django import forms
from .models import Review

# class ReviewForm(forms.Form) :
#     user_name = forms.CharField(label="Your Name" ,  max_length=100 , error_messages= {
#         "required" : "Please enter your name ,  it should not be blank",
#         "max_length" : "Enter a shorter name"
#     })
    
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    
#     rating = forms.IntegerField(label="Your Rating", max_value=5 , min_value=1)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name" : "Your Name",
            "review_text" : "Your Feedback",
            "rating" : "Your Rating"
        }
        error_messages = {
            "user_name" : {
                "required" : "Please enter your name ,  it should not be blank",
                "max_length" : "Enter a short name"
            }
        }