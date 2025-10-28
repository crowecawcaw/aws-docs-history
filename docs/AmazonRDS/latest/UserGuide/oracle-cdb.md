# Configuring an RDS for Oracle CDB

Configuring a CDB is similar to configuring a non-CDB.

###### Topics

- [Creating an RDS for Oracle CDB
  instance](#Oracle.Concepts.single-tenant.creation "#Oracle.Concepts.single-tenant.creation")
- [Connecting to a PDB in your RDS for Oracle
  CDB](#Oracle.Concepts.connecting.pdb "#Oracle.Concepts.connecting.pdb")

## Creating an RDS for Oracle CDB

instance

In RDS for Oracle, creating a CDB instance is almost identical to creating a non-CDB instance.
The difference is that you choose the Oracle multitenant architecture when creating your
DB instance and also choose an architecture configuration: multi-tenant or single-tenant. If you
create tags when you create a CDB in the multi-tenant configuration, RDS propagates the tags
to the initial tenant database. To create a CDB, use the AWS Management Console, the AWS CLI, or the RDS
API.

###### To create a CDB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the Amazon RDS console, choose the AWS Region in
   which you want to create the CDB instance.
3. In the navigation pane, choose **Databases**.
4. Choose **Create database**.
5. In **Choose a database creation method**, select
   **Standard Create**.
6. In **Engine options**, choose **Oracle**.
7. For **Database management type**, choose **Amazon
   RDS**.
8. For **Architecture settings**, choose **Oracle
   multitenant architecture**.
9. For **Architecture configuration**, do either
   of the following:
   - Choose **Multi-tenant configuration** and proceed
     to the next step.
   - Choose **Single-tenant configuration** and skip
     to Step 11.

10. (Multi-tenant configuration) For **Tenant database
    settings**, make the following changes:
    - For **Tenant database name**, enter the name of
      your initial PDB. The PDB name must be different from the CDB name,
      which defaults to `RDSCDB`.
    - For **Tenant database master username**, enter
      the master username of your PDB. You can't use the tenant database
      master username to log in to the CDB itself.
    - For **Credentials management**, choose either of
      the following credentials management options:
      - **Managed in AWS Secrets Manager**

      The managed password is for the initial tenant database
      rather than for the instance. In **Select the
      encryption key**, choose either a KMS key
      that Secrets Manager creates or a key that you have created.

      ###### Note

      We recommend AWS Secrets Manager as the most secure technique
      for managing credentials. Additional charges apply. For
      more information, see [Password management with
      Amazon RDS
      and AWS Secrets Manager](rds-secrets-manager.md "rds-secrets-manager.md").
      - **Self managed**

      To specify a password, clear the **Auto generate a
      password** check box if it is selected. Enter
      the same password in **Master password**
      and **Confirm master password**.

    - For **Tenant database character set**, choose a
      character set for the PDB. You can choose a tenant database
      character set that is different from the CDB character set.

    The default PDB character set is **AL32UTF8**. If
    you choose a nondefault PDB character set, CDB creation might be
    slower.

###### Note

You can't specify multiple tenant databases in the create operation.
The CDB has one PDB when it is created. You can add PDBs to an existing
CDB in a separate operation. 11. (Single-tenant configuration) Choose the settings that you want based on
the options listed in [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md"):

    1. In the **Settings** section, open
     **Credential Settings**. Then do the
     following:


    	1. For **Master username**, enter the name
    	 for a local user in your PDB. You can't use the master
    	 username to log in to the CDB root.
    	2. For **Credentials management**, choose
    	 either of the following credentials management
    	 options:




    		* **Managed in AWS Secrets Manager**


    		In **Select the encryption key**,
    		 choose either a KMS key that Secrets Manager creates or a
    		 key that you have created.


    		###### Note

    		We recommend AWS Secrets Manager as the most secure
    		 technique for managing credentials. Additional
    		 charges apply. For more information, see [Password management with
    		 Amazon RDS
    		 and AWS Secrets Manager](rds-secrets-manager.md "rds-secrets-manager.md").
    		* **Self managed**


    		To specify a password, clear the **Auto
    		 generate a password** check box if it is
    		 selected. Enter the same password in
    		 **Master password** and
    		 **Confirm master
    		 password**.

12. For the remaining sections, specify your DB instance settings. For information
    about each setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
13. Choose **Create database**.
    To create a CDB in the multi-tenant configuration, use the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md")
    command with the following parameters:

- `--db-instance-identifier`
- `--db-instance-class`
- `--engine { oracle-ee-cdb | oracle-se2-cdb }`
- `--master-username`
- `--master-user-password` or
  `--manage-master-user-password`
- `--multi-tenant` (for the single-tenant configuration, either
  don't specify `multi-tenant` or specify
  `--no-multi-tenant`)
- `--allocated-storage`
- `--backup-retention-period`
  For information about each setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

This following example creates an RDS for Oracle DB instance named
`my-cdb-inst` in the multi-tenant configuration. If you
specify `--no-multi-tenant` or don't specify `--multi-tenant`,
the default CDB configuration is single-tenant. The engine is
`oracle-ee-cdb`: a command that specifies `oracle-ee` and
`--multi-tenant` fails with an error. The initial tenant database is
named `mypdb`.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --engine oracle-ee-cdb \
    --db-instance-identifier `my-cdb-inst` \
    --multi-tenant \
    --db-name `mypdb` \
    --allocated-storage `250` \
    --db-instance-class `db.t3.large` \
    --master-username `pdb_admin` \
    --manage-master-user-password \
    --backup-retention-period `3`
```

For Windows:

```
aws rds create-db-instance ^
    --engine oracle-ee-cdb ^
    --db-instance-identifier `my-cdb-inst` ^
    --multi-tenant ^
    --db-name `mypdb` ^
    --allocated-storage `250` ^
    --db-instance-class `db.t3.large` ^
    --master-username `pdb_admin` ^
    --manage-master-user-password \ ^
    --backup-retention-period `3`
```

###### Note

Specify a password other than the prompt shown here as a security best practice.

This command produces output similar to the following. The database name,
character set, national character set, master user, and master user secret
aren't included in the output. You can view this information by using the CLI
command `describe-tenant-databases`.

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "my-cdb-inst",
        "DBInstanceClass": "db.t3.large",
        "MultiTenant": true,
        "Engine": "oracle-ee-cdb",
        "DBResourceId": "db-ABCDEFGJIJKLMNOPQRSTUVWXYZ",
        "DBInstanceStatus": "creating",
        "AllocatedStorage": 250,
        "PreferredBackupWindow": "04:59-05:29",
        "BackupRetentionPeriod": 3,
        "DBSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-0a1bcd2e",
                "Status": "active"
            }
        ],
        "DBParameterGroups": [
            {
                "DBParameterGroupName": "default.oracle-ee-cdb-19",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "DBSubnetGroup": {
            "DBSubnetGroupName": "default",
            "DBSubnetGroupDescription": "default",
            "VpcId": "vpc-1234567a",
            "SubnetGroupStatus": "Complete",
            ...
```

To create a DB instance by using the Amazon RDS API, call the [CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md")
operation.

For information about each setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

## Connecting to a PDB in your RDS for Oracle

CDB

You can use a utility like SQL\*Plus to connect to a PDB. To download Oracle Instant
Client, which includes a standalone version of SQL\*Plus, see [Oracle
Instant Client Downloads](https://www.oracle.com/database/technologies/instant-client/downloads.html "https://www.oracle.com/database/technologies/instant-client/downloads.html").

To connect SQL\*Plus to your PDB, you need the following information:

- PDB name
- Database user name and password
- Endpoint for your DB instance
- Port number

For information about finding the preceding information, see [Finding the endpoint of your RDS for Oracle DB instance](USER_Endpoint.md "USER_Endpoint.md").

###### Example To connect to your PDB using SQL\*Plus

In the following examples, substitute your master user for
`master_user_name`. Also, substitute the endpoint for your
DB instance, and then include the port number and the Oracle SID. The SID value is the name of
the PDB that you specified when you created your DB instance, and not the DB instance
identifier.

For Linux, macOS, or Unix:

```
sqlplus '`master_user_name`@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=`endpoint`)(PORT=`port`))(CONNECT_DATA=(SID=`pdb_name`)))'
```

For Windows:

```
sqlplus `master_user_name`@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=`endpoint`)(PORT=`port`))(CONNECT_DATA=(SID=`pdb_name`)))
```

You should see output similar to the following.

```
SQL*Plus: Release 19.0.0.0.0 Production on Mon Aug 21 09:42:20 2021
```

After you enter the password for the user, the SQL prompt appears.

```
SQL>
```

###### Note

The shorter format connection string (Easy connect or EZCONNECT), such as
`sqlplus
 `username`/`password`@`LONGER-THAN-63-CHARS-RDS-ENDPOINT-HERE`:1521/`database-identifier``,
might encounter a maximum character limit and should not be used to connect.
