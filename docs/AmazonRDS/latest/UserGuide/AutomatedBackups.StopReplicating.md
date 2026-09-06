

# Stopping automated backup replication for Amazon RDS
<a name="AutomatedBackups.StopReplicating"></a>

You can stop backup replication for DB instances using the Amazon RDS console. You can also use the `stop-db-instance-automated-backups-replication` AWS CLI command or the `StopDBInstanceAutomatedBackupsReplication` RDS API operation.

Replicated backups are retained, subject to the backup retention period set when they were created.

## Console
<a name="AutomatedBackups.StopReplicating.Console"></a>

Stop backup replication from the **Automated backups** page in the source Region.

**To stop backup replication to an AWS Region**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose the source Region from the **Region selector**.

1. In the navigation pane, choose **Automated backups**.

1. On the **Current Region** tab, choose the DB instance for which you want to stop backup replication.

1. For **Actions**, choose **Manage cross-Region replication**.

1. Under **Backup replication**, clear the **Enable replication to another AWS Region** check box.

1. Choose **Save**.

Replicated backups are listed on the **Retained** tab of the **Automated backups** page in the destination Region.

## AWS CLI
<a name="AutomatedBackups.StopReplicating.CLI"></a>

Stop backup replication by using the [`stop-db-instance-automated-backups-replication`](https://docs.aws.amazon.com/cli/latest/reference/rds/stop-db-instance-automated-backups-replication.html) AWS CLI command.

The following CLI example stops automated backups of a DB instance from replicating in the US West (Oregon) Region.

**To stop backup replication**
+ Run one of the following commands.

  For Linux, macOS, or Unix:

  ```
  aws rds stop-db-instance-automated-backups-replication \
  --region us-east-1 \
  --source-db-instance-arn "arn:aws:rds:us-west-2:{{123456789012}}:db:{{mydatabase}}"
  ```

  For Windows:

  ```
  aws rds stop-db-instance-automated-backups-replication ^
  --region us-east-1 ^
  --source-db-instance-arn "arn:aws:rds:us-west-2:{{123456789012}}:db:{{mydatabase}}"
  ```

## RDS API
<a name="AutomatedBackups.StopReplicating.API"></a>

Stop backup replication by using the [`StopDBInstanceAutomatedBackupsReplication`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_StopDBInstanceAutomatedBackupsReplication.html) RDS API operation with the following parameters:
+ `Region`
+ `SourceDBInstanceArn`