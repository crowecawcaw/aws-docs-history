

# Integrate Amazon GameLift Servers game client functionality
<a name="gamelift-sdk-client-api"></a>

Integrate Amazon GameLift Servers game hosting functionality into any solution components that need to communicate with the Amazon GameLift Servers service, such as to get game session information or create new game sessions. In most cases, this functionality is built into the backend service component. Add functionality for core tasks, including:
+ Request information and status of active game sessions.
+ Reserve a slot for a new player in an existing game session.
+ Create a new game session for a group of players. 
+ Request matchmaking for one or more players.
+ Provide updated data for existing game sessions.

See [Game client/server interactions with Amazon GameLift Servers](gamelift-sdk-interactions.md) for additional details on how game hosting components interact through the Amazon GameLift Servers SDKs.

## Set up the Amazon GameLift Servers API
<a name="gamelift-sdk-client-api-initialize"></a>

Add the AWS SDK for C\+\+ with Amazon GameLift Servers to a project.

Add code to initialize an Amazon GameLift Servers client and store key settings. This code must run before any code dependent on Amazon GameLift Servers.

1. Set up a client configuration. Use the default client configuration or create a custom client configuration object. For more information, see [AWS::Client::ClientConfiguration](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-core/html/struct_aws_1_1_client_1_1_client_configuration.html) (C\+\+) or [AmazonGameLiftConfig](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/GameLift/TGameLiftConfig.html) (C\#).

   A client configuration specifies a target region and endpoint to use when contacting Amazon GameLift Servers. Region identifies the set of deployed resources (fleets, queues, and matchmakers) to use. The default client configuration sets location to the US East (N. Virginia) Region. To use any other Region, create a custom configuration.

1. Initialize an Amazon GameLift Servers client. Use [Aws::GameLift::GameLiftClient()](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-gamelift/html/class_aws_1_1_game_lift_1_1_game_lift_client.html) (C\+\+) or [AmazonGameLiftClient()](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/GameLift/TGameLiftClient.html) (C\#) with a default client configuration or a custom client configuration.

1. If you're using player sessions, add a mechanism to generate a unique identifier for each player. For more information, see [Generate player IDs](player-sessions-player-identifiers.md).

1. Collect and store the following information:
   + **Target fleet** – If you're manually creating game sessions on a specific fleet, provide a fleet ID or an alias ID that points to the target fleet. If the fleet is multi-location, specify a fleet location. As a best practice, use fleet aliases so that you can switch players from one fleet to another without having to update your backend service.
   + **Target queue** – For games that use multi-fleet queues to place new game sessions, specify the name of the queue to send placement requests to.
   + **AWS credentials** – All calls to Amazon GameLift Servers must provide credentials for the AWS account that hosts the game. You can acquire these credentials by creating a player user, as described in [Set up programmatic access for your game](setting-up-aws-login.md#getting-started-iam-player-user). Depending on how you manage access for the player user, do the following: 
     + If you use a role to manage player user permissions, add code to assume the role before calling an Amazon GameLift Servers API. The request to assume the role returns a set of temporary security credentials. For more information, see [Switching to an IAM role (AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-api.html) in the *IAM User Guide*.
     + If you have long-term security credentials, configure your code to locate and use stored credentials. See [ Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) in the *AWS SDKs and Tools Reference Guide*. For information on storing credentials, see the AWS API references for [(C\+\+)](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-core/html/class_aws_1_1_auth_1_1_a_w_s_credentials.html) and [(.NET)](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-config-creds.html).
     + If you have temporary security credentials, add code to regularly refresh the credentials using the AWS Security Token Service (AWS STS), as described in [Using temporary security credentials with the AWS SDKs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html#using-temp-creds-sdk) in the *IAM User Guide*. The code must request new credentials before the old ones expire.

## Get active game sessions
<a name="gamelift-sdk-client-api-find"></a>

Add code to discover available game sessions and manage game session settings and metadata. 

**Search for active game sessions**

Use [SearchGameSessions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_SearchGameSessions.html) to get information about a specific game session, all active sessions, or sessions that meet a set of search criteria. This call returns a [GameSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameSession.html) object for each active game session that matches your search request. This object contains the DNS name, IP address, and port, which a game client needs to connect to the game session.

Use search criteria to get a filtered list of active game sessions for players to join. For example, you can filter sessions as follows:
+ Exclude game sessions that are full: `CurrentPlayerSessionCount = MaximumPlayerSessionCount`.
+ Choose game sessions based on length of time that the session has been running: Evaluate `CreationTime`.
+ Find game sessions based on a custom game property: `gameSessionProperties.gameMode = "brawl"`.

**Manage game session data**

Use any of the following operations to retrieve or update game session information.
+ [DescribeGameSessionDetails()](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessionDetails.html) – Get a game session's protection status in addition to game session information.
+ [UpdateGameSession()](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameSession.html) – Change a game session's metadata and settings as needed.
+ [GetGameSessionLogUrl](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetGameSessionLogUrl.html) – Access stored game session logs.

## Create game sessions
<a name="gamelift-sdk-client-api-create"></a>

Add code to start new game sessions on your deployed fleets and make them available to players. There are two options for creating game sessions, depending on how your game hosting solution manages game session placements.

**Create a game session with a multi-location queue**

Use [StartGameSessionPlacement](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartGameSessionPlacement.html) to place a request for a new game session in a queue. To use this operation, create a queue. This determines where Amazon GameLift Servers places the new game session. For more information about queues and how to use them, see [Configure game session placement](queues-intro.md).

When creating a game session placement, specify the name of the queue to use, a game session name, a maximum number of concurrent players, and an optional set of game properties. You can also optionally provide a list of players to automatically join the game session. If you include player latency data for relevant Regions, then Amazon GameLift Servers uses this information to place the new game session on a fleet that provides the ideal gameplay experience for the players.

To obtain accurate latency measurements, use Amazon GameLift Servers's UDP ping beacons. These endpoints enable you to measure actual UDP network latency between player devices and potential hosting locations, resulting in more accurate placement decisions than using ICMP pings. For more information on using UDP ping beacons to measure latency, refer to [UDP ping beacons](reference-udp-ping-beacons.md).

Game session placement is an asynchronous process. After you've placed a request, you can let it succeed or time out. You can also cancel the request at any time using [StopGameSessionPlacement](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StopGameSessionPlacement.html). To check the status of your placement request, call [DescribeGameSessionPlacement](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameSessionPlacement.html).

**Create a game session on a specific fleet**

Use [CreateGameSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameSession.html) to create a new session on a specified fleet. This synchronous operation succeeds or fails depending on whether the fleet has resources available to host a new game session. After Amazon GameLift Servers creates the new game session and returns a [GameSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameSession.html) object, you can join players to it.

When you use this operation, provide a fleet ID or alias ID, a session name, and the maximum number of concurrent players for the game. Optionally, you can include a set of game properties. Game properties are defined in an array of key-value pairs.

If you use the Amazon GameLift Servers resource protection feature to limit the number of game sessions that a player can create, then provide the game session creator's player ID.

## Join a player to a game session
<a name="gamelift-sdk-client-api-join"></a>

Add code to reserve a player slot in an active game session and connect game clients to game sessions. This action is available if your game uses player sessions with unique player IDs. For more information about player sessions, see [Amazon GameLift Servers and the player experience](game-sessions-intro.md).

1. 

**Reserve a player slot in a game session**

   To reserve a player slot, create a player session for the game session. There are two ways to do this:
   + If you use [StartGameSessionPlacement](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartGameSessionPlacement.html) or [ StartMatchmaking](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StartMatchmaking.html) to create a game session, you can include one or more players in the request to create player sessions for them in the new game session. 
   + To add players to an existing game session, call [CreatePlayerSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreatePlayerSession.html) or [CreatePlayerSessions](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreatePlayerSessions.html) with a game session ID.

   A player session request must include a unique player ID. For more information, see [Generate player IDs](player-sessions-player-identifiers.md). On receiving the request, Amazon GameLift Servers verifies that the game session is accepting new players and has available player slots. If successful, Amazon GameLift Servers reserves a slot for the player, creates the new player session, and returns a [PlayerSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PlayerSession.html) object. 

   A player session can include a set of custom player data. This data is stored in the newly created player session object. Amazon GameLift Servers passes this object to the game server when the player connects directly to the game session. When requesting multiple player sessions, map each string of player data to a player ID.

1. 

**Connect to a game session**

   Add code to the backend service to retrieve the `PlayerSession` object (such as by calling [DescribePlayerSessions()](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribePlayerSessions.html)) and pass it back to the game client. This object contains the DNS name, IP address, and port. The game client can use this information to establish a direct connection to the server.
   + You can connect using the specified port and the DNS name or IP address assigned to the server process.
   + If your fleets have TLS certificate generation enabled, then connect using the DNS name and port.
   + If your game server validates incoming player connections, then reference the player session ID.

   After making the connection, the game client and server process communicate directly without involving Amazon GameLift Servers. The server maintains communication with Amazon GameLift Servers to report player connection status, health status, and more. 

   If the game server validates incoming players, then it verifies that the player session ID matches a reserved slot in the game session, and either accepts or denies the player connection. When the player disconnects, the server process reports the dropped connection.

## Pass custom game data to a game session
<a name="game-properties"></a>

Your game client can pass data to a game session. When you create a game session, you can include a set of game properties (key-value pairs) or game session data (string values) in the request. You can also update an existing game session with new or updated game data. This data is passed to the game server process that is hosting the game session, for use by the game server code. You cannot delete game properties. 

As an example, let's say that your game defines difficulty levels: `Novice`, `Easy`, `Intermediate`, and `Expert`. A player chooses to join an `Easy`, game. Your game client, through the backend service, requests a new game session with the following game property: `{"Key": "Difficulty", "Value":"Easy"}`. In response, Amazon GameLift Servers prompts an available game server to start a new game session and passes the `GameSession` object. The game server process uses the game property provided to set the game session's difficulty level. 

### Learn more
<a name="w2aab9c13c11c17b7"></a>
+ [GameProperty data type](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameProperty.html) 
+ [SearchGameSessions() examples](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_SearchGameSessions.html#API_SearchGameSessions_Examples) 
+ [UpdateGameSession() GameProperties parameter](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameSession.html#gamelift-UpdateGameSession-request-GameProperties) 