# Upgrading an RDS Custom for Oracle DB instance

To upgrade your RDS Custom for Oracle DB instance, modify it to use a new CEV. This CEV can contain either
new database binaries or a new AMI. For example, to upgrade your Oracle Linux 7.9 DB instance to
Oracle Linux 8, specify the latest AMI, which uses Oracle Linux 8. To upgrade the database
and OS, you must perform two separate upgrades.

###### Note

If you upgrade the database, RDS Custom automatically upgrades read replicas after it
upgrades the primary DB instance. If you upgrade the OS, you must upgrade the replicas
manually.

Before you begin, review [Requirements for RDS Custom for Oracle upgrades](custom-upgrading.md#custom-upgrading-reqs "custom-upgrading.md#custom-upgrading-reqs") and [Considerations for RDS Custom for Oracle database
upgrades](custom-upgrading-considerations.md "custom-upgrading-considerations.md").

###### To upgrade an RDS Custom for Oracle DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then
   choose the RDS Custom for Oracle DB instance that you want to upgrade.
3. Choose **Modify**. The **Modify DB instance** page appears.
4. For **DB engine version**, choose a new CEV. Do the
   following:
   - If you are patching the database, make sure that the CEV specifies
     database binaries that are different from those used by your DB
     instance, and doesn't specify an AMI that is different from the AMI
     currently used by your DB instance.
   - If you are patching the OS, make sure that the CEV specifies an
     AMI that is different from the AMI currently used by your DB instance, and
     doesn't specify different database binaries.

   ###### Warning

   When you patch your OS, you lose your root volume data and any
   existing OS customization.

5. Choose **Continue** to check the summary of modifications.

Choose **Apply immediately** to apply the changes immediately. 6. If your changes are correct, choose **Modify DB instance**. Or choose **Back** to edit
your changes or **Cancel** to cancel your changes.
The following examples show possible upgrade scenarios. The examples assume that
you created an RDS Custom for Oracle DB instance with the following characteristics:

- DB instance named `my-custom-instance`
- CEV named `19.my_cev1`
- Oracle Database 19c using the non-CDB architecture
- Oracle Linux 8 using AMI `ami-1234`
  The latest service-provided AMI is `ami-2345`. You can find AMIs by
  running the CLI command `describe-db-engine-versions`.

###### Topics

- [Upgrading the OS](#custom-upgrading-modify.CLI.os "#custom-upgrading-modify.CLI.os")
- [Upgrading the database](#custom-upgrading-modify.CLI.db "#custom-upgrading-modify.CLI.db")

### Upgrading the OS

In this example, you want to upgrade `ami-1234` to
`ami-2345`, which is the latest service-provided AMI. Because you
are upgrading the OS, the database binaries for `ami-1234` and
`ami-2345` must be the same. You create a new CEV named
`19.my_cev2` based on `19.my_cev1`.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-custom-db-engine-version \
    --engine `custom-oracle-ee` \
    --engine-version `19.my_cev2` \
    --description `"Non-CDB CEV based on ami-2345"` \
    --kms-key-id `key-name` \
    --source-custom-db-engine-version-identifer `arn:aws:rds:us-west-2:123456789012:cev:custom-oracle-ee/19.my_cev1/12345678-ab12-1234-cde1-abcde123456789` \
    --image-id `ami-2345`
```

For Windows:

```
aws rds create-custom-db-engine-version ^
    --engine `custom-oracle-ee` ^
    --engine-version `19.my_cev2` ^
    --description `"Non-CDB CEV based on ami-2345"` ^
    --kms-key-id `key-name` ^
    --source-custom-db-engine-version-identifer `arn:aws:rds:us-west-2:123456789012:cev:custom-oracle-ee/19.my_cev1/12345678-ab12-1234-cde1-abcde123456789` ^
    --image-id `ami-2345`
```

To upgrade an RDS Custom DB instance, use the [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md")
AWS CLI command with the following parameters:

- `--db-instance-identifier` – Specify the RDS Custom for Oracle
  DB instance to be upgraded.
- `--engine-version` – Specify the CEV that has the
  new AMI.
- `--no-apply-immediately` | `--apply-immediately`
  – Specify whether to perform the upgrade immediately or wait
  until the scheduled maintenance window.

The following example upgrades `my-custom-instance` to version
`19.my_cev2`. Only the OS is upgraded.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-custom-instance` \
    --engine-version `19.my_cev2` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-custom-instance` ^
    --engine-version `19.my_cev2` ^
    --apply-immediately
```

### Upgrading the database

In this example, you want to apply Oracle patch p35042068 to your RDS for Oracle
DB instance. Because you upgraded your OS in [Upgrading the OS](#custom-upgrading-modify.CLI.os "#custom-upgrading-modify.CLI.os"), your DB instance is currently
using `19.my_cev2`, which is based on `ami-2345`. You
create a new CEV named `19.my_cev3` that also uses
`ami-2345`, but you specify a new JSON manifest in the
`$MANIFEST` environment variable. Thus, only the database
binaries different in your new CEV and the CEV that your instance is currently
using.

###### Example

For Linux, macOS, or Unix:

```
aws rds create-custom-db-engine-version \
    --engine `custom-oracle-ee` \
    --engine-version `19.my_cev3` \
    --description `"Non-CDB CEV with p35042068 based on ami-2345"` \
    --kms-key-id `key-name` \
    --image-id `ami-2345` \
    --manifest `$MANIFEST`
```

For Windows:

```
aws rds create-custom-db-engine-version ^
    --engine `custom-oracle-ee` ^
    --engine-version `19.my_cev3` ^
    --description `"Non-CDB CEV with p35042068 based on ami-2345"` ^
    --kms-key-id `key-name` ^
    --image-id `ami-2345` ^
    --manifest `$MANIFEST`
```

The following example upgrades `my-custom-instance` to engine
version `19.my_cev3`. Only the database is upgraded.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-custom-instance` \
    --engine-version `19.my_cev3` \
    --apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my-custom-instance` ^
    --engine-version `19.my_cev3` ^
    --apply-immediately
```
