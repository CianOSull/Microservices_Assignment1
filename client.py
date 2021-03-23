import os
import grpc
import time
import data_pb2
import data_pb2_grpc
from random import randint

import logging

def run():
    while True:
        with grpc.insecure_channel('server:50051') as channel:
            stub = data_pb2_grpc.GetDataServiceStub(channel)
            response = stub.GetData(data_pb2.Posts(posts="Passed in String"))
    
        print("Client.py: ", response.received)
        time.sleep(randint(1,6))

if __name__ == "__main__":
    logging.basicConfig()
    run()