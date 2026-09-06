

# AWS IoT Wireless API operations
<a name="iot-wireless-api-reference"></a>

You can perform the following additional API operations when onboarding your LoRaWAN or Sidewalk end devices, or when creating an import task for provisioning Sidewalk end devices in bulk.

The following sections contain additional information about these API operations.

## AWS IoT Wireless API operations for device profiles
<a name="iot-wireless-device-profiles"></a>

You can perform the following API operations for yourLoRaWAN and Sidewalk device profiles:
+ [`CreateDeviceProfile`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateDeviceProfile.html) API or the [`create-device-profile`](https://docs.aws.amazon.com/cli/latest/reference/iotwireless/create-device-profile.html) CLI
+ [`GetDeviceProfile`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetDeviceProfile.html) API or the [`get-device-profile`](https://docs.aws.amazon.com/cli/latest/reference/iotwireless/get-device-profile.html) CLI
+ [`ListDeviceProfiles`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDeviceProfiles.html) API or the [`list-device-profiles`](https://docs.aws.amazon.com/cli/latest/reference/iotwireless/list-device-profiles.html) CLI
+ [`DeleteDeviceProfile`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteDeviceProfile.html) API or the [`delete-device-profile`](https://docs.aws.amazon.com/cli/latest/reference/iotwireless/get-device-profile.html) CLI

The following sections show you how to list and delete profiles. For information about creating and retrieving device profiles, see:
+ [Add device profiles](lorawan-define-profiles.md#lorawan-device-profiles)
+ [Step 1: Create a device profile](iot-sidewalk-add-device.md#iot-sidewalk-profile-create)

### List device profiles in your AWS account
<a name="iot-wireless-profile-list"></a>

You can use the [`ListDeviceProfiles`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDeviceProfiles.html) API operation to list device profiles in your AWS account that you added to AWS IoT Wireless. You can use this information to identify the devices that you want to associate this profile to.

To filter the list to display only LoRaWAN or Sidewalk device profiles, set the `Type` when running the API. Following shows an example CLI command:

```
aws iotwireless list-device-profiles --wireless-device-type "Sidewalk"
```

Running this command returns a list of device profiles that you added, including their profile identifier and Amazon Resource Name (ARN). To retrieve additional details about a specific profile, use the `GetDeviceProfile` API.

```
{
    "DeviceProfileList": [
        {
            "Name": "{{SidewalkDeviceProfile1}}",
            "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d",
            "Arn": "arn:aws:iotwireless:{{us-east-1}}:{{123456789012}}:DeviceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d"
        },
        {
            "Name": "{{SidewalkDeviceProfile2}}",
            "Id": "a1b2c3d4-5678-90ab-cdef-12ab345c67de",
            "Arn": "arn:aws:iotwireless:{{us-east-1}}:{{123456789012}}:DeviceProfile/a1b2c3d4-5678-90ab-cdef-12ab345c67de"
        }
    ]
}
```

### Delete device profiles from your AWS account
<a name="iot-wireless-profile-delete"></a>

You can delete your device profiles using the [`DeleteDeviceProfile`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteDeviceProfile.html) API operation. The following shows an example CLI command:

**Warning**  
Deletion actions can't be undone. The device profile will be permanently removed from your AWS account.

```
aws iotwireless delete-device-profile --name "{{SidewalkProfile}}"
```

This command doesn't produce any output. You can use the `GetDeviceProfile` API or the `ListDeviceProfiles` API operation to verify that the profile has been removed from your account.

## AWS IoT Wireless API operations for LoRaWAN and Sidewalk devices
<a name="iot-wireless-api-devices"></a>

You can perform the following API operations for your LoRaWAN and Sidewalk devices:
+ [`CreateWirelessDevice`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessDevice.html) API or the [`create-wireless-device`](https://docs.aws.amazon.com/cli/latest/reference/create-wireless-device.html) CLI
+ [`GetWirelessDevice`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessDevice.html) API or the [`get-wireless-device`](https://docs.aws.amazon.com/cli/latest/reference/get-wireless-device.html) CLI
+ [`ListWirelessDevices`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessDevices.html) API or the [`list-wireless-devices`](https://docs.aws.amazon.com/cli/latest/reference/list-wireless-devices.html) CLI
+ [`DeleteWirelessDevice`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteWirelessDevice.html) API or the [`delete-wireless-device`](https://docs.aws.amazon.com/cli/latest/reference/delete-wireless-device.html) CLI
+ [`UpdateWirelessDevice`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessDevice.html) API or the [`update-wireless-device`](https://docs.aws.amazon.com/cli/latest/reference/update-wireless-device.html) CLI
+ [`AssociateWirelessDeviceWithThing`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateWirelessDeviceWithThing.html) API or the [`associate-wireless-device-with-thing`](https://docs.aws.amazon.com/cli/latest/reference/associate-wireless-device-with-thing.html) CLI
+ [`DisassociateWirelessDeviceFromThing`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateWirelessDeviceFromThing.html) API or the [`disassociate-wireless-device-from-thing`](https://docs.aws.amazon.com/cli/latest/reference/disassociate-wireless-device-from-thing.html) CLI

The following sections show you how to list and delete devices. For information about creating wireless devices and retrieving device information, see:
+ [Add your wireless device to AWS IoT Core for LoRaWAN](lorawan-end-devices-add.md)
+ [Step 2: Add your Sidewalk device](iot-sidewalk-add-device.md#iot-sidewalk-device-create)

### Associate wireless devices in your AWS account to an IoT thing
<a name="iot-wireless-associate-devices"></a>

To associate your LoRaWAN and Sidewalk devices with an AWS IoT thing, use the `AssociateWirelessDeviceWithThing` API operation.

Things in AWS IoT make it easier to search and manage your devices. Associating a thing with your device lets the device access other AWS IoT Core features. For more information about using this API, see [`AssociateWirelessDeviceWithThing`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateWirelessDeviceWithThing.html).

The following shows an example of running this command. Running this command doesn't produce any output.

```
aws iotwireless associate-wireless-device-with-thing \
    --id {{"12345678-a1b2-3c45-67d8-e90fa1b2c34d"}} \
    --thing-arn "arn:aws:iot:{{us-east-1:123456789012:}}thing/{{MySidewalkThing}}"
```

To disassociate your wireless device from an AWS IoT thing, use the [`DisassociateWirelessDeviceFromThing`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DisassociateWirelessDeviceFromThing.html) API operation, as shown in the following example.

```
aws iotwireless disassociate-wireless-device-from-thing \
    --id {{"12345678-a1b2-3c45-67d8-e90fa1b2c34d"}}
```

### List wireless devices in your AWS account
<a name="iot-wireless-list-devices"></a>

To list wireless devices in your AWS account that you added to AWS IoT Wireless, use the [`ListWirelessDevices`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessDevices.html) API operation. To filter the list to return only LoRaWAN or Sidewalk devices, set the `WirelessDeviceType`.

The following shows an example of running this command:

```
aws iotwireless list-wireless-devices --wireless-device-type Sidewalk
```

Running this command returns a list of devices that you added, including their profile identifier and the Amazon Resource Name (ARN). To retrieve additional details about a specific device, use the [`GetWirelessDevice`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessDevice.html) API operation.

```
{
    "WirelessDeviceList": [
        {
            "Name": "{{mySidewalkDevice}}",
            "DestinationName": "{{SidewalkDestination}}",
            "Id": "1ffd32c8-8130-4194-96df-622f072a315f",
            "Type": "Sidewalk",
            "LastUplinkReceivedAt": "{{null}}",
            "LoRaWAN": "{{null}}",
            "Positioning": "{{Enabled}}",
            "Sidewalk": {
                "AmazonId": "{{null}}",
                "SidewalkId": "{{1234567890123456}}"
                "DeviceCertificates": [
                    {"SigningAlg": "Ed25519",
                    "Value": "{{WUqB/E50VP7oZpHtYoBgpzJXYvhv51y/DBIfzNhrleo4UzOWCs
                    IzbaJwft+IPBSUQthDifJDYik0DuU1jLvuR8cpK7YyI7cUD/oZG+4Pro/s3n
                    AIhyXmhUlepmbveVxM8boiTiaUlL4iB9DoKrB41pWdHeg7hR8BDrE1m4sf5Q
                    9ZUwDy5BqMafeW0RUKZMVunpChji0dwC5VoSSb8IT7V+bKTJXXdZ8lP11jsi
                    uJfwF64Eq1NCe2qKb7gql5u+qBE7vatDOSonwN56I6Ah8HWYRSyJTk7DSJKk
                    nSY7KGyLjs0qMI8L8AeJ++UIO/jOsGnhC6Ku1ba62bEPmIBr+889NhOngiIt
                    1+1DrSOO59a1PLYqfVa5ejKq0tzzbyNG/m/oW72kkGGHRuec2zOXEO86kf4X
                    0qzFfTKoo/6lt67XfXIQkO4wApCgJ8AHwHa3xz+dh+W6mFwYFRqrQQT8s0Sj
                    SuDtLCaqZhnch47MZk7E/itqP4JnJ7RsJHWxXsG2gTNlRghfG+zhpKzVVdvV
                    VZeZ22f2WZ2QoGlzXxrW0/b7mqpO2l+8fzRYYdqAp1AAADGz+gFBeX/ZNN8V
                    JwnsNfgzj4me1HgVJdUo4W9kvx9cr2jHWkC3Oj/bdBTh1+yBjOC53yHlQK/l1
                    GHrEWiWPPnE434LRxnWkwr8EHD4oieJxC8fkIxkQfj+gHh}}"
                    },
                    {"SigningAlg": "P256r1",
                    "Value": "{{WUqB/E50VP7oZpHtYoBgpzJXYvhv51y/DBIfzNhrleojbsxI2iz
                    y1YBsbQTzVPwYflEknYVQ1IIqMxPaRo4jSOuHX0+ixpFdnQb00YfKKmZ/Sj
                    3aT4r8H6cdftGnWJlHzAcERDrJIOz8sjz11Rdp1sF+6BIeU84jQxKMXCvKGv
                    vJrI+qR4nke3fsN9NmgS/c2w/22599di3tf2tFBUXh+FhTAPJq64Xr8Rd4J
                    Z5heZYc7OPTrIi8IcSrQfq0aqnyFlogb9K2C0252s1V3ClmiRq/lWxwZTxu
                    UYX4XpNnFJhTNPmC+gZMHABJhBX8wX9xMd3mDJ/00F1EQKfYw8KWXuBEH4G
                    G0JM1k/Ve75Ql0hAmzf1wedNhSwBzwkVaat0OXcNsC++/AHhqubQ9HrC/LH
                    EmQ4vFCO/K0yBNY+fVOYA+pZPgAnQI9i3H4MmBNd/fONRht1TceFzFOgmUJ
                    ya9F1+WmWkvl9IYbfuglfkb30Yzr57Ks+/wl8wRGwVeCbqn1NaNYTPWRNTq
                    7Re/8DaxVEa7MQEUhSI9rIPLuwK2rZK9mGLjThdj7wJ7AHy0vcqSgNN/nxV
                    JRmROMRSCdZzctV3wrfCHHUZbrfHMIp0bd9h01LijLxWj395AsS5pC7QTpj
                    BtAbLN9SdXOT9w4H1x8Nkp0ujLxWRN37IEy0V9DrPK2w1g74uqWPfUPnSBj
                    tvM55JnQpmm23WQNvHa1Vr6zmWDjzjHpcNirPbzXyBlKEhkX4xylaSMnm4U
                    rVXtAMaAJ/csC4HPTKr3dazdvEkhwGAAAIFByCjSp/5WHc4Ahsy}}"
                    }
                ],
                "DeviceProfileId": "{{12345678-1234-1234-1234-123456789012}}",
                "Positioning": {
                    "DestinationName": "{{LocationDestinationName}}"
                }
            },
            "Arn": "arn:aws:iotwireless:{{us-east-1}}:{{123456789012}}:WirelessDevice/1ffd32c8-8130-4194-96df-622f072a315f"
        }
    ]
}
```

### Delete wireless devices from your AWS account
<a name="iot-wireless-delete-devices"></a>

To delete your wireless devices, pass the `WirelessDeviceID` of the devices you want to delete to the [`DeleteWirelessDevice`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteWirelessDevice.html) API operation.

The following shows an example command:

```
aws iotwireless delete-wireless-device --id "{{23456789-abcd-0123-bcde-fabc012345678}}"
```

This command doesn't produce any output. You can use the `GetWirelessDevice` API or the `ListWirelessDevices` API operation to verify that the device has been removed from your account.

## AWS IoT Wireless API operations for destinations for wireless devices
<a name="iot-wireless-api-destinations"></a>

You can perform the following API operations for destinations for your LoRaWAN and Sidewalk devices:
+ [`CreateDestination`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateDestination.html) API or the [`create-destination`](https://docs.aws.amazon.com/cli/latest/reference/create-destination.html) CLI
+ [`GetDestination`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetDestination.html) API or the [`get-destination`](https://docs.aws.amazon.com/cli/latest/reference/get-destination.html) CLI
+ [`UpdateDestination`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateDestination.html) API or the [`update-destination`](https://docs.aws.amazon.com/cli/latest/reference/update-destination.html) CLI
+ [`ListDestinations`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDestinations.html) API or the [`list-destinations`](https://docs.aws.amazon.com/cli/latest/reference/list-destinations.html) CLI
+ [`DeleteDestination`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteDestination.html) API or the [`delete-destination`](https://docs.aws.amazon.com/cli/latest/reference/delete-destination.html) CLI

The following sections show you how to get, list, update, and delete destinations. For information about creating destinations, see [Add a destination for your Sidewalk end device](iot-sidewalk-qsg-destination.md).

### Get information about your destination
<a name="iot-wireless-get-destination"></a>

You can use the [`GetDestination`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetDestination.html) API operation to get information about the destination that you added to your account for AWS IoT Wireless. Provide the destination name as input to the API. The API will return information about the destination matching the specified identifier.

The following shows an example CLI command:

```
aws iotwireless get-destination --name {{SidewalkDestination}}
```

Running this command returns the parameters of your destination.

```
{
    "Arn": "arn:aws:iotwireless:{{us-east-1}}:{{123456789012}}:Destination/IoTWirelessDestination",
    "Name": "{{SidewalkDestination}}",
    "Expression": "{{IoTWirelessRule}}",
    "ExpressionType": "{{RuleName}}",
    "RoleArn": "arn:aws:iam::{{123456789012}}:role/{{IoTWirelessDestinationRole}}"
}
```

### Update properties of your destination
<a name="iot-wireless-update-destination"></a>

Use the [`UpdateDestination`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateDestination.html) API operation to update properties of your destination that you added to your account for AWS IoT Wireless. The following shows an example CLI command that updates the description property:

```
aws iotwireless update-destination --name {{SidewalkDestination}} \
    --description {{"Destination for messages processed using IoTWirelessRule"}}
```

### List destinations in your AWS account
<a name="iot-wireless-list-destinations"></a>

Use the [`ListDestinations`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDestinations.html) API operation to list destinations in your AWS account that you added to AWS IoT Wireless. To filter the list to return only destinations for LoRaWAN and Sidewalk end devices, use the `WirelessDeviceType` parameter.

The following shows an example CLI command:

```
aws iotwireless list-destinations --wireless-device-type "Sidewalk"
```

Running this command returns a list of destinations that you added, including their Amazon Resource Name (ARN). To retrieve additional details about a specific destination, use the `GetDestination` API.

```
{
    "DestinationList": [
        {
            "Arn": "arn:aws:iotwireless:us-east-1:123456789012:Destination/{{IoTWirelessDestination}}",
            "Name": "{{IoTWirelessDestination}}",
            "Expression": "{{IoTWirelessRule}}",
            "Description": "{{Destination for messages processed using IoTWirelessRule}}",
            "RoleArn": "arn:aws:iam::123456789012:role/{{IoTWirelessDestinationRole}}"
        },
        {
            "Arn": "arn:aws:iotwireless:us-east-1:123456789012:Destination/{{IoTWirelessDestination2}}",
            "Name": "{{IoTWirelessDestination2}}",
            "Expression": "{{IoTWirelessRule2}}",
            "RoleArn": "arn:aws:iam::123456789012:role/{{IoTWirelessDestinationRole}}"
        }
    ]
}
```

### Delete destinations from your AWS account
<a name="iot-wireless-delete-destination"></a>

To delete your destination, pass the name of the destination to be deleted as input to the [`DeleteDestination`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteDestination.html) API operation. The following shows an example CLI command:

**Warning**  
Deletion actions can't be undone. The destination will be permanently removed from your AWS account.

```
aws iotwireless delete-destination --name "{{SidewalkDestination}}"
```

This command doesn't produce any output. You can use the `GetDestination` API or the `ListDestinations` API operation to verify that the destination has been removed from your account.

## AWS IoT Wireless API operations for bulk provisioning Sidewalk devices
<a name="iot-sidewalk-apis-provisioning"></a>

You can perform the following API operations for bulk provisioning your Sidewalk end devices:
+ [`StartWirelessDeviceImportTask`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartWirelessDeviceImportTask.html) API or the [`start-wireless-device-import-task`](https://docs.aws.amazon.com/cli/latest/reference/start-wireless-device-import-task.html) CLI
+ [`StartSingleWirelessDeviceImportTask`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartSingleWirelessDeviceImportTask.html) API or the [`start-single-wireless-device-import-task`](https://docs.aws.amazon.com/cli/latest/reference/start-single-wireless-device-import-task.html) CLI
+ [`ListWirelessDeviceImportTasks`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessDeviceImportTasks.html) API or the [`list-wireless-device-import-tasks`](https://docs.aws.amazon.com/cli/latest/reference/list-wireless-device-import-tasks.html) CLI
+ [`ListDevicesForWirelessDeviceImportTask`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDevicesForWirelessDeviceImportTask.html) API or the [`list-devices-for-wireless-device-import-task`](https://docs.aws.amazon.com/cli/latest/reference/list-devices-for-wireless-device-import-task.html) CLI
+ [`GetWirelessDeviceImportTask`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessDeviceImportTask.html) API or the [`get-wireless-device-import-task`](https://docs.aws.amazon.com/cli/latest/reference/get-wireless-device-import-task.html) CLI
+ [`UpdateWirelessDeviceImportTask`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessDeviceImportTask.html) API or the [`update-wireless-device-import-task`](https://docs.aws.amazon.com/cli/latest/reference/update-wireless-device-import-task.html) CLI
+ [`DeleteWirelessDeviceImportTask`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DeleteWirelessDeviceImportTask.html) API or the [`delete-wireless-device-import-task`](https://docs.aws.amazon.com/cli/latest/reference/delete-wireless-device-import-task.html) CLI

The following sections show you how to get, list, update, and delete import tasks. For information about creating import tasks, see [Provisioning Sidewalk devices using import tasks](sidewalk-provision-bulk-import.md).

### Get information about your import task
<a name="iot-sidewalk-get-import-task"></a>

You can use the [`ListDevicesForWirelessDeviceImportTask`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListDevicesForWirelessDeviceImportTask.html) API operation to retrieve information about a particular import task and the onboarding status of devices in that task. As input to the API operation, specify the import task ID that you obtained from either the `StartWirelessDeviceImportTask` or `StartSingleWirelessDeviceImportTask` API operations. The API will then return information about the import task matching the specified identifier.

The following shows an example CLI command:

```
aws iotwireless list-devices-for-wireless-device-import-task --id {{e2a5995e-743b-41f2-a1e4-3ca6a5c5249f}}
```

Running this command returns your import task information and device onboarding status.

```
{
   "DestinationName": "{{SidewalkDestination}}",
   "ImportedWirelessDeviceList": [ 
      {
         "LoRaWAN": "null",
         "Sidewalk": { 
            "OnboardingStatus": "{{ONBOARDED}}",
            "OnboardingStatusReason":"{{null}}",
            "LastUpdateTime": "{{2023-02021T06:11:09.151Z}}",
            "SidewalkManufacturingSn": "{{82B83C8B35E856F43CE9C3D59B418CC96B996071016DB1C3BE5901F0F3071A4A}}"
         }
      },
      {
         "LoRaWAN": "null",
         "Sidewalk": {
             "OnboardingStatus": "{{PENDING}}",
             "OnboardingStatusReason":"{{null}}",
             "LastUpdateTime": "{{2023-02021T06:22:12.061Z}}",
             "SidewalkManufacturingSn": "{{12345ABCDE6789FABDESBDEF123456789012345FEABC0123679AFEBC01234EF}}"
         }
      }
   ],
   "NextToken": "{{null}}",
   "Positioning": "{{Enabled}}",
   "Sidewalk": {
        Positioning": {
            "DestinationName": "{{SidewalkLocationDestination}}"
        }
   }
}
```

### Get import task device summary
<a name="iot-sidewalk-get-device-summary"></a>

To get a count of summary information of the onboarding status of devices that you added to a particular import task, use the [`GetWirelessDeviceImportTask`](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetWirelessDeviceImportTask.html) API operation. The following shows an example CLI command.

```
aws iotwireless get-wireless-device-import-task --Id {{"e2a5995e-743b-41f2-a1e4-3ca6a5c5249f"}}
```

The following code shows a sample response from the command.

```
{

                "Arn": "arn:aws:iotwireless:us-east-1:123456789012:ImportTask
                    /{{12345678-1234-5678-1234-123456789012}}",
                "CreationTime": "{{2025-09-17T22:13:57.306Z}}",
                "DestinationName": "{{DestinationTest}}",
                "FailedImportedDeviceCount": "{{1}}",
                "Id": "{{12345678-1234-5678-1234-123456789012}}",
                "InitializedImportedDeviceCount": "{{0}}",
                "LoRaWAN": null,
                "OnboardedImportedDeviceCount": "{{0}}",
                "PendingImportedDeviceCount": "{{0}}",
                "Positioning": "{{null}}",
                "Sidewalk": {
                    "DeviceCreationFileList": "{{[]}}",
                    "Positioning": {
                        "DestinationName": "{{null}}"
                    },
                    "Role": "{{null}}"
                },
                "Status": "{{INITIALIZED}}",
                "StatusReason": "{{null}}"
}
```

### Add devices to import task
<a name="iot-sidewalk-update-import-task"></a>

Use the `UpdateWirelessDeviceImportTask` API operation to add devices to an existing import task that you added. You can use this API operation to add the serial numbers (SMSN) of devices that were not previously included the task that you created using the `StartWirelessDeviceImportTask` API operation.

To append devices to the import task, as part of the API request, specify a new CSV file in an Amazon S3 bucket that contains the serial numbers of devices to be added. The request will be accepted only if the onboarding process hasn't already started for devices that are currently in the import task. If the onboarding process has already started, then the `UpdateWirelessDeviceImportTask` API request will fail.

If you still want to append devices to the import task, you can perform the `UpdateWirelessDeviceImportTask` API operation a second time. Before you perform this API operation, the first `UpdateWirelessDeviceImportTask` API request must have completed processing the CSV file in the S3 bucket.

**Note**  
When you perform a `ListImportedWirelessDeviceTasks` API request, the S3 URL of the new CSV file specified using the `UpdateWirelessDeviceImportTask` API operation is currently not returned. Instead, the API operation returns the S3 URL of the request sent originally using the `StartWirelessDeviceImportTask` API request.

 The following shows an example CLI command.

```
aws iotwireless update-wireless-device-import task \
    --Id {{"e2a5995e-743b-41f2-a1e4-3ca6a5c5249f"}} \
    --sidewalk '{"FileForCreateDevices": "s3://{{import_task_bucket}}/{{import_file3}}"}'
```

### List import tasks in your AWS account
<a name="iot-sidewalk-list-import-tasks"></a>

Use the `ListWirelessDeviceImportTasks` API or the `list-imported-wireless-device-tasks` CLI command to list import tasks in your AWS account. The following shows an example CLI command.

```
aws iotwireless list-wireless-device-import-tasks
```

Running this command returns a list of import tasks that you created. The list includes their Amazon S3 CSV files and the IAM role that was specified, the import task ID, and summary information of the device onboarding status.

```
{
   "WirelessDeviceImportTaskList": [
      {
         "Arn": "arn:aws:iotwireless:us-east-1:123456789012:ImportTask
                /{{12345678-1234-5678-1234-123456789012}}",
         "Id": "{{12345678-1234-5678-1234-123456789012}}",
         "DestinationName": "{{DestinationName}}",
         "InitializedImportedDeviceCount": "{{0}}",
         "LoRaWAN": null,
         "FailedImportedDeviceCount": "{{1}}",
         "OnboardedImportedDeviceCount": "{{2}}",
         "PendingImportedDeviceCount": "{{3}}",
         "Positioning": "{{Enabled}}",
         "Sidewalk": {
                    "DeviceCreationFileList": ["s3://{{import_task_bucket}}/{{import_file1}}"],
                    "Positioning": {
                        "DestinationName": "{{SidewalkLocationDestination}}",
                    },
                    "Role": "arn:aws:iam::{{123456789012}}:role/{{service-role}}/{{ACF1zBEI}}",
                    }
         "Status": "{{INITIALIZED}}",
         "StatusReason": "{{null}}",
         "CreationTime": "{{1012202218:23:55}}",
      }
   ]
}
```

### Delete import tasks from your AWS account
<a name="iot-sidewalk-delete-import-task"></a>

To delete an import task, pass the import task ID to the `DeleteWirelessDeviceImportTask` API operation or the `delete-wireless-device-import-task` CLI command.

**Warning**  
Deletion actions can't be undone. The import task will be permanently removed from your AWS account.

When you perform the `DeleteWirelessDeviceImportTask` API request, a background process starts deleting the import task. When the request is in progress, the serial numbers (SMSN) of devices in the import tasks are in the process of deletion. Only after the deletion has completed, you'll be able to see this information using the `ListImportedWirelessDeviceTasks` or the `GetImportedWirelessDeviceTasks` API operations.

If an import task still contains devices that are waiting to be onboarded, the `DeleteWirelessDeviceImportTask` API request will be processed only after all the devices in the import task have either onboarded or failed to onboard. An import task expires after 90 days, and once the task has expired, it can be deleted from your account. However, devices that were onboarded successfully using the import task will not be deleted.

**Note**  
If you attempt to create another import task that includes the serial number of a device that's pending deletion using the `DeleteWirelessDeviceImportTask` API request, then the `StartWirelessDeviceImportTask` API operation will return an error.

The following shows an example CLI command:

```
aws iotwireless delete-import-task --Id "{{e2a5995e-743b-41f2-a1e4-3ca6a5c5249f}}"
```

This command doesn't produce any output. After the task has been deleted, to verify that the import task has been removed from your account, you can use the `GetWirelessDeviceImportTask` API operation or the `ListWirelessDeviceImportTasks` API operation.