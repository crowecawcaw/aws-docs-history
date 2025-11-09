AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DescribeInstancePatchStates` with a CLI

The following code examples show how to use `DescribeInstancePatchStates`.

CLI

**AWS CLI**

**To get the patch summary states for instances**

This `describe-instance-patch-states` example gets the patch summary states for an instance.

```
`aws ssm describe-instance-patch-states \
 --instance-ids `"i-1234567890abcdef0"``

```

Output:

```
{
    "InstancePatchStates": [
        {
            "InstanceId": "i-1234567890abcdef0",
            "PatchGroup": "my-patch-group",
            "BaselineId": "pb-0713accee01234567",
            "SnapshotId": "521c3536-930c-4aa9-950e-01234567abcd",
            "CriticalNonCompliantCount": 2,
            "SecurityNonCompliantCount": 2,
            "OtherNonCompliantCount": 1,
            "InstalledCount": 123,
            "InstalledOtherCount": 334,
            "InstalledPendingRebootCount": 0,
            "InstalledRejectedCount": 0,
            "MissingCount": 1,
            "FailedCount": 2,
            "UnreportedNotApplicableCount": 11,
            "NotApplicableCount": 2063,
            "OperationStartTime": "2021-05-03T11:00:56-07:00",
            "OperationEndTime": "2021-05-03T11:01:09-07:00",
            "Operation": "Scan",
            "LastNoRebootInstallOperationTime": "2020-06-14T12:17:41-07:00",
            "RebootOption": "RebootIfNeeded"
        }
    ]
}
```

For more information, see [About Patch Compliance](about-patch-compliance.md "about-patch-compliance.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeInstancePatchStates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-patch-states.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-patch-states.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example gets the patch summary states for an instance.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407"

```

**Example 2: This example gets the patch summary states for two instances.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407","i-09a618aec652973a9"

```

- For API details, see
  [DescribeInstancePatchStates](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example gets the patch summary states for an instance.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407"

```

**Example 2: This example gets the patch summary states for two instances.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407","i-09a618aec652973a9"

```

- For API details, see
  [DescribeInstancePatchStates](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
