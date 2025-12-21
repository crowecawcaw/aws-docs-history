# Simple setup to onboard and operate

devices

Set up your devices to be onboarded to your managed integrations hub by creating a managed thing and
connecting it to your hub. This section describes the steps to complete the device
onboarding process using simple setup.

## Prerequisites

Complete these steps before attempting to onboard a device:

- Onboard a hub device to the managed integrations hub.
- Install the latest version of AWS CLI from the [Managed Integrations AWS CLI Command Reference](../../../cli/latest/reference/iot-managed-integrations.md "../../../cli/latest/reference/iot-managed-integrations.md")
- Subscribe to [DEVICE_LIFE_CYCLE](managedintegrations-notifications.md#managedintegrations-notification-setup "managedintegrations-notifications.md#managedintegrations-notification-setup") event notifications.

###### Setup steps

- [Step 1: Create a credential locker](#managedintegrations-sdk-v2-cookbook-credential-locker "#managedintegrations-sdk-v2-cookbook-credential-locker")
- [Step 2: Add the credential locker to your hub](#managedintegrations-sdk-v2-cookbook-add-to-hub "#managedintegrations-sdk-v2-cookbook-add-to-hub")
- [Step 3: Create a managed thing with credentials.](#managedintegrations-sdk-v2-cookbook-ss-create-managed-thing "#managedintegrations-sdk-v2-cookbook-ss-create-managed-thing")
- [Step 4: Plug in the device and check its status.](#managedintegrations-sdk-v2-cookbook-ss-check-device-status "#managedintegrations-sdk-v2-cookbook-ss-check-device-status")
- [Step 5: Get Device
  Capabilities](#managedintegrations-sdk-v2-cookbook-ss-check-device-capabilities "#managedintegrations-sdk-v2-cookbook-ss-check-device-capabilities")
- [Step 6: Send a
  command to the managed thing](#managedintegrations-sdk-v2-cookbook-ss-control-device "#managedintegrations-sdk-v2-cookbook-ss-control-device")
- [Step 7: Remove the managed
  thing from your hub](#managedintegrations-sdk-v2-cookbook-clean-up "#managedintegrations-sdk-v2-cookbook-clean-up")

## Step 1: Create a credential locker

Create a credential locker for your device.

###### To create a credential locker

- Use the `create-credential-locker` command. Executing this command will trigger the creation of all
  manufacturing resources including the Wi-Fi setup key pair and device certificate.

**create-credential-locker
example**

```
aws iot-managed-integrations create-credential-locker \
  --name `"DEVICE_NAME"`
```

**Response:**

```
{
  "Id": `"LOCKER_ID"`
  "Arn": "arn:aws:iotmanagedintegrations:`AWS_REGION`:`AWS_ACCOUNT_ID`:credential-locker/`LOCKER_ID`
  "CreatedAt": "2025-06-09T13:58:52.977000+08:00"
}
```

For more information, see the [create-credential-locker](../../../cli/latest/reference/iot-managed-integrations/create-credential-locker.md "../../../cli/latest/reference/iot-managed-integrations/create-credential-locker.md") command in the managed integrations AWS CLI
_Command Reference_.

## Step 2: Add the credential locker to your hub

Add the credential locker to your hub.

###### To add a credential locker to your hub

- Use the following command to add a credential locker to your hub.

```
aws iotmi --region `AWS_REGION` --endpoint `AWS_ENDPOINT` update-managed-thing \
--identifier `"HUB_MANAGED_THING_ID"` --credential-locker-id `"LOCKER_ID"`
```

## Step 3: Create a managed thing with credentials.

Create a managed thing with credentials for your device. Each device requires its
own managed thing.

###### To create a managed thing

- Use the `create-managed-thing` command to create a managed thing for your
  device.

**create-managed-thing
example**

```
#ZWAVE:
aws iot-managed-integrations create-managed-thing --role DEVICE \
--authentication-material '900137947003133...' \ #auth material from zwave qr code
--authentication-material-type ZWAVE_QR_BAR_CODE \
--credential-locker-id ${locker_id}

#ZIGBEE:
aws iot-managed-integrations create-managed-thing --role DEVICE \
--authentication-material 'Z:286...$I:A4DC00.' \ #auth material from zigbee qr code
--authentication-material-type ZIGBEE_QR_BAR_CODE \
--credential-locker-id ${locker_id}
```

###### Note

There are separate commands for Z-wave and Zigbee devices.

**Response:**

```
{
  "Id": `"DEVICE_MANAGED_THING_ID"`
  "Arn": "arn:aws:iotmanagedintegrations:`AWS_REGION`:`AWS_ACCOUNT_ID`:managed-thing/`DEVICE_MANAGED_THING_ID`"
  "CreatedAt": "2025-06-09T13:58:52.977000+08:00"
}
```

For more information, see the [create-managed-thing](../../../cli/latest/reference/iot-managed-integrations/create-managed-thing.md "../../../cli/latest/reference/iot-managed-integrations/create-managed-thing.md") command in the managed integrations AWS CLI
_Command Reference_.

## Step 4: Plug in the device and check its status.

###### Plug in the device and check its status.

- Use the `get-managed-thing` command to check your device's status. The ProvisioningStatus of your managed thing must be ACTIVATED. For more information on ProvisioningStatus, see [Device Provisioning](device-provisioning.md "device-provisioning.md").

**get-managed-thing
example**

```
#KINESIS NOTIFICATION:
{
    "version": "1.0.0",
    "messageId": "4ac684bb7f4c41adbb2eecc1e7991xxx",
    "messageType": "DEVICE_LIFE_CYCLE",
    "source": "aws.iotmanagedintegrations",
    "customerAccountId": "12345678901",
    "timestamp": "2025-06-10T05:30:59.852659650Z",
    "region": "us-east-1",
    "resources": ["XXX"],
    "payload": {
        "deviceDetails": {
            "id": "1e84f61fa79a41219534b6fd57052XXX",
            "arn": "XXX",
            "createdAt": "2025-06-09T06:24:34.336120179Z",
            "updatedAt": "2025-06-10T05:30:59.784157019Z"
        },
        "status": "ACTIVATED"
    }
}
aws iot-managed-integrations get-managed-thing \
--identifier `:"DEVICE_MANAGED_THING_ID"`
```

**Response:**

```
{
  "Id": `"DEVICE_MANAGED_THING_ID"`
  "Arn": "arn:aws:iotmanagedintegrations:`AWS_REGION`:`AWS_ACCOUNT_ID`:managed-thing/`MANAGED_THING_ID`"
  "CreatedAt": "2025-06-09T13:58:52.977000+08:00"
}
```

For more information, see the [get-managed-thing](../../../cli/latest/reference/iot-managed-integrations/get-managed-thing.md "../../../cli/latest/reference/iot-managed-integrations/get-managed-thing.md") command in the managed integrations AWS CLI
_Command Reference_.

## Step 5: Get Device

Capabilities

Use the `get-managed-thing-capabilities` command to obtain your endpoint ID and view
a list of possible actions for your device.

###### To get a device's capabilities

- Use the `get-managed-thing-capabilities` command and note the endpoint ID.

**get-managed-thing-capabilties
example**

```
aws iotmi get-managed-thing-capabilities \
--identifier `"DEVICE_MANAGED_THING_ID"`
```

**Response:**

```
{
    "ManagedThingId": "1e84f61fa79a41219534b6fd57052cbc",
    "CapabilityReport": {
        "version": "1.0.0",
        "nodeId": "zw.FCB10009+06",
        "endpoints": [
            {
                "id": `"ENDPOINT_ID"`
                "deviceTypes": [
                    "On/Off Switch"
                ],
                "capabilities": [
                    {
                        "id": "matter.OnOff@1.4",
                        "name": "On/Off",
                        "version": "6",
                        "properties": [
                            "OnOff"
                        ],
                        "actions": [
                            "Off",
                            "On"
                        ],
                        "events": []
                    }
                    ...
}
```

For more information, see the [get-managed-thing-capabilities](../../../cli/latest/reference/iot-managed-integrations/get-managed-thing-capabilities.md "../../../cli/latest/reference/iot-managed-integrations/get-managed-thing-capabilities.md") command in the managed integrations AWS CLI
_Command Reference_.

## Step 6: Send a

command to the managed thing

Use the `send-managed-thing-command` command to send a toggle action command to your
managed thing.

###### To send a command to your managed thing

- Use the `send-managed-thing-command` command to send a command to your managed
  thing.

**send-managed-thing-command
example**

```
json=$(jq -cr '.|@json') <<EOF
[
  {
    "endpointId": "1",
    "capabilities": [
      {
        "id": "matter.OnOff@1.4",
        "name": "On/Off",
        "version": "1",
        "actions": [
          {
            "name": "Toggle",
            "parameters": {}
          }
        ]
      }
    ]
  }
]
EOF
aws iot-managed-integrations send-managed-thing-command \
--managed-thing-id `"DEVICE_MANAGED_THING_ID"` --endpoints `"ENDPOINT_ID"`

```

###### Note

This example uses jq cli to but you can also pass the entire `endpointId` string

**Response:**

```
{
"TraceId": `"TRACE_ID"`
}
```

For more information, see the [send-managed-thing-command](../../../cli/latest/reference/iot-managed-integrations/send-managed-thing-command.md "../../../cli/latest/reference/iot-managed-integrations/send-managed-thing-command.md") command in the managed integrations AWS CLI
_Command Reference_.

## Step 7: Remove the managed

thing from your hub

Clean up your hub by removing the managed thing.

###### To delete a managed thing

- Use the `delete-managed-thing` command to remove a managed thing from your
  device hub.

**delete-managed-thing
example**

```
aws iot-managed-integrations delete-managed-thing \
--identifier `"DEVICE_MANAGED_THING_ID"`
```

For more information, see the [delete-managed-thing](../../../cli/latest/reference/iot-managed-integrations/delete-managed-thing.md "../../../cli/latest/reference/iot-managed-integrations/delete-managed-thing.md") command in the managed integrations AWS CLI
_Command Reference_.

###### Note

If the device is stuck in a `DELETE_IN_PROGRESS` state, append the `--force` flag to the `delete-managed-thing command`.

###### Note

For Z-wave devices, you need to put the device into pairing mode after executing the command.
