from django.db import models

# Create your models here.
class PizzaShop(models.Model):
    """Pizzzeria Class"""
    class Meta:
        verbose_name = "Пиццерия"
        verbose_name_plural = "Пиццерии"

    name = models.CharField(max_length=50, verbose_name="Pizzeria")
    description = models.TextField(verbose_name="Description")
    rating = models.FloatField(verbose_name="Rating", default=0)
    url = models.URLField(verbose_name="Link")

    def __str__(self):
        return self.name


class Pizza(models.Model):
    class Meta:
        verbose_name = "Пицца"
        verbose_name_plural = "Пиццы"

    pizza_shop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Pizza Name")
    description = models.TextField(verbose_name="Description")
    price = models.FloatField(default=0, verbose_name="Pizza's Price")

    def __str__(self):
        return self.name