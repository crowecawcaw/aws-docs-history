# View Capacity Blocks

After you reserve a Capacity Block, you can view the Capacity Block reservation in your AWS
account. You can view the `start-date` and `end-date` to see
when your reservation will begin and end. Before a Capacity Block reservation begins, the
available capacity appears as zero. You can see how many instances will be available
in your Capacity Block by the tag value for the tag key
`aws:ec2capacityreservation:incrementalRequestedQuantity`.

When a Capacity Block reservation begins, the reservation state changes from
`scheduled` to `active`. We emit an event through Amazon EventBridge
to notify you that the Capacity Block is available to use. For more information, see [Monitor Capacity Blocks using EventBridge](capacity-blocks-monitor.md "capacity-blocks-monitor.md").

Capacity Blocks have the following states:

- `payment-pending` – The upfront payment hasn't been
  processed yet.
- `payment-failed`—The payment couldn't be processed in
  the 12 hour time frame. Your Capacity Block was released.
- `scheduled` – The payment was processed and the Capacity Block
  reservation hasn't started yet.
- `active` – The reserved capacity is available for your
  use.
- `expired` – The Capacity Block reservation expired
  automatically at the date and time specified in your reservation request.
  The reserved capacity is no longer available for your use.

Console

###### To view Capacity Blocks

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Capacity Reservations**.
3. On the **Capacity Reservations overview** page, you see a
   resource table with details about all of your Capacity Reservation resources. To
   find your Capacity Blocks reservations, select
   **Capacity Blocks** from the dropdown list above
   **Capacity Reservation ID**. In the table, you can see
   information about your Capacity Blocks such as start and end dates,
   duration, and status.
4. For more details about a Capacity Block, select the reservation ID
   for the Capacity Block that you want to view. The **Capacity Reservation
   details** page displays all the properties of the
   reservation and the number of instances in use and available in
   the Capacity Block.

###### Note

Before a Capacity Block reservation begins, the available
capacity appears as zero. You can see how many instances
will be available when the Capacity Block reservation starts by
using the following tag value for the tag key:
`aws:ec2capacityreservation:incrementalRequestedQuantity`.

AWS CLI

###### To view Capacity Blocks

By default, when you use the [describe-capacity-reservations](../../../cli/latest/reference/ec2/describe-capacity-reservations.md "../../../cli/latest/reference/ec2/describe-capacity-reservations.md") command both On-Demand Capacity Reservations
and Capacity Block reservations are listed. To view only your Capacity Block
reservations, filter for reservations of type `capacity-block`.

```
aws ec2 describe-capacity-reservations \
    --filters Name=reservation-type,Values=capacity-block
```

PowerShell

###### To view Capacity Blocks

Use the [Get-EC2CapacityReservation](../../../powershell/latest/reference/items/Get-EC2CapacityReservation.md "../../../powershell/latest/reference/items/Get-EC2CapacityReservation.md")
cmdlet. By default, both On-Demand Capacity Reservations and Capacity Block reservations are listed.
To view only your Capacity Block reservations, filter for reservations of type
`capacity-block`.

```
Get-EC2CapacityReservation `
    -Filter @{Name="reservation-type"; Values="capacity-block"}
```
