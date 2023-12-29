import requests
from time import sleep
from datetime import datetime
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text


random.seed(100)


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()

def serialize_datetime(value):
    """Convert datetime objects to a string."""
    if isinstance(value, datetime):
        return value.isoformat()  # Or any other format you prefer
    return value


def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
            #print(pin_result)
            #print(geo_result)
            #print(user_result)
            
            # Sending data to API
            headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}

            # Pinterest post invoke url & data formatting
            pin_url = 'https://s1acipwfb7.execute-api.us-east-1.amazonaws.com/dev/topics/0e8c5a5fa275.pin'

            '''pin_payload = json.dumps({
                "records": [
                    {
                    #Data should be send as pairs of column_name:value, with different columns separated by commas       
                    "value": {"index": pin_result["index"], "unique_id": pin_result["unique_id"], "title": pin_result["title"], "description": pin_result["description"], "poster_name": pin_result["poster_name"], "follower_count": pin_result["follower_count"], "tag_list": pin_result["tag_list"], "is_image_or_video": pin_result["is_image_or_video"], "image_src": pin_result["image_src"], "downloaded": pin_result["downloaded"], "save_location": pin_result["save_location"], "category": pin_result["category"]}
                    }
                ]
            })'''

            pin_payload = json.dumps({
                "records": [
                    {
                    "value": {k: serialize_datetime(v) for k, v in pin_result.items()}
                    }
                ]
            })

            # Pinterest geographical data invoke url & data formatting
            geo_url = 'https://s1acipwfb7.execute-api.us-east-1.amazonaws.com/dev/topics/0e8c5a5fa275.geo'

            '''geo_payload = json.dumps({
                "records": [
                    {
                    #Data should be send as pairs of column_name:value, with different columns separated by commas       
                    "value": {"ind": geo_result["ind"], "timestamp": geo_result["timestamp"], "latitude": geo_result["latitude"], "longitude": geo_result["longitude"], "country": geo_result["country"]}
                    }
                ]
            })'''

            geo_payload = json.dumps({
                "records": [
                    {
                        "value": {k: serialize_datetime(v) for k, v in geo_result.items()}
                    }
                ]
            })

            # Pinterest user data invoke url & data formatting
            user_url = 'https://s1acipwfb7.execute-api.us-east-1.amazonaws.com/dev/topics/0e8c5a5fa275.user'

            '''user_payload = json.dumps({
                "records": [
                    {
                    #Data should be send as pairs of column_name:value, with different columns separated by commas       
                    "value": {"ind": user_result["ind"], "first_name": user_result["first_name"], "last_name": user_result["last_name"], "age": user_result["age"], "date_joined": user_result["date_joined"]}
                    }
                ]
            })'''


            user_payload = json.dumps({
                "records": [
                    {
                        "value": {k: serialize_datetime(v) for k, v in user_result.items()}
                    }
                ]
            })

            # Sending data to API
            try:
                pin_response = requests.request("POST", pin_url, headers=headers, data=pin_payload)
                print(pin_response.status_code)

                geo_response = requests.request("POST",geo_url, headers=headers, data=geo_payload)
                print(geo_response.status_code)

                user_response = requests.request("POST",user_url, headers=headers, data=user_payload)
                print(user_response.status_code)
            
            except Exception as e:
                print(f"Failed to send data to API: {e}")



if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    
    


