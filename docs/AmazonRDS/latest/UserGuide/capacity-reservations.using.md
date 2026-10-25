

# Using a Capacity Reservation with a DB instance
<a name="capacity-reservations.using"></a>

Reserved capacity is used only when you explicitly target the reservation. You reference the reservation by its identifier (`dbcr-`) or its name when you perform any of the following operations:
+ Create a DB instance (`CreateDBInstance`)
+ Create a read replica (`CreateDBInstanceReadReplica`)
+ Restore a DB instance from a snapshot or to a point in time (`RestoreDBInstance*`)
+ Modify a DB instance to move it into a reservation (`ModifyDBInstance`)
+ Start a stopped DB instance (`StartDBInstance`)

The DB instance's engine, DB instance class, license model (for engines that offer more than one), and Availability Zone must match the reservation, and the reservation must have available capacity in that Availability Zone (the matching entry in `AvailableCapacityPerAvailabilityZoneList` has an `AvailableCapacity` greater than 0). If they don't match or no capacity is available, the operation fails with an error that says the Availability Zone doesn't have enough capacity. For a Multi-AZ DB instance, both the primary and the standby Availability Zones must have available capacity.

## Console
<a name="capacity-reservations.using.console"></a>

When you create or restore a DB instance in the Amazon RDS console, in the **Capacity reservation** section, choose the reservation to launch into.

## AWS CLI
<a name="capacity-reservations.using.cli"></a>

Add the `--db-capacity-reservation-identifier` parameter to the create, restore, or modify command. For example, to create a DB instance that uses a reservation:

```
1. aws rds create-db-instance \
2.     --db-instance-identifier {{my-db-instance}} \
3.     --engine {{postgres}} \
4.     --db-instance-class {{db.r7g.large}} \
5.     --availability-zone {{us-east-1a}} \
6.     --allocated-storage {{100}} \
7.     --master-username {{admin}} \
8.     --manage-master-user-password \
9.     --db-capacity-reservation-identifier {{my-reservation}}
```

The `--db-capacity-reservation-identifier` parameter accepts either the reservation name or its `dbcr-` ID.

To restore into a reservation, add the same parameter to the restore command. A snapshot restore takes the engine from the snapshot, but you can override the DB instance class, Availability Zone, and license model – whatever the restored DB instance ends up with must match the reservation.

```
1. aws rds restore-db-instance-from-db-snapshot \
2.     --db-instance-identifier {{my-restored-instance}} \
3.     --db-snapshot-identifier {{my-snapshot}} \
4.     --db-instance-class {{db.r7g.large}} \
5.     --availability-zone {{us-east-1a}} \
6.     --db-capacity-reservation-identifier {{my-reservation}}
```

Point-in-time restores take the same parameter:

```
1. aws rds restore-db-instance-to-point-in-time \
2.     --source-db-instance-identifier {{my-source-instance}} \
3.     --target-db-instance-identifier {{my-restored-instance}} \
4.     --use-latest-restorable-time \
5.     --db-instance-class {{db.r7g.large}} \
6.     --availability-zone {{us-east-1a}} \
7.     --db-capacity-reservation-identifier {{my-reservation}}
```

The `restore-db-instance-from-s3` command accepts the parameter as well.

To move an existing DB instance into a reservation, specify the reservation in a modify request that also changes the DB instance class, the Multi-AZ setting, or the license model, or that converts an RDS for Oracle DB instance from the non-CDB architecture to the CDB architecture. For a CDB conversion, the reservation engine must be `oracle-ee-cdb` or `oracle-se2-cdb`. The reservation must match the configuration that the DB instance has after the change. For example, to scale a DB instance to db.r7g.large and place it in a db.r7g.large reservation:

```
1. aws rds modify-db-instance \
2.     --db-instance-identifier {{my-db-instance}} \
3.     --db-instance-class {{db.r7g.large}} \
4.     --db-capacity-reservation-identifier {{my-reservation}} \
5.     --apply-immediately
```

A modify request that specifies a reservation without one of these changes fails. To move a DB instance into a reservation without changing its configuration, stop the DB instance, and then start it with the reservation. For more information, see [Stopping and starting a DB instance in a reservation](capacity-reservations.stopstart.md).

When DB instances are placed into the reservation, the `AvailableCapacity` for the affected Availability Zone decreases. You can track this with `describe-db-capacity-reservations`.

## RDS API
<a name="capacity-reservations.using.api"></a>

Specify the `DBCapacityReservationIdentifier` parameter in the [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html), [CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html), [RestoreDBInstanceFromDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html), [RestoreDBInstanceToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.html), [RestoreDBInstanceFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromS3.html), [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html), or [StartDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StartDBInstance.html) operation.