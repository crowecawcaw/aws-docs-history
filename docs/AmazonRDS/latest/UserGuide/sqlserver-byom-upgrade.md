

# Upgrading a BYOM DB instance for RDS for SQL Server
<a name="sqlserver-byom-upgrade"></a>

You can apply minor engine version upgrades to your BYOM DB instances on RDS for SQL Server. Minor version upgrades include Microsoft cumulative updates that contain security patches, bug fixes, and performance improvements.

Unlike License Included instances, upgrading a BYOM instance requires a BYOM engine version to be available before you initiate the upgrade.

## Identifying valid upgrade targets
<a name="sqlserver-byom-upgrade.targets"></a>

Before you upgrade, identify which engine versions are available as valid upgrade targets for your current version.

Use the `describe-db-engine-versions` command to list valid minor version upgrade targets:

**Example:**

```
aws rds describe-db-engine-versions \
    --engine sqlserver-ee \
    --engine-version 15.00.4440.1.v1 \
    --include-all \
    --query "DBEngineVersions[?DBEngineMediaType=='Customer Provided'].ValidUpgradeTarget[] | [?IsMajorVersionUpgrade==\`false\`]"
```

**Sample output:**

```
[
    {
        "Engine": "sqlserver-ee",
        "EngineVersion": "15.00.4455.2.v1",
        "AutoUpgrade": false,
        "IsMajorVersionUpgrade": false
    },
    .....
    {
        "Engine": "sqlserver-ee",
        "EngineVersion": "15.00.4465.1.v1",
        "AutoUpgrade": false,
        "IsMajorVersionUpgrade": false
    }
]
```

## Applying a BYOM version upgrade (AWS CLI)
<a name="sqlserver-byom-upgrade.applying"></a>

Before you initiate a version upgrade, take a manual snapshot. Amazon RDS creates automated snapshots, but a manual snapshot gives you a known restore point.

**Example:**

```
aws rds modify-db-instance \
    --db-instance-identifier my-byom-instance \
    --engine-version 15.00.4465.1.v1 \
    --no-apply-immediately
```

**Note**  
When you use `--no-apply-immediately`, Amazon RDS applies the change during the next maintenance window. Use `--apply-immediately` to apply the change immediately. For more information, see [Using the schedule modifications setting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.ApplyImmediately.html).

## Verifying the upgrade
<a name="sqlserver-byom-upgrade.verifying"></a>

After the upgrade completes, verify the new engine version on your DB instance.

**Example:**

```
aws rds describe-db-instances \
    --db-instance-identifier my-byom-instance \
    --query "DBInstances[*].[DBInstanceIdentifier,EngineVersion,DBInstanceStatus,LicenseModel]"
```

```
[
    [
        "my-byom-instance",
        "15.00.4465.1.v1",
        "available",
        "bring-your-own-media"
    ]
]
```

Confirm the following values:
+ `EngineVersion` matches your target version.
+ `DBInstanceStatus` is `available`.
+ `LicenseModel` is `bring-your-own-media`.

## Converting a License Included instance to Bring Your Own Media
<a name="sqlserver-byom-upgrade.converting"></a>

You can convert an existing RDS for SQL Server instance from the License Included model to BYOM. This lets you use your own SQL Server licenses instead of paying the AWS-included license fee.

**Note**  
You must have a BYOM engine version in `available` status for the instance's current engine version.

Use the `modify-db-instance` command to change the license model:

```
aws rds modify-db-instance \
    --db-instance-identifier DB_INSTANCE_IDENTIFIER \
    --license-model bring-your-own-media \
    --no-apply-immediately
```

**Note**  
When you use `--no-apply-immediately`, Amazon RDS applies the change during the next maintenance window. Use `--apply-immediately` to apply the change immediately. For more information, see [Using the schedule modifications setting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.ApplyImmediately.html).

To verify the current license model of your DB instance, use the `describe-db-instances` command and check the `LicenseModel` field in the response. If a modification is in progress, check the `PendingModifiedValues` field for the pending license model. After the modification completes, the `LicenseModel` field reflects the new value. For more information, see [Describing a DB instance](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html).

## Considerations
<a name="sqlserver-byom-upgrade.considerations"></a>
+ Converting from BYOM to License Included is not supported.
+ If your License-Included (LI) instance has read replicas, remove them before converting license model to BYOM, then recreate them after. The new replicas will automatically inherit the BYOM licensing model.
+ If your LI DB instance is running on an instance class that is not supported for BYOM (for example, db.m5 or db.r6i), you cannot convert directly to BYOM. First, modify your instance to a supported instance class (7th generation or newer), then convert the license model as a separate modify operation.