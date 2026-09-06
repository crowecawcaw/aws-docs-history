

# C\+\+ (Unreal) server SDK 5.x for Amazon GameLift Servers -- Data types
<a name="integration-server-sdk5-unreal-datatypes"></a>

Use the Amazon GameLift Servers Unreal server SDK 5.x reference to help you prepare your multiplayer game for use with Amazon GameLift Servers. For details about the integration process, see [Add Amazon GameLift Servers to your game server with the server SDK](gamelift-sdk-server-api.md). If you're using the Amazon GameLift Servers plugin for Unreal, see also [Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md).

**Note**  
This topic describes the Amazon GameLift Servers C\+\+ API that you can use when you build for the Unreal Engine. Specifically, this documentation applies to code that you compile with the `-DBUILD_FOR_UNREAL=1` option. 

[C\+\+ (Unreal) server SDK 5.x for Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md)

**Topics**
+ [FProcessParameters](#integration-server-sdk5-unreal-dataypes-process)
+ [UpdateGameSession](#integration-server-sdk5-unreal-dataypes-updategamesession)
+ [GameSession](#integration-server-sdk5-unreal-dataypes-gamesession)
+ [FServerParameters](#integration-server-sdk5-unreal-dataypes-serverparameters)
+ [FStartMatchBackfillRequest](#integration-server-sdk5-unreal-dataypes-startmatchbackfillrequest)
+ [FPlayer](#integration-server-sdk5-unreal-dataypes-player)
+ [FGameLiftDescribePlayerSessionsRequest](#integration-server-sdk5-unreal-dataypes-playersessions)
+ [FStopMatchBackfillRequest](#integration-server-sdk5-unreal-dataypes-stopmatchbackfillrequest)
+ [FAttributeValue](#integration-server-sdk5-unreal-dataypes-attributevalue)
+ [FGameLiftGetFleetRoleCredentialsRequest](#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsrequest)
+ [FGameLiftLongOutcome](#integration-server-sdk5-unreal-dataypes-awslongoutcome)
+ [FGameLiftStringOutcome](#integration-server-sdk5-unreal-dataypes-awsstringoutcome)
+ [FGameLiftDescribePlayerSessionsOutcome](#integration-server-sdk5-unreal-dataypes-describeplayersessionsoutcome)
+ [FGameLiftDescribePlayerSessionsResult](#integration-server-sdk5-unreal-dataypes-describeplayersessionresult)
+ [FGenericOutcome](#integration-server-sdk5-unreal-dataypes-genericoutcome)
+ [FGameLiftPlayerSession](#integration-server-sdk5-unreal-dataypes-playersession)
+ [FGameLiftGetComputeCertificateOutcome](#integration-server-sdk5-unreal-dataypes-getcomputecertificateoutcome)
+ [FGameLiftGetComputeCertificateResult](#integration-server-sdk5-unreal-dataypes-getcomputecertificateresult)
+ [FGameLiftGetFleetRoleCredentialsOutcome](#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsoutcome)
+ [FGetFleetRoleCredentialsResult](#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsresult)
+ [FGameLiftListContainersNetworkInfoOutcome](#integration-server-sdk5-unreal-dataypes-listcontainersnetworkinfooutcome)
+ [FGameLiftListContainersNetworkInfoResult](#integration-server-sdk5-unreal-dataypes-listcontainersnetworkinforesult)
+ [FContainerNetworkInfo](#integration-server-sdk5-unreal-dataypes-containernetworkinfo)
+ [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror)
+ [Enums](#integration-server-sdk5-unreal-dataypes-enums)

## FProcessParameters
<a name="integration-server-sdk5-unreal-dataypes-process"></a>

This data type contains the set of parameters sent to Amazon GameLift Servers in a [ProcessReady()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-processready).


|  |  | 
| --- |--- |
| **Properties** | Description | 
| LogParameters | An object with directory paths to files that are generated during a game session. Amazon GameLift Servers copies and stores the files for future access.**Type:** `TArray<FString>`<br />**Required:** No | 
| OnHealthCheck | The callback function that Amazon GameLift Servers invokes to request a health status report from the server process. Amazon GameLift Servers calls this function every 60 seconds and waits 60 seconds for a response. The server process returns TRUE if healthy, FALSE if not healthy. If no response is returned, Amazon GameLift Servers records the server process as not healthy. This property is a delegate function defined as `DECLARE_DELEGATE_RetVal(bool, FOnHealthCheck)`; <br /> **Type:** `FOnHealthCheck`<br />**Required:** No | 
| OnProcessTerminate | The callback function that Amazon GameLift Servers invokes to force the server process to shut down. After calling this function, Amazon GameLift Servers waits 5 minutes for the server process to shut down and respond with a [ProcessEnding()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-processending) call before it shuts down the server process.**Type:** `FSimpleDelegate`<br />**Required:** Yes | 
| OnStartGameSession | The callback function that Amazon GameLift Servers invokes to activate a new game session. Amazon GameLift Servers calls this function in response to a client request [CreateGameSession](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateGameSession.html). The callback function passes a [GameSession](#integration-server-sdk5-unreal-dataypes-gamesession) object. This property is a delegate function defined as `DECLARE_DELEGATE_OneParam(FOnStartGameSession, Aws::GameLift::Server::Model::GameSession);` <br />**Type:** `FOnStartGameSession`<br />**Required:** Yes | 
| OnUpdateGameSession | The callback function that Amazon GameLift Servers invokes to pass an updated game session object to the server process. Amazon GameLift Servers calls this function when a match backfill request has been processed to provide updated matchmaker data. It passes a [GameSession](#integration-server-sdk5-unreal-dataypes-gamesession) object, a status update (updateReason), and the match backfill ticket ID. This property is a delegate function defined as `DECLARE_DELEGATE_OneParam(FOnUpdateGameSession, Aws::GameLift::Server::Model::UpdateGameSession);`<br />**Type:** `FOnUpdateGameSession`<br />**Required:** No | 
| Port | The port number the server process listens on for new player connections. The value must fall into the port range configured for any fleet deploying this game server build. This port number is included in game session and player session objects, which game sessions use when connecting to a server process.**Type:** `int`<br />**Required:** Yes | 

## UpdateGameSession
<a name="integration-server-sdk5-unreal-dataypes-updategamesession"></a>

This data type updates to a game session object, which includes the reason that the game session was updated and the related backfill ticket ID if backfill is used to fill player sessions in the game session.


| Properties | **Description** | 
| --- | --- | 
| GameSession | A [GameSession](#integration-server-sdk5-unreal-dataypes-gamesession) object. The GameSession object contains properties describing a game session. **Type:** `Aws::GameLift::Server::GameSession`<br />**Required:** No | 
| UpdateReason | The reason that the game session is being updated. **Type:** `enum class UpdateReason` + MATCHMAKING\_DATA\_UPDATED<br />+ BACKFILL\_FAILED<br />+ BACKFILL\_TIMED\_OUT<br />+ BACKFILL\_CANCELLED<br />**Required:** No  | 
| BackfillTicketId | The ID of the backfill ticket attempting to update the game session.**Type:** `char[]`<br />**Required:** No | 

## GameSession
<a name="integration-server-sdk5-unreal-dataypes-gamesession"></a>

This data type provides details of a game session. 


| Properties | **Description** | 
| --- | --- | 
| GameSessionId | A unique identifier for the game session. A game session ARN has the following format: `arn:aws:gamelift:<region>::gamesession/<fleet ID>/<custom ID string or idempotency token>`.<br />**Type:** `char[]`<br />**Required**: No | 
| Name | A descriptive label of the game session. <br />**Type:** `char[]`<br />**Required**: No | 
| FleetId | A unique identifier for the fleet that the game session is running on.<br />**Type:** `char[]`<br />**Required**: No | 
| MaximumPlayerSessionCount | The maximum number of player connections to the game session.<br />**Type:** `int`<br />**Required**: No | 
| Port | The port number for the game session. To connect to an Amazon GameLift Servers game server, an app needs both the IP address and port number.<br />**Type:** `int`<br />**Required**: No | 
| IpAddress | The IP address of the game session. To connect to an Amazon GameLift Servers game server, an app needs both the IP address and port number.<br />**Type:** `char[]`<br />**Required**: No | 
| GameSessionData | A set of custom game session properties, formatted as a single string value. <br />**Type:** `char[]`<br />**Required**: No | 
| MatchmakerData | Information about the matchmaking process that was used to create the game session, in JSON syntax, formatted as a string. In addition to the matchmaking configuration used, it contains data on all players assigned to the match, including player attributes and team assignments.<br />**Type:** `char[]`<br />**Required**: No | 
| GameProperties | A set of custom properties for a game session, formatted as key:value pairs. These properties are passed with a request to start a new game session.<br />**Type:** `GameProperty[]`<br />**Required**: No | 
| DnsName | The DNS identifier assigned to the instance that's running the game session. Values have the following format:+  TLS-enabled fleets: `<unique identifier>.<region identifier>.amazongamelift.com`.  <br />+  Non-TLS-enabled fleets: `ec2-<unique identifier>.compute.amazonaws.com`.  <br />When connecting to a game session that's running on a TLS-enabled fleet, you must use the DNS name, not the IP address.<br />**Type:** `char[]`<br />**Required**: No | 

## FServerParameters
<a name="integration-server-sdk5-unreal-dataypes-serverparameters"></a>

Information used to maintain the connection between an Amazon GameLift Servers Anywhere server and the Amazon GameLift Servers service. This information is used when launching new server processes with [InitSDK()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-initsdk). For servers hosted on Amazon GameLift Servers managed EC2 instances, use an empty object.


| Properties | **Description** | 
| --- | --- | 
| webSocketUrl | The `GameLiftServerSdkEndpoint` Amazon GameLift Servers returns when you [`RegisterCompute`](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html) for a Amazon GameLift Servers Anywhere compute resource.<br />**Type:** `char[]`<br />**Required**: Yes  | 
| processId | A unique identifier registered to the server process hosting your game.<br />**Type:** `char[]`<br />**Required**: Yes | 
| hostId | The HostID is the ComputeName used when you registered your compute. For more information, see [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html).**Type:** `char[]`<br />**Required**: Yes | 
| fleetId | The unique identifier of the fleet that the compute is registered to. For more information, see [RegisterCompute](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterCompute.html).**Type:** `char[]`<br />**Required**: Yes | 
| authToken | The authentication token generated by Amazon GameLift Servers that authenticates your server to Amazon GameLift Servers. For more information, see [GetComputeAuthToken](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetComputeAuthToken.html).**Type:** `char[]`<br />**Required**: Yes | 

## FStartMatchBackfillRequest
<a name="integration-server-sdk5-unreal-dataypes-startmatchbackfillrequest"></a>

Information used to create a matchmaking backfill request. The game server communicates this information to Amazon GameLift Servers in a [StartMatchBackfill()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-startmatchbackfill) call.


| Properties | **Description** | 
| --- | --- | 
| GameSessionArn | A unique game session identifier. The API operation `[GetGameSessionId](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/integration-server-sdk5-unreal-actions.html#integration-server-sdk5-unreal-getgamesessionid)` returns the identifier in ARN format.<br />**Type:** `char[]`<br />**Required**: Yes | 
| MatchmakingConfigurationArn | A unique identifier, in the form of an ARN, for the matchmaker to use for this request. The matchmaker ARN for the original game session is in the game session object in the matchmaker data property. Learn more about matchmaker data in [Work with matchmaker data](https://docs.aws.amazon.com/gameliftservers/latest/flexmatchguide/match-server.html#match-server-data.html).<br />**Type:** `char[]`<br />**Required**: Yes | 
| Players | A set of data representing all players who are in the game session. The matchmaker uses this information to search for new players who are good matches for the current players.<br />**Type:** `TArray<FPlayer>`<br />**Required**: Yes | 
| TicketId | A unique identifier for a matchmaking or match backfill request ticket. If you don't provide a value, Amazon GameLift Servers generates one. Use this identifier to track the match backfill ticket status or cancel the request if needed. <br />**Type:** `char[]`<br />**Required**: No | 

## FPlayer
<a name="integration-server-sdk5-unreal-dataypes-player"></a>

This data type represents a player in matchmaking. When starting a matchmaking request, a player has a player ID, attributes, and possibly latency data. Amazon GameLift Servers adds team information after a match is made.


| Properties | **Description** | 
| --- | --- | 
| LatencyInMS | A set of values expressed in milliseconds that indicate the amount of latency that a player experiences when connected to a location. <br />If this property is used, the player is only matched for locations listed. If a matchmaker has a rule that evaluates player latency, players must report latency to be matched.<br />**Type:** `TMap>FString, int32<`<br />**Required**: No | 
| PlayerAttributes | A collection of key:value pairs containing player information for use in matchmaking. Player attribute keys must match the PlayerAttributes used in a matchmaking rule set.<br />For more information about player attributes, see [AttributeValue](https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_AttributeValue.html).<br />**Type:** `TMap>FString, FAttributeValue<`<br />**Required**: No | 
| PlayerId | A unique identifier for a player.<br />**Type:** `std::string`<br />**Required**: No | 
| Team | The name of the team that the player is assigned to in a match. You define team name in the matchmaking rule set.<br />**Type:** `FString`<br />**Required**: No | 

## FGameLiftDescribePlayerSessionsRequest
<a name="integration-server-sdk5-unreal-dataypes-playersessions"></a>

An object that specifies which player sessions to retrieve. The server process provides this information with a [DescribePlayerSessions()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-describeplayersessions) call to Amazon GameLift Servers.


| Properties | **Description** | 
| --- | --- | 
| GameSessionId | A unique game session identifier. Use this parameter to request all player sessions for the specified game session. <br />Game session ID format is `FString`. The `GameSessionID` is a custom ID string or a<br />**Type:** `std::string`<br />**Required**: No | 
| PlayerSessionId | The unique identifier for a player session. Use this parameter to request a single specific player session.<br />**Type:** `FString`<br />**Required**: No | 
| PlayerId | The unique identifier for a player. Use this parameter to request all player sessions for a specific player. See [Generate player IDs](player-sessions-player-identifiers.md).<br />**Type:** `FString`<br />**Required**: No | 
| PlayerSessionStatusFilter | The player session status to filter results on. Possible player session statuses include:+  RESERVED – The player session request was received, but the player hasn't connected to the server process or been validated. <br />+  ACTIVE – The player was validated by the server process and is connected. <br />+  COMPLETED – The player connection dropped. <br />+  TIMEDOUT – A player session request was received, but the player didn't connect or wasn't validated within the time-out limit (60 seconds). <br />**Type:** `FString`<br />**Required**: No | 
| NextToken | The token indicating the start of the next page of results. To specify the start of the result set, don't provide a value. If you provide a player session ID, this parameter is ignored.<br />**Type:** `FString`<br />**Required**: No | 
| Limit | The maximum number of results to return. If you provide a player session ID, this parameter is ignored.<br />**Type:** `int`<br />**Required**: No | 

## FStopMatchBackfillRequest
<a name="integration-server-sdk5-unreal-dataypes-stopmatchbackfillrequest"></a>

Information used to cancel a matchmaking backfill request. The game server communicates this information to Amazon GameLift Servers service in a [StopMatchBackfill()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-stopmatchbackfill) call.


| Properties | **Description** | 
| --- | --- | 
| GameSessionArn | A unique game session identifier of the request being canceled.<br />**Type:** `FString`<br />**Required**: Yes | 
| MatchmakingConfigurationArn | A unique identifier of the matchmaker this request was sent to.<br />**Type:** `FString`<br />**Required**: Yes | 
| TicketId | A unique identifier of the backfill request ticket to be canceled.<br />**Type:** `FString`<br />**Required**: Yes | 

## FAttributeValue
<a name="integration-server-sdk5-unreal-dataypes-attributevalue"></a>

Use these values in [FPlayer](#integration-server-sdk5-unreal-dataypes-player) attribute key-value pairs. This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map. Each `AttributeValue` object can use only one of the available properties.


| Properties | Description | 
| --- | --- | 
| attrType | Specifies the type of attribute value.<br />**Type:** An `FAttributeType` [enum](#integration-server-sdk5-unreal-dataypes-enums) value. <br />**Required:** No | 
| S | Represents a string attribute value.<br />**Type:** `FString`<br />**Required:** No | 
| N | Represents a numeric attribute value.<br />**Type:** `double`<br />**Required:** No | 
| SL | Represents an array of string attribute values.<br />**Type:** `TArray<FString>`<br />**Required:** No | 
| SDM | Represents a dictionary of string keys and double values.<br />**Type:** `TMap<FString, double>`<br />**Required:** No | 

## FGameLiftGetFleetRoleCredentialsRequest
<a name="integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsrequest"></a>

This data type provides role credentials that extend limited access to your AWS resources to the game server. For more information, see [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md).


| Properties | **Description** | 
| --- | --- | 
| RoleArn | The Amazon Resource Name (ARN) of the service role that extends limited access to your AWS resources.**Type:** `FString`<br />**Required**: No | 
| RoleSessionName | The name of the session describing the use of the role credentials.**Type:** `FString`<br />**Required**: No | 

## FGameLiftLongOutcome
<a name="integration-server-sdk5-unreal-dataypes-awslongoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** `long`<br />**Required:** No | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `long&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror)<br />**Required:** No | 

## FGameLiftStringOutcome
<a name="integration-server-sdk5-unreal-dataypes-awsstringoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** `FString`<br />**Required:** No | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `FString&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror)<br />**Required:** No | 

## FGameLiftDescribePlayerSessionsOutcome
<a name="integration-server-sdk5-unreal-dataypes-describeplayersessionsoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [FGameLiftDescribePlayerSessionsResult](#integration-server-sdk5-unreal-dataypes-describeplayersessionresult)<br />**Required:** No  | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `FGameLiftDescribePlayerSessionsResult&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror)<br />**Required:** No | 

## FGameLiftDescribePlayerSessionsResult
<a name="integration-server-sdk5-unreal-dataypes-describeplayersessionresult"></a>


| Properties | Description | 
| --- | --- | 
| PlayerSessions | <br />**Type:** `TArray<FGameLiftPlayerSession>`<br />**Required:** Yes | 
| NextToken | The token indicating the start of the next page of results. To specify the start of the result set, don't provide a value. If you provide a player session ID, this parameter is ignored.<br />**Type:** `FString`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror)<br />**Required:** No | 

## FGenericOutcome
<a name="integration-server-sdk5-unreal-dataypes-genericoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror)<br />**Required:** No | 

## FGameLiftPlayerSession
<a name="integration-server-sdk5-unreal-dataypes-playersession"></a>


| Properties | Description | 
| --- | --- | 
| CreationTime | **Type:** `long`<br />**Required:** Yes | 
| FleetId | **Type:** `FString`<br />**Required:** Yes | 
| GameSessionId | **Type:** `FString`<br />**Required:** Yes | 
| IpAddress | **Type:** `FString`<br />**Required:** Yes | 
| PlayerData | **Type:** `FString`<br />**Required:** Yes | 
| PlayerId | **Type:** `FString`<br />**Required:** Yes | 
| PlayerSessionId | **Type:** `FString`<br />**Required:** Yes | 
| Port | **Type:** `int`<br />**Required:** Yes | 
| Status | **Type:** A `PlayerSessionStatus` [enum](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-enums).<br />**Required:** Yes | 
| TerminationTime | **Type:** `long`<br />**Required:** Yes | 
| DnsName | **Type:** `FString`<br />**Required:** Yes | 

## FGameLiftGetComputeCertificateOutcome
<a name="integration-server-sdk5-unreal-dataypes-getcomputecertificateoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [FGameLiftGetComputeCertificateResult](#integration-server-sdk5-unreal-dataypes-getcomputecertificateresult)<br />**Required:** No  | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `FGameLiftGetComputeCertificateResult&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror)<br />**Required:** No | 

## FGameLiftGetComputeCertificateResult
<a name="integration-server-sdk5-unreal-dataypes-getcomputecertificateresult"></a>

The path to the TLS certificate on your compute and the compute's host name.


| Properties | Description | 
| --- | --- | 
| CertificatePath | **Type:** `FString`<br />**Required:** Yes | 
| ComputeName | **Type:** `FString`<br />**Required:** Yes | 

## FGameLiftGetFleetRoleCredentialsOutcome
<a name="integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsoutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [FGetFleetRoleCredentialsResult](#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsresult)<br />**Required:** No  | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `FGameLiftGetFleetRoleCredentialsResult&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror)<br />**Required:** No | 

## FGetFleetRoleCredentialsResult
<a name="integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsresult"></a>


| Properties | Description | 
| --- | --- | 
| AccessKeyId | The access key ID to authenticate and provide access to your AWS resources.<br />**Type:** `FString`<br />**Required:** No | 
| AssumedRoleId | The ID of the user that the service role belongs to.<br />**Type:** `FString`<br />**Required:** No | 
| AssumedRoleUserArn | The Amazon Resource Name (ARN) of the user that the service role belongs to.<br />**Type:** `FString`<br />**Required:** No | 
| Expiration | The amount of time until your session credentials expire.<br />**Type:** `FDateTime`<br />**Required:** No | 
| SecretAccessKey | The secret access key ID for authentication.<br />**Type:** `FString`<br />**Required:** No | 
| SessionToken | A token to identify the current active session interacting with your AWS resources.<br />**Type:** `FString`<br />**Required:** No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [GameLiftError](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-gamelifterror)<br />**Required:** No | 

## FGameLiftListContainersNetworkInfoOutcome
<a name="integration-server-sdk5-unreal-dataypes-listcontainersnetworkinfooutcome"></a>

This data type results from an action and produces an object with the following properties:


| Properties | Description | 
| --- | --- | 
| Result | The result of the action.<br />**Type:** [FGameLiftListContainersNetworkInfoResult](#integration-server-sdk5-unreal-dataypes-listcontainersnetworkinforesult)<br />**Required:** No  | 
| ResultWithOwnership |  The result of the action, cast as an rvalue, so that the calling code can take ownership of the object. <br />**Type:** `FGameLiftListContainersNetworkInfoResult&&`<br />**Required**: No | 
| Success | Whether the action was successful or not.<br />**Type:** `bool`<br />**Required**: Yes | 
| Error | The error that occurred if the action was unsuccessful.<br />**Type:** [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror)<br />**Required:** No | 

## FGameLiftListContainersNetworkInfoResult
<a name="integration-server-sdk5-unreal-dataypes-listcontainersnetworkinforesult"></a>

Network information for all containers running on the same instance as the calling game server process.


| Properties | Description | 
| --- | --- | 
| ContainersNetworkInfo | The list of network information for each container running on the instance.<br />**Type:** `TArray<FContainerNetworkInfo>`<br />**Required:** No | 

## FContainerNetworkInfo
<a name="integration-server-sdk5-unreal-dataypes-containernetworkinfo"></a>

Network information for a single container running on the instance.


| Properties | Description | 
| --- | --- | 
| ContainerName | The name of the container, as defined in the container group definition.<br />**Type:** `FString`<br />**Required:** No | 
| ContainerId | The unique identifier of the container.<br />**Type:** `FString`<br />**Required:** No | 
| IpAddress | The container's local IPv4 address on the Docker bridge network.<br />**Type:** `FString`<br />**Required:** No | 
| ContainerGroupType | The type of container group that the container belongs to.<br />**Type:** An `EContainerGroupType` [enum](#integration-server-sdk5-unreal-dataypes-enums).<br />**Required:** No | 

## FGameLiftError
<a name="integration-server-sdk5-unreal-dataypes-gamelifterror"></a>


| Properties | Description | 
| --- | --- | 
| ErrorType | The type of error.<br />**Type:** A `GameLiftErrorType` [enum](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-enums).<br />**Required:** No  | 
| ErrorName | The name of the error.<br /> **Type:** `std::string` <br />**Required:** No  | 
| ErrorMessage | The error message.<br /> **Type:** `std::string` <br />**Required:** No  | 

## Enums
<a name="integration-server-sdk5-unreal-dataypes-enums"></a>

Enums defined for the server SDK for Amazon GameLift Servers (Unreal) are defined as follows:

**FAttributeType**  
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
+ **UNSUPPORTED\_COMPUTE\_TYPE\_EXCEPTION** – The API that was called was unsupported on the compute type. 

**EPlayerSessionCreationPolicy**  
String value indicating whether the game session accepts new players. Valid values include:   
+ **ACCEPT\_ALL** – Accept all new player sessions. 
+ **DENY\_ALL** – Deny all new player sessions. 
+ **NOT\_SET** – The game session is not set to accept or deny new player sessions. 

**EPlayerSessionStatus**  
+ **ACTIVE**
+ **COMPLETED**
+ **NOT\_SET**
+ **RESERVED**
+ **TIMEDOUT**

**EContainerGroupType**  
The type of container group that a container belongs to. Valid values include:  
+ **GAME\_SERVER** – A game server replica container group. An instance can run multiple game server container groups.
+ **PER\_INSTANCE** – A per-instance daemon container group. An instance runs exactly one per-instance container group.