from django.shortcuts import render , HttpResponse
from .models import Post
from django.db.models import Q
# Create your views here.
def home(request):
    all_data = Post.objects.all()

    return render(request, 'firstapp/home.html', {'all_data': all_data})
def post_detail(request, id):
    single_post = Post.objects.get(id=id)
    return render(request, 'firstapp/post-detail.html', {'single_data': single_post})

def login(request):
    return render(request, 'firstapp/login.html')

def about(request):
    single_post = Post.objects.get(id=1)
    return render(request, 'firstapp/about.html', {'single_data': single_post})

def table(request):
    table_data = Post.objects.all()
    return render(request, 'firstapp/table.html', {'data': table_data})

def search(request):
    search_input = request.GET.get('q')
    if search_input:
        all_data = Post.objects.filter(Q(title__icontains=search_input) | Q(body__icontains=search_input))

    return render(request, 'firstapp/search.html', {'my_data': all_data})

def chart(request):
    thisdata = [15, 10, 25, 12, 8, 30]
    return render(request, 'firstapp/chart.html', {'data':thisdata})