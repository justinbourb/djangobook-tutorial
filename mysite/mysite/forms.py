from django import forms
'''Django’s form system automatically looks for any method whose name starts
with clean_ and ends with the name of a field. If any such method exists,
it’s called during validation. Specifically, the clean_message() method will
be called after the default validation logic for a given field (in this case,
the validation logic for a required CharField). Because the field data has
already been partially processed, we pull it out of self.cleaned_data.'''
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=250)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Your message is too short, please enter more text.")
        return message
