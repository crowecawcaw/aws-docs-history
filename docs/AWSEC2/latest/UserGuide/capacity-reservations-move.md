# Move capacity between Capacity

Reservations

You can move capacity from one Capacity Reservation to another to redistribute your reserved compute
resources as needed. For example, if you need additional capacity in a reservation with
growing usage, and you have capacity available in another reservation, then you can
reallocate that capacity between the two reservations.

## Prerequisites for moving

capacity

As a prerequisite, the two Capacity Reservations must meet the following requirements:

- Both reservations must be in the active state.
- Both reservations must be owned by your AWS account. You cannot move
  capacity between reservations owned by different AWS accounts.
- Both reservations must have the same:
  - Instance type
  - Platform
  - Availability Zone
  - Tenancy
  - Placement group
  - End time

The destination Capacity Reservations instance eligibility (`open` or
`targeted`), and tags, don't have to match the source reservation.
The configuration of both reservations remains the same, except that the source
reservation has reduced capacity and the destination reservation has increased
capacity.

When you specify the quantity of instances to be moved, by default, any available
capacity is moved first, followed by any eligible running instances (the used
capacity in your reservation). For example, if you move 4 instances from a
reservation with 5 used instances and 3 available instances, then the 3 available
instances and 1 used instance will be moved.

###### Note

When you move used capacity from your reservation by specifying a **Quantity to move** that's greater than the available
capacity, only the instances that were launched with their **Capacity Reservation Specification** as `open` will be
moved.

## Considerations

The following considerations apply when moving capacity from one reservation to
another:

- The used capacity can only be moved between Capacity Reservations with `open`
  instance eligibility that are shared with the same set of accounts.
- When you move used capacity, the eligible instances are randomly selected.
  You cannot specify which running instances are moved. If a sufficient number
  of eligible instances are not found to fulfill the move quantity, the move
  operation will fail.
- If you move all of the capacity from the source reservation, the Capacity Reservation will
  be automatically canceled.
- **Future-dated Capacity Reservations** — You can't
  move capacity for a future-dated Capacity Reservation during the commitment period.

###### Note

Moving capacity from a Capacity Block isn't supported.

## Move capacity

You can move capacity from a source Capacity Reservation to a destination Capacity Reservation.

Console

###### To move capacity

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the left navigation pane, choose
   **Capacity Reservations**.
3. Select an On-Demand Capacity Reservation ID that has capacity to move.
4. Under **Actions**, **Manage
   capacity**, choose
   **Move**.
5. On the **Move capacity** page, under
   **Destination Capacity Reservation**, select a reservation
   from the list.
6. Under **Quantity to move**, use the slider or
   type the number of instances to move from the source Capacity Reservation to the
   destination Capacity Reservation.
7. Review the summary, and when you're ready, choose
   **Move**.

AWS CLI

###### To move capacity

Use the [move-capacity-reservation-instances](../../../cli/latest/reference/ec2/move-capacity-reservation-instances.md "../../../cli/latest/reference/ec2/move-capacity-reservation-instances.md") command.
The following example moves 10 instances from the specified
source Capacity Reservation to the specified destination Capacity Reservation.

```
aws ec2 move-capacity-reservation-instances \
    --source-capacity-reservation-id `cr-1234567890abcdef0` \
    --destination-capacity-reservation-id `cr-021345abcdef56789` \
    --instance-count `10`
```

PowerShell

###### To move capacity

Use the [Move-EC2CapacityReservationInstance](../../../powershell/latest/reference/items/Move-EC2CapacityReservationInstance.md "../../../powershell/latest/reference/items/Move-EC2CapacityReservationInstance.md") cmdlet.
The following example moves 10 instances from the specified
source Capacity Reservation to the specified destination Capacity Reservation.

```
Move-EC2CapacityReservationInstance `
    -SourceCapacityReservationId `cr-1234567890abcdef0` `
    -DestinationCapacityReservationId `cr-021345abcdef56789` `
    -InstanceCount `10`
```
