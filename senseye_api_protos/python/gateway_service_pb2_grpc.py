# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import compute_service_pb2 as compute__service__pb2


class GatewayStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AnalyzeVideoStream = channel.stream_stream(
        '/senseye.gateway.Gateway/AnalyzeVideoStream',
        request_serializer=compute__service__pb2.VideoStreamRequest.SerializeToString,
        response_deserializer=compute__service__pb2.VideoStreamResponse.FromString,
        )
    self.AnalyzeVideo = channel.unary_stream(
        '/senseye.gateway.Gateway/AnalyzeVideo',
        request_serializer=compute__service__pb2.VideoStaticRequest.SerializeToString,
        response_deserializer=compute__service__pb2.VideoStreamResponse.FromString,
        )


class GatewayServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AnalyzeVideoStream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AnalyzeVideo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GatewayServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AnalyzeVideoStream': grpc.stream_stream_rpc_method_handler(
          servicer.AnalyzeVideoStream,
          request_deserializer=compute__service__pb2.VideoStreamRequest.FromString,
          response_serializer=compute__service__pb2.VideoStreamResponse.SerializeToString,
      ),
      'AnalyzeVideo': grpc.unary_stream_rpc_method_handler(
          servicer.AnalyzeVideo,
          request_deserializer=compute__service__pb2.VideoStaticRequest.FromString,
          response_serializer=compute__service__pb2.VideoStreamResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'senseye.gateway.Gateway', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
