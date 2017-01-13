from django import forms


class PersonForm(forms.Form):
    id = forms.IntegerField(required=False)
    name = forms.CharField()
    age = forms.IntegerField()
    is_active = forms.Field()
    birthday = forms.DateTimeField()
    status = forms.CharField(required=False)

    def clean_age(self):
        age = self.cleaned_data["age"]
        if not 10 < age < 100:
            raise forms.ValidationError("age must between 10 and 100")
        return age

    def clean_is_active(self):
        return True if self.cleaned_data["is_active"] is True else False
