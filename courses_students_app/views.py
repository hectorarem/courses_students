from django.http import HttpResponseRedirect


def home_render(request):
    return HttpResponseRedirect('/admin')
