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

    # Time Count
    start = time.time()
    extra = False

    with grpc.insecure_channel('server:50051') as channel:
        stub = data_pb2_grpc.GetDataServiceStub(channel)

        for data in data_reader.get_posts():
            data_split = data.split(" @ ")
            # Last index is always empty so remove it
            data_split.pop(-1)
            
            for post in data_split:
                metrics = "<br>"

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
                
                end = time.time()
                amount_of_time = end - start
                if 180 < amount_of_time:
                    start = time.time()
                    extra = True

                metrics += "=============================<br>"
                metrics += "Time counter: " + str(amount_of_time) + "<br>"
                metrics += "=============================<br>"

                # Metric 1
                metrics += "=============================<br>"
                # metrics += "Total count of posts for each author:<br>"
                for author_name in author_count.keys():
                    metrics += " " + author_name + ": " + str(author_count[author_name]) + " @ "
                
                metrics += str(author_count) + "<br>"
                metrics += "=============================<br>"

                if extra:
                    # Metric 2 
                    metrics += "Number of removed posts in last 3 minutes: " + str(removed_count) + "<br>"
                    
                    metrics += "=============================<br>"

                    # Metric 3
                    metrics += "Highest score in last 3 minutes: " + str(highest_score) + "<br>"
                    metrics += "Title of Highest Score in last 3 minutes:\n" + highest_score_title + "<br>"
                    
                    metrics += "=============================<br>"

                # Metric 4
                metrics += "Over 18 count: " + str(over_count) + "<br>"
                metrics += "=============================<br>"

                response = stub.GetData(data_pb2.Posts(posts=metrics))
                
                # Only reset  
                if extra:
                    # Reset it 
                    extra = False

            # response = stub.GetData(data_pb2.Posts(posts="Passed in String"))   
            # response = stub.GetData(data_pb2.Posts(posts=str(data_posts)))

        print("Client.py: ", response.received)
        # time.sleep(randint(1, 6))
        time.sleep(120)

if __name__ == "__main__":
    logging.basicConfig()
    run()