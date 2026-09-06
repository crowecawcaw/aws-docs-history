

# Configuring an RDS for Oracle CDB
<a name="oracle-cdb.configuring"></a>

Configuring a CDB is similar to configuring a non-CDB. 

**Topics**
+ [Creating an RDS for Oracle CDB instance](#Oracle.Concepts.single-tenant.creation)
+ [Connecting to a PDB in your RDS for Oracle CDB](#Oracle.Concepts.connecting.pdb)

## Creating an RDS for Oracle CDB instance
<a name="Oracle.Concepts.single-tenant.creation"></a>

In RDS for Oracle, creating a CDB instance is almost identical to creating a non-CDB instance. The difference is that you choose the Oracle multitenant architecture when creating your DB instance and also choose an architecture configuration: multi-tenant or single-tenant. If you create tags when you create a CDB in the multi-tenant configuration, RDS propagates the tags to the initial tenant database. To create a CDB, use the AWS Management Console, the AWS CLI, or the RDS API.

### Console
<a name="Oracle.Concepts.single-tenant.creation.console"></a>

**To create a CDB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the Amazon RDS console, choose the AWS Region in which you want to create the CDB instance.

1. In the navigation pane, choose **Databases**.

1. Choose **Create database**.

1. In **Choose a database creation method**, select **Standard Create**.

1. In **Engine options**, choose **Oracle**. 

1. For **Database management type**, choose **Amazon RDS**.

1. For **Architecture settings**, choose **Oracle multitenant architecture**. 

1. For **Architecture configuration**, do either of the following:
   + Choose **Multi-tenant configuration** and proceed to the next step.
   + Choose **Single-tenant configuration** and skip to Step 11.

1. (Multi-tenant configuration) For **Tenant database settings**, make the following changes:
   + For **Tenant database name**, enter the name of your initial PDB. The PDB name must be different from the CDB name, which defaults to `RDSCDB`.
   + For **Tenant database master username**, enter the master username of your PDB. You can't use the tenant database master username to log in to the CDB itself.
   + For **Credentials management**, choose either of the following credentials management options:
     + **Managed in AWS Secrets Manager**

       The managed password is for the initial tenant database rather than for the instance. In **Select the encryption key**, choose either a KMS key that Secrets Manager creates or a key that you have created. 
**Note**  
We recommend AWS Secrets Manager as the most secure technique for managing credentials. Additional charges apply. For more information, see [Password management with Amazon RDS and AWS Secrets Manager](rds-secrets-manager.md).
     + **Self managed**

       To specify a password, clear the **Auto generate a password** check box if it is selected. Enter the same password in **Master password** and **Confirm master password**.
   + For **Tenant database character set**, choose a character set for the PDB. You can choose a tenant database character set that is different from the CDB character set.

     The default PDB character set is **AL32UTF8**. If you choose a nondefault PDB character set, CDB creation might be slower. 
**Note**  
You can't specify multiple tenant databases in the create operation. The CDB has one PDB when it is created. You can add PDBs to an existing CDB in a separate operation.

1. (Single-tenant configuration) Choose the settings that you want based on the options listed in [Settings for DB instances](USER_CreateDBInstance.Settings.md):

   1. In the **Settings** section, open **Credential Settings**. Then do the following:

     1. For **Master username**, enter the name for a local user in your PDB. You can't use the master username to log in to the CDB root.

     1. For **Credentials management**, choose either of the following credentials management options:
        + **Managed in AWS Secrets Manager**

          In **Select the encryption key**, choose either a KMS key that Secrets Manager creates or a key that you have created. 
**Note**  
We recommend AWS Secrets Manager as the most secure technique for managing credentials. Additional charges apply. For more information, see [Password management with Amazon RDS and AWS Secrets Manager](rds-secrets-manager.md).
        + **Self managed**

          To specify a password, clear the **Auto generate a password** check box if it is selected. Enter the same password in **Master password** and **Confirm master password**.

1. For the remaining sections, specify your DB instance settings. For information about each setting, see [Settings for DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.Settings.html).

1. Choose **Create database**.

### AWS CLI
<a name="Oracle.Concepts.single-tenant.creation.cli"></a>

To create a CDB in the multi-tenant configuration, use the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) command with the following parameters:
+ `--db-instance-identifier`
+ `--db-instance-class`
+ `--engine { oracle-ee-cdb | oracle-se2-cdb }`
+ `--master-username`
+ `--master-user-password` or `--manage-master-user-password`
+ `--multi-tenant` (for the single-tenant configuration, either don't specify `multi-tenant` or specify `--no-multi-tenant`)
+ `--allocated-storage`
+ `--backup-retention-period`

For information about each setting, see [Settings for DB instances](USER_CreateDBInstance.Settings.md).

This following example creates an RDS for Oracle DB instance named {{my-cdb-inst}} in the multi-tenant configuration. If you specify `--no-multi-tenant` or don't specify `--multi-tenant`, the default CDB configuration is single-tenant. The engine is `oracle-ee-cdb`: a command that specifies `oracle-ee` and `--multi-tenant` fails with an error. The initial tenant database is named {{mypdb}}.

**Example**  
For Linux, macOS, or Unix:  

```
 1. aws rds create-db-instance \
 2.     --engine oracle-ee-cdb \
 3.     --db-instance-identifier {{my-cdb-inst}} \
 4.     --multi-tenant \
 5.     --db-name {{mypdb}} \
 6.     --allocated-storage {{250}} \
 7.     --db-instance-class {{db.m5.large}} \
 8.     --master-username {{pdb_admin}} \
 9.     --manage-master-user-password \
10.     --backup-retention-period {{3}}
```
For Windows:  

```
 1. aws rds create-db-instance ^
 2.     --engine oracle-ee-cdb ^
 3.     --db-instance-identifier {{my-cdb-inst}} ^
 4.     --multi-tenant ^
 5.     --db-name {{mypdb}} ^
 6.     --allocated-storage {{250}} ^
 7.     --db-instance-class {{db.m5.large}} ^
 8.     --master-username {{pdb_admin}} ^
 9.     --manage-master-user-password ^
10.     --backup-retention-period {{3}}
```
This command produces output similar to the following. The database name, character set, national character set, master user, and master user secret aren't included in the output. You can view this information by using the CLI command `describe-tenant-databases`.  

```
 1. {
 2.     "DBInstance": {
 3.         "DBInstanceIdentifier": "my-cdb-inst",
 4.         "DBInstanceClass": "db.m5.large",
 5.         "MultiTenant": true,
 6.         "Engine": "oracle-ee-cdb",
 7.         "DBResourceId": "db-ABCDEFGJIJKLMNOPQRSTUVWXYZ",
 8.         "DBInstanceStatus": "creating",
 9.         "AllocatedStorage": 250,
10.         "PreferredBackupWindow": "04:59-05:29",
11.         "BackupRetentionPeriod": 3,
12.         "DBSecurityGroups": [],
13.         "VpcSecurityGroups": [
14.             {
15.                 "VpcSecurityGroupId": "sg-0a1bcd2e",
16.                 "Status": "active"
17.             }
18.         ],
19.         "DBParameterGroups": [
20.             {
21.                 "DBParameterGroupName": "default.oracle-ee-cdb-19",
22.                 "ParameterApplyStatus": "in-sync"
23.             }
24.         ],
25.         "DBSubnetGroup": {
26.             "DBSubnetGroupName": "default",
27.             "DBSubnetGroupDescription": "default",
28.             "VpcId": "vpc-1234567a",
29.             "SubnetGroupStatus": "Complete",
30.             ...
```

### RDS API
<a name="Oracle.Concepts.single-tenant.creation.api"></a>

To create a DB instance by using the Amazon RDS API, call the [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) operation.

For information about each setting, see [Settings for DB instances](USER_CreateDBInstance.Settings.md). 

## Connecting to a PDB in your RDS for Oracle CDB
<a name="Oracle.Concepts.connecting.pdb"></a>

You can use a utility like SQL\*Plus to connect to a PDB. To download Oracle Instant Client, which includes a standalone version of SQL\*Plus, see [ Oracle Instant Client Downloads](https://www.oracle.com/database/technologies/instant-client/downloads.html).

To connect SQL\*Plus to your PDB, you need the following information:
+ PDB name
+ Database user name and password
+ Endpoint for your DB instance
+ Port number

For information about finding the preceding information, see [Finding the endpoint of your RDS for Oracle DB instance](USER_Endpoint.md).

**Example To connect to your PDB using SQL\*Plus**  
In the following examples, substitute your master user for {{master\_user\_name}}. Also, substitute the endpoint for your DB instance, and then include the port number and the PDB service name. The service name is the name of the PDB that you specified when you created your DB instance, and not the DB instance identifier.  
For Linux, macOS, or Unix:  

```
1. sqlplus '{{master_user_name}}@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={{endpoint}})(PORT={{port}}))(CONNECT_DATA=(SERVICE_NAME={{pdb_name}})))'
```
For Windows:  

```
1. sqlplus {{master_user_name}}@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={{endpoint}})(PORT={{port}}))(CONNECT_DATA=(SERVICE_NAME={{pdb_name}})))
```
You should see output similar to the following.  

```
SQL*Plus: Release 19.0.0.0.0 Production on Mon Aug 21 09:42:20 2021
```
After you enter the password for the user, the SQL prompt appears.  

```
SQL>
```

**Note**  
The shorter format connection string (Easy connect or EZCONNECT), such as `sqlplus {{username}}/{{password}}@{{LONGER-THAN-63-CHARS-RDS-ENDPOINT-HERE}}:1521/{{database-identifier}}`, might encounter a maximum character limit and should not be used to connect. 