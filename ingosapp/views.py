from django.urls import reverse
from .models import ContactProfile, Certificate
from django.views import generic, View
from . forms import ContactForm
import os
from django.http import FileResponse
from django.conf import settings
from django.shortcuts import render, redirect


class FoodScienceView(generic.TemplateView):
    template_name = "ingosapp/food_science.html"

class DownloadCVView(View):
    def get(self, request, *args, **kwargs):
        cv_file_path = os.path.join(settings.MEDIA_ROOT, 'cv', 'Garsvaite_cv_es.pdf')
        response = FileResponse(open(cv_file_path, 'rb'))
        return response

class IndexView(generic.TemplateView):
    template_name = "ingosapp/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        certificates = Certificate.objects.filter(is_active=True)


        context["certificates"] = certificates
        return context


from django.contrib import messages  # Import messages module


class ContactView(View):
    template_name = "ingosapp/index.html"
    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            message = ContactProfile(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            message.save()
            messages.success(request, "Thank you. We will be in touch.")
        else:
            messages.error(request, "There was an error in your submission.")
        return redirect(reverse('ingosapp:contact'))





