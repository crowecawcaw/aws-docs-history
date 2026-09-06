

# Viewing the enrollment of your Aurora DB clusters or global clusters in Amazon RDS Extended Support
<a name="extended-support-viewing"></a>

You can view the enrollment of your Aurora DB clusters or global clusters in RDS Extended Support using the AWS Management Console, the AWS CLI, or the RDS API.

**Note**  
The **RDS Extended Support** column in the console, the -`-engine-lifecycle-support` option in the AWS CLI, and the `EngineLifecycleSupport` parameter in the RDS API only indicate enrollment in RDS Extended Support. Charges for RDS Extended Support only start when your DB engine version has reached the Aurora end of standard support. For more information, see [Amazon Aurora major versions](Aurora.VersionPolicy.Versioning.md#Aurora.VersionPolicy.MajorVersions).   
For example, you have an Aurora PostgreSQL 11 database that is enrolled in RDS Extended Support. On April 1, 2024, Amazon RDS started charging you for RDS Extended Support for this database. On July 31, 2024, you upgraded this database to Aurora PostgreSQL 12. The RDS Extended Support status for this database remains enabled. However, the RDS Extended Support charges for this database stopped because Aurora PostgreSQL 12 hadn't reached Aurora end of standard support yet. Amazon RDS won't charge you for RDS Extended Support for this database until March 1, 2025, which is when Aurora standard support ends for Aurora PostgreSQL 12. 

## Console
<a name="extended-support-viewing-console"></a>

**To view the enrollment of your Aurora DB clusters or global clusters in RDS Extended Support**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**. The value under **RDS Extended Support** indicates if an Aurora DB cluster or global cluster is enrolled in RDS Extended Support. If no value appears, then RDS Extended Support isn't available for your database.
**Tip**  
If the **RDS Extended Support** column doesn't appear, choose the **Preferences** icon, and then turn on **RDS Extended Support**.  
![The Databases section with the RDS Extended Support setting for each database in the RDS console.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/extended-support-view-db-list.png)

1. You can also view the enrollment on the **Configuration** tab for each database. Choose a database under **DB identifier**. On the **Configuration** tab, look under **Extended Support** to see if the database is enrolled or not.   
![The Configuration tab on a database details page that shows the RDS Extended Support status.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/extended-support-view-details-aurora.png)

## AWS CLI
<a name="extended-support-viewing-cli"></a>

To view the enrollment of your databases in RDS Extended Support by using the AWS CLI, run the [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) or [describe-global-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-global-clusters.html) command. 

If RDS Extended Support is available for a database, then the response includes the parameter `EngineLifecycleSupport`. The value `open-source-rds-extended-support` indicates that an Aurora DB cluster or global cluster is enrolled in RDS Extended Support. The value `open-source-rds-extended-support-disabled` indicates that enrollment of the Aurora DB cluster or global cluster in RDS Extended Support was disabled.

**Example**

The following command returns information for all of your Aurora DB clusters:

```
aws rds describe-db-clusters
```

The following response shows that an Aurora PostgreSQL engine running on the Aurora DB cluster `database-1` is enrolled in RDS Extended Support:

```
{
    "DBClusterIdentifier": "database-1",
    ...
    "Engine": "aurora-postgresql",
    ...
    "EngineLifecycleSupport": "open-source-rds-extended-support"
}
```

## RDS API
<a name="extended-support-viewing-api"></a>

To view the enrollment of your databases in RDS Extended Support by using the Amazon RDS API, use the [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) or [DescribeGlobalClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeGlobalClusters.html) operation.

If RDS Extended Support is available for a database, then the response includes the parameter `EngineLifecycleSupport`. The value `open-source-rds-extended-support` indicates that an Aurora DB cluster or global cluster is enrolled in RDS Extended Support. The value `open-source-rds-extended-support-disabled` indicates that enrollment of the Aurora DB cluster or global cluster in RDS Extended Support was disabled.