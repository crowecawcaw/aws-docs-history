# RDS for Oracle releases

RDS for Oracle supports multiple Oracle Database releases.

###### Note

For information about upgrading your releases, see [Upgrading the RDS for Oracle DB engine](USER_UpgradeDBInstance.Oracle.md "USER_UpgradeDBInstance.Oracle.md").

###### Topics

- [Oracle Database 21c with Amazon RDS](#Oracle.Concepts.FeatureSupport.21c "#Oracle.Concepts.FeatureSupport.21c")
- [Oracle Database 19c with Amazon RDS](#Oracle.Concepts.FeatureSupport.19c "#Oracle.Concepts.FeatureSupport.19c")

## Oracle Database 21c with Amazon RDS

Amazon RDS supports Oracle Database 21c, which includes Oracle Enterprise Edition and Oracle Standard Edition 2.
Oracle Database 21c (21.0.0.0) includes many new features and updates from the previous version. A key change is that
Oracle Database 21c supports only the multitenant architecture: you can no longer create a database as a traditional
non-CDB. To learn more about the differences between CDBs and non-CDBs, see [Limitations of RDS for Oracle CDBs](Oracle.Concepts.CDBs.md#Oracle.Concepts.single-tenant-limitations "Oracle.Concepts.CDBs.md#Oracle.Concepts.single-tenant-limitations").

In this section, you can find the features and changes important to using Oracle Database 21c (21.0.0.0) on Amazon RDS.
For a complete list of the changes, see the [Oracle database 21c](https://docs.oracle.com/en/database/oracle/oracle-database/21/index.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/index.html")
documentation. For a complete list of features supported by each Oracle Database 21c edition, see [Permitted
features, options, and management packs by Oracle database offering](https://docs.oracle.com/en/database/oracle/oracle-database/21/dblic/Licensing-Information.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/dblic/Licensing-Information.html") in the Oracle documentation.

### Amazon RDS parameter changes for Oracle Database 21c (21.0.0.0)

Oracle Database 21c (21.0.0.0) includes several new parameters and parameters with new ranges and new default
values.

###### Topics

- [New parameters](#Oracle.Concepts.FeatureSupport.21c.parameters.new "#Oracle.Concepts.FeatureSupport.21c.parameters.new")
- [Changes for the compatible parameter](#Oracle.Concepts.FeatureSupport.21c.parameters.compatible "#Oracle.Concepts.FeatureSupport.21c.parameters.compatible")
- [Removed parameters](#Oracle.Concepts.FeatureSupport.21c.parameters.removed "#Oracle.Concepts.FeatureSupport.21c.parameters.removed")

#### New parameters

The following table shows the new Amazon RDS parameters for Oracle Database 21c (21.0.0.0).

| Name                                                                                                                                                                                                                                                                                                                              | Range of values                                                  | Default value               | Modifiable | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------ | ------ | ----------- | -------- | --- | ------------------------------------------------------------------------------- |
| [blockchain_table_max_no_drop](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/BLOCKCHAIN_TABLE_MAX_NO_DROP.html#GUID-26AF15B2-5621-4602-AA6E-D92842E4285C "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/BLOCKCHAIN_TABLE_MAX_NO_DROP.html#GUID-26AF15B2-5621-4602-AA6E-D92842E4285C") | `NONE                                                            | 0`                          | `NONE`     | Y                                                                                                                           | Lets you control the maximum amount of idle time that can be specified when creating a<br>blockchain table.                                                          |
| [dbnest_enable](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBNEST_ENABLE.html#GUID-2F30C9D3-808E-42CD-ADA6-595FAE518A60 "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBNEST_ENABLE.html#GUID-2F30C9D3-808E-42CD-ADA6-595FAE518A60")                                              | `NONE                                                            | CDB_RESOURCE_PDB_ALL`       | `NONE`     | N                                                                                                                           | Allows you to enable or disable dbNest. DbNest provides operating system resource<br>isolation and management, file system isolation, and secure computing for PDBs. |
| [dbnest_pdb_fs_conf](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBNEST_PDB_FS_CONF.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBNEST_PDB_FS_CONF.html")                                                                                                                   | `NONE                                                            | `pathname``                 | `NONE`     | N                                                                                                                           | Specifies the dbNest file system configuration file for a PDB.                                                                                                       |
| [diagnostics_control](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DIAGNOSTICS_CONTROL.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DIAGNOSTICS_CONTROL.html")                                                                                                                | `ERROR                                                           | WARNING                     | IGNORE`    | `IGNORE`                                                                                                                    | Y                                                                                                                                                                    | Allows you to control and monitor the users who perform potentially unsafe database<br>diagnostic operations. |
| [drcp_dedicated_opt](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DRCP_DEDICATED_OPT.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DRCP_DEDICATED_OPT.html")                                                                                                                   | `YES                                                             | NO`                         | `YES`      | Y                                                                                                                           | Enables or disables the use of dedicated optimization with Database Resident Connection<br>Pooling (DRCP).                                                           |
| [enable_per_pdb_drcp](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ENABLE_PER_PDB_DRCP.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ENABLE_PER_PDB_DRCP.html")                                                                                                                | `true                                                            | false`                      | `true`     | N                                                                                                                           | Controls whether Database Resident Connection Pooling (DRCP) configures one connection<br>pool for the entire CDB or one isolated connection pool for each PDB.      |
| [inmemory_deep_vectorization](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_DEEP_VECTORIZATION.html#GUID-59E87FDC-1DB4-4ACD-A807-D0C1AE44210D "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_DEEP_VECTORIZATION.html#GUID-59E87FDC-1DB4-4ACD-A807-D0C1AE44210D")    | `true                                                            | false`                      | `true`     | Y                                                                                                                           | Enables or disables deep vectorization for In-Memory column store scans.                                                                                             |
| [mandatory_user_profile](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MANDATORY_USER_PROFILE.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MANDATORY_USER_PROFILE.html")                                                                                                       | `profile_name`                                                   | N/A                         | N          | Specifies the mandatory user profile for a CDB or PDB.                                                                      |
| [optimizer_capture_sql_quarantine](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_CAPTURE_SQL_QUARANTINE.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_CAPTURE_SQL_QUARANTINE.html")                                                                         | `true                                                            | false`                      | `false`    | Y                                                                                                                           | Enables or disables the automatic creation of SQL Quarantine configurations.                                                                                         |
| [optimizer_use_sql_quarantine](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_USE_SQL_QUARANTINE.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_USE_SQL_QUARANTINE.html")                                                                                     | `true                                                            | false`                      | `false`    | Y                                                                                                                           | Enables or disables the use of SQL Quarantine configurations.                                                                                                        |
| [result_cache_execution_threshold](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_EXECUTION_THRESHOLD.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_EXECUTION_THRESHOLD.html")                                                                         | `0` to `68719476736`                                             | `2`                         | Y          | Specifies the maximum number of times a PL/SQL function can be executed before its<br>result is stored in the result cache. |
| [result_cache_max_temp_result](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_MAX_TEMP_RESULT.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_MAX_TEMP_RESULT.html")                                                                                     | `0` to `100`                                                     | `5`                         | Y          | Specifies the percentage of `RESULT_CACHE_MAX_TEMP_SIZE` that any single<br>cached query result can consume.                |
| [result_cache_max_temp_size](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_MAX_TEMP_SIZE.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_MAX_TEMP_SIZE.html")                                                                                           | `0` to `2199023255552`                                           | `RESULT_CACHE_SIZE<br>• 10` | Y          | Specifies the maximum amount of temporary tablespace (in bytes) that can be consumed by<br>the result cache.                |
| [sga_min_size](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SGA_MIN_SIZE.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SGA_MIN_SIZE.html")                                                                                                                                     | `0` to `2199023255552` (maximum value is 50% of<br>`sga_target`) | `0`                         | Y          | Indicates a possible minimum value for SGA usage of a pluggable database (PDB).                                             |
| [tablespace_encryption_default_algorithm](https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TABLESPACE_ENCRYPTION_DEFAULT_ALGORITHM.html "https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TABLESPACE_ENCRYPTION_DEFAULT_ALGORITHM.html")                                                    | `GOST256                                                         | SEED128                     | ARIA256    | ARIA192                                                                                                                     | ARIA128                                                                                                                                                              | 3DES168                                                                                                       | AES256 | AES192 | <br>AES128` | `AES128` | Y   | Specifies the default algorithm the database uses when encrypting a tablespace. |

#### Changes for the compatible parameter

The `compatible` parameter has a new maximum value for Oracle Database 21c (21.0.0.0) on Amazon RDS.
The following table shows the new default value.

| Parameter name                                                                                                                                                                                                                                                              | Oracle Database 21c (21.0.0.0) maximum value |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [compatible](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/COMPATIBLE.html#GUID-6C57EE11-BD06-4BB8-A0F7-D6CDDD086FA9 "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/COMPATIBLE.html#GUID-6C57EE11-BD06-4BB8-A0F7-D6CDDD086FA9") | 21.0.0                                       |

#### Removed parameters

The following parameters were removed in Oracle Database 21c (21.0.0.0):

- `remote_os_authent`
- `sec_case_sensitive_logon`
- `unified_audit_sga_queue_size`

## Oracle Database 19c with Amazon RDS

Amazon RDS supports Oracle Database 19c, which includes Oracle Enterprise Edition and Oracle Standard
Edition Two.

Oracle Database 19c (19.0.0.0) includes many new features and updates from the previous version. In
this section, you can find the features and changes important to using Oracle Database 19c (19.0.0.0) on
Amazon RDS. For a complete list of the changes, see the [Oracle database
19c](https://docs.oracle.com/en/database/oracle/oracle-database/19/index.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/index.html") documentation. For a complete list of features supported by each Oracle Database 19c
edition, see [Permitted features, options, and management packs by Oracle database offering](https://docs.oracle.com/en/database/oracle/oracle-database/19/dblic/Licensing-Information.html#GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87 "https://docs.oracle.com/en/database/oracle/oracle-database/19/dblic/Licensing-Information.html#GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87") in the Oracle
documentation.

### Amazon RDS parameter changes for Oracle Database 19c (19.0.0.0)

Oracle Database 19c (19.0.0.0) includes several new parameters and parameters with new ranges and
new default values.

###### Topics

- [New parameters](#Oracle.Concepts.FeatureSupport.19c.Parameters.new "#Oracle.Concepts.FeatureSupport.19c.Parameters.new")
- [Changes to the compatible parameter](#Oracle.Concepts.FeatureSupport.19c.Parameters.compatible "#Oracle.Concepts.FeatureSupport.19c.Parameters.compatible")
- [Removed parameters](#Oracle.Concepts.FeatureSupport.19c.Parameters.compatible.removed-parameters "#Oracle.Concepts.FeatureSupport.19c.Parameters.compatible.removed-parameters")

#### New parameters

The following table shows the new Amazon RDS parameters for Oracle Database 19c (19.0.0.0).

| Name                                                                                                                                                                                                                                                                                                                                 | Values                | Modifiable | Description                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | ---------- | -------------------------------------------------------------------------------------------- |
| [lob_signature_enable](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/lob_signature_enable.html#GUID-62997AB5-1084-4C9A-8258-8CB695C7A1D6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/lob_signature_enable.html#GUID-62997AB5-1084-4C9A-8258-8CB695C7A1D6")                            | TRUE, FALSE (default) | Y          | Enables or disables the LOB locator signature feature.                                       |
| [max_datapump_parallel_per_job](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MAX_DATAPUMP_PARALLEL_PER_JOB.html#GUID-33B1F962-B8C3-4DCE-BE68-66FC5D34ECA3 "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MAX_DATAPUMP_PARALLEL_PER_JOB.html#GUID-33B1F962-B8C3-4DCE-BE68-66FC5D34ECA3") | 1 to 1024, or AUTO    | Y          | Specifies the maximum number of parallel processes allowed for each Oracle Data Pump<br>job. |

#### Changes to the compatible parameter

The `compatible` parameter has a new maximum value for Oracle Database 19c (19.0.0.0) on Amazon RDS.
The following table shows the new default value.

| Parameter name                                                                                                                                                                                                                                                              | Oracle Database 19c (19.0.0.0) maximum value |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [compatible](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/COMPATIBLE.html#GUID-6C57EE11-BD06-4BB8-A0F7-D6CDDD086FA9 "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/COMPATIBLE.html#GUID-6C57EE11-BD06-4BB8-A0F7-D6CDDD086FA9") | 19.0.0                                       |

#### Removed parameters

The following parameters were removed in Oracle Database 19c (19.0.0.0):

- `exafusion_enabled`
- `max_connections`
- `o7_dictionary_access`
