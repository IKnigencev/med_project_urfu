from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from main.forms import CreatePredict, InputResult, PatientForm
from main.models import HistoryUser, Patient, VKResult
from main.utils import get_predict_on_image


def index(request):
    """Главная страница."""
    return render(request, 'main/index.html')


def all_patient(request):
    patients = request.user.patients.all()

    context = {
        'page_obj': patients
    }
    return render(request, 'main/all_patient.html', context)


def profile(request, slug):
    """Страница со списком.

    Исполльзуется для отображения пациентов.
    """

    patient = get_object_or_404(Patient, name=slug)

    res_vkr = patient.patient_res.all()

    context = {
        'patient': patient,
        'res_vkr': res_vkr
    }
    return render(request, 'main/profile.html', context)


def predictImage(request):
    """Загрузка изображения."""
    results = HistoryUser.objects.select_related('author').all()
    form = CreatePredict(
        request.POST or None,
        files=request.FILES or None
    )
    context = {
        'form': form,
        'results': results
    }
    if form.is_valid():
        testImage = form.cleaned_data['image']
        perc = get_predict_on_image(testImage)

        post = form.save(commit=False)
        post.author = request.user
        post.result = perc
        post.save()

    return render(request, 'main/result.html', context)


def create_patient(request):
    """Добавление пациента"""

    form = PatientForm(request.POST or None)

    if form.is_valid():
        patient = form.save(commit=False)
        patient.author = request.user

        patient.save()

        return redirect('main:all')

    context = {
        'form': form
    }
    return render(request, 'main/form_patient.html', context)


def update_patient(request, patient_id):
    res = get_object_or_404(Patient, id=patient_id)

    if request.user != res.author:
        return redirect('main:all')

    form = PatientForm(request.POST or None, instance=res)

    if form.is_valid():
        slug = form.cleaned_data['name']
        form.save()
        return redirect('main:profile', slug)

    is_edit = True
    context = {
        'form': form,
        'is_edit': is_edit
    }
    return render(request, 'main/form_patient.html', context)


def create_vkr(request, slug):

    patient = get_object_or_404(Patient, name=slug)

    if patient.author != request.user:
        return redirect('main:profile', slug)

    form = InputResult(request.POST or None)

    if form.is_valid():
        vkr = form.save(commit=False)
        vkr.patient = patient

        vkr.save()

        return redirect('main:profile', slug)

    context = {
        'form': form,
        'slug': slug
    }
    return render(request, 'main/form_vkr.html', context)


def update_vkr(request, slug, vkr_id):
    vkr = get_object_or_404(VKResult, id=vkr_id)

    if vkr.patient.author != request.user:
        return redirect('main:profile', slug)

    form = InputResult(request.POST or None, instance=vkr)

    if form.is_valid():
        form.save()

        return redirect('main:profile', slug)

    is_edit = True
    context = {
        'is_edit': is_edit,
        'form': form,
        'slug': slug,
        'id': vkr_id
    }
    return render(request, 'main/form_vkr.html', context)


class SearchResultsView(ListView):
    model = Patient
    template_name = 'main/search_results.html'
    queryset = Patient.objects.all()
