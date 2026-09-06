

# Modify the Capacity Reservation settings of your instance
<a name="capacity-reservations-modify-instance"></a>

You can modify the following Capacity Reservation settings for a stopped instance at any time:
+ Start in any Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, and tenancy) and available capacity.
+ Start the instance in a specific Capacity Reservation.
+ Start in any Capacity Reservation that has matching attributes and available capacity in a Capacity Reservation group
+ Prevent the instance from starting in a Capacity Reservation.

------
#### [ Console ]

**To modify instance Capacity Reservation settings**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Instances** and select the instance to modify. Stop the instance if it is not already stopped.

1. Choose **Actions**, **Instance settings**, **Modify Capacity Reservation Settings**.

1. For **Capacity Reservation**, choose one of the following options:
   + **Open** – Launches the instances into any Capacity Reservation that has matching attributes and sufficient capacity for the number of instances you selected. If there is no matching Capacity Reservation with sufficient capacity, the instance uses On-Demand capacity.
   + **None** – Prevents the instances from launching into a Capacity Reservation. The instances run in On-Demand capacity.
   + **Specify Capacity Reservation** – Launches the instances into the selected Capacity Reservation. If the selected Capacity Reservation does not have sufficient capacity for the number of instances you selected, the instance launch fails.
   + **Specify Capacity Reservation group** – Launches the instances into any Capacity Reservation with matching attributes and available capacity in the selected Capacity Reservation group. If the selected group does not have a Capacity Reservation with matching attributes and available capacity, the instances launch into On-Demand capacity.
   + **Specify Capacity Reservation only** – Launches the instances into a Capacity Reservation. If a Capacity Reservation ID isn't specified, the instances launch into an open Capacity Reservation. If capacity isn't available, the instances fail to launch.
   + **Specify Capacity Reservation Resource Group only** – Launches the instances into a Capacity Reservation in a Capacity Reservation Resource Group. If a Capacity Reservation Resource Group ARN isn't specified, the instances launch into an open Capacity Reservation. If capacity isn't available, the instances fail to launch.

------
#### [ AWS CLI ]

**To modify instance Capacity Reservation settings**  
Use the [modify-instance-capacity-reservation-attributes](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-capacity-reservation-attributes.html) command.

The following example changes the Capacity Reservation preference to `none`.

```
aws ec2 modify-instance-capacity-reservation-attributes \
    --instance-id {{i-1234567890abcdef0}} \
    --capacity-reservation-specification CapacityReservationPreference=none
```

The following example the target to a specific Capacity Reservation.

```
aws ec2 modify-instance-capacity-reservation-attributes \
    --instance-id {{i-1234567890abcdef0}} \
    --capacity-reservation-specification \
    CapacityReservationTarget={CapacityReservationId={{cr-1234567890abcdef0}}}
```

The following example changes the target to a specific Capacity Reservation group.

```
aws ec2 modify-instance-capacity-reservation-attributes \
    --instance-id {{i-1234567890abcdef0}} \
    --capacity-reservation-specification \
        CapacityReservationTarget={CapacityReservationResourceGroupArn=arn:aws:resource-groups:{{us-west-2}}:{{123456789012}}:group/{{my-cr-group}}}
```

The following example changes the Capacity Reservation preference to `capacity-reservation-only`. Because it doesn't specify a Capacity Reservation, instances launch into any open Capacity Reservation with matching attributes and available capacity.

```
aws ec2 modify-instance-capacity-reservation-attributes \
    --instance-id {{i-1234567890abcdef0}} \
    --capacity-reservation-specification CapacityReservationPreference=capacity-reservation-only
```

The following example changes the Capacity Reservation preference to `capacity-reservation-only` and changes the target to a specific Capacity Reservation. If capacity isn't available in the specified Capacity Reservation, the instances fail to launch.

```
aws ec2 modify-instance-capacity-reservation-attributes \
    --instance-id {{i-1234567890abcdef0}} \
    --capacity-reservation-specification \
        CapacityReservationPreference=capacity-reservation-only \
        CapacityReservationTarget={CapacityReservationId={{cr-1234567890abcdef0}}}
```

------
#### [ PowerShell ]

**To modify instance Capacity Reservation settings**  
Use the [Edit-EC2InstanceCapacityReservationAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceCapacityReservationAttribute.html) cmdlet.

The following example changes the Capacity Reservation preference to `none`.

```
Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId {{i-1234567890abcdef0}} `
    -CapacityReservationSpecification_CapacityReservationPreference "none"
```

The following example the target to a specific Capacity Reservation.

```
Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId {{i-1234567890abcdef0}} `
    -CapacityReservationTarget_CapacityReservationId {{cr-1234567890abcdef0}}
```

The following example changes the target to a specific Capacity Reservation group.

```
Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId {{i-1234567890abcdef0}} `
    -CapacityReservationTarget_CapacityReservationResourceGroupArn `
        "arn:aws:resource-groups:{{us-west-2}}:{{123456789012}}:group/{{my-cr-group}}"
```

The following example changes the Capacity Reservation preference to `capacity-reservation-only`. Because it doesn't specify a Capacity Reservation, instances launch into any open Capacity Reservation with matching attributes and available capacity.

```
Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId {{i-1234567890abcdef0}} `
    -CapacityReservationSpecification_CapacityReservationPreference "capacity-reservation-only"
```

The following example changes the Capacity Reservation preference to `capacity-reservation-only` and changes the target to a specific Capacity Reservation. If capacity isn't available in the specified Capacity Reservation, the instances fail to launch.

```
Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId {{i-1234567890abcdef0}} `
    -CapacityReservationSpecification_CapacityReservationPreference "capacity-reservation-only" `
    -CapacityReservationTarget_CapacityReservationId {{cr-1234567890abcdef0}}
```

------