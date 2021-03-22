import grpc
from concurrent import futures
import time
import data_pb2
import data_pb2_grpc
import threading

class GetDataService(data_pb2_grpc.GetDataService):
    def __init__(self, *args, **kwargs):
        pass

    def GetData(self, request, context):
        posts = request.posts
        print("Client.py:", posts)

        # I think this should return the message from proto
        return data_pb2.CheckReponse(received=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_GetDataServiceServicer_to_server(GetDataService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while  True:
            print("server on: threads %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt")
        server.stop(0)
    # server.wait_for_termination()

if __name__ == '__main__':
    serve()



