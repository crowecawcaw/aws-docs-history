

# Administering your RDS for Oracle DB instance
<a name="Appendix.Oracle.CommonDBATasks"></a>

Following are the common management tasks that you perform with an RDS for Oracle DB instance. Some tasks are the same for all RDS DB instances. Other tasks are specific to RDS for Oracle.

The following tasks are common to all RDS databases, but Oracle Database has special considerations. For example, you connect to an Oracle database using the Oracle clients SQL\*Plus and SQL Developer.



| Task area | Relevant documentation | 
| --- | --- | 
| **Instance classes, storage, and PIOPS**<br />If you are creating a production instance, learn how instance classes, storage types, and Provisioned IOPS work in Amazon RDS.  | [RDS for Oracle DB instance classes](Oracle.Concepts.InstanceClasses.md)<br />[Amazon RDS storage types](CHAP_Storage.md#Concepts.Storage) | 
| **Multi-AZ deployments**<br />A production DB instance should use Multi-AZ deployments. Multi-AZ deployments provide increased availability, data durability, and fault tolerance for DB instances.  | [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.MultiAZ.md) | 
| **Amazon VPC**<br />If your AWS account has a default virtual private cloud (VPC), then your DB instance is automatically created inside the default VPC. If your account doesn't have a default VPC, and you want the DB instance in a VPC, create the VPC and subnet groups before you create the instance.  | [Working with a DB instance in a VPC](USER_VPC.WorkingWithRDSInstanceinaVPC.md) | 
| **Security groups**<br />By default, DB instances use a firewall that prevents access. Make sure that you create a security group with the correct IP addresses and network configuration to access the DB instance. | [Controlling access with security groups](Overview.RDSSecurityGroups.md) | 
| **Parameter groups**<br />If your DB instance is going to require specific database parameters, create a parameter group before you create the DB instance.  | [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md) | 
| **Option groups**<br />If your DB instance requires specific database options, create an option group before you create the DB instance.  | [Adding options to Oracle DB instances](Appendix.Oracle.Options.md) | 
| **Connecting to your DB instance**<br />After creating a security group and associating it to a DB instance, you can connect to the DB instance using any standard SQL client application such as Oracle SQL\*Plus.  | [Connecting to your Oracle DB instance](USER_ConnectToOracleInstance.md) | 
| **Backup and restore**<br />You can configure your DB instance to take automated backups, or take manual snapshots, and then restore instances from the backups or snapshots.  | [Backing up, restoring, and exporting data](CHAP_CommonTasks.BackupRestore.md) | 
| **Monitoring**<br />You can monitor an Oracle DB instance by using CloudWatch Amazon RDS metrics, events, and enhanced monitoring.  | [Viewing metrics in the Amazon RDS console](USER_Monitoring.md)<br />[Viewing Amazon RDS events](USER_ListEvents.md) | 
| **Log files**<br />You can access the log files for your Oracle DB instance.  | [Monitoring Amazon RDS log files](USER_LogAccess.md) | 

Following, you can find a description for Amazon RDS–specific implementations of common DBA tasks for RDS Oracle. To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB instances. Also, RDS restricts access to certain system procedures and tables that require advanced privileges. In many of the tasks, you run the `rdsadmin` package, which is an Amazon RDS–specific tool that enables you to administer your database.

The following are common DBA tasks for DB instances running Oracle:
+ [System tasks](Appendix.Oracle.CommonDBATasks.System.md)


<a name="dba-tasks-oracle-system-reference"></a>
<table>
<thead>
  <tr><th>Task</th><th>Method</th></tr>
</thead>
<tbody>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.DisconnectingSession.md">Disconnecting a session</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.disconnect</code><br />Oracle method: <code>alter system disconnect session</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.KillingSession.md">Terminating a session</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.kill</code><br />Oracle method: <code>alter system kill session</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.CancellingSQL.md">Canceling a SQL statement in a session</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.cancel</code><br />Oracle method: <code>alter system cancel sql</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.RestrictedSession.md">Enabling and disabling restricted sessions</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.restricted_session</code><br />Oracle method: <code>alter system enable restricted session</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.FlushingSharedPool.md">Flushing the shared pool</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.flush_shared_pool</code><br />Oracle method: <code>alter system flush shared_pool</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.FlushingSharedPool.md#Appendix.Oracle.CommonDBATasks.FlushingBufferCache">Flushing the buffer cache</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.flush_buffer_cache</code><br />Oracle method: <code>alter system flush buffer_cache</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.TransferPrivileges.md">Granting SELECT or EXECUTE privileges to SYS objects</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.grant_sys_object</code><br />Oracle method: <code>grant</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.RevokePrivileges.md">Revoking SELECT or EXECUTE privileges on SYS objects</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.revoke_sys_object</code><br />Oracle method: <code>revoke</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.X-dollar.md">Managing RDS_X$ views for Oracle DB instances</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.create_sys_x$_view</code><br />Oracle method: <code>CREATE VIEW</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.PermissionsNonMasters.md">Granting privileges to non-master users</a></td><td>Amazon RDS method: <code>grant</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.CustomPassword.md">Creating custom functions to verify passwords</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_password_verify.create_verify_function</code><br />Amazon RDS method: <code>rdsadmin.rdsadmin_password_verify.create_passthrough_verify_fcn</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.System.md#Appendix.Oracle.CommonDBATasks.CustomDNS">Setting up a custom DNS server</a></td><td>—</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.SystemEvents.md#Appendix.Oracle.CommonDBATasks.SystemEvents.listing">Listing allowed system diagnostic events</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.list_allowed_system_events</code><br />Oracle method: —</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.SystemEvents.md#Appendix.Oracle.CommonDBATasks.SystemEvents.setting">Setting system diagnostic events</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.set_allowed_system_events</code><br />Oracle method: <code>ALTER SYSTEM SET EVENTS 'set_event_clause'</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.SystemEvents.md#Appendix.Oracle.CommonDBATasks.SystemEvents.listing-set">Listing system diagnostic events that are set</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.list_set_system_events</code><br />Oracle method: <code>ALTER SESSION SET EVENTS 'IMMEDIATE EVENTDUMP(SYSTEM)'</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.SystemEvents.md#Appendix.Oracle.CommonDBATasks.SystemEvents.unsetting">Unsetting system diagnostic events</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.unset_system_event</code><br />Oracle method: <code>ALTER SYSTEM SET EVENTS 'unset_event_clause'</code></td></tr>
</tbody>
</table>


 
+ [Database tasks](Appendix.Oracle.CommonDBATasks.Database.md)


<a name="dba-tasks-oracle-database-reference"></a>
<table>
<thead>
  <tr><th>Task</th><th>Method</th></tr>
</thead>
<tbody>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.RenamingGlobalName.md">Changing the global name of a database</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.rename_global_name</code><br />Oracle method: <code>alter database rename</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.TablespacesAndDatafiles.md#Appendix.Oracle.CommonDBATasks.CreatingTablespacesAndDatafiles">Creating and sizing tablespaces in RDS for Oracle</a></td><td>Amazon RDS method: <code>create tablespace</code><br />Oracle method: <code>alter database</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.TablespacesAndDatafiles.md#Appendix.Oracle.CommonDBATasks.SettingDefaultTablespace">Setting the default tablespace in RDS for Oracle</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.alter_default_tablespace</code><br />Oracle method: <code>alter database default tablespace </code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.TablespacesAndDatafiles.md#Appendix.Oracle.CommonDBATasks.SettingDefTempTablespace">Setting the default temporary tablespace in RDS for Oracle</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.alter_default_temp_tablespace</code><br />Oracle method: <code>alter database default temporary tablespace </code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.TablespacesAndDatafiles.md#Appendix.Oracle.CommonDBATasks.creating-tts-instance-store">Creating a temporary tablespace on the instance store</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.create_inst_store_tmp_tblspace</code><br />Oracle method: <code>create temporary tablespace</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.CheckpointingDatabase.md">Checkpointing a database</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.checkpoint</code><br />Oracle method: <code>alter system checkpoint</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.SettingDistributedRecovery.md">Setting distributed recovery</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.enable_distr_recovery</code><br />Oracle method: <code>alter system enable distributed recovery</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.TimeZoneSupport.md">Setting the database time zone</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.alter_db_time_zone</code><br />Oracle method: <code>alter database set time_zone</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.External_Tables.md">Working with external tables in RDS for Oracle</a></td><td>—</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.AWR.md">Generating performance reports with Automatic Workload Repository (AWR)</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_diagnostic_util</code> procedures<br />Oracle method: <code>dbms_workload_repository</code> package</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.DBLinks.md">Adjusting database links for use with DB instances in a VPC</a></td><td>—</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.DefaultEdition.md">Setting the default edition for a DB instance</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.alter_default_edition</code><br />Oracle method: <code>alter database default edition</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.EnablingAuditing.md">Enabling auditing for the SYS.AUD$ table</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_master_util.audit_all_sys_aud_table</code><br />Oracle method: <code>audit</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.DisablingAuditing.md">Disabling auditing for the SYS.AUD$ table</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_master_util.noaudit_all_sys_aud_table</code><br />Oracle method: <code>noaudit</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.CleanupIndex.md">Cleaning up interrupted online index builds</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_dbms_repair.online_index_clean</code><br />Oracle method: <code>dbms_repair.online_index_clean</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.SkippingCorruptBlocks.md">Skipping corrupt blocks</a></td><td>Amazon RDS method: Several <code>rdsadmin.rdsadmin_dbms_repair</code> procedures<br />Oracle method: <code>dbms_repair</code> package</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.ResizeTempSpaceReadReplica.md">Resizing tablespaces, data files, and tempfiles in RDS for Oracle</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.resize_temp_tablespace</code>, <code>rdsadmin.rdsadmin_util.resize_tempfile</code>, or <code>rdsadmin.rdsadmin_util.autoextend_tempfile</code> procedures<br /><code>rdsadmin.rdsadmin_util.resize_datafile</code> or <code>rdsadmin.rdsadmin_util.autoextend_datafile</code> procedure<br />Oracle method: —</td></tr>
  <tr><td><a href="#Appendix.Oracle.CommonDBATasks.PurgeRecycleBin">Purging the recycle bin</a></td><td>Amazon RDS method: <code>EXEC rdsadmin.rdsadmin_util.purge_dba_recyclebin</code><br />Oracle method: <code>purge dba_recyclebin</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.FullRedaction.md">Setting the default displayed values for full redaction</a></td><td>Amazon RDS method: <code>EXEC rdsadmin.rdsadmin_util.dbms_redact_upd_full_rdct_val</code><br />Oracle method: <code>exec dbms_redact.UPDATE_FULL_REDACTION_VALUES</code></td></tr>
</tbody>
</table>


 
+ [Log tasks](Appendix.Oracle.CommonDBATasks.Log.md)


<a name="dba-tasks-oracle-log-reference"></a>
<table>
<thead>
  <tr><th>Task</th><th>Method</th></tr>
</thead>
<tbody>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Log.md#Appendix.Oracle.CommonDBATasks.SettingForceLogging">Setting force logging</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.force_logging</code><br />Oracle method: <code>alter database force logging</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Log.md#Appendix.Oracle.CommonDBATasks.AddingSupplementalLogging">Setting supplemental logging</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.alter_supplemental_logging</code><br />Oracle method: <code>alter database add supplemental log</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Log.md#Appendix.Oracle.CommonDBATasks.SwitchingLogfiles">Switching online log files</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.switch_logfile</code><br />Oracle method: <code>alter system switch logfile</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Log.md#Appendix.Oracle.CommonDBATasks.RedoLogs">Adding online redo logs</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.add_logfile</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Log.md#Appendix.Oracle.CommonDBATasks.DroppingRedoLogs">Dropping online redo logs</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.drop_logfile</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.ResizingRedoLogs.md">Resizing online redo logs</a></td><td>—</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.RetainRedoLogs.md">Retaining archived redo logs</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.set_configuration</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.download-redo-logs.md">Downloading archived redo logs from Amazon S3</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_archive_log_download.download_log_with_seqnum</code><br />Amazon RDS method: <code>rdsadmin.rdsadmin_archive_log_download.download_logs_in_seqnum_range</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Log.Download.md">Accessing online and archived redo logs</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_master_util.create_archivelog_dir</code><br />Amazon RDS method: <code>rdsadmin.rdsadmin_master_util.create_onlinelog_dir</code></td></tr>
</tbody>
</table>


 
+ [RMAN tasks](Appendix.Oracle.CommonDBATasks.RMAN.md)


<a name="dba-tasks-oracle-rman-reference"></a>
<table>
<thead>
  <tr><th>Task</th><th>Method</th></tr>
</thead>
<tbody>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.ValidateDBFiles.md">Validating database files in RDS for Oracle</a></td><td>Amazon RDS method: <code>rdsadmin_rman_util.procedure</code><br />Oracle method: <code>RMAN VALIDATE</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.BlockChangeTracking.md">Enabling and disabling block change tracking</a></td><td>Amazon RDS method: <code>rdsadmin_rman_util.procedure</code><br />Oracle method: <code>ALTER DATABASE</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Crosscheck.md">Crosschecking archived redo logs</a></td><td>Amazon RDS method: <code>rdsadmin_rman_util.crosscheck_archivelog</code><br />Oracle method: <code>RMAN BACKUP</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.md">Backing up archived redo log files</a></td><td>Amazon RDS method: <code>rdsadmin_rman_util.procedure</code><br />Oracle method: <code>RMAN BACKUP</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.BackupDatabaseFull.md">Performing a full database backup</a></td><td>Amazon RDS method: <code>rdsadmin_rman_util.backup_database_full</code><br />Oracle method: <code>RMAN BACKUP</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.BackupDatabaseIncremental.md">Performing an incremental database backup</a></td><td>Amazon RDS method: <code>rdsadmin_rman_util.backup_database_incremental</code><br />Oracle method: <code>RMAN BACKUP</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.BackupTablespace.md">Backing up a tablespace</a></td><td>Amazon RDS method: <code>rdsadmin_rman_util.backup_database_tablespace</code><br />Oracle method: <code>RMAN BACKUP</code></td></tr>
</tbody>
</table>


 
+ [Oracle Scheduler tasks](Appendix.Oracle.CommonDBATasks.Scheduler.md)


<a name="dba-tasks-oracle-scheduler-reference"></a>
<table>
<thead>
  <tr><th>Task</th><th>Method</th></tr>
</thead>
<tbody>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Scheduler.md#Appendix.Oracle.CommonDBATasks.ModifyScheduler">Modifying DBMS_SCHEDULER jobs</a></td><td>Amazon RDS method: <code>dbms_scheduler.set_attribute</code><br />Oracle method: <code>dbms_scheduler.set_attribute</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Scheduler.md#Appendix.Oracle.CommonDBATasks.Scheduler.maintenance-windows">Modifying AutoTask maintenance windows</a></td><td>Amazon RDS method: <code>dbms_scheduler.set_attribute</code><br />Oracle method: <code>dbms_scheduler.set_attribute</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Scheduler.md#Appendix.Oracle.CommonDBATasks.Scheduler.TimeZone">Setting the time zone for Oracle Scheduler jobs</a></td><td>Amazon RDS method: <code>dbms_scheduler.set_scheduler_attribute</code><br />Oracle method: <code>dbms_scheduler.set_scheduler_attribute</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Scheduler.md#Appendix.Oracle.CommonDBATasks.Scheduler.Disabling">Turning off Oracle Scheduler jobs owned by SYS</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_dbms_scheduler.disable</code><br />Oracle method: <code>dbms_scheduler.disable</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Scheduler.md#Appendix.Oracle.CommonDBATasks.Scheduler.Enabling">Turning on Oracle Scheduler jobs owned by SYS</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_dbms_scheduler.enable</code><br />Oracle method: <code>dbms_scheduler.enable</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Scheduler.md#Appendix.Oracle.CommonDBATasks.Scheduler.Modifying_Calendar">Modifying the Oracle Scheduler repeat interval for jobs of CALENDAR type</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_dbms_scheduler.set_attribute</code><br />Oracle method: <code>dbms_scheduler.set_attribute</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Scheduler.md#Appendix.Oracle.CommonDBATasks.Scheduler.Modifying_Named">Modifying the Oracle Scheduler repeat interval for jobs of NAMED type</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_dbms_scheduler.set_attribute</code><br />Oracle method: <code>dbms_scheduler.set_attribute</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Scheduler.md#Appendix.Oracle.CommonDBATasks.Scheduler.autocommit">Turning off autocommit for Oracle Scheduler job creation</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_dbms_scheduler.set_no_commit_flag</code><br />Oracle method: <code>dbms_isched.set_no_commit_flag</code></td></tr>
</tbody>
</table>


 
+ [Diagnosing problems](Appendix.Oracle.CommonDBATasks.Diagnostics.md)


<a name="dba-tasks-oracle-diagnostic-reference"></a>
<table>
<thead>
  <tr><th>Task</th><th>Method</th></tr>
</thead>
<tbody>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Diagnostics.md#Appendix.Oracle.CommonDBATasks.Incidents">Listing incidents</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_adrci_util.list_adrci_incidents</code><br />Oracle method: ADRCI command <code>show incident</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Diagnostics.md#Appendix.Oracle.CommonDBATasks.Problems">Listing problems</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_adrci_util.list_adrci_problem</code><br />Oracle method: ADRCI command <code>show problem</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Diagnostics.md#Appendix.Oracle.CommonDBATasks.IncPackages">Creating incident packages</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_adrci_util.create_adrci_package</code><br />Oracle method: ADRCI command <code>ips create package</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Diagnostics.md#Appendix.Oracle.CommonDBATasks.ShowTrace">Showing trace files</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_adrci_util.show_adrci_tracefile</code><br />Oracle method: ADRCI command <code>show tracefile</code></td></tr>
</tbody>
</table>


 
+ [Other tasks](Appendix.Oracle.CommonDBATasks.Misc.md)


<a name="dba-tasks-oracle-misc-reference"></a>
<table>
<thead>
  <tr><th>Task</th><th>Method</th></tr>
</thead>
<tbody>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.NewDirectories">Creating and dropping directories in the main data storage space</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.create_directory</code><br />Oracle method: <code>CREATE DIRECTORY</code><br />Amazon RDS method: <code>rdsadmin.rdsadmin_util.drop_directory</code><br />Oracle method: <code>DROP DIRECTORY</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.ListDirectories">Listing files in a DB instance directory</a></td><td>Amazon RDS method: <code>rdsadmin.rds_file_util.listdir</code><br />Oracle method: —</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.ReadingFiles">Reading files in a DB instance directory</a></td><td>Amazon RDS method: <code>rdsadmin.rds_file_util.read_text_file</code><br />Oracle method: —</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.accessing-opatch-files">Accessing Opatch files</a></td><td>Amazon RDS method: <code>rdsadmin.rds_file_util.read_text_file</code> or <code>rdsadmin.tracefile_listing</code><br />Oracle method: <code>opatch</code></td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.setting-task-parameters">Setting parameters for advisor tasks</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.advisor_task_set_parameter</code><br />Oracle method: Various stored package procedures</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.dropping-advisor-task">Disabling AUTO_STATS_ADVISOR_TASK</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.advisor_task_drop</code><br />Oracle method: —</td></tr>
  <tr><td><a href="Appendix.Oracle.CommonDBATasks.Misc.md#Appendix.Oracle.CommonDBATasks.recreating-advisor-task">Re-enabling AUTO_STATS_ADVISOR_TASK</a></td><td>Amazon RDS method: <code>rdsadmin.rdsadmin_util.dbms_stats_init</code><br />Oracle method: —</td></tr>
</tbody>
</table>


 

You can also use Amazon RDS procedures for Amazon S3 integration with Oracle and for running OEM Management Agent database tasks. For more information, see [Amazon S3 integration](oracle-s3-integration.md) and [Performing database tasks with the Management Agent](Oracle.Options.OEMAgent.md#Oracle.Options.OEMAgent.DBTasks).

## Purging the recycle bin
<a name="Appendix.Oracle.CommonDBATasks.PurgeRecycleBin"></a>

When you drop a table, your Oracle database doesn't immediately remove its storage space. The database renames the table and places it and any associated objects in a recycle bin. Purging the recycle bin removes these items and releases their storage space. 

To purge the entire recycle bin, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.purge_dba_recyclebin`. However, this procedure can't purge the recycle bin of `SYS` and `RDSADMIN` objects. If you need to purge these objects, contact AWS Support. 

The following example purges the entire recycle bin.

```
EXEC rdsadmin.rdsadmin_util.purge_dba_recyclebin;
```