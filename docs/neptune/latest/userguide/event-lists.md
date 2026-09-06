

# Amazon Neptune event categories and event messages
<a name="event-lists"></a>

Neptune generates a significant number of events in categories that you can subscribe to using the Neptune console. Each category applies to a source type, which can be a DB instance, DB snapshot, or DB parameter group.

**Note**  
Neptune uses existing Amazon RDS event definitions and IDs.

## Neptune events originating from DB instances
<a name="event-list-instance"></a>

The following table shows a list of events by event category when a DB instance is the source type.



- **availability**
  - **Amazon RDS event ID:** RDS-EVENT-0006 / **Description:** The DB instance restarted.
  - **Amazon RDS event ID:** RDS-EVENT-0004 / **Description:** DB instance shutdown.
  - **Amazon RDS event ID:** RDS-EVENT-0022 / **Description:** An error occurred while restarting the Neptune engine.

- **backup**
  - **Amazon RDS event ID:** RDS-EVENT-0001 / **Description:** Backing up DB instance.
  - **Amazon RDS event ID:** RDS-EVENT-0002 / **Description:** Finished DB Instance backup.

- **configuration change**
  - **Amazon RDS event ID:** RDS-EVENT-0009 / **Description:** The DB instance has been added to a security group.
  - **Amazon RDS event ID:** RDS-EVENT-0024 / **Description:** The DB instance is being converted to a Multi-AZ DB instance.
  - **Amazon RDS event ID:** RDS-EVENT-0030 / **Description:** The DB instance is being converted to a Single-AZ DB instance.
  - **Amazon RDS event ID:** RDS-EVENT-0012 / **Description:** Applying modification to database instance class. 
  - **Amazon RDS event ID:** RDS-EVENT-0018 / **Description:** The current storage settings for this DB instance are being changed.
  - **Amazon RDS event ID:** RDS-EVENT-0011 / **Description:** A parameter group for this DB instance has changed.
  - **Amazon RDS event ID:** RDS-EVENT-0092 / **Description:** A parameter group for this DB instance has finished updating.
  - **Amazon RDS event ID:** RDS-EVENT-0028 / **Description:** Automatic backups for this DB instance have been disabled.
  - **Amazon RDS event ID:** RDS-EVENT-0032 / **Description:** Automatic backups for this DB instance have been enabled.
  - **Amazon RDS event ID:** RDS-EVENT-0025 / **Description:** The DB instance has been converted to a Multi-AZ DB instance.
  - **Amazon RDS event ID:** RDS-EVENT-0029 / **Description:** The DB instance has been converted to a Single-AZ DB instance.
  - **Amazon RDS event ID:** RDS-EVENT-0014 / **Description:** The DB instance class for this DB instance has changed.
  - **Amazon RDS event ID:** RDS-EVENT-0017 / **Description:** The storage settings for this DB instance have changed.
  - **Amazon RDS event ID:** RDS-EVENT-0010 / **Description:** The DB instance has been removed from a security group.

- **creation**
  - **Amazon RDS event ID:** RDS-EVENT-0005
  - **Description:** DB instance created.

- **deletion**
  - **Amazon RDS event ID:** RDS-EVENT-0003
  - **Description:** The DB instance has been deleted.

- **failover**
  - **Amazon RDS event ID:** RDS-EVENT-0034 / **Description:** Neptune is not attempting a requested failover because a failover recently occurred on the DB instance.
  - **Amazon RDS event ID:** RDS-EVENT-0013 / **Description:** A Multi-AZ failover that resulted in the promotion of a standby instance has started.
  - **Amazon RDS event ID:** RDS-EVENT-0015 / **Description:** A Multi-AZ failover that resulted in the promotion of a standby instance is complete. It may take several minutes for the DNS to transfer to the new primary DB instance.
  - **Amazon RDS event ID:** RDS-EVENT-0065 / **Description:** The instance has recovered from a partial failover.
  - **Amazon RDS event ID:** RDS-EVENT-0049 / **Description:** A Multi-AZ failover has completed.
  - **Amazon RDS event ID:** RDS-EVENT-0050 / **Description:** A Multi-AZ activation has started after a successful instance recovery.
  - **Amazon RDS event ID:** RDS-EVENT-0051 / **Description:** A Multi-AZ activation is complete. Your database should be accessible now.
  - **Amazon RDS event ID:** RDS-EVENT-0031 / **Description:** The DB instance has failed due to an incompatible configuration or an underlying storage issue. Begin a point-in-time-restore for the DB instance.
  - **Amazon RDS event ID:** RDS-EVENT-0036 / **Description:** The DB instance is in an incompatible network. Some of the specified subnet IDs are invalid or do not exist.
  - **Amazon RDS event ID:** RDS-EVENT-0035 / **Description:** The DB instance has invalid parameters. For example, if the DB instance could not start because a memory-related parameter is set too high for this instance class, the customer action would be to modify the memory parameter and reboot the DB instance.
  - **Amazon RDS event ID:** RDS-EVENT-0082 / **Description:** Neptune was unable to copy backup data from an Amazon S3 bucket. It is likely that the permissions for Neptune to access the Amazon S3 bucket are configured incorrectly.

- **low storage**
  - **Amazon RDS event ID:** RDS-EVENT-0089 / **Description:** The DB instance has consumed more than 90% of its allocated storage. You can monitor the storage space for a DB instance using the **Free Storage Space** metric.
  - **Amazon RDS event ID:** RDS-EVENT-0007 / **Description:** The allocated storage for the DB instance has been exhausted. To resolve this issue, you should allocate additional storage for the DB instance.

- **maintenance**
  - **Amazon RDS event ID:** RDS-EVENT-0026 / **Description:** Offline maintenance of the DB instance is taking place. The DB instance is currently unavailable.
  - **Amazon RDS event ID:** RDS-EVENT-0027 / **Description:** Offline maintenance of the DB instance is complete. The DB instance is now available.
  - **Amazon RDS event ID:** RDS-EVENT-0047 / **Description:** Patching of the DB instance has completed.

- **notification**
  - **Amazon RDS event ID:** RDS-EVENT-0044 / **Description:** Operator-issued notification. For more information, see the event message.
  - **Amazon RDS event ID:** RDS-EVENT-0048 / **Description:** Patching of the DB instance has been delayed.
  - **Amazon RDS event ID:** RDS-EVENT-0087 / **Description:** The DB instance has been stopped. 
  - **Amazon RDS event ID:** RDS-EVENT-0088 / **Description:** The DB instance has been started.
  - **Amazon RDS event ID:** RDS-EVENT-0154 / **Description:** The DB instance is being started due to it exceeding the maximum allowed time being stopped.
  - **Amazon RDS event ID:** RDS-EVENT-0158 / **Description:** DB instance is in a state that can't be upgraded.
  - **Amazon RDS event ID:** RDS-EVENT-0173 / **Description:** DB instance has been patched.

- **read replica**
  - **Amazon RDS event ID:** RDS-EVENT-0045 / **Description:** An error has occurred in the read replication process. For more information, see the event message.
  - **Amazon RDS event ID:** RDS-EVENT-0046 / **Description:** The read replica has resumed replication. This message appears when you first create a read replica, or as a monitoring message confirming that replication is functioning properly. If this message follows an RDS-EVENT-0045 notification, then replication has resumed following an error or after replication was stopped.
  - **Amazon RDS event ID:** RDS-EVENT-0057 / **Description:** Replication on the read replica was terminated.
  - **Amazon RDS event ID:** RDS-EVENT-0062 / **Description:** Replication on the read replica was manually stopped.
  - **Amazon RDS event ID:** RDS-EVENT-0063 / **Description:** Replication on the read replica was reset.

- **recovery**
  - **Amazon RDS event ID:** RDS-EVENT-0020 / **Description:** Recovery of the DB instance has started. Recovery time will vary with the amount of data to be recovered.
  - **Amazon RDS event ID:** RDS-EVENT-0021 / **Description:** Recovery of the DB instance is complete.
  - **Amazon RDS event ID:** RDS-EVENT-0023 / **Description:** A manual backup has been requested but Neptune is currently in the process of creating a DB snapshot. Submit the request again after Neptune has completed the DB snapshot.
  - **Amazon RDS event ID:** RDS-EVENT-0052 / **Description:** Recovery of the Multi-AZ instance has started. Recovery time will vary with the amount of data to be recovered.
  - **Amazon RDS event ID:** RDS-EVENT-0053 / **Description:** Recovery of the Multi-AZ instance is complete.

- **restoration**
  - **Amazon RDS event ID:** RDS-EVENT-0008 / **Description:** The DB instance has been restored from a DB snapshot.
  - **Amazon RDS event ID:** RDS-EVENT-0019 / **Description:** The DB instance has been restored from a point-in-time backup.



## Neptune events originating from a DB cluster
<a name="event-list-cluster"></a>

The following table shows a list of events by event category when a DB cluster is the source type.



- **failover**
  - **RDS event ID:** RDS-EVENT-0069 / **Description:** A failover for the DB cluster has failed.
  - **RDS event ID:** RDS-EVENT-0070 / **Description:** A failover for the DB cluster has restarted.
  - **RDS event ID:** RDS-EVENT-0071 / **Description:** A failover for the DB cluster has finished.
  - **RDS event ID:** RDS-EVENT-0072 / **Description:** A failover for the DB cluster has begun within the same Availability Zone.
  - **RDS event ID:** RDS-EVENT-0073 / **Description:** A failover for the DB cluster has begun across Availability Zones.
  - **RDS event ID:** RDS-EVENT-0083 / **Description:** Neptune was unable to copy backup data from an Amazon S3 bucket. It is likely that the permissions for Neptune to access the Amazon S3 bucket are configured incorrectly.

- **maintenance**
  - **RDS event ID:** RDS-EVENT-0156
  - **Description:** The DB cluster has a DB engine minor version upgrade available.

- **notification**
  - **RDS event ID:** RDS-EVENT-0076 / **Description:** Migration to an Neptune DB cluster failed.
  - **RDS event ID:** RDS-EVENT-0077 / **Description:** An attempt to convert a table from the source database to database form failed during the migration to an Neptune DB cluster.
  - **RDS event ID:** RDS-EVENT-0150 / **Description:** The DB cluster stopped.
  - **RDS event ID:** RDS-EVENT-0151 / **Description:** The DB cluster started.
  - **RDS event ID:** RDS-EVENT-0152 / **Description:** The DB cluster stop failed.
  - **RDS event ID:** RDS-EVENT-0153 / **Description:** The DB cluster is being started due to it exceeding the maximum allowed time being stopped.



## Neptune events originating from DB cluster snapshot
<a name="event-list-cluster-snapshot"></a>

The following table shows the event category and a list of events when a Neptune DB cluster snapshot is the source type.


| Category | RDS event ID | Description | 
| --- | --- | --- | 
| backup | RDS-EVENT-0074 | Creation of a manual DB cluster snapshot has started. | 
| backup | RDS-EVENT-0075 | A manual DB cluster snapshot has been created. | 
| notification | RDS-EVENT-0162 | DB cluster snapshot export task failed. | 
| notification | RDS-EVENT-0163 | DB cluster snapshot export task canceled. | 
| notification | RDS-EVENT-0164 | DB cluster snapshot export task completed. | 
| backup | RDS-EVENT-0168 | Creating automated cluster snapshot. | 
| backup | RDS-EVENT-0169 | Automated cluster snapshot created. | 
| creation | RDS-EVENT-0170 | DB cluster created. | 
| deletion | RDS-EVENT-0171 | DB cluster deleted. | 
| notification | RDS-EVENT-0172 | Renamed DB cluster from [old DB cluster name] to [new DB cluster name]. | 

## Neptune events originating from DB cluster parameter group
<a name="event-list-parameter-group"></a>

The following table shows the event category and a list of events when a DB cluster parameter group is the source type.


| Category | RDS event ID | Description | 
| --- | --- | --- | 
| configuration change | RDS-EVENT-0037 | The parameter group was modified. | 

## Neptune events originating from a security group
<a name="event-list-security-group"></a>

The following table shows the event category and a list of events when a security group is the source type.


| Category | RDS event ID | Description | 
| --- | --- | --- | 
| configuration change | RDS-EVENT-0038 | The security group has been modified. | 
| failure | RDS-EVENT-0039 | The security group owned by [user] does not exist; authorization for the security group has been revoked. | 