# Requirements for the Oracle Data Guard

switchover

Before initiating the Oracle Data Guard switchover, make sure that your replication environment meets the following
requirements:

- The original standby database is mounted or open read-only.
- Automatic backups are enabled on the original standby database.
- The original primary database and the original standby database are in the
  `available` state.
- The original primary database and the original standby database don't have pending
  maintenance actions in any of the following states: `required`,
  `next window`, or `in progress`. Actions in these states
  block switchover. To learn how to check the status of pending maintenance updates,
  see [Viewing pending maintenance
  updates](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Maintenance.Viewing "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Maintenance.Viewing").

Pending maintenance actions in the `available` state don't block
switchover. RDS for Oracle frequently releases operating system (OS) updates in the
`available` state. These pending OS updates won't block a switchover
unless you schedule them for the next maintenance window, which puts them in the
`next window` state.

###### Note

If you want to defer a scheduled maintenance action so that you can execute a
switchover, choose **Actions** and then **Defer
upgrade** in the RDS console. You can also prevent a switchover
from being blocked by applying a pending maintenance action or moving the
maintenance window to an interval before your switchover. For more information,
see the re:Post article [How to remove RDS pending maintenance items](https://repost.aws/questions/QUV3dBjmVVRnmVV1pAlzjx1w/how-to-remove-rds-pending-maintenance-item "https://repost.aws/questions/QUV3dBjmVVRnmVV1pAlzjx1w/how-to-remove-rds-pending-maintenance-item").

- The original standby database is in the replicating state.
- You aren't attempting to initiate a switchover when either the primary database or standby database is
  currently in a switchover lifecycle. If a replica database is reconfiguring after a switchover, Amazon RDS
  prevents you from initiating another switchover.

###### Note

A _bystander replica_ is a replica in the Oracle Data Guard configuration that isn't the target of the
switchover. Bystander replicas can be in any state during the switchover.

- The original standby database has a configuration that is as close as desired to the original primary
  database. Assume a scenario where the original primary and original standby databases have different options.
  After the switchover completes, Amazon RDS doesn't automatically reconfigure the new primary database to have the
  same options as the original primary database.
- You configure your desired Multi-AZ deployment before initiating a switchover. Amazon RDS doesn't
  manage Multi-AZ as part of the switchover. The Multi-AZ deployment remains as it is.

Assume that db_maz is the primary database in a Multi-AZ deployment, and db_saz is a
Single-AZ replica. You initiate a switchover from db_maz to db_saz. Afterward,
db_maz is a Multi-AZ replica database, and db_saz is a Single-AZ primary database.
The new primary database is now unprotected by a Multi-AZ deployment.

- In preparation for a cross-Region switchover, the primary database doesn't use the same option group as a DB instance outside of the
  replication configuration. For a cross-Region switchover to succeed, the current primary database
  and its read replicas must be the only DB instances to use the option group of the
  current primary database. Otherwise, Amazon RDS prevents the switchover.
