# Amazon RDS Extended Support charges

You will incur charges for all engines enrolled in RDS Extended Support
beginning the day after the Aurora end of standard support date. For the Aurora end of
standard support date, see [Amazon Aurora major versions](Aurora.VersionPolicy.md#Aurora.VersionPolicy.MajorVersions "Aurora.VersionPolicy.md#Aurora.VersionPolicy.MajorVersions").

The additional charge for RDS Extended Support automatically stops when you take one of the
following actions:

- Upgrade to an engine version that's covered under standard support.
- Delete the database that's running a major version past the Aurora
  end of standard support date.
  The charges will restart if your target engine version enters RDS Extended Support in the
  future.

For example, Aurora PostgreSQL 11 enters Extended Support on March 1, 2024, but
charges don't start until April 1, 2024. You upgrade your Aurora PostgreSQL 11 database
to Aurora PostgreSQL 12 on April 30, 2024. You will only be charged for 30 days
of Extended Support on Aurora PostgreSQL 11. You continue running Aurora PostgreSQL 12 on this DB instance past the RDS end of standard support
date of February 28, 2025. Your database will again incur RDS Extended Support charges starting on
March 1, 2025.

For more information, see [Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/").

## Avoiding charges for

Amazon RDS Extended Support

You can avoid being charged for RDS Extended Support by preventing Aurora from
creating or restoring an Aurora DB cluster or a global cluster
past the Aurora end of standard support date. To do this, use the AWS CLI or the
RDS API.

In the AWS CLI, specify `open-source-rds-extended-support-disabled` for
the `--engine-lifecycle-support` option. In the RDS API, specify
`open-source-rds-extended-support-disabled` for the
`LifeCycleSupport` parameter. For more information, see [Creating an
Aurora DB cluster or a global cluster](extended-support-creating-db-instance.md "extended-support-creating-db-instance.md") or [Restoring an
Aurora DB cluster or a global cluster](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md").
