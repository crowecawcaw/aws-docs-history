# Amazon RDS Extended Support with Amazon RDS

RDS Extended Support allows you to continue running a database on a major engine version past the
RDS end
of standard support date for an additional cost.

You can only enroll a database in RDS Extended Support by enabling RDS Extended Support when you first [create](extended-support-creating-db-instance.md "extended-support-creating-db-instance.md") or [restore](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md") a DB instance. You can't
update your RDS Extended Support enrollment status on existing DB instances unless you are restoring
them.

If you enabled RDS Extended Support during the creation or restoration of a DB instance, then after
the RDS end
of standard support date, Amazon RDS will automatically enroll the DB instance in
RDS Extended Support. Automatic enrollment into RDS Extended Support doesn't change the database engine and
doesn't impact the uptime or performance of your DB instance.

RDS Extended Support provides the following updates and technical support:

- Security updates for [critical
  and high CVEs](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss") for your DB instance or DB cluster, including the database
  engine
- Bug fixes and patches for critical issues
- The ability to open support cases and receive troubleshooting help within the
  standard Amazon RDS service level agreement
  This paid offering gives you more time to upgrade to a supported
  major engine version. For example, the RDS end of standard support date for RDS for MySQL
  version 5.7 is February 29, 2024. However, you aren't ready to manually upgrade to
  RDS for MySQL version 8.0 before that date. In this case, Amazon RDS automatically enrolls your
  databases in RDS Extended Support on February 29, 2024, and you can continue to run RDS for MySQL version
  5.7. Starting March 1, 2024, Amazon RDS automatically charges you for RDS Extended Support.

RDS Extended Support is available for up to 3 years past the RDS end of standard support
date for a major engine version. After this time, if you haven't upgraded your
major engine version to a supported version, then Amazon RDS will automatically upgrade
your major engine version. We recommend that you upgrade to a supported major engine version
as soon as possible.

For more information about the RDS end of standard support dates and
the RDS end of Extended Support dates, see [Supported MySQL major versions on Amazon RDS](MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar "MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar") and [Release calendar for Amazon RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-release-calendar.md#Release.Calendar "../PostgreSQLReleaseNotes/postgresql-release-calendar.md#Release.Calendar").

###### Topics

- [Overview of Amazon RDS Extended Support](extended-support-overview.md "extended-support-overview.md")
- [Amazon RDS Extended Support charges](extended-support-charges.md "extended-support-charges.md")
- [Versions with Amazon RDS Extended Support](extended-support-versions.md "extended-support-versions.md")
- [Amazon RDS and customer responsibilities with Amazon RDS Extended Support](extended-support-responsibilities.md "extended-support-responsibilities.md")
- [Creating a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support](extended-support-creating-db-instance.md "extended-support-creating-db-instance.md")
- [Viewing the enrollment of your DB instances or Multi-AZ DB clusters in Amazon RDS Extended Support](extended-support-viewing.md "extended-support-viewing.md")
- [Viewing support dates for engine versions in Amazon RDS Extended Support](extended-support-viewing-support-dates.md "extended-support-viewing-support-dates.md")
- [Restoring a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support](extended-support-restoring-db-instance.md "extended-support-restoring-db-instance.md")
