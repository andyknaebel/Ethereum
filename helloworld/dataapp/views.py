from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import  BlogForm
from .models import Blog
import sqlite3


def add_blog(request):
    if request.method != "POST":
        form = BlogForm()
        return render(request, 'dataapp/blog_form.html', {'form': form}) 
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
        return redirect('/data/blog/blog/' + str(blog_item.id) + '/')  


        
def add_blog_1(request):
    if request.method != "POST":
        form = BlogForm()
        results = Blog.objects.all()
        args = {'form': form, 'results': results}
        return render(request, 'dataapp/blog_form.html', args) 
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
        return redirect('/data/blog/blog/' + str(blog_item.id) + '/')
     

        
def add_blog(request):
    if request.method != "POST":
        form = BlogForm()
        return render(request, 'dataapp/blog_form.html', {'form': form}) 
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
        return redirect('/data/blog/blog/' + str(blog_item.id) + '/')        




def edit_blog(request, id=None):
    blog_item = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, instance=blog_item)
    if form.is_valid():
        form.save()
        return redirect('/data/blog/blog/' + str(blog_item.id) + '/')
    return render(request, 'dataapp/blog_form.html', {'form': form}) 

def blog(request, id=id):
    blog = Blog.objects.get(id=id)
    return render(request, 'dataapp/blog.html', {'blog': blog})

# This is an example that uses templates
def dataview1(request):
    numbers = [1,2,3,4,5,6]
    name = 'Andy Knaebel'
    title = 'This is the main data view page'
    args = {'myName': name, 'theNumbers': numbers, 'theTitle': title}
    return render(request, 'dataapp/maindatapage.html', args)


#  this is an example of creating an in memory table, saving a data element to it, then 
#  retrieing the data element and passing it to the web page. 
def dataviewx(request):
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")
    c.execute("insert into employees values (:first, :last, :pay)", {'first': 'Andy', 'last': 'Knaebel', 'pay': 50000})        
    c.execute("select * from employees")
    dbValues = c.fetchall()
    for row in dbValues:
        name = row[0]
    numbers = [1,2,3,4,5,6]
    # name = 'Andy Knaebel'
    title = 'This is the main data view page'
    args = {'myName': name, 'theNumbers': numbers, 'theTitle': title}
    return render(request, 'dataapp/maindatapage.html', args)   

#  this is an example of calling directy the Blog table which was created using a model.
#  The django namaing convention is 'appname_modelname' in this case dataapp_Blog
#  to see this view used, change the name to dataview.
def dataview2x(request):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("select * from dataapp_Blog")
    dbValues = c.fetchall()
    for row in dbValues:
        name = row[1]
    numbers = [1,2,3,4,5,6]
    # name = 'Andy Knaebel'
    title = 'This is the main data view page'
    args = {'myName': name, 'theNumbers': numbers, 'theTitle': title}
    return render(request, 'dataapp/maindatapage.html', args) 

# this example pulls objects from the Blog table and displays one on a webpage
# by passing the "args" to the html page.
def dataview(request):
    results = Blog.objects.get(pk=1)
    name = results.title
    numbers = results.pk
    title = results.Description
    # name = 'Andy Knaebel'
    # title = 'This is the main data view page'
    # numbers = [1,2,3,4,5,6]
    args = {'myName': name, 'theNumbers': numbers, 'theTitle': title}
    return render(request, 'dataapp/maindatapage2.html', args) 



# This  one is a simple httpresponse, uncomment to test
#def dataview(request):
#    return HttpResponse('got dataapp view')

   