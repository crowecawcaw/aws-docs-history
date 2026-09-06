

# Examples for Amazon EC2 instance topology
<a name="ec2-instance-topology-examples"></a>

You can use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command to describe the topology for your EC2 instances. And you can use the [describe-capacity-reservation-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command to describe the topology of your Capacity Reservations.

When you use the `describe-instance-topology` or `describe-capacity-reservation-topology` command without parameters or filters, the response includes all your instances or Capacity Reservations (depending on the command used) that match the supported instance types for this command in the specified Region. You can specify the Region by including the `--region` parameter, or by setting a default Region. For more information about setting a default Region, see [Select a Region for your Amazon EC2 resources](using-regions-availability-zones-setup.md).

You can include parameters to return instances or Capacity Reservations that match specified instance or Capacity Reservation IDs or placement group names. You can also include filters to return instances or Capacity Reservations that match a specified instance type or instance family, or instances or Capacity Reservations in a specified Availability Zone or Local Zone. You can include a single parameter or filter, or a combination of parameters and filters.

The output is paginated, with up to 20 instances or Capacity Reservations per page by default. You can specify up to 100 instances or Capacity Reservations per page using the `--max-results` parameter.

For more information, see [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) and [describe-reservation-topology-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-reservation-topology-topology.html).

**Required permissions**

The following permissions are required:
+ `ec2:DescribeInstanceTopology` – For describing instance topology
+  `ec2:DescribeCapacityReservationTopology` – For describing Capacity Reservation topology

**Contents**
+ [Example 1: DescribeInstanceTopology - Instance IDs](#instance-topology-ex1)
+ [Example 2: DescribeInstanceTopology - Placement group name parameter](#instance-topology-ex2)
+ [Example 3: DescribeInstanceTopology - Instance type filter](#instance-topology-ex3)
  + [Example 3a – Exact match filter for a specified instance type](#instance-topology-ex3a)
  + [Example 3b – Wild card filter for an instance family](#instance-topology-ex3b)
  + [Example 3c – Combined instance family and exact match filters](#instance-topology-ex3c)
+ [Example 4: DescribeInstanceTopology - Zone ID filter](#instance-topology-ex4)
  + [Example 4a – Availability Zone filter](#instance-topology-ex4a)
  + [Example 4b – Local Zone filter](#instance-topology-ex4b)
  + [Example 4c – Combined Availability Zone and Local Zone filters](#instance-topology-ex4c)
+ [Example 5: DescribeInstanceTopology - Instance type and zone ID filters](#instance-topology-ex5)
+ [Example 6: DescribeCapacityReservationTopology - Capacity Reservation IDs](#instance-topology-ex6)
+ [Example 7: DescribeCapacityReservationTopology - Instance type filter](#instance-topology-ex7)

## Example 1: DescribeInstanceTopology - Instance IDs
<a name="instance-topology-ex1"></a>

------
#### [ AWS CLI ]

**To describe the topology of specific instances**  
Use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command with the `--instance-ids` parameter. The output includes only the instances that match the specified instance IDs.

```
aws ec2 describe-instance-topology \
    --region {{us-west-2}} \
    --instance-ids {{i-1111111111example}} {{i-2222222222example}}
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

------
#### [ PowerShell ]

**To describe the topology of specific instances**  
Use the [Get-EC2InstanceTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTopology.html) cmdlet.

```
Get-EC2InstanceTopology `
    -InstanceId {{i-1111111111example}}, {{i-2222222222example}}
```

------

## Example 2: DescribeInstanceTopology - Placement group name parameter
<a name="instance-topology-ex2"></a>

------
#### [ AWS CLI ]

**To describe the topology of instances in a specific placement group**  
Use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command with the `group-names` parameter. The output includes only the instances that are in either of the specified placement groups.

```
aws ec2 describe-instance-topology \
    --region {{us-west-2}} \
    --group-names {{ML-group}} {{HPC-group}}
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

------
#### [ PowerShell ]

**To describe the topology of instances in a specific placement group**  
Use the [Get-EC2InstanceTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTopology.html) cmdlet.

```
Get-EC2InstanceTopology `
    -GroupName {{ML-group}}, {{HPC-group}}
```

------

## Example 3: DescribeInstanceTopology - Instance type filter
<a name="instance-topology-ex3"></a>

You can filter by a specified instance type (exact match) or filter by an instance family (using a wildcard). You can also combine a specified instance type filter and instance family filter.

### Example 3a – Exact match filter for a specified instance type
<a name="instance-topology-ex3a"></a>

------
#### [ AWS CLI ]

**To describe the topology of instances with a specific instance type**  
Use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command with the `instance-type` filter. The output includes only the instances with the specified instance type.

```
aws ec2 describe-instance-topology \
    --region {{us-west-2}} \
    --filters Name=instance-type,Values={{trn1n.32xlarge}}
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

------
#### [ PowerShell ]

**To describe the topology of instances with a specific instance type**  
Use the [Get-EC2InstanceTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTopology.html) cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="{{trn1n.32xlarge}}"}
```

------

### Example 3b – Wild card filter for an instance family
<a name="instance-topology-ex3b"></a>

------
#### [ AWS CLI ]

**To describe the topology of instances with a specific instance family**  
Use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command with the `instance-type` filter. The output includes only the instances with the specified instance family.

```
aws ec2 describe-instance-topology \
    --region {{us-west-2}} \
    --filters Name=instance-type,Values={{trn1*}}
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

------
#### [ PowerShell ]

**To describe the topology of instances with a specific instance family**  
Use the [Get-EC2InstanceTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTopology.html) cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="{{trn1*}}"}
```

------

### Example 3c – Combined instance family and exact match filters
<a name="instance-topology-ex3c"></a>

------
#### [ AWS CLI ]

**To describe the topology of instances with an instance family or instance type**  
Use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command with the `instance-type` filter. The output includes only the instances that meet the specified criteria.

```
aws ec2 describe-instance-topology \
    --region {{us-west-2}} \
    --filters "Name=instance-type,Values={{p4d*}},{{trn1n.32xlarge}}"
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

------
#### [ PowerShell ]

**To describe the topology of instances with an instance family or instance type**  
Use the [Get-EC2InstanceTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTopology.html) cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="{{p4d*}}", "{{trn1n.32xlarge}}"}
```

------

## Example 4: DescribeInstanceTopology - Zone ID filter
<a name="instance-topology-ex4"></a>

You can use the `zone-id` filter to filter by an Availability Zone or Local Zone. You can also combine an Availability Zone filter and Local Zone filter.

### Example 4a – Availability Zone filter
<a name="instance-topology-ex4a"></a>

------
#### [ AWS CLI ]

**To describe the topology of instances in a specific Availability Zone**  
Use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command with the `zone-id` filter. The output includes only the instances in the specified Availability Zone.

```
aws ec2 describe-instance-topology \
    --region {{us-east-1}} \
    --filters Name=zone-id,Values={{use1-az1}}
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

------
#### [ PowerShell ]

**To describe the topology of instances in a specific Availability Zone**  
Use the [Get-EC2InstanceTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTopology.html) cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="zone-id"; Values="{{use1-az1}}"}
```

------

### Example 4b – Local Zone filter
<a name="instance-topology-ex4b"></a>

------
#### [ AWS CLI ]

**To describe the topology of instances in a specific Local Zone**  
Use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command with the `zone-id` filter. The output includes only the instances in the specified Local Zone.

```
aws ec2 describe-instance-topology \
    --region {{us-east-1}} \
    --filters Name=zone-id,Values={{use1-atl2-az1}}
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

------
#### [ PowerShell ]

**To describe the topology of instances in a specific Local Zone**  
Use the [Get-EC2InstanceTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTopology.html) cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="zone-id"; Values="{{use1-atl2-az1}}"}
```

------

### Example 4c – Combined Availability Zone and Local Zone filters
<a name="instance-topology-ex4c"></a>

------
#### [ AWS CLI ]

**To describe the topology of instances in a specific zone**  
Use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command with the `zone-id` filter. The output includes only the instances that are in either of the specified zones.

```
aws ec2 describe-instance-topology \
    --region {{us-east-1}} \
    --filters Name=zone-id,Values={{use1-az1}},{{use1-atl2-az1}}
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

------
#### [ PowerShell ]

**To describe the topology of instances in a specific zone**  
Use the [Get-EC2InstanceTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTopology.html) cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="zone-id"; Values="{{use1-az1}}", "{{use1-atl2-az1}}"}
```

------

## Example 5: DescribeInstanceTopology - Instance type and zone ID filters
<a name="instance-topology-ex5"></a>

You can combine filters in a single command.

------
#### [ AWS CLI ]

**To describe the topology of instances with specific instance types, instance families, and zones**  
Use the [describe-instance-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-topology.html) command with the `instance-type` and `zone-id` filters. The response contains any instances with either of the specified instance types and are in either of the specified zones.

```
aws ec2 describe-instance-topology \
    --region {{us-east-1}} \
    --filters "Name=instance-type,Values={{p4d*}},{{trn1n.32xlarge}}" \
              "Name=zone-id,Values={{use1-az1}},{{use1-atl2-az1}}"
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

------
#### [ PowerShell ]

**To describe the topology of instances with specific instance types, instance families, and zones**  
Use the [Get-EC2InstanceTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceTopology.html) cmdlet.

```
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="{{p4d*}}", "{{trn1n.32xlarge}}"} `
            @{Name="zone-id"; Values="{{use1-az1}}", "{{use1-atl2-az1}}"}
```

------

## Example 6: DescribeCapacityReservationTopology - Capacity Reservation IDs
<a name="instance-topology-ex6"></a>

------
#### [ AWS CLI ]

**To describe the topology of specific Capacity Reservations**  
Use the [describe-capacity-reservation-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-capacity-reservation-topology.html) command with the `capacity-reservation-id` parameter. The output includes only the Capacity Reservations that match the specified Capacity Reservation IDs.

```
aws ec2 describe-capacity-reservation-topology \
    --region {{us-east-1}} \
    --capacity-reservation-id {{cr-1111111111example}} {{cr-2222222222example}}
```

The following is example output.

```
{
    "CapacityReservations": [
        {
            "CapacityReservationId": "cr-1111111111example",
            "CapacityBlockId": "null",
            "State": "active",
            "InstanceType": "p5.48xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example"
            ],
            "AvailabilityZone": "us-east-1a"
        },
        {
            "CapacityReservationId": "cr-2222222222example",
            "CapacityBlockId": "null",
            "State": "active",
            "InstanceType": "p5en.48xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example"
            ],
            "AvailabilityZone": "us-east-1a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

------
#### [ PowerShell ]

**To describe the topology of specific Capacity Reservations**  
Use the [Get-EC2CapacityReservationTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2CapacityReservationTopology.html) cmdlet.

```
Get-EC2CapacityReservationTopology `
    -CapacityReservationId {{cr-1111111111example}} {{cr-2222222222example}}
```

------

## Example 7: DescribeCapacityReservationTopology - Instance type filter
<a name="instance-topology-ex7"></a>

You can filter by a specified instance type (exact match) or filter by an instance family (using a wildcard). You can also combine a specified instance type filter and instance family filter.

------
#### [ AWS CLI ]

**To describe the topology of Capacity Reservations with a specific instance type**  
Use the [describe-capacity-reservation-topology](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-capacity-reservation-topology.html) command with the `instance-type` filter. The response contains any instances with the specified instance type.

```
aws ec2 describe-capacity-reservation-topology \
    --region {{us-east-1}} \
    --filters Name=instance-type,Values={{p5en.48xlarge}}
```

The following is example output.

```
{
    "CapacityReservations": [
        {
            "CapacityReservationId": "cr-2222222222example",
            "CapacityBlockId": "null",
            "State": "active",
            "InstanceType": "p5en.48xlarge",
            "NetworkNodes": [
                "nn-1111111111example",
                "nn-2222222222example"
            ],
            "AvailabilityZone": "us-east-1a"
        }
    ],
    "NextToken": "SomeEncryptedToken"
}
```

------
#### [ PowerShell ]

**To describe the topology of Capacity Reservations with a specific instance type**  
Use the [Get-EC2CapacityReservationTopology](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2CapacityReservationTopology.html) cmdlet.

```
Get-EC2CapacityReservationTopology `
    -Filter @{Name="instance-type"; Values="{{p5en.48xlarge}}"}
```

------