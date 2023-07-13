from django import forms
from django.forms import ModelForm
from .models import Property, SiteUser
from django.contrib.auth.forms import UserCreationForm


gender_choices = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Other"),
)


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    picture = forms.FileField(required=False)
    age = forms.CharField()
    gender = forms.ChoiceField(choices=gender_choices)
    phone_number = forms.DecimalField(decimal_places=0, max_digits=10)
    budget = forms.DecimalField(decimal_places=2, max_digits=10)
    cleanliness = forms.IntegerField(label="Rate your cleanliness from 1-10")
    noise_level = forms.IntegerField(label="1-10?")
    has_pet = forms.BooleanField(label='Do you have bike ', required=False)
    smoking = forms.BooleanField(label='Do you Smoke or Drink ?', required=False)
    wc_access = forms.BooleanField(label='Do you love Gaming ?', required=False)
    love_rb = forms.BooleanField(label='Do you love Reading books ?', required=False)

    class Meta:
        model = SiteUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'picture', 'age', 'gender',
                  'phone_number', 'budget', 'cleanliness', 'noise_level', 'smoking', 'has_pet', 'wc_access', 'love_rb']


class UpdateUserForm(ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.CharField()
    gender = forms.ChoiceField(choices=gender_choices)
    phone_number = forms.DecimalField(decimal_places=0, max_digits=10)
    budget = forms.DecimalField(decimal_places=2, max_digits=10)
    cleanliness = forms.IntegerField(label="Rate your cleanliness from 1-10")
    noise_level = forms.IntegerField(label="How loud do you tend to be from 1-10?")
    has_pet = forms.BooleanField(label='D you havr bike ?', required=False)
    smoking = forms.BooleanField(label='Do you Smoke or Drink?', required=False)
    wc_access = forms.BooleanField(label='Do you love gaming ?', required=False)
    love_rb = forms.BooleanField(label='Do you love Reading books ?', required=False)

    class Meta:
        model = SiteUser
        fields = ['username', 'first_name', 'last_name', 'picture', 'age', 'gender',
                  'phone_number', 'budget', 'cleanliness', 'noise_level', 'smoking', 'has_pet', 'wc_access', 'love_rb']


class UpdateUserPic(ModelForm):
    picture = forms.FileField(required=False)

    # class Meta:
    #     model = SiteUser
    #     fields = ['picture']


class PropertyForm(ModelForm):
    property_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Name'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your address'}))
    branch = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your branch'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':
                                                               'Write something about you, '
                                                               'your interests, skills '
                                                               'write what you want in your roommate'}))
    price = forms.DecimalField(label="Budget", decimal_places=2, max_digits=10,
                               widget=forms.TextInput(attrs={'placeholder': 'Rent cost per month'}))
    wc_access = forms.BooleanField(label='Are you vegeterian ?', required=False)
    allows_pets = forms.BooleanField(label='Do you allow pets ?', required=False)
    allows_smoking = forms.BooleanField(label='Do you allow smoking?', required=False)
    love_rb = forms.BooleanField(label='Do you love Reading books ?', required=False)
    have_bike = forms.BooleanField(label='Do you have bike ?', required=False)

    picture = forms.FileField(required=False)

    class Meta:
        model = Property
        fields = ['property_name', 'address', 'description', 'branch', 'picture', 'price', 'cleanliness',
                  'wc_access', 'allows_pets', 'allows_smoking', 'love_rb', 'have_bike']


class UpdatePropertyForm(ModelForm):
    property_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'House Name'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your address'}))
    branch = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your branch'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':
                                                                   'Describe the property, you should '
                                                                   'mention the availability and any '
                                                                   'requirements you may have'}))
    price = forms.DecimalField(label="Budget", decimal_places=2, max_digits=10,
                               widget=forms.TextInput(attrs={'placeholder': 'Rent cost per month'}))
    wc_access = forms.BooleanField(label='Is there wheelchair access?', required=False)
    allows_pets = forms.BooleanField(label='Do you allow pets?', required=False)
    allows_smoking = forms.BooleanField(label='Do you allow smoking?', required=False)
    love_rb = forms.BooleanField(label='Do you love Reading books ?', required=False)
    have_bike = forms.BooleanField(label='Do you have bike ?', required=False)

    class Meta:
        model = Property
        fields = ['property_name', 'address', 'description', 'branch', 'picture', 'price', 'cleanliness',
                  'wc_access', 'allows_pets', 'allows_smoking', 'love_rb', 'have_bike']


class UpdatePropertyPic(ModelForm):
    picture = forms.FileField(required=False)

    class Meta:
        model = Property
        fields = ['picture']
