# Amazon Aurora version support

If your Amazon Aurora DB has complex dependencies on specific database engine behavior, we
recommend that you engage in extensive testing before you upgrade to newer database engine
versions. There are long-term support options so that you can maintain your DB clusters on
select Aurora engine versions even after they have been superseded by newer versions. The
following sections explain the long-term support options for your Aurora DB clusters.

## Long-term support for selected Amazon Aurora minor versions

For each Aurora major version, certain minor versions are designated as long-term-support
(LTS) versions, and made available for at least three years. That is, at least one minor
version per major version is made available for longer than the typical 12 months.
Typically, Aurora reminds you six months before the end of this period. Aurora communicates
the following about the upgrade process.

- The timing of certain milestones
- The impact on your DB clusters
- Recommended actions

Notifications with less than six months notice communicate
critical matters, such as security issues, that necessitate quicker action.

LTS minor versions include only critical fixes (through patch versions). An LTS version
doesn't include new features released after its introduction. Once a year, DB clusters
running on an LTS minor version are patched to the latest patch version of the LTS release.
Aurora patches your clusters so that you benefit from cumulative security and stability
fixes. If there are critical fixes, Aurora might patch an LTS minor version more frequently,
such as for security, that need to be applied.

###### Note

If you want to remain on an LTS minor version for the duration of its lifecycle, make
sure to disable automatic minor version upgrade for your DB instances. To avoid
automatically upgrading your DB cluster from the LTS minor version, clear the
**Enable auto minor version upgrade** check box on any DB instance in
your Aurora cluster.

For the version numbers of all Aurora LTS versions, see [Aurora MySQL long-term support (LTS) releases](AuroraMySQL.Update.md#AuroraMySQL.Updates.LTS "AuroraMySQL.Update.md#AuroraMySQL.Updates.LTS") and [Using an Aurora PostgreSQL long-term support (LTS) release](AuroraPostgreSQL.Updates.md "AuroraPostgreSQL.Updates.md").

## Amazon RDS Extended Support for selected Aurora versions

With Amazon RDS Extended Support, you can continue to run your database on a major engine version past the
Aurora end of standard support date for an additional cost. During RDS Extended Support, Amazon RDS will
supply patches for Critical and High CVEs as defined by the National Vulnerability Database
(NVD) CVSS severity ratings. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

RDS Extended Support is only available on certain Aurora versions. For more information, see [Amazon Aurora major versions](Aurora.VersionPolicy.md#Aurora.VersionPolicy.MajorVersions "Aurora.VersionPolicy.md#Aurora.VersionPolicy.MajorVersions").
