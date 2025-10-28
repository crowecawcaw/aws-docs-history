# Server SDK (Unreal) for Amazon GameLift Servers --

Actions

Use the server SDK for Unreal to integrate your multiplayer game for hosting with Amazon GameLift Servers.
For guidance about the integration process, see [Add Amazon GameLift Servers to your game server](gamelift-sdk-server-api.md "gamelift-sdk-server-api.md").

###### Note

This reference is for an earlier version of the server SDK for Amazon GameLift Servers. For the latest
version, see
[C++ (Unreal) server SDK 5.x for
Amazon GameLift Servers -- Actions](integration-server-sdk5-unreal-actions.md "integration-server-sdk5-unreal-actions.md").

This API is defined in `GameLiftServerSDK.h` and
`GameLiftServerSDKModels.h`.

To set up the Unreal Engine plugin and see code examples [Integrate Amazon GameLift Servers into an Unreal Engine
project](integration-engines-setup-unreal.md "integration-engines-setup-unreal.md").

[Server SDK (Unreal) for Amazon GameLift Servers
-- Data types](integration-server-sdk-unreal-ref-datatypes.md "integration-server-sdk-unreal-ref-datatypes.md")

###### Topics

- [AcceptPlayerSession()](#integration-server-sdk-unreal-ref-acceptplayersession "#integration-server-sdk-unreal-ref-acceptplayersession")
- [ActivateGameSession()](#integration-server-sdk-unreal-ref-activategamesession "#integration-server-sdk-unreal-ref-activategamesession")
- [DescribePlayerSessions()](#integration-server-sdk-unreal-ref-describeplayersessions "#integration-server-sdk-unreal-ref-describeplayersessions")
- [GetGameSessionId()](#integration-server-sdk-unreal-ref-getgamesessionid "#integration-server-sdk-unreal-ref-getgamesessionid")
- [GetInstanceCertificate()](#integration-server-sdk-unreal-ref-getinstancecertificate "#integration-server-sdk-unreal-ref-getinstancecertificate")
- [GetSdkVersion()](#integration-server-sdk-unreal-ref-getsdk "#integration-server-sdk-unreal-ref-getsdk")
- [InitSDK()](#integration-server-sdk-unreal-ref-initsdk "#integration-server-sdk-unreal-ref-initsdk")
- [ProcessEnding()](#integration-server-sdk-unreal-ref-processending "#integration-server-sdk-unreal-ref-processending")
- [ProcessReady()](#integration-server-sdk-unreal-ref-processready "#integration-server-sdk-unreal-ref-processready")
- [RemovePlayerSession()](#integration-server-sdk-unreal-ref-removeplayersession "#integration-server-sdk-unreal-ref-removeplayersession")
- [StartMatchBackfill()](#integration-server-sdk-unreal-ref-startmatchbackfill "#integration-server-sdk-unreal-ref-startmatchbackfill")
- [StopMatchBackfill()](#integration-server-sdk-unreal-ref-stopmatchbackfill "#integration-server-sdk-unreal-ref-stopmatchbackfill")
- [TerminateGameSession()](#integration-server-sdk-unreal-ref-terminategamesession "#integration-server-sdk-unreal-ref-terminategamesession")
- [UpdatePlayerSessionCreationPolicy()](#integration-server-sdk-unreal-ref-updateplayersessioncreationpolicy "#integration-server-sdk-unreal-ref-updateplayersessioncreationpolicy")

## AcceptPlayerSession()

Notifies the Amazon GameLift Servers service that a player with the specified player session ID has
connected to the server process and needs validation. Amazon GameLift Servers verifies that the player
session ID is valid—that is, that the player ID has reserved a player slot in the
game session. Once validated, Amazon GameLift Servers changes the status of the player slot from RESERVED
to ACTIVE.

### Syntax

```
FGameLiftGenericOutcome AcceptPlayerSession(const FString& playerSessionId)
```

### Parameters

**playerSessionId**
Unique ID issued by the Amazon GameLift Servers service in response to
a call to the AWS SDK Amazon GameLift Servers API action
[CreatePlayerSession](../../../gamelift/latest/apireference/API_CreatePlayerSession.md "../../../gamelift/latest/apireference/API_CreatePlayerSession.md").
The game client references this ID when connecting to the server process.

Type: FString

Required: Yes

### Return value

Returns a generic outcome consisting of success or failure with an error message.

## ActivateGameSession()

Notifies the Amazon GameLift Servers service that the server process has activated a game session and is
now ready to receive player connections. This action should be called as part of the
`onStartGameSession()` callback function, after all game session
initialization has been completed.

### Syntax

```
FGameLiftGenericOutcome ActivateGameSession()
```

### Parameters

This action has no parameters.

### Return value

Returns a generic outcome consisting of success or failure with an error message.

## DescribePlayerSessions()

Retrieves player session data, including settings, session metadata, and player data.
Use this action to get information for a single player session, for all player sessions
in a game session, or for all player sessions associated with a single player ID.

### Syntax

```
FGameLiftDescribePlayerSessionsOutcome DescribePlayerSessions(const FGameLiftDescribePlayerSessionsRequest &describePlayerSessionsRequest)
```

### Parameters

**describePlayerSessionsRequest**

A [FDescribePlayerSessionsRequest](integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-playersessions "integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-playersessions") object describing which player sessions to retrieve.

Required: Yes

### Return value

If successful, returns a [FDescribePlayerSessionsRequest](integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-playersessions "integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-playersessions")
object containing a set of player session objects that fit the request parameters.
Player session objects have a structure identical to the AWS SDK Amazon GameLift Servers API
[PlayerSession](../../../gamelift/latest/apireference/API_PlayerSession.md "../../../gamelift/latest/apireference/API_PlayerSession.md") data
type.

## GetGameSessionId()

Retrieves the ID of the game session currently being hosted by the server process, if
the server process is active.

### Syntax

```
FGameLiftStringOutcome GetGameSessionId()
```

### Parameters

This action has no parameters.

### Return

value

If successful, returns the game session ID as an
`FGameLiftStringOutcome` object. If not successful, returns an error
message.

## GetInstanceCertificate()

Retrieves the file location of a pem-encoded TLS certificate that is associated with
the fleet and its instances. AWS Certificate Manager generates this certificate when you create a new
fleet with the certificate configuration set to GENERATED. Use this certificate to
establish a secure connection with a game client and to encrypt client/server
communication.

### Syntax

```
FGameLiftGetInstanceCertificateOutcome GetInstanceCertificate()
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

## GetSdkVersion()

Returns the current version number of the SDK built into the server process.

### Syntax

```
FGameLiftStringOutcome GetSdkVersion();
```

### Parameters

This action has no parameters.

### Return

value

If successful, returns the current SDK version as an
`FGameLiftStringOutcome` object. The returned string includes the
version number only (ex. "3.1.5"). If not successful, returns an error
message.

### Example

```
Aws::GameLift::AwsStringOutcome SdkVersionOutcome =
    Aws::GameLift::Server::GetSdkVersion();
```

## InitSDK()

Initializes the Amazon GameLift Servers SDK. This method should be called on launch, before any other
Amazon GameLift Servers-related initialization occurs.

### Syntax

```
FGameLiftGenericOutcome InitSDK()
```

### Parameters

This action has no parameters.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

## ProcessEnding()

Notifies the Amazon GameLift Servers service that the server process is shutting down. This method
should be called after all other cleanup tasks, including shutting down all active game
sessions. This method should exit with an exit code of 0; a non-zero exit code results
in an event message that the process did not exit cleanly.

### Syntax

```
FGameLiftGenericOutcome ProcessEnding()
```

### Parameters

This action has no parameters.

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

## ProcessReady()

Notifies the Amazon GameLift Servers service that the server process is ready to host game sessions.
Call this method after successfully invoking [InitSDK()](#integration-server-sdk-unreal-ref-initsdk "#integration-server-sdk-unreal-ref-initsdk") and completing setup
tasks that are required before the server process can host a game session. This method
should be called only once per process.

### Syntax

```
FGameLiftGenericOutcome ProcessReady(FProcessParameters &processParameters)
```

### Parameters

**FProcessParameters**

A [FProcessParameters](integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-process "integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-process")
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

See the sample code in [Using
the Unreal Engine Plugin](integration-engines-setup-unreal.md#integration-engines-setup-unreal-code "integration-engines-setup-unreal.md#integration-engines-setup-unreal-code").

## RemovePlayerSession()

Notifies the Amazon GameLift Servers service that a player with the specified player session ID has
disconnected from the server process. In response, Amazon GameLift Servers changes the player slot to
available, which allows it to be assigned to a new player.

### Syntax

```
FGameLiftGenericOutcome RemovePlayerSession(const FString& playerSessionId)
```

### Parameters

**playerSessionId**
Unique ID issued by the Amazon GameLift Servers service in response to
a call to the AWS SDK Amazon GameLift Servers API action
[CreatePlayerSession](../../../gamelift/latest/apireference/API_CreatePlayerSession.md "../../../gamelift/latest/apireference/API_CreatePlayerSession.md").
The game client references this ID when connecting to the server process.

Type: FString

Required: Yes

### Return value

Returns a generic outcome consisting of success or failure with an error message.

## StartMatchBackfill()

Sends a request to find new players for open slots in a game session created with
FlexMatch. See also the AWS SDK action [StartMatchBackfill()](../../../gamelift/latest/apireference/API_StartMatchBackfill.md "../../../gamelift/latest/apireference/API_StartMatchBackfill.md"). With
this action, match backfill requests can be initiated by a game server process that is
hosting the game session. Learn more about the [FlexMatch backfill feature](../../../gamelift/latest/flexmatchguide/match-backfill.md "../../../gamelift/latest/flexmatchguide/match-backfill.md").

This action is asynchronous. If new players are successfully matched, the Amazon GameLift Servers
service delivers updated matchmaker data using the callback function
`OnUpdateGameSession()`.

A server process can have only one active match backfill request at a time. To send a
new request, first call [StopMatchBackfill()](#integration-server-sdk-unreal-ref-stopmatchbackfill "#integration-server-sdk-unreal-ref-stopmatchbackfill") to cancel the
original request.

### Syntax

```
FGameLiftStringOutcome StartMatchBackfill (FStartMatchBackfillRequest &startBackfillRequest);
```

### Parameters

**FStartMatchBackfillRequest**

A [FStartMatchBackfillRequest](integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-startmatchbackfillrequest "integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-startmatchbackfillrequest") object that communicates the following information:

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

If successful, returns the match backfill ticket as a
`FGameLiftStringOutcome` object. If not successful, returns an error
message. Ticket status can be tracked using the AWS SDK action [DescribeMatchmaking()](../../../gamelift/latest/apireference/API_DescribeMatchmaking.md "../../../gamelift/latest/apireference/API_DescribeMatchmaking.md").

## StopMatchBackfill()

Cancels an active match backfill request that was created with [StartMatchBackfill()](#integration-server-sdk-unreal-ref-startmatchbackfill "#integration-server-sdk-unreal-ref-startmatchbackfill"). See also the
AWS SDK action [StopMatchmaking()](../../../gamelift/latest/apireference/API_StopMatchmaking.md "../../../gamelift/latest/apireference/API_StopMatchmaking.md"). Learn more about the [FlexMatch backfill feature](../../../gamelift/latest/flexmatchguide/match-backfill.md "../../../gamelift/latest/flexmatchguide/match-backfill.md").

### Syntax

```
FGameLiftGenericOutcome StopMatchBackfill (FStopMatchBackfillRequest &stopBackfillRequest);
```

### Parameters

**StopMatchBackfillRequest**

A [FStopMatchBackfillRequest](integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-stopmatchbackfillrequest "integration-server-sdk-unreal-ref-datatypes.md#integration-server-sdk-unreal-ref-dataypes-stopmatchbackfillrequest") object identifying the matchmaking ticket to cancel:

- ticket ID assigned to the backfill request being
  canceled
- matchmaker the backfill request was sent to
- game session associated with the backfill request

Required: Yes

### Return

value

Returns a generic outcome consisting of success or failure with an error message.

## TerminateGameSession()

**This method is deprecated with version 4.0.1. Instead, the
server process should call [ProcessEnding()](#integration-server-sdk-unreal-ref-processending "#integration-server-sdk-unreal-ref-processending") after a game
session has ended.**

Notifies the Amazon GameLift Servers service that the server process has ended the current game session.
This action is called when the server process will remain active and ready to host a new
game session. It should be called only after your game session termination procedure is
complete, because it signals to Amazon GameLift Servers that the server process is immediately available
to host a new game session.

This action is not called if the server process will be shut down after the game
session stops. Instead, call [ProcessEnding()](#integration-server-sdk-unreal-ref-processending "#integration-server-sdk-unreal-ref-processending") to signal that
both the game session and the server process are ending.

### Syntax

```
FGameLiftGenericOutcome TerminateGameSession()
```

### Parameters

This action has no parameters.

### Return value

Returns a generic outcome consisting of success or failure with an error message.

## UpdatePlayerSessionCreationPolicy()

Updates the current game session's ability to accept new player sessions. A game
session can be set to either accept or deny all new player sessions. (See also the
[`UpdateGameSession()`](../../../gamelift/latest/apireference/API_UpdateGameSession.md "../../../gamelift/latest/apireference/API_UpdateGameSession.md") action in the _Amazon GameLift Servers Service API Reference_).

### Syntax

```
FGameLiftGenericOutcome UpdatePlayerSessionCreationPolicy(EPlayerSessionCreationPolicy policy)
```

### Parameters

**Policy**

Value indicating whether the game session accepts new players.

Type: `EPlayerSessionCreationPolicy` enum. Valid values
include:

- **ACCEPT_ALL** – Accept all
  new player sessions.
- **DENY_ALL** – Deny all new
  player sessions.

Required: Yes

### Return value

Returns a generic outcome consisting of success or failure with an error message.
