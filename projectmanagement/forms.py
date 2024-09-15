from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Project, PROJECT_VISIBILITY

# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm



class ProjectCreationForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Enter project title...", "class": "w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"}))
    description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Enter project description (250 char limit)...", "class": "w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"}))
    visibility = forms.ChoiceField(widget=forms.RadioSelect, choices=PROJECT_VISIBILITY)

    class Meta:
        model = Project
        exclude = ('user', 'stars',)




class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",  widget=forms.TextInput(attrs={'class':'flex justify-start mt-3 rounded w-full p-2 text-sm', 'placeholder':'Email Address'}))
    # first_name = forms.CharField(label="", max_length=100)
    # last_name = forms.CharField(label="", max_length=100)
    
    class Meta:
        model = User
        # fields = ("first_name", "last_name", "email", "username", "password1", "password2")
        fields = ("email", "username", "password1", "password2")


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'flex justify-start mt-3 rounded w-full p-2 text-sm'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="flex mt-1 text-start text-xs text-slate-500">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'

        self.fields['password1'].widget.attrs['class'] = 'flex justify-start mt-3 rounded w-full p-2 text-sm'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="ml-6 mt-1 list-disc text-start text-xs text-slate-500"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'flex justify-start mt-3 rounded w-full p-2 text-sm'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="flex mt-1 text-start text-xs text-slate-500">Enter the same password as before, for verification.</span>'
    



    # def clean_email(self):
    #     email = self.cleaned_data['email'].lower()
    #     try:
    #         user = User.objects.get(email=email)
    #     except Exception as e:
    #         return email
    #     raise forms.ValidationError(f'Email {email} is already in use.')
    
    # def clean_username(self):
    #     email = self.cleaned_data['username']
    #     try:
    #         user = User.objects.get(username=username)
    #     except Exception as e:
    #         return username
    #     raise forms.ValidationError(f'Username {usernmae} is already in use.')
