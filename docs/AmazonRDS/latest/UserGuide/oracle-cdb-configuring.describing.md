# Viewing tenant database

details

You can view details about a tenant database in the same way that you can for a
non-CDB or CDB.

###### To view details about a tenant database

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the Amazon RDS console, choose the
   AWS Region where your DB instance resides.
3. In the navigation pane, choose **Databases**.

![View details about a CDB](images/cdb-list.png)

In the preceding image, the sole tenant database (PDB) appears as a child of
the DB instance. 4. Choose the name of a tenant database.

![View details about a PDB](images/pdb-details.png)
To see details about your PDBs, use the AWS CLI command [describe-tenant-databases](../../../cli/latest/reference/rds/describe-tenant-databases.md "../../../cli/latest/reference/rds/describe-tenant-databases.md").

This following example describes all tenant databases in the specified
Region.

###### Example

For Linux, macOS, or Unix:

```
aws rds describe-tenant-databases --region `us-east-1`
```

For Windows:

```
aws rds describe-tenant-databases --region `us-east-1`
```

This command produces output similar to the following.

```
    "TenantDatabases" : [
         {
            "DBInstanceIdentifier" : "my-cdb-inst",
            "TenantDBName" : "pdb-test",
            "Status" : "available",
            "MasterUsername" : "pdb-test-admin",
            "DbiResourceId" : "db-abc123",
            "TenantDatabaseResourceId" : "tdb-bac456",
            "TenantDatabaseArn" : "arn:aws:rds:us-east-1:123456789012:db:my-cdb-inst:pdb-test",
            "CharacterSetName": "AL32UTF8",
            "NcharCharacterSetName": "AL16UTF16",
            "DeletionProtection": false,
            "PendingModifiedValues": {
                 "MasterUserPassword": "****"
            },
            "TagList": []
         },
         {

            "DBInstanceIdentifier" : "my-cdb-inst2",
            "TenantDBName" : "pdb-dev",
            "Status" : "modifying",
            "MasterUsername" : "masterrdsuser"
            "DbiResourceId" : "db-xyz789",
            "TenantDatabaseResourceId" : "tdb-ghp890",
            "TenantDatabaseArn" : "arn:aws:rds:us-east-1:123456789012:db:my-cdb-inst2:pdb-dev",
            "CharacterSetName": "AL32UTF8",
            "NcharCharacterSetName": "AL16UTF16",
            "DeletionProtection": false,
            "PendingModifiedValues": {
                 "MasterUserPassword": "****"
            },
            "TagList": []
         },
         ... other truncated data
```

The following example describes the tenant databases on DB instance
`my-cdb-inst` in the specified Region.

###### Example

For Linux, macOS, or Unix:

```
aws rds describe-tenant-databases --region `us-east-1` \
    --db-instance-identifier `my-cdb-inst`
```

For Windows:

```
aws rds describe-tenant-databases --region `us-east-1` ^
    --db-instance-identifier `my-cdb-inst`
```

This command produces output similar to the following.

```
{
    "TenantDatabase": {
        "TenantDatabaseCreateTime": "2023-10-19T23:55:30.046Z",
        "DBInstanceIdentifier": "my-cdb-inst",
        "TenantDBName": "pdb-hr",
        "Status": "creating",
        "MasterUsername": "tenant-admin-user",
        "DbiResourceId": "db-abc123",
        "TenantDatabaseResourceId": "tdb-bac567",
        "TenantDatabaseARN": "arn:aws:rds:us-west-2:579508833180:pdb-hr:tdb-abcdefghi1jklmno2p3qrst4uvw5xy6zabc7defghi8jklmn90op",
        "CharacterSetName": "AL32UTF8",
        "NcharCharacterSetName": "AL16UTF16",
        "DeletionProtection": false,
        "PendingModifiedValues": {
            "MasterUserPassword": "****"
        },
        "TagList": [
            {
                "Key": "TEST",
                "Value": "testValue"
            }
        ]
    }
}
```

The following example describes tenant database `pdb1` on DB instance
`my-cdb-inst` in the US East (N. Virginia) Region.

###### Example

For Linux, macOS, or Unix:

```
aws rds describe-tenant-databases --region `us-east-1` \
--db-instance-identifier `my-cdb-inst` \
--tenant-db-name `pdb1`
```

For Windows:

```
aws rds describe-tenant-databases --region `us-east-1` ^
--db-instance-identifier `my-cdb-inst` ^
--tenant-db-name `pdb1`
```

This command produces output similar to the following.

```
{
    "TenantDatabases" : [
        {
            "DbiResourceId" : "db-abc123",
            "TenantDatabaseResourceId" : "tdb-bac567",
            "TenantDatabaseArn" : "arn:aws:rds:us-east-1:123456789012:db:my-cdb-inst:pdb1"
            "DBInstanceIdentifier" : "my-cdb-inst",
            "TenantDBName" : "pdb1",
            "Status" : "ACTIVE",
            "MasterUsername" : "masterawsuser"
            "Port" : "1234",
            "CharacterSetName": "UTF-8",
            "ParameterGroups": [
                {
                    "ParameterGroupName": "tenant-custom-pg",
                    "ParameterApplyStatus": "in-sync"
                }
            ],
            {
            "OptionGroupMemberships": [
                {
                    "OptionGroupName": "tenant-custom-og",
                    "Status": "in-sync"
                }
            ]
         }
    ]
}
```
