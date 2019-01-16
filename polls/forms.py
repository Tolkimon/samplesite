from django.forms import ModelForm
from .models import Question


class QuestionModelsForm(ModelForm):
    class Meta:
        model = Question
        #fields = ['question_text', 'pub_date']
        exclude = ['id']

