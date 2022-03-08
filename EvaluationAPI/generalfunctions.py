def error_message(message, data=None):
    response_dictionary = dict()
    response_dictionary["message"] = message
    response_dictionary["is_success"] = False
    response_dictionary["data"] = data
    return response_dictionary


def success_message(message, data=None):
    response_dictionary = dict()
    response_dictionary["message"] = message
    response_dictionary["is_success"] = True
    response_dictionary["data"] = data
    return response_dictionary
