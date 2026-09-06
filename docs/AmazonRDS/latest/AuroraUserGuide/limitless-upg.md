

# Upgrading Amazon Aurora PostgreSQL Limitless Database
<a name="limitless-upg"></a>

The following apply to upgrading Aurora PostgreSQL Limitless Database:
+ Minor version upgrades are supported.
+ Patching Aurora PostgreSQL Limitless Database is supported. Patches appear as pending maintenance to be applied during your maintenance window.

## Upgrading DB clusters that use Amazon Aurora PostgreSQL Limitless Database
<a name="limitless-upgrade"></a>

You upgrade a DB cluster by modifying it and choosing a new DB engine version. You can use the AWS Management Console or the AWS CLI.

### Console
<a name="limitless-upgrade.CON"></a>

**To upgrade your Limitless Database DB cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Navigate to the **Databases** page.

1. Select the Limitless Database DB cluster that you want to upgrade.

1. Choose **Modify**.

   The **Modify DB cluster** page displays.

1. For **DB engine version**, choose the new DB engine version, for example **Aurora PostgreSQL with Limitless Database (Compatible with PostgreSQL 16.6)**.

1. Choose **Continue**.

1. On the summary page, select whether to apply the changes immediately or during the next scheduled maintenance window, then choose **Modify cluster**.

### CLI
<a name="limitless-upgrade.CLI"></a>

Use the [modify-db-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster.html) AWS CLI command, as shown in the following example.

```
aws rds modify-db-cluster \
    --db-cluster-identifier my-sv2-cluster \
    --engine-version {{16.6-limitless}} \
    --apply-immediately
```