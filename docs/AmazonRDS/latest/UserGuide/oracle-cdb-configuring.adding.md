# Adding an RDS for Oracle tenant database

to your CDB instance

In the RDS for Oracle multi-tenant configuration, a tenant database is a PDB. To add a
tenant database, make sure you meet the following prerequisites:

- Your CDB has the multi-tenant configuration enabled. For more information, see
  [Multi-tenant configuration of
  the CDB architecture](Oracle.Concepts.md#multi-tenant-configuration "Oracle.Concepts.md#multi-tenant-configuration").
- You have the necessary IAM permissions to create the tenant database.
  You can add a tenant database using the AWS Management Console, the AWS CLI, or the RDS API. You
  can't add multiple tenant databases in a single operation: you must add them one at a
  time. If the CDB has backup retention enabled, Amazon RDS backs up the DB instance before and after
  it adds a new tenant database. If the CDB has read replicas,
  you can only add a tenant database to the primary DB instance;
  Amazon RDS automatically creates the tenant database on the replicas.
  Replication health is also validated, ensuring all replicas are available and
  replication lag is less than 5 minutes before the tenant is created.

###### To add a tenant database to your DB instance

1.  Sign in to the AWS Management Console and open the Amazon RDS console at
    [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2.  In the upper-right corner of the Amazon RDS console, choose the
    AWS Region in which you want to create the tenant database.
3.  In the navigation pane, choose **Databases**.
4.  Choose the CDB instance to which you want to add a tenant database. Your
    DB instance must use the multi-tenant configuration of the CDB architecture.
5.  Choose **Actions** and then **Add tenant
    database**.
6.  For **Tenant database settings**, do the following:

        * For **Tenant database name**, enter the name of
         your new PDB.
        * For **Tenant database master username**, enter the
         name of the master user for your PDB.
        * Choose either of the following credentials management
         options:




        	+ **Managed in AWS Secrets Manager**


        	In **Select the encryption key**,
        	 choose either a KMS key that Secrets Manager creates or a key
        	 that you have created.


        	###### Note

        	We recommend AWS Secrets Manager as the most secure
        	 technique for managing credentials. Additional charges apply.
        	 AWS Secrets Manager is not supported for instances using read replicas.
        	 For more information, see [Password management with
        	 Amazon RDS
        	 and AWS Secrets Manager](rds-secrets-manager.md "rds-secrets-manager.md").
        	+ **Self managed**


        	To specify a password, clear the **Auto
        	 generate a password** check box if it is
        	 selected. Enter the same password in **Master
        	 password** and **Confirm master
        	 password**.
        	+ Under **Additional configuration**,
        	 enter the name of your PDB for **Initial
        	 database name**. You can't name the CDB,
        	 which has the default name `RDSCDB`.
        * For **Tenant database character set**, choose
         a character set for the PDB. The default is
         **AL32UTF8**. You can choose a PDB
         character set that is different from the CDB character
         set. If the instance has read replicas, tenants cannot be created
         with a custom character set. You can create your tenants with a custom character set
         before creating a read replica if needed.
        * For **Tenant database national character
         set**, choose a national character set for the PDB.
         The default is **AL32UTF8**. The national
         character set specifies the encoding only for columns that use
         the `NCHAR` data type (`NCHAR`,
         `NVARCHAR2`, and `NCLOB`) and doesn't
         affect database metadata.

    For more information about the preceding settings, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

7.  Choose **Add tenant**.
    To add a tenant database to your CDB with the AWS CLI, use the command [create-tenant-database](../../../cli/latest/reference/rds/create-tenant-database.md "../../../cli/latest/reference/rds/create-tenant-database.md") with the following required
    parameters:

- `--db-instance-identifier`
- `--tenant-db-name`
- `--master-username`
- `--master-user-password`
  This following example creates a tenant database named
  `mypdb2` in the RDS for Oracle CDB instance named
  `my-cdb-inst`. The PDB character set is
  `UTF-16`.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-tenant-database --region us-east-1 \
    --db-instance-identifier `my-cdb-inst` \
    --tenant-db-name `mypdb2` \
    --master-username `mypdb2-admin` \
    --master-user-password `mypdb2-pwd` \
    --character-set-name `UTF-16`
```

For Windows:

```
aws rds create-tenant-database --region us-east-1 \
    --db-instance-identifier `my-cdb-inst` ^
    --tenant-db-name `mypdb2` ^
    --master-username `mypdb2-admin` ^
    --master-user-password `mypdb2-pwd` ^
    --character-set-name `UTF-16`
```

The output looks similar to the following.

```
...}
    "TenantDatabase" :
         {
            "DbiResourceId" : "db-abc123",
            "TenantDatabaseResourceId" : "tdb-bac567",
            "TenantDatabaseArn" : "arn:aws:rds:us-east-1:123456789012:db:my-cdb-inst:mypdb2",
            "DBInstanceIdentifier" : "my-cdb-inst",
            "TenantDBName" : "mypdb2",
            "Status" : "creating",
            "MasterUsername" : "mypdb2",
            "CharacterSetName" : "UTF-16",
            ...
        }
}...
```
