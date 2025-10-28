# Add Amazon GameLift Servers to your game client

Integrate Amazon GameLift Servers into game components that need game session information, create new
game sessions, and add players to games. Depending on your game architecture, this
functionality is in backend services that handle tasks such as player authentication,
matchmaking, or game session placement.

###### Note

For detailed information about how to set up matchmaking for your game, see the [Amazon GameLift Servers FlexMatch Developer
Guide](../flexmatchguide.md "../flexmatchguide.md").

## Set up Amazon GameLift Servers on a backend

service

Add code to initialize an Amazon GameLift Servers client and store key settings. This code must run
before any code dependent on Amazon GameLift Servers.

1. Set up a client configuration. Use the default client configuration or create
   a custom client configuration object. For more information, see [AWS::Client::ClientConfiguration](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-core/html/struct_aws_1_1_client_1_1_client_configuration.html "https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-core/html/struct_aws_1_1_client_1_1_client_configuration.html") (C++) or [AmazonGameLiftConfig](../../../sdkfornet/v3/apidocs/items/GameLift/TGameLiftConfig.md "../../../sdkfornet/v3/apidocs/items/GameLift/TGameLiftConfig.md") (C#).

A client configuration specifies a target region and endpoint to use when
contacting Amazon GameLift Servers. Region identifies the set of deployed resources (fleets,
queues, and matchmakers) to use. The default client configuration sets location
to the US East (N. Virginia) Region. To use any other Region, create a custom
configuration. 2. Initialize an Amazon GameLift Servers client. Use [Aws::GameLift::GameLiftClient()](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-gamelift/html/class_aws_1_1_game_lift_1_1_game_lift_client.html "https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-gamelift/html/class_aws_1_1_game_lift_1_1_game_lift_client.html") (C++) or [AmazonGameLiftClient()](../../../sdkfornet/v3/apidocs/items/GameLift/TGameLiftClient.md "../../../sdkfornet/v3/apidocs/items/GameLift/TGameLiftClient.md") (C#) with a default client configuration or
a custom client configuration. 3. Add a mechanism to generate a unique identifier for each player. For more
information, see [Generate player IDs](player-sessions-player-identifiers.md "player-sessions-player-identifiers.md"). 4. Collect and store the following information:

    * **Target fleet** – Many Amazon GameLift Servers API
     requests must specify a fleet. To do so, use either a fleet ID or an
     alias ID that points to the target fleet. As a best practice, use fleet
     aliases so that you can switch players from one fleet to another without
     having to update your backend services.
    * **Target queue** – For games that
     use multi-fleet queues to place new game sessions, specify the name of
     the queue to use.
    * **AWS credentials** – All calls
     to Amazon GameLift Servers must provide credentials for the AWS account that hosts the
     game. You acquire these credentials by creating a player user, as
     described in [Set up programmatic access for your
     game](setting-up-aws-login.md#getting-started-iam-player-user "setting-up-aws-login.md#getting-started-iam-player-user"). Depending on how
     you manage access for the player user, do the following:




    	+ If you use a role to manage player user permissions, add code
    	 to assume the role before calling an Amazon GameLift Servers API. The request to
    	 assume the role returns a set of temporary security credentials.
    	 For more information, see  [Switching to an IAM role (AWS API)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-api.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-api.md") in the
    	 *IAM User Guide*.
    	+ If you have long-term security credentials, configure your
    	 code to locate and use stored credentials. See [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in in the
    	 *AWS SDKs and Tools Reference Guide*.
    	 For information on storing credentials, see theAWS API
    	 references for [(C++)](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-core/html/class_aws_1_1_auth_1_1_a_w_s_credentials.html "https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-core/html/class_aws_1_1_auth_1_1_a_w_s_credentials.html") and [(.NET)](../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md "../../../sdk-for-net/v3/developer-guide/net-dg-config-creds.md").
    	+ If you have temporary security credentials, add code to
    	 regularly refresh the credentials using the AWS Security Token Service
    	 (AWS STS), as described in [Using temporary security credentials with the AWS
    	 SDKs](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md#using-temp-creds-sdk "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md#using-temp-creds-sdk") in the *IAM User Guide*. The code must request new
    	 credentials before the old ones expire.

## Get game sessions

Add code to discover available game sessions and manage game session settings and
metadata.

**Search for active game sessions**

Use [SearchGameSessions](../apireference/API_SearchGameSessions.md "../apireference/API_SearchGameSessions.md") to get information about a specific game session, all
active sessions, or sessions that meet a set of search criteria. This call returns a
[GameSession](../apireference/API_GameSession.md "../apireference/API_GameSession.md") object for each active game session that matches your search
request.

Use search criteria to get a filtered list of active game sessions for players to
join. For example, you can filter sessions as follows:

- Exclude game sessions that are full: `CurrentPlayerSessionCount =
MaximumPlayerSessionCount`.
- Choose game sessions based on length of time that the session has been
  running: Evaluate `CreationTime`.
- Find game sessions based on a custom game property:
  `gameSessionProperties.gameMode = "brawl"`.

**Manage game sessions**

Use any of the following operations to retrieve or update game session
information.

- [DescribeGameSessionDetails()](../apireference/API_DescribeGameSessionDetails.md "../apireference/API_DescribeGameSessionDetails.md") – Get a game session's
  protection status in addition to game session information.
- [UpdateGameSession()](../apireference/API_UpdateGameSession.md "../apireference/API_UpdateGameSession.md") – Change a game session's metadata and
  settings as needed.
- [GetGameSessionLogUrl](../apireference/API_GetGameSessionLogUrl.md "../apireference/API_GetGameSessionLogUrl.md") – Access stored game session
  logs.

## Create game sessions

Add code to start new game sessions on your deployed fleets and make them available to
players. There are two options for creating game sessions, depending on whether you're
deploying your game in multiple AWS Regions or in a single Region.

**Create a game session in a multi-location
queue**

Use [StartGameSessionPlacement](../apireference/API_StartGameSessionPlacement.md "../apireference/API_StartGameSessionPlacement.md") to place a request for a new game session in a
queue. To use this operation, create a queue. This determines where Amazon GameLift Servers places the new
game session. For more information about queues and how to use them, see [Managing game session placement with Amazon GameLift Servers queues](queues-intro.md "queues-intro.md").

When creating a game session placement, specify the name of the queue to use, a game
session name, a maximum number of concurrent players, and an optional set of game
properties. You can also optionally provide a list of players to automatically join the
game session. If you include player latency data for relevant Regions, then Amazon GameLift Servers uses
this information to place the new game session on a fleet that provides the ideal
gameplay experience for the players.

To obtain accurate latency measurements, use Amazon GameLift Servers's UDP ping beacons. These
endpoints enable you to measure actual UDP network latency between player devices and
potential hosting locations, resulting in more accurate placement decisions than using
ICMP pings. For more information on using UDP ping beacons to measure latency, refer to [UDP ping beacons](reference-udp-ping-beacons.md "reference-udp-ping-beacons.md").

Game session placement is an asynchronous process. After you've placed a request, you
can let it succeed or time out. You can also cancel the request at any time using [StopGameSessionPlacement](../apireference/API_StopGameSessionPlacement.md "../apireference/API_StopGameSessionPlacement.md"). To check the status of your placement request,
call [DescribeGameSessionPlacement](../apireference/API_DescribeGameSessionPlacement.md "../apireference/API_DescribeGameSessionPlacement.md").

**Create a game session on a specific fleet**

Use [CreateGameSession](../apireference/API_CreateGameSession.md "../apireference/API_CreateGameSession.md") to create a new session on a specified fleet. This
synchronous operation succeeds or fails depending on whether the fleet has resources
available to host a new game session. After Amazon GameLift Servers creates the new game session and
returns a [GameSession](../apireference/API_GameSession.md "../apireference/API_GameSession.md") object,
you can join players to it.

When you use this operation, provide a fleet ID or alias ID, a session name, and the
maximum number of concurrent players for the game. Optionally, you can include a set of
game properties. Game properties are defined in an array of key-value pairs.

If you use the Amazon GameLift Servers resource protection feature to limit the number of game sessions
that one player can create, then provide the game session creator's player ID.

## Join a player to a game session

Add code to reserve a player slot in an active game session and connect game clients
to game sessions.

1. ###### Reserve a player slot in a game session

To reserve a player slot, create a new player session for the game session.
For more information about player sessions, see [How players connect to games](game-sessions-intro.md "game-sessions-intro.md").

There are two ways to create new player sessions:

    * Use [StartGameSessionPlacement](../apireference/API_StartGameSessionPlacement.md "../apireference/API_StartGameSessionPlacement.md") to reserve slots for one or more
     players in the new game session.
    * Reserve player slots for one or more players using [CreatePlayerSession](../apireference/API_CreatePlayerSession.md "../apireference/API_CreatePlayerSession.md") or [CreatePlayerSessions](../apireference/API_CreatePlayerSessions.md "../apireference/API_CreatePlayerSessions.md") with a game session ID.

Amazon GameLift Servers first verifies that the game session is accepting new players and has
available player slots. If successful, Amazon GameLift Servers reserves a slot for the player,
creates the new player session, and returns a [PlayerSession](../apireference/API_PlayerSession.md "../apireference/API_PlayerSession.md") object. This object contains the DNS name, IP
address, and port that a game client needs to connect to the game
session.

A player session request must include a unique ID for each player. For more
information, see [Generate player IDs](player-sessions-player-identifiers.md "player-sessions-player-identifiers.md").

A player session can include a set of custom player data. This data is stored
in the newly created player session object, which you can retrieve by calling
[DescribePlayerSessions()](../apireference/API_DescribePlayerSessions.md "../apireference/API_DescribePlayerSessions.md"). Amazon GameLift Servers also passes this object to the game
server when the player connects directly to the game session. When requesting
multiple player sessions, provide a string of player data for each player that's
mapped to the player ID in the request. 2. ###### Connect to a game session

Add code to the game client to retrieve the `PlayerSession` object,
which contains the game session's connection information. Use this information
to establish a direct connection to the server.

    * You can connect using the specified port and the DNS name or IP
     address assigned to the server process.
    * If your fleets have TLS certificate generation enabled, then connect
     using the DNS name and port.
    * If your game server validates incoming player connections, then
     reference the player session ID.

After making the connection, the game client and server process communicate
directly without involving Amazon GameLift Servers. The server maintains communication with Amazon GameLift Servers
to report player connection status, health status, and more. If the game server
validates incoming players, then it verifies that the player session ID matches
a reserved slot in the game session, and accepts or denies the player
connection. When the player disconnects, the server process reports the dropped
connection.

## Use game session properties

Your game client can pass data into a game session by using a game property.
Game properties are key-value pairs that your game server can add, read, list, and change.
You can pass in a game property when you're creating a new game session, or later when the game session is active.
A game session can contain up to 16 game properties.
You cannot delete game properties.

For example, your game offers these difficulty levels: `Novice`, `Easy`, `Intermediate`, and `Expert`.
A player chooses `Easy`, and then begins the game.
Your game client requests new game session from Amazon GameLift Servers by using either `StartGameSessionPlacement` or `CreateGameSession` as explained in the preceding sections.
In the request, the client passes this : `{"Key": "Difficulty", "Value":"Easy"}`.

In response to the request, Amazon GameLift Servers creates a `GameSession` object that contains the specified game property.
Amazon GameLift Servers then instructs an available game server to start the new game session and passes the `GameSession` object.
The game server starts a game session with a `Difficulty` of `Easy`.

### Learn more

- [GameProperty data type](../apireference/API_GameProperty.md "../apireference/API_GameProperty.md")
- [SearchGameSessions() examples](../apireference/API_SearchGameSessions.md#API_SearchGameSessions_Examples "../apireference/API_SearchGameSessions.md#API_SearchGameSessions_Examples")
- [UpdateGameSession() GameProperties parameter](../apireference/API_UpdateGameSession.md#gamelift-UpdateGameSession-request-GameProperties "../apireference/API_UpdateGameSession.md#gamelift-UpdateGameSession-request-GameProperties")
