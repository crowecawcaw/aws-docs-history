

# Serverless Web App Real-Time Data Broadcasting
<a name="serverless-realtime-broadcasting"></a>

Publication date: **March 24, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to create a movie voting application using [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html). You can use backend and client-facing real-time broadcasting with managed GraphQL subscriptions over WebSockets.

## Serverless Web App Real-Time Data Broadcasting
<a name="diagram1"></a>

![Architecture diagram showing real-time data broadcasting using AWS AppSync, AWS Lambda, AWS Step Functions, and Amazon DynamoDB with GraphQL subscriptions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/serverless-realtime-broadcasting/images/serverless-realtime-broadcasting.png)


The following steps describe the architecture:

1. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) Events initiates a workflow in Step Functions every 60 seconds.

1. Step Functions triggers Lambda every 10 seconds.

1. Lambda calls The Movie DB API to retrieve metadata for a single random movie from the most popular movies list.

1. Lambda updates the Movie table, zeroes current votes, and upvotes the leaderboard in the Votes table through GraphQL mutations to AppSync.

1. AppSync updates the Movie table in DynamoDB with the single current movie retrieved from Lambda.

1. All connected clients subscribed to the backend mutation see the same current movie poster and synopsis on screen through the broadcast.

1. Clients vote on the current movie during a 10-second window, and can send and receive chat messages in a public chatroom.

1. Lambda updates the leaderboard and client movie votes through AppSync mutations.

1. The public chatroom displays current messages on a pub/sub channel through Local Resolver. Messages are not persisted on backend storage, and only new messages are displayed.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS AppSync Real-Time Reference Architecture on GitHub](https://github.com/aws-samples/appsync-refarch-realtime)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 24, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.