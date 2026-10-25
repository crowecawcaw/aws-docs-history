

# Canceling a Capacity Reservation
<a name="capacity-reservations.canceling"></a>

Canceling a reservation releases the reserved capacity and stops the associated charges. Any DB instances currently running in the reservation continue to run as normal On-Demand instances.

You can cancel a reservation that is in the `active`, `assessing`, or `delayed` state:
+ `active` – cancel at any time, unless the reservation is still within a commitment duration. A future-dated reservation that has become active can't be canceled until its commitment ends.
+ `assessing` – a future-dated reservation can be canceled while Amazon RDS is still evaluating whether it can deliver the capacity, because no commitment has begun.
+ `delayed` – if Amazon RDS couldn't deliver the capacity on the requested start date, the commitment is waived and you can cancel the reservation immediately.

A reservation in the `scheduled` state can't be canceled. After Amazon RDS accepts a future-dated request and schedules the capacity, the reservation stays in place until its start date, becomes active, and can then be canceled only after its commitment duration ends. Take that into account when you choose a start date and a commitment duration.

Reservations in the `pending`, `expired`, `cancelled`, `failed`, or `unsupported` state can't be canceled. An expired or canceled reservation has already released its capacity.

## Console
<a name="capacity-reservations.canceling.console"></a>

**To cancel a Capacity Reservation**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Capacity reservations**.

1. Select the reservation.

1. Choose **Cancel reservation**, and then confirm the cancellation.

## AWS CLI
<a name="capacity-reservations.canceling.cli"></a>

Use the [cancel-db-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/rds/cancel-db-capacity-reservation.html) command.

```
1. aws rds cancel-db-capacity-reservation \
2.     --db-capacity-reservation-identifier {{my-reservation}}
```

## RDS API
<a name="capacity-reservations.canceling.api"></a>

To cancel a Capacity Reservation by using the Amazon RDS API, call the [CancelDBCapacityReservation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CancelDBCapacityReservation.html) operation with the following parameter:
+ `DBCapacityReservationIdentifier` – The name or the `dbcr-` ID of the Capacity Reservation.