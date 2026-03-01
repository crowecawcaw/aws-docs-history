# Managing Babelfish for Aurora PostgreSQL version updates

Babelfish is an option available with Aurora PostgreSQL version 13.4 and higher
releases. Updates to Babelfish become available with certain new releases of the
Aurora PostgreSQL database engine. For more information, see the [_Release Notes for Aurora PostgreSQL_](../AuroraPostgreSQLReleaseNotes/Welcome.md "../AuroraPostgreSQLReleaseNotes/Welcome.md").

###### Note

Babelfish DB clusters running on any version of Aurora PostgreSQL 13 can't be
upgraded to Aurora PostgreSQL 14.3, 14.4, and 14.5. Also, Babelfish doesn't support a
direct upgrade from 13.x to 15.x. You must first upgrade your 13.x DB cluster to 14.6 and
higher version and then upgrade to 15.x version.

For a list of supported functionality across different Babelfish releases, see
[Supported functionalities in Babelfish by version](babelfish-compatibility.md "babelfish-compatibility.md").

For a list of currently unsupported functionality, see [Unsupported functionalities in Babelfish](babelfish-compatibility.tsql.md "babelfish-compatibility.tsql.md").

You can get a list of Aurora PostgreSQL versions that support Babelfish by querying
your AWS Region using the [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS CLI command, as follows.

For Linux, macOS, or Unix:

```
`$` aws rds describe-db-engine-versions --region us-east-1 \
    --engine aurora-postgresql \
    --query '*[]|[?SupportsBabelfish==`true`].[EngineVersion]' \
    --output text

```

For more information, see [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") in the
_AWS CLI Command Reference_.

In the following topics, you can learn how to identify the version of Babelfish
running on your Aurora PostgreSQL DB cluster, and how to upgrade to a new version.

###### Contents

- [Identifying your version of Babelfish](babelfish-information-identify-version.md "babelfish-information-identify-version.md")
- [Upgrading your Babelfish cluster to a new version](babelfish-information-upgrading.md "babelfish-information-upgrading.md")
  - [Upgrading Babelfish to a new minor version](babelfish-information-upgrading-minor.md "babelfish-information-upgrading-minor.md")
  - [Upgrading Babelfish to a new major version](babelfish-information-upgrading-major.md "babelfish-information-upgrading-major.md")
    - [Before upgrading Babelfish to a new major version](babelfish-information-upgrading-major.md#babelfish-information-upgrading-preliminary "babelfish-information-upgrading-major.md#babelfish-information-upgrading-preliminary")
    - [Performing major version upgrade](babelfish-information-upgrading-major.md#babelfish-performing-major-version-upgrade "babelfish-information-upgrading-major.md#babelfish-performing-major-version-upgrade")
    - [After upgrading to a new major version](babelfish-information-upgrading-major.md#babelfish-information-upgrading-post-upgrade "babelfish-information-upgrading-major.md#babelfish-information-upgrading-post-upgrade")
    - [Example: Upgrading the Babelfish DB cluster to a major release](babelfish-information-upgrading-major.md#babelfish-information-upgrading-example "babelfish-information-upgrading-major.md#babelfish-information-upgrading-example")

- [Using Babelfish product version parameter](babelfish-guc-version.md "babelfish-guc-version.md")
  - [Configuring Babelfish product version parameter](babelfish-guc-version.md#babelfish-guc-version-setvalues "babelfish-guc-version.md#babelfish-guc-version-setvalues")
  - [Affected queries and parameter](babelfish-guc-version.md#babelfish-guc-version-affects "babelfish-guc-version.md#babelfish-guc-version-affects")
  - [Interface with babelfishpg_tsql.version parameter](babelfish-guc-version.md#babelfish-guc-version-tsql "babelfish-guc-version.md#babelfish-guc-version-tsql")
