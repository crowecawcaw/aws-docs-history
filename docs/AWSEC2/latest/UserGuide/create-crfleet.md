# Create a Capacity Reservation Fleet

When you create a Capacity Reservation Fleet it automatically creates Capacity Reservations for the instance types
specified in the Fleet request, up to the specified total target capacity. The
number of instances for which the Capacity Reservation Fleet reserves capacity depends on the total
target capacity and instance type weights that you specify in the request. For more
information, see [Instance type weight](crfleet-concepts.md#instance-weight "crfleet-concepts.md#instance-weight")
and [Total target capacity](crfleet-concepts.md#target-capacity "crfleet-concepts.md#target-capacity").

When you create the Fleet, you must specify the instance types to use and a
priority for each of those instance types. For more information, see [Allocation strategy](crfleet-concepts.md#allocation-strategy "crfleet-concepts.md#allocation-strategy") and [Instance type priority](crfleet-concepts.md#instance-priority "crfleet-concepts.md#instance-priority").

###### Note

The **AWSServiceRoleForEC2CapacityReservationFleet** service-linked role is
automatically created in your account the first time that you create a
Capacity Reservation Fleet. For more information, see [Using service-linked roles for
Capacity Reservation Fleet](using-service-linked-roles.md "using-service-linked-roles.md").

Currently, Capacity Reservation Fleets support the `open` instance matching criteria
only.

AWS CLI

###### To create a Capacity Reservation Fleet

Use the [create-capacity-reservation-fleet](../../../cli/latest/reference/ec2/create-capacity-reservation-fleet.md "../../../cli/latest/reference/ec2/create-capacity-reservation-fleet.md") command.

```
aws ec2 create-capacity-reservation-fleet \
    --total-target-capacity `24` \
    --allocation-strategy prioritized \
    --instance-match-criteria open \
    --tenancy `default` \
    --end-date `2021-12-31T23:59:59.000Z` \
    --instance-type-specifications file://instanceTypeSpecification.json
```

The following are the contents of `instanceTypeSpecification.json`.

```
[
  {
    "InstanceType": "`m5.xlarge`",
    "InstancePlatform": "`Linux/UNIX`",
    "Weight": `3.0`,
    "AvailabilityZone":"`us-east-1a`",
    "EbsOptimized": true,
    "Priority" : `1`
  }
]
```

The following is example output.

```
{
    "Status": "submitted",
    "TotalFulfilledCapacity": 0.0,
    "CapacityReservationFleetId": "crf-abcdef01234567890",
    "TotalTargetCapacity": 24
}
```

PowerShell

###### To create a Capacity Reservation Fleet

Use the [New-EC2CapacityReservationFleet](../../../powershell/latest/reference/items/New-EC2CapacityReservationFleet.md "../../../powershell/latest/reference/items/New-EC2CapacityReservationFleet.md") cmdlet.

```
New-EC2CapacityReservationFleet `
    -TotalTargetCapacity `24` `
    -AllocationStrategy "prioritized" `
    -InstanceMatchCriterion "open" `
    -Tenancy "`default`" `
    -EndDate `2021-12-31T23:59:59.000Z` `
    -InstanceTypeSpecification $specification
```

The specification is defined as follows.

```
$specification = New-Object Amazon.EC2.Model.ReservationFleetInstanceSpecification
$specification.InstanceType = "`m5.xlarge`"
$specification.InstancePlatform = "`Linux/UNIX`"
$specification.Weight = `3.0`
$specification.AvailabilityZone = "`us-east-1a`"
$specification.EbsOptimized = $true
$specification.Priority = `1`
```
