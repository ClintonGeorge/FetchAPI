from pydantic import BaseModel, Extra

class Item(BaseModel):
    shortDescription: str
    price: float
    # extra body parameters are forbidden and should throw error
    class Config:
        extra = Extra.forbid

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[dict]
    total: float
    # extra body parameters are forbidden and should throw error
    class Config:
        extra = Extra.forbid