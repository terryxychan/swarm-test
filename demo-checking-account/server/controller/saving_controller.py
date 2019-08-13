import connexion
import six
import requests
from server.models.balance import Balance  # noqa: E501
from server import util

saving = {
     'balance': 1200.0
}

def saving_get():  # noqa: E501
    """Returns the current saving balance

     # noqa: E501


    :rtype: Balance
    """
    SAVING_API_ENDPOINT = 'http://bankDemo_savingAccount:5000/api/v1/saving'
    get_saving = requests.get(url = SAVING_API_ENDPOINT)
    result = get_saving.json()
    saving["balance"] = result["balance"]
    
    return saving