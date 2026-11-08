

# Creating a BYOM DB instance for RDS for SQL Server
<a name="sqlserver-byom-creating-instance"></a>

Create a BYOM DB instance by using the AWS Management Console, the [AWS CLI](https://aws.amazon.com/cli/), [AWS Tools for PowerShell](https://aws.amazon.com/powershell/), or the [Amazon RDS API](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/Welcome.html). The AWS CLI and AWS Tools for PowerShell come preinstalled in [AWS CloudShell](https://aws.amazon.com/cloudshell/).

**Console** – From the Create database page, you can create a BYOM instance the same way you would create a License Included (LI) instance. The console creates the BYOM engine version behind the scenes on your behalf. Note that building the engine version from your provided installation media adds approximately 20 minutes to the overall instance creation time.

To avoid this additional wait, you can pre-create the BYOM engine version from the Custom engine versions page. After the engine version is created, launching instances against it follows the same timeline as LI instances.

**AWS CLI and AWS Tools for PowerShell** – When you use the AWS CLI or AWS Tools for PowerShell, you first create the BYOM engine version (the `CreateCustomDBEngineVersion` operation), and then create your DB instance (the `CreateDBInstance` operation). The same two steps apply when you upgrade a BYOM DB instance to a new minor version. First, create the target BYOM engine version and wait for it to reach `available` status. Then, modify the DB instance (the `ModifyDBInstance` operation).

## Prerequisites
<a name="sqlserver-byom-creating-instance.prerequisites"></a>

Before you create a BYOM DB instance, verify the following:
+ You have completed the steps in [Creating and managing BYOM engine versions for RDS for SQL Server](sqlserver-byom-creating-cev.md).

## Creating your BYOM DB instance
<a name="sqlserver-byom-creating-instance.creating"></a>

### Console
<a name="sqlserver-byom-creating-instance.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**. Choose **Create database**, and then choose **Full configuration**.

1. On the **Create database** page, do the following:

   1. For **Engine type**, choose **Microsoft SQL Server**.

   1. For **Database management type**, choose **Amazon RDS**.

   1. For **Edition**, choose **SQL Server Enterprise Edition** or **SQL Server Standard Edition**.

   1. Under **Templates**, confirm the template selection. When you choose an edition, the template options change. For Enterprise Edition and Standard Edition, the options are **Production** and **Dev/Test**.

   1. For **License Model**, choose **BYOM (Bring Your Own Media)**.

   1. For **Major engine version**, choose the major version that matches your installation media, for example **SQL Server 2025**.

   1. For **Minor engine version**, choose the minor version, for example `17.00.5005.3.v1`.

   1. For **DB instance identifier**, enter a unique name for your DB instance.

   1. Configure the remaining settings (DB instance class, storage, connectivity, authentication, backups, and maintenance) as you would for a License Included DB instance.

1. Choose **Create database**.

Amazon RDS creates the BYOM engine version automatically and launches your instance.

### AWS CLI
<a name="sqlserver-byom-creating-instance.cli"></a>

Use the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) command with `--license-model bring-your-own-media`.

```
aws rds create-db-instance \
    --engine sqlserver-ee \
    --engine-version 17.00.5005.3.v1 \
    --license-model bring-your-own-media \
    --db-instance-identifier {{my-byom-instance}} \
    --db-instance-class db.m8a.xlarge \
    --master-username {{admin}} \
    --manage-master-user-password \
    --allocated-storage {{200}} \
    --db-subnet-group-name {{my-subnet-group}} \
    --vpc-security-group-ids {{sg-0123456789abcdef0}} \
    --region {{us-west-2}}
```

This example uses `--manage-master-user-password` to store the master user password in AWS Secrets Manager. For more information, see [Password management with Amazon RDS and AWS Secrets Manager](rds-secrets-manager.md).

To set your own password instead, replace `--manage-master-user-password` with the following:

```
--master-user-password {{password}}
```

### PowerShell
<a name="sqlserver-byom-creating-instance.powershell"></a>

Use the [New-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-RDSDBInstance.html) cmdlet with `-LicenseModel bring-your-own-media`.

```
New-RDSDBInstance `
    -Engine sqlserver-ee `
    -EngineVersion 17.00.5005.3.v1 `
    -LicenseModel bring-your-own-media `
    -DBInstanceIdentifier {{my-byom-instance}} `
    -DBInstanceClass db.m8a.xlarge `
    -MasterUsername {{admin}} `
    -ManageMasterUserPassword $true `
    -AllocatedStorage {{200}} `
    -DBSubnetGroupName {{my-subnet-group}} `
    -VpcSecurityGroupId {{sg-0123456789abcdef0}} `
    -Region {{us-west-2}}
```

This example uses `-ManageMasterUserPassword $true` to store the master user password in AWS Secrets Manager. For more information, see [Password management with Amazon RDS and AWS Secrets Manager](rds-secrets-manager.md).

To set your own password instead, replace `-ManageMasterUserPassword $true` with the following:

```
-MasterUserPassword {{password}}
```

## Verifying your BYOM DB instance
<a name="sqlserver-byom-creating-instance.verifying"></a>

After you create the instance, verify that it uses the BYOM license model. Confirm the following values:
+ `LicenseModel` is `bring-your-own-media` – The instance uses your own SQL Server license.
+ `Engine` is `sqlserver-ee` – The correct engine edition.
+ `EngineVersion` is `17.00.5005.3.v1` – The target engine version.

### Console
<a name="sqlserver-byom-creating-instance.verifying.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the name of your DB instance.

1. Choose the **Configuration** tab.

Confirm that **License model** shows **Bring Your Own Media** and **Engine version** shows the target engine version. The **Engine** field at the top of the page shows the edition.

### AWS CLI
<a name="sqlserver-byom-creating-instance.verifying.cli"></a>

Use the [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) command.

```
aws rds describe-db-instances \
    --db-instance-identifier {{my-byom-instance}} \
    --region {{us-west-2}}
```

The output looks like the following.

```
...
            "Engine": "sqlserver-ee",
            ...
            "EngineVersion": "17.00.5005.3.v1",
            ...
            "LicenseModel": "bring-your-own-media",
...
```

### PowerShell
<a name="sqlserver-byom-creating-instance.verifying.powershell"></a>

Use the [Get-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-RDSDBInstance.html) cmdlet.

```
Get-RDSDBInstance `
    -DBInstanceIdentifier {{my-byom-instance}} `
    -Region {{us-west-2}}
```

The output looks like the following.

```
...
Engine                                    : sqlserver-ee
...
EngineVersion                             : 17.00.5005.3.v1
...
LicenseModel                              : bring-your-own-media
...
```

## Considerations
<a name="sqlserver-byom-creating-instance.considerations"></a>
+ If you have existing automation that creates DB instances without specifying a license model, those workflows fail after you create a BYOM engine version for that engine version. Update your automation to specify the license model before you activate a BYOM engine version.