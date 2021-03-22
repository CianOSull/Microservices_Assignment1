import os
import grpc
import time
import data_pb2
import data_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = data_pb2_grpc.GetDataServiceStub(channel)

        while True:
            try: 
                # Set how many posts to read
                # num_of_posts = random.randint(2,10)
                num_of_posts = 1

                data = open("r_dataisbeautiful_posts.csv")

                file_lines = data.readlines()

                # The first line of the file is the headings
                # id, title, score, author, author_flair_text, removed_by, total_awards_received, awarders, created_utc, full_link, num_comments,over_18
                headings = file_lines.pop(0)

                counter = 0

                message = ""

                for line in file_lines:
                    # Counter of posts
                    if(counter == num_of_posts):
                        break

                    message += line + " @ "

                    counter+= 1
                
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