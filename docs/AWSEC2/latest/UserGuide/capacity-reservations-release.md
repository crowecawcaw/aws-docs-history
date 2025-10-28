# Cancel a Capacity Reservation

You can cancel a Capacity Reservation that is in one of the following states:

- `assessing`
- `active` and there is no commitment duration or the commitment
  duration has elapsed. You can't cancel a future-dated Capacity Reservation during the commitment
  duration.

###### Note

You can't modify or cancel a Capacity Block. For more information, see [Capacity Blocks for ML](ec2-capacity-blocks.md "ec2-capacity-blocks.md").

If a future-dated Capacity Reservation enters the `delayed` state, the commitment duration
is waived, and you can cancel it as soon as it enters the `active`
state.

When you cancel a Capacity Reservation, the capacity is released immediately, and it is no longer
reserved for your use.

You can cancel empty Capacity Reservations and Capacity Reservations that have running instances. If you cancel a Capacity Reservation
that has running instances, the instances continue to run normally outside of the
capacity reservation at standard On-Demand Instance rates or at a discounted rate if you have a
matching Savings Plans or Regional Reserved Instance.

After you cancel a Capacity Reservation, instances that target it can no longer launch. Modify these
instances so that they either target a different Capacity Reservation, launch into any open Capacity Reservation with
matching attributes and sufficient capacity, or avoid launching into a Capacity Reservation. For more
information, see [Modify the Capacity Reservation settings of your
instance](capacity-reservations-modify-instance.md "capacity-reservations-modify-instance.md").

Console

###### To cancel a Capacity Reservation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Capacity Reservations** and select the Capacity Reservation to
   cancel.
3. Choose **Cancel reservation**, **Cancel
   reservation**.

AWS CLI

###### To cancel a Capacity Reservation

Use the [cancel-capacity-reservation](../../../cli/latest/reference/ec2/cancel-capacity-reservation.md "../../../cli/latest/reference/ec2/cancel-capacity-reservation.md") command.

```
aws ec2 cancel-capacity-reservation \
    --capacity-reservation-id `cr-1234567890abcdef0`
```

PowerShell

###### To cancel a Capacity Reservation

Use the [Remove-EC2CapacityReservation](../../../powershell/latest/reference/items/Remove-EC2CapacityReservation.md "../../../powershell/latest/reference/items/Remove-EC2CapacityReservation.md") cmdlet.

```
Remove-EC2CapacityReservation `
    -CapacityReservationId `cr-1234567890abcdef0`
```
