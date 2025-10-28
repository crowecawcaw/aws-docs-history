# Troubleshoot Amazon EC2 instance launch issues

The following are troubleshooting tips to help you solve issues when launching an Amazon EC2 instance.

###### Launch Issues

- [Invalid device name](#troubleshooting-launch-devicename "#troubleshooting-launch-devicename")
- [Instance limit exceeded](#troubleshooting-launch-limit "#troubleshooting-launch-limit")
- [Insufficient instance capacity](#troubleshooting-launch-capacity "#troubleshooting-launch-capacity")
- [The requested configuration is currently not supported.
  Please check the documentation for supported configurations.](#troubleshooting-instance-configuration "#troubleshooting-instance-configuration")
- [Instance terminates immediately](#troubleshooting-launch-internal "#troubleshooting-launch-internal")
- [Insufficient permissions](#troubleshooting-launch-permissions "#troubleshooting-launch-permissions")
- [High CPU usage shortly after Windows starts (Windows instances only)](#high-cpu-issue "#high-cpu-issue")

## Invalid device name

### Description

You get the `Invalid device name `device_name`` error when you try to launch
a new instance.

### Cause

If you get this error when you try to launch an instance, the device name specified for one or more
volumes in the request has an invalid device name. Possible causes include:

- The device name might be in use by the selected AMI.
- The device name might be reserved for root volumes.
- The device name might be used for another volume in the request.
- The device name might not be valid for the operating system.

### Solution

To resolve the issue:

- Ensure that the device name is not used in the AMI that you selected. Run the following command
  to view the device names used by the AMI.

```
aws ec2 describe-images --image-id `ami-0abcdef1234567890` --query 'Images[*].BlockDeviceMappings[].DeviceName'
```

- Ensure that you are not using a device name that is reserved for root volumes. For more information,
  see [Available device names](device_naming.md#available-ec2-device-names "device_naming.md#available-ec2-device-names").
- Ensure that each volume specified in your request has a unique device name.
- Ensure that the device names that you specified are in the correct format. For more information,
  see [Available device names](device_naming.md#available-ec2-device-names "device_naming.md#available-ec2-device-names").

## Instance limit exceeded

### Description

You get the `InstanceLimitExceeded` error when you try to launch a new instance or restart a stopped instance.

### Cause

If you get an `InstanceLimitExceeded` error when you try to launch a new
instance or restart a stopped instance, you have reached the limit on the number of
instances that you can launch in a Region. When you create your AWS account, we set
default limits on the number of instances you can run on a per-Region basis.

### Solution

You can request an instance limit increase on a per-region basis. For more information, see [Amazon EC2 service quotas](ec2-resource-limits.md "ec2-resource-limits.md").

## Insufficient instance capacity

### Description

You get the `InsufficientInstanceCapacity` error when you try to launch a new instance or restart a stopped instance.

### Cause

If you get this error when you try to launch an instance or restart a stopped instance,
AWS does not currently have enough available On-Demand capacity to fulfill your
request.

### Solution

To resolve the issue, try the following:

- Wait a few minutes and then submit your request again; capacity can shift
  frequently.
- Submit a new request with a reduced number of instances. For example, if you're making a
  single request to launch 15 instances, try making 3 requests for 5 instances, or 15 requests
  for 1 instance instead.
- If you're launching an instance, submit a new request without specifying an Availability
  Zone.
- If you're launching an instance, submit a new request using a different instance type
  (which you can resize at a later stage). For more information, see [Amazon EC2 instance type changes](ec2-instance-resize.md "ec2-instance-resize.md").
- If you are launching instances into a cluster placement group, you can get an insufficient
  capacity error.

## The requested configuration is currently not supported.

Please check the documentation for supported configurations.

### Description

You get the `Unsupported` error when you try to launch a new instance
because the instance configuration is not supported.

### Cause

The error message provides additional details. For example, an instance type or instance
purchasing option might not be supported in the specified Region or Availability
Zone.

### Solution

Try a different instance configuration. To search for an instance type that meets your
requirements, see [Find an Amazon EC2 instance type](instance-discovery.md "instance-discovery.md").

## Instance terminates immediately

### Description

Your instance goes from the `pending` state to the `terminated`
state.

### Cause

The following are a few reasons why an instance might immediately terminate:

- You've exceeded your EBS volume limits. For more information, see [Amazon EBS volume limits for Amazon EC2 instances](volume_limits.md "volume_limits.md").
- An EBS snapshot is corrupted.
- The root EBS volume is encrypted and you do not have permissions to access the
  KMS key for decryption.
- A snapshot specified in the block device mapping for the AMI is encrypted and you
  do not have permissions to access the KMS key for decryption or you do not have access
  to the KMS key to encrypt the restored volumes.
- The Amazon S3-backed AMI that you used to launch the instance is missing a required part (an
  image.part._xx_ file).

For more information, get the termination reason using one of the following methods.

###### To get the termination reason using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**, and select
   the instance.
3. On the first tab, find the reason next to
   **State transition reason**.

###### To get the termination reason using the AWS CLI

1. Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md") command and specify the instance ID.

```
aws ec2 describe-instances --instance-id `i-1234567890abcdef0`
```

2. Review the JSON response returned by the command and note the values in
   the `StateReason` response element.

The following code block shows an example of a `StateReason`
response element.

```
"StateReason": {
  "Message": "Client.VolumeLimitExceeded: Volume limit exceeded",
  "Code": "Server.InternalError"
},
```

###### To get the termination reason using AWS CloudTrail

For more information, see [Viewing
events with CloudTrail event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the
_AWS CloudTrail User Guide_.

### Solution

Depending on the termination reason, take one of the following actions:

- **`Client.VolumeLimitExceeded: Volume limit
exceeded`** — Delete unused volumes. You can [submit a request](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-ebs "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-ebs") to increase your volume
  limit.
- **`Client.InternalError: Client
error on launch`** — Ensure that you have the
  permissions required to access the AWS KMS keys used to decrypt and encrypt volumes.
  For more information, see [Using
  key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

## Insufficient permissions

### Description

You get the `"`errorMessage`": "You are not authorized to
 perform this operation."` error when you try to launch a new instance, and
the launch fails.

### Cause

If you get this error when you try to launch an instance, you don't have the required IAM
permissions to launch the instance.

Possible missing permissions include:

- `ec2:RunInstances`
- `iam:PassRole`

Other permissions might also be missing. For the list of permissions required to launch an
instance, see the example IAM policies under [Example: Use the EC2 launch instance wizard](iam-policies-ec2-console.md#ex-launch-wizard "iam-policies-ec2-console.md#ex-launch-wizard") and [Launch instances (RunInstances)](ExamplePolicies_EC2.md#iam-example-runinstances "ExamplePolicies_EC2.md#iam-example-runinstances").

### Solution

To resolve the issue:

- If you are making requests as an IAM user, verify that you have the
  following permissions:
  - `ec2:RunInstances` with a wildcard resource ("\*")
  - `iam:PassRole` with the resource matching the role ARN (for example, `arn:aws:iam::999999999999:role/ExampleRoleName`)

- If you don't have the preceding permissions, [edit the IAM policy](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") associated with the IAM
  role or user to add the missing required permissions.

If your issue is not resolved and you continue receiving a launch failure error, you can
decode the authorization failure message included in the error. The decoded message
includes the permissions that are missing from the IAM policy. For more information,
see [How do I
decode an authorization failure message after I receive an
"UnauthorizedOperation" error during an EC2 instance launch?](https://repost.aws/knowledge-center/ec2-not-auth-launch "https://repost.aws/knowledge-center/ec2-not-auth-launch")

## High CPU usage shortly after Windows starts (Windows instances only)

###### Note

This troubleshooting tip is for Windows instances only.

If Windows Update is set to **Check for updates but let me choose whether to
download and install them** (the default instance setting) this check can
consume anywhere from 50 - 99% of the CPU on the instance. If this CPU consumption
causes problems for your applications, you can manually change Windows Update settings
in **Control Panel** or you can use the following script in the Amazon EC2
user data field:

```
`reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" /v AUOptions /t REG_DWORD /d `3` /f net stop wuauserv net start wuauserv`
```

When you run this script, specify a value for /d. The default value is 3. Possible
values include the following:

1. Never check for updates
2. Check for updates but let me choose whether to download and install
   them
3. Download updates but let me choose whether to install them
4. Install updates automatically

After you modify the user data for your instance, you can run it. For more
information, see [Run commands on your Windows instance at launch](user-data.md "user-data.md").
