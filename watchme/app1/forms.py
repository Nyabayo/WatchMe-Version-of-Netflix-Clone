from django.forms import ModelForm
from app1.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['uuid']