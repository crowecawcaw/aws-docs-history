# Prerequisites for zero-ETL integration in Oracle Database@AWS

Before setting up zero-ETL integration, ensure that you meet the following
prerequisites.

## General prerequisites

- **Oracle Database@AWS setup** – Make sure you have at least one VM cluster
  provisioned and running.
- **Integration with zero-ETL enabled** – Make sure
  your VM cluster or Autonomous VM cluster is associated with an ODB network that has zero-ETL
  enabled.
- **Supported Oracle Database versions** – You must use
  Oracle Database 19c (Oracle Exadata) or Oracle Database 19c/23ai (Autonomous Database on Dedicated
  Infrastructure).
- **Same AWS Region** – The source Oracle database and
  target Amazon Redshift cluster must be in the same AWS Region.

## Oracle database prerequisites

You must configure your Oracle database with the following settings.

### Replication user setup

Create a dedicated replication user in each pluggable database (PDB) that you want to
replicate:

- **For Oracle Exadata** – Create user `ODBZEROETLADMIN`
  with a secure password.
- **For Autonomous Database on Dedicated Infrastructure** –
  Use the existing `GGADMIN` user.

Grant the following permissions to the replication user.

```
-- For Autonomous Database on Dedicated Infrastructure only
ALTER USER GGADMIN ACCOUNT UNLOCK;
ALTER USER GGADMIN IDENTIFIED BY `ggadmin-password`;

-- For Oracle Exadata only
GRANT SELECT ON `any-replicated-table` TO "ODBZEROETLADMIN";
GRANT LOGMINING to "ODBZEROETLADMIN";

-- Grant the following permissions to all services.
-- For Oracle Exadata, use the ODBZEROETLADMIN user. For Autonomous Database on Dedicated Infrastructure,
-- use the GGADMIN user.
GRANT CREATE SESSION TO "ODBZEROETLADMIN";
GRANT SELECT ANY TRANSACTION TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$ARCHIVED_LOG TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$LOG TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$LOGFILE TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$LOGMNR_LOGS TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$LOGMNR_CONTENTS TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$DATABASE TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$THREAD TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$PARAMETER TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$NLS_PARAMETERS TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$TIMEZONE_NAMES TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$TRANSACTION TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$CONTAINERS TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_INDEXES TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_OBJECTS TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_TABLES TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_USERS TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_CATALOG TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_CONSTRAINTS TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_CONS_COLUMNS TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_TAB_COLS TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_IND_COLUMNS TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_ENCRYPTED_COLUMNS TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_LOG_GROUPS TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_TAB_PARTITIONS TO "ODBZEROETLADMIN";
GRANT SELECT ON SYS.DBA_REGISTRY TO "ODBZEROETLADMIN";
GRANT SELECT ON SYS.OBJ$ TO "ODBZEROETLADMIN";
GRANT SELECT ON DBA_TABLESPACES TO "ODBZEROETLADMIN";
GRANT SELECT ON DBA_OBJECTS TO "ODBZEROETLADMIN";
GRANT SELECT ON SYS.ENC$ TO "ODBZEROETLADMIN";
GRANT SELECT ON GV_$TRANSACTION TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$DATAGUARD_STATS TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$DATABASE_INCARNATION TO "ODBZEROETLADMIN";
GRANT EXECUTE ON SYS.DBMS_CRYPTO TO "ODBZEROETLADMIN";
GRANT SELECT ON SYS.DBA_DIRECTORIES TO "ODBZEROETLADMIN";
GRANT SELECT ON ALL_VIEWS TO "ODBZEROETLADMIN";
GRANT SELECT ON DBA_SEGMENTS TO "ODBZEROETLADMIN";
GRANT SELECT ON V_$TRANSPORTABLE_PLATFORM TO "ODBZEROETLADMIN";
GRANT CREATE ANY DIRECTORY TO "ODBZEROETLADMIN";
GRANT EXECUTE ON DBMS_FILE_TRANSFER TO "ODBZEROETLADMIN";
GRANT EXECUTE ON DBMS_FILE_GROUP TO "ODBZEROETLADMIN";
```

### Supplemental logging

Enable supplemental logging on your Oracle database to capture change data.

```
-- Check if supplemental logging is enabled
SELECT supplemental_log_data_min FROM v$database;

-- Enable supplemental logging if not already enabled.
-- For Oracle Exadata, enable supplemental logging on both the CDB and PDB.
-- For Autonomous Database on Dedicated Infrastructure, enable supplemental logging on the PDB only.
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA;

-- For Autonomous Database on Dedicated Infrastructure only
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA (PRIMARY KEY) COLUMNS;

-- Archive current online redo log
ALTER SYSTEM ARCHIVE LOG CURRENT;
```

To set up a zero-ETL integration between Oracle Database@AWS and Amazon Redshift, you must configure SSL.

**For Oracle Exadata databases**

You must manually configure SSL on port 2484. This task involves the
following:

- Configuring `(PROTOCOL=tcps)(PORT=2484)` in
  `listener.ora`
- Setting up the wallet using `sqlnet.ora`
- Generating and configuring SSL certificates (see [How To Configure SSL/TCPS For Exadata Cloud Database (ExaCC/ExaCS) (Doc ID
  2947301.1)](https://support.oracle.com/knowledge/Oracle%20Database%20Products/2947301_1.html "https://support.oracle.com/knowledge/Oracle%20Database%20Products/2947301_1.html") in the My Oracle Support documentation)

**For Autonomous Databases**

SSL on port 2484 is enabled by default. No additional configuration is
required.

###### Important

The SSL port is fixed as 2484.

### ASM configuration (Oracle Exadata only)

If Automatic Storage Management (ASM) is enabled on your Oracle Exadata system, you must
create an ASM user.

```
-- Connect to ASM instance
sqlplus / as sysasm

-- Create ASM user
CREATE USER ODBZEROETLASM IDENTIFIED BY "`secure_password`";

-- Grant SYSASM privilege
GRANT SYSASM TO ODBZEROETLASM;

-- Grant additional required privileges
GRANT SELECT ON V_$TRANSPORTABLE_PLATFORM TO "ODBZEROETLASM";
GRANT CREATE ANY DIRECTORY TO "ODBZEROETLASM";
GRANT EXECUTE ON DBMS_FILE_TRANSFER TO "ODBZEROETLASM";
GRANT EXECUTE ON DBMS_FILE_GROUP TO "ODBZEROETLASM";
```

###### Note

ASM configuration is not required for Autonomous Databases.

## AWS service prerequisites

Before setting up zero-ETL integration, set up AWS Secrets Manager and configure IAM
permissions.

### Set up AWS Secrets Manager

Store your Oracle database credentials in AWS Secrets Manager as follows:

1. Create a Customer Managed Key (CMK) in AWS KMS.
2. Store database credentials in Secrets Manager using the CMK.
3. Configure resource policies to allow Oracle Database@AWS access.

To get your TDE key ID and password, use the technique described in [Supported
encryption methods for using Oracle as a source for AWS DMS](../../../dms/latest/userguide/CHAP_Source.md#CHAP_Source.Oracle.Encryption "../../../dms/latest/userguide/CHAP_Source.md#CHAP_Source.Oracle.Encryption"). The following command
generates the base64 wallet.

```
base64 -i cwallet.sso > wallet.b64
```

The following example shows a secret for Oracle Exadata. For
`asm_service_name`, the `111.11.11.11`
represents the virtual IP for the VM node. You can also register the ASM listener with
SCAN.

```
{
  "database_info": [
    {
      "name": "ODBDB_ZETLPDB",
      "service_name": "ODBDB_ZETLPDB.paas.oracle.com",
      "username": "ODBZEROETLADMIN",
      "password": "`secure_password`",
      "tde_key_id": "ORACLE.SECURITY.DB.ENCRYPTION.`key_id`",
      "tde_password": "`tde_password`",
      "certificateWallet": "`base64_encoded_wallet_content`"
    }
  ],
  "asm_info": {
    "asm_user": "odbzeroetlasm",
    "asm_password": "Reinvent_2025",
    "asm_service_name": "`111.11.11.11`:2484/+`ASM`"
  }
}
```

The following example shows a secret for Autonomous Database on Dedicated
Infrastructure.

```
{
  "database_info": [
    {
      "database_name": "ZETLACD_ZETLADBMORECPU",
      "service_name": "ZETLADBMORECPU_high.adw.oraclecloud.com",
      "username": "ggadmin",
      "password": "`secure_password`",
      "certificateWallet": "`base64_encoded_wallet_content`"
    }
  ]
}
```

### Configure IAM permissions

Create IAM policies that allow zero-ETL integration operations. The following example
policy allows describe, create, update, and delete operations for an Exadata VM cluster. For an
Autonomous VM cluster, use the value `cloud-autonomous-vm-cluster` instead of
`cloud-vm-cluster` for the resource ARN.
