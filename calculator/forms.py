from django import forms
from .models import FoodItem


class FoodSelectionForm(forms.Form):
    # Query the database to get the long_desc values for choices
    food_item = forms.ModelChoiceField(
        queryset=FoodItem.objects.all(),
        empty_label="Select a food item",  # Optional, provides an empty label in the dropdown
        to_field_name="long_desc",  # Use the long_desc field as the value
        label='Food Item'
    )
    quantity = forms.IntegerField(label='Quantity')

