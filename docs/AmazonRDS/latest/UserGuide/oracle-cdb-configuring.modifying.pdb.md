

# Modifying an RDS for Oracle tenant database
<a name="oracle-cdb-configuring.modifying.pdb"></a>

You can modify only the PDB name and the master user password of a tenant database in your CDB. Note the following requirements and limitations:
+ To modify the settings of a tenant database in your DB instance, the tenant database must exist. 
+ You can't modify multiple tenant databases in a single operation. You can only modify one tenant database at a time.
+ You can't change the name of a tenant database to `CDB$ROOT` or `PDB$SEED`.
+ If your DB instance has read replicas, you can only modify tenants on the primary DB instance. Replication health is also validated, ensuring the replicas are available and replication lag is less than 5 minutes before the tenant is modified.

You can modify PDBs using the AWS Management Console, the AWS CLI, or the RDS API.

## Console
<a name="oracle-cdb-configuring.modifying.pdb.console"></a>

**To modify the PDB name or master password of a tenant database**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the Amazon RDS console, choose the AWS Region in which you want to create the tenant database.

1. In the navigation pane, choose **Databases**.

1. Choose the tenant database whose database name or master user password you want to modify.

1. Choose **Modify**.

1. For **Tenant database settings**, do any of the following:
   + For **Tenant database name**, enter the new name of your new PDB.
   + For **Tenant database master password**, enter a new password.

1. Choose **Modify tenant**.

## AWS CLI
<a name="oracle-cdb-configuring.modifying.pdb.cli"></a>

To modify a tenant database using the AWS CLI, call the [modify-tenant-database](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-tenant-database.html) command with the following parameters:
+ `--db-instance-identifier` {{value}}
+ `--tenant-db-name {{value}}`
+ `[--new-tenant-db-name {{value}}]`
+ `[--master-user-password {{value}}]`

The following example renames tenant database `pdb1` to `pdb-hr` on DB instance `my-cdb-inst`.

**Example**  
For Linux, macOS, or Unix:  

```
1. aws rds modify-tenant-database --region {{us-east-1}} \
2.     --db-instance-identifier {{my-cdb-inst}} \
3.     --tenant-db-name {{pdb1}} \
4.     --new-tenant-db-name {{pdb-hr}}
```
For Windows:  

```
1. aws rds modify-tenant-database --region {{us-east-1}} ^
2.     --db-instance-identifier {{my-cdb-inst}} ^
3.     --tenant-db-name {{pdb1}} ^
4.     --new-tenant-db-name {{pdb-hr}}
```
This command produces output similar to the following.   

```
{
    "TenantDatabase" : {
        "DbiResourceId" : "db-abc123",
        "TenantDatabaseResourceId" : "tdb-bac567",
        "TenantDatabaseARN" : "arn:aws:rds:us-east-1:123456789012:db:my-cdb-inst:pdb1",
        "DBInstanceIdentifier" : "my-cdb-inst",
        "TenantDBName" : "pdb1",
        "Status" : "modifying",
        "MasterUsername" : "tenant-admin-user",
        "Port" : "6555",
        "CharacterSetName" : "UTF-16",
        "MaxAllocatedStorage" : "1000",
        "ParameterGroups": [
            {
                "ParameterGroupName": "pdb1-params",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "OptionGroupMemberships": [
            {
                "OptionGroupName": "pdb1-options",
                "Status": "in-sync"
            }
        ],
        "PendingModifiedValues": {
            "TenantDBName": "pdb-hr"
        }
    }
}
```