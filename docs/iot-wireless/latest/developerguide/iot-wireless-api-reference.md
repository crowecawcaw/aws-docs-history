# AWS IoT Wireless API operations

You can perform the following additional API operations when onboarding your LoRaWAN or
Sidewalk end devices, or when creating an import task for provisioning
Sidewalk end devices in bulk.

The following sections contain additional information about these API operations.

You can perform the following API operations for yourLoRaWAN and Sidewalk
device profiles:

- [`CreateDeviceProfile`](../../2020-11-22/apireference/API_CreateDeviceProfile.md "../../2020-11-22/apireference/API_CreateDeviceProfile.md") API or the [`create-device-profile`](../../../cli/latest/reference/iotwireless/create-device-profile.md "../../../cli/latest/reference/iotwireless/create-device-profile.md") CLI
- [`GetDeviceProfile`](../../2020-11-22/apireference/API_GetDeviceProfile.md "../../2020-11-22/apireference/API_GetDeviceProfile.md") API or the [`get-device-profile`](../../../cli/latest/reference/iotwireless/get-device-profile.md "../../../cli/latest/reference/iotwireless/get-device-profile.md") CLI
- [`ListDeviceProfiles`](../../2020-11-22/apireference/API_ListDeviceProfiles.md "../../2020-11-22/apireference/API_ListDeviceProfiles.md") API or the [`list-device-profiles`](../../../cli/latest/reference/iotwireless/list-device-profiles.md "../../../cli/latest/reference/iotwireless/list-device-profiles.md") CLI
- [`DeleteDeviceProfile`](../../2020-11-22/apireference/API_DeleteDeviceProfile.md "../../2020-11-22/apireference/API_DeleteDeviceProfile.md") API or the [`delete-device-profile`](../../../cli/latest/reference/iotwireless/get-device-profile.md "../../../cli/latest/reference/iotwireless/get-device-profile.md") CLI
  The following sections show you how to list and delete profiles. For information
  about creating and retrieving device profiles, see:

- [Add device profiles](lorawan-define-profiles.md#lorawan-device-profiles "lorawan-define-profiles.md#lorawan-device-profiles")
- [Step 1: Create a device
  profile](iot-sidewalk-add-device.md#iot-sidewalk-profile-create "iot-sidewalk-add-device.md#iot-sidewalk-profile-create")

### List device profiles in your

AWS account

You can use the [`ListDeviceProfiles`](../../2020-11-22/apireference/API_ListDeviceProfiles.md "../../2020-11-22/apireference/API_ListDeviceProfiles.md") API operation to list device
profiles in your AWS account that you added to AWS IoT Wireless. You can use
this information to identify the devices that you want to associate this profile
to.

To filter the list to display only LoRaWAN or Sidewalk device
profiles, set the `Type` when running the API. Following shows an
example CLI command:

```
aws iotwireless list-device-profiles --wireless-device-type "Sidewalk"
```

Running this command returns a list of device profiles that you added,
including their profile identifier and Amazon Resource Name (ARN). To retrieve
additional details about a specific profile, use the
`GetDeviceProfile` API.

```
{
    "DeviceProfileList": [
        {
            "Name": "`SidewalkDeviceProfile1`",
            "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d",
            "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:DeviceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d"
        },
        {
            "Name": "`SidewalkDeviceProfile2`",
            "Id": "a1b2c3d4-5678-90ab-cdef-12ab345c67de",
            "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:DeviceProfile/a1b2c3d4-5678-90ab-cdef-12ab345c67de"
        }
    ]
}
```

### Delete device profiles from your

AWS account

You can delete your device profiles using the [`DeleteDeviceProfile`](../../2020-11-22/apireference/API_DeleteDeviceProfile.md "../../2020-11-22/apireference/API_DeleteDeviceProfile.md") API operation. The following
shows an example CLI command:

###### Warning

Deletion actions can't be undone. The device profile will be permanently
removed from your AWS account.

```
aws iotwireless delete-device-profile --name "`SidewalkProfile`"
```

This command doesn't produce any output. You can use the
`GetDeviceProfile` API or the `ListDeviceProfiles` API
operation to verify that the profile has been removed from your account.

You can perform the following API operations for your LoRaWAN and
Sidewalk devices:

- [`CreateWirelessDevice`](../../2020-11-22/apireference/API_CreateWirelessDevice.md "../../2020-11-22/apireference/API_CreateWirelessDevice.md") API or the [`create-wireless-device`](../../../cli/latest/reference/create-wireless-device.md "../../../cli/latest/reference/create-wireless-device.md") CLI
- [`GetWirelessDevice`](../../2020-11-22/apireference/API_GetWirelessDevice.md "../../2020-11-22/apireference/API_GetWirelessDevice.md") API or the [`get-wireless-device`](../../../cli/latest/reference/get-wireless-device.md "../../../cli/latest/reference/get-wireless-device.md") CLI
- [`ListWirelessDevices`](../../2020-11-22/apireference/API_ListWirelessDevices.md "../../2020-11-22/apireference/API_ListWirelessDevices.md") API or the [`list-wireless-devices`](../../../cli/latest/reference/list-wireless-devices.md "../../../cli/latest/reference/list-wireless-devices.md") CLI
- [`DeleteWirelessDevice`](../../2020-11-22/apireference/API_DeleteWirelessDevice.md "../../2020-11-22/apireference/API_DeleteWirelessDevice.md") API or the [`delete-wireless-device`](../../../cli/latest/reference/delete-wireless-device.md "../../../cli/latest/reference/delete-wireless-device.md") CLI
- [`UpdateWirelessDevice`](../../2020-11-22/apireference/API_UpdateWirelessDevice.md "../../2020-11-22/apireference/API_UpdateWirelessDevice.md") API or the [`update-wireless-device`](../../../cli/latest/reference/update-wireless-device.md "../../../cli/latest/reference/update-wireless-device.md") CLI
- [`AssociateWirelessDeviceWithThing`](../../2020-11-22/apireference/API_AssociateWirelessDeviceWithThing.md "../../2020-11-22/apireference/API_AssociateWirelessDeviceWithThing.md") API or the
  [`associate-wireless-device-with-thing`](../../../cli/latest/reference/associate-wireless-device-with-thing.md "../../../cli/latest/reference/associate-wireless-device-with-thing.md")
  CLI
- [`DisassociateWirelessDeviceFromThing`](../../2020-11-22/apireference/API_DisassociateWirelessDeviceFromThing.md "../../2020-11-22/apireference/API_DisassociateWirelessDeviceFromThing.md") API or the
  [`disassociate-wireless-device-from-thing`](../../../cli/latest/reference/disassociate-wireless-device-from-thing.md "../../../cli/latest/reference/disassociate-wireless-device-from-thing.md")
  CLI
  The following sections show you how to list and delete devices. For information
  about creating wireless devices and retrieving device information, see:

- [Add your wireless device to
  AWS IoT Core for LoRaWAN](lorawan-end-devices-add.md "lorawan-end-devices-add.md")
- [Step 2: Add your
  Sidewalk device](iot-sidewalk-add-device.md#iot-sidewalk-device-create "iot-sidewalk-add-device.md#iot-sidewalk-device-create")

### Associate wireless devices in

your AWS account to an IoT thing

To associate your LoRaWAN and Sidewalk devices with an AWS IoT thing,
use the `AssociateWirelessDeviceWithThing` API operation.

Things in AWS IoT make it easier to search and manage your devices. Associating
a thing with your device lets the device access other AWS IoT Core features. For
more information about using this API, see [`AssociateWirelessDeviceWithThing`](../../2020-11-22/apireference/API_AssociateWirelessDeviceWithThing.md "../../2020-11-22/apireference/API_AssociateWirelessDeviceWithThing.md").

The following shows an example of running this command. Running this command
doesn't produce any output.

```
aws iotwireless associate-wireless-device-with-thing \
    --id `"12345678-a1b2-3c45-67d8-e90fa1b2c34d"` \
    --thing-arn "arn:aws:iot:`us-east-1:123456789012:`thing/`MySidewalkThing`"
```

To disassociate your wireless device from an AWS IoT thing, use the [`DisassociateWirelessDeviceFromThing`](../../2020-11-22/apireference/API_DisassociateWirelessDeviceFromThing.md "../../2020-11-22/apireference/API_DisassociateWirelessDeviceFromThing.md") API operation,
as shown in the following example.

```
aws iotwireless disassociate-wireless-device-from-thing \
    --id `"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`
```

### List wireless devices in your

AWS account

To list wireless devices in your AWS account that you added to
AWS IoT Wireless, use the [`ListWirelessDevices`](../../2020-11-22/apireference/API_ListWirelessDevices.md "../../2020-11-22/apireference/API_ListWirelessDevices.md") API operation. To filter the
list to return only LoRaWAN or Sidewalk devices, set the
`WirelessDeviceType`.

The following shows an example of running this command:

```
aws iotwireless list-wireless-devices --wireless-device-type Sidewalk
```

Running this command returns a list of devices that you added, including their
profile identifier and the Amazon Resource Name (ARN). To retrieve additional
details about a specific device, use the [`GetWirelessDevice`](../../2020-11-22/apireference/API_GetWirelessDevice.md "../../2020-11-22/apireference/API_GetWirelessDevice.md") API operation.

```
{
    "WirelessDeviceList": [
        {
            "Name": "`mySidewalkDevice`",
            "DestinationName": "`SidewalkDestination`",
            "Id": "1ffd32c8-8130-4194-96df-622f072a315f",
            "Type": "Sidewalk",
            "Sidewalk": {
                "SidewalkId": "`1234567890123456`"
            },
            "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:WirelessDevice/1ffd32c8-8130-4194-96df-622f072a315f"
        }
    ]
}
```

### Delete wireless devices from your

AWS account

To delete your wireless devices, pass the `WirelessDeviceID` of the
devices you want to delete to the [`DeleteWirelessDevice`](../../2020-11-22/apireference/API_DeleteWirelessDevice.md "../../2020-11-22/apireference/API_DeleteWirelessDevice.md") API operation.

The following shows an example command:

```
aws iotwireless delete-wireless-device --id "`23456789-abcd-0123-bcde-fabc012345678`"
```

This command doesn't produce any output. You can use the
`GetWirelessDevice` API or the `ListWirelessDevices`
API operation to verify that the device has been removed from your
account.

You can perform the following API operations for destinations for your LoRaWAN
and Sidewalk devices:

- [`CreateDestination`](../../2020-11-22/apireference/API_CreateDestination.md "../../2020-11-22/apireference/API_CreateDestination.md") API or the [`create-destination`](../../../cli/latest/reference/create-destination.md "../../../cli/latest/reference/create-destination.md") CLI
- [`GetDestination`](../../2020-11-22/apireference/API_GetDestination.md "../../2020-11-22/apireference/API_GetDestination.md") API or the [`get-destination`](../../../cli/latest/reference/get-destination.md "../../../cli/latest/reference/get-destination.md") CLI
- [`UpdateDestination`](../../2020-11-22/apireference/API_UpdateDestination.md "../../2020-11-22/apireference/API_UpdateDestination.md") API or the [`update-destination`](../../../cli/latest/reference/update-destination.md "../../../cli/latest/reference/update-destination.md") CLI
- [`ListDestinations`](../../2020-11-22/apireference/API_ListDestinations.md "../../2020-11-22/apireference/API_ListDestinations.md") API or the [`list-destinations`](../../../cli/latest/reference/list-destinations.md "../../../cli/latest/reference/list-destinations.md") CLI
- [`DeleteDestination`](../../2020-11-22/apireference/API_DeleteDestination.md "../../2020-11-22/apireference/API_DeleteDestination.md") API or the [`delete-destination`](../../../cli/latest/reference/delete-destination.md "../../../cli/latest/reference/delete-destination.md") CLI
  The following sections show you how to get, list, update, and delete destinations.
  For information about creating destinations, see [Add a destination for your
  Sidewalk end device](iot-sidewalk-qsg-destination.md "iot-sidewalk-qsg-destination.md").

### Get information about your

destination

You can use the [`GetDestination`](../../2020-11-22/apireference/API_GetDestination.md "../../2020-11-22/apireference/API_GetDestination.md") API operation to get information
about the destination that you added to your account for AWS IoT Wireless.
Provide the destination name as input to the API. The API will return
information about the destination matching the specified identifier.

The following shows an example CLI command:

```
aws iotwireless get-destination --name `SidewalkDestination`
```

Running this command returns the parameters of your destination.

```
{
    "Arn": "arn:aws:iotwireless:`us-east-1`:`123456789012`:Destination/IoTWirelessDestination",
    "Name": "`SidewalkDestination`",
    "Expression": "`IoTWirelessRule`",
    "ExpressionType": "`RuleName`",
    "RoleArn": "arn:aws:iam::`123456789012`:role/`IoTWirelessDestinationRole`"
}
```

### Update properties of your

destination

Use the [`UpdateDestination`](../../2020-11-22/apireference/API_UpdateDestination.md "../../2020-11-22/apireference/API_UpdateDestination.md") API operation to update
properties of your destination that you added to your account for
AWS IoT Wireless. The following shows an example CLI command that updates the
description property:

```
aws iotwireless update-destination --name `SidewalkDestination` \
    --description `"Destination for messages processed using IoTWirelessRule"`
```

### List destinations in your

AWS account

Use the [`ListDestinations`](../../2020-11-22/apireference/API_ListDestinations.md "../../2020-11-22/apireference/API_ListDestinations.md") API operation to list
destinations in your AWS account that you added to AWS IoT Wireless. To
filter the list to return only destinations for LoRaWAN and Sidewalk
end devices, use the `WirelessDeviceType` parameter.

The following shows an example CLI command:

```
aws iotwireless list-destinations --wireless-device-type "Sidewalk"
```

Running this command returns a list of destinations that you added, including
their Amazon Resource Name (ARN). To retrieve additional details about a
specific destination, use the `GetDestination` API.

```
{
    "DestinationList": [
        {
            "Arn": "arn:aws:iotwireless:us-east-1:123456789012:Destination/`IoTWirelessDestination`",
            "Name": "`IoTWirelessDestination`",
            "Expression": "`IoTWirelessRule`",
            "Description": "`Destination for messages processed using IoTWirelessRule`",
            "RoleArn": "arn:aws:iam::123456789012:role/`IoTWirelessDestinationRole`"
        },
        {
            "Arn": "arn:aws:iotwireless:us-east-1:123456789012:Destination/`IoTWirelessDestination2`",
            "Name": "`IoTWirelessDestination2`",
            "Expression": "`IoTWirelessRule2`",
            "RoleArn": "arn:aws:iam::123456789012:role/`IoTWirelessDestinationRole`"
        }
    ]
}
```

### Delete destinations from your

AWS account

To delete your destination, pass the name of the destination to be deleted as
input to the [`DeleteDestination`](../../2020-11-22/apireference/API_DeleteDestination.md "../../2020-11-22/apireference/API_DeleteDestination.md") API operation. The following
shows an example CLI command:

###### Warning

Deletion actions can't be undone. The destination will be permanently
removed from your AWS account.

```
aws iotwireless delete-destination --name "`SidewalkDestination`"
```

This command doesn't produce any output. You can use the
`GetDestination` API or the `ListDestinations` API
operation to verify that the destination has been removed from your
account.

You can perform the following API operations for bulk provisioning your
Sidewalk end devices:

- [`StartWirelessDeviceImportTask`](../../2020-11-22/apireference/API_StartWirelessDeviceImportTask.md "../../2020-11-22/apireference/API_StartWirelessDeviceImportTask.md") API or the
  [`start-wireless-device-import-task`](../../../cli/latest/reference/start-wireless-device-import-task.md "../../../cli/latest/reference/start-wireless-device-import-task.md") CLI
- [`StartSingleWirelessDeviceImportTask`](../../2020-11-22/apireference/API_StartSingleWirelessDeviceImportTask.md "../../2020-11-22/apireference/API_StartSingleWirelessDeviceImportTask.md") API or the
  [`start-single-wireless-device-import-task`](../../../cli/latest/reference/start-single-wireless-device-import-task.md "../../../cli/latest/reference/start-single-wireless-device-import-task.md")
  CLI
- [`ListWirelessDeviceImportTasks`](../../2020-11-22/apireference/API_ListWirelessDeviceImportTasks.md "../../2020-11-22/apireference/API_ListWirelessDeviceImportTasks.md") API or the
  [`list-wireless-device-import-tasks`](../../../cli/latest/reference/list-wireless-device-import-tasks.md "../../../cli/latest/reference/list-wireless-device-import-tasks.md") CLI
- [`ListDevicesForWirelessDeviceImportTask`](../../2020-11-22/apireference/API_ListDevicesForWirelessDeviceImportTask.md "../../2020-11-22/apireference/API_ListDevicesForWirelessDeviceImportTask.md") API or
  the [`list-devices-for-wireless-device-import-task`](../../../cli/latest/reference/list-devices-for-wireless-device-import-task.md "../../../cli/latest/reference/list-devices-for-wireless-device-import-task.md")
  CLI
- [`GetWirelessDeviceImportTask`](../../2020-11-22/apireference/API_GetWirelessDeviceImportTask.md "../../2020-11-22/apireference/API_GetWirelessDeviceImportTask.md") API or the [`get-wireless-device-import-task`](../../../cli/latest/reference/get-wireless-device-import-task.md "../../../cli/latest/reference/get-wireless-device-import-task.md") CLI
- [`UpdateWirelessDeviceImportTask`](../../2020-11-22/apireference/API_UpdateWirelessDeviceImportTask.md "../../2020-11-22/apireference/API_UpdateWirelessDeviceImportTask.md") API or the
  [`update-wireless-device-import-task`](../../../cli/latest/reference/update-wireless-device-import-task.md "../../../cli/latest/reference/update-wireless-device-import-task.md") CLI
- [`DeleteWirelessDeviceImportTask`](../../2020-11-22/apireference/API_DeleteWirelessDeviceImportTask.md "../../2020-11-22/apireference/API_DeleteWirelessDeviceImportTask.md") API or the
  [`delete-wireless-device-import-task`](../../../cli/latest/reference/delete-wireless-device-import-task.md "../../../cli/latest/reference/delete-wireless-device-import-task.md") CLI
  The following sections show you how to get, list, update, and delete import tasks.
  For information about creating import tasks, see [Provisioning Sidewalk devices
  using import tasks](sidewalk-provision-bulk-import.md "sidewalk-provision-bulk-import.md").

### Get information about your import

task

You can use the [`ListDevicesForWirelessDeviceImportTask`](../../2020-11-22/apireference/API_ListDevicesForWirelessDeviceImportTask.md "../../2020-11-22/apireference/API_ListDevicesForWirelessDeviceImportTask.md") API
operation to retrieve information about a particular import task and the
onboarding status of devices in that task. As input to the API operation,
specify the import task ID that you obtained from either the
`StartWirelessDeviceImportTask` or
`StartSingleWirelessDeviceImportTask` API operations. The API
will then return information about the import task matching the specified
identifier.

The following shows an example CLI command:

```
aws iotwireless list-devices-for-wireless-device-import-task --id `e2a5995e-743b-41f2-a1e4-3ca6a5c5249f`
```

Running this command returns your import task information and device
onboarding status.

```
{
   "DestinationName": "`SidewalkDestination`",
   "ImportedWirelessDeviceList": [
      {
         "Sidewalk": {
            "OnboardingStatus": "`ONBOARDED`",
            "LastUpdateTime": "`2023-02021T06:11:09.151Z`",
            "SidewalkManufacturingSn": "`82B83C8B35E856F43CE9C3D59B418CC96B996071016DB1C3BE5901F0F3071A4A`"
         },
         "Sidewalk": {
             "OnboardingStatus": "`PENDING`",
             "LastUpdateTime": "`2023-02021T06:22:12.061Z`",
             "SidewalkManufacturingSn": "`12345ABCDE6789FABDESBDEF123456789012345FEABC0123679AFEBC01234EF`"
         },
      }
   ]
}
```

### Get import task device

summary

To get a count of summary information of the onboarding status of devices that
you added to a particular import task, use the [`GetWirelessDeviceImportTask`](../../2020-11-22/apireference/API_GetWirelessDeviceImportTask.md "../../2020-11-22/apireference/API_GetWirelessDeviceImportTask.md") API operation. The
following shows an example CLI command.

```
aws iotwireless get-wireless-device-import-task --Id `"e2a5995e-743b-41f2-a1e4-3ca6a5c5249f"`
```

The following code shows a sample response from the command.

```
{
   "NumberOfFailedImportedDevices": 2,
   "NumberOfOnboardedImportedDevices": 4,
   "NumberOfPendingImportedDevices": 1
}
```

### Add devices to import

task

Use the `UpdateWirelessDeviceImportTask` API operation to add
devices to an existing import task that you added. You can use this API
operation to add the serial numbers (SMSN) of devices that were not previously
included the task that you created using the
`StartWirelessDeviceImportTask` API operation.

To append devices to the import task, as part of the API request, specify a
new CSV file in an Amazon S3 bucket that contains the serial numbers of devices to be
added. The request will be accepted only if the onboarding process hasn't
already started for devices that are currently in the import task. If the
onboarding process has already started, then the
`UpdateWirelessDeviceImportTask` API request will fail.

If you still want to append devices to the import task, you can perform the
`UpdateWirelessDeviceImportTask` API operation a second time.
Before you perform this API operation, the first
`UpdateWirelessDeviceImportTask` API request must have completed
processing the CSV file in the S3 bucket.

###### Note

When you perform a `ListImportedWirelessDeviceTasks` API
request, the S3 URL of the new CSV file specified using the
`UpdateWirelessDeviceImportTask` API operation is currently
not returned. Instead, the API operation returns the S3 URL of the request
sent originally using the `StartWirelessDeviceImportTask` API
request.

The following shows an example CLI command.

```
aws iotwireless update-wireless-device-import task \
    --Id `"e2a5995e-743b-41f2-a1e4-3ca6a5c5249f"` \
    --sidewalk '{"FileForCreateDevices": "s3://`import_task_bucket`/`import_file3`"}'
```

### List import tasks in your

AWS account

Use the `ListWirelessDeviceImportTasks` API or the
`list-imported-wireless-device-tasks` CLI command to list import
tasks in your AWS account. The following shows an example CLI command.

```
aws iotwireless list-wireless-device-import-tasks
```

Running this command returns a list of import tasks that you created. The list
includes their Amazon S3 CSV files and the IAM role that was specified, the import
task ID, and summary information of the device onboarding status.

```
{
   "ImportWirelessDeviceTaskList": [
      {
         "FileForCreateDevices": "s3://`import_task_bucket`/`import_file1`",
         "ImportTaskId": "`e2a5995e-743b-41f2-a1e4-3ca6a5c5249f`",
         "NumberOfFailedImportedDevices": 1,
         "NumberOfOnboardedImportedDevices": 3,
         "NumberOfPendingImportedDevices": 2,
         "Role": "arn:aws:iam::`123456789012`:role/`service-role`/`ACF1zBEI`",
         "TimeStamp": "1012202218:23:55"
      },
      {
         "FileForCreateDevices": "s3://`import_task_bucket`/`import_file2`",
         "ImportTaskId": "`a1b234c5-67ef-21a2-a1b2-3cd4e5f6789a`",
         "NumberOfFailedImportedDevices": 2,
         "NumberOfOnboardedImportedDevices": 4,
         "NumberOfPendingImportedDevices": 1,
         "Role": "arn:aws:iam::`123456789012`:role/`service-role`/`CDEFaBC1`",
         "TimeStamp": "1201202210:12:20"
      }
   ]
}
```

### Delete import tasks from your

AWS account

To delete an import task, pass the import task ID to the
`DeleteWirelessDeviceImportTask` API operation or the
`delete-wireless-device-import-task` CLI command.

###### Warning

Deletion actions can't be undone. The import task will be permanently
removed from your AWS account.

When you perform the `DeleteWirelessDeviceImportTask` API request,
a background process starts deleting the import task. When the request is in
progress, the serial numbers (SMSN) of devices in the import tasks are in the
process of deletion. Only after the deletion has completed, you'll be able to
see this information using the `ListImportedWirelessDeviceTasks` or
the `GetImportedWirelessDeviceTasks` API operations.

If an import task still contains devices that are waiting to be onboarded, the
`DeleteWirelessDeviceImportTask` API request will be processed
only after all the devices in the import task have either onboarded or failed to
onboard. An import task expires after 90 days, and once the task has expired, it
can be deleted from your account. However, devices that were onboarded
successfully using the import task will not be deleted.

###### Note

If you attempt to create another import task that includes the serial
number of a device that's pending deletion using the
`DeleteWirelessDeviceImportTask` API request, then the
`StartWirelessDeviceImportTask` API operation will return an
error.

The following shows an example CLI command:

```
aws iotwireless delete-import-task --Id "`e2a5995e-743b-41f2-a1e4-3ca6a5c5249f`"
```

This command doesn't produce any output. After the task has been deleted, to
verify that the import task has been removed from your account, you can use the
`GetWirelessDeviceImportTask` API operation or the
`ListWirelessDeviceImportTasks` API operation.
