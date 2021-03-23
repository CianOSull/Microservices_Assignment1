import os
import grpc
import time
import data_pb2
import data_pb2_grpc
from random import randint

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = data_pb2_grpc.GetDataServiceStub(channel)
        response = stub.GetData(data_pb2.Posts(posts="Passed in String"))
    print("Client.py: ", response.received)

if __name__ == "__main__":
    run()