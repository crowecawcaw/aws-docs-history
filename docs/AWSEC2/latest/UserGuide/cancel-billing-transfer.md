# Cancel or revoke billing assignment

requests for shared EC2 Capacity Reservations

Only the Capacity Reservation owner can cancel a `pending` billing assignment
request. If a pending request is cancelled, it enters the `cancelled`
state and billing of any available, or _unused_, capacity of
the Capacity Reservation remains assigned to Capacity Reservation owner.

After a request is `accepted`, only the Capacity Reservation owner can revoke
billing from the assigned account. If billing is revoked, the request enters the
`revoked` state and billing of any available capacity of the Capacity Reservation
is reassigned to Capacity Reservation owner.

When a request is cancelled or revoked, Amazon EventBridge events are sent to the
Capacity Reservation owner and specified consumer account. For more information, see [Monitor billing assignment requests
for shared Capacity Reservations](billing-ownership-events.md "billing-ownership-events.md").

Console

###### To cancel or revoke a request

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, select **Capacity Reservations**
   and then choose the Capacity Reservation for which to cancel or revoke the
   request.
3. In the **Billing of available capacity**
   section, choose **Cancel transfer** or
   **Revoke transfer**, depending on the
   current state of the request.

AWS CLI

###### To cancel or revoke a request

Use the [disassociate-capacity-reservation-billing-owner](../../../cli/latest/reference/ec2/disassociate-capacity-reservation-billing-owner.md "../../../cli/latest/reference/ec2/disassociate-capacity-reservation-billing-owner.md")
command. For `--unused-reservation-billing-owner-id`,
specify the ID of the AWS account to which the request was
sent.

```
aws ec2 disassociate-capacity-reservation-billing-owner \
    --capacity-reservation-id `cr-01234567890abcdef` \
    --unused-reservation-billing-owner-id `123456789012`
```

PowerShell

###### To cancel or revoke a request

Use the [Unregister-EC2CapacityReservationBillingOwner](../../../powershell/latest/reference/items/Unregister-EC2CapacityReservationBillingOwner.md "../../../powershell/latest/reference/items/Unregister-EC2CapacityReservationBillingOwner.md")
cmdlet. For `-UnusedReservationBillingOwnerId`,
specify the ID of the AWS account to which the request was
sent.

```
Unregister-EC2CapacityReservationBillingOwner `
    -CapacityReservationId `cr-01234567890abcdef` `
    -UnusedReservationBillingOwnerId `123456789012`
```
