# Amazon GameLift Servers Realtime interface

When an Amazon GameLift Servers Realtime script initializes, an interface to the Realtime server is returned.
This topic describes the properties and methods available through the interface. Learn more
about writing Realtime scripts and view a detailed script example in [Customize an Amazon GameLift Servers Realtime script](realtime-script.md "realtime-script.md").

The Realtime interface provides access to the following objects:

- session
- player
- gameMessage
- configuration

###### Realtime Session object

Use these methods to access server-related information and perform server-related
actions.

## getPlayers()

Retrieves a list of peer IDs for players that are currently connected to the game
session. Returns an array of player objects.

### Syntax

```
rtSession.getPlayers()
```

## broadcastGroupMembershipUpdate()

Triggers delivery of an updated group membership list to player group. Specify which
membership to broadcast (groupIdToBroadcast) and the group to receive the update
(targetGroupId). Group IDs must be a positive integer or "-1" to indicate all groups.
See [Amazon GameLift Servers Realtime script example](realtime-script.md#realtime-script-examples "realtime-script.md#realtime-script-examples")
for an example of user-defined group IDs.

### Syntax

```
rtSession.broadcastGroupMembershipUpdate(groupIdToBroadcast, targetGroupId)
```

## getServerId()

Retrieves the server's unique peer ID identifier, which is used to route messages to
the server.

### Syntax

```
rtSession.getServerId()
```

## getAllPlayersGroupId()

Retrieves the group ID for the default group that contains all players currently
connected to the game session.

### Syntax

```
rtSession.getAllPlayersGroupId()
```

## processEnding()

Triggers the Realtime server to terminate the game server. This function must be
called from the Realtime script to exit cleanly from a game session.

### Syntax

```
rtSession.processEnding()
```

## getGameSessionId()

Retrieves the unique ID of the game session currently running.

### Syntax

```
rtSession.getGameSessionId()
```

## getLogger()

Retrieves the interface for logging. Use this to log statements that will be captured
in your game session logs. The logger supports use of "info", "warn", and "error"
statements. For example: `logger.info("<string>")`.

### Syntax

```
rtSession.getLogger()
```

## sendMessage()

Sends a message, created using `newTextGameMessage` or
`newBinaryGameMessage`, from the Realtime server to a player recipient
using the UDP channel. Identify the recipient using the player's peer ID.

### Syntax

```
rtSession.sendMessage(gameMessage, targetPlayer)
```

## sendGroupMessage()

Sends a message, created using `newTextGameMessage` or
`newBinaryGameMessage`, from the Realtime server to all players in a
player group using the UDP channel. Group IDs must be a positive integer or "-1" to
indicate all groups. See [Amazon GameLift Servers Realtime script example](realtime-script.md#realtime-script-examples "realtime-script.md#realtime-script-examples") for an example of user-defined group
IDs.

### Syntax

```
rtSession.sendGroupMessage(gameMessage, targetGroup)
```

## sendReliableMessage()

Sends a message, created using `newTextGameMessage` or
`newBinaryGameMessage`, from the Realtime server to a player recipient
using the TCP channel. Identify the recipient using the player's peer ID.

### Syntax

```
rtSession.sendReliableMessage(gameMessage, targetPlayer)
```

## sendReliableGroupMessage()

Sends a message, created using `newTextGameMessage` or
`newBinaryGameMessage`, from the Realtime server to all players in a
player group using the TCP channel. Group IDs which must be a positive integer or "-1"
to indicate all groups. See [Amazon GameLift Servers Realtime script example](realtime-script.md#realtime-script-examples "realtime-script.md#realtime-script-examples") for an example of user-defined group
IDs.

### Syntax

```
rtSession.sendReliableGroupMessage(gameMessage, targetGroup)
```

## newTextGameMessage()

Creates a new message containing text, to be sent from the server to player recipients
using the SendMessage functions. Message format is similar to the format used in the
client SDK for Realtime (see [RTMessage](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage")). Returns a
`gameMessage` object.

### Syntax

```
rtSession.newTextGameMessage(opcode, sender, payload)
```

## newBinaryGameMessage()

Creates a new message containing binary data, to be sent from the server to player
recipients using the SendMessage functions. Message format is similar to the format used
in the client SDK for Realtime (see [RTMessage](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage")). Returns a
`gameMessage` object.

### Syntax

```
rtSession.newBinaryGameMessage(opcode, sender, binaryPayload)
```

## Player object

Access player-related information.

### player.peerId

Unique ID that is assigned to a game client when it connects to the Realtime
server and joined the game session.

### player.playerSessionId

Player session ID that was referenced by the game client when it connected to the
Realtime server and joined the game session.

###### Game message object

Use these methods to access messages that are received by the Realtime server.
Messages received from game clients have the [RTMessage](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-rtmessage") structure.

## getPayloadAsText()

Gets the game message payload as text.

### Syntax

```
gameMessage.getPayloadAsText()
```

## gameMessage.opcode

Operation code contained in a message.

## gameMessage.payload

Payload contained in a message. May be text or binary.

## gameMessage.sender

Peer ID of the game client that sent a message.

## gameMessage.reliable

Boolean indicating whether the message was sent via TCP (true) or UDP (false).

## Configuration object

The configuration object can be used to override default configurations.

### configuration.maxPlayers

The maximum number of client / server connections that can be accepted by
RealTimeServers.

The default is 32.

### configuration.pingIntervalTime

Time interval in milliseconds that server will attempt to send a ping to all
connected clients to verify connections are healthy.

The default is 3000ms.
