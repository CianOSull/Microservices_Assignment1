import os
import grpc
import time
import data_pb2
import data_pb2_grpc
from random import randint

import logging

import data_reader

def run():
    # Store information from the file
    # The author total number of posts so far
    author_count = {}
    # Total amount of posts removed in the last 3 minutes
    removed_count = 0
    # The highest score and title of post
    highest_score = 0
    highest_score_title = ""
    # Total number of over 18
    over_count = 0

    while True:
        with grpc.insecure_channel('server:50051') as channel:
            stub = data_pb2_grpc.GetDataServiceStub(channel)

            for data in data_reader.get_posts():
                data_split = data.split(" @ ")
                # Last index is always empty so remove it
                data_split.pop(-1)
                
                for post in data_split:
                    metrics = ""


                    post_info = post.split(",")
                    
                    if 12 < len(post_info):
                        diff = len(post_info) - 12

                        for i in range(diff):
                            post_info[1] += "," + post_info[2]
                            post_info.pop(2)

                    # Metric number 1
                    author = post_info[3]

                    if author in author_count:
                        author_count[author] += 1
                    else:
                        author_count[author] = 1

                    # Metric number 2
                    if post_info[5] != "":
                        removed_count += 1

                    # Metric number 3 
                    if highest_score < int(post_info[2]):
                        highest_score = int(post_info[2])
                        highest_score_title = post_info[1]

                    # Metric number 4
                    if post_info[11] == 'True\n':
                        over_count += 1

                    # Metric 1
                    metrics += str(author_count) + "\n"
                    # Metric 2 
                    metrics += "Number of removed posts in last 3 minutes: " + str(removed_count) + "\n"
                    # Metric 3
                    metrics += "Highest score in last 3 minutes: " + str(highest_score) + "\n"
                    metrics += "Title of Highest Score in last 3 minutes:\n" + highest_score_title + "\n"
                    # Metric 4
                    metrics += "Over 18 count: " + str(over_count) + "\n"

                    response = stub.GetData(data_pb2.Posts(posts="metrics"))

            # response = stub.GetData(data_pb2.Posts(posts="Passed in String"))   
            # response = stub.GetData(data_pb2.Posts(posts=str(data_posts)))

        print("Client.py: ", response.received)
        # time.sleep(randint(1, 6))
        time.sleep(120)

if __name__ == "__main__":
    logging.basicConfig()
    run()