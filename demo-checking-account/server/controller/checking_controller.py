import connexion
import six

from server.models.amount import Amount  # noqa: E501
from server.models.balance import Balance  # noqa: E501
from server.models.error import Error  # noqa: E501
from server import util

checking = {
    "balance": 100.0
}

def checking_get():  # noqa: E501
    """Returns the current checking balance

     # noqa: E501


    :rtype: Balance
    """
    Balance = {
        "balance": checking["balance"]
    }
    return Balance


def checking_put(body):  # noqa: E501
    """Deposit (or withdraw) money to (or from) your checking account

     # noqa: E501

    :param body: Amount to deposit or withdraw
    :type body: dict | bytes

    :rtype: Balance
    """
    if connexion.request.is_json:
        body = Amount.from_dict(connexion.request.get_json())  # noqa: E501
        
    new_balance = checking["balance"] + body.amount
    checking["balance"] = new_balance
    
    Balance = {
        "balance": checking["balance"]
    }
    
    return Balance
