from django.shortcuts import render
from django.http import HttpResponse
# from .models import ToDoList, Item
from django.contrib import messages
from .models import ContactProfile, Portfolio, Blog, Testimonial, Certificate
from django.views import generic, View
from . forms import ContactForm
import os
from django.http import FileResponse
from django.conf import settings



class FoodScienceView(generic.TemplateView):
    template_name = "ingosapp/food_science.html"

class FoodAppView(generic.TemplateView):
    template_name = "calculator/food_app.html"

class DownloadCVView(View):
    def get(self, request, *args, **kwargs):
        cv_file_path = os.path.join(settings.MEDIA_ROOT, 'cv', 'Garsvaite_cv_es.pdf')
        response = FileResponse(open(cv_file_path, 'rb'))
        return response

class IndexView(generic.TemplateView):
    template_name = "ingosapp/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context

class ContactView(generic.FormView):
    template_name = "ingosapp/index.html"
    form_class = ContactForm
    success_url = "/"

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
                message_text=form.cleaned_data['message']
        )
            message.success(self.request, "Thank you. We will be in touch.")
            return super().form_valid(form)
        else:
            form = ContactForm()
            return render(request, self.template_name, {'form': form})

class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "ingosapp/portfolio.html"
    paginate_by = 10

    def get_querryset(self):
        return super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = "ingosapp/portfolio-detail.html"

class BlogView(generic.ListView):
    model = Blog
    template_name = "ingosapp/blog.html"
    paginate_by = 10

    def get_querryset(self):
        return super().get_queryset().filter(is_active=True)

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "ingosapp/blog-detail.html"
#
# def home(response):
#     return render(response, "ingosapp/home.html", {})
#
# def author(response):
#     return render(response, "ingosapp/author.html", {})
#
# def foodscience(response):
#     return render(response, "ingosapp/foodscience.html", {})
#
# def foodapp(response):
#     return render(response, "ingosapp/foodapp.html", {})

# def index(response, id):
#     ls = ToDoList.objects.get(id=id)
#     item = ls.item_set.get(id=id)
#     return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.pavadinimas, str(item.tekstas)))


# Create your views here.
