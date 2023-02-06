from fastapi import FastAPI, status, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from datetime import datetime
import random
import string
from . import schemas, rules

app = FastAPI()

# length of id to be generated
N = 32
# id to points map
POINTS_ID_MAP = {}

def generate_id(N) -> str:
    """ Return a randomly generated id of length N from a list of ascii
    letters and digits."""
    id = ''.join(random.choices(string.ascii_letters+string.digits, k=N))
    return id

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """ Overites the 422 Unprocessable entity message to 400 bad request"""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": "The receipt is invalid"}),
    )

@app.post("/receipts/process", tags=['Processor'])
def process(receipt: schemas.Receipt):
    points = 0
    retailer_name = receipt.retailer.strip()
    points += rules.every_char_retailer(retailer_name)
    date_strg = receipt.purchaseDate.strip()
    try:
        # check if date string is in yyyy-mm-dd format else throw error
        date = datetime.strptime(date_strg, r'%Y-%m-%d').date()
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='The receipt is invalid')
    points += rules.day_of_purchase(date)
    time_strg = receipt.purchaseTime.strip()
    try:
        # check if time is in h:m format or throw error
        time = datetime.strptime(time_strg, r'%H:%M').time()
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='The receipt is invalid')
    points += rules.time_of_purchase(time)
    try:
        # check if total is able to be converted to schema type(float) or throw error
        total = receipt.total
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='The receipt is invalid')
    points += rules.total_multiple_of(total)
    points += rules.total_doller_amount(total)
    items_lst = receipt.items
    points += rules.item_pair(items_lst)
    for i in range(len(items_lst)):
        try:
            # check if items is able to parse into schema or throw error
            item = schemas.Item(**items_lst[i])
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='The receipt is invalid')
        desc = item.shortDescription.strip()
        try:
            # check if price is able to be converted to schema type(float) or throw error
            item_price = item.price
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='The receipt is invalid')
        points += rules.item_description(desc, item_price)
    id = generate_id(N)
    POINTS_ID_MAP[id] = points
    return {"id": id}

@app.get('/receipts/{id}/points', tags=['Points'])
def get_points(id: str):
    # check if given id is an already generated one or throw error 
    if id not in POINTS_ID_MAP:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No reciept found for that id')
    else:
        return {"points": POINTS_ID_MAP[id]}
