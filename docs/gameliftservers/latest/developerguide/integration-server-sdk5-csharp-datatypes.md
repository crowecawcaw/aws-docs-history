

# C\# server SDK 5.x for Amazon GameLift Servers -- Data types
<a name="integration-server-sdk5-csharp-datatypes"></a>

Use the Amazon GameLift Servers C\# server SDK 5.x reference to integrate your multiplayer game for hosting with Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server with the server SDK](gamelift-sdk-server-api.md). If you're using the Amazon GameLift Servers plugin for Unity, see also [Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md).

[C\# server SDK 5.x for Amazon GameLift Servers -- Actions](integration-server-sdk5-csharp-actions.md)

**Topics**
+ [LogParameters](#integration-server-sdk5-csharp-dataypes-log)
+ [MetricsParameters](#integration-server-sdk5-csharp-datatypes-metricsparameters)
+ [ProcessParameters](#integration-server-sdk5-csharp-dataypes-process)
+ [UpdateGameSession](#integration-server-sdk5-csharp-dataypes-updategamesession)
+ [GameSession](#integration-server-sdk5-csharp-dataypes-gamesession)
+ [ServerParameters](#integration-server-sdk5-csharp-dataypes-serverparameters)
+ [StartMatchBackfillRequest](#integration-server-sdk5-csharp-dataypes-startmatchbackfillrequest)
+ [Player](#integration-server-sdk5-csharp-dataypes-player)
+ [DescribePlayerSessionsRequest](#integration-server-sdk5-csharp-dataypes-playersessions)
+ [StopMatchBackfillRequest](#integration-server-sdk5-csharp-dataypes-stopmatchbackfillrequest)
+ [GetFleetRoleCredentialsRequest](#integration-server-sdk5-csharp-dataypes-getfleetrolecredentialsrequest)
+ [AttributeValue](#integration-server-sdk5-csharp-datatypes-attributevalue)
+ [AwsStringOutcome](#integration-server-sdk5-csharp-datatypes-awsstringoutcome)
+ [GenericOutcome](#integration-server-sdk5-csharp-datatypes-genericoutcome)
+ [MetricsManagerOutcome](#integration-server-sdk5-csharp-datatypes-metricsmanageroutcome)
+ [DescribePlayerSessionsOutcome](#integration-server-sdk5-csharp-datatypes-describeplayersessionsoutcome)
+ [DescribePlayerSessionsResult](#integration-server-sdk5-csharp-datatypes-describeplayersessionsresult)
+ [PlayerSession](#integration-server-sdk5-csharp-datatypes-playersession)
+ [StartMatchBackfillOutcome](#integration-server-sdk5-csharp-datatypes-startmatchbackfilloutcome)
+ [StartMatchBackfillResult](#integration-server-sdk5-csharp-datatypes-startmatchbackfillresult)
+ [GetComputeCertificateOutcome](#integration-server-sdk5-csharp-datatypes-getcomputecertificateoutcome)
+ [GetComputeCertificateResult](#integration-server-sdk5-csharp-datatypes-getcomputecertificateresult)
+ [GetFleetRoleCredentialsOutcome](#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsoutcome)
+ [GetFleetRoleCredentialsResult](#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsresult)
+ [ListContainersNetworkInfoOutcome](#integration-server-sdk5-csharp-datatypes-listcontainersnetworkinfooutcome)
+ [ListContainersNetworkInfoResult](#integration-server-sdk5-csharp-datatypes-listcontainersnetworkinforesult)
+ [ContainerNetworkInfo](#integration-server-sdk5-csharp-datatypes-containernetworkinfo)
+ [AwsDateTimeOutcome](#integration-server-sdk5-csharp-datatypes-awsdatetimeoutcome)
+ [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)
+ [Enums](#integration-server-sdk5-csharp-datatypes-enums)

## LogParameters
<a name="integration-server-sdk5-csharp-dataypes-log"></a>

Use this data type to identify files generated during a game session that you want the game server to upload to Amazon GameLift Servers after the game session ends. The game server communicates `LogParameters to` Amazon GameLift Servers in a [ProcessReady()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-processready) call.


|  |  | 
| --- |--- |
| **Properties** | Description | 
| LogPaths | The list of directory paths to game server log files you want Amazon GameLift Servers to store for future access. The server process generates these files during each game session. You define file paths and names in your game server and store them in the root game build directory. <br />The log paths must be absolute. For example, if your game build stores game session logs in a path like `MyGame\sessionLogs\`, then the path would be `c:\game\MyGame\sessionLogs` on a Windows instance.<br />**Type:** `List<String>`<br />**Required:** No | 

## MetricsParameters
<a name="integration-server-sdk5-csharp-datatypes-metricsparameters"></a>

Use this data type to configure metrics collection and crash reporting for the game server. The game server communicates `MetricsParameters` to Amazon GameLift Servers in an [InitMetrics()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initmetrics) call.


|  |  | 
| --- |--- |
| **Properties** | Description | 
| StatsdHost | The hostname or IP address of the StatsD server for metrics collection.<br />**Type:** `String`<br />**Required:** No | 
| StatsdPort | The port number of the StatsD server for metrics collection.<br />**Type:** `Integer`<br />**Required:** No | 
| CrashReporterHost | The hostname or IP address of the crash reporter server.<br />**Type:** `String`<br />**Required:** No | 
| CrashReporterPort | The port number of the crash reporter server.<br />**Type:** `Integer`<br />**Required:** No | 
| FlushIntervalMs | The interval in milliseconds for flushing metrics data to the server.<br />**Type:** `Integer`<br />**Required:** No | 
| MaxPacketSize | The maximum size in bytes for metrics packets sent to the server.<br />**Type:** `Integer`<br />**Required:** No | 

## ProcessParameters
<a name="integration-server-sdk5-csharp-dataypes-process"></a>

This data type contains the set of parameters sent to Amazon GameLift Servers in a [ProcessReady()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-processready) call.


|  |  | 
| --- |--- |
| **Properties** | Description | 
| LogParameters | The object with a list of directory paths to game session log files.**Type:** `Aws::GameLift::Server::LogParameters`<br />**Required:** Yes | 
| OnHealthCheck | The name of callback function that Amazon GameLift Servers invokes to request a health status report from the server process. Amazon GameLift Servers calls this function every 60 seconds. After calling this function Amazon GameLift Servers waits 60 seconds for a response, if none is received, Amazon GameLift Servers records the server process as unhealthy.**Type:** `void OnHealthCheckDelegate()`<br />**Required:** Yes | 
| OnProcessTerminate | The name of callback function that Amazon GameLift Servers invokes to force the server process to shut down. After calling this function, Amazon GameLift Servers waits five minutes for the server process to shut down and respond with a [ProcessEnding()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-processending) call before it shuts down the server process.**Type:** `void OnProcessTerminateDelegate()`<br />**Required:** Yes | 
| OnStartGameSession | The name of callback function that Amazon GameLift Servers invokes to activate a new game session. Amazon GameLift Servers calls this function in response to the client request [CreateGameSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameSession.html). The callback function takes a [GameSession](#integration-server-sdk5-csharp-dataypes-gamesession) object.**Type:** `void OnStartGameSessionDelegate(GameSession)`<br />**Required:** Yes | 
| OnUpdateGameSession | The name of callback function that Amazon GameLift Servers invokes to pass an updated game session object to the server process. Amazon GameLift Servers calls this function when a match backfill request has been processed to provide updated matchmaker data. It passes a [GameSession](#integration-server-sdk5-csharp-dataypes-gamesession) object, a status update (updateReason), and the match backfill ticket ID.**Type:** void OnUpdateGameSessionDelegate([UpdateGameSession](#integration-server-sdk5-csharp-dataypes-updategamesession))<br />**Required:** No | 
| Port | The port number that the server process listens on for new player connections. The value must fall into the port range configured for any fleet deploying this game server build. This port number is included in game session and player session objects, which game sessions use when connecting to a server process.**Type:** `Integer`<br />**Required:** Yes | 

## UpdateGameSession
<a name="integration-server-sdk5-csharp-dataypes-updategamesession"></a>

Updated information for a game session object, includes the reason that the game session was updated. If the update is related to a match backfill action, this data type includes the backfill ticket ID.


| Properties | **Description** | 
| --- | --- | 
| GameSession | A [GameSession](#integration-server-sdk5-csharp-dataypes-gamesession) object. The GameSession object contains properties describing a game session. **Type:** `GameSession GameSession()`<br />**Required:** Yes | 
| UpdateReason | The reason that the game session is being updated.**Type:** `UpdateReason UpdateReason()`<br />**Required:** Yes | 
| BackfillTicketId | The ID of the backfill ticket attempting to update the game session.**Type:** `String`<br />**Required:** Yes | 

## GameSession
<a name="integration-server-sdk5-csharp-dataypes-gamesession"></a>

Details of a game session. 


| Properties | **Description** | 
| --- | --- | 
| GameSessionId | A unique identifier for the game session. A game session ARN has the following format: `arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`.<br />**Type:** `String`<br />**Required**: No | 
| Name | A descriptive label of the game session. <br />**Type:** `String`<br />**Required**: No | 
| FleetId | A unique identifier for the fleet that the game session is running on.<br />**Type:** `String`<br />**Required**: No | 
| MaximumPlayerSessionCount | The maximum number of player connections to the game session.<br />**Type:** `Integer`<br />**Required**: No | 
| Port | The port number for the game session. To connect to an Amazon GameLift Servers game server, an app needs both the IP address and port number.<br />**Type:** `Integer`<br />**Required**: No | 
| IpAddress | The IP address of the game session. To connect to an Amazon GameLift Servers game server, an app needs both the IP address and port number.<br />**Type:** `String`<br />**Required**: No | 
| GameSessionData | A set of custom game session properties, formatted as a single string value. <br />**Type:** `String`<br />**Required**: No | 
| MatchmakerData | The information about the matchmaking process that was used to create the game session, in JSON syntax, formatted as a string. In addition to the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments.<br />**Type:** `String`<br />**Required**: No | 
| GameProperties | A set of custom properties for a game session, formatted as key:value pairs. These properties are passed with a request to start a new game session.<br />**Type:** `Dictionary<string, string>`<br />**Required**: No | 
| DnsName | The DNS identifier assigned to the instance that's running the game session. Values have the following format:+  TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com`.  <br />+  Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com`.  <br />When connecting to a game session that's running on a TLS-enabled fleet, you must use the DNS name, not the IP address.<br />**Type:** `String`<br />**Required**: No | 

## ServerParameters
<a name="integration-server-sdk5-csharp-dataypes-serverparameters"></a>

Information used to maintain the connection between an Amazon GameLift Servers Anywhere server and the Amazon GameLift Servers service. This information is used when launching new server processes with [InitSDK()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initsdk). For servers hosted on Amazon GameLift Servers managed EC2 instances, use an empty object.


| Properties | **Description** | 
| --- | --- | 
| WebSocketUrl | The `GameLiftServerSdkEndpoint` returned when you `RegisterCompute` as part of Amazon GameLift Servers Anywhere.<br />**Type:** `String`<br />**Required**: Yes | 
| ProcessId | A unique identifier registered to the server process hosting your game.<br />**Type:** `String`<br />**Required**: Yes | 
| HostId | A unique identifier for the host with the server processes hosting your game. The hostId is the ComputeName used when you registered your compute. For more information see, [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html)<br />**Type:** `String`<br />**Required**: Yes | 
| FleetId | The fleet ID of the fleet that the compute is registered to. For more information see, [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html).**Type:** `String`<br />**Required**: Yes | 
| AuthToken | The authentication token generated by Amazon GameLift Servers that authenticates your server to Amazon GameLift Servers. For more information see, [GetComputeAuthToken](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetComputeAuthToken.html).**Type:** `String`<br />**Required**: Yes | 

## StartMatchBackfillRequest
<a name="integration-server-sdk5-csharp-dataypes-startmatchbackfillrequest"></a>

Information used to create a matchmaking backfill request. The game server communicates this information to Amazon GameLift Servers in a [StartMatchBackfill()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-startmatchbackfill) call.


| Properties | **Description** | 
| --- | --- | 
| GameSessionArn | The unique game session identifier. The API operation `[GetGameSessionId](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-csharp-actions.html#integration-server-sdk5-csharp-getgamesessionid)` returns the identifier in ARN format.<br />**Type:** `String`<br />**Required**: Yes | 
| MatchmakingConfigurationArn | The unique identifier, in the form of an ARN, for the matchmaker to use for this request. The matchmaker ARN for the original game session is in the game session object in the matchmaker data property. Learn more about matchmaker data in [Work with matchmaker data](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-server.html#match-server-data.html).<br />**Type:** `String`<br />**Required**: Yes | 
| Players | A set of data that represents all players who are currently in the game session. The matchmaker uses this information to search for new players who are good matches for the current players.<br />**Type:** `List<Player>`<br />**Required**: Yes | 
| TicketId | The unique identifier for a matchmaking or match backfill request ticket. If you don't provide a value, Amazon GameLift Servers generates one. Use this identifier to track the match backfill ticket status or cancel the request if needed. <br />**Type:** `String`<br />**Required**: No | 

## Player
<a name="integration-server-sdk5-csharp-dataypes-player"></a>

Represents a player in matchmaking. When a matchmaking request starts, a player has a player ID, attributes, and possibly latency data. Amazon GameLift Servers adds team information after a match is made.


| Properties | **Description** | 
| --- | --- | 
| LatencyInMS | A set of values expressed in milliseconds, that indicate the amount of latency that a player experiences when connected to a location. <br />If this property is used, the player is only matched for locations listed. If a matchmaker has a rule that evaluates player latency, players must report latency to be matched.<br />**Type:** `Dictionary<string, int>`<br />**Required**: No | 
| PlayerAttributes | A collection of key:value pairs that contain player information for use in matchmaking. Player attribute keys must match the PlayerAttributes used in a matchmaking rule set.<br />For more information about player attributes, see [AttributeValue](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_AttributeValue.html).<br />**Type:** `Dictionary<string, AttributeValue`<br />**Required**: No | 
| PlayerId | A unique identifier for a player.<br />**Type:** `String`<br />**Required**: No | 
| Team | The name of the team that the player is assigned to in a match. You define team name in the matchmaking rule set.<br />**Type:** `String`<br />**Required**: No | 

## DescribePlayerSessionsRequest
<a name="integration-server-sdk5-csharp-dataypes-playersessions"></a>

This data type is used to specify which player session(s) to retrieve. It can be used in several ways: (1) provide a PlayerSessionId to request a specific player session; (2) provide a GameSessionId to request all player sessions in the specified game session; or (3) provide a PlayerId to request all player sessions for the specified player. For large collections of player sessions, use the pagination parameters to retrieve results as sequential pages.


| Properties | **Description** | 
| --- | --- | 
| GameSessionId | The unique game session identifier. Use this parameter to request all player sessions for the specified game session. Game session ID format is as follows: `arn:aws:gamelift:<region>::gamesession/fleet-<fleet ID>/<ID string>`. The value of <ID string> is either a custom ID string (if one was specified when the game session was created) or a generated string. <br />**Type:** `String`<br />**Required**: No | 
| PlayerSessionId | The unique identifier for a player session.<br />**Type:** `String`<br />**Required**: No | 
| PlayerId | The unique identifier for a player. See [Generate player IDs](player-sessions-player-identifiers.md).<br />**Type:** `String`<br />**Required**: No | 
| PlayerSessionStatusFilter | The player session status to filter results on. Possible player session statuses include the following:+  RESERVED – The player session request has been received, but the player has not yet connected to the server process and/or been validated. <br />+  ACTIVE – The player has been validated by the server process and is currently connected. <br />+  COMPLETED – The player connection has been dropped. <br />+  TIMEDOUT – A player session request was received, but the player did not connect and/or was not validated within the time-out limit (60 seconds). <br />**Type:** `String`<br />**Required**: No | 
| NextToken | The token indicating the start of the next page of results. To specify the start of the result set, don't provide a value. If you provide a player session ID, this parameter is ignored.<br />**Type:** `String`<br />**Required**: No | 
| Limit | The maximum number of results to return. If you provide a player session ID, this parameter is ignored.<br />**Type:** `int`<br />**Required**: No | 

## StopMatchBackfillRequest
<a name="integration-server-sdk5-csharp-dataypes-stopmatchbackfillrequest"></a>

Information used to cancel a matchmaking backfill request. The game server communicates this information to Amazon GameLift Servers service in a [StopMatchBackfill()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-stopmatchbackfill) call.


| Properties | **Description** | 
| --- | --- | 
| GameSessionArn | The unique game session identifier of the request being canceled.<br />**Type:** `string`<br />**Required**: Yes | 
| MatchmakingConfigurationArn | The unique identifier of the matchmaker this request was sent to.<br />**Type:** `string`<br />**Required**: Yes | 
| TicketId | The unique identifier of the backfill request ticket to be canceled.<br />**Type:** `string`<br />**Required**: Yes | 

## GetFleetRoleCredentialsRequest
<a name="integration-server-sdk5-csharp-dataypes-getfleetrolecredentialsrequest"></a>

This data type gives the game server limited access to your other AWS resources. For more information see, [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md).


| Properties | **Description** | 
| --- | --- | 
| RoleArn | The Amazon Resource Name (ARN) of the service role that extends limited access to your AWS resources. **Type:** `string`<br />**Required**: Yes | 
| RoleSessionName | The name of the session that describes the use of the role credentials. **Type:** `string`<br />**Required**: No | 

## AttributeValue
<a name="integration-server-sdk5-csharp-datatypes-attributevalue"></a>

Use these values in [Player](#integration-server-sdk5-csharp-dataypes-player) attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each `AttributeValue` object can use only one of the available properties.


| Properties | Description | 
| --- | --- | 
| attrType | Specifies the type of attribute value.<br />**Type:** An `AttrType` [enum](#integration-server-sdk5-csharp-datatypes-enums) value. <br />**Required:** No | 
| S | Represents a string attribute value.<br />**Type:** `string`<br />**Required:** Yes | 
| N | Represents a numeric attribute value.<br />**Type:** `double`<br />**Required:** Yes | 
| SL | Represents an array of string attribute values.<br />**Type:** `string[]`<br />**Required:** Yes | 
| SDM | Represents a dictionary of string keys and double values.<br />**Type:** `Dictionary<string, double>`<br />**Required:** Yes | 

## AwsStringOutcome
<a name="integration-server-sdk5-csharp-datatypes-awsstringoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** `string`<br />**Required:** No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## GenericOutcome
<a name="integration-server-sdk5-csharp-datatypes-genericoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## MetricsManagerOutcome
<a name="integration-server-sdk5-csharp-datatypes-metricsmanageroutcome"></a>

Represents the result of an [InitMetrics()](integration-server-sdk5-csharp-actions.md#integration-server-sdk5-csharp-initmetrics) call. Contains either a MetricsManager instance on success or error information on failure.


|  |  | 
| --- |--- |
| Result | The MetricsManager instance for collecting and reporting metrics.<br />**Type:** `MetricsManager`<br />**Required:** No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## DescribePlayerSessionsOutcome
<a name="integration-server-sdk5-csharp-datatypes-describeplayersessionsoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [DescribePlayerSessionsResult](#integration-server-sdk5-csharp-datatypes-describeplayersessionsresult)<br />**Required:** No  | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## DescribePlayerSessionsResult
<a name="integration-server-sdk5-csharp-datatypes-describeplayersessionsresult"></a>


| Properties | Description | 
| --- | --- | 
| NextToken | The token indicating the start of the next page of results. To specify the start of the result set, don't provide a value. If you provide a player session ID, this parameter is ignored.<br />**Type:** `string`<br />**Required:** Yes | 
| PlayerSessions | A collection of objects containing properties for each player session that matches the request. <br />**Type:** `IList<PlayerSession>`<br />**Required:**  | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## PlayerSession
<a name="integration-server-sdk5-csharp-datatypes-playersession"></a>


| Properties | Description | 
| --- | --- | 
| CreationTime | **Type:** `long`<br />**Required:** Yes | 
| FleetId | **Type:** `string`<br />**Required:** Yes | 
| GameSessionId | **Type:** `string`<br />**Required:** Yes | 
| IpAddress | **Type:** `string`<br />**Required:** Yes | 
| PlayerData | **Type:** `string`<br />**Required:** Yes | 
| PlayerId | **Type:** `string`<br />**Required:** Yes | 
| PlayerSessionId | **Type:** `string`<br />**Required:** Yes | 
| Port | **Type:** `int`<br />**Required:** Yes | 
| Status | **Type:** A `PlayerSessionStatus` [enum](#integration-server-sdk5-csharp-datatypes-enums).<br />**Required:** Yes | 
| TerminationTime | **Type:** `long`<br />**Required:** Yes | 
| DnsName | **Type:** `string`<br />**Required:** Yes | 

## StartMatchBackfillOutcome
<a name="integration-server-sdk5-csharp-datatypes-startmatchbackfilloutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [StartMatchBackfillResult](#integration-server-sdk5-csharp-datatypes-startmatchbackfillresult)<br />**Required:** No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## StartMatchBackfillResult
<a name="integration-server-sdk5-csharp-datatypes-startmatchbackfillresult"></a>


| Properties | Description | 
| --- | --- | 
| TicketId | **Type:** `string`<br />**Required:** Yes | 

## GetComputeCertificateOutcome
<a name="integration-server-sdk5-csharp-datatypes-getcomputecertificateoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [GetComputeCertificateResult](#integration-server-sdk5-csharp-datatypes-getcomputecertificateresult)<br />**Required:** No  | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## GetComputeCertificateResult
<a name="integration-server-sdk5-csharp-datatypes-getcomputecertificateresult"></a>

The path to the TLS certificate on your compute and the compute's host name.


| Properties | Description | 
| --- | --- | 
| CertificatePath | **Type:** `string`<br />**Required:** Yes | 
| ComputeName | **Type:** `string`<br />**Required:** Yes | 

## GetFleetRoleCredentialsOutcome
<a name="integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [GetFleetRoleCredentialsResult](#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsresult)<br />**Required:** No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## GetFleetRoleCredentialsResult
<a name="integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsresult"></a>


| Properties | Description | 
| --- | --- | 
| AccessKeyId | The access key ID to authenticate and provide access to your AWS resources.<br />**Type:** `string`<br />**Required:** No | 
| AssumedRoleId | The ID of the user that the service role belongs to.<br />**Type:** `string`<br />**Required:** No | 
| AssumedRoleUserArn | The Amazon Resource Name (ARN) of the user that the service role belongs to.<br />**Type:** `string`<br />**Required:** No | 
| Expiration | The amount of time until your session credentials expire.<br />**Type:** `DateTime`<br />**Required:** No | 
| SecretAccessKey | The secret access key ID for authentication.<br />**Type:** `string`<br />**Required:** No | 
| SessionToken | A token to identify the current active session interacting with your AWS resources.<br />**Type:** `string`<br />**Required:** No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## ListContainersNetworkInfoOutcome
<a name="integration-server-sdk5-csharp-datatypes-listcontainersnetworkinfooutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [ListContainersNetworkInfoResult](#integration-server-sdk5-csharp-datatypes-listcontainersnetworkinforesult)<br />**Required:** No  | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## ListContainersNetworkInfoResult
<a name="integration-server-sdk5-csharp-datatypes-listcontainersnetworkinforesult"></a>

Network information for all containers running on the same instance as the calling game server process.


| Properties | Description | 
| --- | --- | 
| ContainersNetworkInfo | The list of network information for each container running on the instance.<br />**Type:** A list of [ContainerNetworkInfo](#integration-server-sdk5-csharp-datatypes-containernetworkinfo) objects<br />**Required:** No | 

## ContainerNetworkInfo
<a name="integration-server-sdk5-csharp-datatypes-containernetworkinfo"></a>

Network information for a single container running on the instance.


| Properties | Description | 
| --- | --- | 
| ContainerName | The name of the container, as defined in the container group definition.<br />**Type:** `string`<br />**Required:** No | 
| ContainerId | The unique identifier of the container.<br />**Type:** `string`<br />**Required:** No | 
| IpAddress | The container's local IPv4 address on the Docker bridge network.<br />**Type:** `string`<br />**Required:** No | 
| ContainerGroupType | The type of container group that the container belongs to.<br />**Type:** A `ContainerGroupType` [enum](#integration-server-sdk5-csharp-datatypes-enums).<br />**Required:** No | 

## AwsDateTimeOutcome
<a name="integration-server-sdk5-csharp-datatypes-awsdatetimeoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** `DateTime`<br />**Required:** No  | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## GameLiftError
<a name="integration-server-sdk5-csharp-datatypes-gamelifterror"></a>


| Properties | Description | 
| --- | --- | 
| ErrorType | The type of error.<br />**Type:** A `GameLiftErrorType` [enum](#integration-server-sdk5-csharp-datatypes-enums).<br />**Required:** No  | 
| ErrorName | The name of the error.<br /> **Type:** `string` <br />**Required:** No  | 
| ErrorMessage | The error message.<br /> **Type:** `string` <br />**Required:** No  | 

## Enums
<a name="integration-server-sdk5-csharp-datatypes-enums"></a>

Enums defined for the server SDK for Amazon GameLift Servers (C\#) are defined as follows:

**AttrType**  
+ **NONE**
+ **STRING**
+ **DOUBLE**
+ **STRING\_LIST**
+ **STRING\_DOUBLE\_MAP**

**GameLiftErrorType**  
String value indicating the error type. Valid values include:  
+ **SERVICE\_CALL\_FAILED** – A call to an AWS service has failed. 
+ **LOCAL\_CONNECTION\_FAILED** – The local connection to Amazon GameLift Servers failed. 
+ **NETWORK\_NOT\_INITIALIZED** – The network has not been initialized. 
+ **GAMESESSION\_ID\_NOT\_SET** – The game session ID has not been set. 
+ **BAD\_REQUEST\_EXCEPTION** 
+ **INTERNAL\_SERVICE\_EXCEPTION** 
+ **UNSUPPORTED\_COMPUTE\_TYPE\_EXCEPTION** – The API that was called was unsupported on the compute type. 
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

**PlayerSessionCreationPolicy**  
String value indicating whether the game session accepts new players. Valid values include:   
+ **ACCEPT\_ALL** – Accept all new player sessions. 
+ **DENY\_ALL** – Deny all new player sessions. 
+ **NOT\_SET** – The game session is not set to accept or deny new player sessions. 

**PlayerSessionStatus**  
+ **ACTIVE**
+ **COMPLETED**
+ **NOT\_SET**
+ **RESERVED**
+ **TIMEDOUT**

**ContainerGroupType**  
The type of container group that a container belongs to. Valid values include:  
+ `GAME_SERVER` – A game server replica container group. An instance can have multiple game server container groups.
+ `PER_INSTANCE` – A per-instance daemon container group. An instance has exactly one per-instance container group.