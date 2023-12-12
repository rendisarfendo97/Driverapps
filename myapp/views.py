from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Driver, Unit, Permintaan


def index(request):
    return render(request, "myapp/index.html")

def home(request):
    # Mendapatkan jumlah data menggunakan metode count
    data_countpermintaan = Unit.objects.count()
    # Mendapatkan jumlah data menggunakan metode count
    data_countdriver = Unit.objects.count()
    # Mendapatkan jumlah data menggunakan metode count
    data_countunit = Unit.objects.count()
    context = {
        'data_countpermintaan': data_countpermintaan,
        'data_countdriver': data_countdriver,
        'data_countunit': data_countpermintaan,
    }
    # Implementasi logika untuk mengunggah data
    return render(request, "myapp/home.html", context)


def upload_data(request):
    # Implementasi logika untuk mengunggah data
    return render(request, "myapp/upload_data.html")


def data_permintaan(request):
    # Implementasi logika untuk mengunggah data
    Permintaans = Permintaan.objects.all()
    # Mendapatkan jumlah data menggunakan metode count
    data_count = Permintaan.objects.count()
    # Menyediakan data ke template
    context = {
        'data_count': data_count,
        'Permintaans': Permintaans,
    }
    return render(request, "myapp/data_permintaan.html", context)

def data_driver(request):
    # Implementasi logika untuk mengunggah data
    Drivers = Driver.objects.all()
    # Mendapatkan jumlah data menggunakan metode count
    data_count = Driver.objects.count()
    # Mendapatkan jumlah data menggunakan metode count ready
    data_ready = Driver.objects.filter(Status="Ready").count()
    # Mendapatkan jumlah data menggunakan metode count nonready
    data_nonready = Driver.objects.filter(Status="Non Ready").count()
    # Menyediakan data ke template
    context = {
        'data_count': data_count,
        'data_ready': data_ready,
        'data_nonready': data_nonready,
        'Drivers': Drivers,
    }
    return render(request, "myapp/data_driver.html", context)

def data_unit(request):
    # Implementasi logika untuk mengunggah data
    Units = Unit.objects.all()
    # Mendapatkan jumlah data menggunakan metode count
    data_count = Unit.objects.count()
    # Mendapatkan jumlah data menggunakan metode count ready
    data_ready = Unit.objects.filter(Status="Ready").count()
    # Mendapatkan jumlah data menggunakan metode count nonready
    data_nonready = Unit.objects.filter(Status="Non Ready").count()
    # Menyediakan data ke template
    context = {
        'data_count': data_count,
        'data_ready': data_ready,
        'data_nonready': data_nonready,
        'Units': Units,
    }
    return render(request, "myapp/data_unit.html", context)
    

def management_user(request):
    # Implementasi logika untuk mengunggah data
    return render(request, "myapp/management_user.html")

def input_driver(request):
    # Implementasi logika untuk mengunggah data
    return render(request, "myapp/input_driver.html")

def input_unit(request):
    # Implementasi logika untuk mengunggah data
    return render(request, "myapp/input_unit.html")

def input_permintaan(request):
    # Implementasi logika untuk mengunggah data
    return render(request, "myapp/input_permintaan.html")

# Insert driver
def insert_driver(request):
    if request.method == "POST":
        KodeDriver = request.POST["KodeDriver"]
        NamaDriver = request.POST["NamaDriver"]
        Kantor = request.POST["Kantor"]
        Status = request.POST["Status"]
        data = Driver(
            KodeDriver=KodeDriver,
            NamaDriver=NamaDriver,
            Kantor=Kantor,
            Status=Status,
        )
        data.save()

        return redirect("data_driver")
    else:
        # Jika metode adalah GET, tampilkan halaman input dengan data Units
        Units = Unit.objects.all()
        context = {
            'Units': Units,
        }
        return render(request, "myapp/input_driver.html", context)

# Insert Unit
def insert_unit(request):
    if request.method == "POST":
        KodeUnit = request.POST["KodeUnit"]
        NamaUnit = request.POST["NamaUnit"]
        PlatNomor = request.POST["PlatNomor"]
        NomerRangka = request.POST["NomerRangka"]
        NomerMesin = request.POST["NomerMesin"]
        Kantor = request.POST["Kantor"]
        Status = request.POST["Status"]
        data = Unit(
            KodeUnit=KodeUnit,
            NamaUnit=NamaUnit,
            PlatNomor=PlatNomor,
            NomerRangka=NomerRangka,
            NomerMesin=NomerMesin,
            Kantor=Kantor,
            Status=Status,
        )
        data.save()

        return redirect("data_unit")
    else:
        return render(request, "myapp/input_unit.html")

# Insert Permintaan
def insert_permintaan(request):
    if request.method == "POST":
        KodePermintaan = request.POST["KodePermintaan"]
        NomerSuratJalan = request.POST["NomerSuratJalan"]
        NamaPermintaan = request.POST["NamaPermintaan"]
        TitikAntar = request.POST["TitikAntar"]
        TitikJemput = request.POST["TitikJemput"]
        NamaDriver = request.POST["NamaDriver"]
        NamaUnit = request.POST["NamaUnit"]
        data = Permintaan(
            KodePermintaan=KodePermintaan,
            NomerSuratJalan=NomerSuratJalan,
            NamaPermintaan=NamaPermintaan,
            TitikAntar=TitikAntar,
            TitikJemput=TitikJemput,
            NamaDriver=NamaDriver,
            NamaUnit=NamaUnit,
        )
        data.save()

        return redirect("data_permintaan")
    else:
        # Mendapatkan jumlah data menggunakan metode count ready
        data_readyunit = Unit.objects.filter(Status="Ready")
        # Mendapatkan jumlah data menggunakan metode count ready
        data_readydriver = Driver.objects.filter(Status="Ready")
        context = {
            'data_readyunit': data_readyunit,
            'data_readydriver': data_readydriver,
        }
        return render(request, "myapp/input_permintaan.html", context)

# Edit Unit
def edit_unit(request, pk):
    unit = Unit.objects.get(id=pk)

    if request.method == "POST":
        print(request.POST)
        unit.KodeUnit = request.POST["KodeUnit"]
        unit.NamaUnit = request.POST["NamaUnit"]
        unit.PlatNomor = request.POST["PlatNomor"]
        unit.NomerRangka = request.POST["NomerRangka"]
        unit.NomerMesin = request.POST["NomerMesin"]
        unit.Kantor = request.POST["Kantor"]
        unit.Status = request.POST["Status"]
        unit.save()
        return redirect("data_unit")
    context = {
        "unit": unit,
    }

    return render(request, "myapp/edit_unit.html", context)

# Hapus Unit
def hapus_unit (request, pk):
    unit = Unit.objects.get(id=pk)
    unit.delete()
    return redirect('data_unit')

# Edit Driver
def edit_driver(request, pk):
    driver = Driver.objects.get(id=pk)
    Units = Unit.objects.all()
    
    if request.method == "POST":
        print(request.POST)
        driver.KodeDriver = request.POST["KodeDriver"]
        driver.NamaDriver = request.POST["NamaDriver"]
        driver.Kantor = request.POST["Kantor"]
        driver.Status = request.POST["Status"]
        driver.save()
        return redirect("data_driver")
    context = {
        "driver": driver,
        "Units": Units,
    }

    return render(request, "myapp/edit_driver.html", context)

# Hapus Driver
def hapus_driver (request, pk):
    driver = Driver.objects.get(id=pk)
    driver.delete()
    return redirect('data_driver')

# Edit Permintaan
def edit_permintaan(request, pk):
    permintaan = Permintaan.objects.get(id=pk)
    Units = Unit.objects.all()
    data_readyunit = Unit.objects.filter(Status="Ready")
    data_readydriver = Driver.objects.filter(Status="Ready")

    if request.method == "POST":
        print(request.POST)
        permintaan.KodePermintaan = request.POST["KodePermintaan"]
        permintaan.NomerSuratJalan = request.POST["NomerSuratJalan"]
        permintaan.NamaPermintaan = request.POST["NamaPermintaan"]
        permintaan.TitikAntar = request.POST["TitikAntar"]
        permintaan.TitikJemput = request.POST["TitikJemput"]
        permintaan.NamaDriver = request.POST["NamaDriver"]
        permintaan.NamaUnit = request.POST["NamaUnit"]
        permintaan.save()
        return redirect("data_permintaan")
    context = {
        "data_readyunit": data_readyunit,
        "data_readydriver": data_readydriver,
        "permintaan": permintaan,
        "Units": Units,
    }

    return render(request, "myapp/edit_permintaan.html", context)

# Hapus Permintaan
def hapus_permintaan (request, pk):
    permintaan = Permintaan.objects.get(id=pk)
    permintaan.delete()
    return redirect('data_permintaan')