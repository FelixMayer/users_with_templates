
from django.shortcuts import render, redirect
from users_app.models import User

def index(request):
    users = User.objects.all()

    context = {
        'users': users
    }
    return render(request, 'index.html', context)


def form_submit(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        age = request.POST['age']
    i = User(first_name = fname, last_name = lname, email_address = email, age = age)
    i.save()
    return redirect('/')

def user_delete(request):
    if request.method == 'POST':
        delete = request.POST['delete']
    d = User.objects.get(id=delete)
    d.delete()
    return redirect('/')