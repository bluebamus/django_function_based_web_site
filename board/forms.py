# from django.forms import TextInput, ModelForm, Textarea
from django import forms
from .models import Board


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={"required": "Please enter the title."}, max_length=128, label="title"
    )
    contents = forms.CharField(
        error_messages={"required": "Please enter your content."},
        widget=forms.Textarea,
        label="content",
    )
    tags = forms.CharField(required=False, label="tag")


class BoardUpdateForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["title", "contents", "tags"]
        # fields = "__all__"
        labels = {
            "title": ("title"),
            "contents": ("contents"),
            "tags": ("tag"),
        }
        widgets = {
            "contents": forms.Textarea(attrs={"cols": 80, "rows": 20}),
        }
        help_texts = {}
        error_messages = {
            "title": {
                "required": ("Please enter the title."),
            },
            "contents": {
                "required": ("Please enter your content."),
            },
        }
