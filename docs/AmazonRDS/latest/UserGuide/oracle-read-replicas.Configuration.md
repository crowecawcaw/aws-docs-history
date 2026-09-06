

# Preparing to create an Oracle replica
<a name="oracle-read-replicas.Configuration"></a>

Before you can begin using your replica, perform the following tasks.

**Topics**
+ [Enabling automatic backups](#oracle-read-replicas.configuration.autobackups)
+ [Enabling force logging mode](#oracle-read-replicas.configuration.force-logging)
+ [Changing your logging configuration](#oracle-read-replicas.configuration.logging-config)
+ [Setting the MAX\_STRING\_SIZE parameter](#oracle-read-replicas.configuration.string-size)
+ [Planning compute and storage resources](#oracle-read-replicas.configuration.planning-resources)

## Enabling automatic backups
<a name="oracle-read-replicas.configuration.autobackups"></a>

Before a DB instance can serve as a source DB instance, make sure to enable automatic backups on the source DB instance. To learn how to perform this procedure, see [Enabling automated backups](USER_WorkingWithAutomatedBackups.Enabling.md).

## Enabling force logging mode
<a name="oracle-read-replicas.configuration.force-logging"></a>

We recommend that you enable force logging mode. In force logging mode, the Oracle database writes redo records even when `NOLOGGING` is used with data definition language (DDL) statements.

**To enable force logging mode**

1. Log in to your Oracle database using a client tool such as SQL Developer.

1. Enable force logging mode by running the following procedure. 

   ```
   exec rdsadmin.rdsadmin_util.force_logging(p_enable => true);
   ```

For more information about this procedure, see [Setting force logging](Appendix.Oracle.CommonDBATasks.Log.md#Appendix.Oracle.CommonDBATasks.SettingForceLogging).

## Changing your logging configuration
<a name="oracle-read-replicas.configuration.logging-config"></a>

For *n* online redo logs of size *m*, RDS automatically creates *n*\+1 standby logs of size *m* on the primary DB instance and all replicas. Whenever you change the logging configuration on the primary, the changes propagate automatically to the replicas. 

If you change your logging configuration, consider the following guidelines:
+ We recommend that you complete the changes before making a DB instance the source for replicas. RDS for Oracle also supports updating the instance after it becomes a source.
+ Before you change the logging configuration on the primary DB instance, check that each replica has enough storage to accommodate the new configuration. 

You can modify the logging configuration for a DB instance by using the Amazon RDS procedures `rdsadmin.rdsadmin_util.add_logfile` and `rdsadmin.rdsadmin_util.drop_logfile`. For more information, see [Adding online redo logs](Appendix.Oracle.CommonDBATasks.Log.md#Appendix.Oracle.CommonDBATasks.RedoLogs) and [Dropping online redo logs](Appendix.Oracle.CommonDBATasks.Log.md#Appendix.Oracle.CommonDBATasks.DroppingRedoLogs).

## Setting the MAX\_STRING\_SIZE parameter
<a name="oracle-read-replicas.configuration.string-size"></a>

Before you create an Oracle replica, ensure that the setting of the `MAX_STRING_SIZE` parameter is the same on the source DB instance and the replica. You can do this by associating them with the same parameter group. If you have different parameter groups for the source and the replica, you can set `MAX_STRING_SIZE` to the same value. For more information about setting this parameter, see [Turning on extended data types for a new DB instance](Oracle.Concepts.ExtendedDataTypes.md#Oracle.Concepts.ExtendedDataTypes.CreateDBInstance).

## Planning compute and storage resources
<a name="oracle-read-replicas.configuration.planning-resources"></a>

Ensure that the source DB instance and its replicas are sized properly, in terms of compute and storage, to suit their operational load. If a replica reaches compute, network, or storage resource capacity, the replica stops receiving or applying changes from its source. Amazon RDS for Oracle doesn't intervene to mitigate high replica lag between a source DB instance and its replicas. You can modify the storage and CPU resources of a replica independently from its source and other replicas.