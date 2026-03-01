# Rebooting a DB instance

You can stop and start the database service on your RDS DB instance in a single operation,
called _rebooting_. Rebooting might be necessary to apply configuration
changes, address minor issues, or resolve network problems without having to perform a full
restart or migration of your database.

###### Note

This topic applies only to rebooting a Single-AZ or Multi-AZ DB
_instance_. For instructions to reboot a Multi-AZ DB cluster, see [Rebooting a Multi-AZ DB cluster and reader DB instances for Amazon RDS](multi-az-db-clusters-concepts-rebooting.md "multi-az-db-clusters-concepts-rebooting.md").

###### Topics

- [Use cases for rebooting a DB instance](#USER_RebootInstance.use-cases "#USER_RebootInstance.use-cases")
- [How rebooting a DB instance works](#USER_RebootInstance.how-it-works "#USER_RebootInstance.how-it-works")
- [How rebooting a DB instance in a Multi-AZ deployment works](#USER_RebootInstance.MAZ "#USER_RebootInstance.MAZ")
- [Considerations when rebooting a DB instance](#USER_RebootInstance.considerations "#USER_RebootInstance.considerations")
- [Prerequisites for rebooting a DB instance](#USER_RebootInstance.prereqs "#USER_RebootInstance.prereqs")
- [Rebooting a DB instance: basic steps](#USER_RebootInstance.steps "#USER_RebootInstance.steps")

## Use cases for rebooting a DB instance

Typically, you reboot your DB instance for maintenance reasons so that your changes take
effect. The following use cases are common:

- **Associating a new DB parameter group** – When you associate a new
  DB parameter group with a DB instance, RDS applies the modified static and dynamic parameters only
  after the DB instance is rebooted. However, if you modify dynamic parameters in the
  DB parameter group after you have associated it with the DB instance, these changes are applied
  immediately without a reboot. For more information, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
- **Applying a change to a static parameter in an existing
  DB parameter group** – When you change a static parameter and save the
  DB parameter group, the status of DB instances associated with this parameter group in the console
  changes to **pending-reboot**. The parameter change takes
  effect only after the associated DB instances are rebooted. When you change a dynamic
  parameter in an existing parameter group, the change takes effect immediately by
  default, without requiring a reboot.

###### Note

The **pending-reboot** status doesn't result in an
automatic reboot during the next maintenance window. To apply the latest
parameter changes to your DB instance, reboot the DB instance manually. For more
information about parameter groups, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

- **Troubleshooting** – You might encounter performance
  or other operational issues that necessitate a reboot. For example, your DB instance
  might be unresponsive.

## How rebooting a DB instance works

When Amazon RDS reboots your DB instance it performs the following sequential tasks:

1. Stops the database service on your DB instance
2. Starts the database service on your DB instance

The reboot process leads to a brief outage. During this outage, the DB instance status is
_rebooting_. An outage occurs for
both a Single-AZ deployment and a Multi-AZ DB instance deployment, even when you reboot
with a failover.

## How rebooting a DB instance in a Multi-AZ deployment works

If the Amazon RDS DB instance is in a Multi-AZ deployment, you can reboot with a
failover. This operation is useful to simulate a failure of a DB instance or restore
operations to the original Availability Zone after a failover.

During the reboot with failover, Amazon RDS does the following

- Interrupts the database abruptly. The DB instance and its client sessions might not
  have time to shut down gracefully.

###### Warning

To avoid the possibility of data loss, we recommend stopping transactions
on your DB instance before rebooting with a failover.

- Performs crash recovery of the database if necessary.
- Switches to a standby replica in another AZ automatically. The AZ change might
  not be reflected in the AWS Management Console, and in calls to the AWS CLI and RDS API, for
  several minutes.
- Updates the DNS record for the DB instance to point to the standby DB instance. As a
  result, you need to clean up and re-establish any existing connections to your
  DB instance. For more information, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.md "Concepts.md").
- Creates an Amazon RDS event after the reboot.

On RDS for Microsoft SQL Server, the failover reboots only the primary DB instance. After the failover, the
primary DB instance becomes the new secondary DB instance. Parameters might not be updated for
Multi-AZ instances. For reboot without failover, both the primary and secondary DB instances
reboot, and parameters are updated after the reboot. If the DB instance is unresponsive, we
recommend reboot without failover.

## Considerations when rebooting a DB instance

Before you reboot your instance, consider the following:

- For a DB instance with read replicas, you can reboot the source DB instance and its read
  replicas independently. After a reboot completes, replication resumes
  automatically.
- The reboot time depends on the crash recovery process, database activity at
  the time of reboot, and the behavior of your specific DB engine. To improve the
  reboot time, we recommend that you reduce database activity as much as possible
  during the reboot. This technique reduces rollback activity for in-transit
  transactions.

## Prerequisites for rebooting a DB instance

Make sure that you meet the following prerequisites:

- Your DB instance must be in the `available` state. Your database can be
  unavailable for several reasons, such as an in-progress backup, a previously
  requested modification, or a maintenance window operation.
- If you force a failover to a different AZ, your DB instance must be configured for
  Multi-AZ.
- If you force a failover to a different AZ, we recommend first stopping
  transactions on your DB instance to prevent possible data loss.

## Rebooting a DB instance: basic steps

You can reboot your DB instance using the AWS Management Console, AWS CLI, or RDS API.

###### To reboot a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and
   then choose the DB instance that you want to reboot.
3. For **Actions**, choose **Reboot**.

The **Reboot DB instance** page appears. 4. (Optional) Choose **Reboot with failover?** to force
a failover from one AZ to another. 5. Choose **Reboot** to reboot your DB instance.

Alternatively, choose **Cancel**.
To reboot a DB instance by using the AWS CLI, call the [`reboot-db-instance`](../../../cli/latest/reference/rds/reboot-db-instance.md "../../../cli/latest/reference/rds/reboot-db-instance.md") command.

###### Example Simple reboot

For Linux, macOS, or Unix:

```
aws rds reboot-db-instance \
    --db-instance-identifier `mydbinstance`
```

For Windows:

```
aws rds reboot-db-instance ^
    --db-instance-identifier `mydbinstance`
```

###### Example Reboot with failover

To force a failover from one AZ to the other in a Multi-AZ DB cluster, use the
`--force-failover` parameter.

For Linux, macOS, or Unix:

```
aws rds reboot-db-instance \
    --db-instance-identifier `mydbinstance` \
    --force-failover
```

For Windows:

```
aws rds reboot-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --force-failover
```

To reboot a DB instance by using the Amazon RDS API, call the [`RebootDBInstance`](../APIReference/API_RebootDBInstance.md "../APIReference/API_RebootDBInstance.md") operation.
