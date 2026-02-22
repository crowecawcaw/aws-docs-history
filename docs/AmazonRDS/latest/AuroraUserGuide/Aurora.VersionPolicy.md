# Amazon Aurora versioning

Amazon Aurora versions are different from the upstream community databases that they’re
compatible with. To help you maintain application compatibility and leverage the latest DB
engine features, the following sections explain Aurora versioning conventions and how Aurora
versions map to their respective community databases.

For a list of the relational databases that are available on Amazon Aurora, see [Supported database engines for
Amazon Aurora database clusters](Aurora.md#Aurora.VersionPolicy.SupportedEngines "Aurora.md#Aurora.VersionPolicy.SupportedEngines").

## Differences in version numbers

between community databases and Aurora

Each Amazon Aurora version is compatible with a specific version of its corresponding
community database. You can find the community version of your database with the
`version` function, and the Aurora version with the `aurora_version`
function.

The following examples show how to find the community version of your database for
Aurora MySQL and Aurora PostgreSQL.

Aurora MySQL
The `version` function returns the community version of your database
for Aurora MySQL.

```
mysql> select version();
```

Output example:

```
+------------------+
|   version()      |
+------------------+
|  8.0.32          |
+------------------+
```

And the `aurora_version` function returns the Aurora version:

```
mysql> select aurora_version(), @@aurora_version;
```

Output example:

```
+------------------+------------------+
| aurora_version() | @@aurora_version |
+------------------+------------------+
| 3.05.2           | 3.05.2           |
+------------------+------------------+
```

Aurora PostgreSQL
The `version` function returns the community version of your database
for Aurora PostgreSQL.

```
postgres=> select version();
```

Output example:

```
-----------------------------------------------------------------------------
PostgreSQL 11.7 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.9.3, 64-bit
(1 row)
```

And the `aurora_version` function returns the Aurora version:

```
postgres=> select aurora_version();
```

Output example:

```
aurora_version
----------------
3.2.2
```

For more information, see [Checking Aurora MySQL versions using SQL](AuroraMySQL.Updates.md#AuroraMySQL.Updates.DBVersions "AuroraMySQL.Updates.md#AuroraMySQL.Updates.DBVersions") and [Identifying versions of
Amazon Aurora PostgreSQL](AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.Versions "AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.Versions").

## Default Amazon Aurora versions

The _default version_ is the version that Aurora chooses
automatically for database creation or upgrade when you don't manually specify a target
engine version. For example, the following command shows the default engine version for
Aurora PostgreSQL (sample output included).

```
aws rds describe-db-engine-versions \
    --engine aurora-postgresql \
    --default-only \
    --query 'DBEngineVersions[0].EngineVersion' \
    --output text

**16.4**
```

Every major version has a corresponding default minor version. Thus, the default minor
version is 16._n_ for Aurora PostgreSQL 16, with version number
_n_ changing when Aurora releases new default minor versions.
Typically, Aurora releases two default minor versions for every major version per year. The
following bash shell script shows the default minor versions for a set of Aurora PostgreSQL
major versions (sample output included).

```
for major in 16 15 14 13 12 11; do
  echo -n "Default for Aurora PostgreSQL major version $major: "
  aws rds describe-db-engine-versions \
    --engine aurora-postgresql \
    --engine-version "$major" \
    --default-only \
    --query 'DBEngineVersions[0].EngineVersion' \
    --output text
done

**Default for Aurora PostgreSQL major version 16: 16.4
Default for Aurora PostgreSQL major version 15: 15.8
Default for Aurora PostgreSQL major version 14: 14.13
Default for Aurora PostgreSQL major version 13: 13.16
Default for Aurora PostgreSQL major version 12: 12.20
Default for Aurora PostgreSQL major version 11: 11.21**
```

If you enable automatic minor version upgrades for your Aurora DB cluster, Aurora uses either the
default minor version or a newer minor version for a given major version. For example, if the
default minor version for Aurora PostgreSQL 15 is 15.8, and newer version 15.10 is also available,
Aurora can automatically upgrade to either 15.8 or 15.10.

## Amazon Aurora major versions

Aurora versions use the
``major`.`minor`.`patch``
scheme. An _Aurora major version_ refers to the MySQL or
PostgreSQL community major version that Aurora is compatible with. Aurora MySQL and
Aurora PostgreSQL major versions are available under standard support at least until community
end of life for the corresponding community version. You can continue to run a major version
past its Aurora end of standard support date for a fee. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md") and [Amazon Aurora pricing](https://aws.amazon.com/rds/aurora/pricing/ "https://aws.amazon.com/rds/aurora/pricing/").

For more information on major versions and the release calendar for Aurora MySQL and
Aurora PostgreSQL, see the following pages in the respective Release Notes:

- [Release calendar for Aurora MySQL major versions](../AuroraMySQLReleaseNotes/AuroraMySQL.md#AuroraMySQL.release-calendars.major "../AuroraMySQLReleaseNotes/AuroraMySQL.md#AuroraMySQL.release-calendars.major")
- [Release calendar for Aurora PostgreSQL major versions](../AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.md#aurorapostgresql.major.versions.supported "../AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.md#aurorapostgresql.major.versions.supported")

You can also view information about support dates for major engine versions by running
the [describe-db-major-engine-versions](../../../cli/latest/reference/rds/describe-db-major-engine-versions.md "../../../cli/latest/reference/rds/describe-db-major-engine-versions.md") AWS CLI command or by using the [DescribeDBMajorEngineVersions](../APIReference/API_DescribeDBMajorEngineVersions.md "../APIReference/API_DescribeDBMajorEngineVersions.md") RDS API operation.

###### Note

Amazon RDS Extended Support for Aurora MySQL version 2 starts on November 1, 2024, but you won't be
charged until December 1, 2024. Between November 1 and November 30, 2024, all Aurora MySQL
version 2 DB clusters are covered under Amazon RDS Extended Support. For more information, see [Amazon RDS Extended Support for selected Aurora versions](Aurora.VersionPolicy.md#Aurora.VersionPolicy.ES "Aurora.VersionPolicy.md#Aurora.VersionPolicy.ES").

### How long Amazon Aurora major

versions remain available

Amazon Aurora major versions remain available at least until community end of life for the
corresponding community version. You can use Aurora end of standard support dates to plan
your testing and upgrade cycles. These dates represent the earliest date that an upgrade
to a newer version might be required. For more information on the dates, see [Amazon Aurora major versions](#Aurora.VersionPolicy.MajorVersions "#Aurora.VersionPolicy.MajorVersions").

Before Aurora asks you to upgrade to a newer major version and to help you plan, you
receive a reminder at least 12 months in advance. The reminders communicate the following about the
upgrade process.

- The timing of certain milestones
- The impact on your DB clusters
- Recommended actions

We recommend that you thoroughly test your applications with new
database versions before upgrading your cluster to a new major version.

After the major version reaches the Aurora end of standard support, any DB cluster still
running the earlier version is automatically upgraded to an Extended Support version during
a scheduled maintenance window. Extended Support charges may apply. For more information
on Amazon RDS Extended Support, see [Using Amazon RDS Extended
support](extended-support.md "extended-support.md").

## Amazon Aurora minor versions

Aurora versions use the
``major`.`minor`.`patch``
scheme. An _Aurora minor version_ provides incremental
community and Aurora-specific improvements to the service, for example new features and
fixes.

For more information on minor versions and the release calendar for Aurora MySQL and
Aurora PostgreSQL, see the following pages in the respective Release Notes:

- [Release calendar for Aurora MySQL minor versions](../AuroraMySQLReleaseNotes/AuroraMySQL.md#AuroraMySQL.release-calendars.minor "../AuroraMySQLReleaseNotes/AuroraMySQL.md#AuroraMySQL.release-calendars.minor")
- [Release calendar for Aurora PostgreSQL minor versions](../AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.md#aurorapostgresql.minor.versions.supported "../AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.md#aurorapostgresql.minor.versions.supported")

The following sections describe details about the cadence and lifetime that you can
expect for Aurora minor versions.

###### Topics

- [How often Amazon Aurora minor
  versions are released](#Aurora.VersionPolicy.MinorVersionCadence "#Aurora.VersionPolicy.MinorVersionCadence")
- [How long Amazon Aurora minor
  versions remain available](#Aurora.VersionPolicy.MinorVersionLifetime "#Aurora.VersionPolicy.MinorVersionLifetime")

### How often Amazon Aurora minor

versions are released

In general, Amazon Aurora minor versions are released quarterly. The release schedule
might vary to pick up additional features or fixes.

### How long Amazon Aurora minor

versions remain available

Typically, Amazon Aurora makes every minor version of a particular major version available
for at least 12 months. At the end of this period, Aurora might automatically upgrade your
database to the default minor version or to a later version. Aurora begins the upgrade
during the scheduled maintenance window for any DB cluster that is running the earlier minor
version.

In some cases, Aurora might replace a minor version of a particular major version
sooner than the usual 12-month period. Reasons can include critical security issues or the
end-of-support date for a major version.

Before beginning automatic upgrades of minor versions that are approaching end of
life, Aurora typically provides a reminder three months in advance. Aurora details the
following about the upgrade process.

- The timing of certain milestones
- The impact on your DB clusters
- Recommended actions

Notifications with less than three months notice describe
critical matters, such as security issues, that require quicker action.

If the **Auto minor version upgrade** setting is enabled, you get a
reminder but no RDS event notification. Aurora upgrades your database within a maintenance
window after the mandatory upgrade deadline has passed.

If the **Auto minor version upgrade** setting isn't enabled, you get
a reminder and an Amazon RDS DB cluster event with a category of `maintenance` and ID of
`RDS-EVENT-0156`. Aurora upgrades your database within the next maintenance
window.

Note that after a minor version reaches the Aurora end of standard support, no
further patch versions will be released for that minor version. To receive critical bug fixes
or CVEs, you must upgrade to a minor version with standard support.

For more information about automatic minor version upgrades, see [Automatic minor version upgrades for Aurora
DB clusters](USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU "USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU").

## Amazon Aurora patch versions

Aurora versions use the
``major`.`minor`.`patch``
scheme. An Aurora patch version includes important fixes added to a minor version after its
initial release (for example, Aurora MySQL 3.04.0, 3.04.1, ..., 3.04.3). While each new minor
version provides new Aurora features, new patch versions within a specific minor version are
primarily used to resolve important issues.

For more information on patching, see [Maintaining an Amazon Aurora DB cluster](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").
