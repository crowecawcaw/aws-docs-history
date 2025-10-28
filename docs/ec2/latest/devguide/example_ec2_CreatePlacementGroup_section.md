# Use `CreatePlacementGroup` with a CLI

The following code examples show how to use `CreatePlacementGroup`.

CLI

**AWS CLI**

**To create a placement group**

This example command creates a placement group with the specified name.

Command:

```
`aws ec2 create-placement-group --group-name `my-cluster` --strategy `cluster``

```

**To create a partition placement group**

This example command creates a partition placement group named `HDFS-Group-A` with five partitions.

Command:

```
`aws ec2 create-placement-group --group-name `HDFS-Group-A` --strategy `partition` --partition-count `5``

```

- For API details, see
  [CreatePlacementGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-placement-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-placement-group.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates a placement group with the specified name.**

```
New-EC2PlacementGroup -GroupName my-placement-group -Strategy cluster

```

- For API details, see
  [CreatePlacementGroup](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates a placement group with the specified name.**

```
New-EC2PlacementGroup -GroupName my-placement-group -Strategy cluster

```

- For API details, see
  [CreatePlacementGroup](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
