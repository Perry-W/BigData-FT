from django.http.response import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import TTFF, FtTest
from .models import CALL
from .models import SS

"""
def index(request):
    ftall=FtTest.objects.all()
    return HttpResponse(ftall)
"""

def testdetail(request, ft_id):
    """
    try:
        detail_ft=FT.objects.get(pk=ft_id)
        print('-----here-----')
    except FT.DoesNotExist:
        print('------there----')
        raise Http404("FT does not exist")
    """
    detail_ft = get_object_or_404(FtTest, pk=ft_id)
    business_call=detail_ft.call_set.all()
    business_ss=detail_ft.ss_set.all()
    return render(request, 'Dept/detail.html', {'detail_ft': detail_ft,'business_call':business_call,'business_ss':business_ss})

def ft_index(request):
    ftall=FtTest.objects.all()
    ttffall=TTFF.objects.all()
    context = {'ftall': ftall,'ttffall':ttffall}
    return render(request, 'Dept/index.html', context)

def business_call(request, call_id):
    calls = get_object_or_404(CALL, pk=call_id)
    return render(request, 'Dept/business_call.html',{'calls':calls})

def business_ss(request, ss_id):
    ss=get_object_or_404(SS, pk=ss_id)
    return render(request, 'Dept/business_ss.html',{'ss':ss})

"""
def ttff_index(request):
    ttffall=TTFF.objects.all()
    context = {'ttffall': ttffall}
    return render(request, 'Dept/index.html', context)
"""
def ttff_detail(request, tf_id):
   
    detail_tf = get_object_or_404(TTFF, pk=tf_id)
    
    return render(request, 'Dept/ttff_detail.html', {'detail_tf': detail_tf})

