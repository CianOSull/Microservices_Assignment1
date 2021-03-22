import grpc
from concurrent import futures
import time
import data_pb2
import data_pb2_grpc
import threading

class GetDataService(data_pb2_grpc.GetDataService):
    def __init__(self, *args, **kwargs):
        # Store information from the file
        # The author total number of posts so far
        self.author_count = {}
        # Total amount of posts removed in the last 3 minutes
        self.removed_count = 0
        # The highest scroe and title of post
        self.highest_score = 0
        self.highest_score_title = ""
        # Total number of over 18
        self.over_count = 0


    def GetData(self, request, context):
        posts = request.posts

        posts = posts.split(" @ ")
        # Remove lastindex as its not needed
        posts.pop(-1)
    
        for post in posts:
            post_info = post.split(",")

            if 12 < len(post_info):
                for i in range(len(post_info) - 12):
                    post_info[1] += "," + post_info[2]
                    post_info.pop(2)

            # Metric number 1
            author_name = post_info[3]

            if author_name in self.author_count:
                self.author_count[author_name] += 1
            else:
                self.author_count[author_name] = 1

            # Metric number 2
            if post_info[5] != "":
                self.removed_count += 1

            # Metric number 3 
            if self.highest_score < int(post_info[2]):
                self.highest_score = int(post_info[2])
                self.highest_score_title = post_info[1]

            # Metric number 4
            if post_info[11] == 'True\n':
                self.over_count += 1

        for author in self.author_count.keys():
            print("Author Name:", author, "\n Post count:", self.author_count[author])

        print("Total amount of posts removed so far:", self.removed_count)
        print("Post title with highest score:\n", self.highest_score_title, "\nHighest score:", self.highest_score)
        print("Total amount of over_18 accounts so far:", self.over_count)

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



