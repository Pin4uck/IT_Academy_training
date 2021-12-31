from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


class NotesListView(ListView):
    paginate_by = 2
    model = Notes
    template_name = 'notebook/index.html'
    context_object_name = 'notes'


def about(request):
    return render(request, 'notebook/about.html')


def select(request):
    return render(request, 'notebook/select.html')


def create(request):
    error = ''
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('n_home')
        else:
            error = 'Форма была неверной'

    form = NotesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'notebook/create.html', data)


class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notebook/note.html'
    context_object_name = 'note'


class NotesUpdateView(UpdateView):
    model = Notes
    template_name = 'notebook/update.html'

    form_class = NotesForm


class NotesDeleteView(DeleteView):
    model = Notes
    template_name = 'notebook/delete.html'
    success_url = '/notebook'
