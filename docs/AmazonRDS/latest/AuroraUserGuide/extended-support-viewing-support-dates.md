# Viewing support dates for engine versions in Amazon RDS Extended Support

You can view information about support dates for engine versions for your Aurora DB clusters
or global clusters in Amazon RDS Extended Support by using
the AWS CLI or the RDS API. This
information can help you plan for upgrades.

AWS CLI commands and RDS API operations return start and end dates for
Aurora
standard support and RDS Extended Support. These dates can also be found in the major engine version
tables. For more information,
see [Amazon Aurora major versions](Aurora.VersionPolicy.md#Aurora.VersionPolicy.MajorVersions "Aurora.VersionPolicy.md#Aurora.VersionPolicy.MajorVersions").

To view the start and end dates for Aurora standard support and
RDS Extended Support for your major engine versions by using the AWS CLI, run the [describe-db-major-engine-versions](../../../cli/latest/reference/rds/describe-db-major-engine-versions.md "../../../cli/latest/reference/rds/describe-db-major-engine-versions.md") command.

This command returns the following relevant parameters:

- `SupportedEngineLifecycles` – This parameter is an array
  of objects that include `LifecycleSupportName`,
  `LifecycleSupportStartDate`, and
  `LifecycleSupportEndDate`.
- `LifecycleSupportName` – This parameter indicates the
  type of support the engine version is in: Aurora standard support
  (`open-source-rds-standard-support`) or RDS Extended Support
  (`open-source-rds-extended-support`).
- `LifecycleSupportStartDate` – This parameter lists the
  start date for either Aurora standard support or RDS Extended Support for
  the major engine version, depending on the value of
  `LifecycleSupportName`.
- `LifecycleSupportEndDate` – This parameter lists the end
  date for either Aurora standard support or RDS Extended Support for
  the major engine version, depending on the value of
  `LifecycleSupportName`.
  **Example**

The response example shows the start and end dates for the
supported engine life cycles `open-source-rds-standard-support` and
`open-source-rds-extended-support` for Aurora MySQL version 2 (MySQL
5.7). RDS Extended Support is available for Aurora MySQL version 2 (MySQL 5.7).

```
{
    "DBMajorEngineVersions": [
        {
            "Engine": "aurora-mysql",
            "MajorEngineVersion": "5.7",
            "SupportedEngineLifecycles": [
                {
                    "LifecycleSupportName": "open-source-rds-standard-support",
                    "LifecycleSupportStartDate": "2018-02-06T00:00:00+00:00",
                    "LifecycleSupportEndDate": "2024-10-31T23:59:59.999000+00:00"
                },
                {
                    "LifecycleSupportName": "open-source-rds-extended-support",
                    "LifecycleSupportStartDate": "2024-11-01T00:00:00+00:00",
                    "LifecycleSupportEndDate": "2027-02-28T23:59:59.999000+00:00"
                }
            ]
        },
        ...
    ]
}
```

To view the start and end dates for Aurora standard support and
RDS Extended Support for your major engine versions by using the RDS API, use the [DescribeDBMajorEngineVersions](../APIReference/API_DescribeDBMajorEngineVersions.md "../APIReference/API_DescribeDBMajorEngineVersions.md") operation.

If RDS Extended Support is available for an engine version, then the response includes the
parameter `SupportedEngineLifeCycles` as an array with two objects. One
object includes the start and end dates for Aurora standard support. The
second object includes the start and end dates for RDS Extended Support.

If RDS Extended Support isn't available for an engine version, then the
response only includes the parameter `SupportedEngineLifeCycles` as an
array with a single object. This object includes the start and end dates for Aurora
standard support.
