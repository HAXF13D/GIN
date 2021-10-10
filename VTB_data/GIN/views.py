from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic import DetailView
from .datafile import init_file_bd, add_to_datebase, get_all_files, get_all_columns

# Create your views here.

"""def index(request):
    return render(request, 'GIN/index.html')"""

def authorization(request):
    return render(request, 'polls/auth.html')

def about(request):
    return render(request, 'polls/about.html')

def sort(request):
    init_file_bd()
    fs = FileSystemStorage()
    name = ""
    if request.POST:
        try:
            uploaded_file = request.FILES['doc']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            category = "default"
            add_to_datebase(str(name), category, str(request.user))
        except Exception as e:
            print(e)
    return render(request, 'polls/main.html',{'files' :get_all_files() , 'fields' :get_all_columns(), "url" : fs.url(name) })

"""class CategoryDetailView(DetailView):
    model = Categories
    template_name = "polls/category_view.html"
    context_object_name = 'category'
    queryset = Categories.objects.all()
"""

"""def upload(request):
    context = {}
    if request.POST:
        uploaded_file = request.FILES['doc']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        print(name)
        context['url'] = fs.url(name)
    return render(request, 'polls/upload.html', context)"""
