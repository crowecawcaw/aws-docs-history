# C++ server SDK 5.x for Amazon GameLift Servers --

Actions

Use the server SDK 5.x reference to integrate your multiplayer game for hosting with
Amazon GameLift Servers. For guidance about the integration process, see [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md").

###### Note

This topic describes the Amazon GameLift Servers C++ API that you can use when you build with the C++ Standard Library (`std`).
Specifically, this documentation applies to code that you compile with the `-DDGAMELIFT_USE_STD=1` option.

[C++ server SDK 5.x for Amazon GameLift Servers -- Data
types](integration-server-sdk5-cpp-datatypes.md "integration-server-sdk5-cpp-datatypes.md")

###### Topics

- [GetSdkVersion()](#integration-server-sdk5-cpp-getsdkversion "#integration-server-sdk5-cpp-getsdkversion")
- [InitSDK()](#integration-server-sdk5-cpp-initsdk "#integration-server-sdk5-cpp-initsdk")
- [InitSDK()](#integration-server-sdk5-cpp-initsdk-anywhere "#integration-server-sdk5-cpp-initsdk-anywhere")
- [ProcessReady()](#integration-server-sdk5-cpp-processready "#integration-server-sdk5-cpp-processready")
- [ProcessReadyAsync()](#integration-server-sdk5-cpp-processreadyasync "#integration-server-sdk5-cpp-processreadyasync")
- [ProcessEnding()](#integration-server-sdk5-cpp-processending "#integration-server-sdk5-cpp-processending")
- [ActivateGameSession()](#integration-server-sdk5-cpp-activategamesession "#integration-server-sdk5-cpp-activategamesession")
- [UpdatePlayerSessionCreationPolicy()](#integration-server-sdk5-cpp-updateplayersessioncreationpolicy "#integration-server-sdk5-cpp-updateplayersessioncreationpolicy")
- [GetGameSessionId()](#integration-server-sdk5-cpp-getgamesessionid "#integration-server-sdk5-cpp-getgamesessionid")
- [GetTerminationTime()](#integration-server-sdk5-cpp-getterm "#integration-server-sdk5-cpp-getterm")
- [AcceptPlayerSession()](#integration-server-sdk5-cpp-acceptplayersession "#integration-server-sdk5-cpp-acceptplayersession")
- [RemovePlayerSession()](#integration-server-sdk5-cpp-removeplayersession "#integration-server-sdk5-cpp-removeplayersession")
- [DescribePlayerSessions()](#integration-server-sdk5-cpp-describeplayersessions "#integration-server-sdk5-cpp-describeplayersessions")
- [StartMatchBackfill()](#integration-server-sdk5-cpp-startmatchbackfill "#integration-server-sdk5-cpp-startmatchbackfill")
- [StopMatchBackfill()](#integration-server-sdk5-cpp-stopmatchbackfill "#integration-server-sdk5-cpp-stopmatchbackfill")
- [GetComputeCertificate()](#integration-server-sdk5-cpp-getcomputecertificate "#integration-server-sdk5-cpp-getcomputecertificate")
- [GetFleetRoleCredentials()](#integration-server-sdk5-cpp-getfleetrolecredentials "#integration-server-sdk5-cpp-getfleetrolecredentials")
- [Destroy()](#integration-server-sdk5-cpp-ref-destroy "#integration-server-sdk5-cpp-ref-destroy")

## GetSdkVersion()

Returns the current version number of the SDK built into the server process.

### Syntax

```
Aws::GameLift::AwsStringOutcome Server::GetSdkVersion();
```

### Return

value

If successful, returns the current SDK version as an [AwsStringOutcome](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-awsstringoutcome "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-awsstringoutcome") object. The
returned object includes the version number (example `5.0.0`). If not
successful, returns an error message.

### Example

```
Aws::GameLift::AwsStringOutcome SdkVersionOutcome = Aws::GameLift::Server::GetSdkVersion();
```

## InitSDK()

Initializes the Amazon GameLift Servers SDK. Call this method on launch before any other initialization
steps related to Amazon GameLift Servers. This action reads server parameters from the host environment to
set up communication between the game server process and the Amazon GameLift Servers service. It uses an
idempotency token, so you safely retry this call when it fails.

If the game server build will be deployed without the Amazon GameLift Servers Agent to a Amazon GameLift Servers Anywhere
fleet or container fleet, call [InitSDK()](#integration-server-sdk5-cpp-initsdk-anywhere "#integration-server-sdk5-cpp-initsdk-anywhere") and specify a set of
server parameters.

### Syntax

```
Server::InitSDKOutcome Server::initSdkOutcome = InitSDK();
```

### Return value

Returns an [InitSDKOutcome](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-initsdkoutcome "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-initsdkoutcome") object that indicates whether the server process
is ready to call [ProcessReady()](#integration-server-sdk5-cpp-processready "#integration-server-sdk5-cpp-processready").

### Example

```
//Call InitSDK to establish a local connection with the Amazon GameLift Servers Agent to enable further communication.
Aws::GameLift::Server::InitSDKOutcome initSdkOutcome =
  Aws::GameLift::Server::InitSDK();
```

## InitSDK()

Initializes the Amazon GameLift Servers SDK. Call this method on launch before any other initialization
steps related to Amazon GameLift Servers. This action requires a set of server parameters to set up
communication between the game server process and the Amazon GameLift Servers service. It uses an
idempotency token, so you safely retry this call when it fails.

If the game server build will be deployed to an Amazon GameLift Servers managed EC2 fleet or to an
Amazon GameLift Servers Anywhere fleet or container fleet with the Amazon GameLift Servers Agent, call [InitSDK()](#integration-server-sdk5-cpp-initsdk "#integration-server-sdk5-cpp-initsdk") without server parameters.

### Syntax

```
Server::InitSDKOutcome Server::initSdkOutcome = InitSDK(serverParameters);
```

### Parameters

[ServerParameters](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-serverparameters "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-serverparameters")

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

Returns an [InitSDKOutcome](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-initsdkoutcome "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-initsdkoutcome") object that indicates whether the server process
is ready to call [ProcessReady()](#integration-server-sdk5-cpp-processready "#integration-server-sdk5-cpp-processready").

###### Note

If calls to `InitSDK()` are failing for game builds deployed to
Anywhere fleets, check the `ServerSdkVersion` parameter used
when creating the build resource.
You must explicitly set this value to the server SDK version in use. The default value for this
parameter is 4.x, which is not compatible. To resolve this issue, create a new build and deploy it to a new fleet.

### Example

Amazon GameLift Servers Anywhere example

```
//Define the server parameters
std::string websocketUrl = "`wss://us-west-1.api.amazongamelift.com`";
std::string processId = "`PID1234`";
std::string fleetId = "`arn:aws:gamelift:us-west-1:111122223333:fleet/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa`";
std::string hostId = "`HardwareAnywhere`";
std::string authToken = "`1111aaaa-22bb-33cc-44dd-5555eeee66ff`";
Aws::GameLift::Server::Model::ServerParameters serverParameters =
  Aws::GameLift::Server::Model::ServerParameters(webSocketUrl, authToken, fleetId, hostId, processId);

//Call InitSDK to establish a local connection with the Amazon GameLift Servers Agent to enable further communication.
Aws::GameLift::Server::InitSDKOutcome initSdkOutcome = Aws::GameLift::Server::InitSDK(serverParameters);
```

## ProcessReady()

Notifies Amazon GameLift Servers that the server process is ready to host game sessions. Call this
method after invoking [InitSDK()](#integration-server-sdk5-cpp-initsdk "#integration-server-sdk5-cpp-initsdk"). This method should be called
only once per process.

### Syntax

`GenericOutcome ProcessReady(const Aws::GameLift::Server::ProcessParameters
 &processParameters);`

### Parameters

**processParameters**

A [ProcessParameters](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-process "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-process")
object communicating the following information about the server
process:

- Names of callback methods implemented in the game server code
  that the Amazon GameLift Servers service invokes to communicate with the server
  process.
- Port number that the server process is listening on.
- Path to any game session-specific files that you want Amazon GameLift Servers to
  capture and store.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example illustrates both the [ProcessReady()](#integration-server-sdk5-cpp-processready "#integration-server-sdk5-cpp-processready") call and delegate
function implementations.

```
// Set parameters and call ProcessReady
std::string serverLog("`serverOut.log`");        // Example of a log file written by the game server
std::vector<std::string> logPaths;
logPaths.push_back(serverLog);
int listenPort = `9339`;

Aws::GameLift::Server::ProcessParameters processReadyParameter =
  Aws::GameLift::Server::ProcessParameters(
    std::bind(&Server::onStartGameSession, this, std::placeholders::_1),
    std::bind(&Server::onProcessTerminate, this),
    std::bind(&Server::OnHealthCheck, this),
    std::bind(&Server::OnUpdateGameSession, this),
    listenPort,
    Aws::GameLift::Server::LogParameters(logPaths)
  );

Aws::GameLift::GenericOutcome outcome =
  Aws::GameLift::Server::ProcessReady(processReadyParameter);

// Implement callback functions
void Server::onStartGameSession(Aws::GameLift::Model::GameSession myGameSession)
{
  // game-specific tasks when starting a new game session, such as loading map
  GenericOutcome outcome =
    Aws::GameLift::Server::ActivateGameSession (maxPlayers);
}

void Server::onProcessTerminate()
{
  // game-specific tasks required to gracefully shut down a game session,
  // such as notifying players, preserving game state data, and other cleanup
  GenericOutcome outcome = Aws::GameLift::Server::ProcessEnding();
}

bool Server::onHealthCheck()
{
  bool health;
  // complete health evaluation within 60 seconds and set health
  return health;
}
```

## ProcessReadyAsync()

Notifies the Amazon GameLift Servers service that the server process is ready to host game sessions.
This method should be called after the server process is ready to host a game session.
The parameters specify the callback function names for Amazon GameLift Servers to call in certain
circumstances. Game server code must implement these functions.

This call is asynchronous. To make a synchronous call, use [ProcessReady()](#integration-server-sdk5-cpp-processready "#integration-server-sdk5-cpp-processready"). See [Initialize the server process](gamelift-sdk-server-api.md#gamelift-sdk-server-initialize "gamelift-sdk-server-api.md#gamelift-sdk-server-initialize") for more details.

### Syntax

```
GenericOutcomeCallable ProcessReadyAsync(
    const Aws::GameLift::Server::ProcessParameters &processParameters);
```

### Parameters

**processParameters**

A [ProcessParameters](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-process "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-process")
object communicating the following information about the server
process:

- Names of callback methods implemented in the game server code
  that the Amazon GameLift Servers service invokes to communicate with the server
  process.
- Port number that the server process is listening on.
- Path to any game session-specific files that you want Amazon GameLift Servers to
  capture and store.

Required: Yes

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
// Set parameters and call ProcessReady
std::string serverLog("`serverOut.log`");        // This is an example of a log file written by the game server
std::vector<std::string> logPaths;
logPaths.push_back(serverLog);
int listenPort = `9339`;

Aws::GameLift::Server::ProcessParameters processReadyParameter =
  Aws::GameLift::Server::ProcessParameters(std::bind(&Server::onStartGameSession, this, std::placeholders::_1),
  std::bind(&Server::onProcessTerminate, this), std::bind(&Server::OnHealthCheck, this),
  std::bind(&Server::OnUpdateGameSession, this), listenPort, Aws::GameLift::Server::LogParameters(logPaths));

Aws::GameLift::GenericOutcomeCallable outcome =
  Aws::GameLift::Server::ProcessReadyAsync(processReadyParameter);

// Implement callback functions
void onStartGameSession(Aws::GameLift::Model::GameSession myGameSession)
{
  // game-specific tasks when starting a new game session, such as loading map
  GenericOutcome outcome = Aws::GameLift::Server::ActivateGameSession (maxPlayers);
}

void onProcessTerminate()
{
  // game-specific tasks required to gracefully shut down a game session,
  // such as notifying players, preserving game state data, and other cleanup
  GenericOutcome outcome = Aws::GameLift::Server::ProcessEnding();
}

bool onHealthCheck()
{
  // perform health evaluation and complete within 60 seconds
  return health;
}
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
Aws::GameLift::GenericOutcome processEndingOutcome = Aws::GameLift::Server::ProcessEnding();
```

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example calls `ProcessEnding()` and `Destroy()` before
terminating the server process with a success or error exit code.

```
Aws::GameLift::GenericOutcome processEndingOutcome = Aws::GameLift::Server::ProcessEnding();
Aws::GameLift::Server::Destroy();

// Exit the process with success or failure
if (processEndingOutcome.IsSuccess()) {
  exit(0);
}
else {
  cout << "ProcessEnding() failed. Error: " << processEndingOutcome.GetError().GetErrorMessage();
  exit(-1);
}
```

## ActivateGameSession()

Notifies Amazon GameLift Servers that the server process has activated a game session and is now ready
to receive player connections. This action should be called as part of the
`onStartGameSession()` callback function, after all game session
initialization.

### Syntax

```
Aws::GameLift::GenericOutcome activateGameSessionOutcome = Aws::GameLift::Server::ActivateGameSession();
```

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example shows `ActivateGameSession()` called as part of the
`onStartGameSession()` delegate function.

```
void onStartGameSession(Aws::GameLift::Model::GameSession myGameSession)
{
  // game-specific tasks when starting a new game session, such as loading map
  GenericOutcome outcome = Aws::GameLift::Server::ActivateGameSession();
}
```

## UpdatePlayerSessionCreationPolicy()

Updates the current game session's ability to accept new player sessions. A game
session can be set to either accept or deny all new player sessions.

### Syntax

```
GenericOutcome UpdatePlayerSessionCreationPolicy(Aws::GameLift::Model::PlayerSessionCreationPolicy newPlayerSessionPolicy);
```

### Parameters

**playerCreationSessionPolicy**

Type: `PlayerSessionCreationPolicy`
[enum](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-enums "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-enums")
value.

Required: Yes

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example sets the current game session's join policy to accept all
players.

```
Aws::GameLift::GenericOutcome outcome =
  Aws::GameLift::Server::UpdatePlayerSessionCreationPolicy(Aws::GameLift::Model::PlayerSessionCreationPolicy::`ACCEPT_ALL`);
```

## GetGameSessionId()

Retrieves the ID of the game session hosted by the active server process.

For idle processes that aren't activated with a game session, the call returns a
[GameLiftError](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-gamelifterror "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-gamelifterror").

### Syntax

```
AwsStringOutcome GetGameSessionId()
```

### Parameters

This action has no parameters.

### Return

value

If successful, returns the game session ID as an [AwsStringOutcome](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-awsstringoutcome "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-awsstringoutcome") object.
If not successful, returns an error message.

For idle processes that aren't activated with a game session, the call returns
`Success`=`True` and
`GameSessionId`=`""`.

### Example

```
Aws::GameLift::AwsStringOutcome sessionIdOutcome = Aws::GameLift::Server::GetGameSessionId();
```

## GetTerminationTime()

Returns the time that a server process is scheduled to be shut down, if a termination
time is available. A server process takes action after receiving an
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

If successful, returns the termination time as an `AwsDateTimeOutcome`
object. The value is the termination time, expressed in elapsed ticks since
`0001 00:00:00`. For example, the date time value `2020-09-13
 12:26:40 -000Z` is equal to `637355968000000000` ticks. If no
termination time is available, returns an error message.

If the process hasn't received a ProcessParameters.OnProcessTerminate() callback,
an error message is returned. For more information about shutting down a server
process, see [Respond to a server process shutdown
notification](gamelift-sdk-server-api.md#gamelift-sdk-server-terminate "gamelift-sdk-server-api.md#gamelift-sdk-server-terminate").

### Example

```
Aws::GameLift::AwsLongOutcome TermTimeOutcome = Aws::GameLift::Server::GetTerminationTime();
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

Unique ID issued by Amazon GameLift Servers when a new player session is created.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example handles a connection request that includes validating and rejecting
non-valid player session IDs.

```
void ReceiveConnectingPlayerSessionID (Connection& connection, const std::string& playerSessionId)
{
  Aws::GameLift::GenericOutcome connectOutcome = Aws::GameLift::Server::AcceptPlayerSession(`playerSessionId`);
  if(connectOutcome.IsSuccess())
  {
    connectionToSessionMap.emplace(connection, playerSessionId);
    connection.Accept();
  }
  else
  {
    connection.Reject(connectOutcome.GetError().GetMessage();
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

**`playerSessionId`**

Unique ID issued by Amazon GameLift Servers when a new player session is created.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
Aws::GameLift::GenericOutcome disconnectOutcome = Aws::GameLift::Server::RemovePlayerSession(`playerSessionId`);
```

## DescribePlayerSessions()

Retrieves player session data which includes settings, session metadata, and player
data. Use this method to get information about the following:

- A single player session
- All player sessions in a game session
- All player sessions associated with a single player ID

### Syntax

```
DescribePlayerSessionsOutcome DescribePlayerSessions(DescribePlayerSessionsRequest describePlayerSessionsRequest)
```

### Parameters

**[DescribePlayerSessionsRequest](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-playersessions "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-playersessions")**

A [DescribePlayerSessionsRequest](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-playersessions "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-playersessions") object that describes which player
sessions to retrieve.

### Return

value

If successful, returns a [DescribePlayerSessionsOutcome](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-describeplayersessionsoutcome "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-describeplayersessionsoutcome") object
containing a set of player session objects that fit the request parameters.

### Example

This example requests all player sessions actively connected to a specified game
session. By omitting _NextToken_ and setting the
_Limit_ value to 10, Amazon GameLift Servers returns the first 10
player session records matching the request.

```
// Set request parameters
Aws::GameLift::Server::Model::DescribePlayerSessionsRequest request;
request.SetPlayerSessionStatusFilter(Aws::GameLift::Server::Model::PlayerSessionStatusMapper::GetNameForPlayerSessionStatus(Aws::GameLift::Server::Model::PlayerSessionStatus::Active));
request.SetLimit(`10`);
request.SetGameSessionId("`the game session ID`");    // can use GetGameSessionId()

// Call DescribePlayerSessions
Aws::GameLift::DescribePlayerSessionsOutcome playerSessionsOutcome = Aws::GameLift::Server::DescribePlayerSessions(request);
```

## StartMatchBackfill()

Sends a request to find new players for open slots in a game session created with
FlexMatch. For more information, see [FlexMatch backfill
feature](../flexmatchguide/match-backfill.md "../flexmatchguide/match-backfill.md").

This action is asynchronous. If new players are matched, Amazon GameLift Servers delivers updated
matchmaker data using the callback function `OnUpdateGameSession()`.

A server process can have only one active match backfill request at a time. To send a
new request, first call [StopMatchBackfill()](#integration-server-sdk5-cpp-stopmatchbackfill "#integration-server-sdk5-cpp-stopmatchbackfill") to cancel the
original request.

### Syntax

```
StartMatchBackfillOutcome StartMatchBackfill (StartMatchBackfillRequest startBackfillRequest);
```

### Parameters

**[StartMatchBackfillRequest](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-startmatchbackfillrequest "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-startmatchbackfillrequest")**

A StartMatchBackfillRequest object that communicates the following
information:

- A ticket ID to assign to the backfill request. This
  information is optional; if no ID is provided, Amazon GameLift Servers will
  generate one.
- The matchmaker to send the request to. The full configuration
  ARN is required. This value is in the game session's matchmaker
  data.
- The ID of the game session to backfill.
- The available matchmaking data for the game session's current
  players.

### Return

value

Returns a [StartMatchBackfillOutcome](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-startmatchbackfilloutcome "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-startmatchbackfilloutcome") object with the match backfill ticket ID, or
failure with an error message.

### Example

```
// Build a backfill request
std::vector<Player> players;
Aws::GameLift::Server::Model::StartMatchBackfillRequest startBackfillRequest;
startBackfillRequest.SetTicketId("`1111aaaa-22bb-33cc-44dd-5555eeee66ff`");  // optional, autogenerated if not provided
startBackfillRequest.SetMatchmakingConfigurationArn("`arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MyMatchmakerConfig`"); //from the game session matchmaker data
startBackfillRequest.SetGameSessionArn("`the game session ARN`");        // can use GetGameSessionId()
startBackfillRequest.SetPlayers(players);                                  // from the game session matchmaker data

// Send backfill request
Aws::GameLift::StartMatchBackfillOutcome backfillOutcome =
  Aws::GameLift::Server::StartMatchBackfill(startBackfillRequest);

// Implement callback function for backfill
void Server::OnUpdateGameSession(Aws::GameLift::Server::Model::GameSession gameSession, Aws::GameLift::Server::Model::UpdateReason updateReason, std::string backfillTicketId)
{
  // handle status messages
  // perform game-specific tasks to prep for newly matched players
}
```

## StopMatchBackfill()

Cancels an active match backfill request. For more information, see [FlexMatch
backfill feature](../flexmatchguide/match-backfill.md "../flexmatchguide/match-backfill.md").

### Syntax

```
GenericOutcome StopMatchBackfill (StopMatchBackfillRequest stopBackfillRequest);
```

### Parameters

**[StopMatchBackfillRequest](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-stopmatchbackfillrequest "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-stopmatchbackfillrequest")**

A StopMatchBackfillRequest object identifying the matchmaking ticket
to cancel:

- The ticket ID assigned to the backfill request.
- The matchmaker the backfill request was sent to.
- The game session associated with the backfill request.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
// Set backfill stop request parameters

Aws::GameLift::Server::Model::StopMatchBackfillRequest stopBackfillRequest;
stopBackfillRequest.SetTicketId("`1111aaaa-22bb-33cc-44dd-5555eeee66ff`");
stopBackfillRequest.SetGameSessionArn("`the game session ARN`"); // can use GetGameSessionId()
stopBackfillRequest.SetMatchmakingConfigurationArn("`arn:aws:gamelift:us-west-2:111122223333:matchmakingconfiguration/MyMatchmakerConfig`");
// from the game session matchmaker data

Aws::GameLift::GenericOutcome stopBackfillOutcome =
  Aws::GameLift::Server::StopMatchBackfill(stopBackfillRequest);
```

## GetComputeCertificate()

Retrieves the path to the TLS certificate used to encrypt the network connection
between your Amazon GameLift Servers Anywhere compute resource and Amazon GameLift Servers. You can use the certificate path
when you register your compute device to a Amazon GameLift Servers Anywhere fleet. For more information
see, [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md").

### Syntax

```
GetComputeCertificateOutcome Server::GetComputeCertificate()
```

### Return

value

Returns a [GetComputeCertificateOutcome](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-getcomputecertificateoutcome "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-getcomputecertificateoutcome").

### Example

```
Aws::GameLift::GetComputeCertificateOutcome certificate = Aws::GameLift::Server::GetComputeCertificate();
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

[GetFleetRoleCredentialsRequest](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-getfleetrolecredentialsrequest "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-dataypes-getfleetrolecredentialsrequest")

### Return value

Returns a [GetFleetRoleCredentialsOutcome](integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsoutcome "integration-server-sdk5-cpp-datatypes.md#integration-server-sdk5-cpp-datatypes-getfleetrolecredentialsoutcome") object.

### Example

```
// form the fleet credentials request
Aws::GameLift::Server::Model::GetFleetRoleCredentialsRequest getFleetRoleCredentialsRequest;
getFleetRoleCredentialsRequest.SetRoleArn("`arn:aws:iam::123456789012:role/service-role/exampleGameLiftAction`");

Aws::GameLift::GetFleetRoleCredentialsOutcome credentials = Aws::GameLift::Server::GetFleetRoleCredentials(getFleetRoleCredentialsRequest);
```

This example shows the use of the optional `RoleSessionName` value to
assign a name to the credentials session for auditing purposes. If you don't provide
a role session name, the default value
"`[fleet-id]`-`[host-id]`" is
used.

```
// form the fleet credentials request
Aws::GameLift::Server::Model::GetFleetRoleCredentialsRequest getFleetRoleCredentialsRequest;
getFleetRoleCredentialsRequest.SetRoleArn("`arn:aws:iam::123456789012:role/service-role/exampleGameLiftAction`");
getFleetRoleCredentialsRequest.SetRoleSessionName("`MyFleetRoleSession`");

Aws::GameLift::GetFleetRoleCredentialsOutcome credentials = Aws::GameLift::Server::GetFleetRoleCredentials(getFleetRoleCredentialsRequest);
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
GenericOutcome Aws::GameLift::Server::Destroy();
```

### Parameters

There are no parameters.

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
Aws::GameLift::GenericOutcome processEndingOutcome = Aws::GameLift::Server::ProcessEnding();
Aws::GameLift::Server::Destroy();

// Exit the process with success or failure
if (processEndingOutcome.IsSuccess()) {
  exit(0);
}
else {
  cout << "ProcessEnding() failed. Error: " << processEndingOutcome.GetError().GetErrorMessage();
  exit(-1);
}
```
