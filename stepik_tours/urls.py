from django.contrib import admin
from django.urls import path

from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='home'),
    path('departure/<str:departure>', DepartureView.as_view(), name='departure'),
    path('tour/<int:tour_id>', TourView.as_view(), name='tour'),
]
