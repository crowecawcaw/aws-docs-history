

# Session-based game server hosting with serverless backend
<a name="session-based-game-server-hosting-with-serverless-backend"></a>

 When developing an architecture for your game, consider the features and capabilities you need and the level of operational management overhead that you are prepared to own. To provide the best balance between ease of operations and flexibility, you can build your game using managed services from cloud providers. Managed services give you the control to develop and customize your own custom game features, while also reducing your burden to deploy and manage infrastructure. 

 Hosting a session-based multiplayer game requires having server infrastructure to host the game server processes as well as a scalable backend for matchmaking and session management. The following reference architecture shows how Amazon GameLift managed hosting and a serverless backend can be used to manage your session-based games. 

![Amazon GameLift managed hosting for session-based games](http://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/images/image2.png)


 The diagram describes the process of getting players into games running on GameLift managed game hosting. It includes the following steps: 

1.  The game client requests an Amazon Cognito identity from an Amazon Cognito identity pool. This can optionally be connected to external identity providers. 

1.  The game client receives temporary access credentials and requests a game session through an Amazon API Gateway by signing the request with the Amazon Cognito credentials. 

1.  API Gateway invokes an AWS Lambda function. 

1.  The Lambda function requests player data from an Amazon DynamoDB table. The Amazon Cognito identity is used to securely request the correct player data because the authenticated identity is provided in the request context data. 

1.  Using the correct player data for additional information (like player skill level), the Lambda function requests a match through GameLift FlexMatch matchmaking. You can define a FlexMatch matchmaking configuration with JSON-based configuration documents. The game client can generate latency metrics by pinging server endpoints in various Regions, and the latency data can be used to support latency-based matchmaking. 

1.  After FlexMatch matches a suitable group of players with suitable latency to a Region, it requests a game session placement through a GameLift queue. The queue contains fleets with one or more registered Region locations. 

1.  When the session is placed on one of the fleet's locations, an event notification is sent to an Amazon SNS topic. 

1.  A Lambda function will receive the Amazon SNS event and process it. 

1.  If the Amazon SNS message is a MatchmakingSucceeded event, the Lambda function writes the result to DynamoDB with the server port and IP address. A time-to-live (TTL) value is used to make sure that matchmaking tickets are deleted from DynamoDB when they no longer needed. 

1.  The game client makes a signed request to API Gateway to check the status of the matchmaking ticket on a specific interval. 

1.  API Gateway invokes a Lambda function that checks the matchmaking ticket status. 

1.  The Lambda function checks DynamoDB to determine whether the ticket has succeeded. If it has succeeded, the Lambda function sends the IP address, port, and the player session ID back to the client. If the ticket failed, the Lambda function sends a response declaring that the match is not ready. 

1.  The game client connects to the game server using TCP or UDP by using the port and IP address provided by the backend. It sends the player session ID to the game server, and the game server validates it using the Amazon GameLift Server SDK. 

 Alternatively, you can modify the preceding architecture to use API Gateway WebSockets with Amazon GameLift. In this approach, communication between the game client and your game backend service occurs using a [WebSocket-based implementation](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_websockets.html). This implementation can be used so that the game backend Lambda function initiates a server-side message to the game client over a WebSocket rather than implementing a polling model. 