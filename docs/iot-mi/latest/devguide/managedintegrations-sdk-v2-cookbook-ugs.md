# User guided setup to onboard and operate

devices

Set up your devices to be onboarded to your managed integrations hub by creating a managed thing an
connecting it to your hub. This section describes the steps to complete the
device onboarding process using user guided setup.

## Prerequisites

Complete these steps before attempting to onboard a device:

- Onboard a hub device to the managed integrations hub.
- Install the latest version of AWS CLI from the [Managed Integrations AWS CLI Command Reference](../../../cli/latest/reference/iot-managed-integrations.md "../../../cli/latest/reference/iot-managed-integrations.md")
- Subscribe to [DEVICE_DISCOVERY_STATUS](managedintegrations-notifications.md#managedintegrations-notification-setup "managedintegrations-notifications.md#managedintegrations-notification-setup") event notifications.

###### User guided setup steps

- [Prerequisite: Enable pairing mode on your Z Wave device](#managedintegrations-sdk-v2-cookbook-pairing-mode "#managedintegrations-sdk-v2-cookbook-pairing-mode")
- [Step 1: Start device discovery](#managedintegrations-sdk-v2-cookbook-device-discovery "#managedintegrations-sdk-v2-cookbook-device-discovery")
- [Step 2: Query the discovery job ID](#managedintegrations-sdk-v2-cookbook-query-discovery "#managedintegrations-sdk-v2-cookbook-query-discovery")
- [Step 3: Create a managed thing for your device](#managedintegrations-sdk-v2-cookbook-ugs-managed-thing "#managedintegrations-sdk-v2-cookbook-ugs-managed-thing")
- [Step 4: Query the
  managed thing](#managedintegrations-sdk-v2-cookbook-query-managed-thing "#managedintegrations-sdk-v2-cookbook-query-managed-thing")
- [Step 5: Get managed thing capabilities](#managedintegrations-sdk-v2-cookbook-check-device-capabilties "#managedintegrations-sdk-v2-cookbook-check-device-capabilties")
- [Step 6: Send a
  command to the managed thing](#managedintegrations-sdk-v2-cookbook-ugs-control-device "#managedintegrations-sdk-v2-cookbook-ugs-control-device")
- [Step 7: Check the
  managed thing state](#managedintegrations-sdk-v2-cookbook-ugs-device-state "#managedintegrations-sdk-v2-cookbook-ugs-device-state")
- [Step 8: Remove managed
  thing from your hub](#managedintegrations-sdk-v2-cookbook-ugs-clean-up "#managedintegrations-sdk-v2-cookbook-ugs-clean-up")

## Prerequisite: Enable pairing mode on your Z Wave device

Enable pairing mode on the Z-wave device.
The pairing mode can vary for each Z-Wave device, so refer to the device's instructions to properly set up the pairing mode.
It is usually a button that the user must press.

## Step 1: Start device discovery

Start device discovery for your hub to obtain a discovery job ID which is used to
onboard your device.

###### To start device discovery

- Use the [start-device-discovery](../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md "../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md") command to obtain the discovery job ID.

**start-device-discovery example**

```
#For Zigbee
  aws iot-managed-integrations start-device-discovery --discovery-type ZIGBEE \
  --controller-identifier `HUB_MANAGED_THING_ID`

  #For Zwave
  aws iot-managed-integrations start-device-discovery --discovery-type ZWAVE \
  --controller-identifier `HUB_MANAGED_THING` \
  --authentication-material-type ZWAVE_INSTALL_CODE \
  --authentication-material 13333

  #For Cloud
  aws iot-managed-integrations start-device-discovery --discovery-type CLOUD \
  --account-association-id `C2C_ASSOCIATION_ID` \

  #For Custom
  aws iot-managed-thing start-device-discovery --discovery-type CUSTOM \
  --controller-identifier `HUB_MANAGED_THING_ID` \
  --custom-protocol-detail `NAME : NON_EMPTY_STRING` \
```

**Response:**

```
{
      "Id": `DISCOVERY_JOB_ID`,
      "StartedAt": "2025-06-03T14:43:12.726000-07:00"
  }
```

###### Note

There are separate commands for Z-wave and Zigbee devices.

For more information, see the [start-device-discovery](../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md "../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md") API in the managed integrations AWS CLI _Command
Reference_.

## Step 2: Query the discovery job ID

Use the `list-discovered-devices` command to get the authentication material of your
device.

###### To query your discovery job ID

- Use the discovery job ID with the list-discovered-devices command to get the
  authentication material of your device.

```
aws iot-managed-integrations list-discovered-devices --identifier `DISCOVERY_JOB_ID`
```

**Response:**

```
"Items": [
    {
        "DeviceTypes": [],
        "DiscoveredAt": "2025-06-03T14:43:37.619000-07:00",
        "AuthenticationMaterial": `AUTHENTICATION_MATERIAL`
    }
]
```

## Step 3: Create a managed thing for your device

Use the `create-managed-thing` command to create a managed thing for your device.
Each device requires its own managed thing.

###### To create a managed thing

- Use the `create-managed-thing` command to create a managed thing for your device.

**create-managed-thing example**

```
aws iot-managed-integrations create-managed-thing \
  --role  DEVICE --authentication-material-type DISCOVERED_DEVICE \
  --authentication-material "`AUTHENTICATION_MATERIAL`"
```

**Response:**

```
{
    "Id": "`DEVICE_MANAGED_THING_ID`"
    "Arn": "arn:aws:iotmanagedintegrations:`AWS_REGION`:`AWS_ACCOUNT_ID`:managed-thing/`DEVICE_MANAGED_THING_ID`"
    "CreatedAt": "2025-06-09T13:58:52.977000+08:00"
  }
```

For more information, see the [create-managed-thing](../../../cli/latest/reference/iot-managed-integrations/create-managed-thing.md "../../../cli/latest/reference/iot-managed-integrations/create-managed-thing.md") command in the managed integrations AWS CLI
_Command Reference_.

## Step 4: Query the

managed thing

You can check if a managed thing is activated by using the `get-managed-thing` command.

###### To query a managed thing

- Use the `get-managed-thing` command to check if the managed thing's
  provisioning status is set to `ACTIVATED`. For more information on
  provisioning status, see [Device Provisioning](device-provisioning.md "device-provisioning.md").

**get-managed-thing example**

```
aws iot-managed-integrations get-managed-thing \
  --identifier "`DEVICE_MANAGED_THING_ID`"
```

**Response:**

```
{
      "Id": "`DEVICE_MANAGED_THING_ID`",
      "Arn": "arn:aws:iotmanagedintegrations:`AWS_REGION`:`AWS_ACCOUNT_ID`:managed-thing/`DEVICE_MANAGED_THING_ID`,
      "Role": "DEVICE",
      "ProvisioningStatus": "ACTIVATED",
      "MacAddress": "`MAC_ADDRESS`",
      "ParentControllerId": "`PARENT_CONTROLLER_ID`",
      "CreatedAt": "2025-06-03T14:46:35.149000-07:00",
      "UpdatedAt": "2025-06-03T14:46:37.500000-07:00",
      "Tags": {}
  }
```

For more information, see the [get-managed-thing](../../../cli/latest/reference/iot-managed-integrations/get-managed-thing.md "../../../cli/latest/reference/iot-managed-integrations/get-managed-thing.md") command in the managed integrations AWS CLI
_Command Reference_.

## Step 5: Get managed thing capabilities

You can view a list of a managed thing's available actions by using the `get-managed-thing-capabiltiies`.

###### To get a device's capabilities

- Use the `get-managed-thing-capabilities` command to obtain the endpoint ID.
  Also note the list of possible actions.

**get-managed-thing-capabilities
example**

```
aws iot-managed-integrations get-managed-thing-capabilities \
  --identifier "`DEVICE_MANAGED_THING_ID`"
```

**Response:**

```
{
      "ManagedThingId": "`DEVICE_MANAGED_THING_ID`",
      "CapabilityReport": {
          "version": "1.0.0",
          "nodeId": "zb.539D+4A1D",
          "endpoints": [
              {
                  "id": "1",
                  "deviceTypes": [
                      "Unknown Device"
                  ],
                  "capabilities": [
                      {
                          "id": "matter.OnOff@1.4",
                          "name": "On/Off",
                          "version": "6",
                          "properties": [
                              "OnOff",
                              "OnOff",
                              "OnTime",
                              "OffWaitTime"
                          ],
                          "actions": [
                              "Off",
                              "On",
                              "Toggle",
                              "OffWithEffect",
                              "OnWithRecallGlobalScene",
                              "OnWithTimedOff"
                          ],
                          ...
  }
```

For more information, see the [get-managed-thing-capabilities](../../../cli/latest/reference/iot-managed-integrations/get-managed-thing-capabilities.md "../../../cli/latest/reference/iot-managed-integrations/get-managed-thing-capabilities.md") command in the managed integrations
AWS CLI*Command Reference*.

## Step 6: Send a

command to the managed thing

You can use the send-managed-thing-command command to send a toggle action command to your managed thing.

###### Send a command to the managed thing using a toggle action.

- Use the `send-managed-thing-command` command to send a toggle action
  command.

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
  --managed-thing-id ${device_managed_thing_id} --endpoints `ENDPOINT_ID`

```

###### Note

This example uses jq cli to but you can also pass the entire `endpointId` string

**Response:**

```
{
  "TraceId": `TRACE_ID`
  }
```

For more information, see the [send-managed-thing-command](../../../cli/latest/reference/iot-managed-integrations/send-managed-thing-command.md "../../../cli/latest/reference/iot-managed-integrations/send-managed-thing-command.md") command in the managed integrations AWS CLI
_Command Reference_.

## Step 7: Check the

managed thing state

Check the managed thing's state to validate the toggle action succeeded.

###### To check a managed thing's device state

- Use the `get-managed-thing-state` command to validate the toggle action
  succeeded.

**get-managed-thing-state example**

```

  aws iot-managed-integrations get-managed-thing-state --managed-thing-id `DEVICE_MANAGED_THING_ID`
```

**Response:**

```
{
      "Endpoints": [
          {
              "endpointId": "1",
              "capabilities": [
                  {
                      "id": "matter.OnOff@1.4",
                      "name": "On/Off",
                      "version": "1.4",
                      "properties": [
                          {
                              "name": "OnOff",
                              "value": {
                                  "propertyValue": true,
                                  "lastChangedAt": "2025-06-03T21:50:39.886Z"
                              }
                          }
                      ]
                  }
              ]
          }
      ]
  }
```

For more information, see the [get-managed-thing-state](../../../cli/latest/reference/iot-managed-integrations/get-managed-thing-state.md "../../../cli/latest/reference/iot-managed-integrations/get-managed-thing-state.md") command in the managed integrations
AWS CLI _Command Reference_.

## Step 8: Remove managed

thing from your hub

Clean up your hub by removing the managed thing.

###### To delete a managed thing

- Use the [delete-managed-thing](../../../cli/latest/reference/iot-managed-integrations/delete-managed-thing.md "../../../cli/latest/reference/iot-managed-integrations/delete-managed-thing.md") command to remove a managed thing.

**delete-managed-thing example**

```
aws iot-managed-integrations delete-managed-thing \
  --identifier `MANAGED_THING_ID`
```

For more information, see the [delete-managed-thing](../../../cli/latest/reference/iot-managed-integrations/delete-managed-thing.md "../../../cli/latest/reference/iot-managed-integrations/delete-managed-thing.md") command in the managed integrations AWS CLI
_Command Reference_.

###### Note

If the device is stuck in a `DELETE_IN_PROGRESS` state, append the
`--force` flag to the `delete-managed-thing`
command.

###### Note

For Z-wave devices, you need to put the device into pairing mode after executing the command.
