

# Lifecycle events
<a name="life-cycle-events"></a>

AWS IoT can publish lifecycle events on the MQTT topics. These events are available by default and they can't be disabled.

**Note**  
Lifecycle messages might be sent out of order. You might receive duplicate messages.  
`thingName` will only be included if the client is connecting using the [exclusive thing](exclusive-thing.md) feature.

**Topics**
+ [Connect/Disconnect events](#connect-disconnect)
+ [Connect attempt failure event](#connect-authfailure-event)
+ [Subscribe/Unsubscribe events](#subscribe-unsubscribe-events)

## Connect/Disconnect events
<a name="connect-disconnect"></a>

**Note**  
With AWS IoT Device Management fleet indexing, you can search for things, run aggregate queries, and create dynamic groups based on thing Connect/Disconnect events. For more information, see [ Fleet indexing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html).

AWS IoT publishes a message to the following MQTT topics when a client connects or disconnects:
+ `$aws/events/presence/connected/{{clientId}}` – A client connected to the message broker.
+ `$aws/events/presence/disconnected/{{clientId}}` – A client disconnected from the message broker.

The following is a list of JSON elements that are contained in the connection/disconnection messages published to the `$aws/events/presence/connected/{{clientId}}` topic.

**clientId**  
The client ID of the connecting or disconnecting client.  
Client IDs that contain \# or \+ do not receive lifecycle events.

**thingName**  
The name of your IoT thing. `thingName` will only be included if the client is connecting using the [exclusive thing](exclusive-thing.md) feature.

**clientInitiatedDisconnect**  
True if the client initiated the disconnect. Otherwise, false. Found in disconnect messages only.

**disconnectReason**  
The reason why the client is disconnecting. Found in disconnect messages only. The following table contains valid values and whether the broker will send [Last Will and Testament (LWT) messages](mqtt.md#mqtt-lwt) when the disconnection occurs.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html)
1If the device has an active connection before receiving this error.  
2To prevent Last Will and Testament (LWT) messages, set `preventWillMessage=true` to override the `DeleteConnection` API's default LWT sending behavior.

**eventType**  
The type of event. Valid values are `connected` or `disconnected`. 

**ipAddress**  
The IP address of the connecting client. This can be in IPv4 or IPv6 format. Found in connection messages only. 

**principalIdentifier**  
The credential used to authenticate. For TLS mutual authentication certificates, this is the certificate ID. For other connections, this is IAM credentials.

**sessionIdentifier**  
A globally unique identifier in AWS IoT that exists for the life of the session.

**timestamp**  
An approximation of when the event occurred.

**versionNumber**  
The version number for the lifecycle event. This is a monotonically increasing long integer value for each client ID connection. The version number can be used by a subscriber to infer the order of lifecycle events.  
The connect and disconnect messages for a client connection have the same version number.  
The version number might skip values and is not guaranteed to be consistently increasing by 1 for each event.  
If a client is not connected for approximately one hour, the version number is reset to 0. For persistent sessions, the version number is reset to 0 after a client has been disconnected longer than the configured time-to-live (TTL) for the persistent session.

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
<a name="reconnect"></a>

The best practice is to always have a wait state implemented for lifecycle events, including [Last Will and Testament (LWT) messages](mqtt.md). When a disconnect message is received, your code should wait a period of time and verify a device is still offline before taking action. One way to do this is by using [SQS Delay Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html). When a client receives a LWT or a lifecycle event, you can enqueue a message (for example, for 5 seconds). When that message becomes available and is processed (by Lambda or another service), you can first check if the device is still offline before taking further action.

## Connect attempt failure event
<a name="connect-authfailure-event"></a>

AWS IoT publishes a message to the following MQTT topic when a client is not authorized to connect or when a last will and testament is configured and the client is not authorized to publish to that last will topic.

```
$aws/events/presence/connect_failed/{{clientId}}
```

The following is a list of JSON elements that are contained in the connect authorization messages published to the `$aws/events/presence/connect_failed/{{clientId}}` topic.

**clientId**  
The client ID of the client that attempted and failed to connect.  
Client IDs that contain \# or \+ do not receive lifecycle events.

**thingName**  
The name of your IoT thing. `thingName` will only be included if the client is connecting using the [exclusive thing](exclusive-thing.md) feature.

**timestamp**  
An approximation of when the event occurred.

**eventType**  
The type of event. Valid value is `connect_failed`.

**connectFailureReason**  
The reason why the connection fails. Valid value is `AUTHORIZATION_FAILED`.

**principalIdentifier**  
The credential used to authenticate. For TLS mutual authentication certificates, this is the certificate ID. For other connections, this is IAM credentials.

**sessionIdentifier**  
A globally unique identifier in AWS IoT that exists for the life of the session.

**ipAddress**  
The IP address of the connecting client. This can be in IPv4 or IPv6 format. Found in connection messages only.

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
<a name="subscribe-unsubscribe-events"></a>

AWS IoT publishes a message to the following MQTT topic when a client subscribes or unsubscribes to an MQTT topic:

```
$aws/events/subscriptions/subscribed/{{clientId}}
```

 or 

```
$aws/events/subscriptions/unsubscribed/{{clientId}}
```

Where `clientId` is the MQTT client ID that connects to the AWS IoT message broker.

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

The following is a list of JSON elements that are contained in the subscribed and unsubscribed messages published to the `$aws/events/subscriptions/subscribed/{{clientId}}` and `$aws/events/subscriptions/unsubscribed/{{clientId}}` topics.

clientId  
The client ID of the subscribing or unsubscribing client.  
Client IDs that contain \# or \+ do not receive lifecycle events.

thingName  
The name of your IoT thing. `thingName` will only be included if the client is connecting using the [exclusive thing](exclusive-thing.md) feature.

eventType  
The type of event. Valid values are `subscribed` or `unsubscribed`. 

principalIdentifier  
The credential used to authenticate. For TLS mutual authentication certificates, this is the certificate ID. For other connections, this is IAM credentials.

sessionIdentifier  
A globally unique identifier in AWS IoT that exists for the life of the session.

timestamp  
An approximation of when the event occurred.

topics  
An array of the MQTT topics to which the client has subscribed.

**Note**  
Lifecycle messages might be sent out of order. You might receive duplicate messages.