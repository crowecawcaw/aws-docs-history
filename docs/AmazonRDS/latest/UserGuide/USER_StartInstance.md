# Starting an Amazon RDS DB instance that was previously stopped

This topic explains how to start an Amazon RDS DB instance that was previously stopped, outlining the
necessary steps and key considerations for resuming use of the database.

You can stop your Amazon RDS DB instance temporarily to save money. After you stop your DB instance, you can
restart it to begin using it again. For more information about stopping a DB instance, see [Stopping an Amazon RDS DB instance temporarily](USER_StopInstance.md "USER_StopInstance.md").

When you start a DB instance that you previously stopped, the DB instance retains information such as the following:

- Instance ID
- Domain Name Server (DNS) endpoint
- DB parameter group
- VPC security group
- DB option group
  Amazon RDS bills in one-second increments for database instances and attached storage. There is a
  10-minute minimum charge when an instance is started.

To start the instance, the Amazon RDS service performs actions such as the following:

- Provisioning the underlying Amazon EC2 instance
- Starting the RDS processes
- Starting the database engine processes
- Attaching the EBS storage volumes
- Enabling Performance Insights if it was previously enabled
- Recovering the DB instance (recovery occurs even after a normal shutdown)
  The time to start your DB instance varies depending on factors such as the instance class,
  network state, DB engine type, database size, and the database state when the instance was shut
  down. The startup process can take minutes to hours. We recommend that you consider the
  variability in startup time when creating your availability plan.

###### To start a DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB
   instance that you want to start.
3. For **Actions**,
   choose **Start**.
   To start a DB instance by using the AWS CLI, call the
   [start-db-instance](../../../cli/latest/reference/rds/start-db-instance.md "../../../cli/latest/reference/rds/start-db-instance.md") command
   with the following option:

- `--db-instance-identifier` –
  The name of the DB instance.

###### Example

```
aws rds start-db-instance --db-instance-identifier `mydbinstance`
```

To start a DB instance by using the Amazon RDS API,
call the
[StartDBInstance](../APIReference/API_StartDBInstance.md "../APIReference/API_StartDBInstance.md") operation
with the following parameter:

- `DBInstanceIdentifier` –
  The name of the DB instance.
