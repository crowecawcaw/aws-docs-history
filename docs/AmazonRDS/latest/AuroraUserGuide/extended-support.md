# Amazon RDS Extended Support with Amazon Aurora

RDS Extended Support allows you to continue running a database on a major engine version past the
Aurora end
of standard support date for an additional cost.

You can only enroll a database in RDS Extended Support by enabling RDS Extended Support when you first [create](extended-support-creating-db-instance.md "extended-support-creating-db-instance.md") or [restore](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md") a DB instance. You can't
update your RDS Extended Support enrollment status on existing DB instances unless you are restoring
them.

If you enabled RDS Extended Support during the creation or restoration of a DB instance, then after
the Aurora end
of standard support date, Amazon Aurora will automatically enroll the DB instance in
RDS Extended Support. Automatic enrollment into RDS Extended Support doesn't change the database engine and
doesn't impact the uptime or performance of your DB instance.

RDS Extended Support provides the following updates and technical support:

- Security updates for [critical
  and high CVEs](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss") for your DB instance or DB cluster, including the database
  engine
- Bug fixes and patches for critical issues
- The ability to open support cases and receive troubleshooting help within the
  standard Amazon RDS service level agreement
  This paid offering gives you more time to upgrade to a supported major
  engine version. For example, the Aurora end of standard support date for Aurora MySQL version
  2 is October 31, 2024. However, you aren't ready to manually upgrade to Aurora MySQL version 3
  before that date. In this case, Amazon Aurora automatically enrolls your cluster in RDS Extended Support
  on October 31, 2024, and you can continue to run Aurora MySQL version 2. Starting December 1,
  2024, Amazon Aurora automatically charges you for RDS Extended Support.

RDS Extended Support is available for up to 3 years past the community
end of life date for a major engine version (3 years and 4
months for Aurora MySQL version 2). After this time, if you haven't upgraded your
major engine version to a supported version, then Amazon Aurora will automatically upgrade
your major engine version. We recommend that you upgrade to a supported major engine version
as soon as possible.

For more information about the Aurora end of standard support dates and
the RDS end of Extended Support dates, see [Release calendar for Aurora MySQL major versions](../AuroraMySQLReleaseNotes/AuroraMySQL.md#AuroraMySQL.release-calendars.major "../AuroraMySQLReleaseNotes/AuroraMySQL.md#AuroraMySQL.release-calendars.major") and [Release calendar for Aurora PostgreSQL major versions](../AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.md#aurorapostgresql.major.versions.supported "../AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.md#aurorapostgresql.major.versions.supported").

###### Topics

- [Overview of Amazon RDS Extended Support](extended-support-overview.md "extended-support-overview.md")
- [Amazon RDS Extended Support charges](extended-support-charges.md "extended-support-charges.md")
- [Versions with Amazon RDS Extended Support](extended-support-versions.md "extended-support-versions.md")
- [Amazon Aurora and customer
  responsibilities with Amazon RDS Extended Support](extended-support-responsibilities.md "extended-support-responsibilities.md")
- [Creating an
  Aurora DB cluster or a global cluster with Amazon RDS Extended Support](extended-support-creating-db-instance.md "extended-support-creating-db-instance.md")
- [Viewing the enrollment of your Aurora DB clusters or global clusters in Amazon RDS Extended Support](extended-support-viewing.md "extended-support-viewing.md")
- [Viewing support dates for engine
  versions in Amazon RDS Extended Support](extended-support-viewing-support-dates.md "extended-support-viewing-support-dates.md")
- [Restoring an
  Aurora DB cluster or a global cluster with Amazon RDS Extended Support](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md")
