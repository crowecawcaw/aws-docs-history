# Converting the single-tenant configuration

to multi-tenant

You can modify the architecture of an RDS for Oracle CDB from the single-tenant configuration to
the multi-tenant configuration. Before and after the conversion, your CDB contains a single
tenant database (PDB). Tags for the DB instance propagate to the initial tenant database created
during the conversion.

Before you begin, make sure that your IAM policy has permission to create a tenant
database. During the conversion, RDS for Oracle migrates the following metadata to the new tenant
database:

- The master username
- The managed master password (if the source CDB integrates with Secrets Manager)
- The database name
- The character set
- The national character set
  Before the conversion, you view the preceding information by using the
  `describe-db-instances` command. After the conversion, you view the
  information by using the `describe-tenant-database` command.

The conversion from single-tenant to multi-tenant has the following limitations:

- You can't later convert back to the single-tenant configuration after you convert
  to the multi-tenant configuration. The conversion is irreversible.
- You can't convert a primary or replica database that has Oracle Data Guard
  enabled.
- You can't upgrade the DB engine version and convert to the multi-tenant configuration
  in the same operation.
- You can't enable or disable managed master user passwords during the
  conversion.

###### To convert a CDB using the single-tenant configuration to the multi-tenant configuration

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the Amazon RDS console, choose the
   AWS Region where your DB instance resides.
3. In the navigation pane, choose **Databases**, and
   then choose the non-CDB instance that you want to convert to a CDB
   instance.
4. Choose **Modify**.
5. For **Architecture settings**, select **Oracle
   multitenant architecture**.
6. For **Architecture configuration**, select
   **Multi-tenant configuration**.
7. (Optional) For **DB parameter group**, choose a new
   parameter group for your CDB instance. The same parameter group
   considerations apply when converting a DB instance as when upgrading a
   DB instance.
8. (Optional) For **Option group**, choose a new option
   group for your CDB instance. The same option group considerations apply
   when converting a DB instance as when upgrading a DB instance.
9. When all the changes are as you want them, choose
   **Continue** and check the summary of
   modifications.
10. Choose **Apply immediately**. This option is required
    when you switch to a multi-tenant configuration. Note that this option
    can cause downtime in some cases.
11. On the confirmation page, review your changes. If they are correct,
    choose **Modify DB instance**.

Or choose **Back** to edit your changes or
**Cancel** to cancel your changes.
To convert a CDB using the single-tenant configuration to the multi-tenant configuration, specify
`--multi-tenant` in the AWS CLI command [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md").

The following example converts the DB instance named `my-st-cdb` from the
single-tenant configuration to the multi-tenant configuration. The `--apply-immediately` option is required.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance --region `us-east-1`\
    --db-instance-identifier `my-st-cdb` \
    --multi-tenant \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance --region `us-east-1` ^
    --db-instance-identifier `my-st-cdb` ^
    --multi-tenant ^
    --apply-immediately
```

The output looks something like the following.

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "my-st-cdb",
        "DBInstanceClass": "db.r5.large",
        "MultiTenant": false,
        "Engine": "oracle-ee-cdb",
        "DBResourceId": "db-AB1CDE2FGHIJK34LMNOPRLXTXU",
        "DBInstanceStatus": "modifying",
        "MasterUsername": "admin",
        "DBName": "ORCL",
        ...
        "EngineVersion": "19.0.0.0.ru-2022-01.rur-2022-01.r1",
        "AutoMinorVersionUpgrade": true,
        "ReadReplicaDBInstanceIdentifiers": [],
        "LicenseModel": "bring-your-own-license",
        "OptionGroupMemberships": [
            {
                "OptionGroupName": "default:oracle-ee-cdb-19",
                "Status": "in-sync"
            }
        ],
        ...
        "PendingModifiedValues": {
            "MultiTenant": "true"
        }
    }
}
```
