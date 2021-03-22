import os
import grpc
import time
import data_pb2
import data_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = data_pb2_grpc.GetDataServiceStub(channel)

        while True:
            try: 
                response = stub.GetData(data_pb2.Posts(posts="Test"))
                print("Data.py: ", response.received)
                time.sleep(10)
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
                channel.unsubscribe(close)
                exit()

def close(channel):
    channel.close()

if __name__ == "__main__":
    run()