import connexion
import six

from server.models.amount import Amount  # noqa: E501
from server.models.balance import Balance  # noqa: E501
from server.models.error import Error  # noqa: E501
from server import util

balance = {
    "balance": 100.0
}

def account_get():  # noqa: E501
    """Returns the current bank balance

     # noqa: E501


    :rtype: Balance
    """
    Balance = {
        "balance": balance["balance"]
    }
    return Balance


def account_put(body):  # noqa: E501
    """Deposit (or withdraw) money to (or from) your bank account

     # noqa: E501

    :param body: Amount to deposit or withdraw
    :type body: dict | bytes

    :rtype: Balance
    """
    if connexion.request.is_json:
        body = Amount.from_dict(connexion.request.get_json())  # noqa: E501
    new_balance = balance["balance"] + body.amount
    balance["balance"] = new_balance
    
    Balance = {
        "balance": balance["balance"]
    }
    
    return Balance

