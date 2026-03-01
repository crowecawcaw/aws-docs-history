# Using an Aurora PostgreSQL long-term support (LTS) release

Each new Aurora PostgreSQL version remains available for a certain amount of time for you to use when you create or
upgrade a DB cluster. After this period, you must upgrade any clusters that use that version. You can manually
upgrade your cluster before the support period ends, or Aurora can automatically upgrade it for you when its
Aurora PostgreSQL version is no longer supported.

Aurora designates certain Aurora PostgreSQL versions as long-term support (LTS) releases. Database clusters that use LTS
releases can stay on the same version longer and undergo fewer upgrade cycles than clusters that use non-LTS
releases. LTS minor versions include only bug fixes (through patch versions) for critical stability and security issues;
an LTS version doesn't include new features released after its introduction.

Once a year, DB clusters running on an LTS minor version are patched to the latest
patch version of the LTS release. We do this patching to help ensure that you benefit from cumulative security and
stability fixes. We might patch an LTS minor version more frequently if there are critical fixes, such as for security,
that need to be applied.

###### Note

If you want to remain on an LTS minor version for the duration of its lifecycle, make sure to disable automatic minor version upgrade for your DB
instances. To avoid automatically upgrading your DB cluster from the LTS minor version, clear the **Enable auto minor version upgrade**
check box on any DB instance in your Aurora cluster.

We recommend that you upgrade to the latest release, instead of using the LTS release, for most of your
Aurora PostgreSQL clusters. Doing so takes advantage of Aurora as a managed service and gives you access to the latest
features and bug fixes. LTS releases are intended for clusters with the following characteristics:

- You can't afford downtime on your Aurora PostgreSQL application for upgrades outside of rare occurrences for
  critical patches.
- The testing cycle for the cluster and associated applications takes a long time for each update to the
  Aurora PostgreSQL database engine.
- The database version for your Aurora PostgreSQL cluster has all the DB engine features and bug fixes that your
  application needs.

The current LTS releases for Aurora PostgreSQL are as follows:

- PostgreSQL 16.8. It was released on April 07, 2025. For more information, see
  [PostgreSQL 16.8](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#aurorapostgresql-versions-version168x "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#aurorapostgresql-versions-version168x") in the _Release Notes for Aurora PostgreSQL_.
- PostgreSQL 15.10. It was released on December 27, 2024. For more information, see
  [PostgreSQL 15.10](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#aurorapostgresql-versions-version1510x "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#aurorapostgresql-versions-version1510x") in the _Release Notes for Aurora PostgreSQL_.
- PostgreSQL 14.6. It was released on January 20, 2023. For more information, see
  [PostgreSQL 14.6](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.146X "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.146X") in the _Release Notes for Aurora PostgreSQL_.
- PostgreSQL 13.9. It was released on January 20, 2023. For more information, see
  [PostgreSQL 13.9](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.139X "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.139X") in the _Release Notes for Aurora PostgreSQL_.
- PostgreSQL 12.9. It was released on February 25, 2022. For more information, see
  [PostgreSQL 12.9](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.129 "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.129") in the _Release Notes for Aurora PostgreSQL_.
- PostgreSQL 11.9 (Aurora PostgreSQL release 3.4. It was released on December 11, 2020. For more information about this version, see
  [PostgreSQL 11.9, Aurora PostgreSQL release 3.4](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.34 "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.34") in the _Release Notes for Aurora PostgreSQL_.
  For details about support timelines and release cycles for the LTS versions, see
  [Release calendars for Aurora PostgreSQL](../AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.md "../AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.md").

For information about how to identify Aurora and database engine versions, see
[Identifying versions of Amazon Aurora PostgreSQL](AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.Versions "AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.Versions").
