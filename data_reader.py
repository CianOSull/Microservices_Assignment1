from random import randint
import time

def get_posts():
    data = open("r_dataisbeautiful_posts.csv")

    file_lines = data.readlines()

    # The first line of the file is the headings
    # id, title, score, author, author_flair_text, removed_by, total_awards_received, awarders, created_utc, full_link, num_comments,over_18
    headings = file_lines.pop(0)

    size_of_data = len(file_lines)
    
    # Get the amount of posts that was streamed in
    for i in range(size_of_data):
        # Defines how many posts to send
        num_of_posts = randint(2,10)
        
        message = ""

        # Get the amount of posts that was streamed in
        for j in range(num_of_posts):
            # Take random posts from the dataset
            line = file_lines[randint(0, size_of_data)]

            # Construct the message string
            message += line + " @ "
        
        # message += "_" + str(i)

        yield message

        time.sleep(2)
    
    data.close()