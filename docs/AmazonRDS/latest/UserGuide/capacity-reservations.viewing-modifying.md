

# Viewing and modifying your Capacity Reservations
<a name="capacity-reservations.viewing-modifying"></a>

After you create a Capacity Reservation, you can view its state and capacity usage at any time, and change the amount of capacity it reserves as your needs change. Viewing a reservation shows the capacity reserved and still available in each Availability Zone, along with its start and end dates, commitment information, and lifecycle state. Modifying a reservation changes the number of DB instances reserved in each Availability Zone while the reservation is active.

**Topics**
+ [Viewing Capacity Reservations](#capacity-reservations.viewing)
+ [Modifying a Capacity Reservation](#capacity-reservations.modifying)

## Viewing Capacity Reservations
<a name="capacity-reservations.viewing"></a>

You can view Amazon RDS Capacity Reservations using the AWS Management Console, the AWS CLI, or the Amazon RDS API.

### Console
<a name="capacity-reservations.viewing.console"></a>

**To view Capacity Reservations**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Capacity reservations**.

1. Select a reservation to see its state, reserved capacity, available capacity in each Availability Zone, start and end dates, and commitment information.  
![Details page for my-reservation: PostgreSQL, db.r7g.large, 2 of 2 units available in us-east-1a.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/odcr-reservation-details-rds.png)

### AWS CLI
<a name="capacity-reservations.viewing.cli"></a>

Use the [describe-db-capacity-reservations](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-capacity-reservations.html) command.

List all reservations in the Region:

```
1. aws rds describe-db-capacity-reservations
```

Describe a specific reservation, by name or by ID:

```
1. aws rds describe-db-capacity-reservations \
2.     --db-capacity-reservation-identifier {{my-reservation}}
```

The response includes `ReservedCapacityPerAvailabilityZone` (capacity reserved in each Availability Zone) and `AvailableCapacityPerAvailabilityZoneList` (capacity not yet in use, broken out by Availability Zone), which you can use to monitor utilization and find which Availability Zone has little available capacity.

### RDS API
<a name="capacity-reservations.viewing.api"></a>

To view Capacity Reservations by using the Amazon RDS API, call the [DescribeDBCapacityReservations](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBCapacityReservations.html) operation. You can specify the following optional parameters:
+ `DBCapacityReservationIdentifier` – The name or the `dbcr-` ID of the Capacity Reservation. If you don't specify it, the operation returns all the Capacity Reservations in the Region.
+ `Filters` – Filters that limit the result. The supported filters are `db-capacity-reservation-name`, `state`, `engine`, `db-instance-class`, and `availability-zone`.
+ `MaxRecords` – The maximum number of records to return, from 20 to 100. The default is 100.
+ `Marker` – The pagination token from a previous request.

## Modifying a Capacity Reservation
<a name="capacity-reservations.modifying"></a>

You can change the reserved capacity of a reservation, that is, the number of DB instances reserved in each Availability Zone. You can also change its end date.

You can modify a reservation only while it is `active` and has not reached its end date. A future-dated reservation can't be modified while it is in the `assessing`, `scheduled`, or `delayed` state – wait until it becomes active on its start date. Reservations in the `pending`, `expired`, `cancelled`, `failed`, or `unsupported` state can't be modified.

The following limits apply to a change in reserved capacity:
+ You can't reduce the capacity below the capacity already in use. The new value must fit the Availability Zone that holds the most DB instances.
+ Increasing the capacity depends on capacity being available, and on your account's Capacity Reservation quota.
+ While a reservation is still within its commitment duration, you can't reduce its capacity below the committed capacity, and you can't set an end date earlier than the commitment end date. For a reservation that was `delayed`, the capacity limit applies until the original commitment end date, but the end date limit doesn't apply.

### Console
<a name="capacity-reservations.modifying.console"></a>

**To modify a Capacity Reservation**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Capacity reservations**.

1. In the list of reservations, select the reservation.

1. For **Actions**, choose **Edit**.

1. Under **Capacity reservation details**, do the following:
   + For **Reserved capacity per AZ**, enter the new number of DB instances to reserve in each Availability Zone.
   + (Optional) For **Capacity reservation ends**, choose **Manually** to keep the reservation until you cancel it, or **At a specific time** to set an end date.  
![Edit page for my-reservation: reserved capacity per AZ of 2, with the end set to Manually.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/odcr-modify-reservation.png)

1. Review the cost impact, and then choose **Save changes**. An increase in capacity or a later end date adds charges immediately. A decrease in capacity or an earlier end date doesn't refund charges for the time that has already passed.

### AWS CLI
<a name="capacity-reservations.modifying.cli"></a>

Use the [modify-db-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-capacity-reservation.html) command.

```
1. aws rds modify-db-capacity-reservation \
2.     --db-capacity-reservation-identifier {{my-reservation}} \
3.     --capacity-per-availability-zone {{4}}
```

The new capacity applies to each Availability Zone in the reservation. Increasing it is subject to capacity being available in all of them. Decreasing it releases the difference and reduces charges.

### RDS API
<a name="capacity-reservations.modifying.api"></a>

To modify a Capacity Reservation by using the Amazon RDS API, call the [ModifyDBCapacityReservation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCapacityReservation.html) operation with the following parameter:
+ `DBCapacityReservationIdentifier` – The name or the `dbcr-` ID of the Capacity Reservation.

Also specify at least one of the following parameters:
+ `CapacityPerAvailabilityZone` – The new number of DB instances to reserve in each Availability Zone.
+ `EndDateType` – `limited` to set an end date, or `unlimited` to keep the reservation until you cancel it.
+ `EndDate` – The new end date, in UTC. Required when `EndDateType` is `limited`.