from django import forms
from django.contrib.comments.forms import CommentDetailsForm

class CommentForm(CommentDetailsForm):
    email = forms.EmailField(label="Email address", required=False)
    name = forms.CharField(label="Name", required=False)
    
    hidden_fields = ('email', 'url', 'name')
    
    def __init__(self, *args, **kwargs):
        for key, field in self.base_fields.iteritems():
            if key in self.hidden_fields:
                field.widget = field.hidden_widget()
        super(CommentForm, self).__init__(*args, **kwargs)
        
    def get_comment_create_data(self):
        if self.cleaned_data['name'] == '':
            self.cleaned_data['name'] = 'Anonymous'
        data = super(CommentForm, self).get_comment_create_data()
        return data
