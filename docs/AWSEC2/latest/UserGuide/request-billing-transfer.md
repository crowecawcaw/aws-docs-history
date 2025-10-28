# Assign billing of a shared EC2 Capacity Reservation

to another account

To assign billing of the available capacity of a shared Capacity Reservation to another
account, the Capacity Reservation owner must initiate a request to the required account. In the
Amazon EC2 console, this request is called a _transfer
request_.

A Capacity Reservation owner can assign billing of the available capacity of Capacity Reservation to an
account only if:

- The Capacity Reservation is already shared with that account.
- The account is consolidated under the same AWS Organizations payer account as
  the Capacity Reservation owner.
  Billing is assigned to the specified account only once they accept the
  request.

When a Capacity Reservation owner initiates a request, an Amazon EventBridge event is sent to the
requested account. For more information, see [Monitor billing assignment requests
for shared Capacity Reservations](billing-ownership-events.md "billing-ownership-events.md").

Console

###### To assign billing of a shared Capacity Reservation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, select **Capacity Reservations**
   and then choose the shared Capacity Reservation.
3. In the **Billing of available capacity**
   section, choose **Assign billing**.
4. In the **Assign billing** screen, select
   the consumer account to which to assign billing, and then
   choose **Request**.

AWS CLI

###### To assign billing of a shared Capacity Reservation

Use the [associate-capacity-reservation-billing-owner](../../../cli/latest/reference/ec2/associate-capacity-reservation-billing-owner.md "../../../cli/latest/reference/ec2/associate-capacity-reservation-billing-owner.md") command.
For `--capacity-reservation-id`, specify the ID of the shared Capacity Reservation.
For `--unused-reservation-billing-owner-id`, specify
the ID of the AWS account to which to assign billing.

```
aws ec2 associate-capacity-reservation-billing-owner \
    --capacity-reservation-id `cr-01234567890abcdef` \
    --unused-reservation-billing-owner-id `123456789012`
```

PowerShell

###### To assign billing of a shared Capacity Reservation

Use the [Register-EC2CapacityReservationBillingOwner](../../../powershell/latest/reference/items/Register-EC2CapacityReservationBillingOwner.md "../../../powershell/latest/reference/items/Register-EC2CapacityReservationBillingOwner.md") cmdlet.
For `-CapacityReservationId`, specify the
ID of the shared Capacity Reservation. For `-UnusedReservationBillingOwnerId`,
specify the ID of the AWS account to which to assign billing.

```
Register-EC2CapacityReservationBillingOwner `
    -CapacityReservationId `cr-01234567890abcdef` `
    -UnusedReservationBillingOwnerId `123456789012`
```
