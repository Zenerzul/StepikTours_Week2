from random import sample

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
        dep_amount = 0
        dep_nights_min = 0
        dep_nights_max = 0
        dep_price_min = 0
        dep_price_max = 0
        for info in tours.values():
            if info["departure"] == departure:
                dep_amount += 1
                if dep_price_min == 0:
                    dep_price_min = info["price"]
                    dep_price_max = info["price"]
                elif info["price"] < dep_price_min:
                    dep_price_min = info["price"]
                elif info["price"] > dep_price_max:
                    dep_price_max = info["price"]
                if dep_nights_min == 0:
                    dep_nights_min = info["nights"]
                    dep_nights_max = info["nights"]
                elif info["nights"] < dep_nights_min:
                    dep_nights_min = info["nights"]
                elif info["nights"] > dep_nights_max:
                    dep_nights_max = info["nights"]

        return render(request, 'tours/departure.html', context={
            "title": title,
            "departures": departures,
            "dep_amount": dep_amount,
            "dep_price_min": dep_price_min,
            "dep_price_max": dep_price_max,
            "dep_nights_min": dep_nights_min,
            "dep_nights_max": dep_nights_max,
            "tours": tours,
            "departure": departure,
            "departure_title": departures[departure][3:]
        })


class TourView(View):
    def get(self, request, id, *args, **kwargs):
        return render(request, 'tours/tour.html', context={
            "title": title,
            "departures": departures,
            "tour_title": tours[id]['title'],
            "nights": tours[id]['nights'],
            "price": tours[id]['price'],
            "description": tours[id]['description'],
            "stars": tours[id]['stars'],
            "date": tours[id]['date'],
            "country": tours[id]['country'],
            "picture": tours[id]['picture'],
            "departure_title": departures[tours[id]['departure']][3:]
        })
