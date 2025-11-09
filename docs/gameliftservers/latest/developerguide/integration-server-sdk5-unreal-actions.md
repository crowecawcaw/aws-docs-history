# C++ (Unreal) server SDK 5.x for

Amazon GameLift Servers -- Actions

Use the Amazon GameLift Servers Unreal server SDK 5.x reference to help you prepare your multiplayer
game for use with Amazon GameLift Servers. For details about the integration process, see [Add Amazon GameLift Servers to your game server with the server
SDK](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md"). If you're
using the Amazon GameLift Servers plugin for Unreal, see also [Amazon GameLift Servers plugin for Unreal Engine](unreal-plugin.md "unreal-plugin.md").

###### Note

This topic describes the Amazon GameLift Servers C++ API that you can use when you build for the Unreal Engine.
Specifically, this documentation applies to code that you compile with the `-DBUILD_FOR_UNREAL=1` option.

[C++ (Unreal) server SDK 5.x for
Amazon GameLift Servers -- Data types](integration-server-sdk5-unreal-datatypes.md "integration-server-sdk5-unreal-datatypes.md")

###### Topics

- [GetSdkVersion()](#integration-server-sdk5-unreal-getsdkversion "#integration-server-sdk5-unreal-getsdkversion")
- [InitSDK()](#integration-server-sdk5-unreal-initsdk "#integration-server-sdk5-unreal-initsdk")
- [InitSDK()](#integration-server-sdk5-unreal-initsdk-anywhere "#integration-server-sdk5-unreal-initsdk-anywhere")
- [ProcessReady()](#integration-server-sdk5-unreal-processready "#integration-server-sdk5-unreal-processready")
- [ProcessEnding()](#integration-server-sdk5-unreal-processending "#integration-server-sdk5-unreal-processending")
- [ActivateGameSession()](#integration-server-sdk5-unreal-activategamesession "#integration-server-sdk5-unreal-activategamesession")
- [UpdatePlayerSessionCreationPolicy()](#integration-server-sdk5-unreal-updateplayersessioncreationpolicy "#integration-server-sdk5-unreal-updateplayersessioncreationpolicy")
- [GetGameSessionId()](#integration-server-sdk5-unreal-getgamesessionid "#integration-server-sdk5-unreal-getgamesessionid")
- [GetTerminationTime()](#integration-server-sdk5-unreal-getterm "#integration-server-sdk5-unreal-getterm")
- [AcceptPlayerSession()](#integration-server-sdk5-unreal-acceptplayersession "#integration-server-sdk5-unreal-acceptplayersession")
- [RemovePlayerSession()](#integration-server-sdk5-unreal-removeplayersession "#integration-server-sdk5-unreal-removeplayersession")
- [DescribePlayerSessions()](#integration-server-sdk5-unreal-describeplayersessions "#integration-server-sdk5-unreal-describeplayersessions")
- [StartMatchBackfill()](#integration-server-sdk5-unreal-startmatchbackfill "#integration-server-sdk5-unreal-startmatchbackfill")
- [StopMatchBackfill()](#integration-server-sdk5-unreal-stopmatchbackfill "#integration-server-sdk5-unreal-stopmatchbackfill")
- [GetComputeCertificate()](#integration-server-sdk5-unreal-getcomputecertificate "#integration-server-sdk5-unreal-getcomputecertificate")
- [GetFleetRoleCredentials()](#integration-server-sdk5-unreal-getfleetrolecredentials "#integration-server-sdk5-unreal-getfleetrolecredentials")
- [Destroy()](#integration-server-sdk5-unreal-ref-destroy "#integration-server-sdk5-unreal-ref-destroy")

## GetSdkVersion()

Returns the current version number of the SDK built into the server process.

### Syntax

```
FGameLiftStringOutcome GetSdkVersion();
```

### Return

value

If successful, returns the current SDK version as an [FGameLiftStringOutcome](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-awsstringoutcome "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-awsstringoutcome")
object. The returned object includes the version number (example
`5.0.0`). If not successful, returns an error message.

### Example

```
Aws::GameLift::AwsStringOutcome SdkVersionOutcome = Aws::GameLift::Server::GetSdkVersion();
```

## InitSDK()

Initializes the Amazon GameLift Servers SDK for a managed EC2 fleet. Call this method on launch, before
any other initialization related to Amazon GameLift Servers occurs. This method reads server parameters
from the host environment to set up communication between the server and the Amazon GameLift Servers
service. It uses an idempotency token, so you safely retry this call when it
fails.

### Syntax

```
FGameLiftGenericOutcome InitSDK()
```

### Return value

If successful, returns an `InitSdkOutcome` object indicating that the
server process is ready to call [ProcessReady()](#integration-server-sdk5-unreal-processready "#integration-server-sdk5-unreal-processready").

### Example

```
//Call InitSDK to establish a local connection with the Amazon GameLift Servers Agent to enable further communication.
FGameLiftGenericOutcome initSdkOutcome = GameLiftSdkModule->InitSDK();
```

## InitSDK()

Initializes the Amazon GameLift Servers SDK for an Anywhere fleet or managed container fleet. Call
this method on launch, before any other initialization related to Amazon GameLift Servers occurs. This
method requires explicit server parameters to set up communication between the server
and the Amazon GameLift Servers service. It uses an idempotency token, so you safely retry this call when it
fails.

### Syntax

```
FGameLiftGenericOutcome InitSDK(serverParameters)
```

### Parameters

[FServerParameters](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-serverparameters "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-serverparameters")

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

If successful, returns an `InitSdkOutcome` object indicating that the
server process is ready to call [ProcessReady()](#integration-server-sdk5-unreal-processready "#integration-server-sdk5-unreal-processready").

###### Note

If calls to `InitSDK()` are failing for game builds deployed to
Anywhere fleets, check the `ServerSdkVersion` parameter used
when creating the build resource.
You must explicitly set this value to the server SDK version in use. The default value for this
parameter is 4.x, which is not compatible. To resolve this issue, create a new build and deploy it to a new fleet.

### Example

```
//Define the server parameters
FServerParameters serverParameters;
parameters.m_authToken = "`1111aaaa-22bb-33cc-44dd-5555eeee66ff`";
parameters.m_fleetId = "`arn:aws:gamelift:us-west-1:111122223333:fleet/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa`";
parameters.m_hostId = "`HardwareAnywhere`";
parameters.m_processId = "`PID1234`";
parameters.m_webSocketUrl = "`wss://us-west-1.api.amazongamelift.com`";

//Call InitSDK to establish a local connection with the Amazon GameLift Servers Agent to enable further communication.
FGameLiftGenericOutcome initSdkOutcome = GameLiftSdkModule->InitSDK(serverParameters);
```

## ProcessReady()

Notifies Amazon GameLift Servers that the server process is ready to host game sessions. Call this
method after invoking [InitSDK()](#integration-server-sdk5-unreal-initsdk "#integration-server-sdk5-unreal-initsdk"). This method should be called
only once per process.

### Syntax

`GenericOutcome ProcessReady(const Aws::GameLift::Server::ProcessParameters
 &processParameters);`

### Parameters

**processParameters**

An [FProcessParameters](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-process "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-process")
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

This example illustrates both the [ProcessReady()](#integration-server-sdk5-unreal-processready "#integration-server-sdk5-unreal-processready") call and delegate
function implementations.

```
//Calling ProcessReady tells Amazon GameLift Servers this game server is ready to receive incoming game sessions!
UE_LOG(GameServerLog, Log, TEXT("Calling Process Ready"));
FGameLiftGenericOutcome processReadyOutcome = GameLiftSdkModule->ProcessReady(*params);
```

## ProcessEnding()

Notifies Amazon GameLift Servers that the server process is terminating. Call this method after all
other cleanup tasks (including shutting down the active game session) and before
terminating the process. Depending on the result of `ProcessEnding()`, the
process exits with success (0) or error (-1) and generates a fleet event. If the process
terminates with an error, the fleet event generated is
`SERVER_PROCESS_TERMINATED_UNHEALTHY`).

### Syntax

```
FGameLiftGenericOutcome ProcessEnding()
```

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
//OnProcessTerminate callback. Amazon GameLift Servers will invoke this callback before shutting down an instance hosting this game server.
//It gives this game server a chance to save its state, communicate with services, etc., before being shut down.
//In this case, we simply tell Amazon GameLift Servers we are indeed going to shutdown.
params->OnTerminate.BindLambda([=]() {
  UE_LOG(GameServerLog, Log, TEXT("Game Server Process is terminating"));
  GameLiftSdkModule->ProcessEnding();
});
```

## ActivateGameSession()

Notifies Amazon GameLift Servers that the server process has activated a game session and is now ready
to receive player connections. This action should be called as part of the
`onStartGameSession()` callback function, after all game session
initialization.

### Syntax

```
FGameLiftGenericOutcome ActivateGameSession()
```

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

This example shows `ActivateGameSession()` called as part of the
`onStartGameSession()` delegate function.

```
//When a game session is created, Amazon GameLift Servers sends an activation request to the game server and passes along the game session object containing game properties and other settings.
//Here is where a game server should take action based on the game session object.
//Once the game server is ready to receive incoming player connections, it should invoke GameLiftServerAPI.ActivateGameSession()
auto onGameSession = [=](Aws::GameLift::Server::Model::GameSession gameSession)
{
  FString gameSessionId = FString(gameSession.GetGameSessionId());
  UE_LOG(GameServerLog, Log, TEXT("GameSession Initializing: %s"), *gameSessionId);
  GameLiftSdkModule->ActivateGameSession();
};
```

## UpdatePlayerSessionCreationPolicy()

Updates the current game session's ability to accept new player sessions. A game
session can be set to either accept or deny all new player sessions.

### Syntax

```
FGameLiftGenericOutcome UpdatePlayerSessionCreationPolicy(EPlayerSessionCreationPolicy policy)
```

### Parameters

**playerCreationSessionPolicy**

String value indicating whether the game session accepts new players.

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
FGameLiftGenericOutcome outcome = GameLiftSdkModule->UpdatePlayerSessionCreationPolicy(Aws::GameLift::Model::EPlayerSessionCreationPolicy::`ACCEPT_ALL`);
```

## GetGameSessionId()

Retrieves the ID of the game session hosted by the active server process.

For idle processes that aren't activated with a game session, the call returns a
[FGameLiftError](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-gamelifterror "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-gamelifterror").

### Syntax

```
FGameLiftStringOutcome GetGameSessionId()
```

### Parameters

This action has no parameters.

### Return

value

If successful, returns the game session ID as an [FGameLiftStringOutcome](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-awsstringoutcome "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-awsstringoutcome") object.
If not successful, returns an error message."

For idle processes that aren't activated with a game session, the call returns
`Success`=`True` and
`GameSessionId`=`""`.

### Example

```
//When a game session is created, Amazon GameLift Servers sends an activation request to the game server and passes along the game session object containing game properties and other settings.
//Here is where a game server should take action based on the game session object.
//Once the game server is ready to receive incoming player connections, it should invoke GameLiftServerAPI.ActivateGameSession()
auto onGameSession = [=](Aws::GameLift::Server::Model::GameSession gameSession)
{
  FString gameSessionId = FString(gameSession.GetGameSessionId());
  UE_LOG(GameServerLog, Log, TEXT("GameSession Initializing: %s"), *gameSessionId);
  GameLiftSdkModule->ActivateGameSession();
};
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

If the process hasn't received a`ProcessParameters.OnProcessTerminate()` callback, an error message is
returned. For more information about shutting down a server process, see [Respond to a server process shutdown
notification](gamelift-sdk-server-api.md#gamelift-sdk-server-terminate "gamelift-sdk-server-api.md#gamelift-sdk-server-terminate").

### Example

```
AwsDateTimeOutcome TermTimeOutcome = GameLiftSdkModule->GetTerminationTime();
```

## AcceptPlayerSession()

Notifies Amazon GameLift Servers that a player with the specified player session ID has connected to the
server process and needs validation. Amazon GameLift Servers verifies that the player session ID is valid.
After the player session is validated, Amazon GameLift Servers changes the status of the player slot from
RESERVED to ACTIVE.

### Syntax

```
FGameLiftGenericOutcome AcceptPlayerSession(const FString& playerSessionId)
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
bool GameLiftManager::AcceptPlayerSession(const FString& playerSessionId, const FString& playerId)
{
  #if WITH_GAMELIFT
  UE_LOG(GameServerLog, Log, TEXT("Accepting GameLift PlayerSession: %s . PlayerId: %s"), *playerSessionId, *playerId);
  FString gsId = GetCurrentGameSessionId();
  if (gsId.IsEmpty()) {
    UE_LOG(GameServerLog, Log, TEXT("No GameLift GameSessionId. Returning early!"));
    return false;
  }

  if (!GameLiftSdkModule->AcceptPlayerSession(playerSessionId).IsSuccess()) {
    UE_LOG(GameServerLog, Log, TEXT("PlayerSession not Accepted."));
    return false;
  }

  // Add PlayerSession from internal data structures keeping track of connected players
  connectedPlayerSessionIds.Add(playerSessionId);
  idToPlayerSessionMap.Add(playerSessionId, PlayerSession{ playerId, playerSessionId });
  return true;
  #else
  return false;
  #endif
}
```

## RemovePlayerSession()

Notifies Amazon GameLift Servers that a player has disconnected from the server process. In response,
Amazon GameLift Servers changes the player slot to available.

### Syntax

```
FGameLiftGenericOutcome RemovePlayerSession(const FString& playerSessionId)
```

### Parameters

**`playerSessionId`**

Unique ID issued by Amazon GameLift Servers when a new player session is created.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
bool GameLiftManager::RemovePlayerSession(const FString& playerSessionId)
{
  #if WITH_GAMELIFT
  UE_LOG(GameServerLog, Log, TEXT("Removing GameLift PlayerSession: %s"), *playerSessionId);

  if (!GameLiftSdkModule->RemovePlayerSession(playerSessionId).IsSuccess()) {
    UE_LOG(GameServerLog, Log, TEXT("PlayerSession Removal Failed"));
    return false;
  }

  // Remove PlayerSession from internal data structures that are keeping track of connected players
  connectedPlayerSessionIds.Remove(playerSessionId);
  idToPlayerSessionMap.Remove(playerSessionId);

  // end the session if there are no more players connected
  if (connectedPlayerSessionIds.Num() == 0) {
    EndSession();
  }

  return true;
  #else
  return false;
  #endif
}
```

## DescribePlayerSessions()

Retrieves player session data which includes settings, session metadata, and player
data. Use this method to get information about the following:

- A single player session
- All player sessions in a game session
- All player sessions associated with a single player ID

### Syntax

```
FGameLiftDescribePlayerSessionsOutcome DescribePlayerSessions(const FGameLiftDescribePlayerSessionsRequest &describePlayerSessionsRequest)
```

### Parameters

**[FGameLiftDescribePlayerSessionsRequest](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-playersessions "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-playersessions")**

A [FGameLiftDescribePlayerSessionsRequest](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-playersessions "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-playersessions") object that describes which player
sessions to retrieve.

### Return

value

If successful, returns a [FGameLiftDescribePlayerSessionsOutcome](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-describeplayersessionsoutcome "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-describeplayersessionsoutcome") object
containing a set of player session objects that fit the request parameters.

### Example

This example requests all player sessions actively connected to a specified game
session. By omitting _NextToken_ and setting the
_Limit_ value to 10, Amazon GameLift Servers returns the first 10
player session records matching the request.

```
void GameLiftManager::DescribePlayerSessions()
{
  #if WITH_GAMELIFT
  FString localPlayerSessions;
  for (auto& psId : connectedPlayerSessionIds)
  {
    PlayerSession ps = idToPlayerSessionMap[psId];
    localPlayerSessions += FString::Printf(TEXT("%s : %s  ; "), *(ps.playerSessionId), *(ps.playerId));
  }
  UE_LOG(GameServerLog, Log, TEXT("LocalPlayerSessions: %s"), *localPlayerSessions);

  UE_LOG(GameServerLog, Log, TEXT("Describing PlayerSessions in this GameSession"));
  FGameLiftDescribePlayerSessionsRequest request;
  request.m_gameSessionId = GetCurrentGameSessionId();

  FGameLiftDescribePlayerSessionsOutcome outcome = GameLiftSdkModule->DescribePlayerSessions(request);
  LogDescribePlayerSessionsOutcome(outcome);
  #endif
}
```

## StartMatchBackfill()

Sends a request to find new players for open slots in a game session created with
FlexMatch. For more information, see [FlexMatch backfill
feature](../flexmatchguide/match-backfill.md "../flexmatchguide/match-backfill.md").

This action is asynchronous. If new players are matched, Amazon GameLift Servers delivers updated
matchmaker data using the callback function `OnUpdateGameSession()`.

A server process can have only one active match backfill request at a time. To send a
new request, first call [StopMatchBackfill()](#integration-server-sdk5-unreal-stopmatchbackfill "#integration-server-sdk5-unreal-stopmatchbackfill") to cancel the
original request.

### Syntax

```
FGameLiftStringOutcome StartMatchBackfill (FStartMatchBackfillRequest &startBackfillRequest);
```

### Parameters

**[FStartMatchBackfillRequest](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-startmatchbackfillrequest "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-startmatchbackfillrequest")**

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

Returns a `StartMatchBackfillOutcome` object with the match backfill
ticket ID, or failure with an error message.

### Example

```
FGameLiftStringOutcome FGameLiftServerSDKModule::StartMatchBackfill(const FStartMatchBackfillRequest& request)
{
  #if WITH_GAMELIFT
  Aws::GameLift::Server::Model::StartMatchBackfillRequest sdkRequest;
  sdkRequest.SetTicketId(TCHAR_TO_UTF8(*request.m_ticketId));
  sdkRequest.SetGameSessionArn(TCHAR_TO_UTF8(*request.m_gameSessionArn));
  sdkRequest.SetMatchmakingConfigurationArn(TCHAR_TO_UTF8(*request.m_matchmakingConfigurationArn));
  for (auto player : request.m_players) {
    Aws::GameLift::Server::Model::Player sdkPlayer;
    sdkPlayer.SetPlayerId(TCHAR_TO_UTF8(*player.m_playerId));
    sdkPlayer.SetTeam(TCHAR_TO_UTF8(*player.m_team));
    for (auto entry : player.m_latencyInMs) {
      sdkPlayer.WithLatencyMs(TCHAR_TO_UTF8(*entry.Key), entry.Value);
    }

    std::map<std::string, Aws::GameLift::Server::Model::AttributeValue> sdkAttributeMap;
    for (auto attributeEntry : player.m_playerAttributes) {
      FAttributeValue value = attributeEntry.Value;
      Aws::GameLift::Server::Model::AttributeValue attribute;
      switch (value.m_type) {
        case FAttributeType::STRING:
          attribute = Aws::GameLift::Server::Model::AttributeValue(TCHAR_TO_UTF8(*value.m_S));
        break;
        case FAttributeType::DOUBLE:
          attribute = Aws::GameLift::Server::Model::AttributeValue(value.m_N);
        break;
        case FAttributeType::STRING_LIST:
          attribute = Aws::GameLift::Server::Model::AttributeValue::ConstructStringList();
          for (auto sl : value.m_SL) {
            attribute.AddString(TCHAR_TO_UTF8(*sl));
          };
        break;
        case FAttributeType::STRING_DOUBLE_MAP:
          attribute = Aws::GameLift::Server::Model::AttributeValue::ConstructStringDoubleMap();
          for (auto sdm : value.m_SDM) {
            attribute.AddStringAndDouble(TCHAR_TO_UTF8(*sdm.Key), sdm.Value);
          };
        break;
      }
      sdkPlayer.WithPlayerAttribute((TCHAR_TO_UTF8(*attributeEntry.Key)), attribute);
    }
    sdkRequest.AddPlayer(sdkPlayer);
  }
  auto outcome = Aws::GameLift::Server::StartMatchBackfill(sdkRequest);
  if (outcome.IsSuccess()) {
    return FGameLiftStringOutcome(outcome.GetResult().GetTicketId());
  }
  else {
    return FGameLiftStringOutcome(FGameLiftError(outcome.GetError()));
  }
  #else
  return FGameLiftStringOutcome("");
  #endif
}
```

## StopMatchBackfill()

Cancels an active match backfill request. For more information, see [FlexMatch
backfill feature](../flexmatchguide/match-backfill.md "../flexmatchguide/match-backfill.md").

### Syntax

```
FGameLiftGenericOutcome StopMatchBackfill (FStopMatchBackfillRequest &stopBackfillRequest);
```

### Parameters

**[FStopMatchBackfillRequest](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-stopmatchbackfillrequest "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-stopmatchbackfillrequest")**

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
FGameLiftGenericOutcome FGameLiftServerSDKModule::StopMatchBackfill(const FStopMatchBackfillRequest& request)
{
  #if WITH_GAMELIFT
  Aws::GameLift::Server::Model::StopMatchBackfillRequest sdkRequest;
  sdkRequest.SetTicketId(TCHAR_TO_UTF8(*request.m_ticketId));
  sdkRequest.SetGameSessionArn(TCHAR_TO_UTF8(*request.m_gameSessionArn));
  sdkRequest.SetMatchmakingConfigurationArn(TCHAR_TO_UTF8(*request.m_matchmakingConfigurationArn));
  auto outcome = Aws::GameLift::Server::StopMatchBackfill(sdkRequest);
  if (outcome.IsSuccess()) {
    return FGameLiftGenericOutcome(nullptr);
  }
  else {
    return FGameLiftGenericOutcome(FGameLiftError(outcome.GetError()));
  }
  #else
  return FGameLiftGenericOutcome(nullptr);
  #endif
}
```

## GetComputeCertificate()

Retrieves the path to the TLS certificate used to encrypt the network connection
between your Amazon GameLift Servers Anywhere compute resource and Amazon GameLift Servers. You can use the certificate path
when you register your compute device to a Amazon GameLift Servers Anywhere fleet. For more information
see, [RegisterCompute](../apireference/API_RegisterCompute.md "../apireference/API_RegisterCompute.md").

### Syntax

```
FGameLiftGetComputeCertificateOutcome FGameLiftServerSDKModule::GetComputeCertificate()
```

### Return

value

Returns a `GetComputeCertificateResponse` object containing the
following:

- CertificatePath: The path to the TLS certificate on your compute resource.
- HostName: The host name of your compute resource.

### Example

```
FGameLiftGetComputeCertificateOutcome FGameLiftServerSDKModule::GetComputeCertificate()
{
  #if WITH_GAMELIFT
  auto outcome = Aws::GameLift::Server::GetComputeCertificate();
  if (outcome.IsSuccess()) {
    auto& outres = outcome.GetResult();
    FGameLiftGetComputeCertificateResult result;
    result.m_certificate_path = UTF8_TO_TCHAR(outres.GetCertificatePath());
    result.m_computeName = UTF8_TO_TCHAR(outres.GetComputeName());
    return FGameLiftGetComputeCertificateOutcome(result);
  }
  else {
    return FGameLiftGetComputeCertificateOutcome(FGameLiftError(outcome.GetError()));
  }
  #else
  return FGameLiftGetComputeCertificateOutcome(FGameLiftGetComputeCertificateResult());
  #endif
}
```

## GetFleetRoleCredentials()

Retrieves IAM role credentials that authorize Amazon GameLift Servers to interact with other
AWS services. For more information, see [Connect your Amazon GameLift Servers hosted game server to other AWS resources](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").

### Syntax

```
FGameLiftGetFleetRoleCredentialsOutcome FGameLiftServerSDKModule::GetFleetRoleCredentials(const FGameLiftGetFleetRoleCredentialsRequest &request)
```

### Parameters

[FGameLiftGetFleetRoleCredentialsRequest](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsrequest "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsrequest")

### Return value

Returns a [FGameLiftGetFleetRoleCredentialsOutcome](integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsoutcome "integration-server-sdk5-unreal-datatypes.md#integration-server-sdk5-unreal-dataypes-getfleetrolecredentialsoutcome") object.

### Example

```
FGameLiftGetFleetRoleCredentialsOutcome FGameLiftServerSDKModule::GetFleetRoleCredentials(const FGameLiftGetFleetRoleCredentialsRequest &request)
{
  #if WITH_GAMELIFT
  Aws::GameLift::Server::Model::GetFleetRoleCredentialsRequest sdkRequest;
  sdkRequest.SetRoleArn(TCHAR_TO_UTF8(*request.m_roleArn));
  sdkRequest.SetRoleSessionName(TCHAR_TO_UTF8(*request.m_roleSessionName));

  auto outcome = Aws::GameLift::Server::GetFleetRoleCredentials(sdkRequest);

  if (outcome.IsSuccess()) {
    auto& outres = outcome.GetResult();
    FGameLiftGetFleetRoleCredentialsResult result;
    result.m_assumedUserRoleArn = UTF8_TO_TCHAR(outres.GetAssumedUserRoleArn());
    result.m_assumedRoleId = UTF8_TO_TCHAR(outres.GetAssumedRoleId());
    result.m_accessKeyId = UTF8_TO_TCHAR(outres.GetAccessKeyId());
    result.m_secretAccessKey = UTF8_TO_TCHAR(outres.GetSecretAccessKey());
    result.m_sessionToken = UTF8_TO_TCHAR(outres.GetSessionToken());
    result.m_expiration = FDateTime::FromUnixTimestamp(outres.GetExpiration());
    return FGameLiftGetFleetRoleCredentialsOutcome(result);
  }
  else {
    return FGameLiftGetFleetRoleCredentialsOutcome(FGameLiftError(outcome.GetError()));
  }
  #else
  return FGameLiftGetFleetRoleCredentialsOutcome(FGameLiftGetFleetRoleCredentialsResult());
  #endif
}
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
FGameLiftGenericOutcome Destroy();
```

### Parameters

There are no parameters.

### Return value

Returns a generic outcome consisting of success or failure with an error message.

### Example

```
// First call ProcessEnding()
FGameLiftGenericOutcome processEndingOutcome = GameLiftSdkModule->ProcessEnding();

// Then call Destroy() to free the SDK from memory
FGameLiftGenericOutcome destroyOutcome = GameLiftSdkModule->Destroy();

// Exit the process with success or failure
if (processEndingOutcome.IsSuccess() && destroyOutcome.IsSuccess())
    {
    UE_LOG(GameServerLog, Log, TEXT("Server process ending successfully"));
}
else {
    if (!processEndingOutcome.IsSuccess()) {
        const FGameLiftError& error = processEndingOutcome.GetError();
        UE_LOG(GameServerLog, Error, TEXT("ProcessEnding() failed. Error: %s"),
        error.m_errorMessage.IsEmpty() ? TEXT("Unknown error") : *error.m_errorMessage);
    }
    if (!destroyOutcome.IsSuccess()) {
        const FGameLiftError& error = destroyOutcome.GetError();
        UE_LOG(GameServerLog, Error, TEXT("Destroy() failed. Error: %s"),
        error.m_errorMessage.IsEmpty() ? TEXT("Unknown error") : *error.m_errorMessage);
    }
}
```
