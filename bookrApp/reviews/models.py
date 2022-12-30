from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50,
                            help_text="Nazwa wydawcy.")
    website = models.URLField(help_text="Witryna wydawcy.")
    email = models.EmailField(help_text="Adres e-mail wydawcy.")
