

# Use Capacity Reservations with placement groups
<a name="cr-cpg"></a>

You can create Capacity Reservations in a placement group to reserve Amazon EC2 compute capacity for your workloads.

Creating a Capacity Reservation in a placement group ensures that you have access to compute capacity in your placement groups when you need it, for as long as you need it. This allows you to scale down while ensuring that the capacity remains available for your use so that you can scale back up when needed. 

After you create a Capacity Reservation in a placement group, you can share it with other AWS accounts. For more information, see [Sharing Capacity Reservations in placement groups](#cpg-cr-sharing).

## Supported placement strategies
<a name="cr-pg-supported-strategies"></a>

You can create Capacity Reservations in placement groups that use the following strategies:
+ Cluster
+ Precision Time

**Note**  
Spread and Partition placement groups do not support Capacity Reservations. Capacity Blocks do not support placement groups.

For information about supported instance types, available Regions, and placement strategies, see [Placement groups for your Amazon EC2 instances](placement-groups.md).

**Topics**
+ [Supported placement strategies](#cr-pg-supported-strategies)
+ [Limitations](#cr-cpg-limitations)
+ [Work with Capacity Reservations in placement groups](#work-with-crs-cpgs)
+ [Sharing Capacity Reservations in placement groups](#cpg-cr-sharing)

## Limitations
<a name="cr-cpg-limitations"></a>

Keep the following in mind when creating Capacity Reservations in placement groups:
+ If an existing Capacity Reservation is not in a placement group, you can't modify the Capacity Reservation to reserve capacity in a placement group. To reserve capacity in a placement group, you must create the Capacity Reservation in the placement group.
+ After you create a Capacity Reservation in a placement group, you can't modify it to reserve capacity outside of the placement group.
+ You can increase your reserved capacity in a placement group by modifying an existing Capacity Reservation in the placement group, or by creating additional Capacity Reservations in the placement group. However, you increase your chances of getting an insufficient capacity error.
+ You can share Capacity Reservations only from the placement group that you own. You cannot share Capacity Reservations from a placement group that you do not own.
+ You can't delete a placement group that has `active` Capacity Reservations. You must cancel all Capacity Reservations in the placement group before you can delete it.

## Work with Capacity Reservations in placement groups
<a name="work-with-crs-cpgs"></a>

To start using Capacity Reservations with placement groups, perform the following steps.

**Note**  
If you want to create a Capacity Reservation in an existing placement group, skip Step 1. Then for Steps 2 and 3, specify the ARN of the existing placement group. 

**Topics**
+ [Step 1: (*Conditional*) Create a placement group for use with a Capacity Reservation](#create-cpg)
+ [Step 2: Create a Capacity Reservation in a placement group](#create-cr-in-cpg)
+ [Step 3: Launch instances into Capacity Reservations in a placement group](#launch-instance-into-cpg)

### Step 1: (*Conditional*) Create a placement group for use with a Capacity Reservation
<a name="create-cpg"></a>

Perform this step only if you need to create a new placement group. To use an existing placement group, skip this step and then for Steps 2 and 3, use the ARN of that placement group.

------
#### [ Console ]

**To create a placement group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Placement Groups**, and then choose **Create placement group**.

1. For **Name**, specify a descriptive name for the placement group.

1. For **Placement strategy**, choose the placement strategy.

1. Choose **Create group**.

1. In the **Placement groups** table, in the **Group ARN** column, make a note of the ARN of the placement group that you created. You'll need it for the next step.

------
#### [ AWS CLI ]

**To create a placement group**  
Use the [create-placement-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-placement-group.html) command.

```
aws ec2 create-placement-group \
    --group-name {{MyPG}} \
    --strategy {{strategy}}
```

Make a note of the placement group ARN returned in the output, because you'll need it for the next step.

------
#### [ PowerShell ]

**To create a placement group**  
Use the [New-EC2PlacementGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2PlacementGroup.html) cmdlet.

```
New-EC2PlacementGroup `
    -GroupName {{my-placement-group}} `
    -Strategy {{strategy}}
```

Make a note of the placement group ARN returned in the output, because you'll need it for the next step.

------

### Step 2: Create a Capacity Reservation in a placement group
<a name="create-cr-in-cpg"></a>

You create a Capacity Reservation in a placement group in the same way that you create any Capacity Reservation. However, you must also specify the ARN of the placement group in which to create the Capacity Reservation. 

**Considerations**
+ The specified placement group must be in the `available` state. If the placement group is in the `pending`, `deleting`, or `deleted` state, the request fails.
+ The Capacity Reservation and the placement group must be in the same Availability Zone. If the request to create the Capacity Reservation specifies an Availability Zone that is different from that of the placement group, the request fails.
+ You can create Capacity Reservations only for instance types that are supported by placement groups. If you specify an unsupported instance type, the request fails.
+ If you create an `open` Capacity Reservation in a placement group and there are existing running instances that have matching attributes (placement group ARN, instance type, Availability Zone, platform, and tenancy), those instances automatically run in the Capacity Reservation.
+ Your request to create a Capacity Reservation could fail if one of the following is true:
  + Amazon EC2 does not have sufficient capacity to fulfill the request. Either try again at a later time, try a different Availability Zone, or try a smaller capacity. If your workload is flexible across instance types and sizes, try different instance attributes.
  + The requested quantity exceeds your On-Demand Instance limit for the selected instance family. Increase your On-Demand Instance limit for the instance family and try again. For more information, see [On-Demand Instance quotas](ec2-on-demand-instances.md#ec2-on-demand-instances-limits).

------
#### [ Console ]

**To create a Capacity Reservation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Capacity Reservations**, and then choose **Create Capacity Reservation**.

1. On the **Create a Capacity Reservation** page, specify the instance type, platform, Availability Zone, Tenancy, quantity, and end date as needed.

1. For **Placement group**, select the ARN of the placement group in which to create the Capacity Reservation.

1. Choose **Create**.

For more information, see [Create a Capacity Reservation](capacity-reservations-create.md).

------
#### [ AWS CLI ]

**To create a Capacity Reservation**  
Use the [create-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-capacity-reservation.html) command. For `--placement-group-arn`, specify the ARN of the placement group in which to create the Capacity Reservation.

```
aws ec2 create-capacity-reservation \
    --instance-type {{instance_type}} \
    --instance-platform {{platform}} \
    --availability-zone-id {{az_id}} \
    --instance-count {{quantity}} \
    --placement-group-arn "{{placement_group_arn}}"
```

------
#### [ PowerShell ]

**To create a Capacity Reservation**  
Use the [Add-EC2CapacityReservation](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2CapacityReservation.html) cmdlet. For `-PlacementGroupArn`, specify the ARN of the placement group in which to create the Capacity Reservation.

```
Add-EC2CapacityReservation `
    -InstanceType {{instance_type}} `
    -InstancePlatform {{platform}} `
    -AvailabilityZoneId {{az_id}} `
    -InstanceCount {{quantity}} `
    -PlacementGroupArn "{{placement_group_arn}}"
```

------

### Step 3: Launch instances into Capacity Reservations in a placement group
<a name="launch-instance-into-cpg"></a>

You can launch an instance into a Capacity Reservation that is in a placement group with one of the following options:
+ *Specifying the ARN of the placement group in which to launch the instance* – When you provide the ARN of a placement group, Amazon EC2 launches the instance into that placement group. You can use one of the following methods: 
  + *Specifying `open`* – You do not have to specify the Capacity Reservation in the instance launch request. If the instance has attributes (placement group ARN, instance type, Availability Zone, platform, and tenancy) that match a Capacity Reservation in the specified placement group, the instance automatically runs in the Capacity Reservation.
  + *Specifying a Capacity Reservation* – If the Capacity Reservation accepts only targeted instance launches, you must specify the target Capacity Reservation in addition to the placement group in the request.
  + *Specifying a Capacity Reservation group* – For more information, see [ Using Capacity Reservation in placement groups with a Capacity Reservation group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cpg-odcr-crg.html).
+ *Specifying only a Capacity Reservation group* – For more information, see [Using Capacity Reservation in placement groups with a Capacity Reservation group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cpg-odcr-crg.html).
+ *Specifying only a Capacity Reservation* – You can launch instances into a Capacity Reservation in a placement group. 
**Note**  
When you launch instances by specifying only a Capacity Reservation or only a Capacity Reservation group, the instances are launched into the Capacity Reservations that are created in the placement group, but the instances are not directly attached to the placement group.

------
#### [ Console ]

**To launch instances into an existing Capacity Reservation**

1. Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md), but don't launch the instance until you've completed the following steps to specify the settings for the placement group and Capacity Reservation.

1. Expand **Advanced details** and do the following:

   1. For **Placement group**, select the placement group in which to launch the instance.

   1. For **Capacity Reservation**, choose one of the following options depending on the configuration of the Capacity Reservation:
      + **Open** – To launch the instances into any `open` Capacity Reservation in the placement group that has matching attributes and sufficient capacity.
      + **Target by ID** – To launch the instances into a Capacity Reservation that accepts only targeted instance launches.
      + **Target by group** – To launch the instances into any Capacity Reservation with matching attributes and available capacity in the selected Capacity Reservation group.

1. In the **Summary** panel, review your instance configuration, and then choose **Launch instance**. For more information, see [Launch an EC2 instance using the launch instance wizard in the console](ec2-launch-instance-wizard.md).

------
#### [ AWS CLI ]

**To launch instances into an existing Capacity Reservation**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command. If you need to target a specific Capacity Reservation or a Capacity Reservation group, specify the `--capacity-reservation-specification` parameter. For `--placement`, specify the `GroupName` parameter and then specify the name of the placement group that you created in the previous steps.

```
aws ec2 run-instances \
    --image-id {{ami-0abcdef1234567890}} \
    --count {{quantity}} \
    --instance-type {{instance_type}} \
    --key-name {{key_pair_name}} \
    --subnet-id {{subnet-0abcdef1234567890}} \
    --capacity-reservation-specification CapacityReservationTarget={CapacityReservationId={{capacity_reservation_id}}} \
    --placement "GroupName={{placement_group_name}}"
```

------
#### [ PowerShell ]

**To launch instances into an existing Capacity Reservation**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet. For `-Placement`, specify the `GroupName` parameter and then specify the name of the placement group that you created in the previous steps.

```
New-EC2Instance `
    -ImageId {{ami-0abcdef1234567890}} `
    -InstanceType {{instance_type}} `
    -KeyName {{key_pair_name}} `
    -SubnetId {{subnet-0abcdef1234567890}} `
    -CapacityReservationTarget_CapacityReservationId {{capacity_reservation_id}} `
    -Placement_GroupName {{placement_group_name}}
```

------

## Sharing Capacity Reservations in placement groups
<a name="cpg-cr-sharing"></a>

You can share Capacity Reservations in placement groups by either sharing only the Capacity Reservations, or by sharing both the Capacity Reservations and the placement group in which they were created.

By sharing only the Capacity Reservation, you give consumer accounts access to that Capacity Reservation only. Consumer accounts have no visibility or access to the placement group in which the Capacity Reservation is created. This gives you fine-grained control over consumer account access. Consumer accounts can't view any information about the placement group, including its ARN. 

When you share the placement group and the Capacity Reservation, the placement group is visible and accessible to consumer accounts. They can launch instances and create their own Capacity Reservations in it. 

For more information, see the following resources.
+ [Launch instances into Capacity Reservations in a placement group](#launch-instance-into-cpg)
+ [Shared Capacity Reservations](capacity-reservation-sharing.md)
+ [Shared placement groups](share-placement-group.md)