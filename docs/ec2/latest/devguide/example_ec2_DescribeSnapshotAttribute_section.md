# Use `DescribeSnapshotAttribute` with a CLI

The following code examples show how to use `DescribeSnapshotAttribute`.

CLI

**AWS CLI**

**To describe the snapshot attributes for a snapshot**

The following `describe-snapshot-attribute` example lists the accounts with which a snapshot is shared.

```
`aws ec2 describe-snapshot-attribute \
 --snapshot-id `snap-01234567890abcedf` \
 --attribute `createVolumePermission``

```

Output:

```
{
    "SnapshotId": "snap-01234567890abcedf",
    "CreateVolumePermissions": [
        {
            "UserId": "123456789012"
        }
    ]
}
```

For more information, see [Share an Amazon EBS snapshot](../../../AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.md#share-unencrypted-snapshot "../../../AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.md#share-unencrypted-snapshot") in the _Amazon Elastic Compute Cloud User Guide_.

- For API details, see
  [DescribeSnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshot-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshot-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the specified attribute of the specified snapshot.**

```
Get-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute ProductCodes

```

**Output:**

```
CreateVolumePermissions    ProductCodes    SnapshotId
-----------------------    ------------    ----------
{}                         {}              snap-12345678
```

**Example 2: This example describes the specified attribute of the specified snapshot.**

```
(Get-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission).CreateVolumePermissions

```

**Output:**

```
Group    UserId
-----    ------
all
```

- For API details, see
  [DescribeSnapshotAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the specified attribute of the specified snapshot.**

```
Get-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute ProductCodes

```

**Output:**

```
CreateVolumePermissions    ProductCodes    SnapshotId
-----------------------    ------------    ----------
{}                         {}              snap-12345678
```

**Example 2: This example describes the specified attribute of the specified snapshot.**

```
(Get-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission).CreateVolumePermissions

```

**Output:**

```
Group    UserId
-----    ------
all
```

- For API details, see
  [DescribeSnapshotAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
