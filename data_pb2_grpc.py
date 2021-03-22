# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_pb2 as data__pb2


class GetDataServiceStub(object):
    """python3 -m grpc_tools.protoc --proto_path=. ./data.proto --python_out=../ --grpc_python_out=../

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetData = channel.unary_unary(
                '/GetDataService/GetData',
                request_serializer=data__pb2.Posts.SerializeToString,
                response_deserializer=data__pb2.CheckReponse.FromString,
                )


class GetDataServiceServicer(object):
    """python3 -m grpc_tools.protoc --proto_path=. ./data.proto --python_out=../ --grpc_python_out=../

    """

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GetDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=data__pb2.Posts.FromString,
                    response_serializer=data__pb2.CheckReponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GetDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GetDataService(object):
    """python3 -m grpc_tools.protoc --proto_path=. ./data.proto --python_out=../ --grpc_python_out=../

    """

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GetDataService/GetData',
            data__pb2.Posts.SerializeToString,
            data__pb2.CheckReponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class GetMetricServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMetric = channel.unary_unary(
                '/GetMetricService/GetMetric',
                request_serializer=data__pb2.Metrics.SerializeToString,
                response_deserializer=data__pb2.ServerReponse.FromString,
                )


class GetMetricServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMetric(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GetMetricServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMetric': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetric,
                    request_deserializer=data__pb2.Metrics.FromString,
                    response_serializer=data__pb2.ServerReponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GetMetricService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GetMetricService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMetric(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GetMetricService/GetMetric',
            data__pb2.Metrics.SerializeToString,
            data__pb2.ServerReponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
