# Launch instances into an existing

Capacity Reservation

You can only launch an instance into a Capacity Reservation that:

- Has matching attributes (instance type, platform, Availability Zone, and
  tenancy)
- Has sufficient available capacity
- Is in the `active` state
  When you launch an instance, you can specify whether to launch the instance into any
  `open` Capacity Reservation, into a specific Capacity Reservation, or into a group of Capacity Reservations.

Alternatively, you can configure the instance to avoid running in a Capacity Reservation, even if you
have an `open` Capacity Reservation that has matching attributes and available capacity.

Launching an instance into a Capacity Reservation reduces its available capacity by the number of
instances launched. For example, if you launch three instances, the available capacity
of the Capacity Reservation is reduced by three.

Console

###### To launch instances into an existing Capacity Reservation

1. Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"), but don't launch the instance until
   you've completed the following steps to specify the settings for the
   placement group and Capacity Reservation.
2. Expand **Advanced details** and do the
   following:
   1. For **Placement group**, select the
      cluster placement group in which to launch the
      instance.
   2. For **Capacity Reservation**, choose one of the following
      options depending on the configuration of the Capacity Reservation:
      - **None** – Prevents the
        instances from launching into a Capacity Reservation. The instances
        run in On-Demand capacity.
      - **Open** – Launches the
        instances into any Capacity Reservation that has matching attributes
        and sufficient capacity for the number of instances
        you selected. If there is no matching Capacity Reservation with
        sufficient capacity, the instance uses On-Demand
        capacity.
      - **Specify Capacity Reservation** – Launches
        the instances into the selected Capacity Reservation. If the
        selected Capacity Reservation does not have sufficient capacity for
        the number of instances you selected, the instance
        launch fails.
      - **Specify Capacity Reservation resource group**
        – Launches the instances into any Capacity Reservation with
        matching attributes and available capacity in the
        selected Capacity Reservation group. If the selected group does not
        have a Capacity Reservation with matching attributes and available
        capacity, the instances launch into On-Demand
        capacity.
      - **Specify Capacity Reservation only** –
        Launches the instances into a Capacity Reservation. If a Capacity Reservation ID
        isn't specified, the instances launch into an open
        Capacity Reservation. If capacity isn't available, the instances
        fail to launch.
      - **Specify Capacity Reservation resource group
        only** – Launches the instances
        into a Capacity Reservation in a Capacity Reservation resource group. If a Capacity Reservation
        resource group ARN isn't specified, the instances
        launch into an open Capacity Reservation. If capacity isn't
        available, the instances fail to launch.

3. In the **Summary** panel, review your instance
   configuration, and then choose **Launch instance**.

AWS CLI

###### To launch an instance into an existing Capacity Reservation

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command and specify the
`--capacity-reservation-specification` option.

The following example launches an instance into any open Capacity Reservation
with matching attributes and available capacity:

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --count `1` \
    --instance-type `t2.micro` \
    --key-name `my-key-pair` \
    --subnet-id `subnet-0abcdef1234567890` \
    --capacity-reservation-specification CapacityReservationPreference=open
```

The following example launches an instance into a `targeted` Capacity Reservation:

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --count `1` \
    --instance-type `t2.micro` \
    --key-name `my-key-pair` \
    --subnet-id `subnet-0abcdef1234567890` \
    --capacity-reservation-specification \
        CapacityReservationTarget={CapacityReservationId=`cr-1234abcd56EXAMPLE`}
```

The following example launches an instance into the specified Capacity Reservation group:

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --count `1` \
    --instance-type `t2.micro` \
    --key-name `my-key-pair` \
    --subnet-id `subnet-0abcdef1234567890` \
    --capacity-reservation-specification \
        CapacityReservationTarget={CapacityReservationResourceGroupArn=arn:aws:resource-groups:`us-west-2`:`123456789012`:group/`my-cr-group`}
```

The following example launches an instance into a Capacity Reservation only. Because it
does not specify a Capacity Reservation ID, the instance launches in any open Capacity Reservation with
matching attributes and available capacity:

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --count `1` \
    --instance-type `t2.micro` \
    --key-name `my-key-pair` \
    --subnet-id `subnet-0abcdef1234567890` \
    --capacity-reservation-specification \
        CapacityReservationPreference=capacity-reservations-only
```

The following example launches an instance into a specific Capacity Reservation only.
If capacity isn't available in the specified Capacity Reservation, the instance fails to launch.

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --count `1` \
    --instance-type `t2.micro` \
    --key-name `my-key-pair` \
    --subnet-id `subnet-0abcdef1234567890` \
    --capacity-reservation-specification \
        CapacityReservationPreference=`capacity-reservations-only` \
        CapacityReservationTarget={CapacityReservationId=`cr-1234abcd56EXAMPLE`}
```

PowerShell

###### To launch an instance into an existing Capacity Reservation

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") cmdlet.

The following example launches an instance into any open Capacity Reservation
with matching attributes and available capacity:

```
New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `t2.micro` `
    -KeyName "`my-key-pair`" `
    -SubnetId `subnet-0abcdef1234567890` `
    -CapacityReservationSpecification_CapacityReservationPreference "open"
```

The following example launches an instance into a `targeted` Capacity Reservation:

```
New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `t2.micro` `
    -KeyName "`my-key-pair`" `
    -SubnetId `subnet-0abcdef1234567890` `
    -CapacityReservationTarget_CapacityReservationId `cr-1234abcd56EXAMPLE`
```

The following example launches an instance into the specified Capacity Reservation group:

```
New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `t2.micro` `
    -KeyName "`my-key-pair`" `
    -SubnetId `subnet-0abcdef1234567890` `
    -CapacityReservationTarget_CapacityReservationResourceGroupArn `
        "arn:aws:resource-groups:`us-west-2`:`123456789012`:group/`my-cr-group`"
```

The following example launches an instance into a Capacity Reservation only. Because it
does not specify a Capacity Reservation ID, the instance launches in any open Capacity Reservation with
matching attributes and available capacity:

```
New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `t2.micro` `
    -KeyName "`my-key-pair`" `
    -SubnetId `subnet-0abcdef1234567890` `
    -CapacityReservationSpecification_CapacityReservationPreference "capacity-reservations-only"
```

The following example launches an instance into a specific Capacity Reservation only.
If capacity isn't available in the specified Capacity Reservation, the instance fails to launch.

```
New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `t2.micro` `
    -KeyName "`my-key-pair`" `
    -SubnetId `subnet-0abcdef1234567890` `
    -CapacityReservationSpecification_CapacityReservationPreference "capacity-reservations-only" `
    -CapacityReservationTarget_CapacityReservationId `cr-1234abcd56EXAMPLE`
```
