

# Performing common RMAN tasks for Oracle DB instances
<a name="Appendix.Oracle.CommonDBATasks.RMAN"></a>

In the following section, you can find how you can perform Oracle Recovery Manager (RMAN) DBA tasks on your Amazon RDS DB instances running Oracle. To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB instances. It also restricts access to certain system procedures and tables that require advanced privileges.

Use the Amazon RDS package `rdsadmin.rdsadmin_rman_util` to perform RMAN backups of your Amazon RDS for Oracle database to disk. The `rdsadmin.rdsadmin_rman_util` package supports full and incremental database file backups, tablespace backups, and archived redo log backups.

After an RMAN backup has finished, you can copy the backup files off the Amazon RDS for Oracle DB instance host. You might do this for the purpose of restoring to a non-RDS host or for long-term storage of backups. For example, you can copy the backup files to an Amazon S3 bucket. For more information, see using [Amazon S3 integration](oracle-s3-integration.md).

The backup files for RMAN backups remain on the Amazon RDS DB instance host until you remove them manually. You can use the `UTL_FILE.FREMOVE` Oracle procedure to remove files from a directory. For more information, see [FREMOVE procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/UTL_FILE.html) in the Oracle Database documentation.

You can't use the RMAN to restore RDS for Oracle DB instances. However, you can use RMAN to restore a backup to an on-premises or Amazon EC2 instance. For more information, see the blog article [Restore an Amazon RDS for Oracle instance to a self-managed instance](https://aws.amazon.com/blogs/database/restore-an-amazon-rds-for-oracle-instance-to-a-self-managed-instance/).

**Note**  
For backing up and restoring to another Amazon RDS for Oracle DB instance, you can continue to use the Amazon RDS backup and restore features. For more information, see [Backing up, restoring, and exporting data](CHAP_CommonTasks.BackupRestore.md).

**Topics**
+ [Prerequisites for RMAN backups](Appendix.Oracle.CommonDBATasks.RMAN-requirements.md)
+ [Common parameters for RMAN procedures](Appendix.Oracle.CommonDBATasks.CommonParameters.md)
+ [Validating database files in RDS for Oracle](Appendix.Oracle.CommonDBATasks.ValidateDBFiles.md)
+ [Enabling and disabling block change tracking](Appendix.Oracle.CommonDBATasks.BlockChangeTracking.md)
+ [Crosschecking archived redo logs](Appendix.Oracle.CommonDBATasks.Crosscheck.md)
+ [Backing up archived redo log files](Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.md)
+ [Performing a full database backup](Appendix.Oracle.CommonDBATasks.BackupDatabaseFull.md)
+ [Performing a full backup of a tenant database](Appendix.Oracle.CommonDBATasks.BackupTenantDatabaseFull.md)
+ [Performing an incremental database backup](Appendix.Oracle.CommonDBATasks.BackupDatabaseIncremental.md)
+ [Performing an incremental backup of a tenant database](Appendix.Oracle.CommonDBATasks.BackupTenantDatabaseIncremental.md)
+ [Backing up a tablespace](Appendix.Oracle.CommonDBATasks.BackupTablespace.md)
+ [Backing up a control file](Appendix.Oracle.CommonDBATasks.backup-control-file.md)
+ [Performing block media recovery](Appendix.Oracle.CommonDBATasks.block-media-recovery.md)