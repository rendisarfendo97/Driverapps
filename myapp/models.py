from django.db import models

# Create Driver.
class Driver(models.Model):
    KodeDriver = models.CharField(max_length=255, default="")
    NamaDriver = models.CharField(max_length=255, default="")
    Kantor = models.CharField(max_length=255, default="")
    NamaUnit = models.CharField(max_length=255, default="")
    Status = models.CharField(max_length=255, default="")

    class Meta:
        db_table = "Driver"


# Create Unit.
class Unit(models.Model):
    KodeUnit = models.CharField(max_length=255, default="")
    NamaUnit = models.CharField(max_length=255, default="")
    PlatNomor = models.CharField(max_length=255, default="")
    NomerRangka = models.CharField(max_length=255, default="")
    NomerMesin = models.CharField(max_length=255, default="")
    Kantor = models.CharField(max_length=255, default="")
    Status = models.CharField(max_length=255, default="")

    class Meta:
        db_table = "Unit"


# Create Permintaan.
class Permintaan(models.Model):
    KodePermintaan = models.CharField(max_length=255, default="")
    NomerSuratJalan = models.CharField(max_length=255, default="")
    NamaPermintaan = models.CharField(max_length=255, default="")
    TitikAntar = models.CharField(max_length=255, default="")
    TitikJemput = models.CharField(max_length=255, default="")
    NamaDriver = models.CharField(max_length=255, default="")
    NamaUnit = models.CharField(max_length=255, default="")
    class Meta:
        db_table = "Permintaan"