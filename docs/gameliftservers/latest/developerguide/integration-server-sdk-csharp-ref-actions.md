# C# server SDK for Amazon GameLift Servers 4.x --

Actions

Use the server SDK reference to integrate your multiplayer game for hosting with Amazon GameLift Servers.
For guidance about the integration process, see [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md").

###### Note

This reference is for an earlier version of the server SDK for Amazon GameLift Servers. For the latest
version, see
[C# server SDK 5.x for Amazon GameLift Servers --
Actions](integration-server-sdk5-csharp-actions.md "integration-server-sdk5-csharp-actions.md").

[C# server SDK for Amazon GameLift Servers 4.x --
Data types](integration-server-sdk-csharp-ref-datatypes.md "integration-server-sdk-csharp-ref-datatypes.md")

###### Topics

- [AcceptPlayerSession()](#integration-server-sdk-csharp-ref-acceptplayersession "#integration-server-sdk-csharp-ref-acceptplayersession")
- [ActivateGameSession()](#integration-server-sdk-csharp-ref-activategamesession "#integration-server-sdk-csharp-ref-activategamesession")
- [DescribePlayerSessions()](#integration-server-sdk-csharp-ref-describeplayersessions "#integration-server-sdk-csharp-ref-describeplayersessions")
- [GetGameSessionId()](#integration-server-sdk-csharp-ref-getgamesessionid "#integration-server-sdk-csharp-ref-getgamesessionid")
- [GetInstanceCertificate()](#integration-server-sdk-csharp-ref-getinstancecertificate "#integration-server-sdk-csharp-ref-getinstancecertificate")
- [GetSdkVersion()](#integration-server-sdk-csharp-ref-getsdk "#integration-server-sdk-csharp-ref-getsdk")
- [GetTerminationTime()](#integration-server-sdk-csharp-ref-getterm "#integration-server-sdk-csharp-ref-getterm")
- [InitSDK()](#integration-server-sdk-csharp-ref-initsdk "#integration-server-sdk-csharp-ref-initsdk")
- [ProcessEnding()](#integration-server-sdk-csharp-ref-processending "#integration-server-sdk-csharp-ref-processending")
- [ProcessReady()](#integration-server-sdk-csharp-ref-processready "#integration-server-sdk-csharp-ref-processready")
- [RemovePlayerSession()](#integration-server-sdk-csharp-ref-removeplayersession "#integration-server-sdk-csharp-ref-removeplayersession")
- [StartMatchBackfill()](#integration-server-sdk-csharp-ref-startmatchbackfill "#integration-server-sdk-csharp-ref-startmatchbackfill")
- [StopMatchBackfill()](#integration-server-sdk-csharp-ref-stopmatchbackfill "#integration-server-sdk-csharp-ref-stopmatchbackfill")
- [TerminateGameSession()](#integration-server-sdk-csharp-ref-terminategamesession "#integration-server-sdk-csharp-ref-terminategamesession")
- [UpdatePlayerSessionCreationPolicy()](#integration-server-sdk-csharp-ref-updateplayersessioncreationpolicy "#integration-server-sdk-csharp-ref-updateplayersessioncreationpolicy")

## AcceptPlayerSession()

Notifies the Amazon GameLift Servers service that a player with the specified player session ID has
connected to the server process and needs validation. Amazon GameLift Servers verifies that the player
session ID is valid—that is, that the player ID has reserved a player slot in the
game session. Once validated, Amazon GameLift Servers changes the status of the player slot from RESERVED
to ACTIVE.

### Syntax

```
GenericOutcome AcceptPlayerSession(String playerSessionId)
```

### Parameters

**playerSessionId**
Unique ID issued by Amazon GameLift Servers when a new player session is created.
A player session ID is specified in a `PlayerSession` object, which is returned in
response to a client call to the _GameLift API_ actions [StartGameSessionPlacement](../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md "../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md"), [CreateGameSession](../../../gamelift/latest/apireference/API_CreateGameSession.md "../../../gamelift/latest/apireference/API_CreateGameSession.md"), [DescribeGameSessionPlacement](../../../gamelift/latest/apireference/API_DescribeGameSessionPlacement.md "../../../gamelift/latest/apireference/API_DescribeGameSessionPlacement.md"), or [DescribePlayerSessions](../../../gamelift/latest/apireference/API_DescribePlayerSessions.md "../../../gamelift/latest/apireference/API_DescribePlayerSessions.md").

Type: String

Required: Yes

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example illustrates a function for handling a connection request, including
validating and rejecting invalid player session IDs.

```
void ReceiveConnectingPlayerSessionID (Connection connection, String playerSessionId){
    var acceptPlayerSessionOutcome =  GameLiftServerAPI.AcceptPlayerSession(playerSessionId);
     if(acceptPlayerSessionOutcome.Success)
    {
        connectionToSessionMap.emplace(connection, playerSessionId);
        connection.Accept();
    }
     else
    {
        connection.Reject(acceptPlayerSessionOutcome.Error.ErrorMessage);    }
}
```

## ActivateGameSession()

Notifies the Amazon GameLift Servers service that the server process has activated a game session and is
now ready to receive player connections. This action should be called as part of the
`onStartGameSession()` callback function, after all game session
initialization has been completed.

### Syntax

```
GenericOutcome ActivateGameSession()
```

### Parameters

This action has no parameters.

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example shows `ActivateGameSession()` being called as part of the
`onStartGameSession()` delegate function.

```
void OnStartGameSession(GameSession gameSession)
{
    // game-specific tasks when starting a new game session, such as loading map

    // When ready to receive players
    var activateGameSessionOutcome = GameLiftServerAPI.ActivateGameSession();
}
```

## DescribePlayerSessions()

Retrieves player session data, including settings, session metadata, and player data.
Use this action to get information for a single player session, for all player sessions
in a game session, or for all player sessions associated with a single player ID.

### Syntax

```
DescribePlayerSessionsOutcome DescribePlayerSessions(DescribePlayerSessionsRequest describePlayerSessionsRequest)
```

### Parameters

**describePlayerSessionsRequest**

A [DescribePlayerSessionsRequest](integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-playersessions "integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-playersessions") object describing which player sessions to retrieve.

Required: Yes

### Return value

If successful, returns a `DescribePlayerSessionsOutcome` object
containing a set of player session objects that fit the request parameters. Player
session objects have a structure identical to the AWS SDK Amazon GameLift Servers API [PlayerSession](../../../gamelift/latest/apireference/API_PlayerSession.md "../../../gamelift/latest/apireference/API_PlayerSession.md") data type.

### Example

This example illustrates a request for all player sessions actively connected to a
specified game session. By omitting _NextToken_ and
setting the _Limit_ value to 10, Amazon GameLift Servers will return
the first 10 player sessions records matching the request.

```
// Set request parameters
var describePlayerSessionsRequest = new Aws.GameLift.Server.Model.DescribePlayerSessionsRequest()
{
    GameSessionId = GameLiftServerAPI.GetGameSessionId().Result,    //gets the ID for the current game session
    Limit = 10,
    PlayerSessionStatusFilter = PlayerSessionStatusMapper.GetNameForPlayerSessionStatus(PlayerSessionStatus.ACTIVE)
};
// Call DescribePlayerSessions
Aws::GameLift::DescribePlayerSessionsOutcome playerSessionsOutcome =
    Aws::GameLift::Server::Model::DescribePlayerSessions(describePlayerSessionRequest);
```

## GetGameSessionId()

Retrieves the ID of the game session currently being hosted by the server process, if
the server process is active.

For idle process that are not yet activated with a game session, the call returns
`Success`=`True` and
`GameSessionId`=`""` (an empty string).

### Syntax

```
AwsStringOutcome GetGameSessionId()
```

### Parameters

This action has no parameters.

### Return

value

If successful, returns the game session ID as an `AwsStringOutcome` object.
If not successful, returns an error message.

### Example

```
var getGameSessionIdOutcome = GameLiftServerAPI.GetGameSessionId();
```

## GetInstanceCertificate()

Retrieves the file location of a pem-encoded TLS certificate that is associated with
the fleet and its instances. AWS Certificate Manager generates this certificate when you create a new
fleet with the certificate configuration set to GENERATED. Use this certificate to
establish a secure connection with a game client and to encrypt client/server
communication.

### Syntax

```
GetInstanceCertificateOutcome GetInstanceCertificate();
```

### Parameters

This action has no parameters.

### Return value

If successful, returns a `GetInstanceCertificateOutcome` object
containing the location of the fleet's TLS certificate file and certificate chain,
which are stored on the instance. A root certificate file, extracted from the
certificate chain, is also stored on the instance. If not successful, returns an
error message.

For more information about the certificate and certificate chain data, see [GetCertificate Response Elements](../../../acm/latest/APIReference/API_GetCertificate.md#API_GetCertificate_ResponseElements "../../../acm/latest/APIReference/API_GetCertificate.md#API_GetCertificate_ResponseElements") in the AWS Certificate Manager API Reference.

### Example

```
var getInstanceCertificateOutcome = GameLiftServerAPI.GetInstanceCertificate();
```

## GetSdkVersion()

Returns the current version number of the SDK built into the server process.

### Syntax

```
AwsStringOutcome GetSdkVersion()
```

### Parameters

This action has no parameters.

### Return

value

If successful, returns the current SDK version as an `AwsStringOutcome`
object. The returned string includes the version number only (ex. "3.1.5"). If not
successful, returns an error message.

### Example

```
var getSdkVersionOutcome = GameLiftServerAPI.GetSdkVersion();
```

## GetTerminationTime()

Returns the time that a server process is scheduled to be shut down, if a termination
time is available. A server process takes this action after receiving an
`onProcessTerminate()` callback from the Amazon GameLift Servers service. Amazon GameLift Servers may call
`onProcessTerminate()` for the following reasons: (1) for poor health
(the server process has reported port health or has not responded to Amazon GameLift Servers, (2) when
terminating the instance during a scale-down event, or (3) when an instance is being
terminated due to a [spot-instance interruption](spot-tasks.md "spot-tasks.md").

If the process has received an `onProcessTerminate()` callback, the value
returned is the estimated termination time. If the process has not received an
`onProcessTerminate()` callback, an error message is returned. Learn more
about [shutting down a server
process](gamelift-sdk-server-api.md#gamelift-sdk-server-terminate "gamelift-sdk-server-api.md#gamelift-sdk-server-terminate").

### Syntax

```
AwsDateTimeOutcome GetTerminationTime()
```

### Parameters

This action has no parameters.

### Return

value

If successful, returns the termination time as an `AwsDateTimeOutcome`
object. The value is the termination time, expressed in elapsed ticks since 0001
00:00:00. For example, the date time value 2020-09-13 12:26:40 -000Z is equal to
637355968000000000 ticks. If no termination time is available, returns an error
message.

### Example

```
var getTerminationTimeOutcome = GameLiftServerAPI.GetTerminationTime();
```

## InitSDK()

Initializes the Amazon GameLift Servers SDK. This method should be called on launch, before any other
Amazon GameLift Servers-related initialization occurs.

### Syntax

```
InitSDKOutcome InitSDK()
```

### Parameters

This action has no parameters.

### Return

value

If successful, returns an InitSdkOutcome object indicating that the server process
is ready to call [ProcessReady()](#integration-server-sdk-csharp-ref-processready "#integration-server-sdk-csharp-ref-processready").

### Example

```
var initSDKOutcome = GameLiftServerAPI.InitSDK();
```

## ProcessEnding()

Notifies the Amazon GameLift Servers service that the server process is shutting down. This method
should be called after all other cleanup tasks, including shutting down all active game
sessions. This method should exit with an exit code of 0; a non-zero exit code results
in an event message that the process did not exit cleanly.

Once the method exits with a code of 0, you can terminate the process with a
successful exit code. You can also exit the process with an error code. If you exit with
an error code, the fleet event will indicated the process terminated abnormally
(`SERVER_PROCESS_TERMINATED_UNHEALTHY`).

### Syntax

```
GenericOutcome ProcessEnding()
```

### Parameters

This action has no parameters.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
var processEndingOutcome = GameLiftServerAPI.ProcessEnding();
if (processReadyOutcome.Success)
   Environment.Exit(0);
// otherwise, exit with error code
Environment.Exit(errorCode);

```

## ProcessReady()

Notifies the Amazon GameLift Servers service that the server process is ready to host game sessions.
Call this method after successfully invoking [InitSDK()](#integration-server-sdk-csharp-ref-initsdk "#integration-server-sdk-csharp-ref-initsdk") and completing setup
tasks that are required before the server process can host a game session. This method
should be called only once per process.

### Syntax

```
GenericOutcome ProcessReady(ProcessParameters processParameters)
```

### Parameters

**processParameters**

A [ProcessParameters](integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-process "integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-process")
object communicating the following information about the server
process:

- Names of callback methods, implemented in the game server
  code, that the Amazon GameLift Servers service invokes to communicate with the
  server process.
- Port number that the server process is listening on.
- Path to any game session-specific files that you want Amazon GameLift Servers to
  capture and store.

Required: Yes

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example illustrates both the [ProcessReady()](#integration-server-sdk-csharp-ref-processready "#integration-server-sdk-csharp-ref-processready") call and
delegate function implementations.

```
// Set parameters and call ProcessReady
var processParams = new ProcessParameters(
   this.OnGameSession,
   this.OnProcessTerminate,
   this.OnHealthCheck,
   this.OnGameSessionUpdate,
   port,
   new LogParameters(new List<string>()          // Examples of log and error files written by the game server
   {
      "C:\\game\\logs",
      "C:\\game\\error"
   })
);

var processReadyOutcome = GameLiftServerAPI.ProcessReady(processParams);

// Implement callback functions
void OnGameSession(GameSession gameSession)
{
   // game-specific tasks when starting a new game session, such as loading map
   // When ready to receive players
   var activateGameSessionOutcome = GameLiftServerAPI.ActivateGameSession();
}

void OnProcessTerminate()
{
   // game-specific tasks required to gracefully shut down a game session,
   // such as notifying players, preserving game state data, and other cleanup
    var ProcessEndingOutcome = GameLiftServerAPI.ProcessEnding();
}

bool OnHealthCheck()
{
    bool isHealthy;
    // complete health evaluation within 60 seconds and set health
    return isHealthy;
}
```

## RemovePlayerSession()

Notifies the Amazon GameLift Servers service that a player with the specified player session ID has
disconnected from the server process. In response, Amazon GameLift Servers changes the player slot to
available, which allows it to be assigned to a new player.

### Syntax

```
GenericOutcome RemovePlayerSession(String playerSessionId)
```

### Parameters

**playerSessionId**
Unique ID issued by Amazon GameLift Servers when a new player session is created.
A player session ID is specified in a `PlayerSession` object, which is returned in
response to a client call to the _GameLift API_ actions [StartGameSessionPlacement](../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md "../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md"), [CreateGameSession](../../../gamelift/latest/apireference/API_CreateGameSession.md "../../../gamelift/latest/apireference/API_CreateGameSession.md"), [DescribeGameSessionPlacement](../../../gamelift/latest/apireference/API_DescribeGameSessionPlacement.md "../../../gamelift/latest/apireference/API_DescribeGameSessionPlacement.md"), or [DescribePlayerSessions](../../../gamelift/latest/apireference/API_DescribePlayerSessions.md "../../../gamelift/latest/apireference/API_DescribePlayerSessions.md").

Type: String

Required: Yes

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
Aws::GameLift::GenericOutcome disconnectOutcome =
    Aws::GameLift::Server::RemovePlayerSession(playerSessionId);
```

## StartMatchBackfill()

Sends a request to find new players for open slots in a game session created with
FlexMatch. See also the AWS SDK action [StartMatchBackfill()](../../../gamelift/latest/apireference/API_StartMatchBackfill.md "../../../gamelift/latest/apireference/API_StartMatchBackfill.md"). With
this action, match backfill requests can be initiated by a game server process that is
hosting the game session. Learn more about the [FlexMatch backfill feature](../flexmatchguide/match-backfill.md "../flexmatchguide/match-backfill.md").

This action is asynchronous. If new players are successfully matched, the Amazon GameLift Servers
service delivers updated matchmaker data using the callback function
`OnUpdateGameSession()`.

A server process can have only one active match backfill request at a time. To send a
new request, first call [StopMatchBackfill()](#integration-server-sdk-csharp-ref-stopmatchbackfill "#integration-server-sdk-csharp-ref-stopmatchbackfill") to cancel the
original request.

### Syntax

```
StartMatchBackfillOutcome StartMatchBackfill (StartMatchBackfillRequest startBackfillRequest);
```

### Parameters

**StartMatchBackfillRequest**

A [StartMatchBackfillRequest](integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-startmatchbackfillrequest "integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-startmatchbackfillrequest") object that communicates the following information:

- A ticket ID to assign to the backfill request. This
  information is optional; if no ID is provided, Amazon GameLift Servers will
  autogenerate one.
- The matchmaker to send the request to. The full configuration
  ARN is required. This value can be acquired from the game
  session's matchmaker data.
- The ID of the game session that is being backfilled.
- Available matchmaking data for the game session's current
  players.

Required: Yes

### Return

value

Returns a StartMatchBackfillOutcome object with the match backfill ticket ID or
failure with an error message.

### Example

```
// Build a backfill request
var startBackfillRequest = new AWS.GameLift.Server.Model.StartMatchBackfillRequest()
{
    TicketId = "`a ticket ID`", //optional
    MatchmakingConfigurationArn = "`the matchmaker configuration ARN`",
    GameSessionId = GameLiftServerAPI.GetGameSessionId().Result,    // gets ID for current game session
        //get player data for all currently connected players
            MatchmakerData matchmakerData =
              MatchmakerData.FromJson(gameSession.MatchmakerData);  // gets matchmaker data for current players
            // get matchmakerData.Players
            // remove data for players who are no longer connected
    Players = ListOfPlayersRemainingInTheGame
};

// Send backfill request
var startBackfillOutcome = GameLiftServerAPI.StartMatchBackfill(startBackfillRequest);

// Implement callback function for backfill
void OnUpdateGameSession(GameSession myGameSession)
{
   // game-specific tasks to prepare for the newly matched players and update matchmaker data as needed
}
```

## StopMatchBackfill()

Cancels an active match backfill request that was created with [StartMatchBackfill()](#integration-server-sdk-csharp-ref-startmatchbackfill "#integration-server-sdk-csharp-ref-startmatchbackfill"). See also the
AWS SDK action [StopMatchmaking()](../../../gamelift/latest/apireference/API_StopMatchmaking.md "../../../gamelift/latest/apireference/API_StopMatchmaking.md"). Learn more about the [FlexMatch backfill feature](../flexmatchguide/match-backfill.md "../flexmatchguide/match-backfill.md").

### Syntax

```
GenericOutcome StopMatchBackfill (StopMatchBackfillRequest stopBackfillRequest);
```

### Parameters

**StopMatchBackfillRequest**

A [StopMatchBackfillRequest](integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-stopmatchbackfillrequest "integration-server-sdk-csharp-ref-datatypes.md#integration-server-sdk-csharp-ref-dataypes-stopmatchbackfillrequest") object identifying the matchmaking ticket to cancel:

- ticket ID assigned to the backfill request being
  canceled
- matchmaker the backfill request was sent to
- game session associated with the backfill request

Required: Yes

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
// Set backfill stop request parameters

var stopBackfillRequest = new AWS.GameLift.Server.Model.StopMatchBackfillRequest()
{
    TicketId = "`a ticket ID`", //optional, if not provided one is autogenerated
    MatchmakingConfigurationArn = "`the matchmaker configuration ARN`", //from the game session matchmaker data
    GameSessionId = GameLiftServerAPI.GetGameSessionId().Result    //gets the ID for the current game session
};

var stopBackfillOutcome = GameLiftServerAPI.StopMatchBackfillRequest(stopBackfillRequest);
```

## TerminateGameSession()

**This method is deprecated with version 4.0.1. Instead, the
server process should call [ProcessEnding()](#integration-server-sdk-csharp-ref-processending "#integration-server-sdk-csharp-ref-processending") after a game
session has ended.**

Notifies the Amazon GameLift Servers service that the server process has ended the current game session.
This action is called when the server process will remain active and ready to host a new
game session. It should be called only after your game session termination procedure is
complete, because it signals to Amazon GameLift Servers that the server process is immediately available
to host a new game session.

This action is not called if the server process will be shut down after the game
session stops. Instead, call [ProcessEnding()](#integration-server-sdk-csharp-ref-processending "#integration-server-sdk-csharp-ref-processending") to signal that
both the game session and the server process are ending.

### Syntax

```
GenericOutcome TerminateGameSession()
```

### Parameters

This action has no parameters.

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example illustrates a server process at the end of a game session.

```
// game-specific tasks required to gracefully shut down a game session,
// such as notifying players, preserving game state data, and other cleanup

var terminateGameSessionOutcome = GameLiftServerAPI.TerminateGameSession();
var processReadyOutcome = GameLiftServerAPI.ProcessReady(processParams);
```

## UpdatePlayerSessionCreationPolicy()

Updates the current game session's ability to accept new player sessions. A game
session can be set to either accept or deny all new player sessions. (See also the
[UpdateGameSession()](../../../gamelift/latest/apireference/API_UpdateGameSession.md "../../../gamelift/latest/apireference/API_UpdateGameSession.md")
action in the _Amazon GameLift Servers Service API Reference_).

### Syntax

```
GenericOutcome UpdatePlayerSessionCreationPolicy(PlayerSessionCreationPolicy playerSessionPolicy)
```

### Parameters

**newPlayerSessionPolicy**

String value indicating whether the game session accepts new players.

Type: [PlayerSessionCreationPolicy](https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_game_lift_1_1_model.html#afa8a7527defe9e7ca0caebc239182c43 "https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_game_lift_1_1_model.html#afa8a7527defe9e7ca0caebc239182c43") enum. Valid values
include:

- **ACCEPT_ALL** – Accept all
  new player sessions.
- **DENY_ALL** – Deny all new
  player sessions.

Required: Yes

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example sets the current game session's join policy to accept all
players.

```
var updatePlayerSessionCreationPolicyOutcomex =
    GameLiftServerAPI.UpdatePlayerSessionCreationPolicy(PlayerSessionCreationPolicy.ACCEPT_ALL);
```
