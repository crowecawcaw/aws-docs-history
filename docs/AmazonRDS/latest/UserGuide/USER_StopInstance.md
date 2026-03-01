# Stopping an Amazon RDS DB instance temporarily

You can stop your DB instance intermittently for temporary testing or for a daily development
activity, for a maximum of 7 consecutive days. The most common use case is cost
optimization. The time to stop your DB instance depends on a number of factors. For more
information, see [Use cases](#USER_StopInstance.Benefits "#USER_StopInstance.Benefits") and [Time considerations](#USER_StopInstance.Time "#USER_StopInstance.Time").

###### Warning

Starting a DB instance requires instance recovery and can take from minutes to hours. Therefore,
if instance availability is a concern, be cautious about stopping a production instance
temporarily. For more information, see [Starting an Amazon RDS DB instance that was previously stopped](USER_StartInstance.md "USER_StartInstance.md").

To stop and start your DB instance in the same operation, reboot the DB instance. For more
information, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").

###### Topics

- [Use cases for stopping your DB instance](#USER_StopInstance.Benefits "#USER_StopInstance.Benefits")
- [Time considerations when stopping your DB instance](#USER_StopInstance.Time "#USER_StopInstance.Time")
- [Supported DB engines, instance classes, and Regions](#USER_StopInstance.Supported "#USER_StopInstance.Supported")
- [Stopping a DB instance in a Multi-AZ deployment](#USER_StopInstance.MAZ "#USER_StopInstance.MAZ")
- [How stopping a DB instance works](#USER_StopInstance.Operation "#USER_StopInstance.Operation")
- [Limitations of stopping your DB instance](#USER_StopInstance.Limitations "#USER_StopInstance.Limitations")
- [Option and parameter group considerations](#USER_StopInstance.OGPG "#USER_StopInstance.OGPG")
- [Public IP address considerations](#USER_StopInstance.PublicIPAddress "#USER_StopInstance.PublicIPAddress")
- [Stopping a DB instance temporarily: basic steps](#USER_StopInstance.Stopping "#USER_StopInstance.Stopping")

## Use cases for stopping your DB instance

Stopping and starting a DB instance is faster and more efficient than creating a DB snapshot, deleting
your DB instance, and then restoring the snapshot when you want to access the instance.
Common use cases for stopping an instance include the following:

- **Cost optimization** – For non-production databases,
  you can stop your Amazon RDS DB instance temporarily to save money. While the instance is
  stopped, you're not charged for DB instance hours.

###### Important

While your DB instance is stopped, you are charged for provisioned storage
(including Provisioned IOPS). You're also charged for backup storage,
including manual snapshots and automated backups within your specified
retention window. However, you're not charged for DB instance hours. For
more information, see [Billing FAQs](http://aws.amazon.com/rds/faqs/#billing "http://aws.amazon.com/rds/faqs/#billing").

- **Daily development** – If you maintain a DB instance for
  development purposes, you can start the instance when it's needed and then shut
  down the instance when it's not needed.
- **Testing** – You might need a temporary DB instance to test
  backup and recovery procedures, migrations, application upgrades, or related
  activities. In these use cases, you can stop the DB instance when it's not
  needed.
- **Training** – If you're conducting training in RDS,
  you might need to start DB instances during the training session and shut them down
  afterward.

## Time considerations when stopping your DB instance

The time to stop your DB instance varies depending on factors such as the instance class,
network state, DB engine type, database state, and workload. The process can take several
minutes or even up to an hour. Even if you don't choose to take a final snapshot, the
service must perform internal operations to ensure data consistency. These operations
might extend the stop time. They can't be skipped. The DB instance status remains in a
stopping state until all operations are complete. These operations include the following
actions:

- Shut down database engine processes.
- Shut down RDS platform processes.
- Detach the EBS storage volumes associated with your DB instance.
- Terminate the underlying Amazon EC2 instance.

To minimize delays, consider taking the following actions:

- Take a manual backup.
- Stop the DB instance during periods of low activity.
- Maintain recent automated backups.

## Supported DB engines, instance classes, and Regions

You can stop and start Amazon RDS DB instances that are running the following DB engines:

- Db2
- MariaDB
- Microsoft SQL Server, including RDS Custom for SQL Server
- MySQL
- Oracle
- PostgreSQL

Stopping and starting a DB instance is supported for all DB instance classes, and in all AWS
Regions.

## Stopping a DB instance in a Multi-AZ deployment

You can stop and start a DB instance in a Multi-AZ deployment. Note the following limitations:

- You can only create a Multi-AZ deployment if your database engine supports it. For more
  information about engine support, see [Supported Regions and DB engines for Multi-AZ DB clusters in Amazon RDS](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").
- RDS for SQL Server doesn't support stopping a DB instance in a Multi-AZ deployment. For more information,
  see [Microsoft SQL Server Multi-AZ deployment limitations, notes, and recommendations](USER_SQLServerMultiAZ.md "USER_SQLServerMultiAZ.md").
- A long time might be required to stop a DB instance.

## How stopping a DB instance works

The stopping operation occurs in the following stages:

1. The DB instance initiates the normal shutdown process.

The status of the DB instance changes to `stopping`. 2. The instance stops running, up to a maximum of 7 consecutive days.

The status of the DB instance changes to `stopped`.

### Characteristics of a stopped DB instance

When in a stopped state, your DB instance has the following characteristics:

- Your stopped DB instance retains the following:

      + Instance ID
      + Domain Name Server (DNS) endpoint
      + Parameter group
      + Security group
      + Option group
      + Amazon S3 transaction logs (necessary for a point-in-time
       restore)

  When you restart a DB instance, it has the same configuration as when you
  stopped it.

- Any storage volumes remain attached to the DB instance, and their data is kept.
  RDS deletes any data stored in the RAM of the DB instance.

While your DB instance is stopped, you are charged for provisioned storage
(including Provisioned IOPS). You're also charged for backup storage,
including manual snapshots and automated backups within your specified
retention window.

- RDS removes pending actions, including scheduled maintenance updates, except for pending
  actions for the option group or DB parameter group of the DB instance.

###### Note

Occasionally, an RDS for PostgreSQL DB instance doesn't shut down cleanly. If this
happens, you see that the instance goes through a recovery process when you
restart it later. This is expected behavior of the database engine, intended to
protect database integrity. Some memory-based statistics and counters don't
retain history and are re-initialized after restart, to capture the operational
workload moving forward.

### Automatic restart of a stopped DB instance

If you don't manually start your DB instance after it is stopped for seven
consecutive days, RDS automatically starts your DB instance for you. This way, your
instance doesn't fall behind any required maintenance updates. To learn how to
stop and start your instance on a schedule, see [How
can I use Step Functions to stop an Amazon RDS instance for longer than 7
days?](https://repost.aws/knowledge-center/rds-stop-seven-days-step-functions "https://repost.aws/knowledge-center/rds-stop-seven-days-step-functions").

## Limitations of stopping your DB instance

The following are some limitations of the stopping operation:

- You can't stop a DB instance that has a read replica, or that is a read replica.
- You can't modify a stopped DB instance.
- You can't delete an option group that is associated with a stopped DB instance.
- You can't delete a DB parameter group that is associated with a stopped DB instance.
- In a Multi-AZ deployment, note the following limitations:
  - You can't stop an RDS for SQL Server DB instance.
  - The primary and secondary Availability Zones might be switched after
    you start the DB instance.

Additional limitations apply to RDS Custom for SQL Server. For more information, see [Starting and stopping an RDS Custom for SQL Server DB instance](custom-managing-sqlserver.md "custom-managing-sqlserver.md").

## Option and parameter group considerations

You can't remove persistent options (including permanent options) from an
option group if there are DB instances associated with that option group.
This functionality is also true of
any DB instance with a state of `stopping`,
`stopped`, or `starting`.

You can change the option group or DB parameter group that is associated with a stopped DB
instance. However, the change doesn't occur until the next time you start the DB
instance. If you chose to apply changes immediately, the change occurs when you start
the DB instance. Otherwise the change occurs during the next maintenance window after
you start the DB instance.

## Public IP address considerations

When you stop a DB instance, it retains its DNS endpoint. If you stop a DB instance that
has a public IP address, Amazon RDS releases its public IP address. When the DB instance is restarted,
it has a different public IP address.

###### Note

You should always connect to a DB instance using the DNS endpoint, not the IP address.

## Stopping a DB instance temporarily: basic steps

You can stop a DB using the AWS Management Console, the AWS CLI, or the RDS API.

###### To stop a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB
   instance that you want to stop.
3. For **Actions**,
   choose **Stop temporarily**.
4. In the **Stop DB instance temporarily** window, select the
   acknowledgement that the DB instance will restart automatically after 7 days.
5. (Optional) Select **Save the DB instance in a snapshot** and enter
   the snapshot name for **Snapshot name**. Choose
   this option if you want to create a snapshot of the DB instance
   before stopping it.
6. Choose **Stop temporarily** to stop the DB instance,
   or choose **Cancel** to cancel the operation.
   To stop a DB instance by using the AWS CLI, call the
   [stop-db-instance](../../../cli/latest/reference/rds/stop-db-instance.md "../../../cli/latest/reference/rds/stop-db-instance.md") command
   with the following option:

- `--db-instance-identifier` –
  the name of the DB instance.

###### Example

```
aws rds stop-db-instance --db-instance-identifier `mydbinstance`
```

To stop a DB instance by using the Amazon RDS API,
call the
[StopDBInstance](../APIReference/API_StopDBInstance.md "../APIReference/API_StopDBInstance.md") operation
with the following parameter:

- `DBInstanceIdentifier` –
  the name of the DB instance.
