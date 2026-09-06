

# Amazon RDS event categories and event messages for Aurora
<a name="USER_Events.Messages"></a>

Amazon RDS generates a significant number of events in categories that you can subscribe to using the Amazon RDS Console, AWS CLI, or the API.

**Topics**
+ [DB cluster events](#USER_Events.Messages.cluster)
+ [DB cluster snapshot events](#USER_Events.Messages.cluster-snapshot)
+ [DB instance events](#USER_Events.Messages.instance)
+ [DB parameter group events](#USER_Events.Messages.parameter-group)
+ [DB security group events](#USER_Events.Messages.security-group)
+ [DB shard group events](#USER_Events.Messages.shard-group)
+ [RDS Proxy events](#USER_Events.Messages.rds-proxy)
+ [Blue/green deployment events](#USER_Events.Messages.BlueGreenDeployments)

## DB cluster events
<a name="USER_Events.Messages.cluster"></a>

The following table shows the event category and a list of events when a DB cluster is the source type.

**Note**  
No event category exists for Aurora Serverless in the DB cluster event type. The Aurora Serverless events range from RDS-EVENT-0141 to RDS-EVENT-0149.


|  Category  | RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| configuration change | RDS-EVENT-0016 | Reset master credentials. | None | 
| configuration change | RDS-EVENT-0179 | Database Activity Streams is started on your database cluster. | For more information see [Monitoring Amazon Aurora with Database Activity Streams](DBActivityStreams.md). | 
| configuration change | RDS-EVENT-0180 | Database Activity Streams is stopped on your database cluster. | For more information see [Monitoring Amazon Aurora with Database Activity Streams](DBActivityStreams.md). | 
| creation | RDS-EVENT-0170 | DB cluster created. | None | 
| deletion | RDS-EVENT-0171 | DB cluster deleted. | None | 
| failover | RDS-EVENT-0069 | Cluster failover failed, check the health of your cluster instances and try again. | None | 
| failover | RDS-EVENT-0070 | Promoting previous primary again: {{name}}. | None | 
| failover | RDS-EVENT-0071 | Completed failover to DB instance: {{name}}. | None | 
| failover | RDS-EVENT-0072 | Started same AZ failover to DB instance: {{name}}. | None | 
| failover | RDS-EVENT-0073 | Started cross AZ failover to DB instance: {{name}}. | None | 
| failure | RDS-EVENT-0083 | Amazon RDS has been unable to create credentials to access your Amazon S3 Bucket for your DB cluster {{name}}. This is due to the S3 snapshot ingestion IAM role not being configured correctly in your account or the specified Amazon S3 bucket cannot be found. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | For more information, see [Physical migration from MySQL by using Percona XtraBackup and Amazon S3](AuroraMySQL.Migrating.ExtMySQL.S3.md) .  | 
| failure | RDS-EVENT-0143 | The DB cluster failed to scale from {{units}} to {{units}} for this reason: {{reason}}. | Scaling failed for the Aurora Serverless DB cluster. | 
| failure | RDS-EVENT-0354 | You can't create the DB cluster because of incompatible resources. {{message}}. | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0355 | The DB cluster can't be created because of insufficient resource limits. {{message}}. | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0387 | Failed to partition DB instances in DB cluster {{name}} for patching. | The operating system upgrades for the DB instances in the DB cluster failed. | 
| failure | RDS-EVENT-0517 | The {{upgrade\_type}} version upgrade for DB cluster {{name}} was canceled because a failover occurred on the associated global database. The DB cluster is now running engine version {{version}}. Retry the upgrade when the global database is available. | Retry the upgrade when the global database is available. | 
| global failover | RDS-EVENT-0181 | Global switchover to DB cluster {{name}} in Region {{name}} started. | This event is for a switchover operation (previously called "managed planned failover").<br />The process can be delayed because other operations are running on the DB cluster. | 
| global failover | RDS-EVENT-0182 | Old primary DB cluster {{name}} in Region {{name}} successfully shut down. | This event is for a switchover operation (previously called "managed planned failover").<br />The old primary instance in the global database isn't accepting writes. All volumes are synchronized. | 
| global failover | RDS-EVENT-0183 | Waiting for data synchronization across global cluster members. Current lags behind primary DB cluster: `{{reason}}`. | This event is for a switchover operation (previously called "managed planned failover").<br />A replication lag is occurring during the synchronization phase of the global database failover. | 
| global failover | RDS-EVENT-0184 | New primary DB cluster {{name}} in Region {{name}} was successfully promoted. | This event is for a switchover operation (previously called "managed planned failover").<br />The volume topology of the global database is reestablished with the new primary volume. | 
| global failover | RDS-EVENT-0185 | Global switchover to DB cluster {{name}} in Region {{name}} finished. | This event is for a switchover operation (previously called "managed planned failover").<br />The global database switchover is finished on the primary DB cluster. Replicas might take long to come online after the failover completes. | 
| global failover | RDS-EVENT-0186 | Global switchover to DB cluster {{name}} in Region {{name}} is cancelled. | This event is for a switchover operation (previously called "managed planned failover"). | 
| global failover | RDS-EVENT-0187 | Global switchover to DB cluster {{name}} in Region {{name}} failed. | This event is for a switchover operation (previously called "managed planned failover"). | 
| global failover | RDS-EVENT-0238 | Global failover to DB cluster {{name}} in Region {{name}} completed. | None | 
| global failover | RDS-EVENT-0239 | Global failover to DB cluster {{name}} in Region {{name}} failed. | None | 
| global failover | RDS-EVENT-0240 | Started resynchronizing members of DB cluster {{name}} in Region {{name}} after global failover. | None | 
| global failover | RDS-EVENT-0241 | Finished resynchronizing members of DB cluster {{name}} in Region {{name}} after global failover. | None | 
| global failover | RDS-EVENT-0397 | Aurora finished changing the DNS name that the global writer endpoint resolves to. | None | 
| global failover | RDS-EVENT-0519 | Global database failover to DB cluster {{name}} in global database {{name}} completed. The DB cluster has no instances. Create a DB instance to access your data. | Create a DB instance to access your data. | 
| global failover | RDS-EVENT-0423 | Waiting for data synchronization with the target DB cluster. Current target DB cluster lag behind the primary DB cluster: `{{%s}}`. | This event is for a switchover operation (previously called "managed planned failover").<br />A replication lag is occurring during the synchronization phase of the global database failover. | 
| maintenance | RDS-EVENT-0156 | The DB cluster has a DB engine minor version upgrade available. | None | 
| maintenance | RDS-EVENT-0173 | Database cluster engine version has been upgraded. | Patching of the DB cluster has completed. | 
| maintenance | RDS-EVENT-0174 | Database cluster is in a state that cannot be upgraded. | None | 
| maintenance | RDS-EVENT-0176 | Database cluster engine major version has been upgraded. | None | 
| maintenance | RDS-EVENT-0177 | Database cluster upgrade is in progress. | None | 
| maintenance | RDS-EVENT-0286 | Database cluster engine {{version\_number}} version upgrade started. Cluster remains online. | None | 
| maintenance | RDS-EVENT-0287 | Operating system upgrade requirement detected. | None | 
| maintenance | RDS-EVENT-0288 | Cluster operating system upgrade starting. | None | 
| maintenance | RDS-EVENT-0289 | Cluster operating system upgrade completed. | None | 
| maintenance | RDS-EVENT-0290 | Database cluster has been patched: source version {{version\_number}} => {{new\_version\_number}}. | None | 
| maintenance | RDS-EVENT-0363 | Upgrade preparation in progress: {{cluster\_name}} | Upgrade prechecks have started for the DB cluster. | 
| maintenance | RDS-EVENT-0388 | Starting offline patches to DB instances in partition {{name}}/{{name}} for DB cluster {{name}}: {{partition\_n}}. | Starting the operating system upgrades for the DB instances in the DB cluster. | 
| maintenance | RDS-EVENT-0389 | We were unable to upgrade your DB cluster operating system. You can wait for the next maintenance window, or you can upgrade your DB cluster operating system manually. | None | 
| maintenance | RDS-EVENT-0518 | The engine version of DB cluster {{name}} has been changed from {{previous\_version}} to {{current\_version}} to align with the new primary cluster {{name}} after a failover. | No action required. This change is automatic and keeps your global database consistent. | 
| maintenance | RDS-EVENT-0424 | The DB cluster {{name}} is running version {{version}}, which is higher than the target upgrade version {{version}} for the global cluster. We don't recommend having a secondary cluster on a higher version than the global cluster, as it can cause issues during failover or switchover. Consider upgrading your global cluster to match. | None | 
| notification | RDS-EVENT-0076 | Failed to migrate from {{name}} to {{name}}. Reason: {{reason}}. | Migration to an Aurora DB cluster failed. | 
| notification | RDS-EVENT-0077 | Failed to convert {{name}}.{{name}} to InnoDB. Reason: {{reason}}. | An attempt to convert a table from the source database to InnoDB failed during the migration to an Aurora DB cluster. | 
| notification | RDS-EVENT-0085 | Unable to upgrade DB cluster {{name}} because the instance {{name}} has a status of {{name}}. Resolve the issue or delete the instance and try again. | An error occurred while attempting to patch the Aurora DB cluster. Check your instance status, resolve the issue, and try again. For more information see [Maintaining an Amazon Aurora DB cluster](USER_UpgradeDBInstance.Maintenance.md). | 
| notification | RDS-EVENT-0141 | Scaling DB cluster from {{units}} to {{units}} for this reason: {{reason}}. | Scaling initiated for the Aurora Serverless DB cluster. | 
| notification | RDS-EVENT-0142 | The DB cluster has scaled from {{units}} to {{units}}. | Scaling completed for the Aurora Serverless DB cluster. | 
| notification | RDS-EVENT-0144 | The DB cluster is being paused. | An automatic pause was initiated for the Aurora Serverless DB cluster. | 
| notification | RDS-EVENT-0145 | The DB cluster is paused. | The Aurora Serverless DB cluster has been paused. | 
| notification | RDS-EVENT-0146 | Pause was canceled for the DB cluster. | The pause was canceled for the Aurora Serverless DB cluster. | 
| notification | RDS-EVENT-0147 | The DB cluster is being resumed. | A resume operation was initiated for the Aurora Serverless DB cluster. | 
| notification | RDS-EVENT-0148 | The DB cluster is resumed. | The resume operation completed for the Aurora Serverless DB cluster. | 
| notification | RDS-EVENT-0149 | The DB cluster has scaled from {{units}} to {{units}}, but scaling wasn't seamless for this reason: {{reason}}. | Seamless scaling completed with the force option for the Aurora Serverless DB cluster. Connections might have been interrupted as required. | 
| notification | RDS-EVENT-0150 | DB cluster stopped. | None | 
| notification | RDS-EVENT-0151 | DB cluster started. | None | 
| notification | RDS-EVENT-0152 | DB cluster stop failed. | None | 
| notification | RDS-EVENT-0153 | DB cluster is being started due to it exceeding the maximum allowed time being stopped. | None | 
| notification | RDS-EVENT-0172 | Renamed cluster from {{name}} to {{name}}. | None | 
| notification | RDS-EVENT-0234 | Export task failed. | The DB cluster export task failed. | 
| notification | RDS-EVENT-0235 | Export task canceled. | The DB cluster export task was canceled. | 
| notification | RDS-EVENT-0236 | Export task completed. | The DB cluster export task completed. | 
| notification | RDS-EVENT-0386 | DB instances in DB cluster {{name}} have been partitioned: {{list\_of\_partitions}}. DB cluster is online. | The operating system upgrades for the DB instances in the DB cluster were successful. | 
| notification | RDS-EVENT-0426 | RDS can't configure the DB cluster {{name}} as a replication source because of idle or long-running transactions. Wait for the transactions to complete or cancel them, and try again. | None | 
| notification | RDS-EVENT-0512 | Volume replacement for DB cluster {{name}} started. | None | 
| notification | RDS-EVENT-0513 | Volume replacement for DB cluster {{name}} completed. | None | 
| maintenance, serverless | RDS-EVENT-0521 | DB cluster serverless platform update starting. | None | 
| maintenance, serverless | RDS-EVENT-0522 | DB cluster serverless platform update completed. Database cluster is online. | None | 

## DB cluster snapshot events
<a name="USER_Events.Messages.cluster-snapshot"></a>

The following table shows the event category and a list of events when a DB cluster snapshot is the source type.



- ** backup **
  - **RDS event ID:** RDS-EVENT-0074
  - **Message:** Creating manual cluster snapshot.
  - **Notes:** None

- ** backup **
  - **RDS event ID:** RDS-EVENT-0075
  - **Message:** Manual cluster snapshot created.
  - **Notes:** None

- **notification**
  - **RDS event ID:** RDS-EVENT-0162
  - **Message:** The cluster snapshot export task failed.
  - **Notes:** None

- **notification**
  - **RDS event ID:** RDS-EVENT-0163
  - **Message:** The cluster snapshot export task was canceled.
  - **Notes:** None

- **notification**
  - **RDS event ID:** RDS-EVENT-0164
  - **Message:** The cluster snapshot export task completed.
  - **Notes:** None

- **backup**
  - **RDS event ID:** RDS-EVENT-0168
  - **Message:** Creating automated cluster snapshot.
  - **Notes:** None

- **backup**
  - **RDS event ID:** RDS-EVENT-0169
  - **Message:** Automated cluster snapshot created.
  - **Notes:** None

- ** failure **
  - **RDS event ID:** RDS-EVENT-0489
  - **Message:** Export task {{name}}: Table extraction failed for table {{name}} due to {{message}}.
  - **Notes:** This event is not supported by faster export.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0491
  - **Message:** Export task {{name}}: Table {{name}} will be exported in a slower single-threaded mode. Please expect a delay in export completion.
  - **Notes:** This event is not supported by faster export.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0492
  - **Message:** Export task {{name}}: Table {{name}} is in progress, and the exported size is {{number}} GB.
  - **Notes:** This event will only be sent for tables taking more than 1 hour to complete.<br />This event is not supported by faster export.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0493
  - **Message:** Export task {{name}} is at {{name}} stage. / **Notes:** None
  - **Message:** Export task {{name}}: Export progress is at {{number}}% with {{number}} table(s) in-progress and {{number}} table(s) finished. The total size of finished tables is {{number}} GB. / **Notes:** This event is not supported by faster export.



## DB instance events
<a name="USER_Events.Messages.instance"></a>

The following table shows the event category and a list of events when a DB instance is the source type.


|  Category  | RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| availability | RDS-EVENT-0004 | DB instance shutdown. | None | 
| availability | RDS-EVENT-0006 | DB instance restarted. | None | 
| availability | RDS-EVENT-0022 | Error restarting mysql: {{message}}. | An error has occurred while restarting Aurora MySQL or RDS for MariaDB. | 
| availability | RDS-EVENT-0419 | Amazon RDS has been unable to access the KMS encryption key for database instance {{name}}. This database will be placed into an inaccessible state. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | None | 
| backtrack | RDS-EVENT-0131 | The actual Backtrack window is smaller than the target Backtrack window you specified. Consider reducing the number of hours in your target Backtrack window. | For more information about backtracking, see [Backtracking an Aurora DB cluster](AuroraMySQL.Managing.Backtrack.md). | 
| backtrack | RDS-EVENT-0132 | The actual Backtrack window is the same as the target Backtrack window. | None | 
| configuration change | RDS-EVENT-0011 | Updated to use DBParameterGroup {{name}}. | None | 
| configuration change | RDS-EVENT-0012 | Applying modification to database instance class.  | None | 
| configuration change | RDS-EVENT-0014 | Finished applying modification to DB instance class. | None | 
| configuration change | RDS-EVENT-0017 | Finished applying modification to allocated storage. | None | 
| configuration change | RDS-EVENT-0025 | Finished applying modification to convert to a Multi-AZ DB instance. | None | 
| configuration change | RDS-EVENT-0029 | Finished applying modification to convert to a standard (Single-AZ) DB instance. | None | 
| configuration change | RDS-EVENT-0033 | There are {{number}} users matching the master username; only resetting the one not tied to a specific host. | None | 
| configuration change | RDS-EVENT-0067 | Unable to reset your password. Error information: {{message}}. | None | 
| configuration change | RDS-EVENT-0078 | Monitoring Interval changed to {{number}}. | The Enhanced Monitoring configuration has been changed. | 
| configuration change | RDS-EVENT-0092 | Finished updating DB parameter group. | None | 
| creation | RDS-EVENT-0005 | DB instance created. | None | 
| deletion | RDS-EVENT-0003 | DB instance deleted. | None | 
| failure | RDS-EVENT-0035 | Database instance put into {{state}}. {{message}}. | The DB instance has invalid parameters. For example, if the DB instance could not start because a memory-related parameter is set too high for this instance class, your action would be to modify the memory parameter and reboot the DB instance. | 
| failure | RDS-EVENT-0036 | Database instance in {{state}}. {{message}}. | The DB instance is in an incompatible network. Some of the specified subnet IDs are invalid or do not exist. | 
| failure | RDS-EVENT-0079 | Amazon RDS has been unable to create credentials for enhanced monitoring and this feature has been disabled. This is likely due to the rds-monitoring-role not being present and configured correctly in your account. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | Enhanced Monitoring can't be enabled without the Enhanced Monitoring IAM role. For information about creating the IAM role, see [To create an IAM role for Amazon RDS enhanced monitoring](USER_Monitoring.OS.Enabling.md#USER_Monitoring.OS.IAMRole). | 
| failure | RDS-EVENT-0080 | Amazon RDS has been unable to configure enhanced monitoring on your instance: {{name}} and this feature has been disabled. This is likely due to the rds-monitoring-role not being present and configured correctly in your account. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | Enhanced Monitoring was disabled because an error occurred during the configuration change. It is likely that the Enhanced Monitoring IAM role is configured incorrectly. For information about creating the enhanced monitoring IAM role, see [To create an IAM role for Amazon RDS enhanced monitoring](USER_Monitoring.OS.Enabling.md#USER_Monitoring.OS.IAMRole). | 
| failure | RDS-EVENT-0082 | Amazon RDS has been unable to create credentials to access your Amazon S3 Bucket for your DB instance {{name}}. This is due to the S3 snapshot ingestion IAM role not being configured correctly in your account or the specified Amazon S3 bucket cannot be found. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | Aurora was unable to copy backup data from an Amazon S3 bucket. It is likely that the permissions for Aurora to access the Amazon S3 bucket are configured incorrectly. For more information, see [Physical migration from MySQL by using Percona XtraBackup and Amazon S3](AuroraMySQL.Migrating.ExtMySQL.S3.md) .  | 
| failure | RDS-EVENT-0353 | The DB instance can't be created because of insufficient resource limits. {{message}}. | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0418 | Amazon RDS is unable to access the KMS encryption key for database instance {{name}}. This is likely due to the key being disabled or Amazon RDS being unable to access it. If this continues the database will be placed into an inaccessible state. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | None | 
| failure | RDS-EVENT-0420 | Amazon RDS can now successfully access the KMS encryption key for database instance {{name}}. | None | 
| low storage | RDS-EVENT-0007 | Allocated storage has been exhausted. Allocate additional storage to resolve. | The allocated storage for the DB instance has been consumed. To resolve this issue, allocate additional storage for the DB instance. For more information, see the [RDS FAQ](https://aws.amazon.com/rds/faqs). You can monitor the storage space for a DB instance using the **Free Storage Space** metric. | 
| low storage | RDS-EVENT-0089 | The free storage capacity for DB instance: {{name}} is low at {{percentage}} of the provisioned storage [Provisioned Storage: {{size}}, Free Storage: {{size}}]. You may want to increase the provisioned storage to address this issue. | The DB instance has consumed more than 90% of its allocated storage. You can monitor the storage space for a DB instance using the **Free Storage Space** metric. | 
| low storage | RDS-EVENT-0227 | Your Aurora cluster's storage is dangerously low with only {{amount}} terabytes remaining. Please take measures to reduce the storage load on your cluster. | The Aurora storage subsystem is running low on space. | 
| maintenance | RDS-EVENT-0026 | Applying off-line patches to DB instance. | Offline maintenance of the DB instance is taking place. The DB instance is currently unavailable. | 
| maintenance | RDS-EVENT-0027 | Finished applying off-line patches to DB instance. | Offline maintenance of the DB instance is complete. The DB instance is now available. | 
| maintenance | RDS-EVENT-0047 | Database instance patched. | None | 
| maintenance | RDS-EVENT-0155 | The DB instance has a DB engine minor version upgrade available. | None | 
| maintenance | RDS-EVENT-0178 | Database instance upgrade is in progress. | None | 
| maintenance | RDS-EVENT-0422 | RDS will replace the host of DB instance {{name}} due to a pending maintenance action. | None | 
| notification | RDS-EVENT-0044 | {{message}} | This is an operator-issued notification. For more information, see the event message. | 
| notification | RDS-EVENT-0048 | Delaying database engine upgrade since this instance has read replicas that need to be upgraded first. | Patching of the DB instance has been delayed. | 
| notification | RDS-EVENT-0087 | DB instance stopped.  | None | 
| notification | RDS-EVENT-0088 | DB instance started. | None | 
| notification | RDS-EVENT-0365 | Timezone files were updated. Restart your RDS instance for the changes to take effect. | None | 
| notification, serverless | RDS-EVENT-0370 | Initiated pause for the DB instance. | A new attempt to pause an idle Aurora serverless DB instance was started. | 
| notification, serverless | RDS-EVENT-0371 | Pause was canceled for the DB instance. | An attempt to pause an idle Aurora serverless DB instance was unsuccessful, due to workload. | 
| notification, serverless | RDS-EVENT-0372 | Successfully paused the DB instance. | The Aurora serverless DB instance was paused. | 
| notification, serverless | RDS-EVENT-0373 | Initiated resume for the DB instance. | The Aurora serverless DB instance started resuming, due to new workload or administrative or maintenance activity. | 
| notification, serverless | RDS-EVENT-0374 | Successfully resumed the DB instance. | The Aurora serverless DB instance resumed. | 
| notification | RDS-EVENT-0385 | Cluster topology is updated. | There are DNS changes to the DB cluster for the DB instance. This includes when new DB instances are added or deleted, or there's a failover. | 
| notification, global database | RDS-EVENT-0390 | Attempt to block writes for DB cluster {{cluster\_id}} in Region {{region\_id}} succeeded. | Aurora began blocking writes at the storage layer in preparation for switchover or failover of an Aurora global database. | 
| notification, global database | RDS-EVENT-0391 | Attempt to block writes for DB cluster {{cluster\_id}} in Region {{region\_id}} timed out. | Aurora wasn't able to block writes at the storage layer in preparation for switchover or failover of an Aurora global database. The switchover or failover will proceed but you might need to recover recently written data from the snapshot of the original primary cluster. | 
| read replica | RDS-EVENT-0045 | Replication has stopped. | This message appears when there is an error during replication. To determine the type of error, see [ Troubleshooting a MySQL read replica problem](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Troubleshooting.html). | 
| read replica | RDS-EVENT-0046 | Replication for the Read Replica resumed. | This message appears when you first create a read replica, or as a monitoring message confirming that replication is functioning properly. If this message follows an `RDS-EVENT-0045` notification, then replication has resumed following an error or after replication was stopped. | 
| read replica | RDS-EVENT-0057 | Replication streaming has been terminated. | None | 
| recovery | RDS-EVENT-0020 | Recovery of the DB instance has started. Recovery time will vary with the amount of data to be recovered. | None | 
| recovery | RDS-EVENT-0021 | Recovery of the DB instance is complete. | None | 
| recovery | RDS-EVENT-0023 | Emergent Snapshot Request: {{message}}. | A manual backup has been requested but Amazon RDS is currently in the process of creating a DB snapshot. Submit the request again after Amazon RDS has completed the DB snapshot. | 
| recovery | RDS-EVENT-0052 | Multi-AZ instance recovery started. | Recovery time will vary with the amount of data to be recovered. | 
| recovery | RDS-EVENT-0053 | Multi-AZ instance recovery completed. Pending failover or activation. | This message indicates that Amazon RDS has prepared your DB instance to initiate a failover to the secondary instance if necessary. | 
| recovery | RDS-EVENT-0361 | Recovery of standby DB instance has started. | The standby DB instance is rebuilt during the recovery process. Database performance is impacted during the recovery process. | 
| recovery | RDS-EVENT-0362 | Recovery of standby DB instance has completed. | The standby DB instance is rebuilt during the recovery process. Database performance is impacted during the recovery process. | 
| restoration | RDS-EVENT-0019 | Restored from DB instance {{name}} to {{name}}. | The DB instance has been restored from a point-in-time backup. | 
| security patching | RDS-EVENT-0230 | A system update is available for your DB instance. For information about applying updates, see 'Maintaining a DB instance' in the RDS User Guide. | A new, minor version, operating system patch is available for your DB instance. For information about applying updates, see [Operating system updates for Aurora DB clusters](USER_UpgradeDBInstance.Maintenance.md#Aurora_OS_updates). | 
| maintenance | RDS-EVENT-0425 | Amazon RDS can't perform the OS upgrade because there are no available IP addresses in the specified subnets. Choose subnets with available IP addresses and try again. | None | 
| maintenance | RDS-EVENT-0429 | Amazon RDS can't perform the OS upgrade because of insufficient capacity available for the {{type}} instance type in the {{zone}} Availability Zone | None | 
| maintenance | RDS-EVENT-0501 | Amazon RDS DB instance's server certificate requires rotation through a pending maintenance action. | DB instance's server certificate requires rotation through a pending maintenance action. Amazon RDS reboots your database during this maintenance to complete the certificate rotation. To schedule this maintenance, go to the **Maintenance & backups** tab and choose **Apply now** or **Schedule for next maintenance window**. If the change is not scheduled, Amazon RDS automatically applies it in your mainteance window on the auto apply date shown in your maintenance action. | 
| maintenance | RDS-EVENT-0502 | Amazon RDS has scheduled a server certificate rotation for DB instance during the next maintenance window. This maintenance will require a database reboot. | None | 
| maintenance, serverless | RDS-EVENT-0523 | Amazon RDS can't perform the Serverless platform update because there are no available IP addresses in the specified subnets. Choose subnets with available IP addresses and try again. | None | 
| maintenance, serverless | RDS-EVENT-0524 | Amazon RDS can't perform the Serverless platform update because of insufficient capacity available. | None | 
| maintenance, serverless | RDS-EVENT-0525 | The Serverless platform update failed for the DB instance {{name}}. | None | 

## DB parameter group events
<a name="USER_Events.Messages.parameter-group"></a>

The following table shows the event category and a list of events when a DB parameter group is the source type.


|  Category  | RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| configuration change | RDS-EVENT-0037 | Updated parameter {{name}} to {{value}} with apply method {{method}}.  | None | 

## DB security group events
<a name="USER_Events.Messages.security-group"></a>

The following table shows the event category and a list of events when a DB security group is the source type.

**Note**  
DB security groups are resources for EC2-Classic. EC2-Classic was retired on August 15, 2022. If you haven't migrated from EC2-Classic to a VPC, we recommend that you migrate as soon as possible. For more information, see [Migrate from EC2-Classic to a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html) in the *Amazon EC2 User Guide* and the blog [ EC2-Classic Networking is Retiring – Here’s How to Prepare](https://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/).


|  Category  | RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| configuration change | RDS-EVENT-0038 | Applied change to security group. | None | 
| failure | RDS-EVENT-0039 | Revoking authorization as {{user}}. | The security group owned by {{user}} doesn't exist. The authorization for the security group has been revoked because it is invalid. | 

## DB shard group events
<a name="USER_Events.Messages.shard-group"></a>

The following table shows the event category and a list of events when a DB shard group is the source type.


|  Category  | RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| failure | RDS-EVENT-0324 | Data load job failed. | The data loading job failed for the reason that appears in the error message. | 
| maintenance | RDS-EVENT-0302 | Your action is required to finalize a pending split shard job {{job\_ID}} for subcluster ID {{number}} in DB shard group {{name}}.<br />To complete the operation invoke the SQL:<pre>SELECT rds_aurora.limitless_finalize_split_shard({{job_ID}});</pre> | None | 
| maintenance | RDS-EVENT-0303 | Finalize for the split shard job {{job\_ID}} has started for subcluster ID {{number}} in DB shard group {{name}}. | None | 
| maintenance | RDS-EVENT-0304 | Split shard job {{job\_ID}} has completed successfully for subcluster ID {{number}} in DB shard group {{name}}. A new shard with subcluster ID {{number}} was added to DB shard group {{name}}. | None | 
| maintenance | RDS-EVENT-0305 | Split shard job {{job\_ID}} has failed for subcluster ID {{number}} in DB shard group {{name}}. | None | 
| maintenance | RDS-EVENT-0366 | Split shard job {{job\_ID}} has started for subcluster ID {{number}} in DB shard group {{name}}. | None | 
| maintenance | RDS-EVENT-0367 | Add router job {{job\_ID}} has started in DB shard group {{name}}. | None | 
| maintenance | RDS-EVENT-0368 | Add router job {{job\_ID}} has completed successfully. A new router with subcluster ID {{number}} was added to DB shard group {{name}}. | None | 
| maintenance | RDS-EVENT-0369 | Add router job {{job\_ID}} has failed in DB shard group {{name}}. | None | 
| maintenance | RDS-EVENT-0394 | Add router job {{job\_ID}} has been canceled in DB shard group {{name}}. | None | 
| maintenance | RDS-EVENT-0395 | Split shard job {{job\_ID}} has been canceled in DB shard group {{name}}. | None | 
| notification | RDS-EVENT-0321 | Initializing infrastructure for the Data Load job. | None | 
| notification | RDS-EVENT-0322 | Data load job is in progress. | None | 
| notification | RDS-EVENT-0323 | Data load job completed successfully. | None | 
| notification | RDS-EVENT-0325 | Canceling Data load job as per customer’s request. | None | 
| notification | RDS-EVENT-0326 | Data load job canceled. | None | 

## RDS Proxy events
<a name="USER_Events.Messages.rds-proxy"></a>

The following table shows the event category and a list of events when an RDS Proxy is the source type.


|  Category  | RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| configuration change | RDS-EVENT-0204 | RDS modified DB proxy {{name}}. | None | 
| configuration change | RDS-EVENT-0207 | RDS modified the end point of the DB proxy {{name}}. | None | 
| configuration change | RDS-EVENT-0213 | RDS detected the addition of the DB instance and automatically added it to the target group of the DB proxy {{name}}. | None | 
| configuration change | RDS-EVENT-0214 | RDS detected deletion of DB instance {{name}} and automatically removed it from target group {{name}} of DB proxy {{name}}. | None | 
| configuration change | RDS-EVENT-0215 | RDS detected deletion of DB cluster {{name}} and automatically removed it from target group {{name}} of DB proxy {{name}}. | None | 
| creation | RDS-EVENT-0203 | RDS created DB proxy {{name}}. | None | 
| creation | RDS-EVENT-0206 | RDS created endpoint {{name}} for DB proxy {{name}}. | None | 
| deletion | RDS-EVENT-0205 | RDS deleted DB proxy {{name}}. | None | 
| deletion | RDS-EVENT-0208 | RDS deleted endpoint {{name}} for DB proxy {{name}}. | None | 
| failure | RDS-EVENT-0243 | RDS failed to provision capacity for proxy {{name}} because there aren't enough IP addresses available in your subnets: {{name}}. To fix the issue, make sure that your subnets have the minimum number of unused IP addresses as recommended in the RDS Proxy documentation. | To determine the recommended number for your instance class, see [Planning for IP address capacity](rds-proxy-network-prereqs.md#rds-proxy-network-prereqs.plan-ip-address). | 
| failure | RDS-EVENT-0275 | RDS throttled some connections to DB proxy {{name}}. The number of simultaneous connection requests from the client to the proxy has exceeded the limit. | None | 

## Blue/green deployment events
<a name="USER_Events.Messages.BlueGreenDeployments"></a>

The following table shows the event category and a list of events when a blue/green deployment is the source type.

For more information about blue/green deployments, see [Using Amazon Aurora Blue/Green Deployments for database updates](blue-green-deployments.md).


|  Category  | Amazon RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| creation | RDS-EVENT-0244 | Blue/green deployment tasks completed. You can make more modifications to the green environment databases or switch over the deployment. | None | 
| failure | RDS-EVENT-0245 | Creation of blue/green deployment failed because {{reason}}. | None | 
| deletion | RDS-EVENT-0246 | Blue/green deployment deleted. | None | 
| notification | RDS-EVENT-0247 | Switchover from {{blue}} to {{green}} started. | None | 
| notification | RDS-EVENT-0248 | Switchover completed on blue/green deployment. | None | 
| failure | RDS-EVENT-0249 | Switchover canceled on blue/green deployment. | None | 
| notification |  RDS-EVENT-0259 | Switchover from DB cluster {{blue}} to {{green}} started. | None | 
| notification |  RDS-EVENT-0260 | Switchover from DB cluster {{blue}} to {{green}} completed. Renamed {{blue}} to {{blue-old}} and {{green}} to {{blue}}. | None | 
| failure |  RDS-EVENT-0261 | Switchover from DB cluster {{blue}} to {{green}} was canceled due to {{reason}}. | None | 
| notification |  RDS-EVENT-0311  | Sequence sync for switchover of DB cluster {{blue}} to {{green}} has initiated. Switchover when using sequences may lead to extended downtime. | None | 
| notification |  RDS-EVENT-0312  | Sequence sync for switchover of DB cluster {{blue}} to {{green}} has completed. | None | 
| failure |  RDS-EVENT-0314  | Sequence sync for switchover of DB cluster {{blue}} to {{green}} was cancelled because sequences failed to sync. | None | 
| notification | RDS-EVENT-0409  | {{message}} | None | 