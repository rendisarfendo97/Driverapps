from django.urls import path

from . import views
from .views import (
    upload_data,
    data_permintaan,
    data_driver,
    data_unit,
    #management_user,
    input_driver,
    input_unit,
    input_permintaan,
    insert_driver,
    insert_unit,
    insert_permintaan,
    edit_unit,
    edit_driver,
    edit_permintaan,
    hapus_unit,
    hapus_driver,
    hapus_permintaan,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("upload_data/", upload_data, name="upload_data"),
    path("data_permintaan/", data_permintaan, name="data_permintaan"),
    path("input_permintaan/", input_permintaan, name="input_permintaan"),
    path("insert_permintaan/", insert_permintaan, name="insert_permintaan"),
    path("data_driver/", data_driver, name="data_driver"),
    path("input_driver/", input_driver, name="input_driver"),
    path("insert_driver", insert_driver, name="insert_driver"),
    path('edit_driver/<int:pk>/', edit_driver, name='edit_driver'),
    path('hapus_driver/<int:pk>/', hapus_driver, name='hapus_driver'),
    path("data_unit/", data_unit, name="data_unit"),
    path("input_unit/", input_unit, name="input_unit"),
    path("insert_unit", insert_unit, name="insert_unit"),
    path('edit_unit/<int:pk>/', edit_unit, name='edit_unit'),
    path('hapus_unit/<int:pk>/', hapus_unit, name='hapus_unit'),
    path('edit_permintaan/<int:pk>/', edit_permintaan, name='edit_permintaan'),
    path('hapus_permintaan/<int:pk>/', hapus_permintaan, name='hapus_permintaan'),
    # path("management_user/", management_user, name="management_user"),
    # path("insert_user/", insert_user, name="insert_user")
]
