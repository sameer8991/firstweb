from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .forms import UserRegisterForm
from .models import Book
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.core.files.storage import FileSystemStorage


# Create your views here.
@login_required
def index(request):
  books=Book.objects.all()
  n=len(books)
  nslides = n//4+ceil((n/4)-(n//4))
  params = {'nslides':nslides, 'range':range(1,nslides),'book':books}
  return  render(request,'books/index.html',params)


def searchMatch(query, item):
	if query in item.book_name.lower() or query in item.author.lower():
		return True
	else:
		return False

@login_required
def search(request):
   query = request.GET.get('search')
   allbooks = []
   catbook = Book.objects.values('category','id')
   cats = {item['category'] for item in catbook }
   for cat in cats:
   		booktemp = Book.objects.filter(category=cat)
   		b = [item for item in booktemp if searchMatch(query, item)]

   		n = len(b)
   		nslides = n//4 +ceil((n/4)-(n//4))
   		if len(b) !=0:
   			allbooks.append([b, range(1,nslides), nslides])
   params = {'allbooks':allbooks, "msg": ""}
   if len(allbooks) == 0 or len(query)<4:
   		params = {'msg': "Book if not found wait sometime"}
   return render(request,'books/search.html' ,params)


def sample(request):

  return render(request, 'books/sample.html')
  
@login_required
def blog(request):
	return render(request, 'books/blog.html')

@login_required
def bookView(request, myid):
  book = Book.objects.filter(id=myid)
  return render(request,'books/bookview.html',{'book':book[0]})

def sign(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'books/sign.html', {'form': form})


def pdf_view(request):
  fs = FileSystemStorage()
  x = [];x.append(fs); print(x)
  filename = 'Thinking_Fast_and_Slow.pdf'

  if fs.exists(filename):
    with fs.open(filename) as pdf:
      response = HttpResponse(pdf, content_type='application/pdf')
      response['Content-Disposition'] = 'inline; filename = Thinking_Fast_and_Slow.pdf'
      return response
  else:
    return HttpResponseNotFound('file not found')
