import os
import grpc
import time
import data_pb2
import data_pb2_grpc
from random import randint

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = data_pb2_grpc.GetDataServiceStub(channel)

        while True:
            try: 
                # Set how many posts to read
                # num_of_posts = random.randint(2,10)
                num_of_posts = randint(2,10)

                data = open("r_dataisbeautiful_posts.csv")

                file_lines = data.readlines()

                size_of_data = len(file_lines)

                # The first line of the file is the headings
                # id, title, score, author, author_flair_text, removed_by, total_awards_received, awarders, created_utc, full_link, num_comments,over_18
                headings = file_lines.pop(0)

                counter = 0

                message = ""

                # Get the amount of posts that was streamed in
                for i in range(num_of_posts):
                    # Take random posts from the dataset
                    line = file_lines[randint(0, size_of_data)]

                    message += line + " @ "
                
                data.close()

                response = stub.GetData(data_pb2.Posts(posts=message))
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