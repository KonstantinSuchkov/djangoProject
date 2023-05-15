from django import forms
from authapp.models import ClientUser
from authapp.forms import ClientUserEditForm
from mainapp.models import ListOfKindergarden
from mainapp.models import Accommodation


# Форма редактирования параметров пользователя
class ClientUserAdminEditForm(ClientUserEditForm):
    class Meta:
        model = ClientUser
        fields = '__all__'


# Форма редактирования параметров стран
class ListOfKindergardenEditForm(forms.ModelForm):
    class Meta:
        model = ListOfKindergarden
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


# Форма редактирования параметров услуг компании
class AccommodationEditForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
