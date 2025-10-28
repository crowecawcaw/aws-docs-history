# Modify an active Capacity Reservation

If you have an existing Capacity Reservation which isn't a good fit for the workload that needs the
capacity, you can modify the instance quantity, instance eligibility (`open`
or `targeted`), and end time (`At specific time` or
`Manually`). If you specify a new instance quantity that exceeds your
remaining On-Demand Instance limit for the selected instance type, the update fails.

The allowed modifications depend on the state of the Capacity Reservation:

- `assessing` or `scheduled` state — You can modify
  the tags only.
- `pending` state — You can't modify the Capacity Reservation in any
  way.
- `active` state but still within the commitment duration —
  You can't decrease the instance count below the committed instance count, or set
  an end date that is before the committed duration. All other modifications are
  allowed.
- `active` state with no commitment duration or elapsed commitment
  duration — All modifications are allowed.
- `expired`, `cancelled`, `unsupported`, or
  `failed` state — You can't modify the Capacity Reservation in any
  way.

###### Considerations

- You can't change the instance type, platform, Availability Zone, or
  tenancy after creation. If you need to modify any of these attributes, we
  recommend that you cancel the reservation, and then create a new one with
  the required attributes.
- If you modify an existing Capacity Reservation by changing the instance eligibility from
  `targeted` to `open`, any running instances that
  match the attributes of the Capacity Reservation, have the
  `CapacityReservationPreference` parameter set to
  `open`, and are not yet running in a Capacity Reservation, will automatically
  use the modified Capacity Reservation.
- To change the instance eligibility, the Capacity Reservation must be completely idle (zero
  usage) because Amazon EC2 can't modify instance eligibility when instances are
  running inside the reservation.

Console

###### To modify a Capacity Reservation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Capacity Reservations**, select the Capacity Reservation to modify, and
   then choose **Edit**.
3. Modify the **Total capacity**, **Capacity Reservation
   ends**, or **Instance eligibility**
   options as needed, and choose **Save**.

AWS CLI

###### To modify a Capacity Reservation

Use the [modify-capacity-reservation](../../../cli/latest/reference/ec2/modify-capacity-reservation.md "../../../cli/latest/reference/ec2/modify-capacity-reservation.md") command. The
following example modifies the specified Capacity Reservation to reserve
capacity for eight instances.

```
aws ec2 modify-capacity-reservation \
    --capacity-reservation-id `cr-1234567890abcdef0` \
    --instance-count `8`
```

PowerShell

###### To modify a Capacity Reservation

Use the [Edit-EC2CapacityReservation](../../../powershell/latest/reference/items/Edit-EC2CapacityReservation.md "../../../powershell/latest/reference/items/Edit-EC2CapacityReservation.md") cmdlet. The following example
modifies the specified Capacity Reservation to reserve capacity for eight instances.

```
Edit-EC2CapacityReservation `
    -CapacityReservationId `cr-1234567890abcdef0` `
    -InstanceCount `8`
```
