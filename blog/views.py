from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.files.storage import FileSystemStorage



# Create your views here.
def post_list(request):
	posts_list= Post.objects.all()


	paginator =Paginator(posts_list,1)
	page =request.GET.get('page',1)
	try:
		posts =paginator.page(page)
	except PageNotInteger:
		posts=paginator.page(1)
	except EmptyPage:
		posts =paginator.page(paginator.num_pages)

	return render(request,'post_list.html',{'posts':posts})

def post_new(request):
	form=PostForm(request.POST or None,request.FILES or None)
	return render(request,'post_edit.html',{'form':form})








# To upload file using with model( less secure)
# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
    	   
#     return render(request, 'simple_upload.html')

