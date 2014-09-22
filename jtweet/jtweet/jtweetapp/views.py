
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.

def index(request):
    return render_to_response('jtweetapp/index.html',
        {},
                              context_instance=RequestContext(request))


def followers(request):
    user = request.user
    return render_to_response('jtweetapp/followers.html',
                              {'followers': user.followers.all()},
                              context_instance=RequestContext(request))