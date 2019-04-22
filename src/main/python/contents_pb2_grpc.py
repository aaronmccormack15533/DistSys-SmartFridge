# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import contents_pb2 as contents__pb2


class ContentsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addfood = channel.unary_unary(
        '/SmartFridge.src.main.python.Contents/addfood',
        request_serializer=contents__pb2.food.SerializeToString,
        response_deserializer=contents__pb2.food.FromString,
        )


class ContentsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addfood(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ContentsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addfood': grpc.unary_unary_rpc_method_handler(
          servicer.addfood,
          request_deserializer=contents__pb2.food.FromString,
          response_serializer=contents__pb2.food.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SmartFridge.src.main.python.Contents', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
