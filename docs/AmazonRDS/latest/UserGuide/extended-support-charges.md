

# Amazon RDS Extended Support charges
<a name="extended-support-charges"></a>

You will incur charges for all engines enrolled in RDS Extended Support beginning the day after the RDS end of standard support date. For the RDS end of standard support date, see [Major versions](MySQL.Concepts.VersionMgmt.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar) and [Release calendar for Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-release-calendar.html). RDS Extended Support charges apply to standby instances in Multi-AZ deployments. 

The additional charge for RDS Extended Support automatically stops when you take one of the following actions: 
+ Upgrade to an engine version that's covered under standard support.
+ Delete the database that's running a major version past the RDS end of standard support date.

The charges will restart if your target engine version enters RDS Extended Support in the future. 

For example, RDS for PostgreSQL 11 enters Extended Support on March 1, 2024, but charges don't start until April 1, 2024. You upgrade your RDS for PostgreSQL 11 database to RDS for PostgreSQL 12 on April 30, 2024. You will only be charged for 30 days of Extended Support on RDS for PostgreSQL 11. You continue running RDS for PostgreSQL 12 on this DB instance past the RDS end of standard support date of February 28, 2025. Your database will again incur RDS Extended Support charges starting on March 1, 2025.

For more information, see [Amazon RDS for MySQL pricing](https://aws.amazon.com/rds/mysql/pricing/) and [Amazon RDS for PostgreSQL pricing](https://aws.amazon.com/rds/postgresql/pricing/).

## Avoiding charges for Amazon RDS Extended Support
<a name="extended-support-avoid-charges"></a>

You can avoid being charged for RDS Extended Support by preventing RDS from creating or restoring a DB instance or a Multi-AZ DB cluster past the RDS end of standard support date. To do this, use the AWS CLI or the RDS API.

You can also avoid being charged for RDS Extended Support by changing the enrollment status of an existing DB instance or DB cluster at any time by modifying the `EngineLifecycleSupport` parameter using the AWS CLI or the RDS API. If you disable the enrollment status of a DB instance or DB cluster that is already past its standard support end date, the instance or cluster automatically upgrades to the next supported major version.

In the AWS CLI, specify `open-source-rds-extended-support-disabled` for the `--engine-lifecycle-support` option. In the RDS API, specify `open-source-rds-extended-support-disabled` for the `EngineLifecycleSupport` parameter. For more information, see [Creating a DB instance or a Multi-AZ DB cluster](extended-support-creating-db-instance.md) or [Restoring a DB instance or a Multi-AZ DB cluster](extended-support-restoring-db-instance.md).