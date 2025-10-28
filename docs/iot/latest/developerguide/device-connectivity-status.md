# Device connectivity status queries

AWS IoT Fleet Indexing supports individual device connectivity querying, allowing you to
efficiently retrieve connectivity status and related metadata for specific devices. This
feature complements existing fleet-wide indexing and querying capabilities.

## How it works

Device connectivity query support can be used for optimized single-device connectivity
status retrieval. This API provides low-latency, high-throughput access to the most recent
device-specific connectivity information. Once you enable connectivity indexing you will
have access to this query API which will be charged as standard queries. For more
information, see [AWS IoT Device Management pricing](<https://aws.amazon.com/iot-device-management/pricing/#:~:text=Search%20queries%20(per%2010%2C000%20queries)> "https://aws.amazon.com/iot-device-management/pricing/#:~:text=Search%20queries%20(per%2010%2C000%20queries)")

## Features

With device connectivity query support, you can:

1. Query the current connectivity state (connected or disconnected) for a given device
   using its `thingName`.
2. Retrieve additional connectivity metadata, including:
   1. Disconnect reason
   2. Timestamps for the most recent connect or disconnect event.

###### Note

Fleet indexing indexes the connectivity status for a device whose connection
`clientId` is the same as the `thingName` of a registered thing in
[Registry.](thing-registry.md "thing-registry.md")

## Benefits

1. **Low latency:** Reflects the most recent device
   connectivity state and offers low latency to reflect connection state changes from IoT
   Core. IoT Core determines a device as disconnected either as soon as it receives a
   disconnect request from the device or in case of a device disconnecting without sending
   a disconnect request. IoT core will wait 1.5x of the configured keep-alive time before
   the client is determined to be disconnected. The Connectivity status API will reflect
   these changes typically under one second after IoT Core determines a device’s connected
   state change.
2. **High throughput:** Supports 350 Transactions Per
   Second (TPS) by default, and can be adjustable to higher upon request.
3. **Data retention:** Stores event data
   indefinitely when Fleet Indexing (FI) ConnectivityIndexing mode is enabled and the thing
   is not deleted. If you disable Connectivity Indexing, the records will not be
   retained.

###### Note

If connectivity status indexing was enabled before the launch of this API, Fleet Indexing begins tracking connectivity status changes after the API launch and reflects the updated status based on those changes.

## Prerequisites

To use device connectivity query support:

1. [Set up an AWS account](setting-up.md "setting-up.md")
2. Onboard and register devices to AWS IoT Core in your preferred region
3. [Enable
   Fleet Indexing](managing-index.md "managing-index.md") with Connectivity indexing

###### Note

No additional setup is required if you already have connectivity indexing
enabled

For detailed setup instructions, refer to the [AWS IoT
Developer Guide](setting-up.md "setting-up.md")

## Examples

```
aws iot get-thing-connectivity-data --thing-name myThingName
```

```

{
   "connected": true,
   "disconnectReason": "NONE",
   "thingName": "myThingName",
   "timestamp": "2024-12-19T10:00:00.000000-08:00"
}
```

- `thingName`: The name of the device as indicated by the request. This
  also matches the clientId used to connect to AWS IoT Core.
- `disconnectReason`: Reason for disconnect. Will be NONE for a connected
  device.
- `connected`: The boolean value true indicating this device is currently
  connected.
- `timestamp`: The timestamp representing the device’s
  most recent disconnect in milliseconds.

```
aws iot get-thing-connectivity-data --thing-name myThingName
```

```

{
   "connected": false,
   "disconnectReason": "CLIENT_INITIATED_DISCONNECT",
   "thingName": "myThingName",
   "timestamp": "2024-12-19T10:30:00.000000-08:00"
}
```

- `thingName`: The name of the device as indicated by the request. This
  also matches the clientId used to connect to AWS IoT Core.
- `disconnectReason`: Reason for disconnect is CLIENT_INITIATED_DISCONNECT
  indicating the client indicated to AWS IoT Core that it would disconnect.
- `connected`: The boolean value false indicating this device is currently
  disconnected.
- `timestamp`: The timestamp representing the device’s
  most recent disconnect in milliseconds.

```
aws iot get-thing-connectivity-data --thing-name neverConnectedThing
```

```

{
   "connected": false,
   "disconnectReason": "UNKNOWN",
   "thingName": "neverConnectedThing"
}
```

- `thingName`: The name of the device as indicated by the request. This
  also matches the clientId used to connect to AWS IoT Core.
- `disconnectReason`: Reason for disconnect. Will be “UNKNOWN” for a device
  which has never been connected or for which Fleet Indexing does not have the last
  disconnect reason stored.
- `connected`: The boolean value false indicating this device is currently
  disconnected.
- `timestamp`: The timestamp is not returned for a device which has never been connected or for which Fleet Indexing does not have the last timestamp stored.
