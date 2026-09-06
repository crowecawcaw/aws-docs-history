

# Device connectivity status queries
<a name="device-connectivity-status"></a>

AWS IoT Fleet Indexing supports individual device connectivity querying, allowing you to efficiently retrieve connectivity status and related metadata for specific devices. This feature complements existing fleet-wide indexing and querying capabilities.

## How it works
<a name="w2aac37c21b5"></a>

Device connectivity query support can be used for optimized single-device connectivity status retrieval. This API provides low-latency, high-throughput access to the most recent device-specific connectivity information. Once you enable connectivity indexing you will have access to this query API which will be charged as standard queries. For more information, see [AWS IoT Device Management pricing](https://aws.amazon.com/iot-device-management/pricing/#:~:text=Search%20queries%20(per%2010%2C000%20queries))

## Features
<a name="w2aac37c21b7"></a>

With device connectivity query support, you can:

1. Query the current connectivity state (connected or disconnected) for a given device using its `thingName`.

1. Retrieve additional connectivity metadata, including:

   1. Disconnect reason

   1. Timestamps for the most recent connect or disconnect event.

   1. Session information including the keep-alive duration

   1. Socket level session information including IP address, port, and VPC endpoint ID. This information is available only when the following conditions are met:

      1. You enable this option in fleet indexing configuration settings.

      1. You have the corresponding permission in the IAM policy when invoking the API.

**Note**  
Fleet indexing indexes the connectivity status for a device whose connection `clientId` is the same as the `thingName` of a registered thing in [Registry](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html). 

## Benefits
<a name="w2aac37c21b9"></a>

1. **Low latency:** Reflects the most recent device connectivity state and offers low latency to reflect connection state changes from IoT Core. IoT Core determines a device as disconnected either as soon as it receives a disconnect request from the device or in case of a device disconnecting without sending a disconnect request. IoT core will wait 1.5x of the configured keep-alive time before the client is determined to be disconnected. The Connectivity status API will reflect these changes typically under one second after IoT Core determines a device’s connected state change.

1. **High throughput:** Supports 350 Transactions Per Second (TPS) by default, and can be adjustable to higher upon request.

1. **Data retention: **Stores event data indefinitely when Fleet Indexing (FI) ConnectivityIndexing mode is enabled and the thing is not deleted. If you disable Connectivity Indexing, the records will not be retained.

**Note**  
If connectivity status indexing was enabled before the launch of this API, Fleet Indexing begins tracking connectivity status changes after the API launch and reflects the updated status based on those changes.

## Prerequisites
<a name="w2aac37c21c11"></a>

To use device connectivity query support:

1. [Set up an AWS account](https://docs.aws.amazon.com/iot/latest/developerguide/setting-up.html)

1. Onboard and register devices to AWS IoT Core in your preferred region

1. [Enable Fleet Indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html) with Connectivity indexing. Optional: Opt-in to receive socket level information by enabling the `includeSocketInformation` option.

**Note**  
No additional setup is required if you already have connectivity indexing enabled.

For detailed setup instructions, refer to the [AWS IoT Developer Guide](https://docs.aws.amazon.com/iot/latest/developerguide/setting-up.html)

## Example
<a name="w2aac37c21c13"></a>

**CLI Command:**

```
aws iot get-thing-connectivity-data --include-socket-information --thing-name myThingName
```

**Response:**

```
{
   "thingName": "myThingName",
   "connected": true,
   "timestamp": "2024-12-19T10:00:00.000000-08:00",
   "disconnectReason": "NONE",
   "sourceIp": "192.0.2.1",
   "sourcePort": 52123,
   "targetIp": "198.51.100.1",
   "targetPort": 8883,
   "vpcEndpointId": "vpce-1234567890abcdef0",
   "keepAliveDuration": 60,
   "cleanSession": true,
   "clientId": "myThingName"
}
```

**API Parameters** 
+ `thingName`: The name of the device registered in AWS IoT Registry. This must match the `clientId` used to connect to AWS IoT Core.
+ `includeSocketInformation`: The `includeSocketInformation` parameter controls whether socket-level network information is included in the API response. When set to true, the response includes the following fields: `sourceIp, sourcePort, targetIp, targetPort, vpcEndpointId`. When `includeSocketInformation` is not specified or set to false, these socket fields are excluded from the response. To restrict specific IAM users from accessing socket information you will need to specify this in their IAM policy by setting the `includeSocketInformation` condition key to be false 

**Response Fields** 
+ `thingName`: The name of the device registered in AWS IoT Registry. This must match the `clientId` used to connect to AWS IoT Core.
+ `connected`: The boolean value true indicating this device is currently connected.
+ `disconnectReason`: Reason for disconnect. Will be `NONE` for a connected device and `UNKNOWN` for a device which has never been connected. For a disconnected device, this will indicate if the disconnection was client initiated, server initiated, due to authentication/authorization issues or due to network issues. For disconnect reason codes, see [LifeCycleEvents ](https://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html)
+ `timestamp`: The timestamp representing the device’s most recent connect or disconnect event.
+ `clientId`: The clientId of the MQTT client. 
+ `keepAliveDuration`: The keep-alive interval in seconds that the client specified when establishing the connection. This determines how frequently the client sends keep-alive messages to maintain the connection. 
+ `cleanSession`: Indicates whether the client is using a clean session. 
+ `sessionExpiry`: The persistent session expiry configuration the client specified when establishing the connection. This determines how long a session will remain active after the client disconnects. 
+ `sourceIp`: The IP address of the client that initiated the connection. Only returned if `includeSocketInformation` is set to be true and user is authorized to retrieve this information. 
+ `sourcePort`: The port number used by the client for the connection. Only returned if `includeSocketInformation` is set to be true and user is authorized to retrieve this information. 
+ `targetIp`: The IP address where the connection request was made to. Only returned if `includeSocketInformation` is set to be true and user is authorized to retrieve this information 
+ `targetPort`: The port number of the AWS IoT Core endpoint that the client connected to. Only returned if `includeSocketInformation` is set to be true and user is authorized to retrieve this information. 
+ `vpcEndpointId`: The ID of the VPC endpoint that the client connected through, if applicable. Only returned if `includeSocketInformation` is set to be true and user is authorized to retrieve this information. 

**Required Permissions**

 To use the GetThingConnectivityData API, you need the following IAM permission 

`iot:GetThingConnectivityData`

 You can scope this permission to specific things using resource based policies. Use the `iot:IncludeSocketInformation` condition to implement granular access control on socket information. The policy example below demonstrates a scenario where you deny the user access to socket information. Please note that this example works when it is the sole policy granting access to the action GetThingConnectivityData. 

**Authorization Policy Examples**

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [ 
  { 
    "Effect": "Allow",
    "Action": [ "iot:GetThingConnectivityData" ],
    "Resource": [ "arn:aws:iot:us-east-1:123456789012:thing/*"],
    "Condition": { 
      "Bool": { 
        "iot:IncludeSocketInformation": "false" 
      } 
    } 
  }] 
}
```