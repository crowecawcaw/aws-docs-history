

# Amazon RDS Extended Support with Amazon RDS
<a name="extended-support"></a>

RDS Extended Support allows you to continue running a database on a major engine version past the RDS end of standard support date for an additional cost. 

You can enroll a database in RDS Extended Support when you first [create](extended-support-creating-db-instance.md) or [restore](extended-support-restoring-db-instance.md) a DB instance. You can also change the enrollment status of an existing DB instance or DB cluster at any time by modifying the `EngineLifecycleSupport` parameter using the AWS CLI or RDS API. This change takes effect immediately with no downtime. For Aurora and Multi-AZ DB clusters, modify the setting at the cluster level.

If you disable the enrollment status of a DB instance or DB cluster that is already past its standard support end date, the instance or cluster automatically upgrades to the next supported major version. See [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) and [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) for more information.

If you enabled RDS Extended Support during the creation or restoration of a DB instance, then after the RDS end of standard support date, Amazon RDS will automatically enroll the DB instance in RDS Extended Support. Automatic enrollment into RDS Extended Support doesn't change the database engine and doesn't impact the uptime or performance of your DB instance. 

RDS Extended Support provides the following updates and technical support:
+ Security updates for [critical and high CVEs](https://nvd.nist.gov/vuln-metrics/cvss) for your DB instance or DB cluster, including the database engine
+ Bug fixes and patches for critical issues
+ The ability to open support cases and receive troubleshooting help within the standard Amazon RDS service level agreement

This paid offering gives you more time to upgrade to a supported major engine version. For example, the RDS end of standard support date for RDS for MySQL version 5.7 is February 29, 2024. However, you aren't ready to manually upgrade to RDS for MySQL version 8.0 before that date. In this case, Amazon RDS automatically enrolls your databases in RDS Extended Support on February 29, 2024, and you can continue to run RDS for MySQL version 5.7. Starting March 1, 2024, Amazon RDS automatically charges you for RDS Extended Support.

RDS Extended Support is available for up to 3 years past the RDS end of standard support date for a major engine version. After this time, if you haven't upgraded your major engine version to a supported version, then Amazon RDS will automatically upgrade your major engine version. We recommend that you upgrade to a supported major engine version as soon as possible.

For more information about the RDS end of standard support dates and the RDS end of Extended Support dates, see [Supported MySQL major versions on Amazon RDS](MySQL.Concepts.VersionMgmt.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar) and [Release calendar for Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-release-calendar.html#Release.Calendar).

**Topics**
+ [Overview of Amazon RDS Extended Support](extended-support-overview.md)
+ [Amazon RDS Extended Support charges](extended-support-charges.md)
+ [Versions with Amazon RDS Extended Support](extended-support-versions.md)
+ [Amazon RDS and customer responsibilities with Amazon RDS Extended Support](extended-support-responsibilities.md)
+ [Creating a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support](extended-support-creating-db-instance.md)
+ [Viewing the enrollment of your DB instances or Multi-AZ DB clusters in Amazon RDS Extended Support](extended-support-viewing.md)
+ [Viewing support dates for engine versions in Amazon RDS Extended Support](extended-support-viewing-support-dates.md)
+ [Restoring a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support](extended-support-restoring-db-instance.md)