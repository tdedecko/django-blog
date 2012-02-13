from django import forms
from django.contrib.comments.forms import CommentDetailsForm, COMMENT_MAX_LENGTH

class CommentForm(CommentDetailsForm):
    # Below fields are not required
    email = forms.EmailField(label="Email address", required=False)
    name = forms.CharField(label="Name", required=False)
    
    # Removes label
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'comment',}), max_length=COMMENT_MAX_LENGTH)

    # Hide fields that we really don't need.
    hidden_fields = ('email', 'url', 'name')
    def __init__(self, *args, **kwargs):
        for key, field in self.base_fields.iteritems():
            if key in self.hidden_fields:
                field.widget = field.hidden_widget()
        super(CommentForm, self).__init__(*args, **kwargs)
        
    # Name defaults to Anonymous if user is not logged in.
    def get_comment_create_data(self):
        if self.cleaned_data['name'] == '':
            self.cleaned_data['name'] = 'Anonymous'
        data = super(CommentForm, self).get_comment_create_data()
        return data
