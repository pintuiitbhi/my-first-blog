from django.shortcuts import render,redirect
from .models import Document
from .forms import DocumentForm

# Create your views here.
def simple_upload(request):
    if request.method == 'POST':
        form1 = DocumentForm(request.POST or None,request.FILES or None)
        if form1.is_valid():
            form1.save()
            return redirect('post_list') #sends to a view defined in any App
    else:
        form1 = DocumentForm()
    return render(request, 'simple_upload.html', {
        'form1': form1
    })

