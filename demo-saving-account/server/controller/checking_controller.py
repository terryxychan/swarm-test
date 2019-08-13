import connexion
import six
import requests
from server.models.balance import Balance  # noqa: E501
from server import util

checking = {
     'balance': 100.0
}

def checking_get():  # noqa: E501
    """Returns the current checking balance

     # noqa: E501


    :rtype: Balance
    """
    CHECKING_API_ENDPOINT = 'http://bankDemo_checkingAccount:5000/api/v1/checking'
    get_checking = requests.get(url = CHECKING_API_ENDPOINT)
    result = get_checking.json()
    checking["balance"] = result["balance"]
    
    return checking
