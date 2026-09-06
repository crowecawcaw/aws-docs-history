

# User guided setup to onboard and operate devices
<a name="managedintegrations-sdk-v2-cookbook-ugs"></a>

Set up your devices to be onboarded to your Managed Integrations hub by creating a managed thing an connecting it to your hub. This section describes the steps to complete the device onboarding process using user guided setup.

## Prerequisites
<a name="managedintegrations-sdk-v2-cookbook-ugs-prereq"></a>

Complete these steps before attempting to onboard a device:
+ Onboard a hub device to the Managed Integrations hub.
+ Install the latest version of AWS CLI from the [Managed Integrations AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/)
+ Subscribe to [DEVICE\_DISCOVERY\_STATUS](managedintegrations-notifications.md#managedintegrations-notification-setup) event notifications.

**Topics**
+ [Prerequisites](#managedintegrations-sdk-v2-cookbook-ugs-prereq)
+ [Prerequisite: Enable pairing mode on your Z Wave device](#managedintegrations-sdk-v2-cookbook-pairing-mode)
+ [Step 1: Start device discovery](#managedintegrations-sdk-v2-cookbook-device-discovery)
+ [Step 2: Query the discovery job ID](#managedintegrations-sdk-v2-cookbook-query-discovery)
+ [Step 3: Create a managed thing for your device](#managedintegrations-sdk-v2-cookbook-ugs-managed-thing)
+ [Step 4: Query the managed thing](#managedintegrations-sdk-v2-cookbook-query-managed-thing)
+ [Step 5: Get managed thing capabilities](#managedintegrations-sdk-v2-cookbook-check-device-capabilties)
+ [Step 6: Send a command to the managed thing](#managedintegrations-sdk-v2-cookbook-ugs-control-device)
+ [Step 7: Check the managed thing state](#managedintegrations-sdk-v2-cookbook-ugs-device-state)
+ [Step 8: Remove managed thing from your hub](#managedintegrations-sdk-v2-cookbook-ugs-clean-up)

## Prerequisite: Enable pairing mode on your Z Wave device
<a name="managedintegrations-sdk-v2-cookbook-pairing-mode"></a>

Enable pairing mode on the Z-wave device. The pairing mode can vary for each Z-Wave device, so refer to the device's instructions to properly set up the pairing mode. It is usually a button that the user must press. 

## Step 1: Start device discovery
<a name="managedintegrations-sdk-v2-cookbook-device-discovery"></a>

Start device discovery for your hub to obtain a discovery job ID which is used to onboard your device.

**To start device discovery**
+ Use the [start-device-discovery](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/start-device-discovery.html) command to obtain the discovery job ID.

  **start-device-discovery example**

  ```
  #For Zigbee
    aws iot-managed-integrations start-device-discovery --discovery-type ZIGBEE \
    --controller-identifier {{HUB_MANAGED_THING_ID}}
    
    #For Zwave
    aws iot-managed-integrations start-device-discovery --discovery-type ZWAVE \
    --controller-identifier {{HUB_MANAGED_THING}} \
    --authentication-material-type ZWAVE_INSTALL_CODE \
    --authentication-material 13333
    
    #For Cloud
    aws iot-managed-integrations start-device-discovery --discovery-type CLOUD \
    --account-association-id {{C2C_ASSOCIATION_ID}} \
    
    #For Custom
    aws iot-managed-thing start-device-discovery --discovery-type CUSTOM \
    --controller-identifier {{HUB_MANAGED_THING_ID}} \
    --custom-protocol-detail {{NAME : NON_EMPTY_STRING}} \
  ```

  **Response:**

  ```
  {
        "Id": {{DISCOVERY_JOB_ID}},
        "StartedAt": "2025-06-03T14:43:12.726000-07:00"
    }
  ```
**Note**  
There are separate commands for Z-wave and Zigbee devices.

  For more information, see the [start-device-discovery](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/start-device-discovery.html) API in the Managed Integrations AWS CLI *Command Reference*.

## Step 2: Query the discovery job ID
<a name="managedintegrations-sdk-v2-cookbook-query-discovery"></a>

Use the `list-discovered-devices` command to get the authentication material of your device.

**To query your discovery job ID**
+ Use the discovery job ID with the list-discovered-devices command to get the authentication material of your device.

  ```
  aws iot-managed-integrations list-discovered-devices --identifier {{DISCOVERY_JOB_ID}}
  ```

**Response:**

```
"Items": [
    {
        "DeviceTypes": [],
        "DiscoveredAt": "2025-06-03T14:43:37.619000-07:00",
        "AuthenticationMaterial": {{AUTHENTICATION_MATERIAL}}
    }
]
```

### Populate Brand and Model for discovered devices
<a name="managedintegrations-sdk-v2-cookbook-brand-model"></a>

During device discovery, discovered devices can optionally report brand and model information through the Matter Basic Information cluster. These values are then returned in the [ListDiscoveredDevices](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListDiscoveredDevices.html#API_ListDiscoveredDevices_ResponseSyntax) and [ListManagedThings](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListManagedThings.html#API_ListManagedThings_ResponseSyntax) responses.

Report the Basic Information cluster (cluster `0x0028`) on the device's root endpoint (`0`) and map:
+ `VendorName` (attribute `0x0001`) → `Brand`
+ `ProductName` (attribute `0x0003`) → `Model`

The following example shows how to report the Basic Information cluster on the root endpoint:

```
"endpoints": [{
    "id": "0",
    "clusters": [{
        "id": "0x0028",
        "attributes": [{
            "id": "0x0001",
            "value": "ExampleBrand"
        }, {
            "id": "0x0003",
            "value": "ExampleModel-X1"
        }]
    }]
}]
```

Both values are strings with a maximum length of 32 characters. If the Basic Information cluster or either attribute is not reported, the corresponding field is omitted from the response.

## Step 3: Create a managed thing for your device
<a name="managedintegrations-sdk-v2-cookbook-ugs-managed-thing"></a>

Use the `create-managed-thing` command to create a managed thing for your device. Each device requires its own managed thing. 

**To create a managed thing**
+ Use the `create-managed-thing` command to create a managed thing for your device.

  **create-managed-thing example**

  ```
  aws iot-managed-integrations create-managed-thing \
    --role  DEVICE --authentication-material-type DISCOVERED_DEVICE \
    --authentication-material "{{AUTHENTICATION_MATERIAL}}"
  ```

  **Response:**

  ```
  {    
      "Id": "{{DEVICE_MANAGED_THING_ID}}"
      "Arn": "arn:aws:iotmanagedintegrations:{{AWS_REGION}}:{{AWS_ACCOUNT_ID}}:managed-thing/{{DEVICE_MANAGED_THING_ID}}"
      "CreatedAt": "2025-06-09T13:58:52.977000+08:00"
    }
  ```

  For more information, see the [create-managed-thing](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/create-managed-thing.html) command in the Managed Integrations AWS CLI *Command Reference*.

## Step 4: Query the managed thing
<a name="managedintegrations-sdk-v2-cookbook-query-managed-thing"></a>

You can check if a managed thing is activated by using the `get-managed-thing` command. 

**To query a managed thing**
+ Use the `get-managed-thing` command to check if the managed thing's provisioning status is set to `ACTIVATED`. For more information on provisioning status, see [Device Provisioning](https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html).

  **get-managed-thing example**

  ```
  aws iot-managed-integrations get-managed-thing \
    --identifier "{{DEVICE_MANAGED_THING_ID}}"
  ```

  **Response:**

  ```
  {
        "Id": "{{DEVICE_MANAGED_THING_ID}}",
        "Arn": "arn:aws:iotmanagedintegrations:{{AWS_REGION}}:{{AWS_ACCOUNT_ID}}:managed-thing/{{DEVICE_MANAGED_THING_ID}},
        "Role": "DEVICE",
        "ProvisioningStatus": "ACTIVATED",
        "MacAddress": "{{MAC_ADDRESS}}",
        "ParentControllerId": "{{PARENT_CONTROLLER_ID}}",
        "CreatedAt": "2025-06-03T14:46:35.149000-07:00",
        "UpdatedAt": "2025-06-03T14:46:37.500000-07:00",
        "Tags": {}
    }
  ```

  For more information, see the [get-managed-thing](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/get-managed-thing.html) command in the Managed Integrations AWS CLI *Command Reference*.

## Step 5: Get managed thing capabilities
<a name="managedintegrations-sdk-v2-cookbook-check-device-capabilties"></a>

You can view a list of a managed thing's available actions by using the `get-managed-thing-capabiltiies`. 

**To get a device's capabilities**
+ Use the `get-managed-thing-capabilities` command to obtain the endpoint ID. Also note the list of possible actions.

  **get-managed-thing-capabilities example**

  ```
  aws iot-managed-integrations get-managed-thing-capabilities \
    --identifier "{{DEVICE_MANAGED_THING_ID}}"
  ```

  **Response:**

  ```
  {
        "ManagedThingId": "{{DEVICE_MANAGED_THING_ID}}",
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

  For more information, see the [get-managed-thing-capabilities](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/get-managed-thing-capabilities.html) command in the Managed Integrations AWS CLI*Command Reference*.

## Step 6: Send a command to the managed thing
<a name="managedintegrations-sdk-v2-cookbook-ugs-control-device"></a>

You can use the send-managed-thing-command command to send a toggle action command to your managed thing. 

**Send a command to the managed thing using a toggle action.**
+ Use the `send-managed-thing-command` command to send a toggle action command.

  **send-managed-thing-command example**

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
    --managed-thing-id ${device_managed_thing_id} --endpoints {{ENDPOINT_ID}}
  ```
**Note**  
This example uses jq cli to but you can also pass the entire `endpointId` string

  **Response:**

  ```
  {    
    "TraceId": {{TRACE_ID}}
    }
  ```

  For more information, see the [send-managed-thing-command](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/send-managed-thing-command.html) command in the Managed Integrations AWS CLI *Command Reference*.

## Step 7: Check the managed thing state
<a name="managedintegrations-sdk-v2-cookbook-ugs-device-state"></a>

Check the managed thing's state to validate the toggle action succeeded.

**To check a managed thing's device state**
+ Use the `get-managed-thing-state` command to validate the toggle action succeeded.

  **get-managed-thing-state example**

  ```
    aws iot-managed-integrations get-managed-thing-state --managed-thing-id {{DEVICE_MANAGED_THING_ID}}
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

  For more information, see the [get-managed-thing-state](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/get-managed-thing-state.html) command in the Managed Integrations AWS CLI* Command Reference*.

## Step 8: Remove managed thing from your hub
<a name="managedintegrations-sdk-v2-cookbook-ugs-clean-up"></a>

Clean up your hub by removing the managed thing.

**To delete a managed thing**
+ Use the [delete-managed-thing](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/delete-managed-thing.html) command to remove a managed thing. 

  **delete-managed-thing example**

  ```
  aws iot-managed-integrations delete-managed-thing \
    --identifier {{MANAGED_THING_ID}}
  ```

  For more information, see the [delete-managed-thing](https://docs.aws.amazon.com/cli/latest/reference/iot-managed-integrations/delete-managed-thing.html) command in the Managed Integrations AWS CLI *Command Reference*.
**Note**  
If the device is stuck in a `DELETE_IN_PROGRESS` state, append the `--force` flag to the `delete-managed-thing` command.
**Note**  
For Z-wave devices, you need to put the device into pairing mode after executing the command.