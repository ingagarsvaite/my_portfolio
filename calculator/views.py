from django.shortcuts import render
from django.views import View
from .forms import FoodSelectionForm
from .models import FoodItem, RefValue
class FoodCalculateView(View):
    template_name = 'calculator/food_app.html'

    def get(self, request):
        form = FoodSelectionForm()
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        template_name = 'calculator/food_app_result.html'
        form = FoodSelectionForm(request.POST)
        if form.is_valid():
            food_item = form.cleaned_data['food_item']
            quantity = form.cleaned_data['quantity']

            selected_food_item = FoodItem.objects.get(pk=food_item.id)
            ref_fiber = RefValue.objects.get(element='fiber').ref_value
            ref_mg = RefValue.objects.get(element='mg').ref_value
            ref_zn = RefValue.objects.get(element='zn').ref_value
            ref_fa = RefValue.objects.get(element='fa').ref_value
            ref_p = RefValue.objects.get(element='p').ref_value
            ref_vitA = RefValue.objects.get(element='vit_a').ref_value
            ref_vitC = RefValue.objects.get(element='vit_c').ref_value
            ref_vitE = RefValue.objects.get(element='vit_e').ref_value

            fiber = ((selected_food_item.fiber_in_g * quantity) / 100 / ref_fiber * 100 if ref_fiber != 0 else 0)
            mg = ((selected_food_item.mg_in_mg * quantity) / 100 / ref_mg * 100 if ref_mg != 0 else 0)
            zn = ((selected_food_item.zn_in_mg * quantity) / 100 / ref_zn * 100 if ref_zn != 0 else 0)
            fa = ((selected_food_item.fa_in_mcg * quantity) / 100 / ref_fa * 100 if ref_fa != 0 else 0)
            p = ((selected_food_item.p_in_mg * quantity) / 100 / ref_p * 100 if ref_p != 0 else 0)
            vit_a = ((selected_food_item.vitamin_a_in_mcg * quantity) / 100 / ref_vitA * 100 if ref_vitA != 0 else 0)
            vit_c = ((selected_food_item.vitamin_c_in_mg * quantity) / 100 / ref_vitC * 100 if ref_vitC != 0 else 0)
            vit_e = ((selected_food_item.vitamin_e_in_mg * quantity) / 100 / ref_vitE * 100 if ref_vitE != 0 else 0)

            data = [fiber, mg, zn, p, fa, vit_a, vit_c, vit_e]
            labels = ["Fiber", "Magnesium", "Zinc", "Phosphor", "Folic Acid", "Vitamin A", "Vitamin C", "Vitamin E"]
            return render(request, "calculator/food_app_result.html", {'food_item': selected_food_item, 'fiber': fiber,
                                                                       'mg': mg, 'zn': zn, 'p': p, 'vit_a' : vit_a,
                                                                       'vit_c' : vit_c, "vit_e" : vit_e, "data": data, "labels" : labels})

        return render(request, self.template_name, {'form': form})

