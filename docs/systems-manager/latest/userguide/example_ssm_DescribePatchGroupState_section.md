AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DescribePatchGroupState` with a CLI

The following code examples show how to use `DescribePatchGroupState`.

CLI

**AWS CLI**

**To get the state of a patch group**

The following `describe-patch-group-state` example retrieves the high-level patch compliance summary for a patch group.

```
`aws ssm describe-patch-group-state \
 --patch-group `"Production"``

```

Output:

```
{
    "Instances": 21,
    "InstancesWithCriticalNonCompliantPatches": 1,
    "InstancesWithFailedPatches": 2,
    "InstancesWithInstalledOtherPatches": 3,
    "InstancesWithInstalledPatches": 21,
    "InstancesWithInstalledPendingRebootPatches": 2,
    "InstancesWithInstalledRejectedPatches": 1,
    "InstancesWithMissingPatches": 3,
    "InstancesWithNotApplicablePatches": 4,
    "InstancesWithOtherNonCompliantPatches": 1,
    "InstancesWithSecurityNonCompliantPatches": 1,
    "InstancesWithUnreportedNotApplicablePatches": 2
}
```

For more information, see About patch groups <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-patchgroups.html>\_\_ and [Understanding patch compliance state values](about-patch-compliance-states.md "about-patch-compliance-states.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribePatchGroupState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-group-state.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-group-state.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example gets the high-level patch compliance summary for a patch group.**

```
Get-SSMPatchGroupState -PatchGroup "Production"

```

**Output:**

```
Instances                          : 4
InstancesWithFailedPatches         : 1
InstancesWithInstalledOtherPatches : 4
InstancesWithInstalledPatches      : 3
InstancesWithMissingPatches        : 0
InstancesWithNotApplicablePatches  : 0
```

- For API details, see
  [DescribePatchGroupState](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example gets the high-level patch compliance summary for a patch group.**

```
Get-SSMPatchGroupState -PatchGroup "Production"

```

**Output:**

```
Instances                          : 4
InstancesWithFailedPatches         : 1
InstancesWithInstalledOtherPatches : 4
InstancesWithInstalledPatches      : 3
InstancesWithMissingPatches        : 0
InstancesWithNotApplicablePatches  : 0
```

- For API details, see
  [DescribePatchGroupState](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
