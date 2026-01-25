# Working with container databases (CDBs) in

RDS Custom for Oracle

You can either create your RDS Custom for Oracle DB instance with the Oracle multitenant architecture
(`custom-oracle-ee-cdb` or `custom-oracle-se2-cdb` engine type) or
with the traditional non-CDB architecture (`custom-oracle-ee` or
`custom-oracle-se2` engine type). When you create a container database (CDB), it
contains one pluggable database (PDB) and one PDB seed. You can create additional PDBs manually
using Oracle SQL.

## PDB and CDB names

When you create an RDS Custom for Oracle CDB instance, you specify a name for the initial PDB. By
default, your initial PDB is named `ORCL`. You can choose a different name.

By default, your CDB is named `RDSCDB`. You can choose a different name. The CDB
name is also the name of your Oracle system identifier (SID), which uniquely identifies
the memory and processes that manage your CDB. For more information about the Oracle SID, see
[Oracle System Identifier (SID)](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/oracle-database-instance.html#GUID-8BB8140D-63ED-454E-AAC3-1964F80D102D "https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/oracle-database-instance.html#GUID-8BB8140D-63ED-454E-AAC3-1964F80D102D") in _Oracle Database
Concepts_.

You can't rename existing PDBs using Amazon RDS APIs. You also can't rename the CDB using the
`modify-db-instance` command.

## PDB management

In the RDS Custom for Oracle shared responsibility model, you are responsible for managing PDBs
and creating any additional PDBs. RDS Custom doesn't restrict the number of PDBs. You can
manually create, modify, and delete PDBs by connecting to the CDB root and running a SQL
statement. Create PDBs on an Amazon EBS data volume to prevent the DB instance from going outside
the support perimeter.

To modify your CDBs or PDBs, complete the following steps:

1. Pause automation to prevent interference with RDS Custom actions.
2. Modify your CDB or PDBs.
3. Back up any modified PDBs.
4. Resume RDS Custom automation.

## Automatic recovery of the CDB root

RDS Custom keeps the CDB root open in the same way as it keeps a non-CDB open. If the
state of the CDB root changes, the monitoring and recovery automation attempts to
recover the CDB root to the desired state. You receive RDS event notifications when the
root CDB is shut down (`RDS-EVENT-0004`) or restarted
(`RDS-EVENT-0006`), similar to the non-CDB architecture. RDS Custom attempts
to open all PDBs in `READ WRITE` mode at DB instance startup. If some PDBs can't be
opened, RDS Custom publishes the following event: `tenant database shutdown`.
