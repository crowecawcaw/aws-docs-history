# View billing assignment requests for

shared EC2 Capacity Reservations

A Capacity Reservation owner can view only the most recent billing assignment request that
they initiated. And consumer accounts can view only the most recent billing
assignment requests sent to them.

Requests can be viewed for 24 hours after they enter the
`cancelled`, `expired`, or `revoked`
state. After 24 hours, they can no longer be viewed.

Console

###### (Capacity Reservation owner) To view requests you initiated

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, select **Capacity Reservations**
   and then choose the shared Capacity Reservation for which to view
   requests.
3. The **Billing of available capacity**
   section shows the most recent request and its current
   state.

###### (Consumer account) To requests sent to you

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, select
   **Capacity Reservations**.
3. If you have pending requests, the **Pending
   billing assignment requests** banner appears at
   the top of the screen. If the banner does not appear, you do
   not have pending requests.

To view the requests, choose **Review
requests** in the banner.

AWS CLI

###### (Capacity Reservation owner) To view requests you initiated

Use the [describe-capacity-reservation-billing-requests](../../../cli/latest/reference/ec2/describe-capacity-reservation-billing-requests.md "../../../cli/latest/reference/ec2/describe-capacity-reservation-billing-requests.md")
command.

```
aws ec2 describe-capacity-reservation-billing-requests \
    --role odcr-owner
```

###### (Consumer account) To view requests sent to you

Use the [describe-capacity-reservation-billing-requests](../../../cli/latest/reference/ec2/describe-capacity-reservation-billing-requests.md "../../../cli/latest/reference/ec2/describe-capacity-reservation-billing-requests.md")
command.

```
aws ec2 describe-capacity-reservation-billing-requests \
    --role unused-reservation-billing-owner
```

PowerShell

###### (Capacity Reservation owner) To view requests you initiated

Use the [Get-EC2CapacityReservationBillingRequest](../../../powershell/latest/reference/items/Get-EC2CapacityReservationBillingRequest.md "../../../powershell/latest/reference/items/Get-EC2CapacityReservationBillingRequest.md") cmdlet.

```
Get-EC2CapacityReservationBillingRequest `
    -Role odcr-owner
```

###### (Consumer account) To view requests sent to you

Use the [Get-EC2CapacityReservationBillingRequest](../../../powershell/latest/reference/items/Get-EC2CapacityReservationBillingRequest.md "../../../powershell/latest/reference/items/Get-EC2CapacityReservationBillingRequest.md") cmdlet.

```
Get-EC2CapacityReservationBillingRequest `
    -Role unused-reservation-billing-owner
```

A request can be in one of the following states.

| State       | Description                                                                                                                                                                                                                                                                                            |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `pending`   | The request has not been accepted or rejected, but it has not yet expired.                                                                                                                                                                                                                             |
| `accepted`  | The request was accepted by the specified account. Billing of available capacity of the Capacity Reservation is assigned to the consumer account.                                                                                                                                                      |
| `rejected`  | The request was rejected by the consumer account.                                                                                                                                                                                                                                                      |
| `cancelled` | The request was cancelled by the Capacity Reservation owner while it was in the `pending` state.                                                                                                                                                                                                       |
| `revoked`   | Billing was revoked from the consumer account for one of the following reasons: <br>• It was explicitly revoked by the Capacity Reservation owner. <br>• The Capacity Reservation is no longer shared with the consumer account. <br>• The consumer account is no longer part of the AWS organization. |
| `expired`   | The request expired because the consumer account did not accept or reject it within 12 hours.                                                                                                                                                                                                          |
