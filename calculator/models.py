from django.db import models


class FoodItem(models.Model):
    long_desc = models.CharField(max_length=255)
    fiber_in_g = models.DecimalField(max_digits=50, decimal_places=2)
    kcal_in_100g = models.DecimalField(max_digits=50, decimal_places=2)
    mg_in_mg = models.DecimalField(max_digits=50, decimal_places=2)
    zn_in_mg = models.DecimalField(max_digits=50, decimal_places=2)
    fa_in_mcg = models.DecimalField(max_digits=50, decimal_places=10)
    p_in_mg = models.DecimalField(max_digits=50, decimal_places=2)
    vitamin_a_in_mcg = models.DecimalField(max_digits=50, decimal_places=2)
    vitamin_c_in_mg = models.DecimalField(max_digits=50, decimal_places=2)
    vitamin_e_in_mg = models.DecimalField(max_digits=50, decimal_places=2)

    class Meta:
        db_table = 'fruits_vegetables'

    def __str__(self):
        return self.long_desc

class RefValue(models.Model):
    element = models.CharField(max_length=250)
    ref_value = models.DecimalField(max_digits=50, decimal_places=2)

    class Meta:
        db_table = 'refvalue'

    def __str__(self):
        return self.element, self.ref_value