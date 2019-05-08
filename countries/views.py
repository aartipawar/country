from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.views import View
from countries.models import City,State,Country
from django.views.decorators.csrf import csrf_exempt
from .forms import CityForm,StateForm,CountryForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CountryView(View):
    def get(self,request):
        if request.method == 'GET':
            country = Country.objects.all()    
            return render(request, 'country.html', {'countries': country})

@csrf_exempt
def get_state(request):
    state_li = []
    country_id = request.POST.get('country_id')
    get_state = State.objects.filter(country=country_id).values('state', 'id')
    for data in get_state:
        res={'state':data['state'],
            'id':data['id']}
        state_li.append(res)
    return JsonResponse({'success':'true','state':state_li})

@csrf_exempt
def get_city(request):
    city_li = []
    state_id = request.POST.get('state_id')
    get_city = City.objects.filter(state=state_id).values('city', 'id')
    for data in get_city:
        res={'city':data['city'],
        'id':data['id']}
        city_li.append(res)
    return JsonResponse({'success':'true','city':city_li})
        


class CityList(View):
    def get(self,request):
        if request.user.is_authenticated:
            city_obj = CityForm()
            print('lll')
            return render(request, 'city.html', {'city_list': city_obj})


# class StateList(View):
#     def get(self,request):
#         if request.user.is_authenticated:
#             state_form = StateForm()
#             return render(request, 'state.html', {'states': state_form })
        
