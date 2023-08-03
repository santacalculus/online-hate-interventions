from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# class LoginForm(forms.Form) :
#     username = forms.CharField(max_length=20, label=" Enter your Prolific ID")

#     # Customizes form validation for properties that apply to more
#     # than one field.  Overrides the forms.Form.clean function.
#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         # Confirms that the username is already present in the
#         # User model database.
#         # user = User.objects.filter(username__exact=username).exists()
        
#         user = User.objects.filter(username__exact=username).first()

#         if user is not None:
#             # If the user exists, authenticate and return the cleaned data.
#             user = authenticate(username=username)
#             cleaned_data['user'] = user
#         else:
#             # If the user does not exist, create a new User instance.
#             new_user = User.objects.create_user(username=username)
#             cleaned_data['user'] = new_user

#         return cleaned_data



class LoginForm(forms.Form) :
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=200, widget = forms.PasswordInput(), label="Enter your Prolific ID")

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        # Confirms that the two password fields match
        if not user:
            raise forms.ValidationError("Invalid username/password")
        # We must return the cleaned data we got from our parent.
        return cleaned_data




class RegisterForm(forms.Form):
    username   = forms.CharField(max_length = 20,
                                 label='Username')
    password  = forms.CharField(max_length = 200, 
                                 label='Prolific ID', 
                                 widget = forms.PasswordInput())
    confirm_password  = forms.CharField(max_length = 200, 
                                 label='Confirm Prolific ID',  
                                 widget = forms.PasswordInput())

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super().clean()

        # Confirms that the two password fields match
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data

    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username
