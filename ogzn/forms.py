from .models import Feedback, Questions
from django.forms import ModelForm, TextInput


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        # fields = ['feedback_kad_num']
        fields = ['feedback_email', 'feedback_kad_num']
        widgets = {
            'feedback_email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите e-mail'
            }),
            # 2цифры: 2цифры: 7цифр: сколькоТоЦифр
            'feedback_kad_num': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00:00:0000000:000'
            }),
        }


class EditForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['quest_id', 'quest_text', 'quest_comment']
        widgets = {
            'quest_id': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ИД вопроса (например: f1)'
            }),
            'quest_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст вопроса'
            }),
            'quest_comment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пояснение'
            }),
        }
