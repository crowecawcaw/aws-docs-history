

# Creating a Capacity Reservation
<a name="capacity-reservations.creating"></a>

When you create a Capacity Reservation, you specify a DB instance class, database engine, and one or more Availability Zones in a single AWS Region, along with the amount of capacity to reserve in each Availability Zone. You can create the reservation for immediate use, or schedule it to begin on a future date ahead of a planned event. After the reservation becomes active, you reference it by name or by identifier to place DB instances into the reserved capacity.

Creating a reservation without a start date makes it immediately active. Capacity is reserved and billing begins immediately.

## Console
<a name="capacity-reservations.creating.console"></a>

**To create a Capacity Reservation**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Capacity reservations**.

1. Choose **Create capacity reservation**.

1. Under **Engine options**, choose **Aurora (MySQL Compatible)** or **Aurora (PostgreSQL Compatible)**.  
![Engine types that you can choose for a Capacity Reservation, with Aurora (PostgreSQL Compatible) selected.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/odcr-create-engine-options-aurora.png)

1. Under **Instance configuration**, choose the DB instance configuration.  
![The db.r7g.large DB instance class selected.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/odcr-create-instance-config.png)

1. Under **Capacity reservation details**, do the following:
   + For **DB capacity reservation name**, enter a name for the reservation. The name must start with a lowercase letter and can contain lowercase letters, digits, and hyphens, up to 63 characters. It can't end with a hyphen or contain two consecutive hyphens.
   + Under **Availability Zones**, select one or more Availability Zones in the current Region. Select the Availability Zones where you plan to place the DB instances that use this reservation.
   + For **Reserved capacity per AZ**, enter the number of DB instances to reserve in each Availability Zone.
   + Under **Capacity reservation starts**, choose **Immediately**.
   + (Optional) Under **Capacity reservation ends**, choose **No end time** to keep the reservation until you cancel it, or **At a specific time** to set an end date.  
![Capacity Reservation details: my-reservation, us-east-1a, 2 per AZ, starts immediately, no end time.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/odcr-create-details.png)

1. (Optional) Add tags.

1. Choose **Create capacity reservation**.

The reservation appears in the list. When its state becomes `active`, capacity is reserved and you can launch DB instances into it by referencing the reservation by name or by identifier. Creating a reservation does not change the placement of DB instances that don't target it.

Billing for an immediately active reservation starts when you create it. To stop the charges, cancel the reservation when you no longer need it. For more information, see [Canceling a Capacity Reservation](capacity-reservations.canceling.md).

## AWS CLI
<a name="capacity-reservations.creating.cli"></a>

Create an immediately active reservation with the [create-db-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-capacity-reservation.html) command.

To reserve capacity in more than one Availability Zone with one reservation, list two or more Availability Zones. You can also create a separate reservation for each Availability Zone, and specify a different reservation for each DB instance in the DB cluster.

```
1. aws rds create-db-capacity-reservation \
2.     --db-capacity-reservation-name {{my-cluster-reservation}} \
3.     --engine {{aurora-postgresql}} \
4.     --db-instance-class {{db.r7g.large}} \
5.     --availability-zones {{us-east-1a}} {{us-east-1b}} \
6.     --capacity-per-availability-zone {{2}}
```

Example response:

```
 1. {
 2.     "DBCapacityReservation": {
 3.         "DBCapacityReservationName": "my-cluster-reservation",
 4.         "DBInstanceClass": "db.r7g.large",
 5.         "Engine": "aurora-postgresql",
 6.         "ReservedCapacityPerAvailabilityZone": 2,
 7.         "AvailableCapacityPerAvailabilityZoneList": [
 8.             {
 9.                 "AvailabilityZone": "us-east-1a",
10.                 "AvailableCapacity": 2
11.             },
12.             {
13.                 "AvailabilityZone": "us-east-1b",
14.                 "AvailableCapacity": 2
15.             }
16.         ],
17.         "CreateDate": "2026-09-21T21:44:50.147000+00:00",
18.         "State": "active",
19.         "DBCapacityReservationArn": "arn:aws:rds:us-east-1:123456789012:db-capacity-reservation:dbcr-abc123example",
20.         "DBCapacityReservationIdentifier": "dbcr-abc123example",
21.         "TagList": []
22.     }
23. }
```

## RDS API
<a name="capacity-reservations.creating.api"></a>

To create a Capacity Reservation by using the Amazon RDS API, call the [CreateDBCapacityReservation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCapacityReservation.html) operation with the following parameters:
+ `DBCapacityReservationName` – A name for the reservation. The name must start with a lowercase letter and can contain lowercase letters, digits, and hyphens, up to 63 characters. It can't end with a hyphen, contain two consecutive hyphens, or start with `dbcr-`.
+ `Engine` – The database engine to reserve capacity for: `aurora-mysql` or `aurora-postgresql`.
+ `DBInstanceClass` – The DB instance class to reserve capacity for, for example `db.r7g.large`.
+ `AvailabilityZones` – One or more Availability Zones in the current AWS Region.
+ `CapacityPerAvailabilityZone` – The number of DB instances to reserve in each Availability Zone.

You can also specify the following optional parameters:
+ `EndDate` – The date and time when the reservation expires, in UTC. If you don't specify it, the reservation doesn't expire.
+ `Tags` – Tags to assign to the Capacity Reservation.

## Creating a future-dated Capacity Reservation
<a name="capacity-reservations.future-dated"></a>

To schedule a reservation to begin on a future date, provide a start date and a commitment duration. Amazon RDS assesses the request, and if it can deliver the capacity, moves the reservation to the `scheduled` state. No charges apply until the start date, when Amazon RDS activates the reservation.

While assessing a request, Amazon RDS might determine that it can support a shorter commitment duration. In that case, Amazon RDS schedules the reservation with the shorter commitment duration, and you are committed to keeping the reservation for a shorter period than you requested. To see the commitment that applies, check `CommitmentInfo.CommitmentEndDate` in the output of `describe-db-capacity-reservations`.

### Console
<a name="capacity-reservations.future-dated.console"></a>

Follow the steps in [Creating a Capacity Reservation](#capacity-reservations.creating). Under **Capacity reservation starts**, do the following:

**To create a future-dated Capacity Reservation**

1. Choose **At a specific time**.

1. Set the **Start date** and **Start time** (must be at least 5 days in the future).

1. Set the **Commitment duration** (minimum 14 days). This is the period you commit to keep the reservation after it becomes active.  
![A future-dated reservation that starts at a specific time with a 14-day commitment.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/odcr-create-future-dated.png)

Complete the remaining steps and choose **Create capacity reservation**. The reservation is created in the `assessing` state and moves to `scheduled` after Amazon RDS accepts the request.

### AWS CLI
<a name="capacity-reservations.future-dated.cli"></a>

Add `--start-date` and `--commitment-duration` to the `create-db-capacity-reservation` command. `--commitment-duration` is specified in seconds (for example, `1209600` for 14 days).

```
1. aws rds create-db-capacity-reservation \
2.     --db-capacity-reservation-name {{peak-reservation}} \
3.     --engine {{aurora-postgresql}} \
4.     --db-instance-class {{db.r7g.large}} \
5.     --availability-zones {{us-east-1a}} \
6.     --capacity-per-availability-zone {{16}} \
7.     --start-date {{2026-11-01T00:00:00Z}} \
8.     --commitment-duration {{1209600}}
```

Example response:

```
 1. {
 2.     "DBCapacityReservation": {
 3.         "DBCapacityReservationName": "peak-reservation",
 4.         "DBInstanceClass": "db.r7g.large",
 5.         "Engine": "aurora-postgresql",
 6.         "ReservedCapacityPerAvailabilityZone": 16,
 7.         "StartDate": "2026-11-01T00:00:00Z",
 8.         "CommitmentInfo": {
 9.             "CommittedCapacityPerAvailabilityZone": 16,
10.             "CommitmentEndDate": "2026-11-15T00:00:00Z"
11.         },
12.         "CreateDate": "2026-09-21T21:44:50.147000+00:00",
13.         "State": "assessing",
14.         "DBCapacityReservationArn": "arn:aws:rds:us-east-1:123456789012:db-capacity-reservation:dbcr-def456example",
15.         "DBCapacityReservationIdentifier": "dbcr-def456example",
16.         "TagList": []
17.     }
18. }
```

**Note**  
Omitting `--start-date` and `--commitment-duration` creates an immediately active reservation. The two future-dated parameters are used together.

### RDS API
<a name="capacity-reservations.future-dated.api"></a>

To create a future-dated Capacity Reservation by using the Amazon RDS API, call the [CreateDBCapacityReservation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCapacityReservation.html) operation with the parameters for an immediately active reservation, and with the following parameters:
+ `StartDate` – The date and time when the reservation starts, in UTC. It must be 5–120 days in the future.
+ `CommitmentDuration` – The length of the commitment, in seconds. The minimum is `1209600` (14 days). For the X family, the minimum is `7257600` (12 weeks).