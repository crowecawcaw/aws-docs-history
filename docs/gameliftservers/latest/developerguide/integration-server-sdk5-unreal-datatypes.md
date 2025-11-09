# C++ (Unreal) server SDK 5.x for

Amazon GameLift Servers -- Data types

Use the Amazon GameLift Servers Unreal server SDK 5.x reference to help you prepare your multiplayer
game for use with Amazon GameLift Servers. For details about the integration process, see [Add Amazon GameLift Servers to your game server with the server
SDK](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md"). If you're
using the Amazon GameLift Servers plugin for Unreal, see also [Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md").

###### Note

This topic describes the Amazon GameLift Servers C++ API that you can use when you build for the Unreal Engine.
Specifically, this documentation applies to code that you compile with the `-DBUILD_FOR_UNREAL=1` option.

[C++ (Unreal) server SDK 5.x for
Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md")

###### Data types

- [FProcessParameters](#integration-server-sdk5-unreal-dataypes-process "#integration-server-sdk5-unreal-dataypes-process")
- [UpdateGameSession](#integration-server-sdk5-unreal-dataypes-updategamesession "#integration-server-sdk5-unreal-dataypes-updategamesession")
- [GameSession](#integration-server-sdk5-unreal-dataypes-gamesession "#integration-server-sdk5-unreal-dataypes-gamesession")
- [FServerParameters](#integration-server-sdk5-unreal-dataypes-serverparameters "#integration-server-sdk5-unreal-dataypes-serverparameters")
- [FStartMatchBackfillRequest](#integration-server-sdk5-unreal-dataypes-startmatchbackfillrequest "#integration-server-sdk5-unreal-dataypes-startmatchbackfillrequest")
- [FPlayer](#integration-server-sdk5-unreal-dataypes-player "#integration-server-sdk5-unreal-dataypes-player")
- [FGameLiftDescribePlayerSessionsRequest](#integration-server-sdk5-unreal-dataypes-playersessions "#integration-server-sdk5-unreal-dataypes-playersessions")
- [FStopMatchBackfillRequest](#integration-server-sdk5-unreal-dataypes-stopmatchbackfillrequest "#integration-server-sdk5-unreal-dataypes-stopmatchbackfillrequest")
- [FAttributeValue](#integration-server-sdk5-unreal-dataypes-attributevalue "#integration-server-sdk5-unreal-dataypes-attributevalue")
- [FGameLiftGetFleetRoleCredentialsRequest](#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsrequest "#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsrequest")
- [FGameLiftLongOutcome](#integration-server-sdk5-unreal-dataypes-awslongoutcome "#integration-server-sdk5-unreal-dataypes-awslongoutcome")
- [FGameLiftStringOutcome](#integration-server-sdk5-unreal-dataypes-awsstringoutcome "#integration-server-sdk5-unreal-dataypes-awsstringoutcome")
- [FGameLiftDescribePlayerSessionsOutcome](#integration-server-sdk5-unreal-dataypes-describeplayersessionsoutcome "#integration-server-sdk5-unreal-dataypes-describeplayersessionsoutcome")
- [FGameLiftDescribePlayerSessionsResult](#integration-server-sdk5-unreal-dataypes-describeplayersessionresult "#integration-server-sdk5-unreal-dataypes-describeplayersessionresult")
- [FGenericOutcome](#integration-server-sdk5-unreal-dataypes-genericoutcome "#integration-server-sdk5-unreal-dataypes-genericoutcome")
- [FGameLiftPlayerSession](#integration-server-sdk5-unreal-dataypes-playersession "#integration-server-sdk5-unreal-dataypes-playersession")
- [FGameLiftGetComputeCertificateOutcome](#integration-server-sdk5-unreal-dataypes-getcomputecertificateoutcome "#integration-server-sdk5-unreal-dataypes-getcomputecertificateoutcome")
- [FGameLiftGetComputeCertificateResult](#integration-server-sdk5-unreal-dataypes-getcomputecertificateresult "#integration-server-sdk5-unreal-dataypes-getcomputecertificateresult")
- [FGameLiftGetFleetRoleCredentialsOutcome](#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsoutcome "#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsoutcome")
- [FGetFleetRoleCredentialsResult](#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsresult "#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsresult")
- [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror "#integration-server-sdk5-unreal-dataypes-gamelifterror")
- [Enums](#integration-server-sdk5-unreal-dataypes-enums "#integration-server-sdk5-unreal-dataypes-enums")

## FProcessParameters

This data type contains the set of parameters sent to Amazon GameLift Servers in a [ProcessReady()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-processready "integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-processready").

|                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Properties**      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| LogParameters       | An object with directory paths to files that are generated during a game<br>session. Amazon GameLift Servers copies and stores the files for future<br>access.**Type:**<br>`TArray<FString>`**Required:**<br>No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| OnHealthCheck       | The callback function that Amazon GameLift Servers invokes to request a health status<br>report from the server process. Amazon GameLift Servers calls this function every 60<br>seconds and waits 60 seconds for a response. The server process returns<br>`TRUE` if healthy, `FALSE` if not healthy. If<br>no response is returned, Amazon GameLift Servers records the server process as not<br>healthy.<br>This property is a delegate function defined as `DECLARE_DELEGATE_RetVal(bool, FOnHealthCheck)`;<br>**Type:**<br>`FOnHealthCheck`\*_Required:_<br>• No                                                                                                                                          |
| OnProcessTerminate  | The callback function that Amazon GameLift Servers invokes to force the server process to<br>shut down. After calling this function, Amazon GameLift Servers waits 5 minutes for the<br>server process to shut down and respond with a [ProcessEnding()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-processending "integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-processending") call<br>before it shuts down the server process.**Type:**<br>`FSimpleDelegate`\*_Required:_<br>• Yes                                                                                                                                                                 |
| OnStartGameSession  | The callback function that Amazon GameLift Servers invokes to activate a new game session.<br>Amazon GameLift Servers calls this function in response to a client request [CreateGameSession](../apireference/API_CreateGameSession.md "../apireference/API_CreateGameSession.md"). The callback function passes a [GameSession](#integration-server-sdk5-unreal-dataypes-gamesession "#integration-server-sdk5-unreal-dataypes-gamesession") object.<br>This property is a delegate function defined as `DECLARE_DELEGATE_OneParam(FOnStartGameSession, Aws::GameLift::Server::Model::GameSession);`<br>**Type:**<br>`FOnStartGameSession`\*_Required:_<br>• Yes                                              |
| OnUpdateGameSession | The callback function that Amazon GameLift Servers invokes to pass an updated game session<br>object to the server process. Amazon GameLift Servers calls this function when a match<br>backfill request has been processed to provide updated matchmaker data.<br>It passes a [GameSession](#integration-server-sdk5-unreal-dataypes-gamesession "#integration-server-sdk5-unreal-dataypes-gamesession") object, a status update<br>(`updateReason`), and the match backfill ticket<br>ID.<br>This property is a delegate function defined as `DECLARE_DELEGATE_OneParam(FOnUpdateGameSession, Aws::GameLift::Server::Model::UpdateGameSession);`<br>**Type:**<br>`FOnUpdateGameSession`\*_Required:_<br>• No |
| Port                | The port number the server process listens on for new player<br>connections. The value must fall into the port range configured for any<br>fleet deploying this game server build. This port number is included in<br>game session and player session objects, which game sessions use when<br>connecting to a server process.**Type:**<br>`int`\*_Required:_<br>• Yes                                                                                                                                                                                                                                                                                                                                         |

## UpdateGameSession

This data type updates to a game session object, which includes the reason that the
game session was updated and the related backfill ticket ID if backfill is used to fill
player sessions in the game session.

| Properties       | **Description**                                                                                                                                                                                                                                                                           |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSession      | A [GameSession](#integration-server-sdk5-unreal-dataypes-gamesession "#integration-server-sdk5-unreal-dataypes-gamesession") object. The<br>`GameSession` object contains properties describing a<br>game session. **Type:**<br>`Aws::GameLift::Server::GameSession`\*_Required:_<br>• No |
| UpdateReason     | The reason that the game session is being updated.<br>**Type:\*<br>• `enum class UpdateReason`<br>• MATCHMAKING_DATA_UPDATED<br>• BACKFILL_FAILED<br>• BACKFILL_TIMED_OUT<br>• BACKFILL_CANCELLED<br>**Required:\*<br>• No                                                                |
| BackfillTicketId | The ID of the backfill ticket attempting to update the game<br>session.**Type:**<br>`char[]`\*_Required:_<br>• No                                                                                                                                                                         |

## GameSession

This data type provides details of a game session.

| Properties                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSessionId             | A unique identifier for the game session. A game session ARN has<br>the following format:<br>`arn:aws:gamelift:<region>::gamesession/<fleet<br>ID>/<custom ID string or idempotency token>`.<br>**Type:**<br>`char[]`<br>**Required**: No                                                                                                                                                                                                                                  |
| Name                      | A descriptive label of the game session.<br>**Type:**<br>`char[]`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                      |
| FleetId                   | A unique identifier for the fleet that the game session is running<br>on.<br>**Type:**<br>`char[]`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                     |
| MaximumPlayerSessionCount | The maximum number of player connections to the game<br>session.<br>**Type:**<br>`int`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                 |
| Port                      | The port number for the game session. To connect to a Amazon GameLift Servers game<br>server, an app needs both the IP address and port number.<br>**Type:**<br>`int`<br>**Required**: No                                                                                                                                                                                                                                                                                  |
| IpAddress                 | The IP address of the game session. To connect to a Amazon GameLift Servers game<br>server, an app needs both the IP address and port number.<br>**Type:**<br>`char[]`<br>**Required**: No                                                                                                                                                                                                                                                                                 |
| GameSessionData           | A set of custom game session properties, formatted as a single<br>string value.<br>**Type:**<br>`char[]`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                               |
| MatchmakerData            | Information about the matchmaking process that was used to create<br>the game session, in JSON syntax, formatted as a string. In addition<br>to the matchmaking configuration used, it contains data on all<br>players assigned to the match, including player attributes and team<br>assignments.<br>**Type:**<br>`char[]`<br>**Required**: No                                                                                                                            |
| GameProperties            | A set of custom properties for a game session, formatted as<br>key:value pairs. These properties are passed with a request to start<br>a new game session.<br>**Type:**<br>`GameProperty[]`<br>**Required**: No                                                                                                                                                                                                                                                            |
| DnsName                   | The DNS identifier assigned to the instance that's running the<br>game session. Values have the following format:<br>• TLS-enabled fleets: `<unique<br>identifier>.<region<br>identifier>.amazongamelift.com`.<br>• Non-TLS-enabled fleets: `ec2-<unique<br>identifier>.compute.amazonaws.com`.<br>When connecting to a game session that's running on a TLS-enabled<br>fleet, you must use the DNS name, not the IP address.<br>**Type:**<br>`char[]`<br>**Required**: No |

## FServerParameters

Information used to maintain the connection between an Amazon GameLift Servers Anywhere server and the
Amazon GameLift Servers service. This information is used when launching new server processes with [InitSDK()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-initsdk "integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-initsdk"). For servers hosted on
Amazon GameLift Servers managed EC2 instances, use an empty object.

| Properties   | **Description**                                                                                                                                                                                                                                                                                             |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| webSocketUrl | The `GameLiftServerSdkEndpoint` Amazon GameLift Servers returns when you<br>[`RegisterCompute`](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md") for a Amazon GameLift Servers Anywhere<br>compute resource.<br>**Type:**<br>`char[]`<br>**Required**: Yes                  |
| processId    | A unique identifier registered to the server process hosting your<br>game.<br>**Type:**<br>`char[]`<br>**Required**: Yes                                                                                                                                                                                    |
| hostId       | The `HostID` is the `ComputeName` used when you<br>registered your compute. For more information see, [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md").**Type:**<br>`char[]`**Required**: Yes                                                             |
| fleetId      | The unique identifier of the fleet that the compute is registered to.<br>For more information see, [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md").**Type:**<br>`char[]`**Required**: Yes                                                                |
| authToken    | The authentication token generated by Amazon GameLift Servers that authenticates your<br>server to Amazon GameLift Servers. For more information see, [GetComputeAuthToken](../apireference/API_GetComputeAuthToken.md "../apireference/API_GetComputeAuthToken.md").**Type:**<br>`char[]`**Required**: Yes |

## FStartMatchBackfillRequest

Information used to create a matchmaking backfill request. The game server
communicates this information to Amazon GameLift Servers in a [StartMatchBackfill()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-startmatchbackfill "integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-startmatchbackfill") call.

| Properties                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSessionArn              | A unique game session identifier. The API operation `GetGameSessionId` returns<br>the identifier in ARN format.<br>**Type:**<br>`char[]`<br>**Required**: Yes                                                                                                                                                                                                                                                                                        |
| MatchmakingConfigurationArn | A unique identifier, in the form of an ARN, for the matchmaker to<br>use for this request. The matchmaker ARN for the original game<br>session is in the game session object in the matchmaker data<br>property. Learn more about matchmaker data in [Work with matchmaker data](../flexmatchguide/match-server.md#match-server-data.html "../flexmatchguide/match-server.md#match-server-data.html").<br>**Type:**<br>`char[]`<br>**Required**: Yes |
| Players                     | A set of data representing all players who are in the game<br>session. The matchmaker uses this information to search for new<br>players who are good matches for the current players.<br>**Type:**<br>`TArray<FPlayer>`<br>**Required**: Yes                                                                                                                                                                                                        |
| TicketId                    | A unique identifier for a matchmaking or match backfill request<br>ticket. If you don't provide a value, Amazon GameLift Servers generates one. Use this<br>identifier to track the match backfill ticket status or cancel the<br>request if needed.<br>**Type:**<br>`char[]`<br>**Required**: No                                                                                                                                                    |

## FPlayer

This data type represents a player in matchmaking. When starting a matchmaking
request, a player has a player ID, attributes, and possibly latency data. Amazon GameLift Servers adds
team information after a match is made.

| Properties       | **Description**                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| LatencyInMS      | A set of values expressed in milliseconds that indicate the amount<br>of latency that a player experiences when connected to a location.<br>If this property is used, the player is only matched for locations<br>listed. If a matchmaker has a rule that evaluates player latency,<br>players must report latency to be matched.<br>**Type:**<br>`TMap>FString, int32<`<br>**Required**: No                 |
| PlayerAttributes | A collection of key:value pairs containing player information for<br>use in matchmaking. Player attribute keys must match the<br>PlayerAttributes used in a matchmaking rule set.<br>For more information about player attributes, see [AttributeValue](../apireference/API_AttributeValue.md "../apireference/API_AttributeValue.md").<br>**Type:**<br>`TMap>FString, FAttributeValue<`<br>**Required**: No |
| PlayerId         | A unique identifier for a player.<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                                                          |
| Team             | The name of the team that the player is assigned to in a match.<br>You define team name in the matchmaking rule set.<br>**Type:**<br>`FString`<br>**Required**: No                                                                                                                                                                                                                                           |

## FGameLiftDescribePlayerSessionsRequest

An object that specifies which player sessions to retrieve. The server process
provides this information with a [DescribePlayerSessions()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-describeplayersessions "integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-describeplayersessions") call to
Amazon GameLift Servers.

| Properties                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GameSessionId             | A unique game session identifier. Use this parameter to request<br>all player sessions for the specified game session.<br>Game session ID format is<br>`FString`. The `GameSessionID`<br>is a custom ID string or a<br>**Type:**<br>`std::string`<br>**Required**: No                                                                                                                                                                                                                                                                                                       |
| PlayerSessionId           | The unique identifier for a player session. Use this parameter to<br>request a single specific player session.<br>**Type:**<br>`FString`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                                                |
| PlayerId                  | The unique identifier for a player. Use this parameter to request<br>all player sessions for a specific player. See [Generate player IDs](player-sessions-player-identifiers.md "player-sessions-player-identifiers.md").<br>**Type:**<br>`FString`<br>**Required**: No                                                                                                                                                                                                                                                                                                     |
| PlayerSessionStatusFilter | The player session status to filter results on. Possible player<br>session statuses include:<br>• RESERVED – The player session request was received,<br>but the player hasn't connected to the server process or<br>been validated.<br>• ACTIVE – The player was validated by the server<br>process and is connected.<br>• COMPLETED – The player connection dropped.<br>• TIMEDOUT – A player session request was received,<br>but the player didn't connect or wasn't validated within the<br>time-out limit (60 seconds).<br>**Type:**<br>`FString`<br>**Required**: No |
| NextToken                 | The token indicating the start of the next page of results. To<br>specify the start of the result set, don't provide a value. If you<br>provide a player session ID, this parameter is ignored.<br>**Type:**<br>`FString`<br>**Required**: No                                                                                                                                                                                                                                                                                                                               |
| Limit                     | The maximum number of results to return. If you provide a player<br>session ID, this parameter is ignored.<br>**Type:**<br>`int`<br>**Required**: No                                                                                                                                                                                                                                                                                                                                                                                                                        |

## FStopMatchBackfillRequest

Information used to cancel a matchmaking backfill request. The game server
communicates this information to Amazon GameLift Servers service in a [StopMatchBackfill()](integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-stopmatchbackfill "integration-server-sdk5-unreal-actions.md#integration-server-sdk5-unreal-stopmatchbackfill") call.

| Properties                  | **Description**                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| GameSessionArn              | A unique game session identifier of the request being<br>canceled.<br>**Type:**<br>`FString`<br>**Required**: Yes    |
| MatchmakingConfigurationArn | A unique identifier of the matchmaker this request was sent<br>to.<br>**Type:**<br>`FString`<br>**Required**: Yes    |
| TicketId                    | A unique identifier of the backfill request ticket to be<br>canceled.<br>**Type:**<br>`FString`<br>**Required**: Yes |

## FAttributeValue

Use these values in [FPlayer](#integration-server-sdk5-unreal-dataypes-player "#integration-server-sdk5-unreal-dataypes-player") attribute key-value pairs.
This object lets you specify an attribute value using any of the valid data types: string, number, string array, or data map.
Each `AttributeValue` object can use only one of the available properties.

| Properties | Description                                                                                                                                                                                                          |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| attrType   | Specifies the type of attribute value.<br>**Type:\*<br>• An `FAttributeType` [enum](#integration-server-sdk5-unreal-dataypes-enums "#integration-server-sdk5-unreal-dataypes-enums") value.<br>**Required:\*<br>• No |
| S          | Represents a string attribute value.<br>**Type:\*<br>• `FString`<br>**Required:\*<br>• No                                                                                                                            |
| N          | Represents a numeric attribute value.<br>**Type:\*<br>• `double`<br>**Required:\*<br>• No                                                                                                                            |
| SL         | Represents an array of string attribute values.<br>**Type:\*<br>• `TArray<FString>`<br>**Required:\*<br>• No                                                                                                         |
| SDM        | Represents a dictionary of string keys and double values.<br>**Type:\*<br>• `TMap<FString, double>`<br>**Required:\*<br>• No                                                                                         |

## FGameLiftGetFleetRoleCredentialsRequest

This data type provides role credentials that extend limited access to your AWS
resources to the game server. For more information see, [Set up an IAM service role for Amazon GameLift Servers](setting-up-role.md "setting-up-role.md").

| Properties      | **Description**                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| RoleArn         | The Amazon Resource Name (ARN) of the service role that extends<br>limited access to your AWS resources.**Type:**<br>`FString`**Required**: No |
| RoleSessionName | The name of the session describing the use of the role<br>credentials.**Type:**<br>`FString`**Required**: No                                   |

## FGameLiftLongOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Result              | The result of the action.<br>**Type:\*<br>• `long`<br>**Required:\*<br>• No                                                                                                                                                          |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `long&&`<br>**Required\*\*: No                                                                             |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                            |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror "#integration-server-sdk5-unreal-dataypes-gamelifterror")<br>**Required:\*<br>• No |

## FGameLiftStringOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Result              | The result of the action.<br>**Type:\*<br>• `FString`<br>**Required:\*<br>• No                                                                                                                                                       |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `FString&&`<br>**Required\*\*: No                                                                          |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                            |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror "#integration-server-sdk5-unreal-dataypes-gamelifterror")<br>**Required:\*<br>• No |

## FGameLiftDescribePlayerSessionsOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result              | The result of the action.<br>**Type:\*<br>• [FGameLiftDescribePlayerSessionsResult](#integration-server-sdk5-unreal-dataypes-describeplayersessionresult "#integration-server-sdk5-unreal-dataypes-describeplayersessionresult")<br>**Required:\*<br>• No |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `FGameLiftDescribePlayerSessionsResult&&`<br>**Required\*\*: No                                                                 |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                                 |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror "#integration-server-sdk5-unreal-dataypes-gamelifterror")<br>**Required:\*<br>• No                      |

## FGameLiftDescribePlayerSessionsResult

| Properties     | Description                                                                                                                                                                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PlayerSessions | **Type:\*<br>• `TArray<FGameLiftPlayerSession>`<br>**Required:\*<br>• Yes                                                                                                                                                                     |
| NextToken      | The token indicating the start of the next page of results. To<br>specify the start of the result set, don't provide a value. If you<br>provide a player session ID, this parameter is ignored.<br>**Type:**<br>`FString`<br>**Required**: No |
| Success        | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                     |
| Error          | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror "#integration-server-sdk5-unreal-dataypes-gamelifterror")<br>**Required:\*<br>• No          |

## FGenericOutcome

This data type results from an action and produces an object with the following properties:

| Properties | Description                                                                                                                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Success    | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                            |
| Error      | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror "#integration-server-sdk5-unreal-dataypes-gamelifterror")<br>**Required:\*<br>• No |

## FGameLiftPlayerSession

| Properties      | Description                                                                                                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CreationTime    | **Type:\*<br>• `long`<br>**Required:\*<br>• Yes                                                                                                                                                                                                     |
| FleetId         | **Type:\*<br>• `FString`<br>**Required:\*<br>• Yes                                                                                                                                                                                                  |
| GameSessionId   | **Type:\*<br>• `FString`<br>**Required:\*<br>• Yes                                                                                                                                                                                                  |
| IpAddress       | **Type:\*<br>• `FString`<br>**Required:\*<br>• Yes                                                                                                                                                                                                  |
| PlayerData      | **Type:\*<br>• `FString`<br>**Required:\*<br>• Yes                                                                                                                                                                                                  |
| PlayerId        | **Type:\*<br>• `FString`<br>**Required:\*<br>• Yes                                                                                                                                                                                                  |
| PlayerSessionId | **Type:\*<br>• `FString`<br>**Required:\*<br>• Yes                                                                                                                                                                                                  |
| Port            | **Type:\*<br>• `int`<br>**Required:\*<br>• Yes                                                                                                                                                                                                      |
| Status          | **Type:\*<br>• A `PlayerSessionStatus` [enum](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-enums "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-enums").<br>**Required:\*<br>• Yes |
| TerminationTime | **Type:\*<br>• `long`<br>**Required:\*<br>• Yes                                                                                                                                                                                                     |
| DnsName         | **Type:\*<br>• `FString`<br>**Required:\*<br>• Yes                                                                                                                                                                                                  |

## FGameLiftGetComputeCertificateOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Result              | The result of the action.<br>**Type:\*<br>• [FGameLiftGetComputeCertificateResult](#integration-server-sdk5-unreal-dataypes-getcomputecertificateresult "#integration-server-sdk5-unreal-dataypes-getcomputecertificateresult")<br>**Required:\*<br>• No |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `FGameLiftGetComputeCertificateResult&&`<br>**Required\*\*: No                                                                 |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                                |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror "#integration-server-sdk5-unreal-dataypes-gamelifterror")<br>**Required:\*<br>• No                     |

## FGameLiftGetComputeCertificateResult

The path to the TLS certificate on your compute and the compute's host name.

| Properties      | Description                                        |
| --------------- | -------------------------------------------------- |
| CertificatePath | **Type:\*<br>• `FString`<br>**Required:\*<br>• Yes |
| ComputeName     | **Type:\*<br>• `FString`<br>**Required:\*<br>• Yes |

## FGameLiftGetFleetRoleCredentialsOutcome

This data type results from an action and produces an object with the following properties:

| Properties          | Description                                                                                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Result              | The result of the action.<br>**Type:\*<br>• [FGetFleetRoleCredentialsResult](#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsresult "#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsresult")<br>**Required:\*<br>• No |
| ResultWithOwnership | The result of the action, cast as an rvalue, so that the calling code can take ownership of the object.<br>**Type:\*<br>• `FGameLiftGetFleetRoleCredentialsResult&&`<br>**Required\*\*: No                                                             |
| Success             | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                              |
| Error               | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [FGameLiftError](#integration-server-sdk5-unreal-dataypes-gamelifterror "#integration-server-sdk5-unreal-dataypes-gamelifterror")<br>**Required:\*<br>• No                   |

## FGetFleetRoleCredentialsResult

| Properties         | Description                                                                                                                                                                                                                                                                                                                 |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AccessKeyId        | The access key ID to authenticate and provide access to your<br>AWS resources.<br>**Type:\*<br>• `FString`<br>**Required:\*<br>• No                                                                                                                                                                                         |
| AssumedRoleId      | The ID of the user that the service role belongs to.<br>**Type:\*<br>• `FString`<br>**Required:\*<br>• No                                                                                                                                                                                                                   |
| AssumedRoleUserArn | The Amazon Resource Name (ARN) of the user that the<br>service role belongs to.<br>**Type:\*<br>• `FString`<br>**Required:\*<br>• No                                                                                                                                                                                        |
| Expiration         | The amount of time until your session credentials<br>expire.<br>**Type:\*<br>• `FDateTime`<br>**Required:\*<br>• No                                                                                                                                                                                                         |
| SecretAccessKey    | The secret access key ID for authentication.<br>**Type:\*<br>• `FString`<br>**Required:\*<br>• No                                                                                                                                                                                                                           |
| SessionToken       | A token to identify the current active session interacting<br>with your AWS resources.<br>**Type:\*<br>• `FString`<br>**Required:\*<br>• No                                                                                                                                                                                 |
| Success            | Whether the action was successful or not.<br>**Type:\*<br>• `bool`<br>**Required\*\*: Yes                                                                                                                                                                                                                                   |
| Error              | The error that occurred if the action was unsuccessful.<br>**Type:\*<br>• [GameLiftError](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-gamelifterror "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-gamelifterror")<br>**Required:\*<br>• No |

## FGameLiftError

| Properties   | Description                                                                                                                                                                                                                                                            |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ErrorType    | The type of error.<br>**Type:\*<br>• A `GameLiftErrorType` [enum](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-enums "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-enums").<br>**Required:\*<br>• No |
| ErrorName    | The name of the error.<br>**Type:**<br>`std::string`<br>\*_Required:_<br>• No                                                                                                                                                                                          |
| ErrorMessage | The error message.<br>**Type:\*<br>• `std::string`<br>**Required:\*<br>• No                                                                                                                                                                                            |

## Enums

Enums defined for the server SDK for Amazon GameLift Servers (Unreal) are defined as follows:

**FAttributeType**

- **NONE**
- **STRING**
- **DOUBLE**
- **STRING_LIST**
- **STRING_DOUBLE_MAP**

**GameLiftErrorType**

String value indicating the error type. Valid values include:

- **SERVICE_CALL_FAILED** – A call to an AWS service has failed.
- **LOCAL_CONNECTION_FAILED** – The local connection to Amazon GameLift Servers failed.
- **NETWORK_NOT_INITIALIZED** – The network has not been initialized.
- **GAMESESSION_ID_NOT_SET** – The game session ID has not been set.
- **BAD_REQUEST_EXCEPTION**
- **INTERNAL_SERVICE_EXCEPTION**
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

**EPlayerSessionCreationPolicy**

String value indicating whether the game session accepts new players.
Valid values include:

- **ACCEPT_ALL** – Accept all new player sessions.
- **DENY_ALL** – Deny all new player sessions.
- **NOT_SET** – The game session is not set to accept or deny new player sessions.

**EPlayerSessionStatus**

- **ACTIVE**
- **COMPLETED**
- **NOT_SET**
- **RESERVED**
- **TIMEDOUT**
