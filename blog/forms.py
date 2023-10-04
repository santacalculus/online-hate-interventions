from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from blog.models import Profile, Post

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

class EntryForm(forms.Form) :
    new_post = forms.CharField(max_length=2000, 
                               label='Join the Discussion!')

class LoginForm(forms.Form) :
    username = forms.CharField(max_length=20)
    # password = forms.CharField(max_length=200, widget = forms.PasswordInput(), label="Enter your Prolific ID")

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        # password = cleaned_data.get('password')
        user = authenticate(username=username)
        # Confirms that the two password fields match
        if not user:
            raise forms.ValidationError("Invalid Prolific ID")
        # We must return the cleaned data we got from our parent.
        return cleaned_data

class ValueForm(forms.ModelForm):    
    class Meta:
        model = Profile
        fields = ['interests', 'value', 'value_importance', 'catchphrase']
        widgets = {
            'interests': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.HiddenInput(),
            # 'form_value': forms.TextInput(attrs={'class': 'form-control'}),
            'value_importance': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'catchphrase': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['interests'].validators.append(validate_meaningful_response)
    #     self.fields['interests'].validators.append(validate_no_excessive_punctuation)
    #     self.fields['interests'].validators.append(validate_min_length)
    #     self.fields['interests'].validators.append(validate_no_patterns)
    #     self.fields['interests'].validators.append(validate_not_trivial)
    #     self.fields['interests'].validators.append(validate_no_repetitive_characters)
      
    #     self.fields['value_importance'].validators.append(validate_meaningful_response)
    #     self.fields['value_importance'].validators.append(validate_no_excessive_punctuation)
    #     self.fields['value_importance'].validators.append(validate_min_length)
    #     self.fields['value_importance'].validators.append(validate_no_patterns)
    #     self.fields['value_importance'].validators.append(validate_not_trivial)
    #     self.fields['value_importance'].validators.append(validate_no_repetitive_characters)
        

    #     self.fields['catchphrase'].validators.append(validate_meaningful_response)
    #     self.fields['catchphrase'].validators.append(validate_no_excessive_punctuation)
    #     self.fields['catchphrase'].validators.append(validate_min_length)
    #     self.fields['catchphrase'].validators.append(validate_no_patterns)
    #     self.fields['catchphrase'].validators.append(validate_not_trivial)
    #     self.fields['catchphrase'].validators.append(validate_no_repetitive_characters)



class RegisterForm(forms.Form):
    username   = forms.CharField(max_length = 20,
                                 label='Prolific ID')
    

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super().clean()
        print(cleaned_data)
    
        

        # We must return the cleaned data we got from our parent.
        return cleaned_data

    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError(" Prolific ID already exists.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username
