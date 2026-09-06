

# Working with tablespaces in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.TablespacesAndDatafiles"></a>

You can use tablespaces with RDS for Oracle, which is a logical storage unit that stores the database's data.

**Important**  
If your DB instance has replicas, we recommend using parameter group settings instead of session-level changes to manage default file locations. Session-level changes to default file locations in the primary instance are not automatically reflected in the replicas. Using parameter group settings ensures consistent file locations across your primary and replica instances.

**Topics**
+ [Specifying database file locations in RDS for Oracle](#Appendix.Oracle.CommonDBATasks.DatabaseFileLocations)
+ [Creating and sizing tablespaces in RDS for Oracle](#Appendix.Oracle.CommonDBATasks.CreatingTablespacesAndDatafiles)
+ [Creating tablespaces on additional storage volumes in RDS for Oracle](#Appendix.Oracle.CommonDBATasks.CreatingTablespacesWithFileLocations)
+ [Setting the default tablespace in RDS for Oracle](#Appendix.Oracle.CommonDBATasks.SettingDefaultTablespace)
+ [Setting the default temporary tablespace in RDS for Oracle](#Appendix.Oracle.CommonDBATasks.SettingDefTempTablespace)
+ [Creating a temporary tablespace on the instance store](#Appendix.Oracle.CommonDBATasks.creating-tts-instance-store)

## Specifying database file locations in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.DatabaseFileLocations"></a>

RDS for Oracle uses Oracle Managed Files (OMF) to name database files. When you create database files the database derives the setting based on the current setting of the `DB_CREATE_FILE_DEST` initialization parameter.

The default value of the `DB_CREATE_FILE_DEST` initialization parameter is `/rdsdbdata/db` for standalone databases and `/rdsdbdata/db/pdb` for containerized (CDB/MT) architecture. If your DB instance has additional storage volumes, then you can set `DB_CREATE_FILE_DEST` to your volume locations. For example, if your instance has a volume mounted on `/rdsdbdata/db`, you can set `DB_CREATE_FILE_DEST` to this value.

You can modify the `DB_CREATE_FILE_DEST` parameter at either the session level or Oracle database instance level.

### Modifying DB\_CREATE\_FILE\_DEST at the instance level
<a name="Appendix.Oracle.CommonDBATasks.InstanceLevelModification"></a>

To modify the parameter at the instance level, update the parameter in the parameter group assigned to your DB instance and apply it. For more information, see [RDS for Oracle initialization parameters](Oracle.Concepts.FeatureSupport.Parameters.md) and [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Modifying.md).

### Modifying DB\_CREATE\_FILE\_DEST at the session level
<a name="Appendix.Oracle.CommonDBATasks.SessionLevelModification"></a>

You can modify the parameter at the session level by executing an `ALTER SESSION` statement. This approach is useful when you want to create database files in a specific location for a particular session without affecting the entire instance.

The following example shows how to check the current parameter value and modify it for the session:

```
SHOW PARAMETER db_create_file_dest

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
db_create_file_dest                  string      /rdsdbdata/db

ALTER SESSION SET db_create_file_dest = '/rdsdbdata2/db';

Session altered.

SHOW PARAMETER db_create_file_dest

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
db_create_file_dest                  string      /rdsdbdata2/db
```

## Creating and sizing tablespaces in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.CreatingTablespacesAndDatafiles"></a>

When you create tablespaces, the database creates the data files in the storage volume specified by the `DB_CREATE_FILE_DEST` initialization parameter at the time of creation. By default, if you don't specify a data file size, tablespaces are created with the default of `AUTOEXTEND ON`, and no maximum size. In the following example, the tablespace {{users1}} is autoextensible.

```
CREATE TABLESPACE {{users1}};
```

Because of these default settings, tablespaces can grow to consume all allocated storage. We recommend that you specify an appropriate maximum size on permanent and temporary tablespaces, and that you carefully monitor space usage. 

The following example creates a tablespace named {{users2}} with a starting size of 1 gigabyte. Because a data file size is specified, but `AUTOEXTEND ON` isn't specified, the tablespace isn't autoextensible.

```
CREATE TABLESPACE {{users2}} DATAFILE SIZE {{1G}};
```

The following example creates a tablespace named {{users3}} with a starting size of 1 gigabyte, autoextend turned on, and a maximum size of 10 gigabytes.

```
CREATE TABLESPACE {{users3}} DATAFILE SIZE {{1G}} AUTOEXTEND ON MAXSIZE {{10G}};
```

The following example creates a temporary tablespace named {{temp01}}.

```
CREATE TEMPORARY TABLESPACE {{temp01}};
```

You can resize a bigfile tablespace by using `ALTER TABLESPACE`. You can specify the size in kilobytes (K), megabytes (M), gigabytes (G), or terabytes (T). The following example resizes a bigfile tablespace named {{users\_bf}} to 200 MB.

```
ALTER TABLESPACE {{users_bf}} RESIZE {{200M}};
```

The following example adds an additional data file to a smallfile tablespace named {{users\_sf}}.

```
ALTER TABLESPACE {{users_sf}} ADD DATAFILE SIZE {{100000M}} AUTOEXTEND ON NEXT {{250m}} MAXSIZE {{UNLIMITED}};
```

## Creating tablespaces on additional storage volumes in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.CreatingTablespacesWithFileLocations"></a>

To create a tablespace on an additional storage volume, modify the `DB_CREATE_FILE_DEST` parameter to the volume location. The following example sets the file location to `/rdsdbdata2/db`.

```
ALTER SESSION SET db_create_file_dest = '/rdsdbdata2/db';

Session altered.
```

In the following example, you create a tablespace on the additional volume `/rdsdbdata2/db`.

```
CREATE TABLESPACE new_tablespace DATAFILE SIZE 10G;

Tablespace created.

SELECT tablespace_name,file_id,file_name FROM dba_data_files
WHERE tablespace_name = 'NEW_TABLESPACE';

TABLESPACE_NAME              FILE_ID FILE_NAME
------------------------- ---------- --------------------------------------------------------------------------------
NEW_TABLESPACE                     7 /rdsdbdata2/db/ORCL_A/datafile/o1_mf_newtable_a123b4c5_.dbf
```

To create a smallfile tablespace and spread its data files across different storage volumes, add data files to the tablespace after you create it. In the following example, you create a tablespace with the data files in the default location of `/rdsdbdata/db`. Then you set the default destination to `/rdsdbdata2/db`. When you add a data file to your newly created tablespace, the database stores the file in `/rdsdbdata2/db`.

```
ALTER SESSION SET db_create_file_dest = '/rdsdbdata/db';

Session altered.

CREATE SMALLFILE TABLESPACE smalltbs DATAFILE SIZE 10G;

Tablespace created.

SELECT tablespace_name,file_id,file_name FROM dba_data_files
WHERE tablespace_name = 'SMALLTBS';

TABLESPACE_NAME              FILE_ID FILE_NAME
------------------------- ---------- --------------------------------------------------------------------------------
SMALLTBS                           8 /rdsdbdata/db/ORCL_A/datafile/o1_mf_smalltbs_n563yryk_.dbf

ALTER SESSION SET db_create_file_dest = '/rdsdbdata2/db';

Session altered.

ALTER TABLESPACE smalltbs ADD DATAFILE SIZE 10G;

Tablespace altered.

SELECT tablespace_name,file_id,file_name FROM dba_data_files
WHERE tablespace_name = 'SMALLTBS';

TABLESPACE_NAME              FILE_ID FILE_NAME
------------------------- ---------- --------------------------------------------------------------------------------
SMALLTBS                           8 /rdsdbdata/db/ORCL_A/datafile/o1_mf_smalltbs_n563yryk_.dbf
SMALLTBS                           9 /rdsdbdata2/db/ORCL_A/datafile/o1_mf_smalltbs_n564004g_.dbf
```

## Setting the default tablespace in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.SettingDefaultTablespace"></a>

To set the default tablespace, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.alter_default_tablespace`. The `alter_default_tablespace` procedure has the following parameters. 



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `tablespace_name` | varchar | — | Yes | The name of the default tablespace. | 

The following example sets the default tablespace to {{users2}}: 

```
EXEC rdsadmin.rdsadmin_util.alter_default_tablespace(tablespace_name => '{{users2}}');
```

To verify the default tablespace setting, run the following query:

```
SELECT PROPERTY_VALUE FROM DATABASE_PROPERTIES WHERE PROPERTY_NAME = 'DEFAULT_PERMANENT_TABLESPACE';
```

## Setting the default temporary tablespace in RDS for Oracle
<a name="Appendix.Oracle.CommonDBATasks.SettingDefTempTablespace"></a>

To set the default temporary tablespace, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.alter_default_temp_tablespace`. The `alter_default_temp_tablespace` procedure has the following parameters. 



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `tablespace_name` | varchar | — | Yes | The name of the default temporary tablespace. | 

The following example sets the default temporary tablespace to {{temp01}}. 

```
EXEC rdsadmin.rdsadmin_util.alter_default_temp_tablespace(tablespace_name => '{{temp01}}');
```

## Creating a temporary tablespace on the instance store
<a name="Appendix.Oracle.CommonDBATasks.creating-tts-instance-store"></a>

To create a temporary tablespace on the instance store, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.create_inst_store_tmp_tblspace`. The `create_inst_store_tmp_tblspace` procedure has the following parameters. 



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_tablespace_name` | varchar | — | Yes | The name of the temporary tablespace. | 

The following example creates the temporary tablespace {{temp01}} in the instance store. 

```
EXEC rdsadmin.rdsadmin_util.create_inst_store_tmp_tblspace(p_tablespace_name => '{{temp01}}');
```

**Important**  
When you run `rdsadmin_util.create_inst_store_tmp_tblspace`, the newly created temporary tablespace is not automatically set as the default temporary tablespace. To set it as the default, see [Setting the default temporary tablespace in RDS for Oracle](#Appendix.Oracle.CommonDBATasks.SettingDefTempTablespace).

For more information, see [Storing temporary data in an RDS for Oracle instance store](CHAP_Oracle.advanced-features.instance-store.md).