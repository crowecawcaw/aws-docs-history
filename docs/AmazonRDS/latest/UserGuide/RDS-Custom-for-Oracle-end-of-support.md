

# RDS Custom for Oracle end of support
<a name="RDS-Custom-for-Oracle-end-of-support"></a>

**Note**  
End of support notice: On March 31, 2027, AWS will end support for Amazon RDS Custom for Oracle. After March 31, 2027, you will no longer be able to access the RDS Custom for Oracle console or RDS Custom for Oracle resources. For more information, see [RDS Custom for Oracle end of support](#RDS-Custom-for-Oracle-end-of-support).

## Overview
<a name="RDS-Custom-for-Oracle-end-of-support-overview"></a>

After careful consideration, AWS has made the decision to discontinue the Amazon RDS Custom for Oracle service. The service will be deprecated effective **March 31, 2027**. This prescriptive guidance provides detailed migration strategies to help you migrate from RDS Custom for Oracle to self-managed Oracle databases on Amazon Elastic Compute Cloud (Amazon EC2).

### Key timelimes
<a name="RDS-Custom-for-Oracle-end-of-support-key_timelines"></a>
+ **From March 31, 2026 to March 31, 2027**: We recommend that you migrate from RDS Custom for Oracle to running Oracle on EC2. During this period, you can continue using RDS Custom for Oracle with existing features and support.
+ **After March 31, 2027**: You will no longer be able to use the RDS Custom for Oracle service.

### Target audience
<a name="RDS-Custom-for-Oracle-end-of-support-target_audience"></a>

This guidance is intended for:
+ Database administrators responsible for Oracle database migrations
+ Cloud architects planning migration strategies
+ DevOps engineers managing database infrastructure
+ IT managers overseeing the migration process

### Prerequisites
<a name="RDS-Custom-for-Oracle-end-of-support-prerequisites"></a>

Before you begin, ensure you have:
+ An active Amazon RDS Custom for Oracle instance running Oracle 19c Enterprise Edition
+ Appropriate AWS Identity and Access Management (IAM) permissions to create and manage EC2 instances
+ Understanding of your database architecture (non-CDB or multitenant CDB with PDBs)
+ Network connectivity planning between source and target instances
+ Backup and recovery strategy for your migration

## Migration options
<a name="RDS-Custom-for-Oracle-end-of-support-migration_options"></a>

As part of the migration process, you can choose one of two migration options based on your business requirements and use case:

### Option 1: RMAN Active Duplication (Online/Offline Migration)
<a name="RDS-Custom-for-Oracle-end-of-support-migration_options-RMAN"></a>

**Best suited for**
+ Workloads that can afford planned downtime during final cutover
+ Simpler migration requirements with fewer moving parts
+ Databases where you want a straightforward, one-time migration
+ Scenarios where you don't need continuous synchronization before cutover

**Key characteristics**
+ **Downtime**: Minimal downtime during final cutover (database remains online during duplication, brief downtime for final cutover)
+ **Complexity**: Lower complexity with direct database duplication
+ **Duration**: Migration time depends on database size and network bandwidth
+ **Fallback**: Requires maintaining the source database until validation is complete
+ **Online capability**: Source database remains online and accessible during the duplication process

**Migration approach:** RMAN active duplication creates an exact copy of the source database on the target by copying database files over the network from the live, running source database. The source database remains online and accessible to applications during the duplication process. For multitenant databases, RMAN automatically duplicates the entire CDB including `CDB$ROOT`, `PDB$SEED`, and all pluggable databases in a single operation. Only a brief cutover window is needed to redirect applications to the new EC2 instance.

### Option 2: Oracle Data Guard (Online Migration)
<a name="RDS-Custom-for-Oracle-end-of-support-migration_options-Oracle-Data-Guard"></a>

**Best suited for**
+ Production workloads requiring minimal downtime
+ Mission-critical databases that must remain available
+ Scenarios where you need continuous synchronization before cutover
+ Migrations requiring built-in fallback capability

**Key characteristics**
+ **Downtime**: Near-zero downtime (seconds to minutes for switchover)
+ **Complexity**: Higher complexity with Data Guard configuration
+ **Duration**: Initial setup time plus continuous synchronization until switchover
+ **Fallback**: Built-in fallback capability by keeping the source as a standby

**Migration approach:** Oracle Data Guard maintains a synchronized standby database by continuously shipping and applying redo logs from the primary database. When you're ready to complete the migration, you perform a switchover that promotes the EC2 standby to primary with minimal downtime. For multitenant databases, Data Guard automatically protects the entire CDB including all PDBs.

 **Decision matrix** 

Use the following matrix to help choose the appropriate migration option:


|  **Aspect**  |  **RMAN Active Duplication**  |  **Oracle Data Guard**  | 
| --- | --- | --- | 
| **Source database availability** | Online during duplication | Online during entire process | 
| **Acceptable downtime** | Minutes to hours (final cutover) | Seconds to minutes (switchover) | 
| **Migration complexity** | Lower | Higher | 
| **Continuous synchronization** | No | Yes | 
| **Fallback capability** | Manual (keep source) | Built-in (automatic) | 
| **Testing before cutover** | Limited | Full testing possible | 
| **Network bandwidth requirement** | High during duplication | Moderate (continuous) | 
| **Best for** | Most migrations, dev/test, planned cutover | Production, mission-critical, near-zero downtime | 

### Architecture considerations
<a name="RDS-Custom-for-Oracle-end-of-support-migration_options-architecture-considerations"></a>

Both migration options support two Oracle database architectures:

 **Non-CDB** 

Traditional single-instance Oracle databases without the multitenant architecture. These databases:
+ Have a single database instance
+ Do not use pluggable databases (PDBs)
+ Are simpler to manage and migrate
+ Typically named ORCL in RDS Custom for Oracle

 **Multitenant (CDB with PDBs)** 

Container databases (CDB) hosting multiple pluggable databases (PDBs), introduced in Oracle 12c. These databases:
+ Have a container database (CDB) with `CDB$ROOT` and `PDB$SEED`
+ Host one or more pluggable databases (PDBs)
+ Provide database consolidation and resource isolation
+ Typically named RDSCDB in RDS Custom for Oracle
+ Use Oracle Managed Files (OMF) with GUID-based subdirectories for PDB data files

**Important note for multitenant migrations**: The target database will be renamed to ORCL during the migration process (source: RDSCDB → target: ORCL). This simplifies the target configuration and aligns with standard naming conventions.

 **Key differences in migration approach** 


|  **Aspect**  |  **Non-CDB**  |  **Multitenant (CDB with PDBs)**  | 
| --- | --- | --- | 
| **Migration scope** | Single database | Entire CDB with all PDBs | 
| **Post-migration state**  | Database open READ WRITE | CDB open READ WRITE; PDBs in MOUNTED state | 
| **PDB management** | N/A | Must open PDBs and configure auto-open | 
| **Cleanup** | Single database | CDB$ROOT (cascades to PDBs); handle C\#\# common users | 
| **Application connections** | Database service | PDB services (not CDB) | 
| **Parameter file** | Standard parameters | Requires enable\_pluggable\_database=TRUE | 
| **Complexity** | Lower | Higher due to multiple containers | 

## Common prerequisites for both migration options
<a name="RDS-Custom-for-Oracle-end-of-support-common-prerequisites"></a>

Before starting either migration option, complete the following prerequisite steps:

1. Launch and configure EC2 instance

   Launch an EC2 instance with the following considerations:
   + **Instance type**: Choose an EC2 instance type that meets the resource requirements of your workload. Using the same instance class as your RDS Custom instance is a good starting point. Consider memory, CPU, and network bandwidth requirements.
   + **Operating system**: Oracle Linux or Red Hat Enterprise Linux (matching or compatible with your RDS Custom OS version)
   + **Oracle software**: Install Oracle Database software (same major version, minor version, Release Update, and ideally the same one-off patches as RDS Custom). Ensure the Oracle software is installed in /u01/app/oracle/ or your preferred location.
   + **Storage**: Configure Amazon EBS volumes with appropriate size and IOPS to meet your workload requirements. Consider using gp3 volumes for cost-effective performance or io2 Block Express for high-performance workloads.

1. Configure storage architecture

   1. File system storage (recommended for most scenarios)
      + Use standard file system directories for Oracle data files
      + Simpler to manage and suitable for most workloads
      + This guidance uses file system storage examples

   1. Oracle Automatic Storage Management (ASM)
      + If your workload requires ASM, install and configure standalone ASM on the EC2 instance
      + Adjust all path parameters in the init file accordingly to use ASM disk groups (e.g., \+DATA, \+FRA)
      + The migration process is similar for ASM, with path adjustments

1. Set up file transfer mechanism

   Create a mechanism to transfer files between RDS Custom and EC2 instances. You have several options:

   1. Option A: Amazon S3 (recommended for most scenarios)
      + Create an Amazon S3 bucket or use an existing one
      + Install and configure AWS CLI on both instances
      + For instructions, see [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

   1. Option B: Direct SCP/SFTP
      + If SSH ports are open between instances, you can transfer files directly
      + Suitable for small files like parameter files and password files

   1. Option C: Amazon EFS
      + If you already have Amazon EFS mounted on both instances, you can use it as a shared file system
      + Suitable for environments with existing EFS infrastructure

      This guidance uses Amazon S3 for examples, but you can adapt the commands for your chosen method.

1. Configure network connectivity

   Ensure network connectivity between the RDS Custom and EC2 instances:
   + **Same VPC**: Security groups must allow bidirectional traffic on the Oracle listener port (default 1521, or your custom port)
   + **Different VPCs (same account)**: Set up VPC peering and configure route tables and security groups
   + **Different accounts**: Set up VPC peering across accounts or use AWS Transit Gateway
   + **Verify connectivity**: Use ping and telnet to test connectivity on the database port

1. Create directory structure on EC2

   The directory structure depends on your database architecture:  
**Example For Non-CDB:**  

   ```
   # Non-CDB directories
   mkdir -p /u01/app/oracle/oradata/ORCL/controlfile/
   mkdir -p /u01/app/oracle/oradata/ORCL/datafile
   mkdir -p /u01/app/oracle/oradata/ORCL/onlinelog
   mkdir -p /u01/app/oracle/oradata/ORCL/arch
   mkdir -p /u01/app/oracle/admin/ORCL/adump
   mkdir -p /u01/app/oracle/backup
   # Set ownership
   chown -R oracle:oinstall /u01/app/oracle/oradata/ORCL
   chown -R oracle:oinstall /u01/app/oracle/admin/ORCL
   chown -R oracle:oinstall /u01/app/oracle/backup
   ```  
**Example For Multitenant (CDB with PDBs)**  

   ```
   # CDB directories
   mkdir -p /u01/app/oracle/oradata/ORCL/controlfile/
   mkdir -p /u01/app/oracle/oradata/ORCL/cdb/datafile
   mkdir -p /u01/app/oracle/oradata/ORCL/pdbseed/datafile
   mkdir -p /u01/app/oracle/oradata/ORCL/onlinelog
   mkdir -p /u01/app/oracle/oradata/ORCL/arch
   mkdir -p /u01/app/oracle/admin/ORCL/adump
   mkdir -p /u01/app/oracle/backup
   # PDB directories (RDS Custom uses OMF with GUID-based paths)
   # Create a generic pdb directory - migration will create subdirectories as needed
   mkdir -p /u01/app/oracle/oradata/ORCL/pdb/datafile
   # Set ownership
   chown -R oracle:oinstall /u01/app/oracle/oradata/ORCL
   chown -R oracle:oinstall /u01/app/oracle/admin/ORCL
   chown -R oracle:oinstall /u01/app/oracle/backup
   ```
**Note**  
RDS Custom for Oracle uses Oracle Managed Files (OMF) for PDB data files with GUID-based subdirectories (e.g., `/rdsdbdata/db/pdb/RDSCDB_A/{{{GUID}}}/datafile/`). The migration process will automatically create the necessary subdirectory structure on the target. You only need to create the parent directories.

   **Storage strategy**: Consider using a separate EBS volume for /u01/app/oracle/backup to easily detach and remove it after migration completes, freeing up storage costs.

1. Verify source database configuration

Before starting the migration, verify your source database configuration:

1. Log in to the RDS Custom database host as the rdsdb user and set the environment:  
**Example**  

   ```
   # For non-CDB
   export ORACLE_HOME=/rdsdbbin/oracle.19.custom.r1.EE.1
   export ORACLE_SID=ORCL
   export PATH=$ORACLE_HOME/bin:$PATH
   
   # For multitenant CDB
   export ORACLE_HOME=/rdsdbbin/oracle.19.custom.r1.EE-CDB.1
   export ORACLE_SID=RDSCDB
   export PATH=$ORACLE_HOME/bin:$PATH
   ```

1. Connect to the database and check the architecture:  
**Example**  

   ```
   sqlplus / as sysdba
   SQL> SELECT name, cdb, open_mode, log_mode FROM v$database;
   ```  
**Example For Non-CDB, expected output**  

   ```
   NAME CDB OPEN_MODE                 LOG_MODE
   --------- --- -------------------- ------------
   ORCL NO  READ  WRITE               ARCHIVELOG
   ```  
**Example For Multitenant (CDB), expected output:**  

   ```
   NAME    CDB  OPEN_MODE             LOG_MODE
   --------- --- -------------------- ------------
   RDSCDB    YES READ WRITE           ARCHIVELOG
   ```

1. **If you have a multitenant CDB**, list all PDBs and their status:  
**Example**  

   ```
   SQL> SELECT con_id, name, open_mode, restricted FROM v$pdbs;
   ```

   Expected output (example with 1 PDB named ORCLDB):  
**Example**  

   ```
   CON_ID     NAME                           OPEN_MODE  RES
   ---------- ------------------------------ ---------- ---
   2          PDB$SEED                       READ ONLY  NO
   3          ORCLDB                         READ WRITE NO
   ```

1. Check the total database size:  
**Example For Non-CDB:**  

   ```
   SQL> SELECT SUM(bytes)/1024/1024/1024 AS total_size_gb FROM dba_data_files;
   ```  
**Example For Multitenant:**  

   ```
   -- Total CDB size (all containers)
   SQL> SELECT SUM(bytes)/1024/1024/1024 AS total_size_gb FROM cdb_data_files;
   -- Size per PDB
   SQL> SELECT p.name AS pdb_name,
         ROUND(SUM(d.bytes)/1024/1024/1024, 2) AS size_gb
   FROM v$pdbs p
   JOIN cdb_data_files d ON p.con_id = d.con_id
   GROUP BY p.name, p.con_id
   ORDER BY p.con_id;
   ```

## Option 1: Physical Migration Using RMAN Active Duplication
<a name="RDS-Custom-for-Oracle-end-of-support-option-1"></a>

**Topics**
+ [When to use RMAN active duplication](#RDS-Custom-for-Oracle-end-of-support-option-1-when-to-use)
+ [RMAN active duplication overview](#RDS-Custom-for-Oracle-end-of-support-option-1-overview)
+ [Migration workflow for RMAN active duplication](#RDS-Custom-for-Oracle-end-of-support-option-1-migration-workflow)
+ [Step 1: Pause Amazon RDS Custom automation](#RDS-Custom-for-Oracle-end-of-support-option-1-step-1)
+ [Step 2: Create password and parameter files](#RDS-Custom-for-Oracle-end-of-support-option-1-step-2)
+ [Step 3: Transfer files to EC2](#RDS-Custom-for-Oracle-end-of-support-option-1-step-3)
+ [Step 4: Edit parameter file on EC2](#RDS-Custom-for-Oracle-end-of-support-option-1-step-4)
+ [Step 5: Configure TNS and listener](#RDS-Custom-for-Oracle-end-of-support-option-1-step-5)
+ [Step 6: Start database in `NOMOUNT` on EC2](#RDS-Custom-for-Oracle-end-of-support-option-1-step-6)
+ [Step 7: Perform RMAN active duplication](#RDS-Custom-for-Oracle-end-of-support-option-1-step-7)
+ [Step 8: Open PDBs (multitenant only)](#RDS-Custom-for-Oracle-end-of-support-option-1-step-8)
+ [Step 9: Remove RDS Custom objects](#RDS-Custom-for-Oracle-end-of-support-option-1-step-9)
+ [Step 10: Configure automatic startup](#RDS-Custom-for-Oracle-end-of-support-option-1-step-10)
+ [Step 11: Final validation](#RDS-Custom-for-Oracle-end-of-support-option-1-step-11)

This section provides detailed steps for migrating your Oracle database from RDS Custom for Oracle to EC2 using RMAN active duplication. This method duplicates from a live, running database, keeping the source online and accessible during the migration process.

### When to use RMAN active duplication
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-when-to-use"></a>

Choose RMAN active duplication when:
+ You want to keep the source database online and accessible during migration
+ You can afford a brief cutover window for final application redirection
+ You want a straightforward migration process with fewer moving parts
+ Your database size and network bandwidth allow for reasonable duplication time
+ You don't need continuous synchronization before cutover
+ You're migrating production, development, or test databases

### RMAN active duplication overview
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-overview"></a>

RMAN active duplication doesn't require a backup of the source database or taking the source database offline. It duplicates the live, running source database to the destination by copying database files over the network while the source remains online and accessible to applications.

**Key advantages:**
+ **Source remains online**: Applications can continue accessing the source database during duplication
+ **No backup required**: Eliminates the need for intermediate backup storage
+ **Direct network transfer**: Database files are copied directly from source to target
+ **Automatic consistency**: RMAN ensures the duplicate database is consistent
+ **Single operation**: For multitenant, duplicates entire CDB including all PDBs in one operation

The duplication process creates an exact copy of the source database on the target, including all data files, control files, and redo logs. The source database continues to serve application requests throughout the duplication process. Only a brief cutover window is needed at the end to redirect applications from the source to the target.

**Typical timeline**

1. **Duplication phase** (source remains online): 30 minutes to several hours depending on database size

1. **Validation phase** (source remains online): Hours to days as needed

1. **Cutover phase** (brief downtime): Minutes to redirect applications to EC2

### Migration workflow for RMAN active duplication
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-migration-workflow"></a>

**RDS Custom DB instance (source) steps:**

1. Pause Amazon RDS Custom automation

1. Verify database architecture (non-CDB or CDB with PDBs)

1. Create a password file and parameter file from the source database

1. Copy the password file and parameter file to the target EC2 instance

1. Verify the source database is running in archive log mode

1. Configure tnsnames.ora on the RDS Custom DB server

**EC2 DB instance (target) steps:**

1. Edit the parameter file for EC2 (architecture-specific)

1. Configure tnsnames.ora on EC2

1. Configure the environment for the EC2 instance

1. Configure Oracle Listener on EC2

1. Start the database on EC2 in NOMOUNT state

**RMAN duplication steps:**

1. Perform RMAN active duplication

1. Open the database (and PDBs for multitenant)

1. Configure PDB auto-open (multitenant only)

1. Remove RDS Custom specific users and objects

1. Create SPFILE and configure automatic startup

1. Resume Amazon RDS Custom automation on source (if keeping it active)

### Step 1: Pause Amazon RDS Custom automation
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-1"></a>

Pause the automation mode on your RDS Custom instance before proceeding with the migration steps to ensure the automation doesn't interfere with the RMAN activity. The --resume-full-automation-mode-minute parameter (240 minutes = 4 hours in this example) should be adjusted based on your database size and expected duplication time.

**Important**: Pausing automation does not affect database availability. The database remains online and accessible to applications during the duplication process.

**Example**  

```
aws rds modify-db-instance \
--db-instance-identifier my-custom-instance \
--automation-mode all-paused \
--resume-full-automation-mode-minute 240 \
--region us-east-1 
--query 'DBInstances[0].AutomationMode'
```

Validate the automation status:

**Example**  

```
aws ds describe-db-instances \
--db-instance-identifier my-custom-instance \
--region us-east-1 \
--query 'DBInstances[0].AutomationMode'
```

Expected output: "`all-paused`"

### Step 2: Create password and parameter files
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-2"></a>

Create a password file using `orapwd`. Retrieve the SYS password from AWS Secrets Manager (stored during RDS Custom instance creation).

**Example**  

```
# Non-CDB
$ORACLE_HOME/bin/orapwd file=/rdsdbdata/config/orapwORCL password={{<SYS_PASSWORD>}} entries=10
# Multitenant
$ORACLE_HOME/bin/orapwd file=/rdsdbdata/config/orapwRDSCDB password={{<SYS_PASSWORD>}} entries=10
```

Create a parameter file from the source database:

**Example**  

```
sqlplus / as sysdba
SQL> CREATE PFILE='/tmp/initORCL.ora' FROM SPFILE; -- Non-CDB
SQL> CREATE PFILE='/tmp/initRDSCDB.ora' FROM SPFILE; -- Multitenant
```

The generated parameter file will contain RDS Custom-specific paths and parameters. For multitenant, key parameters include:
+ `enable_pluggable_database`=`TRUE` (critical for multitenant)
+ `noncdb_compatible`=`TRUE` (for backward compatibility)
+ Data file paths for `CDB$ROOT`, `PDB$SEED`, and all PDBs
+ `db_create_file_dest` and `db_create_online_log_dest_1` for OMF

### Step 3: Transfer files to EC2
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-3"></a>

Choose your preferred file transfer method. This guidance uses Amazon S3 for examples.

 **Using Amazon S3:** 

#### Using Amazon S3:
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-3-ec2"></a>

**Example For Non-CDB:**  

```
# Copy files to Amazon S3 from the RDS Custom instance
aws s3 cp /tmp/initORCL.ora s3://{{<YOUR_BUCKET>}}/
aws s3 cp /rdsdbdata/config/orapwORCL s3://{{<YOUR_BUCKET>}}/
# On EC2, download files
aws s3 cp s3://{{<YOUR_BUCKET>}}/initORCL.ora $ORACLE_HOME/dbs/
aws s3 cp s3://{{<YOUR_BUCKET>}}/orapwORCL $ORACLE_HOME/dbs/
```

**Example For Multitenant**  

```
# Copy files to Amazon S3 from the RDS Custom instance
aws s3 cp /tmp/initRDSCDB.ora s3://{{<YOUR_BUCKET>}}/
aws s3 cp /rdsdbdata/config/orapwRDSCDB s3://{{<YOUR_BUCKET>}}/
# On EC2, download and rename files to use ORCL naming
aws s3 cp s3://{{<YOUR_BUCKET>}}/initRDSCDB.ora $ORACLE_HOME/dbs/initORCL.ora
aws s3 cp s3://{{<YOUR_BUCKET>}}/orapwRDSCDB $ORACLE_HOME/dbs/orapwORCL
```

Validate the files on EC2:

**Example**  

```
ls -l $ORACLE_HOME/dbs/initORCL.ora
ls -l $ORACLE_HOME/dbs/orapwORCL
```

### Step 4: Edit parameter file on EC2
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-4"></a>

The parameter file requires careful editing to ensure successful migration. This is one of the most critical steps in the migration process.

Edit `$ORACLE_HOME/dbs/initORCL.ora` on the EC2 instance and make these critical changes:

1. **Update database name**: For multitenant, change all occurrences of RDSCDB to ORCL

1. **Convert RDS Custom paths to EC2 paths**: Replace /rdsdbdata/ with /u01/app/oracle/

1. 

**Remove RDS Custom-specific parameters**
   + `dg_broker_config_file1` and `dg_broker_config_file2` (if present - indicates a replica existed)
   + `standby_file_management` (if present)
   + `spfile` (we'll create a new SPFILE later)
   + Any `log_archive_dest` parameters pointing to standby destinations (keep only `log_archive_dest_1` for local archiving)

1. **Add file name conversion parameters** (see below)

1. **Adjust memory parameters** based on your EC2 instance size (optional but recommended)

**Understanding file name conversion parameters:** 

The `DB_FILE_NAME_CONVERT` and `LOG_FILE_NAME_CONVERT` parameters are critical for RMAN duplication. They tell RMAN how to map source file paths to target file paths during the duplication process. Without these parameters, RMAN will attempt to create files in the same paths as the source, which will fail on EC2.

**Key considerations:**
+ Each parameter accepts pairs of strings: source path followed by target path
+ Multiple pairs can be specified in a single parameter
+ For multitenant, you must map paths for `CDB$ROOT`, `PDB$SEED`, and all PDBs
+ The order of pairs matters - RMAN processes them in the order specified
+ Paths are case-sensitive and must match exactly

**Path mappings:**


**Non-CDB:**  

|  **RDS Custom path**  |  **EC2 path**  |  **Description**  | 
| --- | --- | --- | 
| /rdsdbbin | /u01/app/oracle | Oracle base | 
| /rdsdbdata/db/ORCL\_A/datafile/ | /u01/app/oracle/oradata/ORCL/datafile/ | Data files | 
| /rdsdbdata/db/ORCL\_A/controlfile/ | /u01/app/oracle/oradata/ORCL/controlfile/ | Control files | 
| /rdsdbdata/db/ORCL\_A/onlinelog/ | /u01/app/oracle/oradata/ORCL/onlinelog/ | Online redo logs | 
| /rdsdbdata/db/ORCL\_A/arch/ | /u01/app/oracle/oradata/ORCL/arch/ | Archive logs | 
| /rdsdbdata/admin/ORCL/adump | /u01/app/oracle/admin/ORCL/adump | Audit dump | 
| /rdsdbdata/log | /u01/app/oracle | Diagnostic destination | 


**Multitenant**  

|  **RDS Custom path**  |  **EC2 path**  |  **Description**  | 
| --- | --- | --- | 
| /rdsdbbin | /u01/app/oracle | Oracle base | 
| /rdsdbdata/db/cdb/RDSCDB/datafile/ | /u01/app/oracle/oradata/ORCL/cdb/datafile/ | CDB root data files | 
| /rdsdbdata/db/cdb/pdbseed/ | /u01/app/oracle/oradata/ORCL/pdbseed/datafile/ | PDB$SEED data files | 
| /rdsdbdata/db/pdb/RDSCDB\_A/ | /u01/app/oracle/oradata/ORCL/pdb/datafile/ | PDB data files (OMF with GUID) | 
| /rdsdbdata/db/cdb/RDSCDB\_A/controlfile/ | /u01/app/oracle/oradata/ORCL/controlfile/ | Control files | 
| /rdsdbdata/db/cdb/RDSCDB\_A/onlinelog/ | /u01/app/oracle/oradata/ORCL/onlinelog/ | Online redo logs | 
| /rdsdbdata/db/cdb/RDSCDB\_A/arch/redolog | /u01/app/oracle/oradata/ORCL/arch/ | Archive logs | 
| /rdsdbdata/admin/RDSCDB/adump | /u01/app/oracle/admin/ORCL/adump | Audit dump | 
| /rdsdbdata/log | /u01/app/oracle | Diagnostic destination | 

**Add conversion parameters:**

**Example Non-CDB:**  

```
*.DB_FILE_NAME_CONVERT='/rdsdbdata/db/ORCL_A/datafile/','/u01/app/oracle/oradata/ORCL/datafile/'
*.LOG_FILE_NAME_CONVERT='/rdsdbdata/db/ORCL_A/onlinelog/','/u01/app/oracle/oradata/ORCL/onlinelog/'
```

**Example **Multitenant** (must include mappings for CDB root, `PDB$SEED`, and all PDB paths):**  

```
*.DB_FILE_NAME_CONVERT='/rdsdbdata/db/cdb/RDSCDB/datafile/','/u01/app/oracle/oradata/ORCL/cdb/datafile/','/rdsdbdata/db/cdb/pdbseed/','/u01/app/oracle/oradata/ORCL/pdbseed/datafile/','/rdsdbdata/db/pdb/RDSCDB_A/','/u01/app/oracle/oradata/ORCL/pdb/datafile/'
 *.LOG_FILE_NAME_CONVERT='/rdsdbdata/db/cdb/RDSCDB_A/onlinelog/','/u01/app/oracle/oradata/ORCL/onlinelog/'
```

**Important**: For multitenant, ensure `enable_pluggable_database`=`TRUE` is present in the parameter file. RDS Custom uses OMF for PDB data files with GUID-based subdirectories - the path mapping handles this automatically.

 **Complete example parameter files:** 

**Example Non-CDB parameter file (`initORCL.ora`):**  

```
ORCL.__data_transfer_cache_size=0
ORCL.__db_cache_size=6039797760
ORCL.__inmemory_ext_roarea=0
ORCL.__inmemory_ext_rwarea=0
ORCL.__java_pool_size=0
ORCL.__large_pool_size=33554432
ORCL.__oracle_base='/u01/app/oracle'
ORCL.__pga_aggregate_target=4966055936
ORCL.__sga_target=7449083904
ORCL.__shared_io_pool_size=134217728
ORCL.__shared_pool_size=1207959552
ORCL.__streams_pool_size=0
ORCL.__unified_pga_pool_size=0
*.archive_lag_target=300
*.audit_file_dest='/u01/app/oracle/admin/ORCL/adump'
*.compatible='19.0.0'
*.control_files='/u01/app/oracle/oradata/ORCL/controlfile/control-01.ctl'
*.db_block_checking='MEDIUM'
*.db_create_file_dest='/u01/app/oracle/oradata/ORCL'
*.db_name='ORCL'
*.db_recovery_file_dest_size=1073741824
*.db_unique_name='ORCL'
*.dbfips_140=FALSE
*.diagnostic_dest='/u01/app/oracle'
*.filesystemio_options='setall'
*.heat_map='OFF'
*.job_queue_processes=50
*.local_listener='(address=(protocol=tcp)(host=)(port=1521))'
*.log_archive_dest_1='location="/u01/app/oracle/oradata/ORCL/arch", valid_for=(ALL_LOGFILES,ALL_ROLES)'
*.log_archive_format='-%s-%t-%r.arc'
*.max_string_size='STANDARD'
*.memory_max_target=12385852416
*.memory_target=12385852416
*.open_cursors=300
*.pga_aggregate_target=0
*.processes=1673
*.recyclebin='OFF'
*.sga_target=0
*.undo_tablespace='UNDO_T1'
*.use_large_pages='FALSE'
*.DB_FILE_NAME_CONVERT='/rdsdbdata/db/ORCL_A/datafile/','/u01/app/oracle/oradata/ORCL/datafile/'
*.LOG_FILE_NAME_CONVERT='/rdsdbdata/db/ORCL_A/onlinelog/','/u01/app/oracle/oradata/ORCL/onlinelog/'
```

**Example Multitenant parameter file (`initORCL.ora`):**  

```
ORCL.__data_transfer_cache_size=0
ORCL.__db_cache_size=6006243328
ORCL.__inmemory_ext_roarea=0
ORCL.__inmemory_ext_rwarea=0
ORCL.__java_pool_size=0
ORCL.__large_pool_size=33554432
ORCL.__oracle_base='/u01/app/oracle'
ORCL.__pga_aggregate_target=4966055936
ORCL.__sga_target=7415529472
ORCL.__shared_io_pool_size=134217728
ORCL.__shared_pool_size=1207959552
ORCL.__streams_pool_size=0
ORCL.__unified_pga_pool_size=0
*.archive_lag_target=300
*.audit_file_dest='/u01/app/oracle/admin/ORCL/adump'
*.compatible='19.0.0'
*.control_files='/u01/app/oracle/oradata/ORCL/controlfile/control-01.ctl'
*.db_block_checking='MEDIUM'
*.db_create_file_dest='/u01/app/oracle/oradata/ORCL/pdb/datafile'
*.db_create_online_log_dest_1='/u01/app/oracle/oradata/ORCL'
*.db_name='ORCL'
*.db_recovery_file_dest_size=1073741824
*.db_unique_name='ORCL'
*.dbfips_140=FALSE
*.diagnostic_dest='/u01/app/oracle'
*.enable_pluggable_database=TRUE
*.filesystemio_options='setall'
*.heat_map='OFF'
*.job_queue_processes=50
*.local_listener='(address=(protocol=tcp)(host=)(port=1521))'
*.log_archive_dest_1='location="/u01/app/oracle/oradata/ORCL/arch", valid_for=(ALL_LOGFILES,ALL_ROLES)'
*.log_archive_format='-%s-%t-%r.arc'
*.max_string_size='STANDARD'
*.memory_max_target=12361688064
*.memory_target=12361688064
*.noncdb_compatible=TRUE
*.open_cursors=300
*.pga_aggregate_target=0
*.processes=1670
*.recyclebin='OFF'
*.sga_target=0
*.undo_tablespace='UNDO_T1'
*.use_large_pages='FALSE'
*.DB_FILE_NAME_CONVERT='/rdsdbdata/db/cdb/RDSCDB/datafile/','/u01/app/oracle/oradata/ORCL/cdb/datafile/','/rdsdbdata/db/cdb/pdbseed/','/u01/app/oracle/oradata/ORCL/pdbseed/datafile/','/rdsdbdata/db/pdb/RDSCDB_A/','/u01/app/oracle/oradata/ORCL/pdb/datafile/'
*.LOG_FILE_NAME_CONVERT='/rdsdbdata/db/cdb/RDSCDB_A/onlinelog/','/u01/app/oracle/oradata/ORCL/onlinelog/'
```

**Key parameter explanations:**
+ `enable_pluggable_database=TRUE`: Required for multitenant CDB. This parameter enables the pluggable database feature.
+ `noncdb_compatible=TRUE`: Set by RDS Custom for backward compatibility. Can be kept or removed based on your requirements.
+ `db_create_file_dest`: Specifies the default location for Oracle Managed Files (OMF). For multitenant, this points to the PDB datafile directory.
+ `db_create_online_log_dest_1`: Specifies the location for online redo logs when using OMF.
+ `DB_FILE_NAME_CONVERT`: Critical for RMAN duplication. Maps source data file paths to target paths.
+ `LOG_FILE_NAME_CONVERT`: Maps source redo log paths to target paths.
+ `memory_target` and `memory_max_target`: Adjust these based on your EC2 instance memory. The values shown are examples.
+ `processes`: Maximum number of operating system processes that can connect to Oracle. Adjust based on your workload.

**Memory sizing guidelines:**

When adjusting memory parameters for your EC2 instance:


|  **EC2 Instance Memory**  |  **Recommended memory\_target**  |  **Recommended memory\_max\_target**  | 
| --- | --- | --- | 
| 16 GB | 12 GB (12884901888 bytes) | 14 GB (15032385536 bytes) | 
| 32 GB | 24 GB (25769803776 bytes) | 28 GB (30064771072 bytes) | 
| 64 GB | 48 GB (51539607552 bytes) | 56 GB (60129542144 bytes) | 
| 128 GB | 96 GB (103079215104 bytes) | 112 GB (120259084288 bytes) | 

Leave approximately 20-25% of system memory for the operating system and other processes.

### Step 5: Configure TNS and listener
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-5"></a>

On both instances, add TNS entries to `tnsnames.ora`:

**Example Non-CDB:**  

```
DB_SOURCE = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{<RDS_CUSTOM_IP>}})(PORT = 1521)) (CONNECT_DATA = (SID = ORCL)))
DB_TARGET = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{<EC2_IP>}})(PORT = 1521)) (CONNECT_DATA = (SID = ORCL)))
```

**Example Multitenant:**  

```
DB_SOURCE = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{<RDS_CUSTOM_IP>}})(PORT = 1521)) (CONNECT_DATA = (SID = RDSCDB)))
DB_TARGET = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{<EC2_IP>}})(PORT = 1521)) (CONNECT_DATA = (SID = ORCL)))
```

**Example Configure listener on EC2 (`$ORACLE_HOME/network/admin/listener.ora`):**  

```
LISTENER = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{<EC2_IP>}})(PORT = 1521)))
SID_LIST_LISTENER = (SID_LIST = (SID_DESC = (GLOBAL_DBNAME = ORCL) (ORACLE_HOME = /u01/app/oracle/product/19.0.0/dbhome_1) (SID_NAME = ORCL)))
```

**Example Start listener:**  

```
lsnrctl start
```

**Note**  
For RMAN active duplication, the TNS entries connect to the database instance using SID (not SERVICE\_NAME). For multitenant, this connects to the CDB, and RMAN automatically duplicates all PDBs.

### Step 6: Start database in `NOMOUNT` on EC2
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-6"></a>

**Example**  

```
export ORACLE_SID=ORCL
export ORACLE_HOME=/u01/app/oracle/product/19.0.0/dbhome_1
export PATH=$ORACLE_HOME/bin:$PATH

sqlplus / as sysdba

SQL> STARTUP NOMOUNT PFILE='$ORACLE_HOME/dbs/initORCL.ora';
```

**Example Verify parameters:**  

```
SQL> SHOW PARAMETER db_name
SQL> SHOW PARAMETER control_files
SQL> SHOW PARAMETER enable_pluggable_database -- For multitenant
```

### Step 7: Perform RMAN active duplication
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-7"></a>

RMAN active duplication copies the database from the live, running source to the target. The source database remains online and accessible to applications throughout this process.

Connect RMAN to both the source and target instances:

**Example**  

```
rman target sys/{{<password>}}@DB_SOURCE auxiliary sys/{{<password>}}@DB_TARGET
```

**Example Expected output for non-CDB:**  

```
Recovery Manager: Release 19.0.0.0.0 - Production
connected to target database: ORCL (DBID=4089929259)
connected to auxiliary database: ORCL (not mounted)
```

**Example Expected output for multitenant:**  

```
Recovery Manager: Release 19.0.0.0.0 - Production
connected to target database: RDSCDB (DBID=4089929259)
connected to auxiliary database: ORCL (not mounted)
```

**Example Run the active duplication command:**  

```
RMAN> DUPLICATE DATABASE TO 'ORCL' FROM ACTIVE DATABASE NOFILENAMECHECK;
```

**Note**  
**Source remains online**: The source database continues to serve application requests during duplication
**For non-CDB**: This duplicates the entire database while it remains online
**For multitenant**: This duplicates the entire CDB including `CDB$ROOT`, `PDB$SEED`, and all PDBs in a single operation while the source remains online
**NOFILENAMECHECK**: Allows RMAN to proceed even if file names differ between source and target
**Duration**: Depends on database size and network bandwidth. For a 100GB database, expect 30-60 minutes
**Network impact:** High network bandwidth usage during duplication, but source database remains accessible

**The RMAN active duplication process includes several phases:**

1. Connecting to source and target databases

1. Creating an `SPFILE` from memory on the target

1. Restoring the control file to the target

1. Mounting the target database

1. Copying all data files from source to target over the network (source remains online)

1. Recovering the target database

1. Opening the target database with `RESETLOGS`

**During duplication, the source database:**
+ Remains in `READ WRITE` mode
+ Continues to accept connections
+ Processes transactions normally
+ Generates redo logs normally
+ Is fully accessible to applications

**Example Monitor progress in another session:**  

```
SQL> SELECT sid, serial#, sofar, totalwork, ROUND(sofar/totalwork*100,2) pct_complete
FROM v$session_longops WHERE totalwork > 0 AND sofar <> totalwork;
```

 **Detailed monitoring and troubleshooting during RMAN duplication:** 

While RMAN duplication is running, you can monitor its progress using several methods:

1. **Monitor RMAN output:**

   The RMAN session will display detailed progress information including:
   + Channel allocation
   + Datafile copy progress
   + Estimated completion time
   + Bytes processed

   ```
   channel ORA_AUX_DISK_1: starting datafile copy
   input datafile file number=00001 name=/rdsdbdata/db/ORCL_A/datafile/system01.dbf
   output file name=/u01/app/oracle/oradata/ORCL/datafile/system01.dbf tag=TAG20260303T120000
   channel ORA_AUX_DISK_1: datafile copy complete, elapsed time: 00:05:23
   channel ORA_AUX_DISK_1: starting datafile copy
   input datafile file number=00003 name=/rdsdbdata/db/ORCL_A/datafile/sysaux01.dbf
   output file name=/u01/app/oracle/oradata/ORCL/datafile/sysaux01.dbf tag=TAG20260303T120000
   ```  
**Example output:**  

   ```
   channel ORA_AUX_DISK_1: starting datafile copy
   input datafile file number=00001 name=/rdsdbdata/db/ORCL_A/datafile/system01.dbf
   output file name=/u01/app/oracle/oradata/ORCL/datafile/system01.dbf tag=TAG20260303T120000
   channel ORA_AUX_DISK_1: datafile copy complete, elapsed time: 00:05:23
   channel ORA_AUX_DISK_1: starting datafile copy
   input datafile file number=00003 name=/rdsdbdata/db/ORCL_A/datafile/sysaux01.dbf
   output file name=/u01/app/oracle/oradata/ORCL/datafile/sysaux01.dbf tag=TAG20260303T120000
   ```

1.  **Monitor long-running operations:**   
**Example In a separate SQL\*Plus session on the target EC2 instance:**  

   ```
   SQL> SELECT sid, serial#, opname, sofar, totalwork,
          ROUND(sofar/totalwork*100,2) pct_complete,
          time_remaining, elapsed_seconds
   FROM v$session_longops
   WHERE totalwork > 0 AND sofar <> totalwork
   ORDER BY start_time;
   ```

**This query shows:**
   + `opname`: Operation name (e.g., "RMAN: full datafile restore")
   + `sofar`: Blocks processed so far
   + `totalwork`: Total blocks to process
   + `pct_complete`: Percentage complete
   + `time_remaining`: Estimated seconds remaining
   + `elapsed_seconds`: Time elapsed so far

1. **Monitor RMAN channels:**  
**Example**  

   ```
   SQL> SELECT sid, serial#, context, sofar, totalwork,
          ROUND(sofar/totalwork*100,2) pct_complete
          FROM v$session_longops
   WHERE opname LIKE 'RMAN%'
          AND totalwork > 0
          AND sofar <> totalwork;
   ```

1. **Check alert log:**  
**Example On the target EC2 instance, monitor the alert log for any errors or warnings:**  

   ```
   tail -f $ORACLE_BASE/diag/rdbms/orcl/ORCL/trace/alert_ORCL.log
   ```

**Common issues during RMAN duplication:**
   + **Network timeout**

     ```
     RMAN-03009: failure of duplicate command on ORA_AUX_DISK_1 channel
     ORA-03135: connection lost contact
     ```

     **Solution**: Increase network timeout values in `sqlnet.ora` on both instances:

     ```
     SQLNET.RECV_TIMEOUT=600
     SQLNET.SEND_TIMEOUT=600
     ```
   + **Insufficient space on target**

     ```
     RMAN-03009: failure of duplicate command
     ORA-19504: failed to create file "/u01/app/oracle/oradata/ORCL/datafile/users01.dbf"
     ORA-27040: file create error, unable to create file
     Linux-x86_64 Error: 28: No space left on device
     ```

     **Solution**: Check available space and add more EBS volume capacity:

     ```
     df -h /u01/app/oracle/oradata
     ```
   + **Parameter file errors**

     ```
     RMAN-05021: this configuration cannot be used
     RMAN-06004: ORACLE error from auxiliary database: ORA-01261: Parameter db_create_file_dest destination string cannot be translated
     ```

     **Solution**: Verify all directories in the parameter file exist and have proper permissions.
   + **Password file mismatch**

     ```
     RMAN-00571: ===========================================================
     RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
     RMAN-00571: ===========================================================
     RMAN-03002: failure of duplicate command at 03/03/2026 12:00:00
     RMAN-06136: ORACLE error from auxiliary database: ORA-01017: invalid username/password; logon denied
     ```

     **Solution**: Ensure the password file on the target matches the source and has the correct name (`orapwORCL`).

### Step 8: Open PDBs (multitenant only)
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-8"></a>

After RMAN duplication completes, the CDB on EC2 is open in `READ WRITE` mode, but all PDBs are in `MOUNTED` state. This is expected behavior - you must open them manually.

Check the current PDB status:

```
SQL> SELECT con_id, name, open_mode FROM v$pdbs;
```

Expected output (example with one PDB named `ORCLDB`):

```
CON_ID     NAME                           OPEN_MODE
---------- ------------------------------ ----------
2          PDB$SEED                       READ ONLY
3          ORCLDB                         MOUNTED
```

Open all PDBs:

```
SQL> ALTER PLUGGABLE DATABASE ALL OPEN;
Pluggable database altered.
```

Verify all PDBs are now open in `READ WRITE` mode:

```
SQL> SELECT con_id, name, open_mode, restricted FROM v$pdbs;
```

Expected output:

```
CON_ID     NAME                           OPEN_MODE  RES
---------- ------------------------------ ---------- ---
2          PDB$SEED                       READ ONLY  NO
3          ORCLDB                         READ WRITE NO
```

Configure auto-open on startup using the save state method (recommended for Oracle 19c):

```
SQL> ALTER PLUGGABLE DATABASE ALL SAVE STATE;
Pluggable database altered.
```

This tells Oracle to remember the current open state of PDBs and restore it on CDB startup.

Verify the saved state:

```
SQL> SELECT con_name, instance_name, state FROM dba_pdb_saved_states;
```

Verify PDB services are registered with the listener:

```
lsnrctl services
```

Expected output should show services for the CDB and each PDB. If services aren't showing:

```
SQL> ALTER SYSTEM REGISTER;
```

Then check again with `lsnrctl services`.

### Step 9: Remove RDS Custom objects
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-9"></a>

Because this is now a self-managed database on EC2, you should remove RDS Custom-specific users and objects. The cleanup process differs between non-CDB and multitenant architectures.

**Important**  
Before dropping RDS-specific users and tablespaces, verify that no application objects exist under these schemas:

```
SQL> SELECT owner, object_type, COUNT(*)
FROM dba_objects
WHERE owner IN ('RDSADMIN', 'RDS_DATAGUARD')
  AND object_name NOT LIKE 'RDS%'
  AND object_name NOT LIKE 'SYS_%'
GROUP BY owner, object_type;
```

If any application objects are found, migrate them to appropriate application schemas before proceeding.

**Example Non-CDB:**  

```
SQL> DROP USER RDSADMIN CASCADE;
SQL> DROP USER RDS_DATAGUARD CASCADE;
SQL> DROP DIRECTORY OPATCH_INST_DIR;
SQL> DROP DIRECTORY OPATCH_LOG_DIR;
SQL> DROP DIRECTORY OPATCH_SCRIPT_DIR;
SQL> DROP TABLESPACE RDSADMIN INCLUDING CONTENTS AND DATAFILES;

-- Verify removal
SQL> SELECT username FROM dba_users WHERE username LIKE '%RDS%';
```

Expected output: `no rows selected`

**Multitenant:**

In a multitenant environment, RDS Custom creates common users in `CDB$ROOT` that are visible across all PDBs. You must clean up from `CDB$ROOT`.

```
-- Connect to CDB$ROOT
SQL> SHOW CON_NAME;
-- Check for RDS-specific common users (including C## prefixed users)
SQL> SELECT username, common, con_id FROM cdb_users
WHERE username LIKE '%RDS%' OR username LIKE 'C##RDS%'
ORDER BY username;

-- Drop non-common users
SQL> DROP USER RDSADMIN CASCADE;
SQL> DROP USER RDS_DATAGUARD CASCADE;

-- If any C## common users exist
-- SQL> DROP USER C##RDSADMIN CASCADE
;
-- Drop directories and tablespace
SQL> DROP DIRECTORY OPATCH_INST_DIR;
SQL> DROP DIRECTORY OPATCH_LOG_DIR;
SQL> DROP DIRECTORY OPATCH_SCRIPT_DIR;
SQL> DROP TABLESPACE RDSADMIN INCLUDING CONTENTS AND DATAFILES;

-- Verify removal from CDB$ROOT
SQL> SELECT username FROM dba_users WHERE username LIKE '%RDS%';

-- Verify removal from each PDB
SQL> ALTER SESSION SET CONTAINER = {{<PDB_NAME>}};
SQL> SELECT username FROM dba_users WHERE username LIKE '%RDS%';
```

Expected output for all queries: `no rows selected`

### Step 10: Configure automatic startup
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-10"></a>

Create `SPFILE`:

```
SQL> CREATE SPFILE FROM PFILE='$ORACLE_HOME/dbs/initORCL.ora';
SQL> SHUTDOWN IMMEDIATE;
SQL> STARTUP;
```

For multitenant, ensure PDBs open:

```
SQL> ALTER PLUGGABLE DATABASE ALL OPEN;
```

Edit `/etc/oratab`:

```
ORCL:/u01/app/oracle/product/19.0.0/dbhome_1:Y
```

### Step 11: Final validation
<a name="RDS-Custom-for-Oracle-end-of-support-option-1-step-11"></a>

**Example Non-CDB:**  

```
SQL> SELECT name, open_mode, log_mode FROM v$database;
SQL> SELECT SUM(bytes)/1024/1024/1024 AS size_gb FROM dba_data_files;
SQL> SELECT COUNT(*) FROM dba_objects WHERE status = 'INVALID';
```

**Example Multitenant:**  

```
SQL> SELECT name, open_mode, log_mode, cdb FROM v$database;
SQL> SELECT con_id, name, open_mode FROM v$pdbs;
SQL> SELECT SUM(bytes)/1024/1024/1024 AS total_size_gb FROM cdb_data_files;
SQL> SELECT con_id, COUNT(*) FROM cdb_objects WHERE status = 'INVALID' GROUP BY con_id;
```

```
Test application connectivity:
# Non-CDB
sqlplus {{<app_user>}}/{{<password>}}@{{<EC2_IP>}}:1521/ORCL

# Multitenant (connect to PDB)
sqlplus {{<app_user>}}/{{<password>}}@{{<EC2_IP>}}:1521/{{<PDB_NAME>}}
```

 **Step 12: Resume RDS Custom automation** 

```
aws rds modify-db-instance \
--db-instance-identifier my-custom-instance \
--automation-mode full \
--region us-east-1
```

 

## Option 2: Physical Migration Using Oracle Data Guard
<a name="RDS-Custom-for-Oracle-end-of-support-option-2"></a>



This section provides detailed steps for migrating your Oracle database from RDS Custom for Oracle to EC2 using Oracle Data Guard. This method is suitable for migrations requiring minimal downtime.

### When to use Oracle Data Guard
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-when-use-odg"></a>

**Choose Oracle Data Guard when:**
+ You require minimal downtime (seconds to minutes for switchover)
+ You're migrating production or mission-critical databases
+ You need continuous synchronization before cutover
+ You want built-in fallback capability
+ You need to test the target database before committing to the migration

### Oracle Data Guard overview
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-odg-overview"></a>

Oracle Data Guard maintains a synchronized standby database by continuously shipping and applying redo logs from the primary database. When you're ready to complete the migration, you perform a switchover that promotes the EC2 standby to primary with minimal downtime (seconds to minutes). For multitenant databases, Data Guard automatically protects the entire CDB including all PDBs. Redo generated by any PDB is shipped to the standby and applied to the corresponding PDB on the standby.

### Migration workflow for Oracle Data Guard
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-odg-workflow"></a>

**RDS Custom DB instance (primary) steps:**

1. Pause Amazon RDS Custom automation

1. Verify database architecture (non-CDB or CDB with PDBs)

1. Confirm the primary database is running in archive log mode and `FORCE_LOGGING` is enabled

1. Create a password file

1. Perform an RMAN online backup of the primary database (or use active duplication)

1. Create a parameter file from the source database

1. Copy the backup sets, parameter file, and password file to the target EC2 instance

**EC2 DB instance (standby) steps:**

1. Copy all files from the source to the EC2 instance

1. Copy the password file to the EC2 instance

1. Edit the parameter file for EC2 (architecture-specific)

1. Create the server parameter file from the parameter file

1. Restore standby control file and database

**Data Guard configuration steps:**

1. Configure Oracle listeners on both instances

1. Configure tnsnames.ora on both instances

1. Start the Oracle Data Guard broker on both instances (optional but recommended)

1. Enable Oracle Data Guard configuration

1. Configure fal\_server and fal\_client on the EC2 standby instance

1. Configure the standby redo log files on both instances

1. Recover the standby instance

1. Perform the manual switchover

1. Open the database (and PDBs for multitenant)

1. Configure PDB auto-open (multitenant only)

1. Remove RDS Custom specific users and objects

1. Create SPFILE and configure automatic startup

### Step 1: Pause Amazon RDS Custom automation
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-1"></a>

Pause the automation mode on your RDS Custom instance. The `--resume-full-automation-mode-minute` parameter should be adjusted based on your database size and expected Data Guard setup time.

```
aws rds modify-db-instance \
  --db-instance-identifier my-custom-instance \
  --automation-mode all-paused \
  --resume-full-automation-mode-minute 480 \
  --region us-east-1
```

Validate the automation status:

```
aws rds describe-db-instances \
  --db-instance-identifier my-custom-instance \
  --region us-east-1 \
  --query 'DBInstances[0].AutomationMode'
```

Expected output: "`all-paused`"

### Step 2: Confirm archive log mode and `FORCE_LOGGING`
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-2"></a>

Oracle Data Guard requires the primary database to be in archive log mode with force logging enabled:

```
sqlplus / as sysdba
SQL> SELECT log_mode, force_logging FROM v$database;
```

Expected output:

```
LOG_MODE     FORCE_LOGGING
------------ -------------
ARCHIVELOG   YES
```

If force logging is not enabled, run:

```
SQL> ALTER DATABASE FORCE LOGGING;
```

### Step 3: Create password and parameter files
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-3"></a>

Create a password file using `orapwd`. Retrieve the SYS password from AWS Secrets Manager.

```
# Non-CDB
$ORACLE_HOME/bin/orapwd file=/rdsdbdata/config/orapwORCL password={{<SYS_PASSWORD>}} entries=10

# Multitenant
$ORACLE_HOME/bin/orapwd file=/rdsdbdata/config/orapwRDSCDB password={{<SYS_PASSWORD>}} entries=10
```

Create a parameter file from the source database:

```
sqlplus / as sysdba
SQL> CREATE PFILE='/tmp/initORCL.ora' FROM SPFILE; -- Non-CDB
SQL> CREATE PFILE='/tmp/initRDSCDB.ora' FROM SPFILE; -- Multitenant
```

### Step 4: Perform RMAN backup or use active duplication
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-4"></a>

You have two options for creating the standby database:

#### Option A: RMAN online backup (recommended for most scenarios)
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-4-a"></a>

Create a backup directory and backup the database:

```
mkdir -p /rdsdbdata/backup
rman target /
RMAN> run {
  backup as compressed backupset
  filesperset 2
  format '/rdsdbdata/backup/db_%U'
  database;
  sql 'alter system archive log current';
  backup as compressed backupset
  filesperset 50
  format '/rdsdbdata/backup/arch_%U'
  archivelog all;
}

RMAN> backup current controlfile for standby format '/rdsdbdata/backup/standby.ctl';
```

**Note**  
For multitenant, the database keyword backs up the entire CDB including all PDBs automatically.

#### Option B: Active duplication (alternative method)
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-4-b"></a>

Skip the backup step and use RMAN active duplication to build the standby directly over the network. This eliminates the need for backup storage and file transfers. After configuring TNS and listeners (see below), run:

```
RMAN> DUPLICATE TARGET DATABASE FOR STANDBY FROM ACTIVE DATABASE DORECOVER;
```

This guidance focuses on Option A (backup-based), but Option B is a valid alternative.

### Step 5: Transfer files to EC2
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-5"></a>

Choose your preferred file transfer method. This guidance uses Amazon S3 for examples.

**Using Amazon S3:**

**Example For Non-CDB:**  

```
# Copy files to Amazon S3 from the RDS Custom instance
aws s3 cp /rdsdbdata/backup s3://{{<YOUR_BUCKET>}}/ --recursive
aws s3 cp /tmp/initORCL.ora s3://{{<YOUR_BUCKET>}}/
aws s3 cp /rdsdbdata/config/orapwORCL s3://{{<YOUR_BUCKET>}}/

# On EC2, download files
aws s3 cp s3://{{<YOUR_BUCKET>}}/backup /u01/app/oracle/backup/ --recursive
aws s3 cp s3://{{<YOUR_BUCKET>}}/initORCL.ora $ORACLE_HOME/dbs/
aws s3 cp s3://{{<YOUR_BUCKET>}}/orapwORCL $ORACLE_HOME/dbs/
```

**Example For Multitenant:**  

```
# Copy files to Amazon S3 from the RDS Custom instance
aws s3 cp /rdsdbdata/backup s3://{{<YOUR_BUCKET>}}/ --recursive
aws s3 cp /tmp/initRDSCDB.ora s3://{{<YOUR_BUCKET>}}/
aws s3 cp /rdsdbdata/config/orapwRDSCDB s3://{{<YOUR_BUCKET>}}/

# On EC2, download and rename files to use ORCL naming
aws s3 cp s3://{{<YOUR_BUCKET>}}/backup /u01/app/oracle/backup/ --recursive
aws s3 cp s3://{{<YOUR_BUCKET>}}/initRDSCDB.ora $ORACLE_HOME/dbs/initORCL.ora
aws s3 cp s3://{{<YOUR_BUCKET>}}/orapwRDSCDB $ORACLE_HOME/dbs/orapwORCL
```

### Step 6: Edit parameter file on EC2
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-6"></a>

Edit `$ORACLE_HOME/dbs/initORCL.ora` on the EC2 instance and make these critical changes:

1. **Update database name**: For multitenant, change all occurrences of `RDSCDB` to `ORCL`

1. **Change db\_unique\_name**: From `ORCL_A` (or `RDSCDB_A`) to `ORCL_B`

1. **Convert RDS Custom paths to EC2 paths**: Replace `/rdsdbdata/` with `/u01/app/oracle/`

1. 

****Remove RDS Custom-specific parameters****
   + `dg_broker_config_file1` and `dg_broker_config_file2` (if present)
   + `standby_file_management` (if present)
   + `spfile` (we'll create a new `SPFILE` later)
   + Any `log_archive_dest` parameters pointing to standby destinations

1. **Adjust memory parameters** based on your EC2 instance size (optional but recommended)

 **Path mappings:** 

**Non-CDB:**
+ `/rdsdbdata/db/ORCL_A/datafile/` → `/u01/app/oracle/oradata/ORCL/datafile/`
+ `/rdsdbdata/db/ORCL_A/controlfile/` → `/u01/app/oracle/oradata/ORCL/controlfile/`
+ `/rdsdbdata/db/ORCL_A/onlinelog/` → `/u01/app/oracle/oradata/ORCL/onlinelog/`
+ `/rdsdbdata/admin/ORCL/adump` → `/u01/app/oracle/admin/ORCL/adump`

**Multitenant:**
+ `/rdsdbdata/db/cdb/RDSCDB/datafile/` → `/u01/app/oracle/oradata/ORCL/cdb/datafile/`
+ `/rdsdbdata/db/cdb/pdbseed/` → `/u01/app/oracle/oradata/ORCL/pdbseed/datafile/`
+ `/rdsdbdata/db/pdb/RDSCDB_A/` → `/u01/app/oracle/oradata/ORCL/pdb/datafile/`
+ `/rdsdbdata/db/cdb/RDSCDB_A/controlfile/` → `/u01/app/oracle/oradata/ORCL/controlfile/`
+ `/rdsdbdata/admin/RDSCDB/adump` → `/u01/app/oracle/admin/ORCL/adump`

**Important**: For multitenant, ensure `enable_pluggable_database`=`TRUE` is present in the parameter file.

### Step 7: Create `SPFILE` and restore standby database
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-7"></a>

Start the instance and create SPFILE:

```
sqlplus / as sysdba
SQL> STARTUP NOMOUNT PFILE='$ORACLE_HOME/dbs/initORCL.ora';
SQL> CREATE SPFILE='/u01/app/oracle/admin/ORCL/pfile/spfileORCL.ora' FROM PFILE='$ORACLE_HOME/dbs/initORCL.ora';
SQL> SHUTDOWN IMMEDIATE;
```

Create symbolic link:

```
ln -sfn /u01/app/oracle/admin/ORCL/pfile/spfileORCL.ora $ORACLE_HOME/dbs/spfileORCL.ora
```

Start the instance and restore:

```
SQL> STARTUP NOMOUNT;
rman target /
```

If backup files are in a different path than the source, catalog them first:

```
RMAN> catalog start with '/u01/app/oracle/backup/';
```

Restore standby control file and mount:

```
RMAN> restore standby controlfile from '/u01/app/oracle/backup/standby.ctl';
RMAN> alter database mount;
```

If data file paths differ (e.g., using ASM), use `SET NEWNAME`:

```
RMAN> run {
set newname for database to '+DATA/%b';
restore database;
switch datafile all;
}
```

Otherwise, simply restore:

```
RMAN> restore database;
```

Recover the database to the last available sequence:

```
RMAN> list backup of archivelog all;
RMAN> recover database until sequence <LAST_SEQ + 1>;
```

**Note**  
For multitenant, RMAN automatically restores and recovers all PDBs. You do not need to restore each PDB separately.

### Step 8: Configure TNS and listeners
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-8"></a>

On both instances, add TNS entries to `tnsnames.ora`:

**Example Non-CDB:**  

```
ORCL_A = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{<RDS_CUSTOM_IP>}})(PORT = 1521)) (CONNECT_DATA = (SID = ORCL)))
ORCL_B = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{<EC2_IP>}})(PORT = 1521)) (CONNECT_DATA = (SID = ORCL)))
```

**Example Multitenant:**  

```
RDSCDB_A = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{<RDS_CUSTOM_IP>}})(PORT = 1521)) (CONNECT_DATA = (SID = RDSCDB)))
ORCL_B = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{<EC2_IP>}})(PORT = 1521)) (CONNECT_DATA = (SID = ORCL)))
```

Configure listeners on both instances. On RDS Custom, append to `listener.ora`:

**Example For Non-CDB:**  

```
SID_LIST_L_ORCL_DG=(SID_LIST = (SID_DESC = (SID_NAME = ORCL)(GLOBAL_DBNAME = ORCL) (ORACLE_HOME = /rdsdbbin/oracle.19.custom.r1.EE.1)))
L_ORCL_DG=(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(PORT = 1521)(HOST = {{<RDS_CUSTOM_IP>}})))
```

**Example For Multitenant:**  

```
SID_LIST_L_RDSCDB_DG=(SID_LIST = (SID_DESC = (SID_NAME = RDSCDB)(GLOBAL_DBNAME = RDSCDB) (ORACLE_HOME = /rdsdbbin/oracle.19.custom.r1.EE-CDB.1)))
L_RDSCDB_DG=(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(PORT = 1521)(HOST = {{<RDS_CUSTOM_IP>}})))
```

Start the listener:

```
$ORACLE_HOME/bin/lsnrctl start L_ORCL_DG # or L_RDSCDB_DG for multitenant
```

On EC2, create `$ORACLE_HOME/network/admin/listener.ora`:

```
SID_LIST_L_ORCL_DG=(SID_LIST = (SID_DESC = (SID_NAME = ORCL)(GLOBAL_DBNAME = ORCL) (ORACLE_HOME = /u01/app/oracle/product/19.0.0/dbhome_1)))
L_ORCL_DG=(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(PORT = 1521)(HOST = {{<EC2_IP>}})))
```

Start the listener:

```
$ORACLE_HOME/bin/lsnrctl start L_ORCL_DG
```

**Note**  
You can use the existing listener on RDS Custom if preferred, but creating a separate Data Guard listener provides better isolation.

**Important**  
If `tnsping` or `listener` connectivity fails, check `iptables` rules on EC2. Many EC2 Linux instances have default `iptables` rules that block port 1521. Add a rule: `sudo iptables -I INPUT 5 -p tcp --dport 1521 -j ACCEPT`

### Step 9: Enable Data Guard broker and configuration
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-9"></a>

On both instances, enable the Data Guard broker:

```
sqlplus / as sysdba
SQL> ALTER SYSTEM SET dg_broker_start=true;
```

On the RDS Custom primary, connect to the Data Guard broker and create the configuration:

```
dgmgrl /
```

**Example For Non-CDB:**  

```
DGMGRL> CREATE CONFIGURATION my_dg_config AS PRIMARY DATABASE IS ORCL_A CONNECT IDENTIFIER IS ORCL_A;
DGMGRL> ADD DATABASE ORCL_B AS CONNECT IDENTIFIER IS ORCL_B MAINTAINED AS PHYSICAL;
```

 

**Example For Multitenant:**  

```
DGMGRL> CREATE CONFIGURATION my_dg_config AS PRIMARY DATABASE IS RDSCDB_A CONNECT IDENTIFIER IS RDSCDB_A;
DGMGRL> ADD DATABASE ORCL_B AS CONNECT IDENTIFIER IS ORCL_B MAINTAINED AS PHYSICAL;
```

Set static connect identifiers and enable:

 

**Example For Non-CDB:**  

```
DGMGRL> edit database orcl_a set property StaticConnectIdentifier='(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(PORT=1521)(HOST=<RDS_CUSTOM_IP>))(CONNECT_DATA=(SID=ORCL)(SERVER=DEDICATED)))';
DGMGRL> edit database orcl_b set property StaticConnectIdentifier='(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(PORT=1521)(HOST={{<EC2_IP>}}))(CONNECT_DATA=(SID=ORCL)(SERVER=DEDICATED)))';
DGMGRL> ENABLE CONFIGURATION;
```

 

**Example For Multitenant:**  

```
DGMGRL> edit database rdscdb_a set property StaticConnectIdentifier='(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(PORT=1521)(HOST=<RDS_CUSTOM_IP>))(CONNECT_DATA=(SID=RDSCDB)(SERVER=DEDICATED)))';
DGMGRL> edit database orcl_b set property StaticConnectIdentifier='(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(PORT=1521)(HOST={{<EC2_IP>}}))(CONNECT_DATA=(SID=ORCL)(SERVER=DEDICATED)))';
DGMGRL> ENABLE CONFIGURATION;
```

**Note**  
Data Guard broker is optional but recommended for easier management. For simple migrations, you can configure Data Guard manually without the broker.

**Note**  
When you enable Data Guard for a CDB, it automatically protects all PDBs. Redo generated by any PDB is shipped to the standby and applied to the corresponding PDB on the standby.

### Step 10: Configure standby redo logs and start recovery
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-10"></a>

On the EC2 standby instance, add standby redo log files (n\+1 where n is the number of online redo log groups):

```
ALTER DATABASE ADD STANDBY LOGFILE ('slog1.rdo') SIZE 128M;
ALTER DATABASE ADD STANDBY LOGFILE ('slog2.rdo') SIZE 128M;
ALTER DATABASE ADD STANDBY LOGFILE ('slog3.rdo') SIZE 128M;
ALTER DATABASE ADD STANDBY LOGFILE ('slog4.rdo') SIZE 128M;
ALTER DATABASE ADD STANDBY LOGFILE ('slog5.rdo') SIZE 128M;
```

**Note**  
For multitenant, standby redo logs are created at the CDB level and are shared by all PDBs.

Configure FAL parameters on the standby:

 

**Example For Non-CDB:**  

```
SQL> alter system set fal_server = 'ORCL_A';
SQL> alter system set fal_client = 'ORCL_B';
```

 

**Example For Multitenant:**  

```
SQL> alter system set fal_server = 'RDSCDB_A';
SQL> alter system set fal_client = 'ORCL_B';
```

Start managed recovery:

```
SQL> recover managed standby database disconnect from session;
```

Monitor the apply lag:

```
SQL> SELECT name, value FROM v$dataguard_stats WHERE name = 'apply lag';
```

**Detailed monitoring and management of Data Guard synchronization:**

Monitoring Data Guard is critical to ensure successful migration. Here are comprehensive monitoring techniques:

1. **Monitor Data Guard statistics:**

   ```
   -- Comprehensive Data Guard statistics
   SQL> SELECT name, value, unit, time_computed, datum_time
   FROM v$dataguard_stats
   ORDER BY name;
   ```

   Key metrics to monitor:
   + transport lag: Time difference between when redo was generated on primary and received on standby
   + apply lag: Time difference between when redo was generated and applied on standby
   + apply rate: Rate at which redo is being applied (MB/sec)
   + redo received: Total redo received by standby
   + redo applied: Total redo applied by standby

1. **Monitor archive log shipping:**

   On the primary (RDS Custom):

   ```
   -- Check archive log generation rate
   SQL> SELECT TO_CHAR(first_time, 'YYYY-MM-DD HH24') AS hour,
          COUNT(*) AS log_count,
          ROUND(SUM(blocks * block_size)/1024/1024/1024, 2) AS size_gb
   FROM v$archived_log
   WHERE first_time > SYSDATE - 1
   GROUP BY TO_CHAR(first_time, 'YYYY-MM-DD HH24')
   ORDER BY hour;
   
   -- Check archive log destination status
   SQL> SELECT dest_id, status, error, destination
   FROM v$archive_dest
   WHERE status != 'INACTIVE';
   ```

   On the standby (EC2):

   ```
   -- Check archive log apply status
   SQL> SELECT sequence#, first_time, next_time, applied
   FROM v$archived_log
   WHERE applied = 'NO'
   ORDER BY sequence#;
   
   -- Check archive log gap
   SQL> SELECT thread#, low_sequence#, high_sequence#
   FROM v$archive_gap;
   ```

1. **Monitor managed recovery process:**

   ```
   -- Check if managed recovery is running
   SQL> SELECT process, status, thread#, sequence#, block#, blocks
   FROM v$managed_standby
   WHERE process LIKE 'MRP%' OR process LIKE 'RFS%';
   
   -- Check recovery progress
   SQL> SELECT process, status, sequence#,
          TO_CHAR(timestamp, 'YYYY-MM-DD HH24:MI:SS') AS timestamp
   FROM v$managed_standby
   ORDER BY process;
   ```

1. **Monitor redo apply rate for multitenant:**

   For multitenant databases, monitor apply rate per PDB:

   ```
   -- Check redo apply rate per container
   SQL> SELECT con_id, name,
          ROUND(SUM(value)/1024/1024, 2) AS redo_applied_mb
   FROM v$con_sysstat cs, v$containers c
   WHERE cs.con_id = c.con_id
     AND cs.name = 'redo size'
   GROUP BY con_id, name
   ORDER BY con_id;
   ```

1. **Monitor standby redo logs:**

   ```
   -- Check standby redo log status
   SQL> SELECT group#, thread#, sequence#, bytes/1024/1024 AS size_mb, status
   FROM v$standby_log
   ORDER BY group#;
   
   -- Check if standby redo logs are being used
   SQL> SELECT group#, thread#, sequence#, status, archived
   FROM v$standby_log
   WHERE status = 'ACTIVE';
   ```

1. **Estimate synchronization completion:**

   Calculate the remaining time based on apply rate:

   ```
   -- Calculate estimated time to catch up
   SQL> SELECT
          ROUND((SELECT value FROM v$dataguard_stats WHERE name = 'apply lag')/60, 2) AS lag_minutes,
          ROUND((SELECT value FROM v$dataguard_stats WHERE name = 'apply rate')/1024, 2) AS apply_rate_mbps,
          ROUND(
            (SELECT value FROM v$dataguard_stats WHERE name = 'apply lag') /
            NULLIF((SELECT value FROM v$dataguard_stats WHERE name = 'apply rate'), 0) / 60,
            2
          ) AS estimated_catchup_minutes
   FROM dual;
   ```

#### Common Data Guard synchronization issues:
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-10-common-issues"></a>



##### Issue 1: High apply lag
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-10-common-issues-1"></a>

Symptoms:

```
SQL> SELECT name, value FROM v$dataguard_stats WHERE name = 'apply lag';
NAME                             VALUE
-------------------------------- -----
apply lag                        +00 01:30:00
```

Causes and solutions:
+ **Insufficient CPU/IO on standby**: Upgrade EC2 instance type or increase EBS IOPS
+ **Network bandwidth limitation**: Use enhanced networking or higher bandwidth instance types
+ **Multiple PDBs with high transaction rate**: Consider increasing redo apply parallelism (requires Active Data Guard license)

```
-- Increase apply parallelism (requires Active Data Guard)
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE PARALLEL 4 DISCONNECT FROM SESSION;
```

##### Issue 2: Archive log gap
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-10-common-issues-2"></a>

Symptoms:

```
SQL> SELECT * FROM v$archive_gap;
THREAD# LOW_SEQUENCE# HIGH_SEQUENCE#
------- ------------- --------------
      1          1234           1240
```

Solution:

```
-- FAL (Fetch Archive Log) will automatically fetch missing logs
-- Verify FAL parameters are set correctly
SQL> SHOW PARAMETER fal_server
SQL> SHOW PARAMETER fal_client

-- Manually register missing archive logs if needed
-- On primary, check if logs still exist
SQL> SELECT name FROM v$archived_log WHERE sequence# BETWEEN 1234 AND 1240;

-- If logs are missing on primary, you may need to rebuild the standby
```

##### Issue 3: Redo transport failure
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-10-common-issues-3"></a>

Symptoms:

```
SQL> SELECT dest_id, status, error FROM v$archive_dest WHERE dest_id = 2;
DEST_ID STATUS    ERROR
------- --------- ----------------------------------------
2       ERROR     ORA-16191: Primary log shipping client not logged on standby
```

Solution:

```
-- Check network connectivity
-- Verify TNS configuration
-- Check listener status on standby
-- Restart log transport

SQL> ALTER SYSTEM SET log_archive_dest_state_2 = 'DEFER';
SQL> ALTER SYSTEM SET log_archive_dest_state_2 = 'ENABLE';
```

##### Issue 4: Managed recovery not applying redo
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-10-common-issues-4"></a>

Symptoms:

```
SQL> SELECT process, status FROM v$managed_standby WHERE process = 'MRP0';
PROCESS   STATUS
--------- ------------
MRP0      WAIT_FOR_LOG
```

Solution:

```
# Check if archive logs are arriving
ls -ltr /u01/app/oracle/oradata/ORCL/arch/

# Check alert log for errors
tail -100 $ORACLE_BASE/diag/rdbms/orcl_b/ORCL/trace/alert_ORCL.log

# Restart managed recovery
sqlplus / as sysdba
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE DISCONNECT FROM SESSION;
```

**For Multitenant**, you can also check the status of each PDB on the standby:

```
SQL> SELECT con_id, name, open_mode, restricted FROM v$pdbs;
```

Expected output (PDBs in `MOUNTED` state on standby):

```
CON_ID     NAME                           OPEN_MODE  RES
---------- ------------------------------ ---------- ---
2          PDB$SEED                       MOUNTED
3          ORCLDB                         MOUNTED
```

**Note**  
On a physical standby, PDBs remain in `MOUNTED` state during managed recovery.

### Step 11: Perform the switchover
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-11"></a>

Once you are satisfied that the standby is fully synchronized and ready, perform the switchover. For multitenant, the switchover will switch the entire CDB (all PDBs) from the RDS Custom primary to the EC2 standby.

On the RDS Custom primary instance, connect to the Data Guard broker and validate both databases are ready for switchover:

**Example For Non-CDB:**  

```
DGMGRL> VALIDATE DATABASE ORCL_A;
DGMGRL> VALIDATE DATABASE ORCL_B;
```

 

**Example For Multitenant:**  

```
DGMGRL> VALIDATE DATABASE RDSCDB_A;
DGMGRL> VALIDATE DATABASE ORCL_B;
```

Both should show `Ready for Switchover: Yes`

Switch over from the RDS Custom primary to the EC2 standby:

```
DGMGRL> SWITCHOVER TO ORCL_B;
```

Verify the switchover is successful:

```
DGMGRL> SHOW CONFIGURATION VERBOSE;
```

The EC2 instance (`ORCL_B`) is now the primary database, and the RDS Custom instance is the physical standby.

### Step 12: Open PDBs (multitenant only)
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-12"></a>

After the switchover, the CDB on EC2 is open in READ WRITE mode, but all PDBs are in MOUNTED state. You must open them manually.

Connect to the new primary on EC2:

```
sqlplus / as sysdba
SQL> SELECT name, open_mode, database_role, cdb FROM v$database;
```

Expected output:

```
NAME      OPEN_MODE            DATABASE_ROLE    CDB
--------- -------------------- ---------------- ---
ORCL      READ WRITE           PRIMARY          YES
```

Check the current PDB status:

```
SQL> SELECT con_id, name, open_mode, restricted FROM v$pdbs;
```

Expected output (PDBs in `MOUNTED` state - example with one PDB named `ORCLDB`):

```
CON_ID     NAME                           OPEN_MODE  RES
---------- ------------------------------ ---------- ---
2          PDB$SEED                       READ ONLY  NO
3          ORCLDB                         MOUNTED
```

Open all PDBs:

```
SQL> ALTER PLUGGABLE DATABASE ALL OPEN;
```

Pluggable database altered.

Verify all PDBs are now open in `READ WRITE` mode:

```
SQL> SELECT con_id, name, open_mode, restricted FROM v$pdbs;
```

Expected output:

```
CON_ID     NAME                           OPEN_MODE  RES
---------- ------------------------------ ---------- ---
2          PDB$SEED                       READ ONLY  NO
3          ORCLDB                         READ WRITE NO
```

### Step 13: Configure PDB auto-open on startup (multitenant only)
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-13"></a>

Configure PDBs to automatically open when the CDB starts using the save state method (recommended for Oracle 19c):

```
SQL> ALTER PLUGGABLE DATABASE ALL SAVE STATE;
Pluggable database altered.
```

Verify the saved state:

```
SQL> SELECT con_name, instance_name, state FROM dba_pdb_saved_states;
```

Verify PDB services are registered with the listener:

```
lsnrctl services
```

Expected output should show services for the CDB and each PDB. If services aren't showing:

```
SQL> ALTER SYSTEM REGISTER;
```

Then check again with `lsnrctl services`.

### Step 14: Remove RDS Custom objects
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-14"></a>

Because this is now a self-managed database on EC2, you should remove RDS Custom specific users and objects. The cleanup process differs slightly between non-CDB and multitenant architectures.

**Important**  
Before dropping RDS-specific users and tablespaces, verify that no application objects exist under these schemas:

```
SQL> SELECT owner, object_type, COUNT(*)
FROM dba_objects
WHERE owner IN ('RDSADMIN', 'RDS_DATAGUARD')
  AND object_name NOT LIKE 'RDS%'
  AND object_name NOT LIKE 'SYS_%'
GROUP BY owner, object_type;
```

If any application objects are found, migrate them to appropriate application schemas before proceeding.

**Non-CDB cleanup:**

```
sqlplus / as sysdba

-- Drop RDS-specific users
SQL> DROP USER RDSADMIN CASCADE;
SQL> DROP USER RDS_DATAGUARD CASCADE;

-- Drop RDS-specific directories
SQL> DROP DIRECTORY OPATCH_INST_DIR;
SQL> DROP DIRECTORY OPATCH_LOG_DIR;
SQL> DROP DIRECTORY OPATCH_SCRIPT_DIR;

-- Drop the RDSADMIN tablespace
SQL> DROP TABLESPACE RDSADMIN INCLUDING CONTENTS AND DATAFILES;

-- Verify removal
SQL> SELECT username FROM dba_users WHERE username LIKE '%RDS%';
```

Expected output: `no rows selected`

**Multitenant cleanup:**

In a multitenant environment, RDS Custom creates common users in `CDB$ROOT` that are visible across all PDBs. You must clean up from `CDB$ROOT`.

```
sqlplus / as sysdba

-- Verify you are in CDB$ROOT
SQL> SHOW CON_NAME;

-- Check for RDS-specific common users (including C## prefixed users)
SQL> SELECT username, common, con_id FROM cdb_users
WHERE username LIKE 'RDS%' OR username LIKE 'C##RDS%'
ORDER BY username;

-- Drop non-common users
SQL> DROP USER RDSADMIN CASCADE;
SQL> DROP USER RDS_DATAGUARD CASCADE;

-- If any C## common users exist
-- Example (adjust based on your findings):
-- SQL> DROP USER C##RDS_DATAGUARD CASCADE;
-- Drop RDS-specific directories
SQL> DROP DIRECTORY OPATCH_INST_DIR;
SQL> DROP DIRECTORY OPATCH_LOG_DIR;
SQL> DROP DIRECTORY OPATCH_SCRIPT_DIR;

-- Drop the RDSADMIN tablespace
SQL> DROP TABLESPACE RDSADMIN INCLUDING CONTENTS AND DATAFILES;

-- Verify removal from CDB$ROOT
SQL> SELECT username FROM dba_users WHERE username LIKE '%RDS%';

-- Verify removal from each PDB (example with one PDB named ORCLDB)
SQL> ALTER SESSION SET CONTAINER = ORCLDB;
SQL> SELECT username FROM dba_users WHERE username LIKE '%RDS%';
```

Expected output for all queries: no rows selected

### Step 15: Configure automatic startup
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-15"></a>

Verify the `SPFILE` is being used:

```
sqlplus / as sysdba
SQL> SHOW PARAMETER spfile;
```

If the `spfile` path is correct, no action is needed. If not, create one:

```
SQL> CREATE SPFILE FROM MEMORY;
```

Restart the database:

```
SQL> SHUTDOWN IMMEDIATE;
SQL> STARTUP;
```

For multitenant, open all PDBs (they should auto-open if you saved state earlier):

```
SQL> SELECT con_id, name, open_mode FROM v$pdbs;
```

If PDBs are not open, open them manually:

```
SQL> ALTER PLUGGABLE DATABASE ALL OPEN;
```

Edit `/etc/oratab`:

```
vi /etc/oratab
```

Change the line for `ORCL` from `N` to `Y`:

```
ORCL:/u01/app/oracle/product/19.0.0/dbhome_1:Y
```

### Step 16: Final validation
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-16"></a>

Perform comprehensive validation on the migrated database.

**Example For Non-CDB:**  

```
sqlplus / as sysdba

-- Verify database role and status
SQL> SELECT name, open_mode, log_mode, database_role FROM v$database;

-- Check database size
SQL> SELECT SUM(bytes)/1024/1024/1024 AS size_gb FROM dba_data_files;

-- Verify all objects are valid
SQL> SELECT owner, object_type, COUNT(*)
     FROM dba_objects
     WHERE status = 'INVALID'
     GROUP BY owner, object_type;

-- Verify data files
SQL> SELECT name, status FROM v$datafile;

-- Test application connectivity
SQL> SELECT username, machine, program FROM v$session WHERE username IS NOT NULL;
```

**Example For Multitenant:**  

```
sqlplus / as sysdba

-- Verify CDB status
SQL> SELECT name, open_mode, log_mode, cdb, database_role FROM v$database;

-- Verify all PDBs are open
SQL> SELECT con_id, name, open_mode, restricted FROM v$pdbs;

-- Check total CDB size
SQL> SELECT SUM(bytes)/1024/1024/1024 AS total_size_gb FROM cdb_data_files;

-- Check size per PDB
SQL> SELECT p.name AS pdb_name,
       ROUND(SUM(d.bytes)/1024/1024/1024, 2) AS size_gb
FROM v$pdbs p
JOIN cdb_data_files d ON p.con_id = d.con_id
GROUP BY p.name,p.con_id
ORDER BY p.con_id;

-- Verify all objects are valid across all PDBs
SQL> SELECT con_id, owner, object_type, COUNT(*)
     FROM cdb_objects
     WHERE status = 'INVALID'
     GROUP BY con_id, owner, object_type;

-- Verify PDB services are registered
SQL> SELECT name FROM v$services ORDER BY name;

Test application connectivity:

# Non-CDB
sqlplus {{<app_user>}}/{{<password>}}@{{<EC2_IP>}}:1521/ORCL

# Multitenant (connect to PDB)
sqlplus {{<app_user>}}/{{<password>}}@{{<EC2_IP}}>:1521/{{<PDB_NAME>}}
```

Test application connectivity:

```
# Non-CDB
sqlplus {{<app_user>}}/{{<password>}}@{{<EC2_IP>}}:1521/ORCL

# Multitenant (connect to PDB)
sqlplus {{<app_user>}}/{{<password>}}@{{<EC2_IP>}}:1521/{{<PDB_NAME>}}
```

### Step 17: Clean up backup files
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-17"></a>

After successful validation, remove backup files and detach the backup volume if using a separate EBS volume:

```
rm -rf /u01/app/oracle/backup/*
```

If using a separate EBS volume for backups:

```
# Unmount the volume
sudo umount /u01/app/oracle/backup

# Detach and delete the EBS volume from AWS Console or CLI
aws ec2 detach-volume --volume-id {{<volume-id>}}
aws ec2 delete-volume --volume-id {{<volume-id>}}
```

### Step 18: Resume RDS Custom automation
<a name="RDS-Custom-for-Oracle-end-of-support-option-2-step-18"></a>

If you plan to keep the RDS Custom instance running as a fallback during a validation period, resume the automation:

```
aws rds modify-db-instance \
  --db-instance-identifier my-custom-instance \
  --automation-mode full \
  --region us-east-1
```

## Troubleshooting common issues
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting"></a>



This section covers common issues you may encounter during migration for both RMAN duplication and Oracle Data Guard approaches, covering both non-CDB and multitenant architectures.

### ORA-09925: Unable to create audit trail file
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-ora-09925"></a>

**Cause:** The audit directory specified in `audit_file_dest` parameter doesn't exist on the target EC2 instance.

 **Solution:** 

Ensure the audit directory exists and has proper permissions:

```
mkdir -p /u01/app/oracle/admin/ORCL/adump
chown -R oracle:oinstall /u01/app/oracle/admin/ORCL
chmod -R 755 /u01/app/oracle/admin/ORCL
```

### ORA-01261: Parameter `db_create_file_dest` destination string cannot be translated
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-ora-01261"></a>

**Cause:** The directory specified in `db_create_file_dest` parameter doesn't exist on the target EC2 instance.

 **Solution:** 

For non-CDB:

```
mkdir -p /u01/app/oracle/oradata/ORCL
chown -R oracle:oinstall /u01/app/oracle/oradata/ORCL
chmod -R 755 /u01/app/oracle/oradata/ORCL
```

For multitenant:

```
mkdir -p /u01/app/oracle/oradata/ORCL/pdb/datafile
chown -R oracle:oinstall /u01/app/oracle/oradata/ORCL
chmod -R 755 /u01/app/oracle/oradata/ORCL
```

### ORA-01804: Failure to initialize timezone information
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-ora-01804"></a>

This error can occur when dropping the `RDSADMIN` user if the RDS source has a higher timezone version than what's installed in your EC2 $ORACLE\_HOME.

 **Solution:** 

1. Check the timezone versions:

   ```
   SELECT * FROM v$timezone_file;
   SELECT PROPERTY_NAME, PROPERTY_VALUE
   FROM database_properties
   WHERE PROPERTY_NAME LIKE '%DST%';
   ```

1. As a workaround, set the timezone file environment variable to match what your $ORACLE\_HOME has available:

   ```
   ls $ORACLE_HOME/oracore/zoneinfo/timezlrg_*.dat
   export ORA_TZFILE=$ORACLE_HOME/oracore/zoneinfo/timezone_40.dat
   ```

   Adjust the number to match the version available in your installation.

1. Retry the drop:

   ```
   sqlplus / as sysdba
   SQL> DROP USER RDSADMIN CASCADE;
   ```

### Cross-RU migration issues (different Release Updates)
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-cross-ru-migration"></a>

**Cause:** The target EC2 instance has a different Oracle Release Update (RU) or one-off patches than the source RDS Custom instance, causing compatibility errors during or after migration.

**Common errors:**
+ ORA-00600 internal errors during redo apply (Data Guard)
+ ORA-39700 database must be opened with `UPGRADE` option
+ Dictionary inconsistencies after migration
+ Invalid objects in `DBA_REGISTRY` or `DBA_OBJECTS`

 **Solution:** 

 **Best practice - Match RU versions and one-off patches exactly:** 

1. Check the exact RU version on both source and target:

   ```
   -- On both source and target
   SQL> SELECT * FROM v$version;
   
   SQL> SELECT patch_id, patch_uid, version, action, status, description
   FROM dba_registry_sqlpatch
   ORDER BY action_time DESC;
   ```

1. Verify the $ORACLE\_HOME patch level:

   ```
   # On both instances
   $ORACLE_HOME/OPatch/opatch lsinventory
   ```

1. If versions don't match, align them before migration by applying or rolling back patches as needed.

1. If you must proceed with mismatched RUs, run datapatch after migration:

   ```
   cd $ORACLE_HOME/OPatch
   ./datapatch -verbose
   ```

1. Check for invalid objects and recompile:

   ```
   SQL> @?/rdbms/admin/utlrp.sql
   
   SQL> SELECT owner, object_type, COUNT(*)
   FROM dba_objects
   WHERE status = 'INVALID'
   GROUP BY owner, object_type;
   ```

### Network connectivity issues
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-network-connectivity"></a>

 

**Cause:** Security groups, network ACLs, or `iptables` blocking the Oracle listener port.

 **Solution:** 

1. Verify security groups allow the port bidirectionally

1. Check iptables on EC2:

   ```
   sudo iptables -L INPUT -n -v
   ```

1. Add rule if needed:

   ```
   # Insert rule before the REJECT rule (typically position 5)
   sudo iptables -I INPUT 5 -p tcp --dport 1521 -j ACCEPT
   
   # For enhanced security, allow only from specific source IPs
   sudo iptables -I INPUT 5 -p tcp -s {{<RDS_Custom_IP>}} --dport 1521 -j ACCEPT
   
   # Save rules permanently
   sudo service iptables save
   ```

1. Test connectivity:

   ```
   telnet {{<EC2_instance_IP>}} 1521
   tnsping DB_SOURCE
   tnsping DB_TARGET
   ```

### PDBs not opening after migration (multitenant only)
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-pdbs-not-opening"></a>

**Cause:** This is expected behavior. After RMAN duplication or Data Guard switchover, the CDB is open but PDBs are in `MOUNTED` state.

 **Solution:** 

Open them manually:

```
SQL> ALTER PLUGGABLE DATABASE ALL OPEN;
```

If a specific PDB fails to open, check the alert log for errors:

```
tail -100 $ORACLE_BASE/diag/rdbms/orcl/ORCL/trace/alert_ORCL.log
```

Common causes include missing data files or path mapping issues.

### PDB data files not found or path mismatch (multitenant only)
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-pdb-data-files-not-found"></a>

**Cause:** The migration didn't map all source paths correctly, especially for OMF-based PDB data files.

 **Solution:** 

1. Check which data files are missing:

   ```
   SQL> SELECT name, status FROM v$datafile WHERE status != 'ONLINE';
   ```

1. If the files were placed in the wrong directory, rename them in the control file:

   ```
   SQL> ALTER DATABASE RENAME FILE '/wrong/path/datafile.dbf' TO '/correct/path/datafile.dbf';
   ```

1. To prevent this, always verify the source data file paths with `SELECT con_id, name FROM v$datafile ORDER BY con_id;` before configuring the parameter file.

### PDB services not registering with listener (multitenant only)
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-pdb-services-not-registering"></a>

**Cause:** The listener is not aware of the PDB services after opening PDBs.

 **Solution:** 

1. Force service registration:

   ```
   SQL> ALTER SYSTEM REGISTER;
   ```

1. If services still don't appear, check the `local_listener` parameter:

   ```
   SQL> SHOW PARAMETER local_listener;
   ```

   Ensure it points to the correct listener address. If needed, update it:

   ```
   SQL> ALTER SYSTEM SET local_listener='(ADDRESS=(PROTOCOL=TCP)(HOST={{<EC2_instance_IP>}})(PORT=1521))';
   SQL> ALTER SYSTEM REGISTER;
   ```

1. Verify with:

   ```
   lsnrctl services
   ```

### PDBs not auto-opening after CDB restart (multitenant only)
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-pdbs-not-opening-after-cdb-restart"></a>

**Cause:** PDB save state was not configured.

 **Solution:** 

Verify that PDB save state was configured:

```
SQL> SELECT con_name, instance_name, state FROM dba_pdb_saved_states;
```

If no rows are returned, save the state:

```
SQL> ALTER PLUGGABLE DATABASE ALL OPEN;
SQL> ALTER PLUGGABLE DATABASE ALL SAVE STATE;
```

### Data Guard redo transport not working
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-odg-redo-transport-failure"></a>

**Cause:** Network connectivity issues, incorrect TNS configuration, or FAL parameters not set.

 **Solution:** 

1. Verify the standby is in MOUNT mode:

   ```
   SQL> SELECT status FROM v$instance;
   ```

1. Check fal\_server and fal\_client are set correctly on the standby:

   ```
   SQL> SHOW PARAMETER fal_server
   SQL> SHOW PARAMETER fal_client
   ```

1. Verify network connectivity:

   ```
   tnsping ORCL_A # or RDSCDB_A for multitenant
   ```

1. Check the log\_archive\_dest\_2 parameter on the primary points to the standby (if configured manually without broker).

 **Data Guard apply lag increasing with multiple PDBs (multitenant only)** 

**Cause:** For CDBs with multiple PDBs, redo apply can be slower due to the volume of changes across all containers.

 **Solution:** 

1. Check the apply rate:

   ```
   SQL> SELECT name, value, unit FROM v$dataguard_stats WHERE name IN ('apply rate', 'apply lag');
   ```

1. Consider increasing parallelism for redo apply (requires Active Data Guard license):

   ```
   SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
   SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE PARALLEL 4 DISCONNECT FROM SESSION;
   ```

1. Verify there are no resource constraints (CPU, I/O) on the standby instance.

 **RMAN archive log backup fails with ORA-19625** 

**Cause:** RDS Custom automation has purged older archive logs from disk, but RMAN's control file still has records of them.

 **Solution:** 

1. Crosscheck and clean up stale archive log entries:

   ```
   RMAN> CROSSCHECK ARCHIVELOG ALL;
   RMAN> DELETE NOPROMPT EXPIRED ARCHIVELOG ALL;
   ```

1. Re-run just the archive log backup:

   ```
   RMAN> RUN {
   SQL 'ALTER SYSTEM ARCHIVE LOG CURRENT';
   BACKUP AS COMPRESSED BACKUPSET
   FILESPERSET 50
   FORMAT '/rdsdbdata/backup/arch_%U'
   ARCHIVELOG ALL;
   }
   ```

### Common user drop fails in multitenant (multitenant only)
<a name="RDS-Custom-for-Oracle-end-of-support-troubleshoting-multitenant-user-drop-fails"></a>

 

**Cause:** Common users (prefixed with C\#\#) must be dropped with the `CONTAINER=ALL` clause.

 **Solution:** 

```
-- For common users
SQL> DROP USER C##RDS_DATAGUARD CASCADE CONTAINER=ALL;

-- For non-common users in CDB$ROOT
SQL> DROP USER RDSADMIN CASCADE;
```

Verify you're connected to `CDB$ROOT`:

```
SQL> SHOW CON_NAME;
```

## Post-migration tasks
<a name="RDS-Custom-for-Oracle-end-of-support-post-migration"></a>

After successful migration, complete these additional tasks to ensure your self-managed Oracle database on EC2 is production-ready.

 **Update application connection strings** 

**For Non-CDB:**
+ Point your applications to the new EC2 instance endpoint
+ Update connection strings to use the EC2 instance IP or hostname
+ Test all application functionality thoroughly

**For Multitenant:**
+ Point your applications to the new EC2 instance PDB service names (e.g., ORCLDB or your specific PDB names)
+ Ensure applications connect to the correct PDB, not the CDB
+ Update connection strings to use PDB service names
+ Test all application functionality for each PDB

Example connection strings:

```
# Non-CDB
jdbc:oracle:thin:@{{<EC2_IP>}}:1521/ORCL

# Multitenant (connect to PDB)
jdbc:oracle:thin:@{{<EC2_IP>}}:1521/ORCLDB
```

 **Configure backup strategy** 

Set up a comprehensive backup strategy for your self-managed database:

**RMAN backups:**
+ Configure automated RMAN backup scripts for full, incremental, and archive log backups
+ Set up backup retention policies based on your recovery point objectives (RPO)
+ Store backups on Amazon S3 for durability and cost-effectiveness
+ Regularly test backup restoration procedures

**AWS Backup:**
+ Use [AWS Backup](https://aws.amazon.com/backup/) for EBS volume snapshots
+ Configure backup schedules and retention policies
+ Enable cross-region backup copies for disaster recovery

**For Multitenant:**
+ RMAN backups of the CDB automatically include all PDBs
+ You can also back up individual PDBs if needed
+ Consider PDB-specific backup schedules based on business requirements

Example RMAN backup script:

```
#!/bin/bash
export ORACLE_HOME=/u01/app/oracle/product/19.0.0/dbhome_1
export ORACLE_SID=ORCL
export PATH=$ORACLE_HOME/bin:$PATH
rman target / << EOF
run {
  backup as compressed backupset database plus archivelog;
  delete noprompt obsolete;
}
exit;
EOF
```

 **Set up monitoring** 

Implement comprehensive monitoring for your EC2-hosted Oracle database:

**Amazon CloudWatch**
+ Set up CloudWatch metrics for EC2 instance health, disk usage, and custom Oracle metrics
+ Create CloudWatch alarms for critical thresholds
+ Use CloudWatch Logs for database alert log monitoring

**Oracle Enterprise Manager (OEM):**
+ If available, configure OEM for database monitoring
+ Set up performance monitoring and diagnostics
+ Configure automated alerts for critical events

**Third-party tools:**
+ Consider tools like Datadog, New Relic, or Prometheus for database monitoring
+ Integrate with your existing monitoring infrastructure

**Key metrics to monitor:**
+ Tablespace usage
+ Archive log space
+ Invalid objects
+ Session counts
+ Wait events
+ CPU and memory utilization
+ I/O performance

**For Multitenant:**
+ Monitor both CDB-level and PDB-level metrics
+ Set up alerts for PDB resource usage and quotas
+ Track PDB-specific performance metrics

 **Configure security groups and network ACLs** 

Review and tighten security for the EC2 instance:

**Security groups:**
+ Restrict database port access to only authorized application servers and bastion hosts
+ Remove any overly permissive rules created during migration
+ Document security group rules and their purposes

**Network ACLs:**
+ Configure VPC network ACLs for additional security layers
+ Implement defense-in-depth security strategy

**SSH access:**
+ Limit SSH access to specific IP ranges or use AWS Systems Manager Session Manager
+ Disable password authentication and use key-based authentication only
+ Implement multi-factor authentication (MFA) for privileged access

**Encryption:**
+ Enable encryption at rest for EBS volumes
+ Enable encryption in transit for database connections using Oracle Native Network Encryption or TLS
+ Rotate encryption keys regularly

**Implement high availability**

If your workload requires high availability, consider implementing:

**Oracle Data Guard:**
+ Configure a new standby database on another EC2 instance for disaster recovery
+ For multitenant, Data Guard protects the entire CDB including all PDBs
+ The standby can be in a different Availability Zone or Region
+ Implement automated failover mechanisms using scripts or third-party tools

**AWS Multi-AZ deployment:**
+ Deploy standby instances in different Availability Zones
+ Use Amazon Route 53 for DNS failover
+ Implement application-level connection pooling with failover support

**Backup and recovery:**
+ Maintain regular backups with tested restore procedures
+ Document recovery time objectives (RTO) and recovery point objectives (RPO)
+ Conduct regular disaster recovery drills

**Perform thorough application testing**

Before decommissioning the RDS Custom instance:

**Functional testing:**
+ Verify all application features work correctly
+ Test all database-dependent functionality
+ Validate data integrity and consistency

**Performance testing:**
+ Compare performance metrics with the RDS Custom baseline
+ Identify and address any performance regressions
+ Optimize queries and indexes as needed

**Load testing:**
+ Test the database under expected peak loads
+ Verify resource utilization stays within acceptable limits
+ Identify and address any bottlenecks

**Failover testing (if HA is configured):**
+ Test failover scenarios
+ Verify application reconnection logic
+ Measure actual RTO and RPO

**Backup and restore testing:**
+ Verify backup and restore procedures work correctly
+ Test point-in-time recovery
+ Validate backup integrity

**For Multitenant:**
+ Test each PDB independently
+ Verify PDB isolation and resource allocation
+ Test PDB-specific operations (clone, unplug/plug, etc.)

**Decommission RDS Custom instance**

After a successful validation period (typically 1-2 weeks):

1. **Final backup**: Take a final backup of the RDS Custom instance for archival purposes

   ```
   # Create final snapshot
   aws rds create-db-snapshot \
     --db-instance-identifier my-custom-instance \
     --db-snapshot-identifier my-custom-instance-final-snapshot \
     --region us-east-1
   ```

1. **Document the migration**: Update runbooks and documentation with the new EC2 configuration

1. **Delete the RDS Custom instance**: Use the AWS Console or CLI to delete the instance

   ```
   # Delete RDS Custom instance without final snapshot (if already created above)
   aws rds delete-db-instance \
     --db-instance-identifier my-custom-instance \
     --skip-final-snapshot \
     --region us-east-1
   
   # Or create a final snapshot before deletion
   aws rds delete-db-instance \
     --db-instance-identifier my-custom-instance \
     --final-db-snapshot-identifier my-custom-instance-final-snapshot \
     --region us-east-1
   ```

1. **Clean up resources**: Remove associated snapshots, parameter groups, and option groups if no longer needed

1. **Update documentation**: Ensure all operational documentation reflects the new EC2-based architecture

## Comparison: RMAN Active Duplication vs Oracle Data Guard
<a name="RDS-Custom-for-Oracle-end-of-support-RMAN-vs-ODG"></a>

The following table summarizes the key differences between the two migration options:


|  **Aspect**  |  **RMAN Active Duplication**  |  **Oracle Data Guard**  | 
| --- | --- | --- | 
| **Source database availability** | Online during entire duplication | Online during entire process | 
| **Downtime** | Minutes (final cutover only) | Seconds to minutes (switchover) | 
| **Complexity** | Lower | Higher | 
| **Migration duration** | Single duplication operation | Initial setup \+ continuous sync | 
| **Continuous synchronization** | No | Yes | 
| **Fallback capability** | Manual (keep source running) | Built-in (automatic) | 
| **Testing before cutover** | Limited (test after duplication) | Full testing possible (standby can be tested) | 
| **Network bandwidth** | High during duplication | Moderate (continuous) | 
| **Source database impact** | Minimal (read operations) | Minimal (redo shipping) | 
| **Best for** | Most migrations, straightforward cutover | Mission-critical, near-zero downtime required | 
| **Non-CDB support** | Yes | Yes | 
| **Multitenant support** | Yes (entire CDB) | Yes (entire CDB) | 
| **Post-migration PDB state** | CDB open, PDBs MOUNTED | CDB open, PDBs MOUNTED | 
| **Requires RMAN** | Yes | Yes (for initial backup in backup-based approach) | 
| **Requires Data Guard** | No | Yes | 
| **Skill level required** | Intermediate | Advanced | 
| **Cutover process** | Redirect applications to EC2 | Switchover command \+ redirect applications | 

## Comparison: Non-CDB vs Multitenant migration
<a name="RDS-Custom-for-Oracle-end-of-support-non-cdb-va-multitenant"></a>

 

The following table summarizes the key differences between migrating non-CDB and multitenant databases:


|  **Aspect**  |  **Non-CDB migration**  |  **Multitenant (CDB with PDBs) migration**  | 
| --- | --- | --- | 
| **Database type** | Single-instance non-CDB (e.g., ORCL) | CDB (source: RDSCDB, target: ORCL) with CDB$ROOT \+ PDB$SEED \+ one or more PDBs | 
| **Migration scope** | Single database | Entire CDB (all PDBs included automatically) | 
| **RMAN duplication scope** | Duplicates single database | Duplicates entire CDB (all containers) | 
| **Data Guard scope** | Protects single database | Protects entire CDB (all PDBs included automatically) | 
| **Parameter file** | Standard init parameters | Must include enable\_pluggable\_database=TRUE | 
| **Post-migration database state** | Database opens in READ WRITE mode | CDB opens in READ WRITE mode; PDBs remain in MOUNTED state | 
| **PDB opening** | N/A | Must manually open all PDBs with ALTER PLUGGABLE DATABASE ALL OPEN | 
| **PDB auto-open on startup** | N/A | Must configure PDB save state or startup trigger | 
| **Validation** | Single database checks | Must validate CDB and each PDB individually | 
| **RDS-specific cleanup** | Drop users/objects from single database | Drop common users from CDB$ROOT (cascades to PDBs); handle C\#\# users | 
| **TNS/Listener configuration** | Single service for database | CDB service \+ individual PDB services dynamically registered | 
| **Application connection strings** | Connect to single database | Connect to individual PDB services (not CDB) | 
| **Backup strategy** | Backup single database | Backup entire CDB (includes all PDBs) or individual PDBs | 
| **Resource management** | Database-level resource management | CDB-level and PDB-level resource management with Resource Manager | 
| **Complexity** | Lower complexity | Higher complexity due to multiple containers and OMF paths | 

## Best practices and recommendations
<a name="RDS-Custom-for-Oracle-end-of-support-best-practices"></a>

This section provides comprehensive best practices for successful migration from RDS Custom for Oracle to EC2.

### Pre-migration planning
<a name="RDS-Custom-for-Oracle-end-of-support-best-practices-pre-migration"></a>

1. Conduct a thorough assessment:

   Before starting the migration, perform a comprehensive assessment of your environment:
   + **Database inventory**: Document all databases, their sizes, architectures (non-CDB vs multitenant), and dependencies
   + **Application dependencies**: Identify all applications connecting to the database and their connection methods
   + **Performance baseline**: Capture performance metrics (CPU, memory, I/O, network) for comparison post-migration
   + **Backup and recovery requirements**: Document RPO (Recovery Point Objective) and RTO (Recovery Time Objective)
   + **Compliance requirements**: Identify any regulatory or compliance requirements that may affect the migration

1. Choose the right EC2 instance type:

   Select an EC2 instance type based on your workload characteristics:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/RDS-Custom-for-Oracle-end-of-support.html)

    **Instance sizing guidelines:** 
   + Start with the same instance class as your RDS Custom instance
   + Monitor resource utilization during a test migration
   + Consider using AWS Compute Optimizer for recommendations
   + Plan for 20-30% headroom for growth and peak loads

1. Design your storage architecture:

   **EBS volume types:**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/RDS-Custom-for-Oracle-end-of-support.html)

   **Storage layout recommendations:**

   ```
   # Recommended layout for production databases
         /u01/app/oracle          # Oracle software (50-100 GB, gp3)
         /u01/app/oracle/oradata  # Data files (sized for database, gp3 or io2)
         /u01/app/oracle/arch     # Archive logs (separate volume, gp3)
         /u01/app/oracle/backup   # Backups (separate volume, gp3, can be detached post-migration)
   ```

    **Benefits of separate volumes:** 
   + Independent IOPS allocation
   + Easier capacity management
   + Simplified backup and snapshot strategies
   + Better performance isolation

1.  Establish a rollback plan:

   Always have a rollback strategy:
   + **Keep RDS Custom instance running** during validation period (1-2 weeks recommended)
   + **Maintain regular backups** of both source and target
   + **Document rollback procedures** including connection string changes
   + **Test rollback process** in a non-production environment
   + **Define rollback criteria** (performance degradation, data inconsistency, application errors)

### Migration execution best practices
<a name="RDS-Custom-for-Oracle-end-of-support-migration-best-practices"></a>

1. **Timing your migration:**

   Choose the optimal time window:
   + **Low-traffic periods**: Weekends, holidays, or off-peak hours
   + **Maintenance windows**: Align with scheduled maintenance if possible
   + **Avoid month-end/quarter-end**: These periods typically have high transaction volumes
   + **Consider time zones**: For global applications, choose a time that minimizes impact across regions

1. **Communication plan:**

   Establish clear communication:
   + **Stakeholder notification**: Inform all stakeholders at least 2 weeks in advance
   + **Application teams**: Coordinate with application teams for connection string updates
   + **Status updates**: Provide regular updates during migration
   + **Escalation path**: Define clear escalation procedures for issues
   + **Post-migration communication**: Confirm successful completion and any follow-up actions

1. **Validation checkpoints:**

   Implement validation at each stage:

    **Pre-migration validation:** 

   ```
   -- Capture object counts
   SQL> SELECT object_type, COUNT(*) FROM dba_objects GROUP BY object_type ORDER BY object_type;
   
   -- Capture tablespace usage
   SQL> SELECT tablespace_name, ROUND(SUM(bytes)/1024/1024/1024, 2) AS size_gb
   FROM dba_data_files GROUP BY tablespace_name;
   
   -- Capture user counts
   SQL> SELECT COUNT(*) FROM dba_users;
   
   -- For multitenant, capture PDB information
   SQL> SELECT con_id, name, open_mode FROM v$pdbs;
   ```

    **Post-migration validation:** 

   ```
   -- Verify object counts match
   SQL> SELECT object_type, COUNT(*) FROM dba_objects GROUP BY object_type ORDER BY object_type;
   
   -- Verify no invalid objects
   SQL> SELECT owner, object_type, object_name FROM dba_objects WHERE status = 'INVALID';
   
   -- Verify tablespace usage
   SQL> SELECT tablespace_name, ROUND(SUM(bytes)/1024/1024/1024, 2) AS size_gb
   FROM dba_data_files GROUP BY tablespace_name;
   
   -- Verify database size matches
   SQL> SELECT SUM(bytes)/1024/1024/1024 AS total_size_gb FROM dba_data_files;
   
   -- For multitenant, verify all PDBs are open
   SQL> SELECT con_id, name, open_mode FROM v$pdbs;
   ```

1. **Performance validation:**

   Compare performance metrics before and after migration:

   ```
   -- Capture AWR snapshots before migration (on RDS Custom)
   SQL> EXEC DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT;
   
   -- After migration (on EC2), compare metrics
   SQL> SELECT snap_id, begin_interval_time, end_interval_time
   FROM dba_hist_snapshot
   ORDER BY snap_id DESC
   FETCH FIRST 10 ROWS ONLY;
   
   -- Generate AWR report for comparison
   SQL> @?/rdbms/admin/awrrpt.sql
   ```

   Key metrics to compare:
   + Average active sessions
   + DB time per transaction
   + Physical reads per second
   + Logical reads per second
   + Redo size per second
   + User calls per second
   + Parse time per execute

### Post-migration optimization
<a name="RDS-Custom-for-Oracle-end-of-support-best-practices-post-migration-optimization"></a>

1. After migration, optimize database performance:

   1. **Database performance tuning:**

       **Gather statistics:** 

      ```
      -- Gather dictionary statistics
      SQL> EXEC DBMS_STATS.GATHER_DICTIONARY_STATS;
      
      -- Gather fixed object statistics
      SQL> EXEC DBMS_STATS.GATHER_FIXED_OBJECTS_STATS;
      
      -- Gather schema statistics
      SQL> EXEC DBMS_STATS.GATHER_SCHEMA_STATS('SCHEMA_NAME', cascade=>TRUE);
      
      -- For multitenant, gather statistics for each PDB
      SQL> ALTER SESSION SET CONTAINER = PDB_NAME;
      SQL> EXEC DBMS_STATS.GATHER_DATABASE_STATS(cascade=>TRUE);
      ```

      **Optimize memory parameters:**

      ```
      -- Enable Automatic Memory Management (if not already enabled)
      SQL> ALTER SYSTEM SET MEMORY_TARGET = 24G SCOPE=SPFILE;
      SQL> ALTER SYSTEM SET MEMORY_MAX_TARGET = 28G SCOPE=SPFILE;
      SQL> SHUTDOWN IMMEDIATE;
      SQL> STARTUP;
      
      -- Or use Automatic Shared Memory Management
      SQL> ALTER SYSTEM SET SGA_TARGET = 16G SCOPE=SPFILE;
      SQL> ALTER SYSTEM SET PGA_AGGREGATE_TARGET = 8G SCOPE=SPFILE;
      ```

      **Configure result cache:**

      ```
      -- Enable result cache for frequently accessed queries
      SQL> ALTER SYSTEM SET RESULT_CACHE_MAX_SIZE = 1G;
      SQL> ALTER SYSTEM SET RESULT_CACHE_MODE = MANUAL;
      ```

   1. Storage optimization:

      **Enable compression:**

      ```
      -- For tables with infrequent updates
      ALTER TABLE large_table MOVE COMPRESS FOR OLTP;
      
      -- For archive/historical data
      ALTER TABLE archive_table MOVE COMPRESS FOR ARCHIVE HIGH;
      
      -- Rebuild indexes after compression
      ALTER INDEX index_name REBUILD ONLINE;
      ```

      **Implement partitioning:**

      ```
      -- For large tables, consider partitioning
      -- Example: Range partitioning by date
      CREATE TABLE sales_partitioned (
          sale_id NUMBER,
          sale_date DATE,
          amount NUMBER
      )
      PARTITION BY RANGE (sale_date) (
          PARTITION sales_2024 VALUES LESS THAN (TO_DATE('2025-01-01', 'YYYY-MM-DD')),
          PARTITION sales_2025 VALUES LESS THAN (TO_DATE('2026-01-01', 'YYYY-MM-DD')),
          PARTITION sales_2026 VALUES LESS THAN (MAXVALUE)
      );
      ```

   1. Implement monitoring and alerting:

      **CloudWatch custom metrics:**

      Create a script to publish Oracle metrics to CloudWatch:

      ```
      #!/bin/bash
      # publish_oracle_metrics.sh
      
      INSTANCE_ID=$(ec2-metadata --instance-id | cut -d " " -f 2)
      REGION=$(ec2-metadata --availability-zone | cut -d " " -f 2 | sed 's/[a-z]$//')
      
      # Get tablespace usage
      TABLESPACE_USAGE=$(sqlplus -s / as sysdba << EOF
      SET PAGESIZE 0 FEEDBACK OFF VERIFY OFF HEADING OFF ECHO OFF
      SELECT ROUND(MAX(percent_used), 2)
      FROM (
           SELECT tablespace_name,
                  ROUND((used_space/tablespace_size)*100, 2) AS percent_used
           FROM dba_tablespace_usage_metrics
      );
      EXIT;
      EOF
      )
      
      # Publish to CloudWatch
      aws cloudwatch put-metric-data \
        --region $REGION \
        --namespace "Oracle/Database" \
        --metric-name "TablespaceUsage" \
        --value $TABLESPACE_USAGE \
        --unit Percent \
        --dimensions InstanceId=$INSTANCE_ID,Database=ORCL
      # Add more metrics as needed (sessions, wait events, etc.)
      ```

      **Set up CloudWatch alarms:**

      ```
      # Create alarm for high tablespace usage
      aws cloudwatch put-metric-alarm \
        --alarm-name oracle-high-tablespace-usage \
        --alarm-description "Alert when tablespace usage exceeds 85%" \
        --metric-name TablespaceUsage \
        --namespace Oracle/Database \
        --statistic Maximum \
        --period 300 \
        --evaluation-periods 2 \
        --threshold 85 \
        --comparison-operator GreaterThanThreshold \
        --alarm-actions arn:aws:sns:region:account-id:topic-name
      ```

   1. Security hardening:

      **Database security:**

      ```
      -- Enforce password complexity
      ALTER PROFILE DEFAULT LIMIT
          PASSWORD_LIFE_TIME 90
          PASSWORD_GRACE_TIME 7
          PASSWORD_REUSE_TIME 365
          PASSWORD_REUSE_MAX 5
          FAILED_LOGIN_ATTEMPTS 5
          PASSWORD_LOCK_TIME 1;
      
      -- Enable audit
      ALTER SYSTEM SET AUDIT_TRAIL = DB, EXTENDED SCOPE=SPFILE;
      SHUTDOWN IMMEDIATE;
      STARTUP;
      
      -- Audit critical operations
      AUDIT ALL ON SYS.AUD$ BY ACCESS;
      AUDIT CREATE USER BY ACCESS;
      AUDIT DROP USER BY ACCESS;
      AUDIT ALTER USER BY ACCESS;
      AUDIT CREATE SESSION BY ACCESS WHENEVER NOT SUCCESSFUL;
      ```

      **Network security:**

      ```
      # Restrict SSH access
      sudo vi /etc/ssh/sshd_config
      # Set: PermitRootLogin no
      # Set: PasswordAuthentication no
      
      # Configure firewall
      sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.0.0/8" port port="1521" protocol="tcp" accept'
      sudo firewall-cmd --reload
      
      # Enable Oracle Native Network Encryption
      # Edit sqlnet.ora
      SQLNET.ENCRYPTION_SERVER = REQUIRED
      SQLNET.ENCRYPTION_TYPES_SERVER = (AES256, AES192, AES128)
      SQLNET.CRYPTO_CHECKSUM_SERVER = REQUIRED
      SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER = (SHA256, SHA384, SHA512)
      ```

1. Backup and recovery strategy:

   **Implement comprehensive backup strategy:**

   ```
   #!/bin/bash
   # rman_backup.sh - Daily incremental backup script
   
   export ORACLE_HOME=/u01/app/oracle/product/19.0.0/dbhome_1
   export ORACLE_SID=ORCL
   export PATH=$ORACLE_HOME/bin:$PATH
   
   # Backup to local disk
   rman target / << EOF
   RUN {
       ALLOCATE CHANNEL ch1 DEVICE TYPE DISK FORMAT '/u01/app/oracle/backup/inc_%U';
       BACKUP INCREMENTAL LEVEL 1 DATABASE PLUS ARCHIVELOG;
       DELETE NOPROMPT OBSOLETE;
       CROSSCHECK BACKUP;
       DELETE NOPROMPT EXPIRED BACKUP;
   }
   EXIT;
   EOF
   
   # Copy backups to S3
   aws s3 sync /u01/app/oracle/backup/ s3://my-oracle-backups/$(date +%Y%m%d)/ \
       --storage-class STANDARD_IA \
       --exclude "*" \
       --include "inc_*" \
       --include "arch_*"
   
   # Clean up local backups older than 7 days
   find /u01/app/oracle/backup/ -name "inc_*" -mtime +7 -delete
   find /u01/app/oracle/backup/ -name "arch_*" -mtime +7 -delete
   ```

   **Schedule backups with cron:**

   ```
   # Edit crontab
   crontab -e
   
   # Add backup schedule
   # Full backup on Sunday at 2 AM
   0 2 * * 0 /home/oracle/scripts/rman_full_backup.sh >> /home/oracle/logs/backup_full.log 2>&1
   
   # Incremental backup Monday-Saturday at 2 AM
   0 2 * * 1-6 /home/oracle/scripts/rman_incremental_backup.sh >> /home/oracle/logs/backup_inc.log 2>&1
   
   # Archive log backup every 4 hours
   0 */4 * * * /home/oracle/scripts/rman_archivelog_backup.sh >> /home/oracle/logs/backup_arch.log 2>&1
   ```

### Cost optimization
<a name="RDS-Custom-for-Oracle-end-of-support-cost-optimization"></a>

 **1. Right-sizing:** 

After migration, monitor and optimize costs:
+ **Use AWS Cost Explorer** to analyze EC2 and EBS costs
+ **Enable AWS Compute Optimizer** for instance type recommendations
+ **Review CloudWatch metrics** to identify underutilized resources
+ **Consider Reserved Instances** or Savings Plans for predictable workloads

 **2. Storage optimization:** 
+ **Implement lifecycle policies** for S3 backups (move to Glacier after 30 days)
+ **Delete unused EBS snapshots** regularly
+ **Use gp3 instead of gp2** for cost savings with same performance
+ **Detach and delete backup volumes** after migration completes

 **3. Automation:** 
+ **Automate start/stop** of non-production databases during off-hours
+ **Use AWS Systems Manager** for patch management
+ **Implement auto-scaling** for read replicas if using Data Guard

## Conclusion
<a name="RDS-Custom-for-Oracle-end-of-support-conclusion"></a>

This prescriptive guidance provided detailed migration strategies for moving your Oracle databases from Amazon RDS Custom for Oracle to self-managed Oracle databases on Amazon EC2. With the RDS Custom for Oracle service deprecation effective March 31, 2027, it's important to plan and execute your migration well in advance.

 **Key takeaways** 

 **Migration options:** 
+ **RMAN Active Duplication**: Best for most migrations, keeps source database online during duplication, requires only brief cutover window for application redirection
+ **Oracle Data Guard**: Best for mission-critical workloads requiring near-zero downtime, providing continuous synchronization and built-in switchover capability

 **Architecture support:** 
+ Both migration options support non-CDB (traditional single-instance) and multitenant (CDB with PDBs) architectures
+ For multitenant, both methods automatically handle the entire CDB including all PDBs in a single operation
+ PDBs require manual opening and auto-open configuration post-migration

 **Critical success factors:** 
+ Proper network configuration and connectivity between source and target
+ Exact version compatibility (major version, minor version, Release Update, and one-off patches)
+ Adequate network bandwidth for data transfer (RMAN) or redo shipping (Data Guard)
+ Understanding that RMAN active duplication keeps source online - only brief cutover needed
+ Thorough testing and validation before decommissioning the source
+ Comprehensive post-migration tasks including backup, monitoring, and security configuration

 **Next steps:** 

1. Assess your database architecture (non-CDB or multitenant)

1. Choose the appropriate migration option based on your downtime tolerance and complexity requirements

1. Complete all prerequisite steps including EC2 instance setup and network configuration

1. Follow the detailed migration steps for your chosen option

1. Perform thorough validation and testing

1. Complete post-migration tasks to ensure production readiness

1. Decommission the RDS Custom instance after successful validation

 **Additional resources** 
+ [Amazon RDS Custom for Oracle User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom.html)
+ [Oracle Database Documentation](https://docs.oracle.com/en/database/)
+ [Oracle RMAN Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/)
+ [Oracle Data Guard Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/)
+ [AWS Database Migration Service](https://aws.amazon.com/dms/)
+ [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/)

 **Support** 

For assistance with your migration:
+ Contact AWS Support through the AWS Management Console
+ Consult with Oracle support for database-specific questions

## **Document information**
<a name="RDS-Custom-for-Oracle-end-of-support-document-information"></a>

**Last updated:** March 2026

**Contributors:**
+ Sharath Chandra Kampili, Database Specialist Solutions Architect, Amazon Web Services
+ Ibrahim Emara, Database Specialist Solution Architect, Amazon Web Services
+ Vetrivel Subramani, Database Specialist Solution Architect, Amazon Web Services