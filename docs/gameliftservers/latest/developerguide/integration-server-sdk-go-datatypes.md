

# Go server SDK for Amazon GameLift Servers -- Data types
<a name="integration-server-sdk-go-datatypes"></a>

Use the server SDK reference to integrate your multiplayer game for hosting with Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server with the server SDK](gamelift-sdk-server-api.md).

`GameLiftServerAPI.go` defines the Go server SDK actions.

[Go server SDK for Amazon GameLift Servers -- Actions](integration-server-sdk-go-actions.md)

**Topics**
+ [LogParameters](#integration-server-sdk-go-dataypes-log)
+ [MetricsParameters](#integration-server-sdk-go-dataypes-metrics)
+ [ProcessParameters](#integration-server-sdk-go-dataypes-process)
+ [UpdateGameSession](#integration-server-sdk-go-dataypes-updategamesession)
+ [GameSession](#integration-server-sdk-go-dataypes-gamesession)
+ [ServerParameters](#integration-server-sdk-go-dataypes-serverparameters)
+ [StartMatchBackfillRequest](#integration-server-sdk-go-dataypes-startmatchbackfillrequest)
+ [Player](#integration-server-sdk-go-dataypes-player)
+ [DescribePlayerSessionsRequest](#integration-server-sdk-go-dataypes-playersessions)
+ [StopMatchBackfillRequest](#integration-server-sdk-go-dataypes-stopmatchbackfillrequest)
+ [GetFleetRoleCredentialsRequest](#integration-server-sdk-go-dataypes-getfleetrolecredentialsrequest)

## LogParameters
<a name="integration-server-sdk-go-dataypes-log"></a>

An object identifying files generated during a game session that you want Amazon GameLift Servers to upload and store after the game session ends. The game server provides `LogParameters` to Amazon GameLift Servers as part of a `ProcessParameters` object in a [ProcessReady()](integration-server-sdk-go-actions.md#integration-server-sdk-go-processready) call.


|  |  | 
| --- |--- |
| **Properties** | Description | 
| LogPaths | The list of directory paths to game server log files that you want Amazon GameLift Servers to store for future access. The server process generates these files during each game session. You define file paths and names in your game server and store them in the root game build directory. <br />The log paths must be absolute. For example, if your game build stores game session logs in a path such as `MyGame\sessionLogs\`, then the path would be `c:\game\MyGame\sessionLogs` on a Windows instance.<br />**Type:** `[]string`<br />**Required:** No | 

## MetricsParameters
<a name="integration-server-sdk-go-dataypes-metrics"></a>

An object communicating configuration parameters for initializing the metrics system. This configuration is used to set up StatsD reporting, crash reporting, and metrics processing behavior. The game server provides `MetricsParameters` to Amazon GameLift Servers as part of a [InitMetrics()](integration-server-sdk-go-actions.md#integration-server-sdk-go-initmetrics) call.


|  |  | 
| --- |--- |
| **Properties** | Description | 
| StatsdHost | The StatsD server host for metrics reporting (e.g., "localhost").<br />**Type:** `string`<br />**Required:** Yes | 
| StatsdPort | The StatsD server port for metrics reporting (e.g., 8125).<br />**Type:** `int`<br />**Required:** Yes | 
| CrashReporterHost | The crash reporter host for crash tracking and process monitoring.<br />**Type:** `string`<br />**Required:** Yes | 
| CrashReporterPort | The crash reporter port for crash tracking and process monitoring.<br />**Type:** `int`<br />**Required:** Yes | 
| FlushIntervalMs | The metrics flush interval in milliseconds. Controls how frequently metrics are sent to StatsD.<br />**Type:** `int`<br />**Required:** Yes | 
| MaxPacketSize | The maximum packet size for metrics in bytes. Limits the size of UDP packets sent to StatsD.<br />**Type:** `int`<br />**Required:** Yes | 

## ProcessParameters
<a name="integration-server-sdk-go-dataypes-process"></a>

An object describing the communication between a server process and Amazon GameLift Servers. The server process provides this information to Amazon GameLift Servers with a call to [ProcessReady()](integration-server-sdk-go-actions.md#integration-server-sdk-go-processready).


|  |  | 
| --- |--- |
| **Properties** | Description | 
| LogParameters | An object with directory paths to files that are generated during a game session. Amazon GameLift Servers copies and stores the files for future access.**Type:** `LogParameters`<br />**Required:** No | 
| OnHealthCheck | The callback function that Amazon GameLift Servers invokes to request a health status report from the server process. Amazon GameLift Servers calls this function every 60 seconds and waits 60 seconds for a response. The server process returns TRUE if healthy, FALSE if not healthy. If no response is returned, Amazon GameLift Servers records the server process as not healthy.**Type:** `OnHealthCheck func() bool`<br />**Required:** No | 
| OnProcessTerminate | The callback function that Amazon GameLift Servers invokes to force the server process to shut down. After calling this function, Amazon GameLift Servers waits 5 minutes for the server process to shut down and respond with a [ProcessEnding()](integration-server-sdk-go-actions.md#integration-server-sdk-go-processending) call before it shuts down the server process.**Type:** `OnProcessTerminate func()`<br />**Required:** Yes | 
| OnStartGameSession | The callback function that Amazon GameLift Servers invokes to pass an updated game session object to the server process. Amazon GameLift Servers calls this function when a match backfill request has been processed to provide updated matchmaker data. It passes a [GameSession](#integration-server-sdk-go-dataypes-gamesession) object, a status update (updateReason), and the match backfill ticket ID.**Type:** `OnStartGameSession func (model.GameSession )`<br />**Required:** Yes | 
| OnUpdateGameSession | The callback function that Amazon GameLift Servers invokes to pass updated game session information to the server process. Amazon GameLift Servers calls this function after processing a match backfill request to provide updated matchmaker data. **Type:** `OnUpdateGameSession func (model.UpdateGameSession)`<br />**Required:** No | 
| Port | The port number that the server process listens on for new player connections. The value must fall into the port range configured for any fleet deploying this game server build. This port number is included in game session and player session objects, which game sessions use when connecting to a server process.**Type:** `int`<br />**Required:** Yes | 

## UpdateGameSession
<a name="integration-server-sdk-go-dataypes-updategamesession"></a>

The updates to a game session object, which includes the reason that the game session was updated, and the related backfill ticket ID if backfill is being used to fill player sessions in the game session.


| Properties | **Description** | 
| --- | --- | 
| GameSession | A [GameSession](#integration-server-sdk-go-dataypes-gamesession) object. The GameSession object contains properties describing a game session. **Type:** `GameSession GameSession()`<br />**Required:** Yes | 
| UpdateReason | The reason that the game session is being updated.**Type:** `UpdateReason UpdateReason()`<br />**Required:** Yes | 
| BackfillTicketId | The ID of the backfill ticket attempting to update the game session.**Type:** `String`<br />**Required:** No | 

## GameSession
<a name="integration-server-sdk-go-dataypes-gamesession"></a>

The details of a game session. 


| Properties | **Description** | 
| --- | --- | 
| GameSessionId | A unique identifier for the game session. A game session Amazon Resource Name (ARN) has the following format: `arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`.<br />**Type:** `String`<br />**Required**: No | 
| Name | A descriptive label of the game session. <br />**Type:** `String`<br />**Required**: No | 
| FleetId | A unique identifier for the fleet that the game session is running on.<br />**Type:** `String`<br />**Required**: No | 
| MaximumPlayerSessionCount | The maximum number of player connections to the game session.<br />**Type:** `Integer`<br />**Required**: No | 
| Port | The port number for the game session. To connect to an Amazon GameLift Servers game server, an app needs both the IP address and port number.<br />**Type:** `Integer`<br />**Required**: No | 
| IpAddress | The IP address of the game session. To connect to an Amazon GameLift Servers game server, an app needs both the IP address and port number.<br />**Type:** `String`<br />**Required**: No | 
| GameSessionData | A set of custom game session properties, formatted as a single string value. <br />**Type:** `String`<br />**Required**: No | 
| MatchmakerData | The information about the matchmaking process that was used to create the game session, in JSON syntax, formatted as a string. In addition to the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments.<br />**Type:** `String`<br />**Required**: No | 
| GameProperties | A set of custom properties for a game session, formatted as key:value pairs. These properties are passed with a request to start a new game session.<br />**Type:** `map[string] string`<br />**Required**: No | 
| DnsName | The DNS identifier assigned to the instance that's running the game session. Values have the following format:+  TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com`.  <br />+  Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com`.  <br />When connecting to a game session that's running on a TLS-enabled fleet, you must use the DNS name, not the IP address.<br />**Type:** `String`<br />**Required**: No | 

## ServerParameters
<a name="integration-server-sdk-go-dataypes-serverparameters"></a>

Information used to maintain the connection between an Amazon GameLift Servers Anywhere server and the Amazon GameLift Servers service. This information is used when launching new server processes with [InitSDK()](integration-server-sdk-go-actions.md#integration-server-sdk-go-initsdk). For servers hosted on Amazon GameLift Servers managed EC2 instances, use an empty object.


| Properties | **Description** | 
| --- | --- | 
| WebSocketURL | The `GameLiftServerSdkEndpoint` Amazon GameLift Servers returns when you [`RegisterCompute`](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html) for an Amazon GameLift Servers Anywhere compute resource.<br />**Type:** `string`<br />**Required**: Yes | 
| ProcessID | A unique identifier registered to the server process hosting your game.<br />**Type:** `string`<br />**Required**: Yes | 
| HostID | The unique identifier of the compute resource that's hosting the new server process. <br />The `HostID` is the `ComputeName` used when you registered your compute. For more information, see [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html).<br />**Type:** `string`<br />**Required**: Yes | 
| FleetID | The unique identifier of the fleet that the compute is registered to. For more information, see [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html).**Type:** `string`<br />**Required**: Yes | 
| AuthToken | The authentication token generated by Amazon GameLift Servers that authenticates your server to Amazon GameLift Servers. For more information, see [GetComputeAuthToken](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetComputeAuthToken.html).**Type:** `string`<br />**Required**: Yes | 

## StartMatchBackfillRequest
<a name="integration-server-sdk-go-dataypes-startmatchbackfillrequest"></a>

Information used to create a matchmaking backfill request. The game server communicates this information to Amazon GameLift Servers in a [StartMatchBackfill()](integration-server-sdk-go-actions.md#integration-server-sdk-go-startmatchbackfill) call.


| Properties | **Description** | 
| --- | --- | 
| GameSessionArn | The unique game session identifier. The API operation `[GetGameSessionId](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk-go-actions.html#integration-server-sdk-go-getgamesessionid)` returns the identifier in ARN format.<br />**Type:** `String`<br />**Required**: Yes | 
| MatchmakingConfigurationArn | The unique identifier (in the form of an ARN) for the matchmaker to use for this request. The matchmaker ARN for the original game session is in the game session object in the matchmaker data property. For more information about matchmaker data, see [Work with matchmaker data](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-server.html#match-server-data.html).<br />**Type:** `String`<br />**Required**: Yes | 
| Players | A set of data that represents all players who are currently in the game session. The matchmaker uses this information to search for new players who are good matches for the current players.<br />**Type:** `[]model.Player`<br />**Required**: Yes | 
| TicketId | The unique identifier for a matchmaking or match backfill request ticket. If you don't provide a value, Amazon GameLift Servers generates one. Use this identifier to track the match backfill ticket status or cancel the request if needed. <br />**Type:** `String`<br />**Required**: No | 

## Player
<a name="integration-server-sdk-go-dataypes-player"></a>

The object that represents a player in matchmaking. When a matchmaking request starts, a player has a player ID, attributes, and possibly latency data. Amazon GameLift Servers adds team information after a match is made.


| Properties | **Description** | 
| --- | --- | 
| LatencyInMS | A set of values expressed in milliseconds that indicate the amount of latency that a player experiences when connected to a location. <br />If this property is used, the player is only matched for locations listed. If a matchmaker has a rule that evaluates player latency, players must report latency to be matched.<br />**Type:** `map[string] int`<br />**Required**: No | 
| PlayerAttributes | A collection of key:value pairs that contain player information for use in matchmaking. Player attribute keys must match the PlayerAttributes used in a matchmaking rule set.<br />For more information about player attributes, see [AttributeValue](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_AttributeValue.html).<br />**Type:** `map[string] AttributeValue`<br />**Required**: No | 
| PlayerId | A unique identifier for a player.<br />**Type:** `String`<br />**Required**: No | 
| Team | The name of the team that the player is assigned to in a match. You define the team name in the matchmaking rule set.<br />**Type:** `String`<br />**Required**: No | 

## DescribePlayerSessionsRequest
<a name="integration-server-sdk-go-dataypes-playersessions"></a>

An object that specifies which player sessions to retrieve. The server process provides this information with a [DescribePlayerSessions()](integration-server-sdk-go-actions.md#integration-server-sdk-go-describeplayersessions) call to Amazon GameLift Servers.


| Properties | **Description** | 
| --- | --- | 
| GameSessionID | A unique game session identifier. Use this parameter to request all player sessions for the specified game session. <br />Game session ID format is `arn:aws:gamelift:<region>::gamesession/fleet-<fleet ID>/<ID string>`. The `GameSessionID` is a custom ID string or a generated string. <br />**Type:** `String`<br />**Required**: No | 
| PlayerSessionID | The unique identifier for a player session. Use this parameter to request a single specific player session.<br />**Type:** `String`<br />**Required**: No | 
| PlayerID | The unique identifier for a player. Use this parameter to request all player sessions for a specific player. See [Generate player IDs](player-sessions-player-identifiers.md).<br />**Type:** `String`<br />**Required**: No | 
| PlayerSessionStatusFilter | The player session status to filter results on. Possible player session statuses include:+  RESERVED – The player session request was received, but the player hasn't connected to the server process or been validated. <br />+  ACTIVE – The player was validated by the server process and is connected. <br />+  COMPLETED – The player connection dropped. <br />+  TIMEDOUT – A player session request was received, but the player didn't connect or wasn't validated within the time-out limit (60 seconds). <br />**Type:** `String`<br />**Required**: No | 
| NextToken | The token indicating the start of the next page of results. To specify the start of the result set, don't provide a value. If you provide a player session ID, this parameter is ignored.<br />**Type:** `String`<br />**Required**: No | 
| Limit | The maximum number of results to return. If you provide a player session ID, this parameter is ignored.<br />**Type:** `int`<br />**Required**: No | 

## StopMatchBackfillRequest
<a name="integration-server-sdk-go-dataypes-stopmatchbackfillrequest"></a>

Information used to cancel a matchmaking backfill request. The game server communicates this information to Amazon GameLift Servers service in a [StopMatchBackfill()](integration-server-sdk-go-actions.md#integration-server-sdk-go-stopmatchbackfill) call.


| Properties | **Description** | 
| --- | --- | 
| GameSessionArn | The unique game session identifier of the request being canceled.<br />**Type:** `string`<br />**Required**: No | 
| MatchmakingConfigurationArn | The unique identifier of the matchmaker this request was sent to.<br />**Type:** `string`<br />**Required**: No | 
| TicketId | The unique identifier of the backfill request ticket to be canceled.<br />**Type:** `string`<br />**Required**: No | 

## GetFleetRoleCredentialsRequest
<a name="integration-server-sdk-go-dataypes-getfleetrolecredentialsrequest"></a>

The role credentials that extend limited access to your AWS resources to the game server. For more information, see [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md).


| Properties | **Description** | 
| --- | --- | 
| RoleArn | The ARN of the service role that extends limited access to your AWS resources.**Type:** `string`<br />**Required**: Yes | 
| RoleSessionName | The name of the session that describes the use of the role credentials.**Type:** `string`<br />**Required:** Yes | 