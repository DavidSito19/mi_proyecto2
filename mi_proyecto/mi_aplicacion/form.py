from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Row, Column


from mi_aplicacion.models import Escuela, Maestro

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        fields = ["nombre", "siglas"]

class MaestroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        action_type = kwargs.pop('action_type', 'create')
        super(MaestroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        if action_type == 'delete':
            button_text = 'Borrar'
        elif action_type == 'edit':
            button_text = 'Actualizar'
        else:
            button_text = 'Guardar'
        
        self.helper.layout = Layout(
            Row(
                Column(Field('nombre'), css_class='form-group col-md-4 mb-0'),
                Column(Field('sexo'), css_class='form-group col-md-4 mb-0'),
                Column(Field('fecha_nacimiento'), css_class='form-group col-md-4 mb-0'),
                
                css_class='form-row'
            ),
            Row(
                Column(Field('escuela'), css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', button_text)
        )
    class Meta:
        model = Maestro
        fields = ["nombre", "escuela", "sexo", "fecha_nacimiento"]
        labels = {
            "nombre": "Nombre del maestro",
            "escuela": "Escuela a la que pertenece",
            "sexo": "Sexo del maestro",
            "fecha_nacimiento": "Fecha de nacimiento del maestro",
        }
        widget = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})

        }