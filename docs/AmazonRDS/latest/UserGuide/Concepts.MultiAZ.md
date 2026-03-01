# Converting a DB instance to a Multi-AZ deployment for Amazon RDS

Modifying a DB instance to a Multi-AZ deployment improves availability by adding a
standby instance in another Availability Zone. The process involves minimal downtime and
requires careful planning around storage and performance impacts. This change enhances
fault tolerance and reduces recovery time in case of failures, making it ideal for
high-availability environments.

If you have a DB instance in a Single-AZ deployment and modify it to a Multi-AZ DB instance
deployment, Amazon RDS performs the following actions:

1. Takes a snapshot of the primary DB instance's Amazon Elastic Block Store (EBS) volumes.
2. Creates new volumes for the standby replica from the snapshot. These volumes initialize in the background, and
   maximum volume performance is achieved after the data is fully initialized.
3. Turns on synchronous block-level replication between the volumes of the primary and standby replicas.

###### Important

Creating a standby DB instance from a snapshot during a Single-AZ to Multi-AZ
conversion avoids downtime but might impact performance, particularly for
write-sensitive workloads. The synchronous replication can increase I/O latency,
affecting database performance. As a best practice, avoid converting a production DB
instance to a Multi-AZ DB instance.

Instead, create a read replica, enable backups on it, convert it to Multi-AZ, load
data into its volumes, and then promote it to the primary DB instance. For more
information, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

There are two ways to modify a DB instance to be a Multi-AZ DB instance deployment:

###### Topics

- [Convert to a Multi-AZ DB instance deployment with the RDS console](#Concepts.MultiAZ.Migrating.Convert "#Concepts.MultiAZ.Migrating.Convert")
- [Modifying a DB instance to be a Multi-AZ DB instance deployment](#Concepts.MultiAZ.Migrating.Modify "#Concepts.MultiAZ.Migrating.Modify")

## Convert to a Multi-AZ DB instance deployment with the RDS console

You can use the RDS console to convert a DB instance to a Multi-AZ DB instance deployment.

You can only use the console to complete the conversion. To use the AWS CLI or RDS API, follow the
instructions in [Modifying a DB instance to be a Multi-AZ DB instance deployment](#Concepts.MultiAZ.Migrating.Modify "#Concepts.MultiAZ.Migrating.Modify").

###### To convert to a Multi-AZ DB instance deployment with the RDS console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB
   instance that you want to modify.
3. From **Actions**, choose **Convert to Multi-AZ deployment**.
4. On the confirmation page, choose **Apply immediately** to apply the changes immediately.
   Choosing this option doesn't cause downtime, but there is a possible performance impact. Alternatively,
   you can choose to apply the update during the next maintenance window. For more
   information, see [Using the schedule modifications setting](USER_ModifyInstance.md "USER_ModifyInstance.md").
5. Choose **Convert to Multi-AZ**.

## Modifying a DB instance to be a Multi-AZ DB instance deployment

You can modify a DB instance to be a Multi-AZ DB instance deployment in the following
ways:

- Using the RDS console, modify the DB instance, and set **Multi-AZ deployment**
  to **Yes**.
- Using the AWS CLI, call the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md")
  command, and set the `--multi-az` option.
- Using the RDS API, call the [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") operation, and set the `MultiAZ`
  parameter to `true`.

For information about modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md"). After the modification is complete, Amazon RDS triggers an event
(RDS-EVENT-0025) that indicates the process is complete. You can monitor Amazon RDS events. For more
information about events, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
