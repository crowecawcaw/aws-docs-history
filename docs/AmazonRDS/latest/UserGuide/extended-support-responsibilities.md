# Amazon RDS and customer

responsibilities with Amazon RDS Extended Support

The following content describes the responsibilities of Amazon RDS and your
responsibilities with RDS Extended Support.

###### Topics

- [Amazon RDS responsibilities](#extended-support-rds-responsibilities "#extended-support-rds-responsibilities")
- [Your
  responsibilities](#extended-support-customer-responsibilities "#extended-support-customer-responsibilities")

## Amazon RDS responsibilities

After the RDS end of standard support date, Amazon RDS will supply
patches, bug fixes, and upgrades for engines that are enrolled in RDS Extended Support. This
will occur for up to 3 years, or until you stop using the engines, whichever happens
first.

The patches will be for Critical and High CVEs as defined by the National
Vulnerability Database (NVD) CVSS severity ratings. For more information, see [Vulnerability Metrics](https://nvd.nist.gov/vuln-metrics/cvss# "https://nvd.nist.gov/vuln-metrics/cvss#").

## Your

responsibilities

You're responsible for applying the patches, bug fixes, and upgrades given for
DB instances or Multi-AZ DB clusters enrolled in RDS Extended Support.
Amazon RDS reserves the right to change, replace, or withdraw such
patches, bug fixes, and upgrades at any time. If a patch is necessary to address
security or critical stability issues, Amazon RDS reserves the right
to update your DB instances or Multi-AZ DB clusters with the patch, or to
require that you install the patch.

You're also responsible for upgrading your engine to a newer engine version
_before_ the RDS end of Extended Support date. The RDS end
of Extended Support date is typically 3 years after the RDS
standard support date. For the RDS end of Extended Support date for
your database major engine version, see [Major versions](MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar "MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar") and
[Release calendar for Amazon RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-release-calendar.md "../PostgreSQLReleaseNotes/postgresql-release-calendar.md").

If you don't upgrade your engine, then after the RDS end of Extended Support date, Amazon RDS will attempt to upgrade your engine to a newer engine
version that's supported under RDS standard support. If the upgrade fails, then
Amazon RDS reserves the right to delete the DB instance or Multi-AZ DB cluster that's running the engine past the RDS end
of standard support date. However, before doing so, Amazon RDS will preserve your
data from that engine.
