
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Row
from crispy_forms.layout import Column




    


class CustomForm(forms.Form):
    name = forms.CharField(required=None)
    email = forms.EmailField(required=None)
    mobile = forms.IntegerField(required=None)
    address = forms.CharField(required=None)
    exeperice_1 = forms.CharField(required=None)
    exeperice_2 = forms.CharField(required=None)
    Job_Description = forms.CharField(widget=forms.Textarea,required=None)
    Project_Info = forms.CharField(widget=forms.Textarea,required=None)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = ' container justify-content-center '
        self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-5  mb-10'),
			),
			Row(
				Column('email', css_class='form-group col-md-5  mb-10'),
			),
			Row(
				Column('mobile', css_class='form-group col-md-5  mb-10'),
			),
			Row(
				Column('address', css_class='form-group col-md-5  mb-10'),
			),
			Row(
				Column('exeperice_1', css_class='form-group col-md-5  mb-10'),
						),	
			Row(
				Column('exeperice_2', css_class='form-group col-md-5  mb-10'),
						),
			Row(
				Column('Job_Description', css_class='form-group col-md-5  mb-10'),
						),
   				
			Row(
				Column('Project_Info', css_class='form-group col-md-5  mb-10'),
						),
			Submit('submit','Submit',css_class="btn-success")
			
		)
        
  