from django.shortcuts import render, redirect

from .models import Shows

# /shows - GET - method should return a template that displays all the shows in a table


def index(request):
    context = {
        'shows': Shows.objects.all()
    }
    return render(request, 'all_shows.html', context)


# /shows/new- GET - method should return a template containing the form for adding a new TV show
def new(request):
    return render(request, 'add_show.html')


# /shows/create - POST - method should add the show to the database, then redirect to /shows/<id>
def create(request):
    if request.method == 'POST':
        Shows.objects.create(

            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description'],
        )
    return redirect('/')


# /shows/<id> - GET - method should return a template that displays the specific show's information
def show_info(request, show_id):
    context = {
        'show': Shows.objects.get(id=show_id)
    }
    return render(request, "show_info.html", context)


# /shows/<id>/edit - GET - method should return a template that displays a form for editing the TV show with the id specified in the url
def edit(request, show_id):
    this_show = Shows.objects.get(id=show_id)
    context = {
        'show': this_show
        }
    return render(request, 'edit_show.html', context)


# /shows/<id>/update - POST - method should update the specific show in the database, then redirect to /shows/<id>
def update(request, show_id):
    # some code here update specific show in db
    if request.method == 'POST':
        show = Shows.objects.get(id=show_id)
        show.title = request.POST['title']
        show.title = request.POST['title'],
        show.network = request.POST['network'],
        release_date = request.POST['release_date'],
        show.description = request.POST['description'],
    return redirect('/shows/<int:show_id>')


# /shows/<id>/destroy - POST - method should delete the show with the specified id from the database, then redirect to /shows
def destroy(request, show_id):
    # grabs instance of class, by using get the show id
    to_delete = Shows.objects.get(id=show_id)
    #  deletes show w id from db
    to_delete.delete()
    return redirect('/shows')

