

# Functions and stored procedures for Amazon RDS for Microsoft SQL Server
<a name="SQLServer.Concepts.General.StoredProcedures"></a>

Following, you can find a list of the Amazon RDS functions and stored procedures that help automate SQL Server tasks. 



- **Administrative tasks**
  - **Procedure or function:** `rds_drop_database` / **Where it's used:** [Dropping a database in an Amazon RDS for Microsoft SQL Server DB instance](Appendix.SQLServer.CommonDBATasks.DropMirrorDB.md)
  - **Procedure or function:** `rds_failover_time` / **Where it's used:** [Determining the last failover time for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.LastFailover.md)
  - **Procedure or function:** rds\_manage\_view\_db\_permission / **Where it's used:** [Deny or allow viewing database names for Amazon RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.ManageView.md)
  - **Procedure or function:** `rds_modify_db_name` / **Where it's used:** [Renaming a Amazon RDS for Microsoft SQL Server database in a Multi-AZ deployment](Appendix.SQLServer.CommonDBATasks.RenamingDB.md)
  - **Procedure or function:** `rds_read_error_log` / **Where it's used:** [Viewing error and agent logs](Appendix.SQLServer.CommonDBATasks.Logs.md#Appendix.SQLServer.CommonDBATasks.Logs.SP)
  - **Procedure or function:** `rds_set_configuration` / **Where it's used:** This operation is used to set various DB instance configurations:+  [Change data capture for Multi-AZ instances](Appendix.SQLServer.CommonDBATasks.CDC.md#Appendix.SQLServer.CommonDBATasks.CDC.Multi-AZ) <br />+  [Setting the retention period for trace and dump files](Appendix.SQLServer.CommonDBATasks.TraceFiles.md#Appendix.SQLServer.CommonDBATasks.TraceFiles.PurgeTraceFiles) <br />+  [Compressing backup files](SQLServer.Procedural.Importing.Native.Compression.md) 
  - **Procedure or function:** `rds_set_database_online` / **Where it's used:** [Transitioning a Amazon RDS for SQL Server database from OFFLINE to ONLINE](Appendix.SQLServer.CommonDBATasks.TransitionOnline.md)
  - **Procedure or function:** `rds_set_system_database_sync_objects`<br />`rds_fn_get_system_database_sync_objects`<br />`rds_fn_server_object_last_sync_time` / **Where it's used:** [Turning on SQL Server Agent job replication](Appendix.SQLServer.CommonDBATasks.Agent.md#SQLServerAgent.Replicate)
  - **Procedure or function:** `rds_show_configuration` / **Where it's used:** To see the values that are set using `rds_set_configuration`, see these topics:+  [Change data capture for Multi-AZ instances](Appendix.SQLServer.CommonDBATasks.CDC.md#Appendix.SQLServer.CommonDBATasks.CDC.Multi-AZ) <br />+  [Setting the retention period for trace and dump files](Appendix.SQLServer.CommonDBATasks.TraceFiles.md#Appendix.SQLServer.CommonDBATasks.TraceFiles.PurgeTraceFiles) 
  - **Procedure or function:** `rds_shrink_tempdbfile` / **Where it's used:** [Shrinking the tempdb database](SQLServer.TempDB.Shrinking.md)

- **Change data capture (CDC)**
  - **Procedure or function:** `rds_cdc_disable_db` / **Where it's used:** [Disabling CDC](Appendix.SQLServer.CommonDBATasks.CDC.md)
  - **Procedure or function:** `rds_cdc_enable_db` / **Where it's used:** [Enabling CDC](Appendix.SQLServer.CommonDBATasks.CDC.md)

- **Database Mail**
  - **Procedure or function:** `rds_fn_sysmail_allitems` / **Where it's used:** [Viewing messages, logs, and attachments](SQLServer.DBMail.View.md)
  - **Procedure or function:** `rds_fn_sysmail_event_log` / **Where it's used:** [Viewing messages, logs, and attachments](SQLServer.DBMail.View.md)
  - **Procedure or function:** `rds_fn_sysmail_mailattachments` / **Where it's used:** [Viewing messages, logs, and attachments](SQLServer.DBMail.View.md)
  - **Procedure or function:** `rds_sysmail_control` / **Where it's used:** This operation is used in starting and stopping the mail queue:+  [Starting the mail queue](SQLServer.DBMail.StartStop.md#SQLServer.DBMail.Start) <br />+  [Stopping the mail queue](SQLServer.DBMail.StartStop.md#SQLServer.DBMail.Stop) 
  - **Procedure or function:** `rds_sysmail_delete_mailitems_sp` / **Where it's used:** [Deleting messages](SQLServer.DBMail.Delete.md)

- **Native backup and restore**
  - **Procedure or function:** `rds_backup_database` / **Where it's used:** [Backing up a database](SQLServer.Procedural.Importing.Native.Using.md#SQLServer.Procedural.Importing.Native.Using.Backup)
  - **Procedure or function:** `rds_cancel_task` / **Where it's used:** [Canceling a task](SQLServer.Procedural.Importing.Native.Using.md#SQLServer.Procedural.Importing.Native.Using.Cancel)
  - **Procedure or function:** `rds_finish_restore` / **Where it's used:** [Finishing a database restore](SQLServer.Procedural.Importing.Native.Using.md#SQLServer.Procedural.Importing.Native.Finish.Restore)
  - **Procedure or function:** `rds_restore_database` / **Where it's used:** [Restoring a database](SQLServer.Procedural.Importing.Native.Using.md#SQLServer.Procedural.Importing.Native.Using.Restore)
  - **Procedure or function:** `rds_restore_log` / **Where it's used:** [Restoring a log](SQLServer.Procedural.Importing.Native.Using.md#SQLServer.Procedural.Importing.Native.Restore.Log)

- **Amazon S3 file transfer**
  - **Procedure or function:** `rds_delete_from_filesystem` / **Where it's used:** [Deleting files on the RDS DB instance](Appendix.SQLServer.Options.S3-integration.using.deleting-files.md)
  - **Procedure or function:** `rds_download_from_s3` / **Where it's used:** [Downloading files from an Amazon S3 bucket to a SQL Server DB instance](Appendix.SQLServer.Options.S3-integration.using.md#Appendix.SQLServer.Options.S3-integration.using.download)
  - **Procedure or function:** `rds_gather_file_details` / **Where it's used:** [Listing files on the RDS DB instance](Appendix.SQLServer.Options.S3-integration.using.listing-files.md)
  - **Procedure or function:** `rds_upload_to_s3` / **Where it's used:** [Uploading files from a SQL Server DB instance to an Amazon S3 bucket](Appendix.SQLServer.Options.S3-integration.using.md#Appendix.SQLServer.Options.S3-integration.using.upload)

- **Microsoft Distributed Transaction Coordinator (MSDTC)**
  - **Procedure or function:** `rds_msdtc_transaction_tracing`
  - **Where it's used:** [Using transaction tracing](Appendix.SQLServer.Options.MSDTC.md#MSDTC.Tracing)

- **SQL Server Audit**
  - **Procedure or function:** `rds_fn_get_audit_file`
  - **Where it's used:** [Viewing audit logs](Appendix.SQLServer.Options.Audit.AuditRecords.md)

- **Transparent Data Encryption**
  - **Procedure or function:** `rds_backup_tde_certificate`<br />`rds_drop_tde_certificate`<br />`rds_restore_tde_certificate`<br />`rds_fn_list_user_tde_certificates`
  - **Where it's used:** [Support for Transparent Data Encryption in SQL Server](Appendix.SQLServer.Options.TDE.md)

- **Microsoft Business Intelligence (MSBI)**
  - **Procedure or function:** `rds_msbi_task` / **Where it's used:** This operation is used with SQL Server Analysis Services (SSAS):+  [Deploying SSAS projects on Amazon RDS](SSAS.Deploy.md) <br />+  [Adding a domain user as a database administrator](SSAS.Use.md#SSAS.Admin) <br />+  [Backing up an SSAS database](SSAS.Backup.md) <br />+  [Restoring an SSAS database](SSAS.Restore.md) <br />This operation is also used with SQL Server Integration Services (SSIS):+  [Administrative permissions on SSISDB](SSIS.Permissions.md) <br />+  [Deploying an SSIS project](SSIS.Deploy.md) <br />SQL Server Reporting Services (SSRS) and Power BI Report Server (PBIRS) also use this operation:+  [Granting access to domain users](SSRS.Access.md#SSRS.Access.Grant) <br />+  [Revoking system-level permissions](SSRS.Access.Revoke.md) 
  - **Procedure or function:** `rds_fn_task_status` / **Where it's used:** This operation shows the status of MSBI tasks:+  SSAS: [Monitoring the status of a deployment task](SSAS.Monitor.md) <br />+  SSIS: [Monitoring the status of a deployment task](SSIS.Monitor.md) <br />+  SSRS: [Monitoring the status of a task](SSRS.Monitor.md) 

- **SSIS**
  - **Procedure or function:** `rds_drop_ssis_database` / **Where it's used:** [Dropping the SSISDB database](SSIS.DisableDrop.md#SSIS.Drop)
  - **Procedure or function:** `rds_sqlagent_proxy` / **Where it's used:** [Creating an SSIS proxy](SSIS.Use.md#SSIS.Use.Proxy)

- **SSRS and PBIRS**
  - **Procedure or function:** `rds_drop_ssrs_databases`
  - **Where it's used:** [Deleting the SSRS or PBIRS databases](SSRS.DisableDelete.md#SSRS.Drop)

- **Resource Governor**
  - **Procedure or function:** `rds_create_resource_pool` / **Where it's used:** [Create resource Pool](ResourceGovernor.Using.md#ResourceGovernor.CreateResourcePool)
  - **Procedure or function:** `rds_alter_resource_pool` / **Where it's used:** [Alter resource pool](ResourceGovernor.Using.md#ResourceGovernor.AlterResourcePool)
  - **Procedure or function:** `rds_drop_resource_pool` / **Where it's used:** [Drop resource pool](ResourceGovernor.Using.md#ResourceGovernor.DropResourcePool)
  - **Procedure or function:** `rds_create_workload_group` / **Where it's used:** [Create workload group](ResourceGovernor.Using.md#ResourceGovernor.CreateWorkloadGroup)
  - **Procedure or function:** `rds_alter_workload_group` / **Where it's used:** [Alter workload group](ResourceGovernor.Using.md#ResourceGovernor.AlterWorkloadGroup)
  - **Procedure or function:** `rds_drop_workload_group` / **Where it's used:** [Drop workload group](ResourceGovernor.Using.md#ResourceGovernor.DropWorkloadGroup)
  - **Procedure or function:** `rds_create_classifier_function` / **Where it's used:** [Create and register classifier function](ResourceGovernor.Using.md#ResourceGovernor.ClassifierFunction)
  - **Procedure or function:** `rds_drop_classifier_function` / **Where it's used:** [Drop classifier function](ResourceGovernor.Using.md#ResourceGovernor.DropClassifier)
  - **Procedure or function:** `rds_alter_resource_governor_configuration` / **Where it's used:** [Resource governor configuration changes](ResourceGovernor.Using.md#ResourceGovernor.ConfigChanges)
  - **Procedure or function:** `rds_bind_tempdb_metadata_to_resource_pool` / **Where it's used:** [Bind TempDB to a resource pool](ResourceGovernor.Using.md#ResourceGovernor.BindTempDB)
  - **Procedure or function:** `rds_unbind_tempdb_metadata_from_resource_pool` / **Where it's used:** [Unbind TempDB from a resource pool](ResourceGovernor.Using.md#ResourceGovernor.UnbindTempDB)
  - **Procedure or function:** `rds_cleanup_resource_governor` / **Where it's used:** [Cleanup resource governor](ResourceGovernor.Using.md#ResourceGovernor.Cleanup)

