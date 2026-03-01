# Viewing support dates for engine versions in Amazon RDS Extended Support

You can view information about support dates for engine versions for your DB instances or Multi-AZ DB clusters in Amazon RDS Extended Support by using
the AWS CLI or the RDS API. This
information can help you plan for upgrades.

AWS CLI commands and RDS API operations return start and end dates for
RDS
standard support and RDS Extended Support. These dates can also be found in the major engine version
tables. For more information, see [Supported MySQL major versions on Amazon RDS](MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar "MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar") and [Release calendar for Amazon RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-release-calendar.md "../PostgreSQLReleaseNotes/postgresql-release-calendar.md") in the _Amazon RDS for PostgreSQL
Release Notes_.

To view the start and end dates for RDS standard support and
RDS Extended Support for your major engine versions by using the AWS CLI, run the [describe-db-major-engine-versions](../../../cli/latest/reference/rds/describe-db-major-engine-versions.md "../../../cli/latest/reference/rds/describe-db-major-engine-versions.md") command.

This command returns the following relevant parameters for
open source engines (MariaDB, MySQL, and PostgreSQL). It doesn't return these
parameters for commercial engines (Db2, SQL Server, and Oracle).

- `SupportedEngineLifecycles` – This parameter is an array
  of objects that include `LifecycleSupportName`,
  `LifecycleSupportStartDate`, and
  `LifecycleSupportEndDate`.
- `LifecycleSupportName` – This parameter indicates the
  type of support the engine version is in: RDS standard support
  (`open-source-rds-standard-support`) or RDS Extended Support
  (`open-source-rds-extended-support`). For MariaDB, this parameter only returns RDS
  standard support
  (`open-source-rds-standard-support`).
- `LifecycleSupportStartDate` – This parameter lists the
  start date for either RDS standard support or RDS Extended Support for
  the major engine version, depending on the value of
  `LifecycleSupportName`.
- `LifecycleSupportEndDate` – This parameter lists the end
  date for either RDS standard support or RDS Extended Support for
  the major engine version, depending on the value of
  `LifecycleSupportName`.
  **Example**

The response example shows the following information:

- The start and end dates for the supported engine
  lifecycles `open-source-rds-standard-support` and
  `open-source-rds-extended-support` for MySQL 5.7. RDS Extended Support
  is available for MySQL 5.7.
- The start and end dates for the supported engine lifecycle
  `open-source-rds-standard-support` for MariaDB 10.6.
  RDS Extended Support isn't available for MariaDB 10.6.
- No information about supported engine lifecycles for SQL Server Enterprise
  Edition 13 because SQL Server is a commercial engine.

```
{
    "DBMajorEngineVersions": [
        {
            "Engine": "mysql",
            "MajorEngineVersion": "5.7",
            "SupportedEngineLifecycles": [
                {
                    "LifecycleSupportName": "open-source-rds-standard-support",
                    "LifecycleSupportStartDate": "2016-02-22T00:00:00+00:00",
                    "LifecycleSupportEndDate": "2024-02-29T23:59:59.999000+00:00"
                },
                {
                    "LifecycleSupportName": "open-source-rds-extended-support",
                    "LifecycleSupportStartDate": "2024-03-01T00:00:00+00:00",
                    "LifecycleSupportEndDate": "2027-02-28T23:59:59.999000+00:00"
                }
            ]
        },
        {
            "Engine": "mariadb",
            "MajorEngineVersion": "10.6",
            "SupportedEngineLifecycles": [
                {
                    "LifecycleSupportName": "open-source-rds-standard-support",
                    "LifecycleSupportStartDate": "2022-02-03T00:00:00+00:00",
                    "LifecycleSupportEndDate": "2026-07-31T23:59:59.999000+00:00"
                }
            ]
        },
        {
            "Engine": "sqlserver-ee",
            "MajorEngineVersion": "13.00"
        },
        ...
    ]
}
```

To view the start and end dates for RDS standard support and
RDS Extended Support for your major engine versions by using the RDS API, use the [DescribeDBMajorEngineVersions](../APIReference/API_DescribeDBMajorEngineVersions.md "../APIReference/API_DescribeDBMajorEngineVersions.md") operation.

If RDS Extended Support is available for an engine version, then the response includes the
parameter `SupportedEngineLifeCycles` as an array with two objects. One
object includes the start and end dates for RDS standard support. The
second object includes the start and end dates for RDS Extended Support.

If RDS Extended Support isn't available for an open source engine
version (MariaDB, MySQL, and PostgreSQL), then the response only includes the
parameter `SupportedEngineLifeCycles` as an array with a single object.
This object includes the start and end dates for RDS standard support.

If the engine version is for a commercial engine (Db2, SQL
Server, and Oracle), then the response doesn't include the parameter
`SupportedEngineLifeCycles`.
