from datetime import datetime
import math

def every_char_retailer(retailer: str) -> int:
    """ 1 point for every alphanumeric character.

    Args:
        retailer: retailer's name

    Returns:
        points: updated points
    """
    points = 0
    for c in retailer:
        if c.isalpha():
            points += 1
    return points

def total_doller_amount(total: float) -> int:
    """ 50 points if the total is a round dollar amount with no cents.
    
    Args:
        total

    Returns:
        points: updated points
    """
    points = 0
    if total == float(round(total)):
        points += 50
    return points

def total_multiple_of(total: float) -> int:
    """ 25 points if the total is a multiple of 0.25

    Args:
        total

    Returns:
        points: updated points
    """
    points = 0
    if total % 0.25 == 0.0:
        points += 25
    return points

def item_pair(items: list) -> int:
    """ 5 points for each pair of items
    
    Args:
        items: list of items

    returns:
        points: updated points
    """
    points = 0
    points += (5*(len(items)//2))
    return points

def item_description(item_desc: str, price: float) -> int:
    """ round up of 0.2 x price of items those with descriptions length
    is multiple of 3.

    Args: 
        item_desc: item description of respective item,
        price: price of respective item,
        points
    
    returns:
        points: updated points
    """
    points = 0
    if len(item_desc)%3 == 0:
        price *= 0.2
        points += math.ceil(price)
    return points

def day_of_purchase(purchase_date: datetime.date) -> int:
    """ 6 points if the purchase date is odd.

    Args:
        purchase_date: date,

    returns:
        points: updated points
    """
    points = 0
    day = purchase_date.day
    if day % 2 == 1:
        points += 6
    return points

def time_of_purchase(purchase_time: datetime.time) -> int:
    """ 10 points if the purchase time is between 2pm and 4pm

        Args:
            purchase_time: time of purchase,

        returns:
            points: updated points
    """
    points=0
    # 2pm formatted to be in 24 hour clock and coverted to date object 
    time_2PM = datetime.strptime('14:00', r'%H:%M').time()
    # 2pm formatted to be in 24 hour clock and coverted to date object 
    time_4PM = datetime.strptime('16:00', r'%H:%M').time()                        
    if purchase_time > time_2PM and purchase_time < time_4PM:
        points+=10
    return points

