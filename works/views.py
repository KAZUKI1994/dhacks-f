from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.template import RequestContext, loader

from django.templatetags.static import static
from django.views.generic.edit import FormView
from django.forms.models import modelformset_factory
from .models import Works, WorksForm
from .forms import ContactForm
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, requires_csrf_token

from .models import Works
from .forms import UserForm



from django.core.mail import send_mail
import json
# Create your views here.
# トップ画面


class IndexView(generic.ListView):
    template_name = "works/index.html"
    # get_template_names="base.html"
    context_object_name = "new_archieve_list"
    #############

    icon_images = {
        0: static("images/img0.png"),
        1: static("images/img1.png"),
        2: static("images/img2.png"),
        3: static("images/img3.png"),
        4: static("images/img4.png"),
    }

    def get_queryset(self):
        return Works.objects.order_by('dead_line')[:10]

# バイト詳細情報画面


class DetailView(generic.DetailView):
	model = Works
	template_name = "works/detail.html"
	slug_url_kwarg = 'detail'

#新規登録画面
def register(request):
	return render(request, 'works/register.html')


#ログイン画面
def login(request):
	return render(request, 'works/login.html')

# バイトフォーム画面
@csrf_protect
def jobform(request):
    JobFormSet = modelformset_factory(Works, fields="__all__")
    if request.method == "POST":
        formset = JobFormSet(request.POST, request.FILES)
        if formset.is_valid():
            #mail
            data = request.POST
            send_mail('here','投稿できました。','shinjimadoshisha@gmail.com',[data.__getitem__('form-0-pub_mail'),], fail_silently=False)

            formset.save()
    else:
        formset = JobFormSet()
        ctxt = RequestContext(request, {})
        return render_to_response("works/jobform.html", {"formset": formset}, ctxt)
# バイトフォーム画面
# class jobform(View):


def userform(request):
    form = UserForm()

    return render(request, 'works/jobform.html', {'form': form})
