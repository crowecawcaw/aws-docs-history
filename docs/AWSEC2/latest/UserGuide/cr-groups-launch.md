# Launch instances into Capacity Reservations in a group

You can launch instances into your existing Capacity Reservations by specifying a Capacity Reservation
Resource Group ARN. Instances that target a group match with any Capacity Reservation in the
group that has matching attributes (instance type, platform, Availability
Zone, and tenancy) and available capacity.

When you launch instances using the [launch instance
wizard](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md") or the RunInstances API, you can specify only one purchasing
option (one reservation type) per launch. To launch into multiple
reservation types in the group at once, use [Amazon EC2
Fleet](ec2-fleet.md "ec2-fleet.md") or [Auto Scaling
groups](../../../autoscaling/ec2/userguide.md "../../../autoscaling/ec2/userguide.md").

For step-by-step walkthroughs on how to launch instances into multiple Capacity Reservation
types using a Capacity Reservation Resource Group, see the following tutorials: via [EC2 Fleet](ec2-fleet-launch-instances-multiple-cr-types-walkthrough.md "ec2-fleet-launch-instances-multiple-cr-types-walkthrough.md") and
via [Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/use-distribution-segments.md "../../../autoscaling/ec2/userguide/use-distribution-segments.md").

## On-Demand Capacity Reservations

To launch instances into On-Demand Capacity Reservations in a group, specify the
group ARN using the `CapacityReservationTarget` parameter
with the `CapacityReservationResourceGroupArn` field.

Amazon EC2 launches instances into any matching On-Demand Capacity Reservation in the
group. If no matching capacity is available, the instances launch using
On-Demand capacity.

If you don't want instances to launch as On-Demand when no matching
capacity is available, set `CapacityReservationPreference` to
`capacity-reservations-only`. With this setting, instances
fail to launch if no matching On-Demand Capacity Reservation in the group has available
capacity.

Console

###### To launch instances into On-Demand Capacity Reservations in a group

1. Follow the procedure to launch an instance, but
   don't launch the instance until you've completed the
   following steps.
2. Expand **Advanced
   details**.
3. For **Purchasing option**, leave
   as **None** (default).
4. For **Capacity Reservation**,
   choose **Specify Capacity Reservation Resource
   Group** (default) or **Only launch
   in a Capacity Reservation Resource Group** (to prevent
   On-Demand fallback), then select the group.
5. Choose **Launch
   instance**.

AWS CLI

###### To launch instances into On-Demand Capacity Reservations in a group

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command with the
`--capacity-reservation-specification`
parameter.

The following example launches instances into a group. If
the group does not have an ODCR with matching attributes and
available capacity, the instances launch as On-Demand
instances.

```
aws ec2 run-instances \
    --instance-type `c5.xlarge` \
    --image-id `ami-0abcdef1234567890` \
    --count `3` \
    --capacity-reservation-specification \
        CapacityReservationTarget={CapacityReservationResourceGroupArn=`arn:aws:resource-groups:sa-east-1:123456789012:group/MyCRGroup`}
```

The following example launches instances into a group. If
the group does not have an ODCR with matching attributes and
available capacity, the instances fail to launch.

```
aws ec2 run-instances \
    --instance-type `c5.xlarge` \
    --image-id `ami-0abcdef1234567890` \
    --count `3` \
    --capacity-reservation-specification \
        CapacityReservationPreference=capacity-reservations-only,CapacityReservationTarget={CapacityReservationResourceGroupArn=`arn:aws:resource-groups:sa-east-1:123456789012:group/MyCRGroup`}
```

### Targeting a specific placement group

Optionally, if your group contains On-Demand Capacity Reservations in a placement
group, you can also specify the placement group ID along with the
Capacity Reservation Resource Group ARN to place all launched instances into that
placement group.

###### Note

Capacity Blocks do not support placement groups. You can't specify a
placement group when your request targets Capacity Blocks in a
Capacity Reservation Resource Group.

## Interruptible Capacity Reservations

To launch instances into interruptible Capacity Reservations in a group, specify the
group ARN and select the interruptible purchasing option. Amazon EC2 places
instances into any active interruptible Capacity Reservation in the group with matching
attributes and available capacity. If no matching capacity is available,
the instances fail to launch.

Console

###### To launch instances into interruptible Capacity Reservations in a group

1. Follow the procedure to launch an instance, but
   don't launch the instance until you've completed the
   following steps.
2. Expand **Advanced
   details**.
3. For **Purchasing option**, choose
   **Interruptible Capacity
   Reservations**.
4. For **Capacity Reservation**,
   choose **Specify Capacity Reservation Resource
   Group** and select the group.
5. Choose **Launch
   instance**.

AWS CLI

###### To launch instances into interruptible Capacity Reservations in a group

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command with the
`--instance-market-options` and
`--capacity-reservation-specification`
parameters.

```
aws ec2 run-instances \
    --instance-type `c5.xlarge` \
    --image-id `ami-0abcdef1234567890` \
    --count `3` \
    --instance-market-options MarketType=interruptible-capacity-reservation \
    --capacity-reservation-specification \
        CapacityReservationTarget={CapacityReservationResourceGroupArn=`arn:aws:resource-groups:sa-east-1:123456789012:group/MyCRGroup`}
```

## Capacity Blocks

To launch instances into Capacity Blocks in a group, specify the group
ARN and select the Capacity Blocks purchasing option. Amazon EC2 places
instances into any active Capacity Block in the group with matching
attributes and available capacity. If no matching capacity is available,
the instances fail to launch.

###### Note

You can't specify a placement group when launching into Capacity
Blocks in a Capacity Reservation Resource Group.

Console

###### To launch instances into Capacity Blocks in a group

1. Follow the procedure to launch an instance, but
   don't launch the instance until you've completed the
   following steps.
2. Expand **Advanced
   details**.
3. For **Purchasing option**, choose
   **Capacity Blocks**.
4. For **Capacity Reservation**,
   choose **Specify Capacity Reservation Resource
   Group** and select the group.
5. Choose **Launch
   instance**.

AWS CLI

###### To launch instances into Capacity Blocks in a group

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command with the
`--instance-market-options` and
`--capacity-reservation-specification`
parameters.

```
aws ec2 run-instances \
    --instance-type `p5.48xlarge` \
    --image-id `ami-0abcdef1234567890` \
    --count `1` \
    --instance-market-options MarketType=capacity-block \
    --capacity-reservation-specification \
        CapacityReservationTarget={CapacityReservationResourceGroupArn=`arn:aws:resource-groups:sa-east-1:123456789012:group/MyCRGroup`}
```
