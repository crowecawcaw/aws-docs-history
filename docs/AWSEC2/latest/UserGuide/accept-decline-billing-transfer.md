

# Accept or reject billing of a shared EC2 Capacity Reservation
<a name="accept-decline-billing-transfer"></a>

If you receive a billing assignment request for a Capacity Reservation that is shared with you, you can either accept or reject it. The request remains in the `pending` state until it is accepted or rejected.

If you accept the request, it enters the `accepted` state, and billing of any available, or *unused*, capacity of that Capacity Reservation is assigned to your account from that point onward. After you accept a request, only the Capacity Reservation owner can revoke billing from your account.

If you reject the request, it enters the `rejected` state, and billing of the available capacity of the Capacity Reservation remains assigned to the Capacity Reservation owner.

Requests expire if they are not accepted or rejected within 12 hours. If a request expires, billing of any unused capacity of the Capacity Reservation remains assigned to the Capacity Reservation owner.

When a request is accepted or rejected, an Amazon EventBridge event is sent to the Capacity Reservation owner's account. When a request expires, an Amazon EventBridge event is sent to the Capacity Reservation owner and the consumer account. For more information, see [Monitor billing assignment requests for shared Capacity Reservations](billing-ownership-events.md).

------
#### [ Console ]

**To accept or reject a request**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation panel, select **Capacity Reservations**.

1. If you have pending requests, the **Pending billing assignment requests** banner appears at the top of the screen. If the banner does not appear, you do not have pending requests.

   To view the requests, choose **Review requests** in the banner.

1. Select the request to accept or reject, and then choose either **Accept** or **Reject**.

------
#### [ AWS CLI ]

**To accept a request**  
Use the [accept-capacity-reservation-billing-ownership](https://docs.aws.amazon.com/cli/latest/reference/ec2/accept-capacity-reservation-billing-ownership.html) command. For `--capacity-reservation-id`, specify the ID of the Capacity Reservation for which to accept the request.

```
aws ec2 accept-capacity-reservation-billing-ownership \
    --capacity-reservation-id {{cr-01234567890abcdef}}
```

**To reject a request**  
Use the [reject-capacity-reservation-billing-ownership](https://docs.aws.amazon.com/cli/latest/reference/ec2/reject-capacity-reservation-billing-ownership.html) command. For `--capacity-reservation-id`, specify the ID of the Capacity Reservation for which to reject the request.

```
aws ec2 reject-capacity-reservation-billing-ownership \
    --capacity-reservation-id {{cr-01234567890abcdef}}
```

------
#### [ PowerShell ]

**To accept a request**  
Use the [Approve-EC2CapacityReservationBillingOwnership](https://docs.aws.amazon.com/powershell/latest/reference/items/Approve-EC2CapacityReservationBillingOwnership.html) cmdlet.

```
Approve-EC2CapacityReservationBillingOwnership `
    -CapacityReservationId {{cr-01234567890abcdef}}
```

**To reject a request**  
Use the [Deny-EC2CapacityReservationBillingOwnership](https://docs.aws.amazon.com/powershell/latest/reference/items/Deny-EC2CapacityReservationBillingOwnership.html) cmdlet.

```
Deny-EC2CapacityReservationBillingOwnership `
    -CapacityReservationId {{cr-01234567890abcdef}}
```

------