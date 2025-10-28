# Amazon GameLift Servers Realtime client API (C#) reference:

Actions

This C# Realtime Client API reference can help you prepare your multiplayer game for use
with Amazon GameLift Servers Realtime deployed on Amazon GameLift Servers fleets.

- Synchronous Actions
- [Asynchronous
  Callbacks](realtime-sdk-csharp-ref-callbacks.md "realtime-sdk-csharp-ref-callbacks.md")
- [Data Types](realtime-sdk-csharp-ref-datatypes.md "realtime-sdk-csharp-ref-datatypes.md")

## Client()

Initializes a new client to communicate with the Realtime server and identifies the
type of connection to use.

### Syntax

```
public Client(ClientConfiguration configuration)
```

### Parameters

**clientConfiguration**

Configuration details specifying the client/server connection type.
You can opt to call Client() without this parameter; however, this
approach results in an unsecured connection by default.

Type: [ClientConfiguration](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-clientconfiguration "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-clientconfiguration")

Required: No

### Return value

Returns an instance of the Realtime client for use with communicating with the
Realtime server.

## Connect()

Requests a connection to a server process that is hosting a game session.

### Syntax

```
public ConnectionStatus Connect(string endpoint, int remoteTcpPort, int listenPort, ConnectionToken token)
```

### Parameters

**endpoint**

DNS name or IP address of the game session to connect to. The endpoint
is specified in a `GameSession` object, which is returned in
response to a client call to the _AWS SDK
Amazon GameLift Servers API_ actions [StartGameSessionPlacement](../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md "../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md"), [CreateGameSession](../../../gamelift/latest/apireference/API_CreateGameSession.md "../../../gamelift/latest/apireference/API_CreateGameSession.md"), or [DescribeGameSessions](../../../gamelift/latest/apireference/API_SearchGameSessions.md "../../../gamelift/latest/apireference/API_SearchGameSessions.md").

###### Note

If the Realtime server is running on a fleet with a TLS
certificate, you must use the DNS name.

Type: String

Required: Yes

**remoteTcpPort**

Port number for the TCP connection assigned to the game session. This
information is specified in a `GameSession` object, which is
returned in response to a [StartGameSessionPlacement](../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md "../../../gamelift/latest/apireference/API_StartGameSessionPlacement.md")
[CreateGameSession](../../../gamelift/latest/apireference/API_CreateGameSession.md "../../../gamelift/latest/apireference/API_CreateGameSession.md"), or [DescribeGameSession](../../../gamelift/latest/apireference/API_DescribeGameSession.md "../../../gamelift/latest/apireference/API_DescribeGameSession.md") request.

Type: Integer

Valid Values: 1900 to 2000.

Required: Yes

**listenPort**

Port number that the game client is listening on for messages sent
using the UDP channel.

Type: Integer

Valid Values: 33400 to 33500.

Required: Yes

**token**

Optional information that identifies the requesting game client to the
server process.

Type: [ConnectionToken](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-connectiontoken "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-connectiontoken")

Required: Yes

### Return

value

Returns a [ConnectionStatus](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-enums "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-enums") enum value indicating the client's connection status.

## Disconnect()

When connected to a game session, disconnects the game client from the game session.

### Syntax

```
public void Disconnect()
```

### Parameters

This action has no parameters.

### Return

value

This method does not return anything.

## NewMessage()

Creates a new message object with a specified operation code. Once a message object is
returned, complete the message content by specifying a target, updating the delivery
method, and adding a data payload as needed. Once completed, send the message using
`SendMessage()`.

### Syntax

```
public RTMessage NewMessage(int opCode)
```

### Parameters

**opCode**

Developer-defined operation code that identifies a game event or
action, such as a player move or a server notification.

Type: Integer

Required: Yes

### Return

value

Returns an [RTMessage](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage") object containing
the specified operation code and default delivery method. The delivery intent
parameter is set to `FAST` by default.

## SendMessage()

Sends a message to a player or group using the delivery method specified.

### Syntax

```
public void SendMessage(RTMessage message)
```

### Parameters

**message**

Message object that specifies the target recipient, delivery method,
and message content.

Type: [RTMessage](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage")

Required: Yes

### Return

value

This method does not return anything.

## JoinGroup()

Adds the player to the membership of a specified group. Groups can contain any of the
players that are connected to the game. Once joined, the player receives all future
messages sent to the group and can send messages to the entire group.

### Syntax

```
public void JoinGroup(int targetGroup)
```

### Parameters

**targetGroup**

Unique ID that identifies the group to add the player to. Group IDs
are developer-defined.

Type: Integer

Required: Yes

### Return

value

This method does not return anything. Because this request is sent using the
reliable (TCP) delivery method, a failed request triggers the callback [OnError()](realtime-sdk-csharp-ref-callbacks.md#realtime-sdk-csharp-ref-callbacks-onerror "realtime-sdk-csharp-ref-callbacks.md#realtime-sdk-csharp-ref-callbacks-onerror").

## LeaveGroup()

Removes the player from the membership of a specified group. Once no longer in the
group, the player does not receive messages sent to the group and cannot send messages
to the entire group.

### Syntax

```
public void LeaveGroup(int targetGroup)
```

### Parameters

**targetGroup**

Unique ID identifying the group to remove the player from. Group IDs
are developer-defined.

Type: Integer

Required: Yes

### Return

value

This method does not return anything. Because this request is sent using the
reliable (TCP) delivery method, a failed request triggers the callback [OnError()](realtime-sdk-csharp-ref-callbacks.md#realtime-sdk-csharp-ref-callbacks-onerror "realtime-sdk-csharp-ref-callbacks.md#realtime-sdk-csharp-ref-callbacks-onerror").

## RequestGroupMembership()

Requests that a list of players in the specified group be sent to the game client. Any
player can request this information, regardless of whether they are a member of the
group or not. In response to this request, the membership list is sent to the client via
an [OnGroupMembershipUpdated()](realtime-sdk-csharp-ref-callbacks.md#realtime-sdk-csharp-ref-callbacks-ongroupupdate "realtime-sdk-csharp-ref-callbacks.md#realtime-sdk-csharp-ref-callbacks-ongroupupdate") callback.

### Syntax

```
public void RequestGroupMembership(int targetGroup)
```

### Parameters

**targetGroup**

Unique ID identifying the group to get membership information for.
Group IDs are developer-defined.

Type: Integer

Required: Yes

### Return value

This method does not return anything.
