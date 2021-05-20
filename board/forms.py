from django.forms import TextInput, ModelForm, Textarea
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


class ManyToManyInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        super(TextInput, self).__init__(*args, **kwargs)

    def value_from_datadict(self, data, files, name):
        print("value_from_datadict inside")
        value = data.get(name)
        if value:
            return value.split(",")


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
            "tags": ManyToManyInput(),
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
