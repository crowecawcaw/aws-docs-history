# C# server SDK 5.x for Amazon GameLift Servers -- Data types

Use the Amazon GameLift Servers C# server SDK 5.x reference to integrate your multiplayer game for
hosting with Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server with the server SDK](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md"). If you're
using the Amazon GameLift Servers plugin for Unity, see also [Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md "unity-plug-in.md").

[C# server SDK 5.x for Amazon GameLift Servers -- Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md")

###### Data types

- [LogParameters](#integration-server-sdk5-csharp-dataypes-log "#integration-server-sdk5-csharp-dataypes-log")
- [MetricsParameters](#integration-server-sdk5-csharp-datatypes-metricsparameters "#integration-server-sdk5-csharp-datatypes-metricsparameters")
- [ProcessParameters](#integration-server-sdk5-csharp-dataypes-process "#integration-server-sdk5-csharp-dataypes-process")
- [UpdateGameSession](#integration-server-sdk5-csharp-dataypes-updategamesession "#integration-server-sdk5-csharp-dataypes-updategamesession")
- [GameSession](#integration-server-sdk5-csharp-dataypes-gamesession "#integration-server-sdk5-csharp-dataypes-gamesession")
- [ServerParameters](#integration-server-sdk5-csharp-dataypes-serverparameters "#integration-server-sdk5-csharp-dataypes-serverparameters")
- [StartMatchBackfillRequest](#integration-server-sdk5-csharp-dataypes-startmatchbackfillrequest "#integration-server-sdk5-csharp-dataypes-startmatchbackfillrequest")
- [Player](#integration-server-sdk5-csharp-dataypes-player "#integration-server-sdk5-csharp-dataypes-player")
- [DescribePlayerSessionsRequest](#integration-server-sdk5-csharp-dataypes-playersessions "#integration-server-sdk5-csharp-dataypes-playersessions")
- [StopMatchBackfillRequest](#integration-server-sdk5-csharp-dataypes-stopmatchbackfillrequest "#integration-server-sdk5-csharp-dataypes-stopmatchbackfillrequest")
- [GetFleetRoleCredentialsRequest](#integration-server-sdk5-csharp-dataypes-getfleetrolecredentialsrequest "#integration-server-sdk5-csharp-dataypes-getfleetrolecredentialsrequest")
- [AttributeValue](#integration-server-sdk5-csharp-datatypes-attributevalue "#integration-server-sdk5-csharp-datatypes-attributevalue")
- [AwsStringOutcome](#integration-server-sdk5-csharp-datatypes-awsstringoutcome "#integration-server-sdk5-csharp-datatypes-awsstringoutcome")
- [GenericOutcome](#integration-server-sdk5-csharp-datatypes-genericoutcome "#integration-server-sdk5-csharp-datatypes-genericoutcome")
- [MetricsManagerOutcome](#integration-server-sdk5-csharp-datatypes-metricsmanageroutcome "#integration-server-sdk5-csharp-datatypes-metricsmanageroutcome")
- [DescribePlayerSessionsOutcome](#integration-server-sdk5-csharp-datatypes-describeplayersessionsoutcome "#integration-server-sdk5-csharp-datatypes-describeplayersessionsoutcome")
- [DescribePlayerSessionsResult](#integration-server-sdk5-csharp-datatypes-describeplayersessionsresult "#integration-server-sdk5-csharp-datatypes-describeplayersessionsresult")
- [PlayerSession](#integration-server-sdk5-csharp-datatypes-playersession "#integration-server-sdk5-csharp-datatypes-playersession")
- [StartMatchBackfillOutcome](#integration-server-sdk5-csharp-datatypes-startmatchbackfilloutcome "#integration-server-sdk5-csharp-datatypes-startmatchbackfilloutcome")
- [StartMatchBackfillResult](#integration-server-sdk5-csharp-datatypes-startmatchbackfillresult "#integration-server-sdk5-csharp-datatypes-startmatchbackfillresult")
- [GetComputeCertificateOutcome](#integration-server-sdk5-csharp-datatypes-getcomputecertificateoutcome "#integration-server-sdk5-csharp-datatypes-getcomputecertificateoutcome")
- [GetComputeCertificateResult](#integration-server-sdk5-csharp-datatypes-getcomputecertificateresult "#integration-server-sdk5-csharp-datatypes-getcomputecertificateresult")
- [GetFleetRoleCredentialsOutcome](#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsoutcome "#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsoutcome")
- [GetFleetRoleCredentialsResult](#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsresult "#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsresult")
- [ListContainersNetworkInfoOutcome](#integration-server-sdk5-csharp-datatypes-listcontainersnetworkinfooutcome "#integration-server-sdk5-csharp-datatypes-listcontainersnetworkinfooutcome")
- [ListContainersNetworkInfoResult](#integration-server-sdk5-csharp-datatypes-listcontainersnetworkinforesult "#integration-server-sdk5-csharp-datatypes-listcontainersnetworkinforesult")
- [ContainerNetworkInfo](#integration-server-sdk5-csharp-datatypes-containernetworkinfo "#integration-server-sdk5-csharp-datatypes-containernetworkinfo")
- [AwsDateTimeOutcome](#integration-server-sdk5-csharp-datatypes-awsdatetimeoutcome "#integration-server-sdk5-csharp-datatypes-awsdatetimeoutcome")
- [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")
- [Enums](#integration-server-sdk5-csharp-datatypes-enums "#integration-server-sdk5-csharp-datatypes-enums")

## LogParameters

Use this data type to identify files generated during a game session that you
want the game server to upload to Amazon GameLift Servers after the game session ends. The game server
communicates `LogParameters to` Amazon GameLift Servers in a [ProcessReady()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-processready "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-processready") call.

|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Properties** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| LogPaths       | The list of directory paths to game server log files you want<br>Amazon GameLift Servers to store for future access. The server process generates these<br>files during each game session. You define file paths and names in<br>your game server and store them in the root game build directory.<br>The log paths must be absolute. For example, if your game build<br>stores game session logs in a path like<br>`MyGame\sessionLogs\`, then the path would be<br>`c:\game\MyGame\sessionLogs` on a Windows<br>instance.<br>**Type:**<br>`List<String>`<br>**Required:*<br>• No |

## MetricsParameters

Use this data type to configure metrics collection and crash reporting for the game server.
The game server communicates `MetricsParameters` to Amazon GameLift Servers in an [InitMetrics()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initmetrics "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initmetrics") call.

|                   |                                                                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Properties**    | **Description**                                                                                                          |
| StatsdHost        | The hostname or IP address of the StatsD server for metrics collection.<br>**Type:**<br>`String`<br>**Required:*<br>• No |
| StatsdPort        | The port number of the StatsD server for metrics collection.<br>**Type:**<br>`Integer`<br>**Required:*<br>• No           |
| CrashReporterHost | The hostname or IP address of the crash reporter server.<br>**Type:**<br>`String`<br>**Required:*<br>• No                |
| CrashReporterPort | The port number of the crash reporter server.<br>**Type:**<br>`Integer`<br>**Required:*<br>• No                          |
| FlushIntervalMs   | The interval in milliseconds for flushing metrics data to the server.<br>**Type:**<br>`Integer`<br>**Required:*<br>• No  |
| MaxPacketSize     | The maximum size in bytes for metrics packets sent to the server.<br>**Type:**<br>`Integer`<br>**Required:*<br>• No      |

## ProcessParameters

This data type contains the set of parameters sent to Amazon GameLift Servers in a [ProcessReady()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-processready "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-processready") call.

|                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Properties**      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| LogParameters       | The object with a list of directory paths to game session log<br>files.**Type:**<br>`Aws::GameLift::Server::LogParameters`**Required:**<br>Yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| OnHealthCheck       | The name of callback function that Amazon GameLift Servers invokes to request a health<br>status report from the server process. Amazon GameLift Servers calls this function every<br>60 seconds. After calling this function Amazon GameLift Servers waits 60 seconds for a<br>response, if none is received, Amazon GameLift Servers records the server process as<br>unhealthy.**Type:**<br>`void OnHealthCheckDelegate()`**Required:*<br>• Yes                                                                                                                                                                                                                                                                    |
| OnProcessTerminate  | The name of callback function that Amazon GameLift Servers invokes to force the server<br>process to shut down. After calling this function, Amazon GameLift Servers waits five<br>minutes for the server process to shut down and respond with a [ProcessEnding()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-processending "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-processending") call<br>before it shuts down the server process.**Type:**<br>`void OnProcessTerminateDelegate()`**Required:*<br>• Yes                                                                                                                                            |
| OnStartGameSession  | The name of callback function that Amazon GameLift Servers invokes to activate a new<br>game session. Amazon GameLift Servers calls this function in response to the client<br>request [CreateGameSession](../apireference/API_CreateGameSession.md "../apireference/API_CreateGameSession.md"). The callback function takes a [GameSession](#integration-server-sdk5-csharp-dataypes-gamesession "#integration-server-sdk5-csharp-dataypes-gamesession") object.**Type:**<br>`void OnStartGameSessionDelegate(GameSession)`**Required:*<br>• Yes                                                                                                                                                                     |
| OnUpdateGameSession | The name of callback function that Amazon GameLift Servers invokes to pass an updated<br>game session object to the server process. Amazon GameLift Servers calls this function<br>when a match backfill request has been processed to provide updated<br>matchmaker data. It passes a [GameSession](#integration-server-sdk5-csharp-dataypes-gamesession "#integration-server-sdk5-csharp-dataypes-gamesession") object, a status update<br>(`updateReason`), and the match backfill ticket<br>ID.**Type:*<br>• void<br>OnUpdateGameSessionDelegate([UpdateGameSession](#integration-server-sdk5-csharp-dataypes-updategamesession "#integration-server-sdk5-csharp-dataypes-updategamesession"))**Required:**<br>No |
| Port                | The port number that the server process listens on for new player<br>connections. The value must fall into the port range configured for any<br>fleet deploying this game server build. This port number is included in<br>game session and player session objects, which game sessions use when<br>connecting to a server process.**Type:**<br>`Integer`**Required:*<br>• Yes                                                                                                                                                                                                                                                                                                                                        |

## UpdateGameSession

Updated information for a game session object, includes the reason that the game
session was updated. If the update is related to a match backfill action, this data type
includes the backfill ticket ID.

| Properties       | **Description**                                                                                                                                                                                                                                                                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSession      | A [GameSession](#integration-server-sdk5-csharp-dataypes-gamesession "#integration-server-sdk5-csharp-dataypes-gamesession") object. The<br>`GameSession` object contains properties describing a<br>game session. **Type:**<br>`GameSession GameSession()`**Required:*<br>• Yes |
| UpdateReason     | The reason that the game session is being updated.**Type:**<br>`UpdateReason UpdateReason()`**Required:*<br>• Yes                                                                                                                                                                |
| BackfillTicketId | The ID of the backfill ticket attempting to update the game<br>session.**Type:**<br>`String`**Required:*<br>• Yes                                                                                                                                                                |

## GameSession

Details of a game session.

| Properties                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSessionId             | A unique identifier for the game session. A game session ARN has<br>the following format:<br>`arn:aws:gamelift:<region>::gamesession/<fleet<br>ID>/<custom ID string or idempotency token>`.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                  |
| Name                      | A descriptive label of the game session.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                      |
| FleetId                   | A unique identifier for the fleet that the game session is running<br>on.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                     |
| MaximumPlayerSessionCount | The maximum number of player connections to the game<br>session.<br>**Type:**<br>`Integer`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                             |
| Port                      | The port number for the game session. To connect to an Amazon GameLift Servers game<br>server, an app needs both the IP address and port number.<br>**Type:**<br>`Integer`<br>**Required**: No                                                                                                                                                                                                                                                                             |
| IpAddress                 | The IP address of the game session. To connect to an Amazon GameLift Servers game<br>server, an app needs both the IP address and port number.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                                                                |
| GameSessionData           | A set of custom game session properties, formatted as a single<br>string value.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                               |
| MatchmakerData            | The information about the matchmaking process that was used to<br>create the game session, in JSON syntax, formatted as a string. In<br>addition to the matchmaking configuration used, it contains data on all<br>players assigned to the match, including player attributes and team<br>assignments.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                        |
| GameProperties            | A set of custom properties for a game session, formatted as<br>key:value pairs. These properties are passed with a request to start<br>a new game session.<br>**Type:**<br>`Dictionary<string, string>`<br>**Required**: No                                                                                                                                                                                                                                                |
| DnsName                   | The DNS identifier assigned to the instance that's running the<br>game session. Values have the following format:<br>• TLS-enabled fleets: `<unique<br>identifier>.<region<br>identifier>.amazongamelift.com`.<br>• Non-TLS-enabled fleets: `ec2-<unique<br>identifier>.compute.amazonaws.com`.<br>When connecting to a game session that's running on a TLS-enabled<br>fleet, you must use the DNS name, not the IP address.<br>**Type:**<br>`String`<br>**Required**: No |

## ServerParameters

Information used to maintain the connection between an Amazon GameLift Servers Anywhere server and the
Amazon GameLift Servers service. This information is used when launching new server processes with [InitSDK()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initsdk "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initsdk"). For servers hosted on
Amazon GameLift Servers managed EC2 instances, use an empty object.

| Properties   | **Description**                                                                                                                                                                                                                                                                                                                     |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WebSocketUrl | The `GameLiftServerSdkEndpoint` returned when you<br>`RegisterCompute` as part of Amazon GameLift Servers Anywhere.<br>**Type:**<br>`String`<br>**Required**: Yes                                                                                                                                                                   |
| ProcessId    | A unique identifier registered to the server process hosting your<br>game.<br>**Type:**<br>`String`<br>**Required**: Yes                                                                                                                                                                                                            |
| HostId       | A unique identifier for the host with the server processes hosting<br>your game. The hostId is the ComputeName used when you registered<br>your compute. For more information see, [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md")<br>**Type:**<br>`String`<br>**Required**: Yes |
| FleetId      | The fleet ID of the fleet that the compute is registered to. For more<br>information see, [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md").**Type:**<br>`String`**Required**: Yes                                                                                                 |
| AuthToken    | The authentication token generated by Amazon GameLift Servers that authenticates your<br>server to Amazon GameLift Servers. For more information see, [GetComputeAuthToken](../apireference/API_GetComputeAuthToken.md "../apireference/API_GetComputeAuthToken.md").**Type:**<br>`String`**Required**: Yes                         |

## StartMatchBackfillRequest

Information used to create a matchmaking backfill request. The game server
communicates this information to Amazon GameLift Servers in a [StartMatchBackfill()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-startmatchbackfill "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-startmatchbackfill") call.

| Properties                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GameSessionArn              | The unique game session identifier. The API operation `GetGameSessionId` returns<br>the identifier in ARN format.<br>**Type:**<br>`String`<br>**Required**: Yes                                                                                                                                                                                                                                                                                        |
| MatchmakingConfigurationArn | The unique identifier, in the form of an ARN, for the matchmaker<br>to use for this request. The matchmaker ARN for the original game<br>session is in the game session object in the matchmaker data<br>property. Learn more about matchmaker data in [Work with matchmaker data](../flexmatchguide/match-server.md#match-server-data.html "../flexmatchguide/match-server.md#match-server-data.html").<br>**Type:**<br>`String`<br>**Required**: Yes |
| Players                     | A set of data that represents all players who are currently in the<br>game session. The matchmaker uses this information to search for new<br>players who are good matches for the current players.<br>**Type:**<br>`List<Player>`<br>**Required**: Yes                                                                                                                                                                                                |
| TicketId                    | The unique identifier for a matchmaking or match backfill request<br>ticket. If you don't provide a value, Amazon GameLift Servers generates one. Use this<br>identifier to track the match backfill ticket status or cancel the<br>request if needed.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                    |

## Player

Represents a player in matchmaking. When a matchmaking request starts, a player has a
player ID, attributes, and possibly latency data. Amazon GameLift Servers adds team information after a
match is made.

| Properties       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LatencyInMS      | A set of values expressed in milliseconds, that indicate the<br>amount of latency that a player experiences when connected to a<br>location.<br>If this property is used, the player is only matched for locations<br>listed. If a matchmaker has a rule that evaluates player latency,<br>players must report latency to be matched.<br>**Type:**<br>`Dictionary<string, int>`<br>**Required**: No               |
| PlayerAttributes | A collection of key:value pairs that contain player information<br>for use in matchmaking. Player attribute keys must match the<br>PlayerAttributes used in a matchmaking rule set.<br>For more information about player attributes, see [AttributeValue](../apireference/API_AttributeValue.md "../apireference/API_AttributeValue.md").<br>**Type:**<br>`Dictionary<string, AttributeValue`<br>**Required**: No |
| PlayerId         | A unique identifier for a player.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                    |
| Team             | The name of the team that the player is assigned to in a match.<br>You define team name in the matchmaking rule set.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                                 |

## DescribePlayerSessionsRequest

This data type is used to specify which player session(s) to retrieve. It can be used
in several ways: (1) provide a PlayerSessionId to request a specific player session; (2)
provide a GameSessionId to request all player sessions in the specified game session; or
(3) provide a PlayerId to request all player sessions for the specified player. For
large collections of player sessions, use the pagination parameters to retrieve results
as sequential pages.

| Properties                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSessionId             | The unique game session identifier. Use this parameter to request<br>all player sessions for the specified game session. Game session ID<br>format is as follows:<br>`arn:aws:gamelift:<region>::gamesession/fleet-<fleet<br>ID>/<ID string>`. The value of <ID string><br>is either a custom ID string (if one was specified when the game<br>session was created) or a generated string.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                 |
| PlayerSessionId           | The unique identifier for a player session.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PlayerId                  | The unique identifier for a player. See [Generate player IDs](player-sessions-player-identifiers.md "player-sessions-player-identifiers.md").<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PlayerSessionStatusFilter | The player session status to filter results on. Possible player<br>session statuses include the following:<br>• RESERVED – The player session request has been<br>received, but the player has not yet connected to the server<br>process and/or been validated.<br>• ACTIVE – The player has been validated by the<br>server process and is currently connected.<br>• COMPLETED – The player connection has been<br>dropped.<br>• TIMEDOUT – A player session request was received,<br>but the player did not connect and/or was not validated<br>within the time-out limit (60 seconds).<br>**Type:**<br>`String`<br>**Required**: No |
| NextToken                 | The token indicating the start of the next page of results. To<br>specify the start of the result set, don't provide a value. If you<br>provide a player session ID, this parameter is ignored.<br>**Type:**<br>`String`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                            |
| Limit                     | The maximum number of results to return. If you provide a player<br>session ID, this parameter is ignored.<br>**Type:**<br>`int`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## StopMatchBackfillRequest

Information used to cancel a matchmaking backfill request. The game server
communicates this information to Amazon GameLift Servers service in a [StopMatchBackfill()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-stopmatchbackfill "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-stopmatchbackfill") call.

| Properties                  | **Description**                                                                                                       |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| GameSessionArn              | The unique game session identifier of the request being<br>canceled.<br>**Type:**<br>`string`<br>**Required**: Yes    |
| MatchmakingConfigurationArn | The unique identifier of the matchmaker this request was sent<br>to.<br>**Type:**<br>`string`<br>**Required**: Yes    |
| TicketId                    | The unique identifier of the backfill request ticket to be<br>canceled.<br>**Type:**<br>`string`<br>**Required**: Yes |

## GetFleetRoleCredentialsRequest

This data type gives the game server limited access to your other AWS resources.
For more information see, [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md "setting-up-role.md").

| Properties      | **Description**                                                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| RoleArn         | The Amazon Resource Name (ARN) of the service role that extends<br>limited access to your AWS resources.<br>**Type:**<br>`string`<br>**Required**: Yes |
| RoleSessionName | The name of the session that describes the use of the role<br>credentials.<br>**Type:**<br>`string`<br>**Required**: No                                |

## AttributeValue

Use these values in [Player](#integration-server-sdk5-csharp-dataypes-player "#integration-server-sdk5-csharp-dataypes-player") attribute key-value pairs.
This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map.
Each `AttributeValue` object can use only one of the available properties.

| Properties | Description                                                                                                                                                                                                    |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| attrType   | Specifies the type of attribute value.<br>**Type:_<br>• An `AttrType` [enum](#integration-server-sdk5-csharp-datatypes-enums "#integration-server-sdk5-csharp-datatypes-enums") value.<br>**Required:_<br>• No |
| S          | Represents a string attribute value.<br>**Type:_<br>• `string`<br>**Required:_<br>• Yes                                                                                                                        |
| N          | Represents a numeric attribute value.<br>**Type:_<br>• `double`<br>**Required:_<br>• Yes                                                                                                                       |
| SL         | Represents an array of string attribute values.<br>**Type:_<br>• `string[]`<br>**Required:_<br>• Yes                                                                                                           |
| SDM        | Represents a dictionary of string keys and double values.<br>**Type:_<br>• `Dictionary<string, double>`<br>**Required:_<br>• Yes                                                                               |

## AwsStringOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result     | The result of the action.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                                                                                         |
| Success    | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                              |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No |

## GenericOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Success    | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                              |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No |

## MetricsManagerOutcome

Represents the result of an [InitMetrics()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initmetrics "integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initmetrics") call. Contains either a
MetricsManager instance on success or error information on failure.

|         |                                                                                                                                                                                                                                     |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result  | The MetricsManager instance for collecting and reporting metrics.<br>**Type:_<br>• `MetricsManager`<br>**Required:_<br>• No                                                                                                         |
| Success | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                              |
| Error   | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No |

## DescribePlayerSessionsOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                                        |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result     | The result of the action.<br>**Type:_<br>• [DescribePlayerSessionsResult](#integration-server-sdk5-csharp-datatypes-describeplayersessionsresult "#integration-server-sdk5-csharp-datatypes-describeplayersessionsresult")<br>**Required:_<br>• No |
| Success    | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                                             |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No                |

## DescribePlayerSessionsResult

| Properties     | Description                                                                                                                                                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NextToken      | The token indicating the start of the next page of results. To<br>specify the start of the result set, don't provide a value. If you<br>provide a player session ID, this parameter is ignored.<br>**Type:_<br>• `string`<br>**Required:_<br>• Yes |
| PlayerSessions | A collection of objects containing properties for each player session that matches the request.<br>**Type:*<br>• `IList<PlayerSession>`<br>**Required:**                                                                                           |
| Success        | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                                             |
| Error          | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No                |

## PlayerSession

| Properties      | Description                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CreationTime    | **Type:_<br>• `long`<br>**Required:_<br>• Yes                                                                                                                             |
| FleetId         | **Type:_<br>• `string`<br>**Required:_<br>• Yes                                                                                                                           |
| GameSessionId   | **Type:_<br>• `string`<br>**Required:_<br>• Yes                                                                                                                           |
| IpAddress       | **Type:_<br>• `string`<br>**Required:_<br>• Yes                                                                                                                           |
| PlayerData      | **Type:_<br>• `string`<br>**Required:_<br>• Yes                                                                                                                           |
| PlayerId        | **Type:_<br>• `string`<br>**Required:_<br>• Yes                                                                                                                           |
| PlayerSessionId | **Type:_<br>• `string`<br>**Required:_<br>• Yes                                                                                                                           |
| Port            | **Type:_<br>• `int`<br>**Required:_<br>• Yes                                                                                                                              |
| Status          | **Type:_<br>• A `PlayerSessionStatus` [enum](#integration-server-sdk5-csharp-datatypes-enums "#integration-server-sdk5-csharp-datatypes-enums").<br>**Required:_<br>• Yes |
| TerminationTime | **Type:_<br>• `long`<br>**Required:_<br>• Yes                                                                                                                             |
| DnsName         | **Type:_<br>• `string`<br>**Required:_<br>• Yes                                                                                                                           |

## StartMatchBackfillOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                            |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result     | The result of the action.<br>**Type:_<br>• [StartMatchBackfillResult](#integration-server-sdk5-csharp-datatypes-startmatchbackfillresult "#integration-server-sdk5-csharp-datatypes-startmatchbackfillresult")<br>**Required:_<br>• No |
| Success    | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                                 |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No    |

## StartMatchBackfillResult

| Properties | Description                                     |
| ---------- | ----------------------------------------------- |
| TicketId   | **Type:_<br>• `string`<br>**Required:_<br>• Yes |

## GetComputeCertificateOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result     | The result of the action.<br>**Type:_<br>• [GetComputeCertificateResult](#integration-server-sdk5-csharp-datatypes-getcomputecertificateresult "#integration-server-sdk5-csharp-datatypes-getcomputecertificateresult")<br>**Required:_<br>• No |
| Success    | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                                          |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No             |

## GetComputeCertificateResult

The path to the TLS certificate on your compute and the compute's host name.

| Properties      | Description                                     |
| --------------- | ----------------------------------------------- |
| CertificatePath | **Type:_<br>• `string`<br>**Required:_<br>• Yes |
| ComputeName     | **Type:_<br>• `string`<br>**Required:_<br>• Yes |

## GetFleetRoleCredentialsOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                                           |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result     | The result of the action.<br>**Type:_<br>• [GetFleetRoleCredentialsResult](#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsresult "#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsresult")<br>**Required:_<br>• No |
| Success    | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                                                |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No                   |

## GetFleetRoleCredentialsResult

| Properties         | Description                                                                                                                                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AccessKeyId        | The access key ID to authenticate and provide access to your<br>AWS resources.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                                    |
| AssumedRoleId      | The ID of the user that the service role belongs to.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                                                              |
| AssumedRoleUserArn | The Amazon Resource Name (ARN) of the user that the<br>service role belongs to.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                                   |
| Expiration         | The amount of time until your session credentials<br>expire.<br>**Type:_<br>• `DateTime`<br>**Required:_<br>• No                                                                                                                    |
| SecretAccessKey    | The secret access key ID for authentication.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                                                                      |
| SessionToken       | A token to identify the current active session interacting<br>with your AWS resources.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                            |
| Success            | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                              |
| Error              | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No |

## ListContainersNetworkInfoOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                                                 |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result     | The result of the action.<br>**Type:_<br>• [ListContainersNetworkInfoResult](#integration-server-sdk5-csharp-datatypes-listcontainersnetworkinforesult "#integration-server-sdk5-csharp-datatypes-listcontainersnetworkinforesult")<br>**Required:_<br>• No |
| Success    | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                                                      |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No                         |

## ListContainersNetworkInfoResult

Network information for all containers running on the same instance as the calling
game server process.

| Properties            | Description                                                                                                                                                                                                                                                                                    |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ContainersNetworkInfo | The list of network information for each container running on the instance.<br>**Type:_<br>• A list of [ContainerNetworkInfo](#integration-server-sdk5-csharp-datatypes-containernetworkinfo "#integration-server-sdk5-csharp-datatypes-containernetworkinfo") objects<br>**Required:_<br>• No |

## ContainerNetworkInfo

Network information for a single container running on the instance.

| Properties         | Description                                                                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ContainerName      | The name of the container, as defined in the container group definition.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                                            |
| ContainerId        | The unique identifier of the container.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                                                                             |
| IpAddress          | The container's local IPv4 address on the Docker bridge network.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                                                    |
| ContainerGroupType | The type of container group that the container belongs to.<br>**Type:_<br>• A `ContainerGroupType` [enum](#integration-server-sdk5-csharp-datatypes-enums "#integration-server-sdk5-csharp-datatypes-enums").<br>**Required:_<br>• No |

## AwsDateTimeOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                         |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result     | The result of the action.<br>**Type:_<br>• `DateTime`<br>**Required:_<br>• No                                                                                                                                                       |
| Success    | Whether the action was successful or not.<br>**Type:*<br>• `bool`<br>**Required**: Yes                                                                                                                                              |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:_<br>• [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror "#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:_<br>• No |

## GameLiftError

| Properties   | Description                                                                                                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ErrorType    | The type of error.<br>**Type:_<br>• A `GameLiftErrorType` [enum](#integration-server-sdk5-csharp-datatypes-enums "#integration-server-sdk5-csharp-datatypes-enums").<br>**Required:_<br>• No |
| ErrorName    | The name of the error.<br>**Type:**<br>`string`<br>**Required:*<br>• No                                                                                                                      |
| ErrorMessage | The error message.<br>**Type:_<br>• `string`<br>**Required:_<br>• No                                                                                                                         |

## Enums

Enums defined for the server SDK for Amazon GameLift Servers (C#) are defined as follows:

**AttrType**

- **NONE**
- **STRING**
- **DOUBLE**
- **STRING\_LIST**
- **STRING\_DOUBLE\_MAP**

**GameLiftErrorType**

String value indicating the error type. Valid values include:

- **SERVICE\_CALL\_FAILED** – A call to an AWS service has failed.
- **LOCAL\_CONNECTION\_FAILED** – The local connection to Amazon GameLift Servers failed.
- **NETWORK\_NOT\_INITIALIZED** – The network has not been initialized.
- **GAMESESSION\_ID\_NOT\_SET** – The game session ID has not been set.
- **BAD\_REQUEST\_EXCEPTION**
- **INTERNAL\_SERVICE\_EXCEPTION**
- **UNSUPPORTED\_COMPUTE\_TYPE\_EXCEPTION** – The API that was called was unsupported on the compute type.
- **ALREADY\_INITIALIZED** – The Amazon GameLift Servers Server or Client has already been initialized with Initialize().
- **FLEET\_MISMATCH** – The target fleet does not match the fleet of a gameSession or playerSession.
- **GAMELIFT\_CLIENT\_NOT\_INITIALIZED** – The Amazon GameLift Servers client has not been initialized.
- **GAMELIFT\_SERVER\_NOT\_INITIALIZED** – The Amazon GameLift Servers server has not been initialized.
- **GAME\_SESSION\_ENDED\_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the game session ended.
- **GAME\_SESSION\_NOT\_READY** – The Amazon GameLift Servers Server Game Session was not activated.
- **GAME\_SESSION\_READY\_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the game session is ready.
- **INITIALIZATION\_MISMATCH** – A client method was called after Server::Initialize(), or vice versa.
- **NOT\_INITIALIZED** – The Amazon GameLift Servers Server or Client has not been initialized with Initialize().
- **NO\_TARGET\_ALIASID\_SET** – A target aliasId has not been set.
- **NO\_TARGET\_FLEET\_SET** – A target fleet has not been set.
- **PROCESS\_ENDING\_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the process is ending.
- **PROCESS\_NOT\_ACTIVE** – The server process is not yet active, not bound to a GameSession, and cannot accept or process PlayerSessions.
- **PROCESS\_NOT\_READY** – The server process is not yet ready to be activated.
- **PROCESS\_READY\_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the process is ready.
- **SDK\_VERSION\_DETECTION\_FAILED** – SDK version detection failed.
- **STX\_CALL\_FAILED** – A call to the XStx server backend component has failed.
- **STX\_INITIALIZATION\_FAILED** – The XStx server backend component has failed to initialize.
- **UNEXPECTED\_PLAYER\_SESSION** – An unregistered player session was encountered by the server.
- **WEBSOCKET\_CONNECT\_FAILURE**
- **WEBSOCKET\_CONNECT\_FAILURE\_FORBIDDEN**
- **WEBSOCKET\_CONNECT\_FAILURE\_INVALID\_URL**
- **WEBSOCKET\_CONNECT\_FAILURE\_TIMEOUT**
- **WEBSOCKET\_RETRIABLE\_SEND\_MESSAGE\_FAILURE** – Retriable failure to send a message to the GameLift Service WebSocket.
- **WEBSOCKET\_SEND\_MESSAGE\_FAILURE** – Failure to send a message to the GameLift Service WebSocket.
- **MATCH\_BACKFILL\_REQUEST\_VALIDATION** – Validation of the request failed.
- **PLAYER\_SESSION\_REQUEST\_VALIDATION** – Validation of the request failed.

**PlayerSessionCreationPolicy**

String value indicating whether the game session accepts new players.
Valid values include:

- **ACCEPT\_ALL** – Accept all new player sessions.
- **DENY\_ALL** – Deny all new player sessions.
- **NOT\_SET** – The game session is not set to accept or deny new player sessions.

**PlayerSessionStatus**

- **ACTIVE**
- **COMPLETED**
- **NOT\_SET**
- **RESERVED**
- **TIMEDOUT**

**ContainerGroupType**

The type of container group that a container belongs to. Valid values
include:

- `GAME_SERVER` – A game server replica container
  group. An instance can have multiple game server container groups.
- `PER_INSTANCE` – A per-instance daemon container
  group. An instance has exactly one per-instance container group.
