# Use cases for additional storage volumes in RDS for Oracle

Additional storage volumes support various database management scenarios.
The following sections describe common use cases and implementation approaches.

###### Topics

- [Extending storage capacity beyond 64 TiB](#User_Oracle_AdditionalStorage.UseCases.Extendingstoragecapacity "#User_Oracle_AdditionalStorage.UseCases.Extendingstoragecapacity")
- [Storage tiering of frequently and infrequently accessed data on separate volumes](#User_Oracle_AdditionalStorage.UseCases.Storagetiering "#User_Oracle_AdditionalStorage.UseCases.Storagetiering")
- [Temporary storage for data loading and unloading](#User_Oracle_AdditionalStorage.UseCases.Temporarystorage "#User_Oracle_AdditionalStorage.UseCases.Temporarystorage")
- [Using Oracle transportable tablespaces with an additional storage volume](#User_Oracle_AdditionalStorage.UseCases.TransportableTablespaces "#User_Oracle_AdditionalStorage.UseCases.TransportableTablespaces")

## Extending storage capacity beyond 64 TiB

You can use additional storage volumes when your primary storage volume approaches the
64 TiB limit but need more storage space in your database. You can attach additional storage
volumes to your DB instance, each up to 64TiB, using the `modify-db-instance` command. After
attaching additional storage volumes, you can create tablespaces on additional storage volumes
and move objects such as tables, indexes, and partitions to these tablespaces using standard Oracle SQL.
For more information, see [Database management operations with additional storage volumes in RDS for Oracle](User_Oracle_AdditionalStorage.md#User_Oracle_AdditionalStorage.DBManagement "User_Oracle_AdditionalStorage.md#User_Oracle_AdditionalStorage.DBManagement").

## Storage tiering of frequently and infrequently accessed data on separate volumes

You can use additional storage volumes to optimize cost and performance
by configuring different storage types between volumes. For example, you can use
high-performance Provisioned IOPS SSD storage (io2) volumes for frequently accessed
data while storing historical data on cost-effective General Purpose (gp3) storage volumes.
You can move specific database objects (tables, indexes, and partitions) to these
tablespaces using standard Oracle commands. For more information, see [Database management operations with additional storage volumes in RDS for Oracle](User_Oracle_AdditionalStorage.md#User_Oracle_AdditionalStorage.DBManagement "User_Oracle_AdditionalStorage.md#User_Oracle_AdditionalStorage.DBManagement").

## Temporary storage for data loading and unloading

You can use additional storage volumes as temporary storage for large data loads or exports with the following steps:

- Create a directory on an additional storage volume with the following command:

```
BEGIN
rdsadmin.rdsadmin_util.create_directory(
            p_directory_name => 'DATA_PUMP_DIR2',
            p_database_volume_name => 'rdsdbdata2');
END;
/
```

- After the creation of the directory, follow the steps described in [Importing using Oracle Data Pump](Oracle.Procedural.Importing.md "Oracle.Procedural.Importing.md") to export and import your data to the new directory.
- After the completion of the operation, remove files and optionally delete the volume to
  save the storage costs. You can remove the additional storage volume only when the volume is empty.

## Using Oracle transportable tablespaces with an additional storage volume

You can use additional storage volumes to move datafiles to an
additional storage volume using Oracle transportable tablespaces with the following steps:

- Set `db_create_file_dest` parameter at session level before importing
  transportable tablespaces into the target database with an additional storage volume.

```
ALTER SESSION SET db_create_file_dest = '/rdsdbdata2/db';

VAR x CLOB;

BEGIN
:x := rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces(
p_tablespace_list => 'TBTEST1',
p_directory_name => 'XTTS_DIR_DATA2',
p_platform_id => 13);
END;
/

PRINT :x;
```

- Check the transportable tablespace import status:

```
ALTER SESSION SET nls_date_format = 'DD.MM.YYYY HH24:MI:SS';

COL xtts_operation_start_utc FORMAT A30
COL xtts_operation_end_utc FORMAT A30
COL xtts_operation_state FORMAT A30
COL xtts_operation_type FORMAT A30

SELECT xtts_operation_start_utc, xtts_operation_type, xtts_operation_state
FROM rdsadmin.rds_xtts_operation_info;
```

- When transportable tablespace import completes, import transportable tablespace metadata.

```
BEGIN
rdsadmin.rdsadmin_transport_util.import_xtts_metadata(
p_datapump_metadata_file => 'xttdump.dmp',
p_directory_name => 'XTTS_DIR_DATA2');
END;
/
```
