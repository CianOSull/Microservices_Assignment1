import grpc
from concurrent import futures
import time
import data_pb2
import data_pb2_grpc
import threading

class GetMetricService(data_pb2_grpc.GetMetricService):
    def __init__(self, *args, **kwargs):
        pass

    def GetMetric(self, request, context):
        metrics = request.metrics

        print(metrics)

        return data_pb2.ServerReponse(response=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_pb2_grpc.add_GetMetricServiceServicer_to_server(GetMetricService(), server)
    server.add_insecure_port('[::]:50052')
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