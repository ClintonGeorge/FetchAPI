from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_process_pass():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                    }
            ],
        "total": "35 "
        }
   )
    assert response.status_code == 200

def test_process_total_value_unparse():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                    }
            ],
        "total": "something"
        }
   )
    assert response.status_code == 400

def test_process_missing_keys():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                    }
            ],
        "total": "35.35"
        }
   )
    assert response.status_code == 400

def test_process_empty_values():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                    }
            ],
        "total": "35.35"
        }
   )
    assert response.status_code == 200

def test_process_additional_body_parameters():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "location": "3201 S State Street",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                    }
            ],
        "total": "35.35"
        }
   )
    assert response.status_code == 400

def test_process_incorrect_date_data():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-31-23",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                    }
            ],
        "total": "35.35"
        }
   )
    assert response.status_code == 400    

def test_process_incorrect_date_format():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022/01/01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                    }
            ],
        "total": "35.35"
        }
   )
    assert response.status_code == 400

def test_process_incorrect_time_data():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-31-23",
            "purchaseTime": "25",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                    }
            ],
        "total": "35.35"
        }
   )
    assert response.status_code == 400

def test_process_incorrect_time_format():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13::01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                    }
            ],
        "total": "35.35"
        }
   )
    assert response.status_code == 400

def test_process_incorrect_item_price_data():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-31-23",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6 "
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "free"
                    }
            ],
        "total": "35.35"
        }
   )
    assert response.status_code == 400

def test_process_incorrect_item_parse():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "Target",
            "purchaseDate": "2022-31-23",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                },{
                "shortDescription": "Emils Cheese Pizza",
                },{
                "shortDescription": "Knorr Creamy Chicken",
                },{
                "shortDescription": "Doritos Nacho Cheese",
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                    }
            ],
        "total": "35.35"
        }
   )
    assert response.status_code == 400

def test_process_pass_2():
    response = client.post(
        "/receipts/process",
        json={
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                    }
            ],
        "total": "9.00"
        }
   )
    assert response.status_code == 200

def test_read_item_bad_token():
    response = client.get("/receipts/fffffff/points")
    assert response.status_code == 404

    