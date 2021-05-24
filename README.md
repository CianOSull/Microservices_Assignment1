# Microservices_Assignment1
First assignment about using Docker and GRPC to create 3 microservices.

Project Specification:<br />
Overview<br />
Thus far, we have covered the concept of microservices, bounded contexts and various architectural and integration concepts. We have also covered tools and technologies that can help us build and deploy microservices (see lab documents 1 to 4). This assignment requires that you analyse a requirement and devise an appropriate architecture and implementation.<br />

Problem Description<br />
You are to analyse a stream of data from Reddit. You will simulate the stream of data by reading posts from a data file and serving them through a stream channel to an analytics client. The client should analyse each post as it arrives and calculate 4 different types of metric / result:1. an aggregate metric, such as a total or average2. a rolling 3-minute metric, e.g. sentiment within the last 3 minutes3. a single post which is the most or least of some criteria4. anything else of your choice that is not based on the post titleThere should be a single web page that displays those metrics / results whenever the page is loaded or refreshed. It is up to you how and where the web page gets the data.It is recommended that on average 2 posts per second should be streamed, though there should be some random variability.<br />

The Posts<br />
The file r_dataisbeautiful_posts.csv has more than 190,000 posts in CSV format. All the posts are from the “Data is Beautiful” subreddit. The file was downloaded from https://www.kaggle.com/unanimad/dataisbeautiful and has the following comma separated fields:Id, title, score, author, author_flair_text, removed_by, total_awards_received, awarders, created_utc, full_link, num_comments, over_18There is no post text or comments associated with the posts, just the post title.<br />

The Microservices<br />
There are likely to be at least 3 microservices in your architecture, e.g. one that reads the posts and streams them to a client connection, the client microservice that does the analytics, and a web server microservice that serves out that single web page. There may also be a data storage microservice.<br />

Technical Considerations<br />
Use gRPC as the communication mechanism and use a stream channel to send the posts to the client.Flask is recommended for the web server and web page. A simple table is all that is required. You could consider using a charting library or you could improvise by using hash symbols to build up a bar chart, for example. You have a lot of freedom here.Because a sleep is placed between each tweet read, it should be possible to keep refreshing the web page (either automatically or manually) to see updated metrics / results.Use Docker (with Dockerfiles) for each microservice and use Docker Compose to orchestrate your system. It should be possible to simply enter “docker-compose up” to bring your system up.<br />
