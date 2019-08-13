import connexion
import six

from server.models.amount import Amount  # noqa: E501
from server.models.balance import Balance  # noqa: E501
from server.models.error import Error  # noqa: E501
from server import util

saving = {
    "balance": 1200.0
}

def saving_get():  # noqa: E501
    """Returns the current saving balance

     # noqa: E501


    :rtype: Balance
    """
    Balance = {
        "balance": saving["balance"]
    }
    return Balance



def saving_put(body):  # noqa: E501
    """Deposit (or withdraw) money to (or from) your saving account

     # noqa: E501

    :param body: Amount to deposit or withdraw
    :type body: dict | bytes

    :rtype: Balance
    """
    if connexion.request.is_json:
        body = Amount.from_dict(connexion.request.get_json())  # noqa: E501
    new_balance = saving["balance"] + body.amount
    saving["balance"] = new_balance
    
    Balance = {
        "balance": saving["balance"]
    }
    
    return Balance
