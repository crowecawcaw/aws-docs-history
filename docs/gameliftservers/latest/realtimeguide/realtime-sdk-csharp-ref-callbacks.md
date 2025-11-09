# Amazon GameLift Servers Realtime client API (C#) reference:

Asynchronous callbacks

Use this C# Realtime Client API reference to help you prepare your multiplayer game for
use with Amazon GameLift Servers Realtime deployed on Amazon GameLift Servers fleets.

- [Synchronous Actions](realtime-sdk-csharp-ref-actions.md "realtime-sdk-csharp-ref-actions.md")
- Asynchronous Callbacks
- [Data Types](realtime-sdk-csharp-ref-datatypes.md "realtime-sdk-csharp-ref-datatypes.md")
  A game client needs to implement these callback methods to respond to events. The
  Realtime server invokes these callbacks to send game-related information to the game
  client. Callbacks for the same events can also be implemented with custom game logic in the
  Realtime server script. See [Script callbacks for Amazon GameLift Servers Realtime](realtime-script-callbacks.md "realtime-script-callbacks.md").

Callback methods are defined in `ClientEvents.cs`.

## OnOpen()

Invoked when the server process accepts the game client's connection request and opens
a connection.

### Syntax

```
public void OnOpen()
```

### Parameters

This method takes no parameters.

### Return

value

This method does not return anything.

## OnClose()

Invoked when the server process terminates the connection with the game client, such
as after a game session ends.

### Syntax

```
public void OnClose()
```

### Parameters

This method takes no parameters.

### Return

value

This method does not return anything.

## OnError()

Invoked when a failure occurs for a Realtime Client API request. This callback can be
customized to handle a variety of connection errors.

### Syntax

```
private void OnError(byte[] args)
```

### Parameters

This method takes no parameters.

### Return

value

This method does not return anything.

## OnDataReceived()

Invoked when the game client receives a message from the Realtime server. This is
the primary method by which messages and notifications are received by a game
client.

### Syntax

```
public void OnDataReceived(DataReceivedEventArgs dataReceivedEventArgs)
```

### Parameters

**dataReceivedEventArgs**

Information related to message activity.

Type: [DataReceivedEventArgs](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-dataeventargs "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-dataeventargs")

Required: Yes

### Return

value

This method does not return anything.

## OnGroupMembershipUpdated()

Invoked when the membership for a group that the player belongs to has been updated.
This callback is also invoked when a client calls
`RequestGroupMembership`.

### Syntax

```
public void OnGroupMembershipUpdated(GroupMembershipEventArgs groupMembershipEventArgs)
```

### Parameters

**groupMembershipEventArgs**

Information related to group membership activity.

Type: [GroupMembershipEventArgs](realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-groupeventargs "realtime-sdk-csharp-ref-datatypes.md#realtime-sdk-csharp-ref-datatypes-groupeventargs")

Required: Yes

### Return

value

This method does not return anything.
