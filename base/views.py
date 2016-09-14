from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
    entry_point = reverse('lessons_index')

    return HttpResponseRedirect(entry_point)
