

# Using a Capacity Reservation with an Aurora DB instance
<a name="capacity-reservations.using"></a>

Reserved capacity is used only when you explicitly target the reservation. You reference the reservation by its identifier (`dbcr-`) or its name when you perform any of the following operations:
+ Create a DB instance in a DB cluster (`CreateDBInstance`) – for the writer and for each Aurora Replica
+ Modify a DB instance to move it into a reservation (`ModifyDBInstance`)

The DB instance's engine, DB instance class, and Availability Zone must match the reservation, and the reservation must have available capacity in that Availability Zone (the matching entry in `AvailableCapacityPerAvailabilityZoneList` has an `AvailableCapacity` greater than 0). If they don't match or no capacity is available, the operation fails with an error that says the Availability Zone doesn't have enough capacity.

## Console
<a name="capacity-reservations.using.console"></a>

When you add a DB instance to an Aurora DB cluster in the Amazon RDS console, in the **Capacity reservation** section, choose the reservation to launch into.

## AWS CLI
<a name="capacity-reservations.using.cli"></a>

Add the `--db-capacity-reservation-identifier` parameter to the create or modify command. For example, to create a DB instance that uses a reservation:

```
1. aws rds create-db-instance \
2.     --db-instance-identifier {{my-db-instance}} \
3.     --db-cluster-identifier {{my-aurora-cluster}} \
4.     --engine {{aurora-postgresql}} \
5.     --db-instance-class {{db.r7g.large}} \
6.     --availability-zone {{us-east-1a}} \
7.     --db-capacity-reservation-identifier {{my-reservation}}
```

The `--db-capacity-reservation-identifier` parameter accepts either the reservation name or its `dbcr-` ID.

To restore into a reservation, restore the DB cluster first, and then add its DB instances with the reservation. A DB cluster restore (`restore-db-cluster-from-snapshot` or `restore-db-cluster-to-point-in-time`) creates the DB cluster without DB instances and doesn't take a Capacity Reservation.

```
 1. aws rds restore-db-cluster-from-snapshot \
 2.     --db-cluster-identifier {{my-restored-cluster}} \
 3.     --snapshot-identifier {{my-cluster-snapshot}} \
 4.     --engine {{aurora-postgresql}}
 5. 
 6. aws rds create-db-instance \
 7.     --db-instance-identifier {{my-restored-instance}} \
 8.     --db-cluster-identifier {{my-restored-cluster}} \
 9.     --engine {{aurora-postgresql}} \
10.     --db-instance-class {{db.r7g.large}} \
11.     --db-capacity-reservation-identifier {{my-reservation}}
```

To move an existing DB instance into a reservation, specify the reservation in a modify request that also changes the DB instance class. The reservation must match the configuration that the DB instance has after the change. For example, to scale a DB instance to db.r7g.large and place it in a db.r7g.large reservation:

```
1. aws rds modify-db-instance \
2.     --db-instance-identifier {{my-db-instance}} \
3.     --db-instance-class {{db.r7g.large}} \
4.     --db-capacity-reservation-identifier {{my-reservation}} \
5.     --apply-immediately
```

A modify request that specifies a reservation without a DB instance class change fails.

When DB instances are placed into the reservation, the `AvailableCapacity` for the affected Availability Zone decreases. You can track this with `describe-db-capacity-reservations`.

## RDS API
<a name="capacity-reservations.using.api"></a>

Specify the `DBCapacityReservationIdentifier` parameter in the [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) or [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation.