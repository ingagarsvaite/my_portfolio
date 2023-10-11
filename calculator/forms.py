from django import forms
from .models import FoodItem
from django.forms import formset_factory


class FoodSelectionForm(forms.Form):
    food_item = forms.ModelChoiceField(
        queryset=FoodItem.objects.all(),
        empty_label="Select a food item",
        to_field_name="long_desc",
        label='Food Item'
    )
    quantity = forms.DecimalField(label='Quantity in grams', min_value=0.01)

    def has_changed(self):
        # Check if any data in the form has changed
        return any(field for field in self.changed_data if field != 'food_item')

FoodSelectionFormSet = formset_factory(FoodSelectionForm, extra=10)