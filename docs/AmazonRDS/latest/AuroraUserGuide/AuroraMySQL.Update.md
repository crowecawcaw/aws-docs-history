# Long-term support (LTS) and beta releases for Amazon Aurora MySQL

Aurora MySQL provides long-term support (LTS) and beta releases for some Aurora MySQL engine versions.

###### Topics

- [Aurora MySQL long-term support (LTS) releases](#AuroraMySQL.Updates.LTS "#AuroraMySQL.Updates.LTS")
- [Aurora MySQL beta releases](#AuroraMySQL.Updates.Beta "#AuroraMySQL.Updates.Beta")

## Aurora MySQL long-term support (LTS) releases

Each new Aurora MySQL version remains available for a certain amount of time for you to use when you create or upgrade a DB cluster.
After this period, you must upgrade any clusters that use that version. You can manually upgrade your cluster before the support
period ends, or Aurora can automatically upgrade it for you when its Aurora MySQL version is no longer supported.

Aurora designates certain Aurora MySQL versions as long-term support (LTS) releases. DB clusters that use LTS releases can stay on the
same version longer and undergo fewer upgrade cycles than clusters that use non-LTS releases. Database clusters that use LTS releases can
stay on the same minor version for at least three years, or until end of standard support for the major version, whichever comes first.
When a DB cluster that's on an LTS release is required to upgrade,
Aurora upgrades it to the next LTS release. That way, the cluster doesn't need to be upgraded again for a long time.

During the lifetime of an Aurora MySQL LTS release, new patch levels introduce fixes to important issues. The patch levels don't
include any new features. You can choose whether to apply such patches to DB clusters running the LTS release. We recommend customers
running LTS releases to upgrade to the latest patch release of the LTS minor version at least once a year to take advantage of high severity
security and operational fixes. For certain critical fixes, Amazon might perform a managed upgrade to a patch level within the same LTS release.
Such managed upgrades are performed automatically within the cluster maintenance window. All Aurora MySQL releases (both LTS and non-LTS releases)
undergo extensive stability and operational testing. Select minor versions are designated as LTS releases to enable customers to stay on those minor
versions longer without upgrading to a newer minor version.

We recommend that you upgrade to the latest release, instead of using the LTS release, for most of your Aurora MySQL clusters. Doing
so takes advantage of Aurora as a managed service and gives you access to the latest features and bug fixes. The LTS releases are
intended for clusters with the following characteristics:

- You can't afford downtime on your Aurora MySQL application for upgrades outside of rare occurrences for critical patches.
- The testing cycle for the cluster and associated applications takes a long time for each update to the Aurora MySQL database
  engine.
- The database version for your Aurora MySQL cluster has all the DB engine features and bug fixes that your application
  needs.

The current LTS releases for Aurora MySQL are as follows:

- Aurora MySQL version 3.10.\*.
- Aurora MySQL version 3.04.\*.

For more details about the LTS version, see
[Database
engine updates for Amazon Aurora MySQL version 3](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md") in the _Release Notes for Aurora MySQL_.

###### Note

We recommend that you disable automatic minor version upgrades for LTS versions. Set the `AutoMinorVersionUpgrade` parameter to
`false`, or clear the **Enable auto minor version upgrade** check box on the AWS Management Console.

If you don't disable it, your DB cluster could be upgraded to a non-LTS version.

## Aurora MySQL beta releases

An Aurora MySQL beta release is an early, security fix–only release in a limited number of AWS Regions. These fixes are
later deployed more broadly across all Regions with the next patch release.

The numbering for a beta release is similar to an Aurora MySQL minor version, but with an extra fourth digit, for example
2.12.0.1 or 3.05.0.1.

For more information, see [Database engine updates for Amazon Aurora MySQL
version 2](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md") and [Database engine updates for Amazon Aurora MySQL
version 3](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md") in the _Release Notes for Aurora MySQL_.
