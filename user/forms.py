from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "kullanici adi")
    password = forms.CharField(label = "parola",widget = forms.PasswordInput)
    

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label = "Kullanici Adi")
    password = forms.CharField(max_length=20,label = "parola",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label = "parola tekrar",widget = forms.PasswordInput)

    def clean(self):
        
        username = self.cleaned_data.get('usernane')
        confirm = self.cleaned_data.get('confirm')
        password = self.cleaned_data.get('password')

        if password and confirm and password != confirm :
            raise forms.ValidationError("parolalar eslesmiyor.")
        
        values = {
            "username" : username ,
            "password" : password


        }
        return values



            
            
        