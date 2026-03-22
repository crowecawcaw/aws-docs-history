# Setting up Oracle GoldenGate

To set up Oracle GoldenGate using Amazon RDS, configure the hub on an Amazon EC2 instance, and then configure the
source and target databases. The following sections give an example of how to set up Oracle GoldenGate
for use with Amazon RDS for Oracle.

###### Topics

- [Setting up an Oracle GoldenGate hub on Amazon EC2](#Appendix.OracleGoldenGate.Hub "#Appendix.OracleGoldenGate.Hub")
- [Setting up a source database for use with Oracle GoldenGate on Amazon RDS](#Appendix.OracleGoldenGate.Source "#Appendix.OracleGoldenGate.Source")
- [Setting up a target database for use with Oracle GoldenGate on Amazon RDS](#Appendix.OracleGoldenGate.Target "#Appendix.OracleGoldenGate.Target")

## Setting up an Oracle GoldenGate hub on Amazon EC2

To create an Oracle GoldenGate hub on an Amazon EC2 instance, you first create an Amazon EC2 instance with a full
client installation of Oracle RDBMS. The Amazon EC2 instance must also have Oracle GoldenGate software
installed. The Oracle GoldenGate software versions depend on the source and target database
versions. For more information about installing Oracle GoldenGate, see the [Oracle GoldenGate
documentation](https://docs.oracle.com/en/middleware/goldengate/core/index.html "https://docs.oracle.com/en/middleware/goldengate/core/index.html").

The Amazon EC2 instance that serves as the Oracle GoldenGate hub stores and processes the transaction
information from the source database into trail files. To support this process, make
sure that you meet the following requirements:

- You have allocated enough storage for the trail files.
- The Amazon EC2 instance has enough processing power to manage the amount of data.
- The EC2 instance has enough memory to store the transaction information before it's written to
  the trail file.

###### To set up an Oracle GoldenGate classic architecture hub on an Amazon EC2 instance

1. Create subdirectories in the Oracle GoldenGate directory.

In the Amazon EC2 command line shell, start `ggsci`, the Oracle GoldenGate command
interpreter. The `CREATE SUBDIRS` command creates subdirectories
under the `/gg` directory for parameter, report, and
checkpoint files.

```
prompt$ cd /gg
prompt$ ./ggsci

GGSCI> CREATE SUBDIRS
```

2. Configure the `mgr.prm` file.

The following example adds lines to the `$GGHOME/dirprm/mgr.prm`
file.

```
PORT 8199
PurgeOldExtracts ./dirdat/*, UseCheckpoints, MINKEEPDAYS 5
```

3. Start the manager.

The following example starts `ggsci` and runs the `start
 mgr` command.

```
GGSCI> start mgr
```

The Oracle GoldenGate hub is now ready for use.

## Setting up a source database for use with Oracle GoldenGate on Amazon RDS

Complete the following tasks to set up a source database for use with Oracle GoldenGate.

###### Setup steps

- [Step 1: Turn on supplemental logging on the source database](#Appendix.OracleGoldenGate.Source.Logging "#Appendix.OracleGoldenGate.Source.Logging")
- [Step 2: Set the ENABLE_GOLDENGATE_REPLICATION initialization parameter to true](#Appendix.OracleGoldenGate.Source.enable-gg-rep "#Appendix.OracleGoldenGate.Source.enable-gg-rep")
- [Step 3: Set the log retention period on the source database](#Appendix.OracleGoldenGate.Source.Retention "#Appendix.OracleGoldenGate.Source.Retention")
- [Step 4: Create an Oracle GoldenGate user account on the source database](#Appendix.OracleGoldenGate.Source.Account "#Appendix.OracleGoldenGate.Source.Account")
- [Step 5: Grant user account privileges on the source database](#Appendix.OracleGoldenGate.Source.Privileges "#Appendix.OracleGoldenGate.Source.Privileges")
- [Step 6: Add a TNS alias for the source database](#Appendix.OracleGoldenGate.Source.TNS "#Appendix.OracleGoldenGate.Source.TNS")

### Step 1: Turn on supplemental logging on the source database

To turn on the minimum database-level supplemental logging, run the following PL/SQL
procedure:

```
EXEC rdsadmin.rdsadmin_util.alter_supplemental_logging(p_action => 'ADD')
```

### Step 2: Set the ENABLE_GOLDENGATE_REPLICATION initialization parameter to true

When you set the `ENABLE_GOLDENGATE_REPLICATION` initialization parameter to
`true`, it allows database services to support logical replication.
If your source database is on an Amazon RDS DB instance, make sure that you have a parameter
group assigned to the DB instance with the `ENABLE_GOLDENGATE_REPLICATION`
initialization parameter set to `true`. For more information about the
`ENABLE_GOLDENGATE_REPLICATION` initialization parameter, see the
[Oracle Database documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ENABLE_GOLDENGATE_REPLICATION.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ENABLE_GOLDENGATE_REPLICATION.html").

### Step 3: Set the log retention period on the source database

Make sure that you configure the source database to retain archived redo logs. Consider
the following guidelines:

- Specify the duration for log retention in hours. The minimum value is one
  hour.
- Set the duration to exceed any potential downtime of the source DB
  instance, any potential period of communication, and any potential period of
  networking issues for the source instance. Such a duration lets Oracle GoldenGate
  recover logs from the source instance as needed.
- Ensure that you have sufficient storage on your instance for the
  files.

For example, set the retention period for archived redo logs to 24 hours.

```
EXEC rdsadmin.rdsadmin_util.set_configuration('archivelog retention hours',24)
```

If you don't have log retention enabled, or if the retention value is too small, you
receive an error message similar to the following.

```
2022-03-06 06:17:27  ERROR   OGG-00446  error 2 (No such file or directory)
opening redo log /rdsdbdata/db/GGTEST3_A/onlinelog/o1_mf_2_9k4bp1n6_.log for sequence 1306
Not able to establish initial position for begin time 2022-03-06 06:16:55.
```

Because your DB instance retains your archived redo logs, make sure that you have sufficient
space for the files. To see how much space you have used in the last
`num_hours` hours, run the following query, replacing
`num_hours` with the number of hours.

```
SELECT SUM(BLOCKS * BLOCK_SIZE) BYTES FROM V$ARCHIVED_LOG
   WHERE NEXT_TIME>=SYSDATE-`num_hours`/24 AND DEST_ID=1;
```

### Step 4: Create an Oracle GoldenGate user account on the source database

Oracle GoldenGate runs as a database user and requires the appropriate database privileges to access
the redo and archived redo logs for the source database. To provide these, create a
user account on the source database. For more information about the permissions for
an Oracle GoldenGate user account, see the [Oracle documentation](https://docs.oracle.com/en/middleware/goldengate/core/19.1/oracle-db/establishing-oracle-goldengate-credentials.html#GUID-79122058-27B0-4FB6-B3DC-B7D1B67EB053 "https://docs.oracle.com/en/middleware/goldengate/core/19.1/oracle-db/establishing-oracle-goldengate-credentials.html#GUID-79122058-27B0-4FB6-B3DC-B7D1B67EB053").

The following statements create a user account named `oggadm1`.

```
CREATE TABLESPACE administrator;
CREATE USER oggadm1  IDENTIFIED BY "`password`"
   DEFAULT TABLESPACE ADMINISTRATOR TEMPORARY TABLESPACE TEMP;
ALTER USER oggadm1 QUOTA UNLIMITED ON administrator;
```

###### Note

Specify a password other than the prompt shown here as a security best practice.

### Step 5: Grant user account privileges on the source database

In this task, you grant necessary account privileges for database users on your
source database.

###### To grant account privileges on the source database

1. Grant the necessary privileges to the Oracle GoldenGate user account using the SQL
   command `grant` and the `rdsadmin.rdsadmin_util`
   procedure `grant_sys_object`. The following statements grant
   privileges to a user named `oggadm1`.

```
GRANT CREATE SESSION, ALTER SESSION TO oggadm1;
GRANT RESOURCE TO oggadm1;
GRANT SELECT ANY DICTIONARY TO oggadm1;
GRANT FLASHBACK ANY TABLE TO oggadm1;
GRANT SELECT ANY TABLE TO oggadm1;
GRANT SELECT_CATALOG_ROLE TO `rds_master_user_name` WITH ADMIN OPTION;
EXEC rdsadmin.rdsadmin_util.grant_sys_object ('DBA_CLUSTERS', 'OGGADM1');
GRANT EXECUTE ON DBMS_FLASHBACK TO oggadm1;
GRANT SELECT ON SYS.V_$DATABASE TO oggadm1;
GRANT ALTER ANY TABLE TO oggadm1;
```

2. Grant the privileges needed by a user account to be an Oracle GoldenGate administrator. Run the
   following PL/SQL program.

```
EXEC rdsadmin.rdsadmin_dbms_goldengate_auth.grant_admin_privilege (
    grantee                 => 'OGGADM1',
    privilege_type          => 'capture',
    grant_select_privileges => true,
    do_grants               => TRUE);
```

To revoke privileges, use the procedure
`revoke_admin_privilege` in the same package.

### Step 6: Add a TNS alias for the source database

Add the following entry to `$ORACLE_HOME/network/admin/tnsnames.ora` in the
Oracle home to be used by the `EXTRACT` process. For more information on
the `tnsnames.ora` file, see the [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/netrf/local-naming-parameters-in-tns-ora-file.html#GUID-7F967CE5-5498-427C-9390-4A5C6767ADAA "https://docs.oracle.com/en/database/oracle/oracle-database/19/netrf/local-naming-parameters-in-tns-ora-file.html#GUID-7F967CE5-5498-427C-9390-4A5C6767ADAA").

```
OGGSOURCE=
   (DESCRIPTION=
        (ENABLE=BROKEN)
        (ADDRESS_LIST=
            (ADDRESS=(PROTOCOL=TCP)(HOST=goldengate-source.abcdef12345.us-west-2.rds.amazonaws.com)(PORT=8200)))
        (CONNECT_DATA=(SERVICE_NAME=ORCL))
    )
```

## Setting up a target database for use with Oracle GoldenGate on Amazon RDS

In this task, you set up a target DB instance for use with Oracle GoldenGate.

###### Setup steps

- [Step 1: Set the ENABLE_GOLDENGATE_REPLICATION initialization parameter to true](#Appendix.OracleGoldenGate.Target.enable-gg-rep "#Appendix.OracleGoldenGate.Target.enable-gg-rep")
- [Step 2: Create an Oracle GoldenGate user account on the target database](#Appendix.OracleGoldenGate.Target.User "#Appendix.OracleGoldenGate.Target.User")
- [Step 3: Grant account privileges on the target database](#Appendix.OracleGoldenGate.Target.Privileges "#Appendix.OracleGoldenGate.Target.Privileges")
- [Step 4: Add a TNS alias for the target database](#Appendix.OracleGoldenGate.Target.TNS "#Appendix.OracleGoldenGate.Target.TNS")

### Step 1: Set the ENABLE_GOLDENGATE_REPLICATION initialization parameter to true

When you set the `ENABLE_GOLDENGATE_REPLICATION` initialization
parameter is to `true`, it allows database services to support logical
replication. If your source database is on an Amazon RDS DB instance, make sure that you have a
parameter group assigned to the DB instance with the
`ENABLE_GOLDENGATE_REPLICATION` initialization parameter set to
`true`. For more information about the
`ENABLE_GOLDENGATE_REPLICATION` initialization parameter, see the
[Oracle Database documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ENABLE_GOLDENGATE_REPLICATION.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ENABLE_GOLDENGATE_REPLICATION.html").

### Step 2: Create an Oracle GoldenGate user account on the target database

Oracle GoldenGate runs as a database user and requires the appropriate database privileges. To make
sure it has these privileges, create a user account on the target database.

The following statement creates a user named `oggadm1`.

```
CREATE TABLESPSACE administrator;
CREATE USER oggadm1  IDENTIFIED BY "`password`"
   DEFAULT TABLESPACE administrator
   TEMPORARY TABLESPACE temp;
ALTER USER oggadm1 QUOTA UNLIMITED ON administrator;
```

###### Note

Specify a password other than the prompt shown here as a security best practice.

### Step 3: Grant account privileges on the target database

In this task, you grant necessary account privileges for database users on your target
database.

###### To grant account privileges on the target database

1. Grant necessary privileges to the Oracle GoldenGate user account on the target
   database. In the following example, you grant privileges to
   `oggadm1`.

```
GRANT CREATE SESSION        TO oggadm1;
GRANT ALTER SESSION         TO oggadm1;
GRANT CREATE CLUSTER        TO oggadm1;
GRANT CREATE INDEXTYPE      TO oggadm1;
GRANT CREATE OPERATOR       TO oggadm1;
GRANT CREATE PROCEDURE      TO oggadm1;
GRANT CREATE SEQUENCE       TO oggadm1;
GRANT CREATE TABLE          TO oggadm1;
GRANT CREATE TRIGGER        TO oggadm1;
GRANT CREATE TYPE           TO oggadm1;
GRANT SELECT ANY DICTIONARY TO oggadm1;
GRANT CREATE ANY TABLE      TO oggadm1;
GRANT ALTER ANY TABLE       TO oggadm1;
GRANT LOCK ANY TABLE        TO oggadm1;
GRANT SELECT ANY TABLE      TO oggadm1;
GRANT INSERT ANY TABLE      TO oggadm1;
GRANT UPDATE ANY TABLE      TO oggadm1;
GRANT DELETE ANY TABLE      TO oggadm1;
```

2. Grant the privileges needed by a user account to be an Oracle GoldenGate administrator. Run the
   following PL/SQL program.

```
EXEC rdsadmin.rdsadmin_dbms_goldengate_auth.grant_admin_privilege (
    grantee                 => 'OGGADM1',
    privilege_type          => 'apply',
    grant_select_privileges => true,
    do_grants               => TRUE);
```

To revoke privileges, use the procedure
`revoke_admin_privilege` in the same package.

### Step 4: Add a TNS alias for the target database

Add the following entry to `$ORACLE_HOME/network/admin/tnsnames.ora` in the
Oracle home to be used by the `REPLICAT` process. For Oracle Multitenant
databases, make sure that the TNS alias points to the service name of the PDB. For
more information on the `tnsnames.ora` file, see the [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/netrf/local-naming-parameters-in-tns-ora-file.html#GUID-7F967CE5-5498-427C-9390-4A5C6767ADAA "https://docs.oracle.com/en/database/oracle/oracle-database/19/netrf/local-naming-parameters-in-tns-ora-file.html#GUID-7F967CE5-5498-427C-9390-4A5C6767ADAA").

```
OGGTARGET=
    (DESCRIPTION=
        (ENABLE=BROKEN)
        (ADDRESS_LIST=
            (ADDRESS=(PROTOCOL=TCP)(HOST=goldengate-target.abcdef12345.us-west-2.rds.amazonaws.com)(PORT=8200)))
        (CONNECT_DATA=(SERVICE_NAME=ORCL))
    )
```
