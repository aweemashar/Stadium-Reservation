from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from django.http import JsonResponse
from django.db.models import Count,Q
from .generalfunctions import *
from .serializers import *
from .models import *
import json


@action(detail=True, methods=['GET'])
def manage_view(request):
    """
    Dummy API to test Routing
    :param request: None
    :return: Hello Message
    """
    print("hello world")
    result_data = {'message': "Hello"}
    return JsonResponse(result_data)


@csrf_exempt
@action(detail=True, methods=['POST'])
def create_restaurant(request):
    """
    To create an object of Restaurant
    :param request:
        name (str): name of restaurant to be created
        type (str): type of restaurant to be created
        address (str): address of restaurant to be created
    :return:
        {
            message (str),
            data    (Dictionary Object in case od data otherwise None)
            is_success: (bool)
        }
    """
    request_body = request.body.decode('utf-8')
    body_params = json.loads(request_body)
    restaurant_name = body_params['name']
    restaurant_type = body_params['type']
    restaurant_address = body_params['address']
    Restaurant.objects.create(restaurant_name = restaurant_name,
                              restaurant_type=restaurant_type,
                              address = restaurant_address)
    response_dictionary = success_message("Restaurant Created", )
    return JsonResponse(response_dictionary)
 #

@csrf_exempt
@action(detail=True, methods=['GET'])
def get_restaurant(request):
    """
    To create an object of Restaurant
    :param request:
        id  (int): ID against which data has to be return
    :return:
        {
            message (str),
            data (dict) (Dictionary Object in case od data otherwise None)
            is_success: (bool)
        }
    """
    request_body = request.body.decode('utf-8')
    body_params = json.loads(request_body)
    restaurant_id = body_params['id']
    try:
        restaurant_obj = Restaurant.objects.get(id=restaurant_id)
        restaurant_data = {
            'restaurant_name':restaurant_obj.restaurant_name,
            'restaurant_type':restaurant_obj.restaurant_type,
            'restaurant_address':restaurant_obj.address
        }
    except Exception as exc:
        response_dictionary = error_message(exc)
        return JsonResponse(response_dictionary)

    response_dictionary = success_message("Restaurant Created",restaurant_data )
    return JsonResponse(response_dictionary)


@action(detail=True, methods=['GET'])
def get_stadium_free_time_slot(request):
    """
    This Function will return the available time slots of stadium for reservation when providing the stadium_id
    :param request:
    stadium_id (int) : stadium id against which stadium information is stored in database
    :return: Json Object {
    message (str) , is_success (bool)
    data {
    stadium_id (int) ,stadium_name (str),address (str)
    available_slots [
    id (int), date (date), start_time (time), end_time (time)]
        }
    }
    """
    request_body = json.loads(request.body.decode('utf-8'))
    if request_body['stadium_id'] is None or request_body['stadium_id'] is "":
        response_dictionary = error_message("Invalid Key")
        return JsonResponse(response_dictionary)
    else:
        try:
            response_data = dict()
            stadium_id = int(request_body['stadium_id'])
            result_data = StadiumAvailabililty.objects.filter(stadium_id_id=stadium_id, is_available=True)
            if len(result_data) != 0:
                response_data['stadium_id'] = result_data[0].stadium_id_id
                response_data['stadium_name'] = result_data[0].stadium_id.name
                response_data['address'] = result_data[0].stadium_id.address
                response_data['available_slots'] = list()
                for result_data_obj in result_data:
                    time_slot_obj = dict()
                    time_slot_obj['id'] = result_data_obj.id
                    time_slot_obj['date'] = result_data_obj.free_slots_start_time.date()
                    time_slot_obj['start_time'] = result_data_obj.free_slots_start_time.time()
                    time_slot_obj['end_time'] = result_data_obj.free_slots_end_time.time()
                    response_data['available_slots'].append(time_slot_obj)
                response_data = TimeSlotSerializer(result_data, many=True,
                                                context={"request": request}).data

                response_dictionary = success_message("Time Slots for requested Stadiums are: ", response_data)

            else:
                response_dictionary = success_message("No time slots available for requested stadium.",)

        except Exception as e:
            response_dictionary = error_message("AN unexpected error has occurred " ,str(e))
            return JsonResponse(response_dictionary)
    return JsonResponse(response_dictionary)





