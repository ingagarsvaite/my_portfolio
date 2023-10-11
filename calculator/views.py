import random
from django.shortcuts import render
from django.views import View
from .forms import FoodSelectionForm
from .models import FoodItem, RefValue
from django.forms import formset_factory
from .forms import FoodSelectionFormSet


FoodSelectionFormSet = formset_factory(FoodSelectionForm, extra=10)

class FoodCalculateView(View):
    template_name = 'calculator/food_app.html'

    def get(self, request):
        formset = FoodSelectionFormSet()
        return render(request, self.template_name, {'formset': formset})

    def post(self, request):
        formset = FoodSelectionFormSet(request.POST)
        results = []
        colors = ["blue", "red", "green", "pink", "purple", "yellow", "orange", "grey", "mint"]
        data_fiber = []
        data_mg = []
        data_zn = []
        data_p = []
        data_fa = []
        data_vita = []
        data_vitc = []
        data_vite = []
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    food_item = form.cleaned_data['food_item']
                    quantity = form.cleaned_data['quantity']

                    selected_food_item = FoodItem.objects.get(pk=food_item.id)
                    ref_fiber = RefValue.objects.get(element='fiber').ref_value
                    ref_mg = RefValue.objects.get(element='mg').ref_value
                    ref_zn = RefValue.objects.get(element='zn').ref_value
                    # ref_fa = RefValue.objects.get(element='fa').ref_value
                    ref_p = RefValue.objects.get(element='p').ref_value
                    ref_vitA = RefValue.objects.get(element='vit_a').ref_value
                    ref_vitC = RefValue.objects.get(element='vit_c').ref_value
                    ref_vitE = RefValue.objects.get(element='vit_e').ref_value

                    fiber = float(((selected_food_item.fiber_in_g * quantity) / 100 / ref_fiber * 100 if ref_fiber != 0 else 0))
                    mg = float(((selected_food_item.mg_in_mg * quantity) / 100 / ref_mg * 100 if ref_mg != 0 else 0))
                    zn = float(((selected_food_item.zn_in_mg * quantity) / 100 / ref_zn * 100 if ref_zn != 0 else 0))
                    # fa = float(((selected_food_item.fa_in_mcg * quantity) / 100 / ref_fa * 100 if ref_fa != 0 else 0))
                    p = float(((selected_food_item.p_in_mg * quantity) / 100 / ref_p * 100 if ref_p != 0 else 0))
                    vit_a = float(((selected_food_item.vitamin_a_in_mcg * quantity) / 100 / ref_vitA * 100 if ref_vitA != 0 else 0))
                    vit_c = float(((selected_food_item.vitamin_c_in_mg * quantity) / 100 / ref_vitC * 100 if ref_vitC != 0 else 0))
                    vit_e = float(((selected_food_item.vitamin_e_in_mg * quantity) / 100 / ref_vitE * 100 if ref_vitE != 0 else 0))

                    color = random.choice(colors)

                    result = {'food_item': selected_food_item,
                              'fiber': fiber,
                              'mg': mg,
                              'zn': zn,
                              'p': p,
                              'vit_a': vit_a,
                              'vit_c': vit_c,
                              "vit_e": vit_e,
                              "color": color}

                    data_fiber.append(fiber)
                    data_mg.append(mg)
                    data_zn.append(zn)
                    data_p.append(p)
                    # data_fa.append(fa)
                    data_vita.append(vit_a)
                    data_vitc.append(vit_c)
                    data_vite.append(vit_e)

                    results.append(result)

        sum_fiber = sum(data_fiber)
        sum_mg = sum(data_mg)
        sum_zn = sum(data_zn)
        # sum_fa = sum(data_fa)
        sum_p = sum(data_p)
        sum_vita = sum(data_vita)
        sum_vite = sum(data_vite)
        sum_vitc = sum(data_vitc)

        # Pass the sums to the template context
        context = {
            "results" : results,
            'sum_fiber': sum_fiber,
            'sum_mg': sum_mg,
            "sum_zn" : sum_zn,
            # "sum_fa" : sum_fa,
            "sum_p" : sum_p,
            "sum_vita" : sum_vita,
            "sum_vitc": sum_vitc,
            "sum_vite": sum_vite,
            "colors" : colors
        }

        return render(request, 'calculator/food_app_result.html', context)
