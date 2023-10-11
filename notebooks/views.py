from django.shortcuts import render
from django.views import generic
from nbconvert import HTMLExporter

# Create your views here.

class TheBestView(generic.TemplateView):
    template_name = "notebooks/notebook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notebook_filename = 'notebooks/jupyter/thebest.ipynb'
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_file(open(notebook_filename, 'rb'))

        context['title'] = 'Finding out the best fruit or veggie out there!'
        context['jupyter_html'] = body

        return context
class MgView(generic.TemplateView):
    template_name = "notebooks/notebook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notebook_filename = 'notebooks/jupyter/magnesium.ipynb'
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_file(open(notebook_filename, 'rb'))

        context['title'] = 'Magnesium in fruits and vegetables:'
        context['jupyter_html'] = body

        return context

class FaView(generic.TemplateView):
    template_name = "notebooks/notebook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notebook_filename = 'notebooks/jupyter/folic_acid.ipynb'
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_file(open(notebook_filename, 'rb'))

        context['title'] = 'Folic acid in fruits and vegetables:'
        context['jupyter_html'] = body

        return context

class PView(generic.TemplateView):
    template_name = "notebooks/notebook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notebook_filename = 'notebooks/jupyter/phosphor.ipynb'
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_file(open(notebook_filename, 'rb'))

        context['title'] = 'Phosphor in fruits and vegetables:'
        context['jupyter_html'] = body

        return context

class VitAView(generic.TemplateView):
    template_name = "notebooks/notebook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notebook_filename = 'notebooks/jupyter/vitamin_a.ipynb'
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_file(open(notebook_filename, 'rb'))

        context['title'] = 'Vitamin A in fruits and vegetables:'
        context['jupyter_html'] = body

        return context

class VitCView(generic.TemplateView):
    template_name = "notebooks/notebook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notebook_filename = 'notebooks/jupyter/vitamin_c.ipynb'
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_file(open(notebook_filename, 'rb'))

        context['title'] = 'Vitamin C in fruits and vegetables:'
        context['jupyter_html'] = body

        return context

class VitEView(generic.TemplateView):
    template_name = "notebooks/notebook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notebook_filename = 'notebooks/jupyter/vitamin_e.ipynb'
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_file(open(notebook_filename, 'rb'))

        context['title'] = 'Vitamin E in fruits and vegetables:'
        context['jupyter_html'] = body

        return context

class ZnView(generic.TemplateView):
    template_name = "notebooks/notebook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notebook_filename = 'notebooks/jupyter/zinc.ipynb'
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_file(open(notebook_filename, 'rb'))

        context['title'] = 'Zinc in fruits and vegetables:'
        context['jupyter_html'] = body

        return context

class FiberView(generic.TemplateView):
    template_name = "notebooks/notebook.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        notebook_filename = 'notebooks/jupyter/Foodscience.ipynb'
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_file(open(notebook_filename, 'rb'))

        context['title'] = 'Analysis of fiber in different food groups'
        context['jupyter_html'] = body

        return context