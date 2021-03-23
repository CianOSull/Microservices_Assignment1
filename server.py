import grpc
from concurrent import futures
import time
import data_pb2
import data_pb2_grpc
import threading

import logging
import datetime
import redis


class GetDataService(data_pb2_grpc.GetDataService):
    def __init__(self, *args, **kwargs):
        pass

    def GetData(self, request, context):
        response = data_pb2.CheckReponse(received="Server.py: %s!" % request.posts)

        try:

            conn = redis.StrictRedis(host='redis', port=6379)
            conn.set("log.greeter_server." + str(datetime.datetime.now()), "Client Says: " + request.posts)
        
        except Exception as ex:
            print('Error:', ex)
        
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_GetDataServiceServicer_to_server(GetDataService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()



