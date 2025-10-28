# Provisioning Sidewalk devices

using import tasks

This section shows how you can provision Sidewalk devices in bulk using the
AWS IoT console, or the AWS IoT Core for Amazon Sidewalk API operations, or the AWS CLI. The following
sections explain how to bulk provision your Sidewalk devices.

###### Topics

- [How Sidewalk bulk provisioning
  works](#provision-bulk-works "#provision-bulk-works")
- [Key considerations for
  Sidewalk bulk provisioning](#provision-bulk-considerations "#provision-bulk-considerations")
- [CSV file format](#provision-csv-format "#provision-csv-format")
- [How to use Sidewalk bulk
  provisioning](#provision-bulk-use "#provision-bulk-use")
- [Provision Sidewalk devices in
  bulk](sidewalk-bulk-provision-how.md "sidewalk-bulk-provision-how.md")
- [View import task and device
  onboarding status](sidewalk-bulk-provision-status.md "sidewalk-bulk-provision-status.md")

## How Sidewalk bulk provisioning

works

The following steps illustrate how bulk provisioning works.

1. ###### Starting wireless device import task

To provision Sidewalk devices in bulk, you must create an import
task and provide the Sidewalk manufacturing serial number (SMSN) of
the devices to be onboarded to AWS IoT Core for Amazon Sidewalk. You obtained the
Sidewalk manufacturing serial number (SMSN) of the devices as a CSV
file in your email after the manufacturer uploaded the control logs to
Amazon Sidewalk. For more information about the workflow and how you obtain the
control log, see [Manufacturing Amazon Sidewalk devices](https://docs.sidewalk.amazon/manufacturing/ "https://docs.sidewalk.amazon/manufacturing/") in the _Amazon Sidewalk documentation_. 2. ###### Running import process in background

When AWS IoT Core for Amazon Sidewalk receives the import task request, it starts setting
things up and starts a background process that polls the system frequently.
Once the background process receives the import task instruction, it starts
reading the CSV file. AWS IoT Core for Amazon Sidewalk simultaneously checks whether the
control logs have been received from Amazon Sidewalk. 3. ###### Creating wireless device records

When the control log is received from Amazon Sidewalk, AWS IoT Core for Amazon Sidewalk checks
whether the serial numbers in the control log match the SMSN values in the
CSV file. If the serial numbers match, AWS IoT Core for Amazon Sidewalk will start creating
wireless device records for the Sidewalk devices that correspond to
these serial numbers. Once all the devices have been onboarded, the import
task is marked as _Completed_.

## Key considerations for

Sidewalk bulk provisioning

When provisioning your Sidewalk devices in bulk to AWS IoT Core for Amazon Sidewalk,
following are some key considerations.

- You must perform bulk provisioning using the AWS IoT console or the
  AWS IoT Core for Amazon Sidewalk API operations in the same AWS account where you created
  the device profile.
- Before you bulk provision your Sidewalk devices, your device
  profile must already contain DAK information that indicates factory support.
  Otherwise, bulk provisioning using the AWS IoT console, or the bulk
  provisioning API operations can fail.
- After you start an import task, it can take at least 10 minutes or longer
  to process the CSV file, import the wireless devices, and onboard them to
  AWS IoT Core for Amazon Sidewalk.
- The wireless device import task will run for 90 days, once started. During
  this time, it checks whether the control logs have been received from Amazon
  Sidewalk. If the control log is not received from Amazon Sidewalk before
  90 days, the task will be marked as _Completed_ with a message indicating that it has expired when
  you view the task details. The onboarding status of the devices in the
  import task that were waiting for the control log will be marked as
  _Failed_.
- When you attempt to update an import task that you've already created, you
  can only add additional devices to the task. You can add new devices anytime
  after creating an import task and before the task has started on devices
  that were already added to the import task. If the update file contains
  serial numbers of devices that already exist in the original import task,
  these serial numbers will be ignored.
- When you request an update operation, the same IAM role as the one you
  used when creating the import task will be assumed to access the CSV file in
  the Amazon S3 bucket.
- An import task can be deleted only if the task has already completed
  successfully or if the task failed to update. A task might fail to update in
  cases such as when an incorrect IAM role was provided or when an Amazon S3
  bucket file wasn't found. An import task cannot be updated or deleted if it
  is in the `PENDING` state.
- The CSV file that you import to the task must use the format described in
  the following section.

## CSV file format

The CSV file that's contained in an Amazon S3 bucket that you specify for the import
task must use the following format:

- Row 1 must use the keyword `smsn`, which indicates that the CSV
  file being imported contains the SMSN of the devices to be imported.
- Rows 2 and after must contain the SMSN of the devices to be onboarded. The
  device SMSN must be in the 64 hex character format.

This JSON file shows a sample CSV file format.

```
smsn
1C1A10B0AC0A200C012BBAC2CBB1B21CB12C0CA2AC1C1BB22CAA01C1B0B01122
B122C2B1121BACA2221001AC1B22012AAC11112C11C2A100C1C2B012A1100C10
02B222C110B0A210B0A0C2C112CCCAC21C1C0B0AA1221AB1022A2CC11B1B1122
C2C021CA1C111CCAB1221C0021C1C2AAA0AA1A2A01ABC10CBAACCA2A0121022A
0CB22C01BBC2CA2C0B11001121ACB2ABB0BB0121C2BA101C012CC2B20C011AC0
```

## How to use Sidewalk bulk

provisioning

The following steps show you how to use Amazon Sidewalk bulk provisioning.

1. ###### Provide device serial numbers

To provision your Sidewalk devices, you must provide the serial
numbers of the devices to be onboarded. You can provision your devices using
either of the following methods.

    * Provision each device individually using their Sidewalk
     manufacturing serial number (SMSN). This method is useful when you
     want to test the workflow and onboard your device faster without
     having to upload a CSV file with the appropriate IAM role, or
     waiting for the devices to be ready to be onboarded to the
     task.
    * Provision devices in bulk by providing an Amazon S3 bucket URL that
     contains the SMSN of the devices to be provisioned in a CSV file.
     This method is especially useful when you have a large number of
     devices to be onboarded. In this case, onboarding each device
     individually can be tedious. Instead, you only need to provide the
     path to the CSV file that has been uploaded to an Amazon S3 bucket, and
     the IAM role to access the file.

2. ###### Obtain import task and device onboarding status

For each import task that you create, you can retrieve information about
the task onboarding status and the onboarding status of devices added to the
task. You can also see additional status information, such as a reason as to
why a task or device onboarding failed. For more information, see 3. ###### (Optional) Update or delete import task

You can update or delete an import task that you've already
created.

    * You can update an import task and add additional devices to the
     task anytime before the task has started on devices that have
     already been added. AWS IoT Core for Amazon Sidewalk assumes the same IAM role as
     the one that you used when creating the import task. When you create
     the task, specify the new CSV file that contains the serial numbers
     of devices that you want to add to the task.


    ###### Note

    When you're updating an existing import task, you can only add
     devices to the task. AWS IoT Core for Amazon Sidewalk performs a union operation
     between the devices that are already in the import task and the
     devices that you're attempting to add to the task. If the new
     file contains serial numbers of devices that already exist in
     the import task, these serial numbers will be ignored.
    * You can delete an import task that has already completed
     successfully, or an import task that failed to update in cases such
     as when the IAM role information is incorrect, or when an S3
     bucket file isn't available when creating or updating a task.

###### Topics

- [Provision Sidewalk devices in
  bulk](sidewalk-bulk-provision-how.md "sidewalk-bulk-provision-how.md")
- [View import task and device
  onboarding status](sidewalk-bulk-provision-status.md "sidewalk-bulk-provision-status.md")
