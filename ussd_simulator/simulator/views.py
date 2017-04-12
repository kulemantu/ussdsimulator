from django_ussd.http.views import UssdSimulatorView
import requests
 
 
class UssdSimulator(UssdSimulatorView):
    """
    This class inherits from the UssdSimulatorView
    """
    # initial_input is required by UssdSimulatorView and we set it to an empty string
    initial_input = ''
    # you can use the Ussd simulator in the same app you have created the ussd app but that won't work for now given
    # django_ussd.core uses django 1.8.4 and django_ussd.http uses django 1.10
    # hence you need to set standalone_ussd_simulator = True in this case since it's
    standalone_ussd_simulator = True
    # This is the endpoint from which the ussd app is running from
    ussd_view_url_name = 'http://10.0.0.15:8000/ussd/'
 
    # overide the request_handler
    def request_handler(self, **kwargs):
        """
        Handles the request from the UssdSimulator
        :param kwargs:
        :return:
        """
        return requests.get(kwargs['ussd_url'],
                            params=dict(
                            msisdn=kwargs['phoneNumber'],
                            sessionId=kwargs['sessionId'],
                            input=kwargs['input']
                            ))
 
    def response_handler(self, response):
        """
        This sends back the response to the UssdSimulator. The response contains a boolean and
        The message if the boolean is False it doesn't display an input box and vice versa
        :param response:
        :return:
        """
        response_status = response.headers['Freeflow']
        response_message = response.content
        print(response)
        if response_status == 'FB':
            return False, response_message
        else:
            return True, response_message