

# C\+\+ server SDK 5.x for Amazon GameLift Servers -- Data types
<a name="integration-server-sdk5-cpp-datatypes"></a>

Use the Amazon GameLift Servers C\+\+ server SDK 5.x reference to integrate your multiplayer game for hosting with Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server with the server SDK](gamelift-sdk-server-api.md).

**Note**  
This topic describes the Amazon GameLift Servers C\+\+ API that you can use when you build with the C\+\+ Standard Library (`std`). Specifically, this documentation applies to code that you compile with the `-DDGAMELIFT_USE_STD=1` option. 

[C\+\+ server SDK 5.x for Amazon GameLift Servers -- Actions](integration-server-sdk5-cpp-actions.md)

**Topics**
+ [LogParameters](#integration-server-sdk5-cpp-dataypes-log)
+ [MetricsParameters](#integration-server-sdk5-cpp-datatypes-metricsparameters)
+ [CustomLoggerConfiguration](#integration-server-sdk5-cpp-datatypes-customloggerconfiguration)
+ [ProcessParameters](#integration-server-sdk5-cpp-dataypes-process)
+ [UpdateGameSession](#integration-server-sdk5-cpp-dataypes-updategamesession)
+ [GameSession](#integration-server-sdk5-cpp-dataypes-gamesession)
+ [ServerParameters](#integration-server-sdk5-cpp-dataypes-serverparameters)
+ [StartMatchBackfillRequest](#integration-server-sdk5-cpp-dataypes-startmatchbackfillrequest)
+ [Player](#integration-server-sdk5-cpp-dataypes-player)
+ [DescribePlayerSessionsRequest](#integration-server-sdk5-cpp-dataypes-playersessions)
+ [StopMatchBackfillRequest](#integration-server-sdk5-cpp-dataypes-stopmatchbackfillrequest)
+ [AttributeValue](#integration-server-sdk5-cpp-dataypes-attributevalue)
+ [GetFleetRoleCredentialsRequest](#integration-server-sdk5-cpp-dataypes-getfleetrolecredentialsrequest)
+ [AwsLongOutcome](#integration-server-sdk5-cpp-datatypes-awslongoutcome)
+ [AwsStringOutcome](#integration-server-sdk5-cpp-datatypes-awsstringoutcome)
+ [DescribePlayerSessionsOutcome](#integration-server-sdk5-cpp-datatypes-describeplayersessionsoutcome)
+ [DescribePlayerSessionsResult](#integration-server-sdk5-cpp-datatypes-describeplayersessionsresult)
+ [GenericOutcome](#integration-server-sdk5-cpp-datatypes-genericoutcome)
+ [GenericOutcomeCallable](#integration-server-sdk5-cpp-datatypes-genericoutcomecallable)
+ [PlayerSession](#integration-server-sdk5-cpp-datatypes-playersession)
+ [StartMatchBackfillOutcome](#integration-server-sdk5-cpp-datatypes-startmatchbackfilloutcome)
+ [StartMatchBackfillResult](#integration-server-sdk5-cpp-datatypes-startmatchbackfillresult)
+ [GetComputeCertificateOutcome](#integration-server-sdk5-cpp-datatypes-getcomputecertificateoutcome)
+ [GetComputeCertificateResult](#integration-server-sdk5-cpp-datatypes-getcomputecertificateresult)
+ [GetFleetRoleCredentialsOutcome](#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsoutcome)
+ [GetFleetRoleCredentialsResult](#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsresult)
+ [ListContainersNetworkInfoOutcome](#integration-server-sdk5-cpp-datatypes-listcontainersnetworkinfooutcome)
+ [ListContainersNetworkInfoResult](#integration-server-sdk5-cpp-datatypes-listcontainersnetworkinforesult)
+ [ContainerNetworkInfo](#integration-server-sdk5-cpp-datatypes-containernetworkinfo)
+ [InitSDKOutcome](#integration-server-sdk5-cpp-datatypes-initsdkoutcome)
+ [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)
+ [Enums](#integration-server-sdk5-cpp-dataypes-enums)

## LogParameters
<a name="integration-server-sdk5-cpp-dataypes-log"></a>

An object identifying files generated during a game session that you want Amazon GameLift Servers to upload and store after the game session ends. The game server provides `LogParameters` to Amazon GameLift Servers as part of a `ProcessParameters` object in a [ProcessReady()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-processready) call.


|  |  | 
| --- |--- |
| **Properties** | Description | 
| LogPaths | The list of directory paths to game server log files you want Amazon GameLift Servers to store for future access. The server process generates these files during each game session. You define file paths and names in your game server and store them in the root game build directory. <br />The log paths must be absolute. For example, if your game build stores game session logs in a path like `MyGame\sessionLogs\`, then the path would be `c:\game\MyGame\sessionLogs` on a Windows instance.<br />**Type:** `std:vector<std::string>`<br />**Required:** No | 

## MetricsParameters
<a name="integration-server-sdk5-cpp-datatypes-metricsparameters"></a>

Use this data type to configure metrics collection and crash reporting for the game server. The game server communicates `MetricsParameters` to Amazon GameLift Servers in an [InitMetrics()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initmetrics) call.


|  |  | 
| --- |--- |
| **Properties** | Description | 
| StatsdHost | The hostname or IP address of the StatsD server for metrics collection.<br />**Type:** `std::string`<br />**Required:** No | 
| StatsdPort | The port number of the StatsD server for metrics collection.<br />**Type:** `int`<br />**Required:** No | 
| CrashReporterHost | The hostname or IP address of the crash reporter server.<br />**Type:** `std::string`<br />**Required:** No | 
| CrashReporterPort | The port number of the crash reporter server.<br />**Type:** `int`<br />**Required:** No | 
| FlushIntervalMs | The interval in milliseconds for flushing metrics data to the server.<br />**Type:** `int`<br />**Required:** No | 
| MaxPacketSize | The maximum size in bytes for metrics packets sent to the server.<br />**Type:** `int`<br />**Required:** No | 

## CustomLoggerConfiguration
<a name="integration-server-sdk5-cpp-datatypes-customloggerconfiguration"></a>

Use this data type to route the server SDK's log output to a custom log callback. The game server communicates `CustomLoggerConfiguration` to Amazon GameLift Servers in an [InitCustomLogger()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initcustomlogger) call.


|  |  | 
| --- |--- |
| **Properties** | Description | 
| callback | Amazon GameLift Servers invokes this callback function for each log message. The function receives the log level, the pre-formatted message string, and the `userData` context pointer. The message pointer is valid only for the duration of the callback invocation; copy the message if you need to retain it. The SDK serializes callback invocations, but any thread might invoke the callback. This value must not be `null`; the operation rejects a `null` callback with `BAD_REQUEST_EXCEPTION`.<br />**Type:** `Aws::GameLift::Server::LogCallback` (`void(*)(LogLevel level, const char* message, void* userData)`)<br />**Required:** Yes | 
| userData | A user-provided context pointer that Amazon GameLift Servers passes to the callback on each invocation. The SDK doesn't manage its lifetime. This pointer must remain valid until the process terminates.<br />**Type:** `void*`<br />**Required:** No | 
| minimumLogLevel | The minimum log level for the SDK. Amazon GameLift Servers will not invoke the provided callback for logs below this level. The default value is `LogLevel::Info`. To disable logging, set this value to `LogLevel::Off`.<br />**Type:** `Aws::GameLift::Server::LogLevel` enum value<br />**Required:** No | 

## ProcessParameters
<a name="integration-server-sdk5-cpp-dataypes-process"></a>

This data type contains the set of parameters sent to Amazon GameLift Servers in a [ProcessReady()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-processready).


|  |  | 
| --- |--- |
| **Properties** | Description | 
| LogParameters | An object with directory paths to files that are generated during a game session. Amazon GameLift Servers copies and stores the files for future access.**Type:** `Aws::GameLift::Server::LogParameters`<br />**Required:** No | 
| OnHealthCheck | The callback function that Amazon GameLift Servers invokes to request a health status report from the server process. Amazon GameLift Servers calls this function every 60 seconds and waits 60 seconds for a response. The server process returns TRUE if healthy, FALSE if not healthy. If no response is returned, Amazon GameLift Servers records the server process as not healthy.**Type:** `std::function<bool()> onHealthCheck`<br />**Required:** No | 
| OnProcessTerminate | The callback function that Amazon GameLift Servers invokes to force the server process to shut down. After calling this function, Amazon GameLift Servers waits 5 minutes for the server process to shut down and respond with a [ProcessEnding()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-processending) call before it shuts down the server process.**Type:** `std::function<void()> onProcessTerminate`<br />**Required:** Yes | 
| OnStartGameSession | The callback function that Amazon GameLift Servers invokes to activate a new game session. Amazon GameLift Servers calls this function in response to a client request [CreateGameSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameSession.html). The callback function passes a [GameSession](#integration-server-sdk5-cpp-dataypes-gamesession) object.**Type:** `const std::function<void(Aws::GameLift::Model::GameSession)> onStartGameSession`<br />**Required:** Yes | 
| OnUpdateGameSession | The callback function that Amazon GameLift Servers invokes to pass an updated game session object to the server process. Amazon GameLift Servers calls this function when a match backfill request has been processed to provide updated matchmaker data. It passes a [GameSession](#integration-server-sdk5-cpp-dataypes-gamesession) object, a status update (updateReason), and the match backfill ticket ID.**Type:** `std::function<void(Aws::GameLift::Server::Model::UpdateGameSession)> onUpdateGameSession`<br />**Required:** No | 
| Port | The port number the server process listens on for new player connections. The value must fall into the port range configured for any fleet deploying this game server build. This port number is included in game session and player session objects, which game sessions use when connecting to a server process.**Type:** `Integer`<br />**Required:** Yes | 

## UpdateGameSession
<a name="integration-server-sdk5-cpp-dataypes-updategamesession"></a>

This data type updates to a game session object, which includes the reason that the game session was updated and the related backfill ticket ID if backfill is used to fill player sessions in the game session.


| Properties | **Description** | 
| --- | --- | 
| GameSession | A [GameSession](#integration-server-sdk5-cpp-dataypes-gamesession) object. The GameSession object contains properties describing a game session. **Type:** `Aws::GameLift::Server::GameSession`<br />**Required:** Yes | 
| UpdateReason | The reason that the game session is being updated.**Type:** `Aws::GameLift::Server::UpdateReason`<br />**Required:** Yes | 
| BackfillTicketId | The ID of the backfill ticket attempting to update the game session.**Type:** `std::string`<br />**Required:** No | 

## GameSession
<a name="integration-server-sdk5-cpp-dataypes-gamesession"></a>

This data type provides details of a game session. 


| Properties | **Description** | 
| --- | --- | 
| GameSessionId | A unique identifier for the game session. A game session ARN has the following format: `arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`.<br />**Type:** `std::string`<br />**Required**: No | 
| Name | A descriptive label of the game session. <br />**Type:** `std::string`<br />**Required**: No | 
| FleetId | A unique identifier for the fleet that the game session is running on.<br />**Type:** `std::string`<br />**Required**: No | 
| MaximumPlayerSessionCount | The maximum number of player connections to the game session.<br />**Type:** `int`<br />**Required**: No | 
| Port | The port number for the game session. To connect to an Amazon GameLift Servers game server, an app needs both the IP address and port number.<br />**Type:** `in`<br />**Required**: No | 
| IpAddress | The IP address of the game session. To connect to an Amazon GameLift Servers game server, an app needs both the IP address and port number.<br />**Type:** `std::string`<br />**Required**: No | 
| GameSessionData | A set of custom game session properties, formatted as a single string value. <br />**Type:** `std::string`<br />**Required**: No | 
| MatchmakerData | Information about the matchmaking process that was used to create the game session, in JSON syntax, formatted as a string. In addition to the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments.<br />**Type:** `std::string`<br />**Required**: No | 
| GameProperties | A set of custom properties for a game session, formatted as key:value pairs. These properties are passed with a request to start a new game session.<br />**Type:** `std :: vector < GameProperty >`<br />**Required**: No | 
| DnsName | The DNS identifier assigned to the instance that's running the game session. Values have the following format:+  TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com`.  <br />+  Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com`.  <br />When connecting to a game session that's running on a TLS-enabled fleet, you must use the DNS name, not the IP address.<br />**Type:** `std::string`<br />**Required**: No | 

## ServerParameters
<a name="integration-server-sdk5-cpp-dataypes-serverparameters"></a>

Information that a game server process uses to establish a connection with the Amazon GameLift Servers service. Include these parameters when calling [InitSDK()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk-anywhere) only if the game server build will be deployed to an Anywhere fleet or a container fleet without the Amazon GameLift Servers Agent. For all other deployment scenarios, call [InitSDK()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-initsdk) without parameters.


| Properties | **Description** | 
| --- | --- | 
| webSocketUrl | The `GameLiftServerSdkEndpoint` Amazon GameLift Servers returns when you [`RegisterCompute`](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html) for a Amazon GameLift Servers Anywhere compute resource.<br />**Type:** `std::string`<br />**Required**: Yes  | 
| processId | A unique identifier registered to the server process hosting your game.<br />**Type:** `std::string`<br />**Required**: Yes | 
| hostId | The HostID is the ComputeName used when you registered your compute. For more information see, [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html).**Type:** `std::string`<br />**Required**: Yes | 
| fleetId | The unique identifier of the fleet that the compute is registered to. For more information see, [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html).**Type:** `std::string`<br />**Required**: Yes | 
| authToken | The authentication token generated by Amazon GameLift Servers that authenticates your server to Amazon GameLift Servers. For more information see, [GetComputeAuthToken](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetComputeAuthToken.html).**Type:** `std::string`<br />**Required**: Yes | 

## StartMatchBackfillRequest
<a name="integration-server-sdk5-cpp-dataypes-startmatchbackfillrequest"></a>

Information used to create a matchmaking backfill request. The game server communicates this information to Amazon GameLift Servers in a [StartMatchBackfill()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-startmatchbackfill) call.


| Properties | **Description** | 
| --- | --- | 
| GameSessionArn | A unique game session identifier. The API operation `[GetGameSessionId](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-cpp-actions.html#integration-server-sdk5-cpp-getgamesessionid)` returns the identifier in ARN format.<br />**Type:** `std::string`<br />**Required**: Yes | 
| MatchmakingConfigurationArn | A unique identifier, in the form of an ARN, for the matchmaker to use for this request. The matchmaker ARN for the original game session is in the game session object in the matchmaker data property. Learn more about matchmaker data in [Work with matchmaker data](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-server.html#match-server-data.html).<br />**Type:** `std::string`<br />**Required**: Yes | 
| Players | A set of data representing all players who are in the game session. The matchmaker uses this information to search for new players who are good matches for the current players.<br />**Type:** `std::vector<Player>`<br />**Required**: Yes | 
| TicketId | A unique identifier for a matchmaking or match backfill request ticket. If you don't provide a value, Amazon GameLift Servers generates one. Use this identifier to track the match backfill ticket status or cancel the request if needed. <br />**Type:** `std::string`<br />**Required**: No | 

## Player
<a name="integration-server-sdk5-cpp-dataypes-player"></a>

This data type represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and possibly latency data. Amazon GameLift Servers adds team information after a match is made.


| Properties | **Description** | 
| --- | --- | 
| LatencyInMS | A set of values expressed in milliseconds that indicate the amount of latency that a player experiences when connected to a location. <br />If this property is used, the player is only matched for locations listed. If a matchmaker has a rule that evaluates player latency, players must report latency to be matched.<br />**Type:** `Dictionary<string,int>`<br />**Required**: No | 
| PlayerAttributes | A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the PlayerAttributes used in a matchmaking rule set.<br />For more information about player attributes, see [AttributeValue](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_AttributeValue.html).<br />**Type:** `std::map<std::string,AttributeValue>`<br />**Required**: No | 
| PlayerId | A unique identifier for a player.<br />**Type:** `std::string`<br />**Required**: No | 
| Team | The name of the team that the player is assigned to in a match. You define team name in the matchmaking rule set.<br />**Type:** `std::string`<br />**Required**: No | 

## DescribePlayerSessionsRequest
<a name="integration-server-sdk5-cpp-dataypes-playersessions"></a>

An object that specifies which player sessions to retrieve. The server process provides this information with a [DescribePlayerSessions()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-describeplayersessions) call to Amazon GameLift Servers.


| Properties | **Description** | 
| --- | --- | 
| GameSessionId | A unique game session identifier. Use this parameter to request all player sessions for the specified game session. <br />Game session ID format is `arn:aws:gamelift:<region>::gamesession/fleet-<fleet ID>/<ID string>`. The `GameSessionID` is a custom ID string or a<br />**Type:** `std::string`<br />**Required**: No | 
| PlayerSessionId | The unique identifier for a player session. Use this parameter to request a single specific player session.<br />**Type:** `std::string`<br />**Required**: No | 
| PlayerId | The unique identifier for a player. Use this parameter to request all player sessions for a specific player. See [Generate player IDs](player-sessions-player-identifiers.md).<br />**Type:** `std::string`<br />**Required**: No | 
| PlayerSessionStatusFilter | The player session status to filter results on. Possible player session statuses include:+  RESERVED – The player session request was received, but the player hasn't connected to the server process or been validated. <br />+  ACTIVE – The player was validated by the server process and is connected. <br />+  COMPLETED – The player connection dropped. <br />+  TIMEDOUT – A player session request was received, but the player didn't connect or wasn't validated within the time-out limit (60 seconds). <br />**Type:** `std::string`<br />**Required**: No | 
| NextToken | The token indicating the start of the next page of results. To specify the start of the result set, don't provide a value. If you provide a player session ID, this parameter is ignored.<br />**Type:** `std::string`<br />**Required**: No | 
| Limit | The maximum number of results to return. If you provide a player session ID, this parameter is ignored.<br />**Type:** `int`<br />**Required**: No | 

## StopMatchBackfillRequest
<a name="integration-server-sdk5-cpp-dataypes-stopmatchbackfillrequest"></a>

Information used to cancel a matchmaking backfill request. The game server communicates this information to Amazon GameLift Servers service in a [StopMatchBackfill()](integration-server-sdk5-cpp-actions.md#integration-server-sdk5-cpp-stopmatchbackfill) call.


| Properties | **Description** | 
| --- | --- | 
| GameSessionArn | A unique game session identifier of the request being canceled.<br />**Type:** `char[]`<br />**Required**: No | 
| MatchmakingConfigurationArn | A unique identifier of the matchmaker this request was sent to.<br />**Type:** `char[]`<br />**Required**: No | 
| TicketId | A unique identifier of the backfill request ticket to be canceled.<br />**Type:** `char[]`<br />**Required**: No | 

## AttributeValue
<a name="integration-server-sdk5-cpp-dataypes-attributevalue"></a>

Use these values in [Player](#integration-server-sdk5-cpp-dataypes-player) attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each `AttributeValue` object must use exactly one of the available properties: `S`, `N`, `SL`, or `SDM`.


| Properties | Description | 
| --- | --- | 
| AttrType | Specifies the type of attribute value. Possible attribute value types include: + **NONE**<br />+ **STRING**<br />+ **DOUBLE**<br />+ **STRING\_LIST**<br />+ **STRING\_DOUBLE\_MAP**<br />**Required:** No | 
| S | Represents a string attribute value.<br />**Type:** `std::string`<br />**Required:** No | 
| N | Represents a numeric attribute value.<br />**Type:** `double`<br />**Required:** No | 
| SL | Represents an array of string attribute values.<br />**Type:** `std::vector<std::string>`<br />**Required:** No | 
| SDM | Represents a dictionary of string keys and double values.<br />**Type:** `std::map<std::string, double>`<br />**Required:** No | 

## GetFleetRoleCredentialsRequest
<a name="integration-server-sdk5-cpp-dataypes-getfleetrolecredentialsrequest"></a>

This data type gives the game server limited access to your other AWS resources. For more information see, [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md).


| Properties | **Description** | 
| --- | --- | 
| RoleArn | The Amazon Resource Name (ARN) of the service role that extends limited access to your AWS resources.**Type:** `std::string`<br />**Required**: No | 
| RoleSessionName | The role session name that you can use to uniquely identify an AWS Security Token Service [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) session. This name is exposed in audit logs such as those in CloudTrail. **Type:** `std::string` <br />**Required**: No  | 

## AwsLongOutcome
<a name="integration-server-sdk5-cpp-datatypes-awslongoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** `long`<br />**Required:** No | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `long&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## AwsStringOutcome
<a name="integration-server-sdk5-cpp-datatypes-awsstringoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** `std::string`<br />**Required:** No | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `long&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## DescribePlayerSessionsOutcome
<a name="integration-server-sdk5-cpp-datatypes-describeplayersessionsoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [DescribePlayerSessionsResult](#integration-server-sdk5-cpp-datatypes-describeplayersessionsresult)<br />**Required:** No  | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `Aws::GameLift::Server::Model::DescribePlayerSessionsResult&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## DescribePlayerSessionsResult
<a name="integration-server-sdk5-cpp-datatypes-describeplayersessionsresult"></a>

A collection of objects containing properties for each player session that matches the request. 


| Properties | Description | 
| --- | --- | 
| NextToken | A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored. <br />**Type:** `std::string`<br />**Required:** Yes | 
| PlayerSessions | **Type:** `IList<PlayerSession>`<br />**Required:**  | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `std::string&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## GenericOutcome
<a name="integration-server-sdk5-cpp-datatypes-genericoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## GenericOutcomeCallable
<a name="integration-server-sdk5-cpp-datatypes-genericoutcomecallable"></a>

This data type is an asynchronous generic outcome. It has the following properties: 


| Properties | Description | 
| --- | --- | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## PlayerSession
<a name="integration-server-sdk5-cpp-datatypes-playersession"></a>

This data type represents a player session that Amazon GameLift Servers passes to the game server. For more information, see [PlayerSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PlayerSession.html). 


| Properties | Description | 
| --- | --- | 
| CreationTime | **Type:** `long`<br />**Required:** No | 
| FleetId | **Type:** `std::string`<br />**Required:** No | 
| GameSessionId | **Type:** `std::string`<br />**Required:** No | 
| IpAddress | **Type:** `std::string`<br />**Required:** No | 
| PlayerData | **Type:** `std::string`<br />**Required:** No | 
| PlayerId | **Type:** `std::string`<br />**Required:** No | 
| PlayerSessionId | **Type:** `std::string`<br />**Required:** No | 
| Port | **Type:** `int`<br />**Required:** No | 
| Status | Player session status to filter results on. When a PlayerSessionId or PlayerId is provided, then the PlayerSessionStatusFilter has no effect on the response. <br />**Type:** A `PlayerSessionStatus` enum. Possible values include the following: + **ACTIVE**<br />+ **COMPLETED**<br />+ **NOT\_SET**<br />+ **RESERVED**<br />+ **TIMEDOUT**<br />**Required:** No | 
| TerminationTime | **Type:** `long`<br />**Required:** No | 
| DnsName | **Type:** `std::string`<br />**Required:** No | 

## StartMatchBackfillOutcome
<a name="integration-server-sdk5-cpp-datatypes-startmatchbackfilloutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [StartMatchBackfillResult](#integration-server-sdk5-cpp-datatypes-startmatchbackfillresult)<br />**Required:** No | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `StartMatchBackfillResult&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## StartMatchBackfillResult
<a name="integration-server-sdk5-cpp-datatypes-startmatchbackfillresult"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| TicketId | A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift Servers will generate one in the form of a UUID. Use this identifier to track the match backfill ticket status and retrieve match results. <br />**Type:** `std::string`<br />**Required:** No | 

## GetComputeCertificateOutcome
<a name="integration-server-sdk5-cpp-datatypes-getcomputecertificateoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [GetComputeCertificateResult](#integration-server-sdk5-cpp-datatypes-getcomputecertificateresult)<br />**Required:** No  | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `Aws::GameLift::Server::Model::GetComputeCertificateResult&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## GetComputeCertificateResult
<a name="integration-server-sdk5-cpp-datatypes-getcomputecertificateresult"></a>

The path to the TLS certificate on your compute and the compute's host name.


| Properties | Description | 
| --- | --- | 
| CertificatePath | The path to the TLS certificate on your compute resource. When using an Amazon GameLift Servers managed fleet, this path contains: +  `certificate.pem`: The end-user certificate. The full certificate chain is the combination of `certificateChain.pem` appended to this certificate. <br />+  `certificateChain.pem`: The certificate chain that contains the root certificate and intermediate certificates. <br />+  `rootCertificate.pem`: The root certificate. <br />+  `privateKey.pem`: The private key for the end-user certificate. <br />**Type:** `std::string`<br />**Required:** No | 
| ComputeName | The name of your compute resource.<br />**Type:** `std::string`<br />**Required:** No | 

## GetFleetRoleCredentialsOutcome
<a name="integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [GetFleetRoleCredentialsResult](#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsresult)<br />**Required:** No  | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `Aws::GameLift::Server::Model::GetFleetRoleCredentialsResult`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## GetFleetRoleCredentialsResult
<a name="integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsresult"></a>


| Properties | Description | 
| --- | --- | 
| AccessKeyId | The access key ID to authenticate and provide access to your AWS resources.<br />**Type:** `string`<br />**Required:** No | 
| AssumedRoleId | The ID of the user that the service role belongs to.<br />**Type:** `string`<br />**Required:** No | 
| AssumedRoleUserArn | The Amazon Resource Name (ARN) of the user that the service role belongs to.<br />**Type:** `string`<br />**Required:** No | 
| Expiration | The amount of time until your session credentials expire.<br />**Type:** `DateTime`<br />**Required:** No | 
| SecretAccessKey | The secret access key ID for authentication.<br />**Type:** `string`<br />**Required:** No | 
| SessionToken | A token to identify the current active session interacting with your AWS resources.<br />**Type:** `string`<br />**Required:** No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## ListContainersNetworkInfoOutcome
<a name="integration-server-sdk5-cpp-datatypes-listcontainersnetworkinfooutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [ListContainersNetworkInfoResult](#integration-server-sdk5-cpp-datatypes-listcontainersnetworkinforesult)<br />**Required:** No  | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `Aws::GameLift::Server::Model::ListContainersNetworkInfoResult&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## ListContainersNetworkInfoResult
<a name="integration-server-sdk5-cpp-datatypes-listcontainersnetworkinforesult"></a>

Network information for all containers running on the same instance as the calling game server process.


| Properties | Description | 
| --- | --- | 
| ContainersNetworkInfo | The list of network information for each container running on the instance.<br />**Type:** `std::vector<ContainerNetworkInfo>` when `GAMELIFT_USE_STD` is defined; otherwise a fixed array with an accessor named `GetContainersNetworkInfoCount()`.<br />**Required:** No | 

## ContainerNetworkInfo
<a name="integration-server-sdk5-cpp-datatypes-containernetworkinfo"></a>

Network information for a single container running on the instance.


| Properties | Description | 
| --- | --- | 
| ContainerName | The name of the container, as defined in the container group definition.<br />**Type:** `std::string` when `GAMELIFT_USE_STD` is defined; otherwise `char[]`.<br />**Required:** No | 
| ContainerId | The unique identifier of the container.<br />**Type:** `std::string` when `GAMELIFT_USE_STD` is defined; otherwise `char[]`.<br />**Required:** No | 
| IpAddress | The container's local IPv4 address on the Docker bridge network.<br />**Type:** `std::string` when `GAMELIFT_USE_STD` is defined; otherwise `char[]`.<br />**Required:** No | 
| ContainerGroupType | The type of container group that the container belongs to.<br />**Type:** A `ContainerGroupType` [enum](#integration-server-sdk5-cpp-dataypes-enums).<br />**Required:** No | 

## InitSDKOutcome
<a name="integration-server-sdk5-cpp-datatypes-initsdkoutcome"></a>

**Note**  
`InitSDKOutcome` is returned only when you build the SDK with the `std` flag. If you build with the `nostd` flag, then [GenericOutcome](#integration-server-sdk5-cpp-datatypes-genericoutcome) is returned instead.


| Properties | Description | 
| --- | --- | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-cpp-datatypes-gamelifterror)<br />**Required:** No | 

## GameLiftError
<a name="integration-server-sdk5-cpp-datatypes-gamelifterror"></a>


| Properties | Description | 
| --- | --- | 
| ErrorType | The type of error.<br />**Type:** A `GameLiftErrorType` [enum](#integration-server-sdk5-cpp-dataypes-enums).<br />**Required:** No  | 
| ErrorName | The name of the error.<br /> **Type:** `std::string` <br />**Required:** No  | 
| ErrorMessage | The error message.<br /> **Type:** `std::string` <br />**Required:** No  | 

## Enums
<a name="integration-server-sdk5-cpp-dataypes-enums"></a>

Enums defined for the server SDK for Amazon GameLift Servers (C\+\+) are defined as follows: 

**GameLiftErrorType**  
String value indicating the error type. Valid values include:  
+ **BAD\_REQUEST\_EXCEPTION** 
+ **GAMESESSION\_ID\_NOT\_SET** – The game session ID has not been set. 
+ **INTERNAL\_SERVICE\_EXCEPTION** 
+ **UNSUPPORTED\_COMPUTE\_TYPE\_EXCEPTION** – The API that was called was unsupported on the compute type. 
+ **LOCAL\_CONNECTION\_FAILED** – The local connection to Amazon GameLift Servers failed. 
+ **NETWORK\_NOT\_INITIALIZED** – The network has not been initialized. 
+ **SERVICE\_CALL\_FAILED** – A call to an AWS service has failed. 
+ **WEBSOCKET\_CONNECT\_FAILURE** 
+ **WEBSOCKET\_CONNECT\_FAILURE\_FORBIDDEN** 
+ **WEBSOCKET\_CONNECT\_FAILURE\_INVALID\_URL** 
+ **WEBSOCKET\_CONNECT\_FAILURE\_TIMEOUT** 
+ **ALREADY\_INITIALIZED** – The Amazon GameLift Servers Server or Client has already been initialized with Initialize(). 
+ **FLEET\_MISMATCH** – The target fleet does not match the fleet of a gameSession or playerSession. 
+ **GAMELIFT\_CLIENT\_NOT\_INITIALIZED** – The Amazon GameLift Servers client has not been initialized. 
+ **GAMELIFT\_SERVER\_NOT\_INITIALIZED** – The Amazon GameLift Servers server has not been initialized. 
+ **GAME\_SESSION\_ENDED\_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the game session ended. 
+ **GAME\_SESSION\_NOT\_READY** – The Amazon GameLift Servers Server Game Session was not activated. 
+ **GAME\_SESSION\_READY\_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the game session is ready. 
+ **INITIALIZATION\_MISMATCH** – A client method was called after Server::Initialize(), or vice versa. 
+ **NOT\_INITIALIZED** – The Amazon GameLift Servers Server or Client has not been initialized with Initialize(). 
+ **NO\_TARGET\_ALIASID\_SET** – A target aliasId has not been set. 
+ **NO\_TARGET\_FLEET\_SET** – A target fleet has not been set. 
+ **PROCESS\_ENDING\_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the process is ending. 
+ **PROCESS\_NOT\_ACTIVE** – The server process is not yet active, not bound to a GameSession, and cannot accept or process PlayerSessions. 
+ **PROCESS\_NOT\_READY** – The server process is not yet ready to be activated. 
+ **PROCESS\_READY\_FAILED** – the server SDK for Amazon GameLift Servers could not contact the service to report the process is ready. 
+ **SDK\_VERSION\_DETECTION\_FAILED** – SDK version detection failed. 
+ **STX\_CALL\_FAILED** – A call to the XStx server backend component has failed. 
+ **STX\_INITIALIZATION\_FAILED** – The XStx server backend component has failed to initialize. 
+ **UNEXPECTED\_PLAYER\_SESSION** – An unregistered player session was encountered by the server. 
+ **WEBSOCKET\_CONNECT\_FAILURE** 
+ **WEBSOCKET\_CONNECT\_FAILURE\_FORBIDDEN** 
+ **WEBSOCKET\_CONNECT\_FAILURE\_INVALID\_URL** 
+ **WEBSOCKET\_CONNECT\_FAILURE\_TIMEOUT** 
+ **WEBSOCKET\_RETRIABLE\_SEND\_MESSAGE\_FAILURE** – Retriable failure to send a message to the GameLift Service WebSocket. 
+ **WEBSOCKET\_SEND\_MESSAGE\_FAILURE** – Failure to send a message to the GameLift Service WebSocket. 
+ **MATCH\_BACKFILL\_REQUEST\_VALIDATION** – Validation of the request failed. 
+ **PLAYER\_SESSION\_REQUEST\_VALIDATION** – Validation of the request failed. 

**ContainerGroupType**  
The type of container group that a container belongs to. Valid values include:  
+ **GAME\_SERVER** – A game server replica container group. An instance can have multiple game server container groups. 
+ **PER\_INSTANCE** – A per-instance daemon container group. An instance has exactly one per-instance container group. 

**PlayerSessionCreationPolicy**  
String value indicating whether the game session accepts new players. Valid values include:   
+ **ACCEPT\_ALL** – Accept all new player sessions. 
+ **DENY\_ALL** – Deny all new player sessions. 
+ **NOT\_SET** – The game session is not set to accept or deny new player sessions. 

**LogLevel**  
The severity level of a log message. Values increase in severity from `Trace` (most verbose) to `Fatal` (most severe). `Off` is not a log severity, but you can use it as the minimum log level in a [CustomLoggerConfiguration](#integration-server-sdk5-cpp-datatypes-customloggerconfiguration) to disable logging. Valid values include:  
+ **Trace** – The most verbose level, used for fine-grained diagnostic messages.
+ **Debug** – Detailed information useful for debugging.
+ **Info** – General informational messages. This is the default minimum log level.
+ **Warn** – Messages that indicate a potential problem.
+ **Error** – Messages that indicate a recoverable error.
+ **Fatal** – The most severe level, used for unrecoverable errors.
+ **Off** – Disables all log callback dispatching.