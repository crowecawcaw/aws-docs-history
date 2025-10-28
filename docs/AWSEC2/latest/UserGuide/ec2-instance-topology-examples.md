# Examples for Amazon EC2 instance topology

You can use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command to describe the instance topology
for your EC2 instances.

When you use the `describe-instance-topology` command without parameters or
filters, the response includes all your instances that match the supported instance
types for this command in the specified Region. You can specify the Region by including
the `--region` parameter, or by setting a default Region. For more
information about setting a default Region, see [Select a Region for your Amazon EC2
resources](using-regions-availability-zones-setup.md "using-regions-availability-zones-setup.md").

You can include parameters to return instances that match specified instance IDs or
placement group names. You can also include filters to return instances that match a
specified instance type or instance family, or instances in a specified Availability
Zone or Local Zone. You can include a single parameter or filter, or a combination of
parameters and filters.

The output is paginated, with up to 20 instances per page by default. You can specify
up to 100 instances per page using the `--max-results` parameter.

For more information, see [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md").

###### Required permissions

The following permission is required to describe instance topology:

- `ec2:DescribeInstanceTopology`

###### Examples

- [Example 1 – Instance IDs](ec2-instance-topology-examples.md#instance-topology-ex1 "ec2-instance-topology-examples.md#instance-topology-ex1")
- [Example 2 – Placement group name
  parameter](ec2-instance-topology-examples.md#instance-topology-ex2 "ec2-instance-topology-examples.md#instance-topology-ex2")
- [Example 3 – Instance type filter](ec2-instance-topology-examples.md#instance-topology-ex3 "ec2-instance-topology-examples.md#instance-topology-ex3")
  - [Example 3a – Exact match
    filter for a specified instance type](ec2-instance-topology-examples.md#instance-topology-ex3a "ec2-instance-topology-examples.md#instance-topology-ex3a")
  - [Example 3b – Wild card
    filter for an instance family](ec2-instance-topology-examples.md#instance-topology-ex3b "ec2-instance-topology-examples.md#instance-topology-ex3b")
  - [Example 3c – Combined
    instance family and exact match filters](ec2-instance-topology-examples.md#instance-topology-ex3c "ec2-instance-topology-examples.md#instance-topology-ex3c")

- [Example 4 – Zone ID filter](ec2-instance-topology-examples.md#instance-topology-ex4 "ec2-instance-topology-examples.md#instance-topology-ex4")
  - [Example 4a – Availability Zone
    filter](ec2-instance-topology-examples.md#instance-topology-ex4a "ec2-instance-topology-examples.md#instance-topology-ex4a")
  - [Example 4b – Local Zone
    filter](ec2-instance-topology-examples.md#instance-topology-ex4b "ec2-instance-topology-examples.md#instance-topology-ex4b")
  - [Example 4c – Combined
    Availability Zone and Local Zone filters](ec2-instance-topology-examples.md#instance-topology-ex4c "ec2-instance-topology-examples.md#instance-topology-ex4c")

- [Example 5 – Instance type and zone ID filters](ec2-instance-topology-examples.md#instance-topology-ex5 "ec2-instance-topology-examples.md#instance-topology-ex5")

## Example 1 – Instance IDs

AWS CLI

###### To describe the topology of specific instances

Use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command with the
`--instance-ids` parameter. The output includes only the
instances that match the specified instance IDs.

```
aws ec2 describe-instance-topology \
    --region `us-west-2` \
    --instance-ids `i-1111111111example` `i-2222222222example`
```

The following is example output.

```
{
    "Instances": [
        {
            "InstanceId": "i-1111111111example",
            "InstanceType": "p4d.24xlarge",
            "GroupName": "ML-group",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3333333333example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az2",
            "AvailabilityZone": "us-west-2a"
        },
        {
            "InstanceId": "i-2222222222example",
            "InstanceType": "trn1n.32xlarge",
            "GroupName": "HPC-group",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3214313214example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az2",
            "AvailabilityZone": "us-west-2a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

PowerShell

###### To describe the topology of specific instances

Use the [Get-EC2InstanceTopology](../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md "../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md")
cmdlet.

```
Get-EC2InstanceTopology `
    -InstanceId `i-1111111111example`, `i-2222222222example`
```

## Example 2 – Placement group name

parameter

AWS CLI

###### To describe the topology of instances in a specific placement group

Use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command with the
`group-names` parameter. The output includes only the instances
that are in either of the specified placement groups.

```
aws ec2 describe-instance-topology \
    --region `us-west-2` \
    --group-names `ML-group` `HPC-group`
```

The following is example output.

```
{
    "Instances": [
        {
            "InstanceId": "i-1111111111example",
            "InstanceType": "p4d.24xlarge",
            "GroupName": "ML-group",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3333333333example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az2",
            "AvailabilityZone": "us-west-2a"
        },
        {
            "InstanceId": "i-2222222222example",
            "InstanceType": "trn1n.32xlarge",
            "GroupName": "HPC-group",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3214313214example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az2",
            "AvailabilityZone": "us-west-2a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

PowerShell

###### To describe the topology of instances in a specific placement group

Use the [Get-EC2InstanceTopology](../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md "../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md")
cmdlet.

```
Get-EC2InstanceTopology `
    -GroupName `ML-group`, `HPC-group`
```

## Example 3 – Instance type filter

You can filter by a specified instance type (exact match) or filter by an instance
family (using a wildcard). You can also combine a specified instance type filter and
instance family filter.

### Example 3a – Exact match

filter for a specified instance type

AWS CLI

###### To describe the topology of instances with a specific instance type

Use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command with
the `instance-type` filter. The output includes
only the instances with the specified instance type.

```
aws ec2 describe-instance-topology \
    --region `us-west-2` \
    --filters Name=instance-type,Values=`trn1n.32xlarge`
```

The following is example output.

```
{
    "Instances": [
        {
            "InstanceId": "i-2222222222example",
            "InstanceType": "trn1n.32xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3333333333example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az2",
            "AvailabilityZone": "us-west-2a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

PowerShell

###### To describe the topology of instances with a specific instance type

Use the [Get-EC2InstanceTopology](../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md "../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md")
cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="`trn1n.32xlarge`"}
```

### Example 3b – Wild card

filter for an instance family

AWS CLI

###### To describe the topology of instances with a specific instance family

Use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command with
the `instance-type` filter. The output includes only the
instances with the specified instance family.

```
aws ec2 describe-instance-topology \
    --region `us-west-2` \
    --filters Name=instance-type,Values=`trn1*`
```

The following is example output.

```
{
    "Instances": [
        {
            "InstanceId": "i-2222222222example",
            "InstanceType": "trn1n.32xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3333333333example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az2",
            "AvailabilityZone": "us-west-2a"
        },
        {
            "InstanceId": "i-3333333333example",
            "InstanceType": "trn1.32xlarge",
            "NetworkNodes": [
                "nn-1212121212example",
                "nn-1211122211example",
                "nn-1311133311example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az4",
            "AvailabilityZone": "us-west-2d"
        },
        {
            "InstanceId": "i-444444444example",
            "InstanceType": "trn1.2xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-5434334334example",
                "nn-1235301234example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az2",
            "AvailabilityZone": "us-west-2a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

PowerShell

###### To describe the topology of instances with a specific instance family

Use the [Get-EC2InstanceTopology](../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md "../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md")
cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="`trn1*`"}
```

### Example 3c – Combined

instance family and exact match filters

AWS CLI

###### To describe the topology of instances with an instance family or instance type

Use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command with
the `instance-type` filter. The output includes only the
instances that meet the specified criteria.

```
aws ec2 describe-instance-topology \
    --region `us-west-2` \
    --filters "Name=instance-type,Values=`p4d*`,`trn1n.32xlarge`"
```

The following is example output.

```
{
    "Instances": [
        {
            "InstanceId": "i-1111111111example",
            "InstanceType": "p4d.24xlarge",
            "GroupName": "ML-group",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3333333333example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az2",
            "AvailabilityZone": "us-west-2a"
        },
        {
            "InstanceId": "i-2222222222example",
            "InstanceType": "trn1n.32xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-4343434343example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "usw2-az2",
            "AvailabilityZone": "us-west-2a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

PowerShell

###### To describe the topology of instances with an instance family or instance type

Use the [Get-EC2InstanceTopology](../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md "../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md")
cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="`p4d*`", "`trn1n.32xlarge`"}
```

## Example 4 – Zone ID filter

You can use the `zone-id` filter to filter by an Availability Zone or
Local Zone. You can also combine an Availability Zone filter and Local Zone
filter.

### Example 4a – Availability Zone

filter

AWS CLI

###### To describe the topology of instances in a specific Availability Zone

Use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command with
the `zone-id` filter. The output includes only the instances
in the specified Availability Zone.

```
aws ec2 describe-instance-topology \
    --region `us-east-1` \
    --filters Name=zone-id,Values=`use1-az1`
```

The following is example output.

```
{
    "Instances": [
        {
            "InstanceId": "i-2222222222example",
            "InstanceType": "trn1n.32xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3214313214example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "use1-az1",
            "AvailabilityZone": "us-east-1a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

PowerShell

###### To describe the topology of instances in a specific Availability Zone

Use the [Get-EC2InstanceTopology](../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md "../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md")
cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="zone-id"; Values="`use1-az1`"}
```

### Example 4b – Local Zone

filter

AWS CLI

###### To describe the topology of instances in a specific Local Zone

Use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command with
the `zone-id` filter. The output includes only the instances
in the specified Local Zone.

```
aws ec2 describe-instance-topology \
    --region `us-east-1` \
    --filters Name=zone-id,Values=`use1-atl2-az1`
```

The following is example output.

```
{
    "Instances": [
        {
            "InstanceId": "i-1111111111example",
            "InstanceType": "p4d.24xlarge",
            "GroupName": "ML-group",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3333333333example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "use1-atl2-az1",
            "AvailabilityZone": "us-east-1-atl-2a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

PowerShell

###### To describe the topology of instances in a specific Local Zone

Use the [Get-EC2InstanceTopology](../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md "../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md")
cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="zone-id"; Values="`use1-atl2-az1`"}
```

### Example 4c – Combined

Availability Zone and Local Zone filters

AWS CLI

###### To describe the topology of instances in a specific zone

Use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command with
the `zone-id` filter. The output includes only the instances that
are in either of the specified zones.

```
aws ec2 describe-instance-topology \
    --region `us-east-1` \
    --filters Name=zone-id,Values=`use1-az1`,`use1-atl2-az1`
```

The following is example output.

```
{
    "Instances": [
        {
            "InstanceId": "i-1111111111example",
            "InstanceType": "p4d.24xlarge",
            "GroupName": "ML-group",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3333333333example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "use1-atl2-az1",
            "AvailabilityZone": "us-east-1-atl-2a"
        },
        {
            "InstanceId": "i-2222222222example",
            "InstanceType": "trn1n.32xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3214313214example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "use1-az1",
            "AvailabilityZone": "us-east-1a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

PowerShell

###### To describe the topology of instances in a specific zone

Use the [Get-EC2InstanceTopology](../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md "../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md")
cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="zone-id"; Values="`use1-az1`", "`use1-atl2-az1`"}
```

## Example 5 – Instance type and zone ID filters

You can combine filters in a single command.

AWS CLI

###### To describe the topology of instances with specific instance types, instance families, and zones

Use the [describe-instance-topology](../../../cli/latest/reference/ec2/describe-instance-topology.md "../../../cli/latest/reference/ec2/describe-instance-topology.md") command with the
`instance-type` and `zone-id` filters. The response
contains any instances with either of the specified instance types and are in
either of the specified zones.

```
aws ec2 describe-instance-topology \
    --region `us-east-1` \
    --filters "Name=instance-type,Values=`p4d*`,`trn1n.32xlarge`" \
              "Name=zone-id,Values=`use1-az1`,`use1-atl2-az1`"
```

The following is example output.

```
{
    "Instances": [
        {
            "InstanceId": "i-1111111111example",
            "InstanceType": "p4d.24xlarge",
            "GroupName": "ML-group",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3333333333example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "use1-atl2-az1",
            "AvailabilityZone": "us-east-1-atl-2a"
        },
        {
            "InstanceId": "i-2222222222example",
            "InstanceType": "trn1n.32xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example",
                "nn-3214313214example"
            ],
            "CapacityBlockId": "null",
            "ZoneId": "use1-az1",
            "AvailabilityZone": "us-east-1a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

PowerShell

###### To describe the topology of instances with specific instance types, instance families, and zones

Use the [Get-EC2InstanceTopology](../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md "../../../powershell/latest/reference/items/Get-EC2InstanceTopology.md")
cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="`p4d*`", "`trn1n.32xlarge`"} `
            @{Name="zone-id"; Values="`use1-az1`", "`use1-atl2-az1`"}
```
