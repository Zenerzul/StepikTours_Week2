from random import sample

from django.http import Http404
from django.shortcuts import render
from django.views import View

from tours.data import title, subtitle, description, departures, tours


class MainView(View):
    def get(self, request, *args, **kwargs):
        tours_number = sample(range(1, 17), 6)
        tours_random_six = {}
        for tour in tours:
            if tour in tours_number:
                tours_random_six[tour] = tours[tour]
        return render(request, 'tours/index.html', context={
            'departures': departures,
            'title': title,
            'subtitle': subtitle,
            'description': description,
            'tours': tours,
            'tours_random_six': tours_random_six
        })


class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):
        if departure not in departures.keys():
            raise Http404
        else:
            departure_amount = sum(1 for tour in tours.values() if tour["departure"] == departure)
            departure_price_max = max(int(tour["price"]) for tour in tours.values() if tour["departure"] == departure)
            departure_price_min = min(int(tour["price"]) for tour in tours.values() if tour["departure"] == departure)
            departure_nights_max = max(int(tour["nights"]) for tour in tours.values() if tour["departure"] == departure)
            departure_nights_min = min(int(tour["nights"]) for tour in tours.values() if tour["departure"] == departure)
            return render(request, 'tours/departure.html', context={
                'title': title,
                'departures': departures,
                'departure_amount': departure_amount,
                'departure_price_min': departure_price_min,
                'departure_price_max': departure_price_max,
                'departure_nights_min': departure_nights_min,
                'departure_nights_max': departure_nights_max,
                'tours': tours,
                'departure': departure,
                'departure_title': departures[departure][3:]
            })


class TourView(View):
    def get(self, request, tour_id, *args, **kwargs):
        if tour_id not in tours.keys():
            raise Http404
        else:
            return render(request, 'tours/tour.html', context={
                'title': title,
                'departures': departures,
                'tour_title': tours[tour_id]['title'],
                'nights': tours[tour_id]['nights'],
                'price': tours[tour_id]['price'],
                'description': tours[tour_id]['description'],
                'stars': tours[tour_id]['stars'],
                'date': tours[tour_id]['date'],
                'country': tours[tour_id]['country'],
                'picture': tours[tour_id]['picture'],
                'departure_title': departures[tours[tour_id]['departure']][3:]
            })
