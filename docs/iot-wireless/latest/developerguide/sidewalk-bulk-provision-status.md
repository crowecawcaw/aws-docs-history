# View import task and device

onboarding status

Your wireless device import tasks and Sidewalk devices that you've added to
the task can have one of the following status messages. You'll see these messages
displayed in the AWS IoT console, or when you use any of the AWS IoT Wireless API
operations or AWS CLI commands to retrieve information about these tasks and their
devices.

## View import task status

information

After you've created an import task, you can view the import task that you created
and the onboarding status of devices added to the task. The onboarding status
indicates the number of devices that are pending onboarding, the number of devices
that have been onboarded successfully, and the number of devices that failed to
onboard.

When an import task has just been created, the **Pending count**
will display a value that corresponds to the number of devices that were added. Once
the task starts and reads the CSV file to create the wireless device records, the
**Pending count** will decrease, and the **Success
count** will increase as the devices are onboarded successfully. If any
device fails to onboard, the **Failed count** will increase.

To view the import task and device onboarding status:

- ###### Using the AWS IoT console

In the [Sidewalk
devices hub](https://console.aws.amazon.com/iot/home#/wireless/devices?tab=sidewalk "https://console.aws.amazon.com/iot/home#/wireless/devices?tab=sidewalk") of the AWS IoT console, you can see the import
tasks that you created and a count of the summary of the onboarding
status information of your devices. If you view the details of any of
the import tasks that you created, you can see additional information
about the device onboarding status.

- ###### Using the AWS IoT Wireless API or AWS CLI

To view the device onboarding status, use any of the following
AWS IoT Wireless API operations or the corresponding AWS CLI command.
.

    + ###### [`ListWirelessDeviceImportTasks`](../apireference/API_ListWirelessDeviceImportTasks.md "../apireference/API_ListWirelessDeviceImportTasks.md") API
     or [`list-wireless-device-import-tasks`](../../../cli/latest/reference/list-wireless-device-import-tasks.md "../../../cli/latest/reference/list-wireless-device-import-tasks.md")
     CLI


    This API operation returns information about all the import
     tasks that have been added to your account for
     AWS IoT Wireless and their status. It also returns a count of
     the summary of onboarding status of Sidewalk devices in
     these tasks.
    + ###### [`ListDevicesForWirelessDeviceImportTask`](../apireference/API_ListDevicesForWirelessDeviceImportTask.md "../apireference/API_ListDevicesForWirelessDeviceImportTask.md")
     API or [`list-devices-for-wireless-device-import-task`](../../../cli/latest/reference/list-devices-for-wireless-device-import-task.md "../../../cli/latest/reference/list-devices-for-wireless-device-import-task.md")
     CLI


    This API operation returns information about the specified
     import task and its status, and information about all
     Sidewalk devices that have been added to the import task
     and their onboarding status information.
    + ###### [`GetWirelessDeviceImportTask`](../apireference/API_GetWirelessDeviceImportTask.md "../apireference/API_GetWirelessDeviceImportTask.md") API or
     [`get-wireless-device-import-task`](../../../cli/latest/reference/get-wireless-device-import-task.md "../../../cli/latest/reference/get-wireless-device-import-task.md")
     CLI


    This API operation returns information about the specified
     import task and its status, and a count of the summary of
     onboarding status of Sidewalk devices in that
     task.

## Import task status

The import tasks that you have created in your AWS account can have one of
the following status messages. The status indicates whether your import task has
started processing, or has completed, or failed. You can also use the AWS IoT
console or the `StatusReason` parameter of any of the
AWS IoT Wireless API operations to retrieve additional status details.

- ###### INITIALIZING

AWS IoT Core for Amazon Sidewalk has received the wireless device import task
request and is in the process of setting up the task.

- ###### INITIALIZED

AWS IoT Core for Amazon Sidewalk has completed setting up the import task and is
waiting for the control log to arrive so that it can import the
devices using their serial numbers (SMSN) and continue processing
the task.

- ###### PENDING

The import task is waiting in the queue to be processed.
AWS IoT Core for Amazon Sidewalk is evaluating other tasks that are in the processing
queue.

- ###### COMPLETE

The import task has been processed and completed.

- ###### FAILED

The import task or device task failed. You can use the
`StatusReason` parameter to identify why the import
task failed, such as a validation exception.

- ###### DELETING

The import task has been marked for deletion and is in the process
of being deleted.

## Device onboarding

status

The Sidewalk devices that you added to your import task can have one of
the following status messages. The status indicates whether your devices are
ready to be onboarded, or has onboarded, or failed to onboard. You can also use
the AWS IoT console or the `OnboardingStatusReason` parameter of the
AWS IoT Wireless API operation,
`ListDevicesForWirelessDeviceImportTask`, to retrieve additional
status details.

- ###### INITIALIZED

AWS IoT Core for Amazon Sidewalk has completed setting up the import task and is
waiting for the control log to arrive so that it can import the
devices using their serial numbers (SMSN) and continue processing
the task.

- ###### PENDING

The import task is waiting in the queue to be processed and to
start onboarding your devices to the task. AWS IoT Core for Amazon Sidewalk is
evaluating other tasks that are in the processing queue.

- ###### ONBOARDED

The Sidewalk device has been successfully onboarded to the
import task.

- ###### FAILED

The import task or device task failed, and the Sidewalk
device failed to onboard to the task. You can use the
`OnboardingStatusReason` parameter to retrieve
additional details about why the device onboarding failed.
