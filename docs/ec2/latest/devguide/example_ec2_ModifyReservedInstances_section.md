# Use `ModifyReservedInstances` with a CLI

The following code examples show how to use `ModifyReservedInstances`.

CLI

**AWS CLI**

**To modify Reserved Instances**

This example command moves a Reserved Instance to another Availability Zone in the same region.

Command:

```
`aws ec2 modify-reserved-instances --reserved-instances-ids `b847fa93-e282-4f55-b59a-1342f5bd7c02` --target-configurations `AvailabilityZone=us-west-1c,Platform=EC2-Classic,InstanceCount=10``

```

Output:

```
{
  "ReservedInstancesModificationId": "rimod-d3ed4335-b1d3-4de6-ab31-0f13aaf46687"
}
```

**To modify the network platform of Reserved Instances**

This example command converts EC2-Classic Reserved Instances to EC2-VPC.

Command:

```
`aws ec2 modify-reserved-instances --reserved-instances-ids `f127bd27-edb7-44c9-a0eb-0d7e09259af0` --target-configurations `AvailabilityZone=us-west-1c,Platform=EC2-VPC,InstanceCount=5``

```

Output:

```
{
  "ReservedInstancesModificationId": "rimod-82fa9020-668f-4fb6-945d-61537009d291"
}
```

For more information, see Modifying Your Reserved Instances in the _Amazon EC2 User Guide_.

**To modify the instance size of Reserved Instances**

This example command modifies a Reserved Instance that has 10 m1.small Linux/UNIX instances in us-west-1c so that 8
m1.small instances become 2 m1.large instances, and the remaining 2 m1.small become 1 m1.medium instance in the same
Availability Zone. Command:

```
`aws ec2 modify-reserved-instances --reserved-instances-ids `1ba8e2e3-3556-4264-949e-63ee671405a9` --target-configurations `AvailabilityZone=us-west-1c,Platform=EC2-Classic,InstanceCount=2,InstanceType=m1.large` `AvailabilityZone=us-west-1c,Platform=EC2-Classic,InstanceCount=1,InstanceType=m1.medium``

```

Output:

```
{
    "ReservedInstancesModificationId": "rimod-acc5f240-080d-4717-b3e3-1c6b11fa00b6"
}
```

For more information, see Modifying the Instance Size of Your Reservations in the _Amazon EC2 User Guide_.

- For API details, see
  [ModifyReservedInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-reserved-instances.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-reserved-instances.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example modifies the Availability Zone, instance count, and platform for the specified Reserved instances.**

```
$config = New-Object Amazon.EC2.Model.ReservedInstancesConfiguration
$config.AvailabilityZone = "us-west-2a"
$config.InstanceCount = 1
$config.Platform = "EC2-VPC"

Edit-EC2ReservedInstance `
-ReservedInstancesId @("FE32132D-70D5-4795-B400-AE435EXAMPLE", "0CC556F3-7AB8-4C00-B0E5-98666EXAMPLE") `
-TargetConfiguration $config

```

- For API details, see
  [ModifyReservedInstances](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example modifies the Availability Zone, instance count, and platform for the specified Reserved instances.**

```
$config = New-Object Amazon.EC2.Model.ReservedInstancesConfiguration
$config.AvailabilityZone = "us-west-2a"
$config.InstanceCount = 1
$config.Platform = "EC2-VPC"

Edit-EC2ReservedInstance `
-ReservedInstancesId @("FE32132D-70D5-4795-B400-AE435EXAMPLE", "0CC556F3-7AB8-4C00-B0E5-98666EXAMPLE") `
-TargetConfiguration $config

```

- For API details, see
  [ModifyReservedInstances](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
