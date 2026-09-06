

# Managed Integrations notifications
<a name="managedintegrations-notifications"></a>

Managed Integrations notifications deliver updates and key insights from devices. Notifications include connector events, device commands, lifecycle events, OTA (Over-the-Air) updates, and error reports. These insights provide actionable information to create automated workflows, take immediate actions, or store event data for troubleshooting.

Currently, only Amazon Kinesis data streams are supported as a destination for managed integrations notifications. You will first need to set up an Amazon Kinesis data stream and allow Managed Integrations access to the data stream before setting up notifications. 

## Set up Amazon Kinesis for notifications
<a name="kinesis-setup"></a>

**Contents**
+ [Step 1: Create an Amazon Kinesis data stream](#create-data-stream)
+ [Step 2: Create a permissions policy](#create-permissions-policy)
+ [Step 3: Navigate to the IAM dashboard and select Roles](#navigate-roles)
+ [Step 4: Use a Custom trust policy](#custom-trust-policy)
+ [Step 5: Apply your permissions policy](#apply-permissions-policy)
+ [Step 6: Enter a role name](#finalize-role)

To setup Amazon Kinesis for Managed Integrations notifications, follow these steps:

### Step 1: Create an Amazon Kinesis data stream
<a name="create-data-stream"></a>

An Amazon Kinesis Data Stream can ingest a large amount of data in real time, durably store the data, and make the data available for consumption by applications.

**To create an Amazon Kinesis data stream**
+ To create a Kinesis data stream, follow the steps outlined in [Create and manage Kinesis data streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html).

### Step 2: Create a permissions policy
<a name="create-permissions-policy"></a>

Create a permissions policy that allows Managed Integrations to access your Kinesis data stream.

**To create a permissions policy**
+ To create a permissions policy, copy the policy below and follow the steps outlined in [Create policies using the JSON editor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-json-editor)

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Action": "kinesis:PutRecord",
              "Resource": "*",
              "Effect": "Allow"
          }
      ]
  }
  ```

------

### Step 3: Navigate to the IAM dashboard and select Roles
<a name="navigate-roles"></a>

Open the IAM dashboard and click **Roles**.

**To navigate to the IAM dashboard**
+ **Open the IAM dashboard and click Roles.**

  For more information, see [IAM role creation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *AWS Identity and Access Management* User Guide.

### Step 4: Use a Custom trust policy
<a name="custom-trust-policy"></a>

You can use a custom trust policy to grant Managed Integrations access to the Kinesis data stream.

**To use a custom trust policy**
+ **Create a new role and choose Custom trust policy. Click Next. **

  The following policy allows Managed Integrations to assume the role, and the `Condition` statement helps prevent confused deputy issues. 

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
                  "Service": "iotmanagedintegrations.amazonaws.com"
          },
              "Action": "sts:AssumeRole",
              "Condition": {
                  "StringEquals": {
                      "aws:SourceAccount": "{{123456789012}}"
              },
                  "ArnLike": {
                      "aws:SourceArn": "arn:aws:iotmanagedintegrations:{{ca-central-1}}:{{123456789012}}:*"
              }
          }
          }
      ]
  }
  ```

------

### Step 5: Apply your permissions policy
<a name="apply-permissions-policy"></a>

Add the permissions policy you created in step 2 to the role.

**To add a permissions policy**
+ **On the Add permissions page, search for and add the permissions policy you created in step 2. Click Next. **

### Step 6: Enter a role name
<a name="finalize-role"></a>
+ **Enter a role name and click Create role.**

## Set up Managed Integrations notifications
<a name="managedintegrations-notification-setup"></a>

**Topics**
+ [Step 1: Give user permissions to call the CreateDestination API](#user-permissions)
+ [Step 2: Call the CreateDestination API](#call-createdestination)
+ [Step 3: Call the CreateNotificationConfiguration API](#call-notification-config)

To setup Managed Integrations notifications, follow these steps:

### Step 1: Give user permissions to call the CreateDestination API
<a name="user-permissions"></a>
+ **Give user permissions to call the `CreateDestination` API**

   The following policy defines the requirements for the user to call the [CreateDestination](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateDestination.html) API.

   See [ Grant a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) in the *AWS Identity and Access Management* User Guide to get passrole permissions to managed integrations. 

------
#### [ JSON ]

****  

  ```
  {
        "Version":"2012-10-17",		 	 	 
        "Statement":[
           {
              "Effect":"Allow",
              "Action":"iam:PassRole",
              "Resource":"arn:aws:iam::{{123456789012}}:role/{{ROLE_CREATED_IN_PREVIOUS_STEP}}",
              "Condition":{
                 "StringEquals":{
                    "iam:PassedToService":"iotmanagedintegrations.amazonaws.com"
             }
          }
           },
           {
              "Effect":"Allow",
              "Action":"iotmanagedintegrations:CreateDestination",
              "Resource":"*"
           }
        ]
  }
  ```

------

### Step 2: Call the CreateDestination API
<a name="call-createdestination"></a>
+ **Call the `CreateDestination` API**

  After you have created your Amazon Kinesis data stream and stream access role, call the [CreateDestination](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateDestination.html) API to create your notification destination where the notifications will be routed to. For the `DeliveryDestinationArn` parameter, use the `arn` from your new Amazon Kinesis data stream.

  ```
  {
      "DeliveryDestinationArn": "Your Kinesis arn"
      "DeliveryDestinationType": "KINESIS"
      "Name": "DestinationName"
      "ClientToken": {{"string"}}
      "RoleArn": "arn:aws:iam::{{accountID}}:role/{{ROLE_CREATED_IN_PREVIOUS_STEP}}"
  }
  ```
**Note**  
`ClientToken` is an idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.

### Step 3: Call the CreateNotificationConfiguration API
<a name="call-notification-config"></a>
+ **Call the `CreateNotificationConfiguration` API**

  Lastly, use the [CreateNotificationConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateNotificationConfiguration.html) API to create the notification configuration that routes the chosen event types to your destination represented by the Kinesis data stream. In the `DestinationName` parameter, use the same destination name as when you initially called the `CreateDestination` API.

  ```
  {
      "EventType": "DEVICE_EVENT"
      "DestinationName" // This name has to be identical to the name in createDestination API
      "ClientToken": {{"string"}}
  }
  ```

## Event types monitored with Managed Integrations
<a name="managedintegrations-notification-listevents"></a>

The following are the event types monitored with Managed Integrations notifications:
+ `DEVICE_COMMAND`
  + The status of the [SendManagedThingCommand](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_SendManagedThingCommand.html) API command. Valid values are either `succeeded` or `failed`.

    ```
    {
                  "version":"0",
                  "messageId":"6a7e8feb-b491-4cf7-a9f1-bf3703467718",
                  "messageType":"DEVICE_COMMAND",
                  "source":"aws.iotmanagedintegrations",
                  "customerAccountId":"123456789012",
                  "timestamp":"1731623291671",
                  "region":"ca-central-1",
                  "resources":[
                        "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/6a7e8feb-b491-4cf7-a9f1-bf3703467718"
                  ],
                  "payload":{
                    "traceId":"1234567890abcdef0",
                    "receivedAt":"2017-12-22T18:43:48Z",
                    "executedAt":"2017-12-22T18:43:48Z",
                    "result":"failed"
                  }
    }
    ```
+ `DEVICE_COMMAND_REQUEST`
  + The command request from Web Real-Time Communication (WebRTC).

    The WebRTC standard allows communication between two peers. These peers can transmit real-time video, audio, and arbitrary data. Managed Integrations supports WebRTC to enable these types of streaming between a customer mobile application and an end-user's device. For more information on the WebRTC standard, see [WebRTC](https://webrtc.org/).

    ```
    {
                  "version":"0",
                  "messageId":"6a7e8feb-b491-4cf7-a9f1-bf3703467718",
                  "messageType":"DEVICE_COMMAND_REQUEST",
                  "source":"aws.iotmanagedintegrations",
                  "customerAccountId":"123456789012",
                  "timestamp":"1731623291671",
                  "region":"ca-central-1",
                  "resources":[
                      "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/6a7e8feb-b491-4cf7-a9f1-bf3703467718"
                  ],
                  "payload":{
                    "endpoints":[{
                      "endpointId":"1",
                      "capabilities":[{
                        "id":"aws.DoorLock",
                        "name":"Door Lock",
                        "version":"1.0"
                      }]
                    }]
                  }
    }
    ```
+ `DEVICE_DISCOVERY_STATUS`
  + The discovery status of the device.

    ```
    {
          "version":"0",
          "messageId":"6a7e8feb-b491-4cf7-a9f1-bf3703467718",
          "messageType":"DEVICE_DISCOVERY_STATUS",
          "source":"aws.iotmanagedintegrations",
          "customerAccountId":"123456789012",
          "timestamp":"2017-12-22T18:43:48Z",
          "region":"ca-central-1",
          "resources":[
            "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/6a7e8feb-b491-4cf7-a9f1-bf3703467718"
          ],
          "payload":{
            "deviceCount": 1,
            "deviceDiscoveryId": "123",
            "status": "SUCCEEDED"
          }
    }
    ```
+ `DEVICE_EVENT`
  + A notification of a device event occurring.

    ```
    {
          "version":"1.0",
          "messageId":"2ed545027bd347a2b855d28f94559940",
          "messageType":"DEVICE_EVENT",
          "source":"aws.iotmanagedintegrations",
          "customerAccountId":"123456789012",
          "timestamp":"1731630247280",
          "resources":[
            "/quit/1b15b39992f9460ba82c6c04595d1f4f"
          ],
          "payload":{
            "iotMiArrivalTimestamp":"2026-06-26T21:28:14.697Z",
            "endpoints":[{
              "endpointId":"1",
              "capabilities":[{
                "id":"aws.DoorLock",
                "name":"Door Lock",
                "version":"1.0",
                "properties":[{
                  "name":"ActuatorEnabled",
                  "value":"true"
                }]
              }]
            }]
          }
    }
    ```

    The `DEVICE_EVENT` payload contains the following fields:
    + `iotMiArrivalTimestamp`, String (ISO 8601): The timestamp indicating when the device event was published by the device into Managed Integrations. Use this field to determine the latency between when the event was generated by the device and when Managed Integrations received it.
    + `endpoints`: The list of device endpoints and their updated capability properties.

    The `timestamp` field in the outer message envelope indicates when the notification was delivered to Kinesis. The `iotMiArrivalTimestamp` in the payload indicates when the event arrived into Managed Integrations. These two timestamps can differ if there is processing latency between event arrival and the notification delivery.
+ `DEVICE_LIFE_CYCLE`

  Reflects changes in status of device life cycle (this includes onboarding status and connected/disconnected status).
  + Onboarding status update event.

    ```
    { 
          "version": "1.0.0", 
          "messageId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
          "messageType": "DEVICE_LIFE_CYCLE",
          "source": "aws.iotmanagedintegrations",
          "customerAccountId": "123456789012",
          "timestamp": "2024-11-14T19:55:57.568284645Z",
          "region": "ca-central-1",
          "resources": [
            "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
            ],
          "payload": {
            "deviceDetails": {
              "id": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
              "arn": "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
              "createdAt": "2024-11-14T19:55:57.515841147Z",
              "updatedAt": "2024-11-14T19:55:57.515841559Z"
            },
            "status": "UNCLAIMED" 
          } 
    }
    ```
  + Device connected status event.

    ```
    {
        "version": "1.0",
        "messageId": "a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6",
        "messageType": "DEVICE_LIFE_CYCLE",
        "source": "aws.iotmanagedintegrations",
        "customerAccountId": "123456789012",
        "timestamp": "2024-11-14T19:55:57.568284645Z",
        "region": "ca-central-1",
        "resources": [
            "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
        ],
        "payload": {
            "managedThingId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            "managedThingArn": "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            "clientId": "iotmi-example-client-id",
            "timestamp": "1768000475344",
            "eventType": "connected",
            "sessionIdentifier": "q1w2e3r4-t5y6-u7i8-o9p0-a1s2d3f4g5h6",
            "principalIdentifier": "z1x2c3v4b5n6m7a8s9d0f1g2h3j4k5l6p7o8i9u0y1t2r3e4w5q6a7z8x9c0v1b2",
            "ipAddress": "192.0.2.100",
            "versionNumber": "0"
        }
    }
    ```
  + Device disconnected status event.

    ```
    {
        "version": "1.0",
        "messageId": "b2n3m4a5-s6d7-f8g9-h0j1-k2l3z4x5c6v7",
        "messageType": "DEVICE_LIFE_CYCLE",
        "source": "aws.iotmanagedintegrations",
        "customerAccountId": "123456789012",
        "timestamp": "2024-11-14T19:55:57.568284645Z",
        "region": "ca-central-1",
        "resources": [
            "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
        ],
        "payload": {
            "managedThingId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            "managedThingArn": "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            "clientId": "iotmi-example-client-id",
            "timestamp": "1768000492431",
            "eventType": "disconnected",
            "sessionIdentifier": "p9o8i7u6-y5t4-r3e2-w1q0-m9n8b7v6c5x4",
            "principalIdentifier": "a1s2d3f4g5h6j7k8l9z0x1c2v3b4n5m6q7w8e9r0t1y2u3i4o5p6a7s8d9f0g1h2",
            "versionNumber": "0",
            "disconnectReason": "CLIENT_INITIATED_DISCONNECT"
        }
    }
    ```
+ `DEVICE_OTA`
  + A device OTA notification.

    ```
    {
        "version": "1.0.0",
        "messageId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "messageType": "DEVICE_OTA",
        "source": "aws.iotmanagedintegrations",
        "customerAccountId": "123456789012",
        "timestamp": "2024-11-14T19:55:57.568284645Z",
        "region": "ca-central-1",
        "resources": [
            "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7",
            "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8"
        ],
        "payload": {
            "operation": "CREATE_OTA",
            "otaTaskId": "ota-job-abc123def456",
            "status": "IN_PROGRESS",
            "otaType": "ONE_TIME"
        }
    }
    ```
+ `DEVICE_STATE`
  + A notification when the state of a device has been updated.

    ```
    { 
          "messageType": "DEVICE_STATE",
          "source": "aws.iotmanagedintegrations",
          "customerAccountId": "123456789012",
          "timestamp": "1731623291671",
          "resources": [
            "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:managed-thing/61889008880012345678"
          ],
          "payload": {
            "addedStates": {
              "endpoints": [{
                "endpointId": "nonEndpointId",
                "capabilities": [{
                  "id": "aws.OnOff",
                  "name": "On/Off",
                  "version": "1.0",
                  "properties": [{
                    "name": "OnOff",
                    "value": {
                      "propertyValue": "\"onoff\"",
                      "lastChangedAt": "2024-06-11T01:38:09.000414Z"
                    }
                  }
                ]}
              ]}
            ]}
          } 
    }
    ```
+ `ACCOUNT_ASSOCIATION`
  + A notification when an account association state changes to IN\_PROGRESS.

    ```
    {
        "version": "1.0.0",
        "messageId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "messageType": "ACCOUNT_ASSOCIATION",
        "source": "aws.iotmanagedintegrations",
        "customerAccountId": "123456789012",
        "timestamp": "2026-01-20T23:59:34.009284802Z",
        "region": "ca-central-1",
        "resources": ["arn:aws:iotmanagedintegrations:ca-central-1:123456789012:account-association/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"],
        "payload": {
            "traceId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            "logLevel": "INFO",
            "resourceType": "account-association",
            "resourceId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            "connectorDestinationId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            "associationArn": "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:account-association/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
            "state": "ASSOCIATION_IN_PROGRESS",
            "isServiceError": false,
            "isCustomerError": false,
            "details": "AccountAssociation State is updated to IN_PROGRESS during StartAccountAssociationRefresh"
        }
    }
    ```
  + A notification when an account association completes successfully.

    ```
    {
        "version": "1.0.0",
        "messageId": "b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7",
        "messageType": "ACCOUNT_ASSOCIATION",
        "source": "aws.iotmanagedintegrations",
        "customerAccountId": "123456789012",
        "timestamp": "2026-01-20T23:59:44.672304821Z",
        "region": "ca-central-1",
        "resources": ["arn:aws:iotmanagedintegrations:ca-central-1:123456789012:account-association/b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7"],
        "payload": {
            "traceId": "b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7",
            "logLevel": "INFO",
            "resourceType": "account-association",
            "resourceId": "b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7",
            "connectorDestinationId": "b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7",
            "associationArn": "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:account-association/b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7",
            "state": "ASSOCIATION_SUCCEEDED",
            "isServiceError": false,
            "isCustomerError": false,
            "details": "AccountAssociation has completed successfully"
        }
    }
    ```
+ `CONNECTOR_ERROR_REPORT`
  + This notification is sent when a cloud-to-cloud (C2C) connector reports an error while processing a request on your behalf, such as a command or device discovery that returned a non-success response.

    ```
    {
        "version": "1.0.0",
        "messageId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "messageType": "CONNECTOR_ERROR_REPORT",
        "source": "aws.iotmanagedintegrations",
        "customerAccountId": "123456789012",
        "timestamp": "2026-01-20T23:59:34.009284802Z",
        "region": "ca-central-1",
        "resources": [
            "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:account-association/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
        ],
        "payload": {
            "statusCode": 0,
            "resourceType": "account-association",
            "resourceId": [
                "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
            ],
            "associationArn": [
                "arn:aws:iotmanagedintegrations:ca-central-1:123456789012:account-association/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
            ],
            "connectorDestinationId": "b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7",
            "connectorDeviceId": "connectorDeviceId11597664a",
            "operation": "AWS.SendCommand",
            "operationVersion": "1.0",
            "traceId": "f4be7a5d55d34cc=_1",
            "logLevel": "ERROR",
            "message": "AWS.SendCommand operation failed during asynchronous invocation of the connector: Connector response exception: responseCode=xxx, responseMessage=Mocking a ValidationException with error code xxx",
            "managedThingId": "c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8"
        }
    }
    ```

    The `managedThingId` field is included when it can be resolved for the request. Fields without a value are omitted from the payload.