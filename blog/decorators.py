from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect

# Based on http://passingcuriosity.com/2009/writing-view-decorators-for-django/
def staff_only(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated() and user.is_staff:
                return view_func(request, *args, **kwargs)
            messages.error(request, 'Only staff may view this page. Please login as a staff user.')
            return HttpResponseRedirect(settings.LOGIN_URL)
        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__
        return _view
    if function is None:
        return _dec
    else:
        return _dec(function)