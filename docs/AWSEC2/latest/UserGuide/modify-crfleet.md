# Modify a Capacity Reservation Fleet

You can modify the total target capacity and date of a Capacity Reservation Fleet at any time. When
you modify the total target capacity of a Capacity Reservation Fleet, the Fleet automatically creates
new Capacity Reservations, or modifies or cancels existing Capacity Reservations in the Fleet to meet the new total
target capacity. When you modify the end date for the Fleet, the end dates for all
of the individual Capacity Reservations are updated accordingly.

###### Considerations

- After you modify a Fleet, its status transitions to `modifying`. You
  can't attempt additional modifications to a Fleet while it is in the
  `modifying` state.
- You can't modify the tenancy, Availability Zone, instance types, instance
  platforms, priorities, or weights used by a Capacity Reservation Fleet. If you need to change any of
  these parameters, you might need to cancel the existing Fleet and create a new one
  with the required parameters.
- You can't specify `--end-date` and `--remove-end-date`
  in the same command.

AWS CLI

###### To modify a Capacity Reservation Fleet

Use the [modify-capacity-reservation-fleet](../../../cli/latest/reference/ec2/modify-capacity-reservation-fleet.md "../../../cli/latest/reference/ec2/modify-capacity-reservation-fleet.md") command.

**Example 1: Modify total target capacity**

```
aws ec2 modify-capacity-reservation-fleet \
    --capacity-reservation-fleet-id `crf-01234567890abcedf` \
    --total-target-capacity `160`
```

**Example 2: Modify end date**

```
aws ec2 modify-capacity-reservation-fleet \
    --capacity-reservation-fleet-id `crf-01234567890abcedf` \
    --end-date `2021-07-04T23:59:59.000Z`
```

**Example 3: Remove end date**

```
aws ec2 modify-capacity-reservation-fleet \
    --capacity-reservation-fleet-id `crf-01234567890abcedf` \
    --remove-end-date
```

PowerShell

###### To modify a Capacity Reservation Fleet

Use the [Edit-EC2CapacityReservationFleet](../../../powershell/latest/reference/items/Edit-EC2CapacityReservationFleet.md "../../../powershell/latest/reference/items/Edit-EC2CapacityReservationFleet.md") cmdlet.

**Example 1: Modify total target capacity**

```
Edit-EC2CapacityReservationFleet `
    -CapacityReservationFleetId `crf-01234567890abcedf` `
    -TotalTargetCapacity `160`
```

**Example 2: Modify end date**

```
Edit-EC2CapacityReservationFleet `
    -CapacityReservationFleetId `crf-01234567890abcedf` `
    -EndDate `2021-07-04T23:59:59.000Z`
```

**Example 3: Remove end date**

```
Edit-EC2CapacityReservationFleet `
    -CapacityReservationFleetId `crf-01234567890abcedf` `
    -RemoveEndDate
```
