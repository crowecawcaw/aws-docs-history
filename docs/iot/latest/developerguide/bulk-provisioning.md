# Bulk registration

You can use the [`start-thing-registration-task`](../apireference/API_StartThingRegistrationTask.md "../apireference/API_StartThingRegistrationTask.md") command to register things in
bulk. This command takes a provisioning template, an S3 bucket name, a key name, and
a role ARN that allows access to the file in the S3 bucket. The file in the S3
bucket contains the values used to replace the parameters in the template. The file
must be a newline-delimited JSON file. Each line contains all of the parameter
values for registering a single device. For example:

```
{"ThingName": "foo", "SerialNumber": "123", "CSR": "csr1"}
{"ThingName": "bar", "SerialNumber": "456", "CSR": "csr2"}
```

The following bulk registration-related API operations might be useful:

- [ListThingRegistrationTasks](../apireference/API_ListThingRegistrationTasks.md "../apireference/API_ListThingRegistrationTasks.md"): Lists the current bulk thing
  provisioning tasks.
- [DescribeThingRegistrationTask](../apireference/API_DescribeThingRegistrationTask.md "../apireference/API_DescribeThingRegistrationTask.md"): Provides information about a
  specific bulk thing registration task.
- [StopThingRegistrationTask](../apireference/API_StopThingRegistrationTask.md "../apireference/API_StopThingRegistrationTask.md"): Stops a bulk thing registration
  task.
- [ListThingRegistrationTaskReports](../apireference/API_ListThingRegistrationTaskReports.md "../apireference/API_ListThingRegistrationTaskReports.md"): Used to check the results and
  failures for a bulk thing registration task.

###### Note

- Only one bulk registration operation task can run at a time (per
  account).
- Bulk registration operations call other AWS IoT control plane API
  operations. These calls might exceed the [AWS IoT Throttling
  Quotas](../../../general/latest/gr/iot-core.md#throttling-limits "../../../general/latest/gr/iot-core.md#throttling-limits") in your account and cause throttle errors. Contact
  [AWS
  Customer Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") to raise your AWS IoT throttling quotas, if
  necessary.
