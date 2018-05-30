from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # it is recommended to specifiy each field, but
        # I am not doing that for this example, I am just
        # using the all method.
        #
        # to specifiy fields use
        # fields = ['title', 'nextfield']
        # 
        # or you can use exclude to only exclude a couple
        # exclude = ['title']