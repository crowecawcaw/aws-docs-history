# C# server SDK 5.x for Amazon GameLift Servers --

Actions

Use the server SDK 5.x reference to integrate your multiplayer game for hosting with
Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md"). If you're
using the Amazon GameLift Servers plugin for Unity, see also [Amazon GameLift Servers plugin for Unity (server SDK 5.x)](unity-plug-in.md "unity-plug-in.md").

[C# server SDK 5.x for Amazon GameLift Servers --
Data types](integration-server-sdk5-csharp-datatypes.md "integration-server-sdk5-csharp-datatypes.md")

###### Topics

- [GetSdkVersion()](#integration-server-sdk5-csharp-getsdkversion "#integration-server-sdk5-csharp-getsdkversion")
- [InitSDK()](#integration-server-sdk5-csharp-initsdk "#integration-server-sdk5-csharp-initsdk")
- [InitSDK()](#integration-server-sdk5-csharp-initsdk-anywhere "#integration-server-sdk5-csharp-initsdk-anywhere")
- [ProcessReady()](#integration-server-sdk5-csharp-processready "#integration-server-sdk5-csharp-processready")
- [ProcessEnding()](#integration-server-sdk5-csharp-processending "#integration-server-sdk5-csharp-processending")
- [ActivateGameSession()](#integration-server-sdk5-csharp-activategamesession "#integration-server-sdk5-csharp-activategamesession")
- [UpdatePlayerSessionCreationPolicy()](#integration-server-sdk5-csharp-updateplayersessioncreationpolicy "#integration-server-sdk5-csharp-updateplayersessioncreationpolicy")
- [GetGameSessionId()](#integration-server-sdk5-csharp-getgamesessionid "#integration-server-sdk5-csharp-getgamesessionid")
- [GetTerminationTime()](#integration-server-sdk5-csharp-getterm "#integration-server-sdk5-csharp-getterm")
- [AcceptPlayerSession()](#integration-server-sdk5-csharp-acceptplayersession "#integration-server-sdk5-csharp-acceptplayersession")
- [RemovePlayerSession()](#integration-server-sdk5-csharp-removeplayersession "#integration-server-sdk5-csharp-removeplayersession")
- [DescribePlayerSessions()](#integration-server-sdk5-csharp-describeplayersessions "#integration-server-sdk5-csharp-describeplayersessions")
- [StartMatchBackfill()](#integration-server-sdk5-csharp-startmatchbackfill "#integration-server-sdk5-csharp-startmatchbackfill")
- [StopMatchBackfill()](#integration-server-sdk5-csharp-stopmatchbackfill "#integration-server-sdk5-csharp-stopmatchbackfill")
- [GetComputeCertificate()](#integration-server-sdk5-csharp-getcomputecertificate "#integration-server-sdk5-csharp-getcomputecertificate")
- [GetFleetRoleCredentials()](#integration-server-sdk5-csharp-getfleetrolecredentials "#integration-server-sdk5-csharp-getfleetrolecredentials")
- [Destroy()](#integration-server-sdk5-csharp-destroy "#integration-server-sdk5-csharp-destroy")

## GetSdkVersion()

Returns the current version number of the SDK built into the server process.

### Syntax

```
AwsStringOutcome GetSdkVersion();
```

### Return

value

If successful, returns the current SDK version as an [AwsStringOutcome](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-awsstringoutcome "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-awsstringoutcome") object. The
returned string includes the version number (example `5.0.0`). If not
successful, returns an error message.

### Example

```
var getSdkVersionOutcome = GameLiftServerAPI.GetSdkVersion();
```

## InitSDK()

Initializes the Amazon GameLift Servers SDK for a managed EC2 fleet. Call this method on launch, before
any other initialization related to Amazon GameLift Servers occurs. This method reads server parameters
from the host environment to set up communication between the server and the Amazon GameLift Servers
service. It uses an idempotency token, so you safely retry this call when it
fails.

### Syntax

```
GenericOutcome InitSDK();
```

### Return value

If successful, returns an InitSdkOutcome object to indicate that the server
process is ready to call [ProcessReady()](#integration-server-sdk5-csharp-processready "#integration-server-sdk5-csharp-processready").

### Example

```
//Call InitSDK to establish a local connection with the GameLift agent to enable further communication.
GenericOutcome initSDKOutcome = GameLiftServerAPI.InitSDK();
```

## InitSDK()

Initializes the Amazon GameLift Servers SDK for an Anywhere fleet. Call this method on launch, before
any other initialization related to Amazon GameLift Servers occurs. This method requires explicit server
parameters to set up communication between the server and the Amazon GameLift Servers service. It uses an
idempotency token, so you safely retry this call when it fails.

### Syntax

```
GenericOutcome InitSDK(ServerParameters serverParameters);
```

### Parameters

[ServerParameters](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-serverparameters "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-serverparameters")

To initialize a game server on an Amazon GameLift Servers Anywhere fleet, construct a
`ServerParameters` object with the following
information:

- The URL of the WebSocket used to connect to your game server.
- The ID of the process used to host your game server.
- The ID of the compute hosting your game server processes.
- The ID of the Amazon GameLift Servers fleet containing your Amazon GameLift Servers Anywhere
  compute.
- The authorization token generated by the Amazon GameLift Servers operation.

### Return value

If successful, returns an InitSdkOutcome object to indicate that the server
process is ready to call [ProcessReady()](#integration-server-sdk5-csharp-processready "#integration-server-sdk5-csharp-processready").

###### Note

If calls to `InitSDK()` are failing for game builds deployed to
Anywhere fleets, check the `ServerSdkVersion` parameter used
when creating the build resource.
You must explicitly set this value to the server SDK version in use. The default value for this
parameter is 4.x, which is not compatible. To resolve this issue, create a new build and deploy it to a new fleet.

### Example

```
//Define the server parameters
string websocketUrl = "`wss://us-west-1.api.amazongamelift.com`";
string processId = "`PID1234`";
string fleetId = "`aarn:aws:gamelift:us-west-1:111122223333:fleet/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa`";
string hostId = "`HardwareAnywhere`";
string authToken = "`1111aaaa-22bb-33cc-44dd-5555eeee66ff`";
ServerParameters serverParameters =
  new ServerParameters(webSocketUrl, processId, hostId, fleetId, authToken);

//Call InitSDK to establish a local connection with the GameLift agent to enable further communication.
GenericOutcome initSDKOutcome = GameLiftServerAPI.InitSDK(serverParameters);
```

## ProcessReady()

Notifies Amazon GameLift Servers that the server process is ready to host game sessions. Call this
method after invoking [InitSDK()](#integration-server-sdk5-csharp-initsdk "#integration-server-sdk5-csharp-initsdk"). This method should be
called only once per process.

### Syntax

```
GenericOutcome ProcessReady(ProcessParameters processParameters)
```

### Parameters

**[ProcessParameters](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-process "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-process")**

A `ProcessParameters` object holds information about the
server process.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example illustrates both the method and delegate function
implementations.

```
// Set parameters and call ProcessReady
ProcessParameters processParams = new ProcessParameters(
  this.OnStartGameSession,
  this.OnProcessTerminate,
  this.OnHealthCheck,
  this.OnUpdateGameSession,
  port,
  new LogParameters(new List<string>()
  // Examples of log and error files written by the game server
  {
    "`C:\\game\\logs`",
    "`C:\\game\\error`"
  })
);
GenericOutcome processReadyOutcome = GameLiftServerAPI.ProcessReady(processParams);
```

## ProcessEnding()

Notifies Amazon GameLift Servers that the server process is terminating. Call this method after all
other cleanup tasks (including shutting down the active game session) and before
terminating the process. Depending on the result of `ProcessEnding()`, the
process exits with success (0) or error (-1) and generates a fleet event. If the process
terminates with an error, the fleet event generated is
`SERVER_PROCESS_TERMINATED_UNHEALTHY`.

### Syntax

```
GenericOutcome ProcessEnding()
```

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example calls `ProcessEnding()` and `Destroy()` before
terminating the server process with a success or error exit code.

```
GenericOutcome processEndingOutcome = GameLiftServerAPI.ProcessEnding();
GameLiftServerAPI.Destroy();

if (processEndingOutcome.Success)
  {
    Environment.Exit(0);
  }
else
  {
    Console.WriteLine("ProcessEnding() failed. Error: " + processEndingOutcome.Error.ToString());
    Environment.Exit(-1);
  }
```

## ActivateGameSession()

Notifies Amazon GameLift Servers that the server process has activated a game session and is now ready
to receive player connections. This action should be called as part of the
`onStartGameSession()` callback function, after all game session
initialization.

### Syntax

```
GenericOutcome ActivateGameSession()
```

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example shows `ActivateGameSession()` being called as part of the
`onStartGameSession()` delegate function.

```
void OnStartGameSession(GameSession gameSession)
{
  // game-specific tasks when starting a new game session, such as loading map
  // When ready to receive players
  GenericOutcome activateGameSessionOutcome = GameLiftServerAPI.ActivateGameSession();
}
```

## UpdatePlayerSessionCreationPolicy()

Updates the current game session's ability to accept new player sessions. A game
session can be set to either accept or deny all new player sessions.

### Syntax

```
GenericOutcome UpdatePlayerSessionCreationPolicy(PlayerSessionCreationPolicy playerSessionPolicy)
```

### Parameters

**playerSessionPolicy**

String value that indicates whether the game session accepts new
players.

Valid values include:

- **ACCEPT_ALL** – Accept all
  new player sessions.
- **DENY_ALL** – Deny all new
  player sessions.

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example sets the current game session's join policy to accept all
players.

```
GenericOutcome updatePlayerSessionPolicyOutcome =
  GameLiftServerAPI.UpdatePlayerSessionCreationPolicy(PlayerSessionCreationPolicy.`ACCEPT_ALL`);
```

## GetGameSessionId()

Retrieves the ID of the game session hosted by the active server process.

For idle processes that aren't activated with a game session, the call returns a
[GameLiftError](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-gamelifterror "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-gamelifterror").

### Syntax

```
AwsStringOutcome GetGameSessionId()
```

### Return

value

If successful, returns the game session ID as an [AwsStringOutcome](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-awsstringoutcome "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-awsstringoutcome") object.
If not successful, returns an error message."

### Example

```
AwsStringOutcome getGameSessionIdOutcome = GameLiftServerAPI.GetGameSessionId();
```

## GetTerminationTime()

Returns the time that a server process is scheduled to be shut down, if a termination
time is available. A server process takes this action after receiving an
`onProcessTerminate()` callback from Amazon GameLift Servers. Amazon GameLift Servers calls
`onProcessTerminate()` for the following reasons:

- When the server process has reported poor health or has not responded to
  Amazon GameLift Servers.
- When terminating the instance during a scale-down event.
- When an instance is terminated due to a [spot-instance interruption](spot-tasks.md "spot-tasks.md").

### Syntax

```
AwsDateTimeOutcome GetTerminationTime()
```

### Return value

If successful, returns the termination time as an [AwsDateTimeOutcome](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-awsdatetimeoutcome "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-awsdatetimeoutcome")
object. The value is the termination time, expressed in elapsed ticks since
`0001 00:00:00`. For example, the date time value `2020-09-13
 12:26:40 -000Z` is equal to `637355968000000000` ticks. If no
termination time is available, returns an error message.

### Example

```
AwsDateTimeOutcome getTerminationTimeOutcome = GameLiftServerAPI.GetTerminationTime();
```

## AcceptPlayerSession()

Notifies Amazon GameLift Servers that a player with the specified player session ID has connected to the
server process and needs validation. Amazon GameLift Servers verifies that the player session ID is valid.
After the player session is validated, Amazon GameLift Servers changes the status of the player slot from
RESERVED to ACTIVE.

### Syntax

```
GenericOutcome AcceptPlayerSession(String playerSessionId)
```

### Parameters

playerSessionId

Unique ID issued by GameLift when a new player session is
created.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example illustrates a function for handling a connection request, including
validating and rejecting invalid player session IDs.

```
void ReceiveConnectingPlayerSessionID (Connection connection, String playerSessionId)
{
  GenericOutcome acceptPlayerSessionOutcome = GameLiftServerAPI.AcceptPlayerSession(playerSessionId);
  if(acceptPlayerSessionOutcome.Success)
  {
    connectionToSessionMap.emplace(connection, playerSessionId);
    connection.Accept();
  }
  else
  {
    connection.Reject(acceptPlayerSessionOutcome.Error.ErrorMessage);
  }
}
```

## RemovePlayerSession()

Notifies Amazon GameLift Servers that a player has disconnected from the server process. In response,
Amazon GameLift Servers changes the player slot to available.

### Syntax

```
GenericOutcome RemovePlayerSession(String playerSessionId)
```

### Parameters

**playerSessionId**

Unique ID issued by Amazon GameLift Servers when a new player session is created.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
GenericOutcome removePlayerSessionOutcome = GameLiftServerAPI.RemovePlayerSession(playerSessionId);
```

## DescribePlayerSessions()

Retrieves player session data which includes settings, session metadata, and player
data. Use this action to get information for a single player session, for all player
sessions in a game session, or for all player sessions associated with a single player
ID.

### Syntax

```
DescribePlayerSessionsOutcome DescribePlayerSessions(DescribePlayerSessionsRequest describePlayerSessionsRequest)
```

### Parameters

**[DescribePlayerSessionsRequest](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-playersessions "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-playersessions")**

A [DescribePlayerSessionsRequest](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-playersessions "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-playersessions") object that describes which
player sessions to retrieve.

### Return value

If successful, returns a [DescribePlayerSessionsOutcome](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-describeplayersessionsoutcome "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-describeplayersessionsoutcome") object that
contains a set of player session objects that fit the request parameters.

### Example

This example illustrates a request for all player sessions actively connected to a
specified game session. By omitting _NextToken_ and
setting the _Limit_ value to 10, Amazon GameLift Servers will return
the first 10 player session records matching the request.

```
// Set request parameters
DescribePlayerSessionsRequest describePlayerSessionsRequest = new DescribePlayerSessionsRequest()
{
  GameSessionId = GameLiftServerAPI.GetGameSessionId().Result,    //gets the ID for the current game session
  Limit = `10`,
  PlayerSessionStatusFilter =
    PlayerSessionStatusMapper.GetNameForPlayerSessionStatus(PlayerSessionStatus.`ACTIVE`)
};
// Call DescribePlayerSessions
DescribePlayerSessionsOutcome describePlayerSessionsOutcome =
  GameLiftServerAPI.DescribePlayerSessions(describePlayerSessionsRequest);
```

## StartMatchBackfill()

Sends a request to find new players for open slots in a game session created with
FlexMatch. For more information, see [FlexMatch
backfill feature](../flexmatchguide/match-backfill.md "../flexmatchguide/match-backfill.md").

This action is asynchronous. If new players are matched, Amazon GameLift Servers delivers updated
matchmaker data using the callback function `OnUpdateGameSession()`.

A server process can have only one active match backfill request at a time. To send a
new request, first call [StopMatchBackfill()](#integration-server-sdk5-csharp-stopmatchbackfill "#integration-server-sdk5-csharp-stopmatchbackfill") to cancel the
original request.

### Syntax

```
StartMatchBackfillOutcome StartMatchBackfill (StartMatchBackfillRequest startBackfillRequest);
```

### Parameters

**[StartMatchBackfillRequest](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-startmatchbackfillrequest "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-startmatchbackfillrequest")**

A `StartMatchBackfillRequest` object holds information
about the backfill request.

### Return

value

Returns a [StartMatchBackfillOutcome](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-startmatchbackfilloutcome "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-startmatchbackfilloutcome") object with the match backfill ticket ID, or
failure with an error message.

### Example

```
// Build a backfill request
StartMatchBackfillRequest startBackfillRequest = new StartMatchBackfillRequest()
{
  TicketId = "`1111aaaa-22bb-33cc-44dd-5555eeee66ff`", //optional
  MatchmakingConfigurationArn = "`arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MyMatchmakerConfig`",
  GameSessionId = GameLiftServerAPI.GetGameSessionId().Result,    // gets ID for current game session
  MatchmakerData matchmakerData =
    MatchmakerData.FromJson(gameSession.MatchmakerData),  // gets matchmaker data for current players
  // get matchmakerData.Players
  // remove data for players who are no longer connected
  Players = ListOfPlayersRemainingInTheGame
};

// Send backfill request
StartMatchBackfillOutcome startBackfillOutcome = GameLiftServerAPI.StartMatchBackfill(startBackfillRequest);

// Implement callback function for backfill
void OnUpdateGameSession(GameSession myGameSession)
{
  // game-specific tasks to prepare for the newly matched players and update matchmaker data as needed
}
```

## StopMatchBackfill()

Cancels an active match backfill request. For more information, see [FlexMatch backfill feature](../flexmatchguide/match-backfill.md "../flexmatchguide/match-backfill.md").

### Syntax

```
GenericOutcome StopMatchBackfill (StopMatchBackfillRequest stopBackfillRequest);
```

### Parameters

**[StopMatchBackfillRequest](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-stopmatchbackfillrequest "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-stopmatchbackfillrequest")**

A `StopMatchBackfillRequest` object that provides details
about the matchmaking ticket you are stopping.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
// Set backfill stop request parameters
StopMatchBackfillRequest stopBackfillRequest = new StopMatchBackfillRequest(){
  TicketId = "`1111aaaa-22bb-33cc-44dd-5555eeee66ff`", //optional, if not provided one is autogenerated
  MatchmakingConfigurationArn = "`arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MyMatchmakerConfig`",
  GameSessionId = GameLiftServerAPI.GetGameSessionId().Result    //gets the ID for the current game session
};
GenericOutcome stopBackfillOutcome = GameLiftServerAPI.StopMatchBackfillRequest(stopBackfillRequest);
```

## GetComputeCertificate()

Retrieves the path to the TLS certificate used to encrypt the network connection
between the game server and your game client. You can use the certificate path
when you register your compute device to a Amazon GameLift Servers Anywhere fleet. For more information
see, [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md").

### Syntax

```
GetComputeCertificateOutcome GetComputeCertificate();
```

### Return

value

Returns a GetComputeCertificateResponse object that contains the following:

- CertificatePath: The path to the TLS certificate on your compute resource.
  When using an Amazon GameLift Servers managed fleet, this path contains:
  - `certificate.pem`: The end-user certificate. The full certificate chain is the combination of `certificateChain.pem` appended to this certificate.
  - `certificateChain.pem`: The certificate chain that contains the root certificate and intermediate certificates.
  - `rootCertificate.pem`: The root certificate.
  - `privateKey.pem`: The private key for the end-user certificate.

- ComputeName: The name of your compute resource.

### Example

```
GetComputeCertificateOutcome getComputeCertificateOutcome = GameLiftServerAPI.GetComputeCertificate();
```

## GetFleetRoleCredentials()

Retrieves IAM role credentials that authorize Amazon GameLift Servers to interact with other
AWS services. For more information, see [Communicate with other AWS resources from
your fleets](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").

### Syntax

```
GetFleetRoleCredentialsOutcome GetFleetRoleCredentials(GetFleetRoleCredentialsRequest request);
```

### Parameters

[GetFleetRoleCredentialsRequest](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-getfleetrolecredentialsrequest "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-dataypes-getfleetrolecredentialsrequest")

Role credentials that extend limited access to your AWS resources to
the game server.

### Return value

Returns a [GetFleetRoleCredentialsOutcome](integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsoutcome "integration-server-sdk5-csharp-datatypes.md#integration-server-sdk5-csharp-datatypes-getfleetrolecredentialsoutcome") object.

### Example

```
// form the fleet credentials request
GetFleetRoleCredentialsRequest getFleetRoleCredentialsRequest = new GetFleetRoleCredentialsRequest(){
  RoleArn = "`arn:aws:iam::123456789012:role/service-role/exampleGameLiftAction`"
};
GetFleetRoleCredentialsOutcome GetFleetRoleCredentialsOutcome credentials = GetFleetRoleCredentials(getFleetRoleCredentialsRequest);
```

## Destroy()

Frees the Amazon GameLift Servers game server SDK from memory. As a best practice, call this method
after `ProcessEnding()` and before terminating the process. If you're using
an Anywhere fleet and you're not terminating server processes after every game session,
call `Destroy()` and then `InitSDK()` to reinitialize before
notifying Amazon GameLift Servers that the process is ready to host a game session with
`ProcessReady()`.

### Syntax

```
GenericOutcome Destroy()
```

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
// Operations to end game sessions and the server process
GenericOutcome processEndingOutcome = GameLiftServerAPI.ProcessEnding();

// Shut down and destroy the instance of the GameLift Game Server SDK
GenericOutcome destroyOutcome = GameLiftServerAPI.Destroy();

// Exit the process with success or failure
if (processEndingOutcome.Success)
  {
    Environment.Exit(0);
  }
else
  {
    Console.WriteLine("ProcessEnding() failed. Error: " + processEndingOutcome.Error.ToString());
    Environment.Exit(-1);
  }
```
