import grpc
from concurrent import futures
import time

import contents_pb2 as contents_pb2
import contents_pb2_grpc as contents_pb2_grpc

class ContentsServicer(contents_pb2_grpc.ContentsServicer):
    def __init__(self, *args, **kwargs):
        self.server_port = 8080

    def addfood(self, request, context):
        totalfood = []
        added_food = request.name

        totalfood.append(added_food)

        print("added " + added_food)

        return contents_pb2.FoodResp(added_food)

    def start_server(self):
        fridge_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        contents_pb2_grpc.add_ContentsServicer_to_server(ContentsServicer(), fridge_server)

        fridge_server.add_insecure_port('[::]:{}'.format(self.server_port))

        fridge_server.start()
        print('------------------')
        print('Server starting')
        print('------------------')

        try:
            while True:
                time.sleep(60*60*60)
        except KeyboardInterrupt:
            fridge_server.stop(0)
            print('------------------')
            print('Server stopped')
            print('------------------')

curr_server = ContentsServicer()
curr_server.start_server()
