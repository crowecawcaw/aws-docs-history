# Lifecycle events

AWS IoT can publish lifecycle events on the MQTT topics. These events are available by
default and they can't be disabled.

###### Note

Lifecycle messages might be sent out of order. You might receive duplicate
messages.

`thingName` will only be included if the client is connecting using the
[exclusive thing](exclusive-thing.md "exclusive-thing.md") feature.

###### In this topic:

- [Connect/Disconnect events](#connect-disconnect "#connect-disconnect")
- [Connect attempt failure event](#connect-authfailure-event "#connect-authfailure-event")
- [Subscribe/Unsubscribe events](#subscribe-unsubscribe-events "#subscribe-unsubscribe-events")

## Connect/Disconnect events

###### Note

With AWS IoT Device Management fleet indexing, you can search for things, run aggregate queries, and create dynamic groups
based on thing Connect/Disconnect events. For more information, see [Fleet
indexing](iot-indexing.md "iot-indexing.md").

AWS IoT publishes a message to the following MQTT topics when a client connects or
disconnects:

- `$aws/events/presence/connected/`clientId``
  – A client connected to the message broker.
- `$aws/events/presence/disconnected/`clientId``
  – A client disconnected from the message broker.

The following is a list of JSON elements that are contained in the
connection/disconnection messages published to the
`$aws/events/presence/connected/`clientId``
topic.

**clientId**

The client ID of the connecting or disconnecting client.

###### Note

Client IDs that contain # or + do not receive lifecycle
events.

**thingName**

The name of your IoT thing. `thingName` will only be
included if the client is connecting using the [exclusive thing](exclusive-thing.md "exclusive-thing.md") feature.

**clientInitiatedDisconnect**

True if the client initiated the disconnect. Otherwise, false. Found
in disconnect messages only.

**disconnectReason**

The reason why the client is disconnecting. Found in disconnect
messages only. The following table contains valid values and whether the
broker will send [Last Will and Testament (LWT)
messages](mqtt.md#mqtt-lwt "mqtt.md#mqtt-lwt") when the disconnection occurs.

| Disconnect reason             | Description                                                                                                                                                                                                                                                                     | The broker will send the LWT messages |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `AUTH_ERROR`                  | The client failed to authenticate or authorization<br>failed.                                                                                                                                                                                                                   | Yes1                                  |
| `CLIENT_INITIATED_DISCONNECT` | The client indicates that it will disconnect. The<br>client can do this by sending either a MQTT<br>`DISCONNECT` control packet or a<br>`Close frame` if the client is using a<br>WebSocket connection.                                                                         | No                                    |
| `CLIENT_ERROR`                | The client did something wrong that causes it to<br>disconnect. For example, a client will be disconnected<br>for sending more than 1 MQTT `CONNECT` packet<br>on the same connection or if the client attempts to<br>publish with a payload that exceeds the payload<br>limit. | Yes                                   |
| `CONNECTION_LOST`             | The client-server connection is cut off. This can<br>happen during a period of high network latency or when<br>the internet connection is lost.                                                                                                                                 | Yes                                   |
| `DUPLICATE_CLIENTID`          | The client is using a client ID that is already in<br>use. In this case, the client that is already connected<br>will be disconnected with this disconnect<br>reason.                                                                                                           | Yes                                   |
| `FORBIDDEN_ACCESS`            | The client is not allowed to be connected. For<br>example, a client with a denied IP address will fail to<br>connect.                                                                                                                                                           | Yes1                                  |
| `MQTT_KEEP_ALIVE_TIMEOUT`     | If there is no client-server communication for 1.5x<br>of the client's keep-alive time, the client is<br>disconnected.                                                                                                                                                          | Yes                                   |
| `SERVER_ERROR`                | Disconnected due to unexpected server issues.                                                                                                                                                                                                                                   | Yes                                   |
| `SERVER_INITIATED_DISCONNECT` | Server intentionally disconnects a client for<br>operational reasons.                                                                                                                                                                                                           | Yes                                   |
| `API_INITIATED_DISCONNECT`    | The client was disconnected using the `DeleteConnection` API.                                                                                                                                                                                                                   | Yes2                                  |
| `THROTTLED`                   | The client is disconnected for exceeding a throttling<br>limit.                                                                                                                                                                                                                 | Yes                                   |
| `WEBSOCKET_TTL_EXPIRATION`    | The client is disconnected because a WebSocket has<br>been connected longer than its time-to-live<br>value.                                                                                                                                                                     | Yes                                   |
| `CUSTOMAUTH_TTL_EXPIRATION`   | The client is disconnected because it has been<br>connected longer than the time-to-live value of its<br>custom authorizer.                                                                                                                                                     | Yes                                   |

1If the device has an active connection before receiving this error.

2To prevent Last Will and Testament (LWT) messages, set `preventWillMessage=true` to override the `DeleteConnection` API's default LWT sending behavior.

**eventType**

The type of event. Valid values are `connected` or
`disconnected`.

**ipAddress**

The IP address of the connecting client. This can be in IPv4 or IPv6
format. Found in connection messages only.

**principalIdentifier**

The credential used to authenticate. For TLS mutual authentication
certificates, this is the certificate ID. For other connections, this is
IAM credentials.

**sessionIdentifier**

A globally unique identifier in AWS IoT that exists for the life of the
session.

**timestamp**

An approximation of when the event occurred.

**versionNumber**

The version number for the lifecycle event. This is a monotonically
increasing long integer value for each client ID connection. The version
number can be used by a subscriber to infer the order of lifecycle
events.

###### Note

The connect and disconnect messages for a client connection have
the same version number.

The version number might skip values and is not guaranteed to be
consistently increasing by 1 for each event.

If a client is not connected for approximately one hour, the
version number is reset to 0. For persistent sessions, the version
number is reset to 0 after a client has been disconnected longer
than the configured time-to-live (TTL) for the persistent
session.

A connect message has the following structure.

```
{
    "clientId": "186b5",
    "thingName": "exampleThing",
    "timestamp": 1573002230757,
    "eventType": "connected",
    "sessionIdentifier": "00000000-0000-0000-0000-000000000000",
    "principalIdentifier": "12345678901234567890123456789012",
    "ipAddress": "192.0.2.0",
    "versionNumber": 0
}
```

A disconnect message has the following structure.

```
{
    "clientId": "186b5",
    "thingName": "exampleThing",
    "timestamp": 1573002340451,
    "eventType": "disconnected",
    "sessionIdentifier": "00000000-0000-0000-0000-000000000000",
    "principalIdentifier": "12345678901234567890123456789012",
    "clientInitiatedDisconnect": true,
    "disconnectReason": "CLIENT_INITIATED_DISCONNECT",
    "versionNumber": 0
}
```

### Handling client disconnections

The best practice is to always have a wait state implemented for lifecycle
events, including [Last Will and Testament (LWT)
messages](mqtt.md "mqtt.md"). When a disconnect message is received, your code should
wait a period of time and verify a device is still offline before taking action.
One way to do this is by using [SQS Delay Queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.md"). When a client receives a LWT or a lifecycle
event, you can enqueue a message (for example, for 5 seconds). When that message
becomes available and is processed (by Lambda or another service), you can first
check if the device is still offline before taking further action.

## Connect attempt failure event

AWS IoT publishes a message to the following MQTT topic when a client is not
authorized to connect or when a last will and testament is configured and the client
is not authorized to publish to that last will topic.

```
$aws/events/presence/connect_failed/`clientId`
```

The following is a list of JSON elements that are contained in the connect
authorization messages published to the
`$aws/events/presence/connect_failed/`clientId``
topic.

**clientId**

The client ID of the client that attempted and failed to
connect.

###### Note

Client IDs that contain # or + do not receive lifecycle
events.

**thingName**

The name of your IoT thing. `thingName` will only be
included if the client is connecting using the [exclusive
thing](exclusive-thing.md "exclusive-thing.md") feature.

**timestamp**

An approximation of when the event occurred.

**eventType**

The type of event. Valid value is `connect_failed`.

**connectFailureReason**

The reason why the connection fails. Valid value is
`AUTHORIZATION_FAILED`.

**principalIdentifier**

The credential used to authenticate. For TLS mutual authentication
certificates, this is the certificate ID. For other connections, this is
IAM credentials.

**sessionIdentifier**

A globally unique identifier in AWS IoT that exists for the life of the
session.

**ipAddress**

The IP address of the connecting client. This can be in IPv4 or IPv6
format. Found in connection messages only.

A connection failure message has the following structure.

```
{
    "clientId": "186b5",
    "thingName": "exampleThing",
    "timestamp": 1460065214626,
    "eventType": "connect_failed",
    "connectFailureReason": "AUTHORIZATION_FAILED",
    "principalIdentifier": "12345678901234567890123456789012",
    "sessionIdentifier": "00000000-0000-0000-0000-000000000000",
    "ipAddress" : "192.0.2.0"
}
```

## Subscribe/Unsubscribe events

AWS IoT publishes a message to the following MQTT topic when a client subscribes or
unsubscribes to an MQTT topic:

```
$aws/events/subscriptions/subscribed/`clientId`
```

or

```
$aws/events/subscriptions/unsubscribed/`clientId`
```

Where `clientId` is the MQTT client ID that connects to the AWS IoT
message broker.

The message published to this topic has the following structure:

```
{
    "clientId": "186b5",
    "thingName": "exampleThing",
    "timestamp": 1460065214626,
    "eventType": "subscribed" | "unsubscribed",
    "sessionIdentifier": "00000000-0000-0000-0000-000000000000",
    "principalIdentifier": "12345678901234567890123456789012",
    "topics" : ["foo/bar","device/data","dog/cat"]
}
```

The following is a list of JSON elements that are contained in the subscribed and
unsubscribed messages published to the
`$aws/events/subscriptions/subscribed/`clientId``
 and
 `$aws/events/subscriptions/unsubscribed/`clientId``
topics.

clientId

The client ID of the subscribing or unsubscribing client.

###### Note

Client IDs that contain # or + do not receive lifecycle
events.

thingName

The name of your IoT thing. `thingName` will only be
included if the client is connecting using the [exclusive thing](exclusive-thing.md "exclusive-thing.md") feature.

eventType

The type of event. Valid values are `subscribed` or
`unsubscribed`.

principalIdentifier

The credential used to authenticate. For TLS mutual authentication
certificates, this is the certificate ID. For other connections, this is
IAM credentials.

sessionIdentifier

A globally unique identifier in AWS IoT that exists for the life of the
session.

timestamp

An approximation of when the event occurred.

topics

An array of the MQTT topics to which the client has subscribed.

###### Note

Lifecycle messages might be sent out of order. You might receive duplicate
messages.
