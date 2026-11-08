

# Upgrading a BYOM DB instance for RDS for SQL Server
<a name="sqlserver-byom-upgrade"></a>

You can apply minor engine version upgrades to your BYOM DB instances on RDS for SQL Server. Minor version upgrades include Microsoft cumulative updates that contain security patches, bug fixes, and performance improvements.

Unlike License Included instances, upgrading a BYOM instance requires a BYOM engine version to be available before you initiate the upgrade.

You can identify upgrade targets, apply the upgrade, and verify it by using the AWS Management Console, the [AWS CLI](https://aws.amazon.com/cli/), [AWS Tools for PowerShell](https://aws.amazon.com/powershell/), or the [Amazon RDS API](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/Welcome.html). The AWS CLI and AWS Tools for PowerShell come preinstalled in [AWS CloudShell](https://aws.amazon.com/cloudshell/).

## Identifying valid upgrade targets
<a name="sqlserver-byom-upgrade.targets"></a>

Before you upgrade, identify which engine versions are available as valid upgrade targets for your current version.

### Console
<a name="sqlserver-byom-upgrade.targets.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Select your BYOM DB instance, and then choose **Modify**.

1. Open the **Minor engine version** list. The list shows the minor versions that are available for your DB instance.

1. Choose **Cancel**.

### AWS CLI
<a name="sqlserver-byom-upgrade.targets.cli"></a>

Use the [describe-db-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-engine-versions.html) command to list valid minor version upgrade targets.

```
aws rds describe-db-engine-versions \
    --engine sqlserver-ee \
    --engine-version 17.00.4075.5.v1 \
    --include-all \
    --query "DBEngineVersions[?DBEngineMediaType=='Customer Provided'].ValidUpgradeTarget[] | [?IsMajorVersionUpgrade==\`false\`]" \
    --region {{us-west-2}}
```

The output looks like the following.

```
[
    {
        "Engine": "sqlserver-ee",
        "EngineVersion": "17.00.5005.3.v1",
        "Description": "SQL Server 2025 17.00.5005.3.v1",
        "AutoUpgrade": false,
        "IsMajorVersionUpgrade": false
    }
]
```

The output shows that you can upgrade from `17.00.4075.5.v1` to `17.00.5005.3.v1`.

### PowerShell
<a name="sqlserver-byom-upgrade.targets.powershell"></a>

Use the [Get-RDSDBEngineVersion](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-RDSDBEngineVersion.html) cmdlet to list valid minor version upgrade targets.

```
(Get-RDSDBEngineVersion `
    -Engine sqlserver-ee `
    -EngineVersion 17.00.4075.5.v1 `
    -IncludeAll $true `
    -Region {{us-west-2}} |
Where-Object DBEngineMediaType -eq 'Customer Provided').ValidUpgradeTarget |
Where-Object { -not $_.IsMajorVersionUpgrade } |
Format-Table Engine, EngineVersion, AutoUpgrade, IsMajorVersionUpgrade
```

The output looks like the following.

```
Engine       EngineVersion   AutoUpgrade IsMajorVersionUpgrade
------       -------------   ----------- ---------------------
sqlserver-ee 17.00.5005.3.v1       False                 False
```

The output shows that you can upgrade from `17.00.4075.5.v1` to `17.00.5005.3.v1`.

## Applying a BYOM version upgrade
<a name="sqlserver-byom-upgrade.applying"></a>

Before you initiate a version upgrade, take a manual snapshot. Amazon RDS creates automated snapshots, but a manual snapshot gives you a known restore point.

### Console
<a name="sqlserver-byom-upgrade.applying.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Select your BYOM DB instance, and then choose **Modify**.

1. For **Minor engine version**, choose the target version, for example `17.00.5005.3.v1`.

1. Choose **Continue**.

1. Under **Schedule modifications**, choose **Apply during the next scheduled maintenance window** or **Apply immediately**.

1. Choose **Modify DB instance**.

### AWS CLI
<a name="sqlserver-byom-upgrade.applying.cli"></a>

Use the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command.

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-byom-instance}} \
    --engine-version 17.00.5005.3.v1 \
    --no-apply-immediately \
    --region {{us-west-2}}
```

### PowerShell
<a name="sqlserver-byom-upgrade.applying.powershell"></a>

Use the [Edit-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-RDSDBInstance.html) cmdlet.

```
Edit-RDSDBInstance `
    -DBInstanceIdentifier {{my-byom-instance}} `
    -EngineVersion 17.00.5005.3.v1 `
    -ApplyImmediately $false `
    -Region {{us-west-2}}
```

**Note**  
By default, Amazon RDS applies the change during the next maintenance window. You can also choose to apply the change immediately. For more information, see [Using the schedule modifications setting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.ApplyImmediately.html).

## Verifying the upgrade
<a name="sqlserver-byom-upgrade.verifying"></a>

After the upgrade completes, verify the new engine version on your DB instance. Confirm the following values:
+ `EngineVersion` matches your target version.
+ `DBInstanceStatus` is `available`.
+ `LicenseModel` is `bring-your-own-media`.

### Console
<a name="sqlserver-byom-upgrade.verifying.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the name of your DB instance.

1. Choose the **Configuration** tab.

Under **Configuration**, confirm that **Engine version** shows the target version and **License model** shows **Bring Your Own Media**.

### AWS CLI
<a name="sqlserver-byom-upgrade.verifying.cli"></a>

Use the [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) command.

```
aws rds describe-db-instances \
    --db-instance-identifier {{my-byom-instance}} \
    --query "DBInstances[*].[DBInstanceIdentifier,EngineVersion,DBInstanceStatus,LicenseModel]" \
    --region {{us-west-2}}
```

The output looks like the following.

```
[
    [
        "my-byom-instance",
        "17.00.5005.3.v1",
        "available",
        "bring-your-own-media"
    ]
]
```

### PowerShell
<a name="sqlserver-byom-upgrade.verifying.powershell"></a>

Use the [Get-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-RDSDBInstance.html) cmdlet.

```
Get-RDSDBInstance `
    -DBInstanceIdentifier {{my-byom-instance}} `
    -Region {{us-west-2}} |
Format-Table DBInstanceIdentifier, EngineVersion, DBInstanceStatus, LicenseModel
```

The output looks like the following.

```
DBInstanceIdentifier EngineVersion   DBInstanceStatus LicenseModel
-------------------- -------------   ---------------- ------------
my-byom-instance     17.00.5005.3.v1 available        bring-your-own-media
```

## Converting a License Included instance to Bring Your Own Media
<a name="sqlserver-byom-upgrade.converting"></a>

You can convert an existing RDS for SQL Server instance from the License Included model to BYOM. This lets you use your own SQL Server licenses instead of paying the AWS-included license fee.

**Note**  
You must have a BYOM engine version in `available` status for the instance's current engine version.

### Console
<a name="sqlserver-byom-upgrade.converting.console"></a>

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Select the License Included DB instance, and then choose **Modify**.

1. For **License Model**, choose **BYOM (Bring Your Own Media)**. Keep the current **Minor engine version**.

1. Choose **Continue**.

1. Under **Schedule modifications**, choose **Apply during the next scheduled maintenance window** or **Apply immediately**.

1. Choose **Modify DB instance**.

### AWS CLI
<a name="sqlserver-byom-upgrade.converting.cli"></a>

Use the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command to change the license model.

```
aws rds modify-db-instance \
    --db-instance-identifier {{my-li-instance}} \
    --license-model bring-your-own-media \
    --no-apply-immediately \
    --region {{us-west-2}}
```

### PowerShell
<a name="sqlserver-byom-upgrade.converting.powershell"></a>

Use the [Edit-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-RDSDBInstance.html) cmdlet to change the license model.

```
Edit-RDSDBInstance `
    -DBInstanceIdentifier {{my-li-instance}} `
    -LicenseModel bring-your-own-media `
    -ApplyImmediately $false `
    -Region {{us-west-2}}
```

**Note**  
By default, Amazon RDS applies the change during the next maintenance window. You can also choose to apply the change immediately. For more information, see [Using the schedule modifications setting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.ApplyImmediately.html).

To verify the current license model of your DB instance, check the `LicenseModel` field in the output. If a modification is in progress, check the `PendingModifiedValues` field for the pending license model. After the modification completes, the `LicenseModel` field reflects the new value. For more information, see [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) (AWS CLI) and [Get-RDSDBInstance](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-RDSDBInstance.html) (AWS Tools for PowerShell).

## Considerations
<a name="sqlserver-byom-upgrade.considerations"></a>
+ Converting from BYOM to License Included is not supported.
+ If your License-Included (LI) instance has read replicas, remove them before converting license model to BYOM, then recreate them after. The new replicas will automatically inherit the BYOM licensing model.
+ If your License Included DB instance runs on an instance class that doesn't support BYOM (for example, `db.m5` or `db.r6i`), you can't convert it directly to BYOM. First, modify your DB instance to an instance class that supports BYOM for your engine version, and then convert the license model as a separate modify operation. To find supported instance classes, see [Amazon RDS for SQL Server pricing](https://aws.amazon.com/rds/sqlserver/pricing/) (for **License Model**, choose **Bring your own media**) or [DB instance class support for Microsoft SQL Server](SQLServer.Concepts.General.InstanceClasses.md).