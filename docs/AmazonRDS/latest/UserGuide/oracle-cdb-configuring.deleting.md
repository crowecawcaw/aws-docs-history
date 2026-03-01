# Deleting an RDS for Oracle tenant database from your CDB

You can delete a tenant database (PDB) using the AWS Management Console, the AWS CLI, or the RDS API.
Consider the following prerequisites and limitations:

- The tenant database and DB instance must exist.
- For the deletion to succeed, one of the following situations must
  exist:
  - The tenant database and DB instance are available.

  ###### Note

  You can take a final snapshot, but only if the tenant database and DB instance
  were in an available state before you issued the
  `delete-tenant-database` command.
  This snapshot will only be taken on the primary instance if the DB instance has read replicas.
  - The tenant database is being created.
  - The DB instance is modifying the tenant database.
  - If the DB instance has read replicas these constraints apply to all replicas.

- You can't delete multiple tenant databases in a single operation.
- You can't delete a tenant database if it is the only tenant in the CDB.
- You can't delete a tenant database on a read replica,
  you can only delete a tenant on the primary DB instance.
  Replication health is also validated, ensuring the replication lag is less than
  5 minutes before the tenant is deleted.

###### To delete a tenant database

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and
   then choose the tenant database that you want to delete.
3. For **Actions**, choose
   **Delete**.
4. To create a final DB snapshot for the DB instance, choose **Create final
   snapshot?**.
5. If you chose to create a final snapshot, enter the **Final
   snapshot name**.
6. Enter `delete me` in the box.
7. Choose **Delete**.
   To delete a tenant database using the AWS CLI, call the [delete-tenant-database](../../../cli/latest/reference/rds/delete-tenant-database.md "../../../cli/latest/reference/rds/delete-tenant-database.md") command with the following
   parameters:

- `--db-instance-identifier
`value``
- `--tenant-db-name `value``
- `[--skip-final-snapshot | --no-skip-final-snapshot]`
- `[--final-snapshot-identifier
 `value`]`
  This following example deletes the tenant database named
  `pdb-test` from the CDB named
  `my-cdb-inst`. By default, the operation creates a
  final snapshot.

###### Example

For Linux, macOS, or Unix:

```
aws rds delete-tenant-database --region `us-east-1` \
    --db-instance-identifier `my-cdb-inst` \
    --tenant-db-name `pdb-test` \
    --final-snapshot-identifier `final-snap-pdb-test`
```

For Windows:

```
aws rds delete-tenant-database --region `us-east-1` ^
    --db-instance-identifier `my-cdb-inst` ^
    --tenant-db-name `pdb-test` ^
    --final-snapshot-identifier `final-snap-pdb-test`
```

This command produces output similar to the following.

```
{
    "TenantDatabase" : {
        "DbiResourceId" : "db-abc123",
        "TenantDatabaseResourceId" : "tdb-bac456",
        "TenantDatabaseArn" : "arn:aws:rds:us-east-1:123456789012:db:my-cdb-inst:pdb-test",
        "DBInstanceIdentifier" : "my-cdb-inst",
        "TenantDBName" : "pdb-test",
        "Status" : "deleting",
        "MasterUsername" : "pdb-test-admin"
        "Port" : "6555",
        "CharacterSetName" : "UTF-16",
        "MaxAllocatedStorage" : "1000",
        "ParameterGroups": [
            {
                "ParameterGroupName": "tenant-1-params",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "OptionGroupMemberships": [
            {
                "OptionGroupName": "tenant-1-options",
                "Status": "in-sync"
            }
        ]
    }
}
```
