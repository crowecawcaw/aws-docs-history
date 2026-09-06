

# Multiplayer Session-based Game Hosting on AWS
<a name="multiplayer-session-based-game-hosting-on-aws"></a>

Publication date: **September 1, 2022 ([Diagram history](#diagram-history))**

This architecture enables you to use Amazon GameLift Servers multi-Region fleets and a serverless backend solution to host a session-based multiplayer game.

## Multiplayer Session-based Game Hosting on AWS Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how to use Amazon GameLift Servers multi-Region fleets and a serverless backend solution to host a session-based multiplayer game.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/multiplayer-session-based-game-hosting-on-aws/images/multiplayer-session-based-game-hosting-on-aws.png)


1. The game client requests an **Amazon Cognito** identity and temporary AWS credentials.

1. The client signs a matchmaking request to **API Gateway** with the temporary credentials. The request includes client latency information to supported AWS Regions.

1. **API Gateway** calls an **AWS Lambda** function with player identity information.

1. The **Lambda** function gets the player skill level from a **DynamoDB** table.

1. The **Lambda** function requests matchmaking from **Amazon GameLift Servers FlexMatch** with player skill and latency data.

1. **Amazon GameLift Servers FlexMatch** creates a match with multiple players, and an **Amazon GameLift Servers** queue allocates a session in an **Amazon GameLift Servers**fleet location based on the latency data.

1. **Amazon GameLift Servers FlexMatch** publishes an event to **Amazon SNS** on matchmaking success.

1. **Amazon SNS** triggers a subscribed **Lambda** function for ticket processing.

1. The **Lambda** function stores the ticket result in a **DynamoDB** table.

1. The game client polls for matchmaking success on a defined interval from **API Gateway**.

1. The **Lambda** function checks matchmaking information from the **DynamoDB** table and informs the client of a successful match by returning server IP, port, and player session ID.

1. The client connects directly to the server and sends the player session ID. The **Amazon GameLift Servers Server SDK** is used to validate the player session.

1. Game servers send logs and metrics to **Amazon CloudWatch** with the **CloudWatch** agent.

## Further reading
<a name="further-reading"></a>

 For additional information, see the following resources: 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | September 1, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.