# Available PostgreSQL database versions

Amazon RDS supports DB instances running several editions of PostgreSQL. You can specify
any currently available PostgreSQL version when creating a new DB instance. You can
specify the major version (such as PostgreSQL 14), and any available minor version for
the specified major version. If no version is specified, Amazon RDS defaults to an available
version, typically the most recent version. If a major version is specified but a minor
version is not, Amazon RDS defaults to a recent release of the major version you have
specified.

To see a list of available versions, as well as defaults for newly created DB
instances, use the [`describe-db-engine-versions`](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS CLI command. For example, to
display the default PostgreSQL engine version, use the following command:

```
aws rds describe-db-engine-versions --default-only --engine postgres
```

For details about the PostgreSQL versions that are supported on Amazon RDS, see the [_Amazon RDS for PostgreSQL Release Notes_](../PostgreSQLReleaseNotes/Welcome.md "../PostgreSQLReleaseNotes/Welcome.md"). You can also view information
about support dates for major engine versions by running the [describe-db-major-engine-versions](../../../cli/latest/reference/rds/describe-db-major-engine-versions.md "../../../cli/latest/reference/rds/describe-db-major-engine-versions.md") AWS CLI command or by using the [DescribeDBMajorEngineVersions](../APIReference/API_DescribeDBMajorEngineVersions.md "../APIReference/API_DescribeDBMajorEngineVersions.md") RDS API operation.

If you aren't ready to manually upgrade to a new major engine version before the RDS
end of standard support date, Amazon RDS will automatically enroll your databases in
Amazon RDS Extended Support after the RDS end of standard support date. Then, you can continue to run
RDS for PostgreSQL version 11 and higher. For more information, see [Amazon RDS Extended Support with Amazon RDS](extended-support.md "extended-support.md") and [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/").

## Deprecated versions for Amazon RDS for PostgreSQL

Note the following deprecated versions:

- RDS for PostgreSQL 10 was deprecated in February 2023.
- RDS for PostgreSQL 9.6 was deprecated in March 2022.
- RDS for PostgreSQL 9.5 was deprecated in March 2021.

To learn more about deprecation policy for RDS for PostgreSQL, see [Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/ "https://aws.amazon.com/rds/faqs/"). For more information about
PostgreSQL versions, see [Versioning Policy](https://www.postgresql.org/support/versioning/ "https://www.postgresql.org/support/versioning/") in the PostgreSQL documentation.
