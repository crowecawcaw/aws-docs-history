

# Amazon RDS event categories and event messages
<a name="USER_Events.Messages"></a>

Amazon RDS generates a significant number of events in categories that you can subscribe to using the Amazon RDS Console, AWS CLI, or the API.

**Topics**
+ [DB cluster events](#USER_Events.Messages.cluster)
+ [DB cluster snapshot events](#USER_Events.Messages.cluster-snapshot)
+ [DB instance events](#USER_Events.Messages.instance)
+ [DB parameter group events](#USER_Events.Messages.parameter-group)
+ [DB security group events](#USER_Events.Messages.security-group)
+ [DB snapshot events](#USER_Events.Messages.snapshot)
+ [RDS Proxy events](#USER_Events.Messages.rds-proxy)
+ [Blue/green deployment events](#USER_Events.Messages.BlueGreenDeployments)
+ [Custom engine version events](#USER_Events.Messages.CEV)

## DB cluster events
<a name="USER_Events.Messages.cluster"></a>

The following table shows the event category and a list of events when a DB cluster is the source type.

For more information about Multi-AZ DB cluster deployments, see [Multi-AZ DB cluster deployments for Amazon RDS](multi-az-db-clusters-concepts.md).


|  Category  | RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| configuration change | RDS-EVENT-0016 | Reset master credentials. | None | 
| creation | RDS-EVENT-0170 | DB cluster created. | None | 
| failover | RDS-EVENT-0069 | Cluster failover failed, check the health of your cluster instances and try again. | None | 
| failover | RDS-EVENT-0070 | Promoting previous primary again: {{name}}. | None | 
| failover | RDS-EVENT-0071 | Completed failover to DB instance: {{name}}. | None | 
| failover | RDS-EVENT-0072 | Started same AZ failover to DB instance: {{name}}. | None | 
| failover | RDS-EVENT-0073 | Started cross AZ failover to DB instance: {{name}}. | None | 
| failure | RDS-EVENT-0354 | You can't create the DB cluster because of incompatible resources. {{message}}. | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0355 | The DB cluster can't be created because of insufficient resource limits. {{message}}. | The {{message}} includes details about the failure. | 
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
| maintenance | RDS-EVENT-0410 | The pre-check started for the database cluster engine version upgrade. | None | 
| maintenance | RDS-EVENT-0412 | The pre-check for the database cluster engine version upgrade failed or timed out. | None | 
| maintenance | RDS-EVENT-0413 | The DB cluster pre-upgrade tasks are in progress. | None | 
| maintenance | RDS-EVENT-0414 | The DB cluster post-upgrade tasks are in progress. | None | 
| maintenance | RDS-EVENT-0417 | Database cluster engine version upgrade started. | None | 
| notification | RDS-EVENT-0172 | Renamed cluster from {{name}} to {{name}}. | None | 
| read replica | RDS-EVENT-0411 | The pre-check finished for the database cluster engine version upgrade. | None | 

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
| availability | RDS-EVENT-0022 | Error restarting mysql: {{message}}. | An error has occurred while restarting MySQL. | 
| availability | RDS-EVENT-0221 | DB instance has reached the storage-full threshold, and the database has been shut down. You can increase the allocated storage to address this issue. | None | 
| availability | RDS-EVENT-0222 | Free storage capacity for DB instance {{name}} is low at {{percentage}} of the allocated storage [Allocated storage: {{amount}}, Free storage: {{amount}}]. The database will be shut down to prevent corruption if free storage is lower than {{amount}}. You can increase the allocated storage to address this issue. | Applies only to RDS for MySQL when a DB instance consumes more than 90% of the allocated storage. Monitor the storage space for a DB instance using the Free Storage Space metric. For more information, see [Amazon RDS DB instance storage](CHAP_Storage.md). | 
| availability | RDS-EVENT-0330 | The free storage capacity of the dedicated transaction log volume is too low for DB instance {{name}}. The log volume free storage is {{percentage}} of the allocated storage. [Allocated storage: {{amount}}, Free storage: {{amount}}] The database will be shut down to prevent corruption if the free storage is lower than {{amount}}. You can disable the dedicated transaction log volume to resolve this issue. | For more information, see [Dedicated log volume (DLV)](CHAP_Storage.md#CHAP_Storage.dlv). | 
| availability | RDS-EVENT-0331 | The free storage capacity of the dedicated transaction log volume is too low for DB instance {{name}}. The log volume free storage is {{percentage}} of the provisioned storage. [Provisioned Storage: {{amount}}, Free Storage: {{amount}}] You can disable the dedicated transaction log volume to resolve this issue. | For more information, see [Dedicated log volume (DLV)](CHAP_Storage.md#CHAP_Storage.dlv). | 
| availability | RDS-EVENT-0396 | Amazon RDS has scheduled a reboot for this read replica in this instance's next maintenance window after internal user password rotation. | None | 
| availability | RDS-EVENT-0419 | Amazon RDS has been unable to access the KMS encryption key for database instance {{name}}. This database will be placed into an inaccessible state. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | None | 
| backup | RDS-EVENT-0001 | Backing up DB instance. | None | 
| backup | RDS-EVENT-0002 | Finished DB instance backup. | None | 
| backup | RDS-EVENT-0086 | We are unable to associate the option group {{name}} with the database instance {{name}}. Confirm that option group {{name}} is supported on your DB instance class and configuration. If so, verify all option group settings and retry. | For more information see [Working with option groups](USER_WorkingWithOptionGroups.md). | 
| configuration change | RDS-EVENT-0011 | Updated to use DBParameterGroup {{name}}. | None | 
| configuration change | RDS-EVENT-0012 | Applying modification to database instance class.  | None | 
| configuration change | RDS-EVENT-0014 | Finished applying modification to DB instance class. | None | 
| configuration change | RDS-EVENT-0016 | Reset master credentials. | None | 
| configuration change | RDS-EVENT-0017 | Finished applying modification to allocated storage. | None | 
| configuration change | RDS-EVENT-0018 | Applying modification to allocated storage. | None | 
| configuration change | RDS-EVENT-0024 | Applying modification to convert to a Multi-AZ DB instance. | None | 
| configuration change | RDS-EVENT-0025 | Finished applying modification to convert to a Multi-AZ DB instance. | None | 
| configuration change | RDS-EVENT-0028 | Disabled automated backups. | None | 
| configuration change | RDS-EVENT-0029 | Finished applying modification to convert to a standard (Single-AZ) DB instance. | None | 
| configuration change | RDS-EVENT-0030 | Applying modification to convert to a standard (Single-AZ) DB instance. | None | 
| configuration change | RDS-EVENT-0032 | Enabled automated backups. | None | 
| configuration change | RDS-EVENT-0033 | There are {{number}} users matching the master username; only resetting the one not tied to a specific host. | None | 
| configuration change | RDS-EVENT-0067 | Unable to reset your password. Error information: {{message}}. | None | 
| configuration change | RDS-EVENT-0078 | Monitoring Interval changed to {{number}}. | The Enhanced Monitoring configuration has been changed. | 
| configuration change | RDS-EVENT-0092 | Finished updating DB parameter group. | None | 
| configuration change | RDS-EVENT-0217 | Applying autoscaling-initiated modification to allocated storage. | None | 
| configuration change | RDS-EVENT-0218 | Finished applying autoscaling-initiated modification to allocated storage. | None | 
| configuration change | RDS-EVENT-0295 | Storage configuration upgrade started. | None | 
| configuration change | RDS-EVENT-0296 | Storage configuration upgrade completed. | None | 
| configuration change | RDS-EVENT-0332 | The dedicated log volume is disabled. | For more information, see [Dedicated log volume (DLV)](CHAP_Storage.md#CHAP_Storage.dlv). | 
| configuration change | RDS-EVENT-0333 | Disabling the dedicated log volume has started. | For more information, see [Dedicated log volume (DLV)](CHAP_Storage.md#CHAP_Storage.dlv). | 
| configuration change | RDS-EVENT-0334 | Enabling the dedicated log volume has started. | For more information, see [Dedicated log volume (DLV)](CHAP_Storage.md#CHAP_Storage.dlv). | 
| configuration change | RDS-EVENT-0335 | The dedicated log volume is enabled. | For more information, see [Dedicated log volume (DLV)](CHAP_Storage.md#CHAP_Storage.dlv). | 
| configuration change | RDS-EVENT-0383 | {{engine version}} doesn't support the memcached plugin. RDS will continue upgrading your DB instance and remove this plugin. | Starting with MySQL 8.3.0, the memcached plugin isn't supported. For more information, see [Changes in MySQL 8.3.0 (2024-01-16, Innovation Release)](https://dev.mysql.com/doc/relnotes/mysql/8.3/en/news-8-3-0.html). | 
| creation | RDS-EVENT-0005 | DB instance created. | None | 
| deletion | RDS-EVENT-0003 | DB instance deleted. | None | 
| failover | RDS-EVENT-0013 | Multi-AZ instance failover started. | A Multi-AZ failover that resulted in the promotion of a standby DB instance has started. | 
| failover | RDS-EVENT-0015 | Multi-AZ failover to standby complete - DNS propagation may take a few minutes. | A Multi-AZ failover that resulted in the promotion of a standby DB instance is complete. It may take several minutes for the DNS to transfer to the new primary DB instance. | 
| failover | RDS-EVENT-0034 | Abandoning user requested failover since a failover recently occurred on the database instance. | Amazon RDS isn't attempting a requested failover because a failover recently occurred on the DB instance. | 
| failover | RDS-EVENT-0049 | Multi-AZ instance failover completed. | None | 
| failover | RDS-EVENT-0050 | Multi-AZ instance activation started. | A Multi-AZ activation has started after a successful DB instance recovery. This event occurs if Amazon RDS promotes the primary DB instance to the same AZ as the previous primary DB instance. | 
| failover | RDS-EVENT-0051 | Multi-AZ instance activation completed. | A Multi-AZ activation is complete. Your database should be accessible now.  | 
| failover | RDS-EVENT-0065 | Recovered from partial failover. | None | 
| failure | RDS-EVENT-0031 | DB instance put into {{name}} state. RDS recommends that you initiate a point-in-time-restore. | The DB instance has failed due to an incompatible configuration or an underlying storage issue. Begin a point-in-time-restore for the DB instance. | 
| failure | RDS-EVENT-0035 | Database instance put into {{state}}. {{message}}. | The DB instance has invalid parameters. For example, if the DB instance could not start because a memory-related parameter is set too high for this instance class, your action would be to modify the memory parameter and reboot the DB instance. | 
| failure | RDS-EVENT-0036 | Database instance in {{state}}. {{message}}. | The DB instance is in an incompatible network. Some of the specified subnet IDs are invalid or do not exist. | 
| failure | RDS-EVENT-0058 | The Statspack installation failed. {{message}}. | Error while creating Oracle Statspack user account `PERFSTAT`. Drop the account before you add the `STATSPACK` option. | 
| failure | RDS-EVENT-0079 | Amazon RDS has been unable to create credentials for enhanced monitoring and this feature has been disabled. This is likely due to the rds-monitoring-role not being present and configured correctly in your account. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | Enhanced Monitoring can't be enabled without the Enhanced Monitoring IAM role. For information about creating the IAM role, see [To create an IAM role for Amazon RDS enhanced monitoring](USER_Monitoring.OS.Enabling.md#USER_Monitoring.OS.IAMRole). | 
| failure | RDS-EVENT-0080 | Amazon RDS has been unable to configure enhanced monitoring on your instance: {{name}} and this feature has been disabled. This is likely due to the rds-monitoring-role not being present and configured correctly in your account. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | Enhanced Monitoring was disabled because an error occurred during the configuration change. It is likely that the Enhanced Monitoring IAM role is configured incorrectly. For information about creating the enhanced monitoring IAM role, see [To create an IAM role for Amazon RDS enhanced monitoring](USER_Monitoring.OS.Enabling.md#USER_Monitoring.OS.IAMRole). | 
| failure | RDS-EVENT-0081 | Amazon RDS has been unable to create credentials for {{name}} option. This is due to the {{name}} IAM role not being configured correctly in your account. Please refer to the troubleshooting section in the Amazon RDS documentation for further details. | The IAM role that you use to access your Amazon S3 bucket for SQL Server native backup and restore is configured incorrectly. For more information, see [Setting up for native backup and restore](SQLServer.Procedural.Importing.Native.Enabling.md). | 
| failure | RDS-EVENT-0165 | The RDS Custom DB instance is outside the support perimeter. | It's your responsibility to fix configuration issues that put your RDS Custom DB instance into the `unsupported-configuration` state. If the issue is with the AWS infrastructure, you can use the console or the AWS CLI to fix it. If the issue is with the operating system or the database configuration, you can log in to the host to fix it.<br />For more information, see [RDS Custom support perimeter](custom-concept.md#custom-troubleshooting.support-perimeter). | 
| failure | RDS-EVENT-0188 | The DB instance is in a state that can't be upgraded. {{message}} | Amazon RDS was unable to upgrade a MySQL DB instance because of incompatibilities related to the data dictionary. The DB instance was rolled back to MySQL version 5.7 because an attempted upgrade to version 8.0 failed, or rolled back to MySQL version 8.0 because an attempted upgrade to version 8.4 failed. For more information, see [Rollback after failure to upgrade](USER_UpgradeDBInstance.MySQL.Major.md#USER_UpgradeDBInstance.MySQL.Major.RollbackAfterFailure). | 
| failure | RDS-EVENT-0219 | DB instance is in an invalid state. No actions are necessary. Autoscaling will retry later. | None | 
| failure | RDS-EVENT-0220 | DB instance has undergone the maximum number of storage modifications allowed within a 24-hour period. No actions are necessary. Autoscaling will retry when the DB instance is eligible for another storage modification. | None | 
| failure | RDS-EVENT-0223 | Storage autoscaling is unable to scale the storage for the reason: {{reason}}. | None | 
| failure | RDS-EVENT-0224 | Storage autoscaling has triggered a pending scale storage task that will reach or exceed the maximum storage threshold. Increase the maximum storage threshold. | None | 
| failure | RDS-EVENT-0237 | DB instance has a storage type that's currently unavailable in the Availability Zone. Autoscaling will retry later. | None | 
| failure | RDS-EVENT-0254 | Underlying storage quota for this customer account has exceeded the limit. Please increase the allowed storage quota to let the scaling go through on the instance. | None | 
| failure | RDS-EVENT-0278 | The DB instance creation failed. {{message}} | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0279 | The promotion of the RDS Custom read replica failed. {{message}} | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0280 | RDS Custom couldn't upgrade the DB instance because the pre-check failed. {{message}} | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0281 | RDS Custom couldn't modify the DB instance because the pre-check failed. {{message}} | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0282 | RDS Custom couldn't modify the DB instance because the Elastic IP permissions aren't correct. Please confirm the Elastic IP address is tagged with `AWSRDSCustom`. | None | 
| failure | RDS-EVENT-0283 | RDS Custom couldn't modify the DB instance because the Elastic IP limit has been reached in your account. Release unused Elastic IPs or request a quota increase for your Elastic IP address limit. | None | 
| failure | RDS-EVENT-0284 | RDS Custom couldn't convert the instance to high availability because the pre-check failed. {{message}} | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0285 | RDS Custom couldn't create a final snapshot for the DB instance because {{message}}. | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0421 | RDS Custom couldn't convert the DB instance to a Multi-AZ deployment: {{message}}. The instance will remain a Single-AZ deployment. See the RDS User Guide for information about Multi-AZ deployments for RDS Custom for Oracle. | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0306 | Storage configuration upgrade failed. Please retry the upgrade. | None | 
| failure | RDS-EVENT-0315 | Unable to move incompatible-network database, {{name}}, to the available status: {{message}} | The database networking configuration is invalid. The database could not be moved from incompatible-network to available. | 
| failure | RDS-EVENT-0328 | Failed to join a host to a domain. Domain membership status for instance {{instancename}} has been set to Failed. | None | 
| failure | RDS-EVENT-0329 | Failed to join a host to your domain. During the domain join process, Microsoft Windows returned the error code {{message}}. Verify your network and permission configurations and issue a `modify-db-instance` request to re-attempt the domain join. | When using a self-managed Active Directory, see [Troubleshooting self-managed Active Directory](USER_SQLServer_SelfManagedActiveDirectory.TroubleshootingSelfManagedActiveDirectory.md). | 
| failure | RDS-EVENT-0353 | The DB instance can't be created because of insufficient resource limits. {{message}}. | The {{message}} includes details about the failure. | 
| failure | RDS-EVENT-0356 | RDS was unable to configure the Kerberos endpoint in your domain. This might prevent Kerberos authentication for your DB instance. Verify the network configuration between your DB instance and domain controllers. | None | 
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
| maintenance | RDS-EVENT-0264 | The pre-check started for the DB engine version upgrade. | None | 
| maintenance | RDS-EVENT-0265 | The pre-check finished for the DB engine version upgrade. | None | 
| maintenance | RDS-EVENT-0266 | The downtime started for the DB instance. | None | 
| maintenance | RDS-EVENT-0267 | The engine version upgrade started. | None | 
| maintenance | RDS-EVENT-0268 | The engine version upgrade finished. | None | 
| maintenance | RDS-EVENT-0269 | The post-upgrade tasks are in progress. | None | 
| maintenance | RDS-EVENT-0270 | The DB engine version upgrade failed. The engine version upgrade rollback succeeded. | None | 
| maintenance | RDS-EVENT-0398 | Waiting for the DB engine version upgrade to finish on the primary DB instance. | Emitted on a read replica during a major engine version upgrade. | 
| maintenance | RDS-EVENT-0399 | Waiting for the DB engine version upgrade to finish on the read replicas. | Emitted on source DB engine during a major engine version upgrade. | 
| maintenance | RDS-EVENT-0422 | RDS will replace the host of DB instance {{name}} due to a pending maintenance action. | None | 
| maintenance, failure | RDS-EVENT-0195 | {{message}} | The update of the Oracle time zone file failed. For more information, see [Oracle time zone file autoupgrade](Appendix.Oracle.Options.Timezone-file-autoupgrade.md). | 
| maintenance, notification | RDS-EVENT-0191 | A new version of the time zone file is available for update. | If you update your RDS for Oracle DB engine, Amazon RDS generates this event if you haven't chosen a time zone file upgrade and the database doesn’t use the latest DST time zone file available on the instance. For more information, see [Oracle time zone file autoupgrade](Appendix.Oracle.Options.Timezone-file-autoupgrade.md). | 
| maintenance, notification | RDS-EVENT-0192 | The update of your time zone file has started. | The upgrade of your Oracle time zone file has begun. For more information, see [Oracle time zone file autoupgrade](Appendix.Oracle.Options.Timezone-file-autoupgrade.md). | 
| maintenance, notification | RDS-EVENT-0193 | No update is available for the current time zone file version. | Your Oracle DB instance is using latest time zone file version, and either of the following statements is true:+  You recently added the `TIMEZONE_FILE_AUTOUPGRADE` option. <br />+  Your Oracle DB engine is being upgraded. <br />For more information, see [Oracle time zone file autoupgrade](Appendix.Oracle.Options.Timezone-file-autoupgrade.md). | 
| maintenance, notification | RDS-EVENT-0194 | The update of your time zone file has finished. | The update of your Oracle time zone file has completed. For more information, see [Oracle time zone file autoupgrade](Appendix.Oracle.Options.Timezone-file-autoupgrade.md). | 
| notification | RDS-EVENT-0044 | {{message}} | This is an operator-issued notification. For more information, see the event message. | 
| notification | RDS-EVENT-0048 | Delaying database engine upgrade since this instance has read replicas that need to be upgraded first. | Patching of the DB instance has been delayed. | 
| notification | RDS-EVENT-0054 | {{message}} | The MySQL storage engine you are using is not InnoDB, which is the recommended MySQL storage engine for Amazon RDS. For information about MySQL storage engines, see [Supported storage engines for RDS for MySQL](MySQL.Concepts.FeatureSupport.md#MySQL.Concepts.Storage). | 
| notification | RDS-EVENT-0055 | {{message}} | The number of tables you have for your DB instance exceeds the recommended best practices for Amazon RDS. Reduce the number of tables on your DB instance. For information about recommended best practices, see [Amazon RDS basic operational guidelines](CHAP_BestPractices.md#CHAP_BestPractices.DiskPerformance). | 
| notification | RDS-EVENT-0056 | {{message}} | The number of databases you have for your DB instance exceeds the recommended best practices for Amazon RDS. Reduce the number of databases on your DB instance. For information about recommended best practices, see [Amazon RDS basic operational guidelines](CHAP_BestPractices.md#CHAP_BestPractices.DiskPerformance). | 
| notification | RDS-EVENT-0064 | The TDE encryption key was rotated successfully. | For information about recommended best practices, see [Amazon RDS basic operational guidelines](CHAP_BestPractices.md#CHAP_BestPractices.DiskPerformance).  | 
| notification | RDS-EVENT-0084 | Unable to convert the DB instance to Multi-AZ: {{message}}. | You attempted to convert a DB instance to Multi-AZ, but it contains in-memory file groups that are not supported for Multi-AZ. For more information, see [Multi-AZ deployments for Amazon RDS for Microsoft SQL Server](USER_SQLServerMultiAZ.md).  | 
| notification | RDS-EVENT-0087 | DB instance stopped.  | None | 
| notification | RDS-EVENT-0088 | DB instance started. | None | 
| notification | RDS-EVENT-0154 | DB instance is being started due to it exceeding the maximum allowed time being stopped. | None | 
| notification | RDS-EVENT-0157 | Unable to modify the DB instance class. {{message}}. | RDS can't modify the DB instance class because the target instance class can't support the number of databases that exist on the source DB instance. The error message appears as: "The instance has *N* databases, but after conversion it would only support *N*". For more information, see [Limitations for Microsoft SQL Server DB instances](CHAP_SQLServer.md#SQLServer.Concepts.General.FeatureSupport.Limits). | 
| notification | RDS-EVENT-0158 | Database instance is in a state that cannot be upgraded: {{message}}. | None | 
| notification | RDS-EVENT-0167 | {{message}} | The RDS Custom support perimeter configuration has changed. | 
| notification | RDS-EVENT-0189 | The gp2 burst balance credits for the RDS database instance are low. To resolve this issue, reduce IOPS usage or modify your storage settings to enable higher performance. | The gp2 burst balance credits for the RDS database instance are low. To resolve this issue, reduce IOPS usage or modify your storage settings to enable higher performance. For more information, see [I/O credits and burst performance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_gp2) in the *Amazon Elastic Compute Cloud User Guide*. | 
| notification | RDS-EVENT-0225 | Allocated storage size {{amount}} GB is approaching the maximum storage threshold {{amount}} GB. Increase the maximum storage threshold. | This event is invoked when the allocated storage reaches 80% of the maximum storage threshold. To avoid the event, increase the maximum storage threshold. | 
| notification | RDS-EVENT-0231 | Your DB instance's storage modification encountered an internal error. The modification request is pending and will be retried later. | An error has occurred in the read replication process. For more information, see the event message.<br />In addition, see the troubleshooting section for read replicas for your DB engine.+  [Troubleshooting a MariaDB read replica problem](USER_ReadRepl.Troubleshooting.MariaDB.md) <br />+  [Troubleshooting a SQL Server read replica problem](SQLServer.ReadReplicas.Troubleshooting.md) <br />+  [ Troubleshooting a MySQL read replica problem](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Troubleshooting.html) <br />+  [Troubleshooting RDS for Oracle replicas](oracle-read-replicas.troubleshooting.md)  | 
| notification | RDS-EVENT-0253 | The database is using the doublewrite buffer. {{message}}. For more information see the RDS Optimized Writes for {{name}} documentation. | RDS Optimized Writes is incompatible with the instance storage configuration. For more information, see [Improving write performance with RDS Optimized Writes for MySQL](rds-optimized-writes.md) and [Improving write performance with Amazon RDS Optimized Writes for MariaDB](rds-optimized-writes-mariadb.md).<br />You can perform storage configuration upgrade to enable Optimized Writes by [Creating a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-creating.html). | 
| notification | RDS-EVENT-0297 | The storage configuration for DB instance {{name}} supports a maximum size of 16384 GiB. Perform a storage configuration upgrade to support storage sizes greater than 16384 GiB. | You cannot increase the allocated storage size of the DB instance beyond 16384 GiB. To overcome this limitation, perform a storage configuration upgrade. For more information, see [Upgrading the storage file system for a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.UpgradeFileSystem). | 
| notification | RDS-EVENT-0298 | The storage configuration for DB instance {{name}} supports a maximum table size of 2048 GiB. Perform a storage configuration upgrade to support table sizes greater than 2048 GiB. | RDS MySQL and MariaDB instances with this limitation cannot have a table size exceeding 2048 GiB. To overcome this limitation, perform a storage configuration upgrade. For more information, see [Upgrading the storage file system for a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.UpgradeFileSystem). | 
| notification | RDS-EVENT-0327 | Amazon RDS could not find the secret {{SECRET ARN}}. {{message.}} | None | 
| notification | RDS-EVENT-0365 | Timezone files were updated. Restart your RDS instance for the changes to take effect. | None | 
| notification | RDS-EVENT-0385 | Cluster topology is updated. | There are DNS changes to the DB cluster for the DB instance. This includes when new DB instances are added or deleted, or there's a failover. | 
| notification | RDS-EVENT-0403 | A database workload is causing the system to run critically low on memory. To help mitigate the issue, RDS automatically set the value of innodb\_buffer\_pool\_size to {{amount}}. | Applies only to RDS for MySQL and RDS for MariaDB DB instances. | 
| notification | RDS-EVENT-0404 | A database workload is causing the system to run critically low on memory. To help mitigate the issue, RDS automatically set the value of shared\_buffers to {{amount}}. | Applies only to RDS for PostgreSQL DB instances. | 
| read replica | RDS-EVENT-0045 | Replication has stopped. | This message appears when there is an error during replication. To determine the type of error, see [ Troubleshooting a MySQL read replica problem](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Troubleshooting.html). | 
| read replica | RDS-EVENT-0046 | Replication for the Read Replica resumed. | This message appears when you first create a read replica, or as a monitoring message confirming that replication is functioning properly. If this message follows an `RDS-EVENT-0045` notification, then replication has resumed following an error or after replication was stopped. | 
| read replica | RDS-EVENT-0057 | Replication streaming has been terminated. | None | 
| read replica | RDS-EVENT-0062 | Replication for the Read Replica has been manually stopped. | None | 
| read replica | RDS-EVENT-0063 | Replication from Non RDS instance has been reset. | None | 
| read replica | RDS-EVENT-0202 | Read replica creation failed. | None | 
| read replica | RDS-EVENT-0233 | The Switchover to the read replica started. | None | 
| read replica | RDS-EVENT-0357 | Replication channel {{name}} started. | For information about replication channels, see [Configuring multi-source-replication for Amazon RDS for MySQL](mysql-multi-source-replication.md). | 
| read replica | RDS-EVENT-0358 | Replication channel {{name}} stopped. | For information about replication channels, see [Configuring multi-source-replication for Amazon RDS for MySQL](mysql-multi-source-replication.md). | 
| read replica | RDS-EVENT-0359 | Replication channel {{name}} was manually stopped. | For information about replication channels, see [Configuring multi-source-replication for Amazon RDS for MySQL](mysql-multi-source-replication.md). | 
| read replica | RDS-EVENT-0360 | Replication channel {{name}} was reset. | For information about replication channels, see [Configuring multi-source-replication for Amazon RDS for MySQL](mysql-multi-source-replication.md). | 
| read replica | RDS-EVENT-0415 | The upgrade process resumed replication on the read replica. | None | 
| read replica | RDS-EVENT-0416 | The upgrade process stopped replication on the read replica. | None | 
| recovery | RDS-EVENT-0020 | Recovery of the DB instance has started. Recovery time will vary with the amount of data to be recovered. | None | 
| recovery | RDS-EVENT-0021 | Recovery of the DB instance is complete. | None | 
| recovery | RDS-EVENT-0023 | Emergent Snapshot Request: {{message}}. | A manual backup has been requested but Amazon RDS is currently in the process of creating a DB snapshot. Submit the request again after Amazon RDS has completed the DB snapshot. | 
| recovery | RDS-EVENT-0052 | Multi-AZ instance recovery started. | Recovery time will vary with the amount of data to be recovered. | 
| recovery | RDS-EVENT-0053 | Multi-AZ instance recovery completed. Pending failover or activation. | This message indicates that Amazon RDS has prepared your DB instance to initiate a failover to the secondary instance if necessary. | 
| recovery | RDS-EVENT-0066 | Instance will be degraded while mirroring is reestablished: {{message}}. | The SQL Server DB instance is re-establishing its mirror. Performance will be degraded until the mirror is reestablished. A database was found with non-FULL recovery model. The recovery model was changed back to FULL and mirroring recovery was started. (<dbname>: <recovery model found>[,...])" | 
| recovery | RDS-EVENT-0166 | {{message}} | The RDS Custom DB instance is inside the support perimeter. | 
| recovery | RDS-EVENT-0361 | Recovery of standby DB instance has started. | The standby DB instance is rebuilt during the recovery process. Database performance is impacted during the recovery process. | 
| recovery | RDS-EVENT-0362 | Recovery of standby DB instance has completed. | The standby DB instance is rebuilt during the recovery process. Database performance is impacted during the recovery process. | 
| restoration | RDS-EVENT-0019 | Restored from DB instance {{name}} to {{name}}. | The DB instance has been restored from a point-in-time backup. | 
| security | RDS-EVENT-0068 | Decrypting hsm partition password to update instance. | RDS is decrypting the AWS CloudHSM partition password to make updates to the DB instance. For more information see [Oracle Database Transparent Data Encryption (TDE) with AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/oracle-tde.html) in the *AWS CloudHSM User Guide*. | 
| security patching | RDS-EVENT-0230 | A system update is available for your DB instance. For information about applying updates, see 'Maintaining a DB instance' in the RDS User Guide. | A new Operating System update is available.<br />A new, minor version, operating system update is available for your DB instance. For information about applying updates, see [Operating system updates for RDS DB instances](USER_UpgradeDBInstance.Maintenance.md#OS_Updates). | 
| maintenance | RDS-EVENT-0425 | Amazon RDS can't perform the OS upgrade because there are no available IP addresses in the specified subnets. Choose subnets with available IP addresses and try again. | None | 
| maintenance | RDS-EVENT-0429 | Amazon RDS can't perform the OS upgrade because of insufficient capacity available for the {{type}} instance type in the {{zone}} Availability Zone | None | 
| maintenance | RDS-EVENT-0501 | Amazon RDS DB instance's server certificate requires rotation through a pending maintenance action. | DB instance's server certificate requires rotation through a pending maintenance action. Amazon RDS reboots your database during this maintenance to complete the certificate rotation. To schedule this maintenance, go to the **Maintenance & backups** tab and choose **Apply now** or **Schedule for next maintenance window**. If the change is not scheduled, Amazon RDS automatically applies it in your mainteance window on the auto apply date shown in your maintenance action. | 
| maintenance | RDS-EVENT-0502 | Amazon RDS has scheduled a server certificate rotation for DB instance during the next maintenance window. This maintenance will require a database reboot. | None | 

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

## DB snapshot events
<a name="USER_Events.Messages.snapshot"></a>

The following table shows the event category and a list of events when a DB snapshot is the source type.



- ** creation **
  - **RDS event ID:** RDS-EVENT-0040
  - **Message:** Creating manual snapshot.
  - **Notes:** None

- ** creation **
  - **RDS event ID:** RDS-EVENT-0042
  - **Message:** Manual snapshot created.
  - **Notes:** None

- ** creation **
  - **RDS event ID:** RDS-EVENT-0090
  - **Message:** Creating automated snapshot.
  - **Notes:** None

- ** creation **
  - **RDS event ID:** RDS-EVENT-0091
  - **Message:** Automated snapshot created.
  - **Notes:** None

- ** deletion **
  - **RDS event ID:** RDS-EVENT-0041
  - **Message:** Deleted user snapshot.
  - **Notes:** None

- ** notification **
  - **RDS event ID:** RDS-EVENT-0059
  - **Message:** Started copy of snapshot{{name}} from region {{name}}.
  - **Notes:** This is a cross-Region snapshot copy.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0060
  - **Message:** Finished copy of snapshot {{name}} from region {{name}} in {{number}} minutes.
  - **Notes:** This is a cross-Region snapshot copy.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0061
  - **Message:** Canceled snapshot copy request of {{name}} from region {{name}}.
  - **Notes:** This is a cross-Region snapshot copy.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0159
  - **Message:** The snapshot export task failed.
  - **Notes:** None

- ** notification **
  - **RDS event ID:** RDS-EVENT-0160
  - **Message:** The snapshot export task was canceled.
  - **Notes:** None

- ** notification **
  - **RDS event ID:** RDS-EVENT-0161
  - **Message:** The snapshot export task completed.
  - **Notes:** None

- ** notification **
  - **RDS event ID:** RDS-EVENT-0196
  - **Message:** Started copy of snapshot {{name}} in region {{name}}.
  - **Notes:** This is a local snapshot copy.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0197
  - **Message:** Finished copy of snapshot {{name}} in region {{name}}.
  - **Notes:** This is a local snapshot copy.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0190
  - **Message:** Canceled snapshot copy request of {{name}} in region {{name}}.
  - **Notes:** This is a local snapshot copy.

- ** restoration **
  - **RDS event ID:** RDS-EVENT-0043
  - **Message:** Restored from snapshot {{name}}.
  - **Notes:** A DB instance is being restored from a DB snapshot.

- ** failure **
  - **RDS event ID:** RDS-EVENT-0484
  - **Message:** Export task {{name}}: Table extraction failed for table {{name}} due to {{name}}. 
  - **Notes:** This event is not supported by faster export.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0486
  - **Message:** Export task {{name}}: Table {{name}} will be exported in a slower single-threaded mode. Please expect a delay in export completion.
  - **Notes:** This event is not supported by faster export.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0487
  - **Message:** Export task {{name}}: Table {{name}} is in progress, and the exported size is {{number}} GB.
  - **Notes:** This event will only be sent for tables taking more than 1 hour to complete.<br />This event is not supported by faster export.

- ** notification **
  - **RDS event ID:** RDS-EVENT-0488
  - **Message:** Export task {{name}} is at {{name}} stage. / **Notes:** None
  - **Message:** Export task {{name}}: Export progress is at {{number}}% with {{number}} table(s) in-progress and {{number}} table(s) finished. The total size of finished tables is {{number}} GB. / **Notes:** This event is not supported by faster export.



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

For more information about blue/green deployments, see [Using Amazon RDS Blue/Green Deployments for database updates](blue-green-deployments.md).


|  Category  | Amazon RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| creation | RDS-EVENT-0244 | Blue/green deployment tasks completed. You can make more modifications to the green environment databases or switch over the deployment. | None | 
| failure | RDS-EVENT-0245 | Creation of blue/green deployment failed because {{reason}}. | None | 
| deletion | RDS-EVENT-0246 | Blue/green deployment deleted. | None | 
| notification | RDS-EVENT-0247 | Switchover from {{blue}} to {{green}} started. | None | 
| notification | RDS-EVENT-0248 | Switchover completed on blue/green deployment. | None | 
| failure | RDS-EVENT-0249 | Switchover canceled on blue/green deployment. | None | 
| notification | RDS-EVENT-0250  | Switchover from primary/read replica {{blue}} to {{green}} started. | None | 
| notification | RDS-EVENT-0251  | Switchover from primary/read replica {{blue}} to {{green}} completed. Renamed {{blue}} to {{blue-old}} and {{green}} to {{blue}}. | None | 
| failure | RDS-EVENT-0252  | Switchover from primary/read replica {{blue}} to {{green}} was canceled due to {{reason}}. | None | 
| notification | RDS-EVENT-0307  | Sequence sync for switchover of {{blue}} to {{green}} has initiated. Switchover when using sequences may lead to extended downtime. | None | 
| notification | RDS-EVENT-0308  | Sequence sync for switchover of {{blue}} to {{green}} has completed. | None | 
| failure | RDS-EVENT-0310  | Sequence sync for switchover of {{blue}} to {{green}} was cancelled because sequences failed to sync. | None | 
| notification | RDS-EVENT-0405 | Your storage volumes are being initialized. | None | 
| notification | RDS-EVENT-0406 | Your storage volumes have been initialized. | None | 
| notification | RDS-EVENT-0409  | {{message}} | None | 

## Custom engine version events
<a name="USER_Events.Messages.CEV"></a>

The following table shows the event category and a list of events when a custom engine version is the source type.


|  Category  | Amazon RDS event ID |  Message  |  Notes  | 
| --- | --- | --- | --- | 
| creation | RDS-EVENT-0316 | Preparing to create custom engine version {{name}}. The entire creation process may take up to four hours to complete. | None | 
| creation | RDS-EVENT-0317 | Creating custom engine version {{name}}. | None | 
| creation | RDS-EVENT-0318 | Validating custom engine version {{name}}. | None | 
| creation | RDS-EVENT-0319 | Custom engine version {{name}} has been created successfully. | None | 
| creation | RDS-EVENT-0320 | RDS can't create custom engine version {{name}} because of an internal issue. We are addressing the problem and will contact you if necessary. For further assistance, contact [AWS Premium Support/](https://console.aws.amazon.com/support/). | None | 
| failure | RDS-EVENT-0198 | Creation failed for custom engine version {{name}}. {{message}} | The {{message}} includes details about the failure, such as missing files. | 
| failure | RDS-EVENT-0277 | Failure during deletion of custom engine version {{name}}. {{message}} | The {{message}} includes details about the failure. | 
| restoring | RDS-EVENT-0352 | The maximum database count supported for point-in-time restore has changed. | The {{message}} includes details about the event. | 