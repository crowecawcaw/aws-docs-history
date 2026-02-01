# C++ server SDK 5.x for Amazon GameLift Servers -- Data

types

Use the Amazon GameLift Servers C++ server SDK 5.x reference to integrate your multiplayer game for
hosting with Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server with the server
SDK](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md").

###### Note

This topic describes the Amazon GameLift Servers C++ API that you can use when you build with the C++ Standard Library (`std`).
Specifically, this documentation applies to code that you compile with the `-DDGAMELIFT_USE_STD=1` option.

[C++ server SDK 5.x for Amazon GameLift Servers --
Actions](integration-server-sdk5-cpp-actions.md "integration-server-sdk5-cpp-actions.md")

###### Data types

- [LogParameters](#integration-server-sdk5-cpp-dataypes-log "#integration-server-sdk5-cpp-dataypes-log")
- [MetricsParameters](#integration-server-sdk5-cpp-datatypes-metricsparameters "#integration-server-sdk5-cpp-datatypes-metricsparameters")
- [ProcessParameters](#integration-server-sdk5-cpp-dataypes-process "#integration-server-sdk5-cpp-dataypes-process")
- [UpdateGameSession](#integration-server-sdk5-cpp-dataypes-updategamesession "#integration-server-sdk5-cpp-dataypes-updategamesession")
- [GameSession](#integration-server-sdk5-cpp-dataypes-gamesession "#integration-server-sdk5-cpp-dataypes-gamesession")
- [ServerParameters](#integration-server-sdk5-cpp-dataypes-serverparameters "#integration-server-sdk5-cpp-dataypes-serverparameters")
- [StartMatchBackfillRequest](#integration-server-sdk5-cpp-dataypes-startmatchbackfillrequest "#integration-server-sdk5-cpp-dataypes-startmatchbackfillrequest")
- [Player](#integration-server-sdk5-cpp-dataypes-player "#integration-server-sdk5-cpp-dataypes-player")
- [DescribePlayerSessionsRequest](#integration-server-sdk5-cpp-dataypes-playersessions "#integration-server-sdk5-cpp-dataypes-playersessions")
- [StopMatchBackfillRequest](#integration-server-sdk5-cpp-dataypes-stopmatchbackfillrequest "#integration-server-sdk5-cpp-dataypes-stopmatchbackfillrequest")
- [AttributeValue](#integration-server-sdk5-cpp-dataypes-attributevalue "#integration-server-sdk5-cpp-dataypes-attributevalue")
- [GetFleetRoleCredentialsRequest](#integration-server-sdk5-cpp-dataypes-getfleetrolecredentialsrequest "#integration-server-sdk5-cpp-dataypes-getfleetrolecredentialsrequest")
- [AwsLongOutcome](#integration-server-sdk5-cpp-datatypes-awslongoutcome "#integration-server-sdk5-cpp-datatypes-awslongoutcome")
- [AwsStringOutcome](#integration-server-sdk5-cpp-datatypes-awsstringoutcome "#integration-server-sdk5-cpp-datatypes-awsstringoutcome")
- [DescribePlayerSessionsOutcome](#integration-server-sdk5-cpp-datatypes-describeplayersessionsoutcome "#integration-server-sdk5-cpp-datatypes-describeplayersessionsoutcome")
- [DescribePlayerSessionsResult](#integration-server-sdk5-cpp-datatypes-describeplayersessionsresult "#integration-server-sdk5-cpp-datatypes-describeplayersessionsresult")
- [GenericOutcome](#integration-server-sdk5-cpp-datatypes-genericoutcome "#integration-server-sdk5-cpp-datatypes-genericoutcome")
- [GenericOutcomeCallable](#integration-server-sdk5-cpp-datatypes-genericoutcomecallable "#integration-server-sdk5-cpp-datatypes-genericoutcomecallable")
- [PlayerSession](#integration-server-sdk5-cpp-datatypes-playersession "#integration-server-sdk5-cpp-datatypes-playersession")
- [StartMatchBackfillOutcome](#integration-server-sdk5-cpp-datatypes-startmatchbackfilloutcome "#integration-server-sdk5-cpp-datatypes-startmatchbackfilloutcome")
- [StartMatchBackfillResult](#integration-server-sdk5-cpp-datatypes-startmatchbackfillresult "#integration-server-sdk5-cpp-datatypes-startmatchbackfillresult")
- [GetComputeCertificateOutcome](#integration-server-sdk5-cpp-datatypes-getcomputecertificateoutcome "#integration-server-sdk5-cpp-datatypes-getcomputecertificateoutcome")
- [GetComputeCertificateResult](#integration-server-sdk5-cpp-datatypes-getcomputecertificateresult "#integration-server-sdk5-cpp-datatypes-getcomputecertificateresult")
- [GetFleetRoleCredentialsOutcome](#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsoutcome "#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsoutcome")
- [GetFleetRoleCredentialsResult](#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsresult "#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsresult")
- [InitSDKOutcome](#integration-server-sdk5-cpp-datatypes-initsdkoutcome "#integration-server-sdk5-cpp-datatypes-initsdkoutcome")
- [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")
- [Enums](#integration-server-sdk5-cpp-dataypes-enums "#integration-server-sdk5-cpp-dataypes-enums")

## LogParameters

An object identifying files generated during a game session that you want Amazon GameLift Servers to
upload and store after the game session ends. The game server provides
`LogParameters` to Amazon GameLift Servers as part of a `ProcessParameters`
object in a [ProcessReady()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-processready "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-processready") call.

|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Properties** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| LogPaths       | The list of directory paths to game server log files you want<br>Amazon GameLift Servers to store for future access. The server process generates these<br>files during each game session. You define file paths and names in<br>your game server and store them in the root game build directory.<br>The log paths must be absolute. For example, if your game build<br>stores game session logs in a path like<br>`MyGame\sessionLogs\`, then the path would be<br>`c:\game\MyGame\sessionLogs` on a Windows<br>instance.<br>**Type:**<br>`std:vector<std::string>`<br>\*_Required:_<br>• No |

## MetricsParameters

Use this data type to configure metrics collection and crash reporting for the game server.
The game server communicates `MetricsParameters` to Amazon GameLift Servers in an [InitMetrics()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initmetrics "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initmetrics") call.

|                   |                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Properties**    | **Description**                                                                                                                |
| StatsdHost        | The hostname or IP address of the StatsD server for metrics collection.<br>**Type:**<br>`std::string`<br>\*_Required:_<br>• No |
| StatsdPort        | The port number of the StatsD server for metrics collection.<br>**Type:**<br>`int`<br>\*_Required:_<br>• No                    |
| CrashReporterHost | The hostname or IP address of the crash reporter server.<br>**Type:**<br>`std::string`<br>\*_Required:_<br>• No                |
| CrashReporterPort | The port number of the crash reporter server.<br>**Type:**<br>`int`<br>\*_Required:_<br>• No                                   |
| FlushIntervalMs   | The interval in milliseconds for flushing metrics data to the server.<br>**Type:**<br>`int`<br>\*_Required:_<br>• No           |
| MaxPacketSize     | The maximum size in bytes for metrics packets sent to the server.<br>**Type:**<br>`int`<br>\*_Required:_<br>• No               |

## ProcessParameters

This data type contains the set of parameters sent to Amazon GameLift Servers in a [ProcessReady()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-processready "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-processready").

|                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Properties**      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| LogParameters       | An object with directory paths to files that are generated during a game<br>session. Amazon GameLift Servers copies and stores the files for future<br>access.**Type:**<br>`Aws::GameLift::Server::LogParameters`**Required:**<br>No                                                                                                                                                                                                                                                                                                                                                                                 |
| OnHealthCheck       | The callback function that Amazon GameLift Servers invokes to request a health status<br>report from the server process. Amazon GameLift Servers calls this function every 60<br>seconds and waits 60 seconds for a response. The server process returns<br>`TRUE` if healthy, `FALSE` if not healthy. If<br>no response is returned, Amazon GameLift Servers records the server process as not<br>healthy.**Type:**<br>`std::function<bool()><br>onHealthCheck`\*_Required:_<br>• No                                                                                                                                |
| OnProcessTerminate  | The callback function that Amazon GameLift Servers invokes to force the server process to<br>shut down. After calling this function, Amazon GameLift Servers waits 5 minutes for the<br>server process to shut down and respond with a [ProcessEnding()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-processending "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-processending") call<br>before it shuts down the server process.**Type:**<br>`std::function<void()><br>onProcessTerminate`\*_Required:_<br>• Yes                                                       |
| OnStartGameSession  | The callback function that Amazon GameLift Servers invokes to activate a new game session.<br>Amazon GameLift Servers calls this function in response to a client request [CreateGameSession](../apireference/API_CreateGameSession.md "../apireference/API_CreateGameSession.md").<br>The callback function passes a [GameSession](#integration-server-sdk5-cpp-dataypes-gamesession "#integration-server-sdk5-cpp-dataypes-gamesession") object.**Type:**<br>`const<br>std::function<void(Aws::GameLift::Model::GameSession)><br>onStartGameSession`\*_Required:_<br>• Yes                                         |
| OnUpdateGameSession | The callback function that Amazon GameLift Servers invokes to pass an updated game session<br>object to the server process. Amazon GameLift Servers calls this function when a match<br>backfill request has been processed to provide updated matchmaker data.<br>It passes a [GameSession](#integration-server-sdk5-cpp-dataypes-gamesession "#integration-server-sdk5-cpp-dataypes-gamesession") object, a status update<br>(`updateReason`), and the match backfill ticket<br>ID.**Type:**<br>`std::function<void(Aws::GameLift::Server::Model::UpdateGameSession)><br>onUpdateGameSession`\*_Required:_<br>• No |
| Port                | The port number the server process listens on for new player<br>connections. The value must fall into the port range configured for any<br>fleet deploying this game server build. This port number is included in<br>game session and player session objects, which game sessions use when<br>connecting to a server process.**Type:**<br>`Integer`\*_Required:_<br>• Yes                                                                                                                                                                                                                                           |

## UpdateGameSession

This data type updates to a game session object, which includes the reason that the
game session was updated and the related backfill ticket ID if backfill is used to fill
player sessions in the game session.

| Properties       | **Description**                                                                                                                                                                                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GameSession      | A [GameSession](#integration-server-sdk5-cpp-dataypes-gamesession "#integration-server-sdk5-cpp-dataypes-gamesession") object. The<br>`GameSession` object contains properties describing a<br>game session. **Type:**<br>`Aws::GameLift::Server::GameSession`\*_Required:_<br>• Yes |
| UpdateReason     | The reason that the game session is being updated.**Type:**<br>`Aws::GameLift::Server::UpdateReason`\*_Required:_<br>• Yes                                                                                                                                                           |
| BackfillTicketId | The ID of the backfill ticket attempting to update the game<br>session.**Type:**<br>`std::string`\*_Required:_<br>• No                                                                                                                                                               |

## GameSession

This data type provides details of a game session.

| Properties                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSessionId             | A unique identifier for the game session. A game session ARN has<br>the following format:<br>`arn:aws:gamelift:<region>::gamesession/<fleet<br>ID>/<custom ID string or idempotency token>`.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                  |
| Name                      | A descriptive label of the game session.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                      |
| FleetId                   | A unique identifier for the fleet that the game session is running<br>on.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                     |
| MaximumPlayerSessionCount | The maximum number of player connections to the game<br>session.<br>**Type:**<br>`int`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                      |
| Port                      | The port number for the game session. To connect to an Amazon GameLift Servers game<br>server, an app needs both the IP address and port number.<br>**Type:**<br>`in`<br>**Required**: No                                                                                                                                                                                                                                                                                       |
| IpAddress                 | The IP address of the game session. To connect to an Amazon GameLift Servers game<br>server, an app needs both the IP address and port number.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                |
| GameSessionData           | A set of custom game session properties, formatted as a single<br>string value.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                               |
| MatchmakerData            | Information about the matchmaking process that was used to create<br>the game session, in JSON syntax, formatted as a string. In addition<br>to the matchmaking configuration used, it contains data on all<br>players assigned to the match, including player attributes and team<br>assignments.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                            |
| GameProperties            | A set of custom properties for a game session, formatted as<br>key:value pairs. These properties are passed with a request to start<br>a new game session.<br>**Type:**<br>`std :: vector < GameProperty >`<br>**Required**: No                                                                                                                                                                                                                                                 |
| DnsName                   | The DNS identifier assigned to the instance that's running the<br>game session. Values have the following format:<br>• TLS-enabled fleets: `<unique<br>identifier>.<region<br>identifier>.amazongamelift.com`.<br>• Non-TLS-enabled fleets: `ec2-<unique<br>identifier>.compute.amazonaws.com`.<br>When connecting to a game session that's running on a TLS-enabled<br>fleet, you must use the DNS name, not the IP address.<br>**Type:**<br>`std::string`<br>**Required**: No |

## ServerParameters

Information that a game server process uses to establish a connection with the Amazon GameLift Servers
service. Include these parameters when calling [InitSDK()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk-anywhere "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk-anywhere") only if the game
server build will be deployed to an Anywhere fleet or a container fleet without the
Amazon GameLift Servers Agent. For all other deployment scenarios, call [InitSDK()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk") without parameters.

| Properties   | **Description**                                                                                                                                                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| webSocketUrl | The `GameLiftServerSdkEndpoint` Amazon GameLift Servers returns when you<br>[`RegisterCompute`](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md") for a Amazon GameLift Servers Anywhere<br>compute resource.<br>**Type:**<br>`std::string`<br>**Required**: Yes                  |
| processId    | A unique identifier registered to the server process hosting your<br>game.<br>**Type:**<br>`std::string`<br>**Required**: Yes                                                                                                                                                                                    |
| hostId       | The `HostID` is the `ComputeName` used when you<br>registered your compute. For more information see, [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md").**Type:**<br>`std::string`**Required**: Yes                                                             |
| fleetId      | The unique identifier of the fleet that the compute is registered to.<br>For more information see, [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md").**Type:**<br>`std::string`**Required**: Yes                                                                |
| authToken    | The authentication token generated by Amazon GameLift Servers that authenticates your<br>server to Amazon GameLift Servers. For more information see, [GetComputeAuthToken](../apireference/API_GetComputeAuthToken.md "../apireference/API_GetComputeAuthToken.md").**Type:**<br>`std::string`**Required**: Yes |

## StartMatchBackfillRequest

Information used to create a matchmaking backfill request. The game server
communicates this information to Amazon GameLift Servers in a [StartMatchBackfill()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-startmatchbackfill "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-startmatchbackfill") call.

| Properties                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSessionArn              | A unique game session identifier. The API operation `GetGameSessionId` returns<br>the identifier in ARN format.<br>**Type:**<br>`std::string`<br>**Required**: Yes                                                                                                                                                                                                                                                                                        |
| MatchmakingConfigurationArn | A unique identifier, in the form of an ARN, for the matchmaker to<br>use for this request. The matchmaker ARN for the original game<br>session is in the game session object in the matchmaker data<br>property. Learn more about matchmaker data in [Work with matchmaker data](../flexmatchguide/match-server.md#match-server-data.html "../flexmatchguide/match-server.md#match-server-data.html").<br>**Type:**<br>`std::string`<br>**Required**: Yes |
| Players                     | A set of data representing all players who are in the game<br>session. The matchmaker uses this information to search for new<br>players who are good matches for the current players.<br>**Type:**<br>`std::vector<Player>`<br>**Required**: Yes                                                                                                                                                                                                         |
| TicketId                    | A unique identifier for a matchmaking or match backfill request<br>ticket. If you don't provide a value, Amazon GameLift Servers generates one. Use this<br>identifier to track the match backfill ticket status or cancel the<br>request if needed.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                    |

## Player

This data type represents a player in matchmaking. When starting a matchmaking
request, a player has a player ID, attributes, and possibly latency data. Amazon GameLift Servers adds
team information after a match is made.

| Properties       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| LatencyInMS      | A set of values expressed in milliseconds that indicate the amount<br>of latency that a player experiences when connected to a location.<br>If this property is used, the player is only matched for locations<br>listed. If a matchmaker has a rule that evaluates player latency,<br>players must report latency to be matched.<br>**Type:**<br>`Dictionary<string,int>`<br>**Required**: No                     |
| PlayerAttributes | A collection of key:value pairs containing player information for<br>use in matchmaking. Player attribute keys must match the<br>PlayerAttributes used in a matchmaking rule set.<br>For more information about player attributes, see [AttributeValue](../apireference/API_AttributeValue.md "../apireference/API_AttributeValue.md").<br>**Type:**<br>`std::map<std::string,AttributeValue>`<br>**Required**: No |
| PlayerId         | A unique identifier for a player.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                |
| Team             | The name of the team that the player is assigned to in a match.<br>You define team name in the matchmaking rule set.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                             |

## DescribePlayerSessionsRequest

An object that specifies which player sessions to retrieve. The server process
provides this information with a [DescribePlayerSessions()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-describeplayersessions "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-describeplayersessions") call to
Amazon GameLift Servers.

| Properties                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSessionId             | A unique game session identifier. Use this parameter to request<br>all player sessions for the specified game session.<br>Game session ID format is<br>`arn:aws:gamelift:<region>::gamesession/fleet-<fleet<br>ID>/<ID string>`. The `GameSessionID`<br>is a custom ID string or a<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                            |
| PlayerSessionId           | The unique identifier for a player session. Use this parameter to<br>request a single specific player session.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                                                |
| PlayerId                  | The unique identifier for a player. Use this parameter to request<br>all player sessions for a specific player. See [Generate player IDs](player-sessions-player-identifiers.md "player-sessions-player-identifiers.md").<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                                     |
| PlayerSessionStatusFilter | The player session status to filter results on. Possible player<br>session statuses include:<br>• RESERVED – The player session request was received,<br>but the player hasn't connected to the server process or<br>been validated.<br>• ACTIVE – The player was validated by the server<br>process and is connected.<br>• COMPLETED – The player connection dropped.<br>• TIMEDOUT – A player session request was received,<br>but the player didn't connect or wasn't validated within the<br>time-out limit (60 seconds).<br>**Type:**<br>`std::string`<br>**Required**: No |
| NextToken                 | The token indicating the start of the next page of results. To<br>specify the start of the result set, don't provide a value. If you<br>provide a player session ID, this parameter is ignored.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                                                               |
| Limit                     | The maximum number of results to return. If you provide a player<br>session ID, this parameter is ignored.<br>**Type:**<br>`int`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                                                            |

## StopMatchBackfillRequest

Information used to cancel a matchmaking backfill request. The game server
communicates this information to Amazon GameLift Servers service in a [StopMatchBackfill()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-stopmatchbackfill "integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-stopmatchbackfill") call.

| Properties                  | **Description**                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| GameSessionArn              | A unique game session identifier of the request being<br>canceled.<br>**Type:**<br>`char[]`<br>**Required**: No    |
| MatchmakingConfigurationArn | A unique identifier of the matchmaker this request was sent<br>to.<br>**Type:**<br>`char[]`<br>**Required**: No    |
| TicketId                    | A unique identifier of the backfill request ticket to be<br>canceled.<br>**Type:**<br>`char[]`<br>**Required**: No |

## AttributeValue

Use these values in [Player](#integration-server-sdk5-cpp-dataypes-player "#integration-server-sdk5-cpp-dataypes-player") attribute key-value pairs.
This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map.
Each `AttributeValue` object must use exactly one of the available properties: `S`, `N`, `SL`, or `SDM`.

| Properties | Description                                                                                                                                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AttrType   | Specifies the type of attribute value.<br>Possible attribute value types include:<br>• **NONE**<br>• **STRING**<br>• **DOUBLE**<br>• **STRING_LIST**<br>• **STRING_DOUBLE_MAP**<br>\*_Required:_<br>• No |
| S          | Represents a string attribute value.<br>**Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                            |
| N          | Represents a numeric attribute value.<br>**Type:\*<br>• `double`<br>**Required:\*<br>• No                                                                                                                |
| SL         | Represents an array of string attribute values.<br>**Type:\*<br>• `std::vector<std::string>`<br>**Required:\*<br>• No                                                                                    |
| SDM        | Represents a dictionary of string keys and double values.<br>**Type:\*<br>• `std::map<std::string, double>`<br>**Required:\*<br>• No                                                                     |

## GetFleetRoleCredentialsRequest

This data type gives the game server limited access to your other AWS resources.
For more information see, [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md "setting-up-role.md").

| Properties      | **Description**                                                                                                                                                                                                                                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RoleArn         | The Amazon Resource Name (ARN) of the service role that extends<br>limited access to your AWS resources.**Type:**<br>`std::string`**Required**: No                                                                                                                                                                                                |
| RoleSessionName | The role session name that you can use to uniquely identify an AWS Security Token Service [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") session.<br>This name is exposed in audit logs such as those in CloudTrail.<br>**Type:\*<br>• `std::string`<br>**Required\*\*: No |

## AwsLongOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result              | The result of the action.<br>**Type:\*<br>• `long`<br>**Required:\*<br>• No                                                                                                                                                     |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `long&&`<br>**Required\*\*: No                                                                        |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                       |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No |

## AwsStringOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result              | The result of the action.<br>**Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                              |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `long&&`<br>**Required\*\*: No                                                                        |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                       |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No |

## DescribePlayerSessionsOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result              | The result of the action.<br>**Type:\*<br>• [DescribePlayerSessionsResult](#integration-server-sdk5-cpp-datatypes-describeplayersessionsresult "#integration-server-sdk5-cpp-datatypes-describeplayersessionsresult")<br>**Required:\*<br>• No |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `Aws::GameLift::Server::Model::DescribePlayerSessionsResult&&`<br>**Required\*\*: No                                 |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                      |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No                |

## DescribePlayerSessionsResult

A collection of objects containing properties for each player session that matches the request.

| Properties          | Description                                                                                                                                                                                                                                                                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NextToken           | A token that indicates the start of the next sequential page of results.<br>Use the token that is returned with a previous call to this operation.<br>To start at the beginning of the result set, do not specify a value.<br>If a player session ID is specified, this parameter is ignored.<br>**Type:\*<br>• `std::string`<br>**Required:\*<br>• Yes |
| PlayerSessions      | **Type:\*<br>• `IList<PlayerSession>`<br>**Required:\*\*                                                                                                                                                                                                                                                                                                |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `std::string&&`<br>**Required\*\*: No                                                                                                                                                                                         |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                                                                                                                               |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No                                                                                                                         |

## GenericOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Success    | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                       |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No |

## GenericOutcomeCallable

This data type is an asynchronous generic outcome.
It has the following properties:

| Properties | Description                                                                                                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Success    | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                       |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No |

## PlayerSession

This data type represents a player session that Amazon GameLift Servers passes to the game server.
For more information, see [PlayerSession](../apireference/API_PlayerSession.md "../apireference/API_PlayerSession.md").

| Properties      | Description                                                                                                                                                                                                                                                                                                                                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CreationTime    | **Type:\*<br>• `long`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                              |
| FleetId         | **Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                       |
| GameSessionId   | **Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                       |
| IpAddress       | **Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                       |
| PlayerData      | **Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                       |
| PlayerId        | **Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                       |
| PlayerSessionId | **Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                       |
| Port            | **Type:\*<br>• `int`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                               |
| Status          | Player session status to filter results on.<br>When a PlayerSessionId or PlayerId is provided, then the PlayerSessionStatusFilter has no effect on the response.<br>**Type:\*<br>• A `PlayerSessionStatus` enum.<br>Possible values include the following:<br>• **ACTIVE**<br>• **COMPLETED**<br>• **NOT_SET**<br>• **RESERVED**<br>• **TIMEDOUT**<br>**Required:\*<br>• No |
| TerminationTime | **Type:\*<br>• `long`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                              |
| DnsName         | **Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                       |

## StartMatchBackfillOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result              | The result of the action.<br>**Type:\*<br>• [StartMatchBackfillResult](#integration-server-sdk5-cpp-datatypes-startmatchbackfillresult "#integration-server-sdk5-cpp-datatypes-startmatchbackfillresult")<br>**Required:\*<br>• No |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `StartMatchBackfillResult&&`<br>**Required\*\*: No                                                       |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                          |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No    |

## StartMatchBackfillResult

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TicketId   | A unique identifier for a matchmaking ticket.<br>If no ticket ID is specified here, Amazon GameLift Servers will generate one in the form of a UUID.<br>Use this identifier to track the match backfill ticket status and retrieve match results.<br>**Type:\*<br>• `std::string`<br>**Required:\*<br>• No |

## GetComputeCertificateOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result              | The result of the action.<br>**Type:\*<br>• [GetComputeCertificateResult](#integration-server-sdk5-cpp-datatypes-getcomputecertificateresult "#integration-server-sdk5-cpp-datatypes-getcomputecertificateresult")<br>**Required:\*<br>• No |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `Aws::GameLift::Server::Model::GetComputeCertificateResult&&`<br>**Required\*\*: No                               |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                   |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No             |

## GetComputeCertificateResult

The path to the TLS certificate on your compute and the compute's host name.

| Properties      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CertificatePath | The path to the TLS certificate on your compute resource.<br>When using an Amazon GameLift Servers managed fleet, this path contains:<br>• `certificate.pem`: The end-user certificate. The full certificate chain is the combination of `certificateChain.pem` appended to this certificate.<br>• `certificateChain.pem`: The certificate chain that contains the root certificate and intermediate certificates.<br>• `rootCertificate.pem`: The root certificate.<br>• `privateKey.pem`: The private key for the end-user certificate.<br>**Type:\*<br>• `std::string`<br>**Required:\*<br>• No |
| ComputeName     | The name of your compute resource.<br>**Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## GetFleetRoleCredentialsOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result              | The result of the action.<br>**Type:\*<br>• [GetFleetRoleCredentialsResult](#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsresult "#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsresult")<br>**Required:\*<br>• No |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `Aws::GameLift::Server::Model::GetFleetRoleCredentialsResult`<br>**Required\*\*: No                                     |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                         |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No                   |

## GetFleetRoleCredentialsResult

| Properties         | Description                                                                                                                                                                                                                                                                                                                 |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AccessKeyId        | The access key ID to authenticate and provide access to your<br>AWS resources.<br>**Type:\*<br>• `string`<br>**Required:\*<br>• No                                                                                                                                                                                          |
| AssumedRoleId      | The ID of the user that the service role belongs to.<br>**Type:\*<br>• `string`<br>**Required:\*<br>• No                                                                                                                                                                                                                    |
| AssumedRoleUserArn | The Amazon Resource Name (ARN) of the user that the<br>service role belongs to.<br>**Type:\*<br>• `string`<br>**Required:\*<br>• No                                                                                                                                                                                         |
| Expiration         | The amount of time until your session credentials<br>expire.<br>**Type:\*<br>• `DateTime`<br>**Required:\*<br>• No                                                                                                                                                                                                          |
| SecretAccessKey    | The secret access key ID for authentication.<br>**Type:\*<br>• `string`<br>**Required:\*<br>• No                                                                                                                                                                                                                            |
| SessionToken       | A token to identify the current active session interacting<br>with your AWS resources.<br>**Type:\*<br>• `string`<br>**Required:\*<br>• No                                                                                                                                                                                  |
| Success            | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                                                                                                   |
| Error              | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-gamelifterror "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:\*<br>• No |

## InitSDKOutcome

###### Note

`InitSDKOutcome` is returned only when you build the SDK with the `std` flag.
If you build with the `nostd` flag, then [GenericOutcome](#integration-server-sdk5-cpp-datatypes-genericoutcome "#integration-server-sdk5-cpp-datatypes-genericoutcome") is returned instead.

| Properties | Description                                                                                                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Success    | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                       |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror "#integration-server-sdk5-cpp-datatypes-gamelifterror")<br>**Required:\*<br>• No |

## GameLiftError

| Properties   | Description                                                                                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ErrorType    | The type of error.<br>**Type:\*<br>• A `GameLiftErrorType` [enum](#integration-server-sdk5-cpp-dataypes-enums "#integration-server-sdk5-cpp-dataypes-enums").<br>**Required:\*<br>• No |
| ErrorName    | The name of the error.<br>**Type:**<br>`std::string`<br>\*_Required:_<br>• No                                                                                                          |
| ErrorMessage | The error message.<br>**Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                            |

## Enums

Enums defined for the server SDK for Amazon GameLift Servers (C++) are defined as follows:

**GameLiftErrorType**

String value indicating the error type. Valid values include:

- **BAD_REQUEST_EXCEPTION**
- **GAMESESSION_ID_NOT_SET** – The game session ID has not been set.
- **INTERNAL_SERVICE_EXCEPTION**
- **LOCAL_CONNECTION_FAILED** – The local connection to Amazon GameLift Servers failed.
- **NETWORK_NOT_INITIALIZED** – The network has not been initialized.
- **SERVICE_CALL_FAILED** – A call to an AWS service has failed.
- **WEBSOCKET_CONNECT_FAILURE**
- **WEBSOCKET_CONNECT_FAILURE_FORBIDDEN**
- **WEBSOCKET_CONNECT_FAILURE_INVALID_URL**
- **WEBSOCKET_CONNECT_FAILURE_TIMEOUT**
- **ALREADY_INITIALIZED** – The Amazon GameLift Servers Server or Client has already been initialized with Initialize().
- **FLEET_MISMATCH** – The target fleet does not match the fleet of a gameSession or playerSession.
- **GAMELIFT_CLIENT_NOT_INITIALIZED** – The Amazon GameLift Servers client has not been initialized.
- **GAMELIFT_SERVER_NOT_INITIALIZED** – The Amazon GameLift Servers server has not been initialized.
- **GAME_SESSION_ENDED_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the game session ended.
- **GAME_SESSION_NOT_READY** – The Amazon GameLift Servers Server Game Session was not activated.
- **GAME_SESSION_READY_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the game session is ready.
- **INITIALIZATION_MISMATCH** – A client method was called after Server::Initialize(), or vice versa.
- **NOT_INITIALIZED** – The Amazon GameLift Servers Server or Client has not been initialized with Initialize().
- **NO_TARGET_ALIASID_SET** – A target aliasId has not been set.
- **NO_TARGET_FLEET_SET** – A target fleet has not been set.
- **PROCESS_ENDING_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the process is ending.
- **PROCESS_NOT_ACTIVE** – The server process is not yet active, not bound to a GameSession, and cannot accept or process PlayerSessions.
- **PROCESS_NOT_READY** – The server process is not yet ready to be activated.
- **PROCESS_READY_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the process is ready.
- **SDK_VERSION_DETECTION_FAILED** – SDK version detection failed.
- **STX_CALL_FAILED** – A call to the XStx server backend component has failed.
- **STX_INITIALIZATION_FAILED** – The XStx server backend component has failed to initialize.
- **UNEXPECTED_PLAYER_SESSION** – An unregistered player session was encountered by the server.
- **WEBSOCKET_CONNECT_FAILURE**
- **WEBSOCKET_CONNECT_FAILURE_FORBIDDEN**
- **WEBSOCKET_CONNECT_FAILURE_INVALID_URL**
- **WEBSOCKET_CONNECT_FAILURE_TIMEOUT**
- **WEBSOCKET_RETRIABLE_SEND_MESSAGE_FAILURE** – Retriable failure to send a message to the GameLift Service WebSocket.
- **WEBSOCKET_SEND_MESSAGE_FAILURE** – Failure to send a message to the GameLift Service WebSocket.
- **MATCH_BACKFILL_REQUEST_VALIDATION** – Validation of the request failed.
- **PLAYER_SESSION_REQUEST_VALIDATION** – Validation of the request failed.

**PlayerSessionCreationPolicy**

String value indicating whether the game session accepts new players.
Valid values include:

- **ACCEPT_ALL** – Accept all new player sessions.
- **DENY_ALL** – Deny all new player sessions.
- **NOT_SET** – The game session is not set to accept or deny new player sessions.
