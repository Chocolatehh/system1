from functools import wraps
from django.http import HttpResponseRedirect


def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/login/')
        return view_func(request, *args, **kwargs)

    return wrapped_view


