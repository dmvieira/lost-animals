from django.shortcuts import render
from forms import PetForm


# Create your views here.
def index(request):
    context = dict(jedi='sou sim')
    return render(request, 'lostpet/index.html', context)


def new(request):
    if request.method == 'POST':
        formset = PetForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = PetForm()
    print formset
    print dir(formset)
    return render(request, 'lostpet/new.html', dict(form=formset))
