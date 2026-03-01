# Versions with Amazon RDS Extended Support

RDS Extended Support is only available for major versions. It isn't
available for minor versions.

RDS Extended Support is available for RDS for MySQL and for RDS for PostgreSQL.
For more information, see [Major versions](MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar "MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.ReleaseCalendar") and [Release calendar for Amazon RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-release-calendar.md "../PostgreSQLReleaseNotes/postgresql-release-calendar.md") in the _Amazon RDS for PostgreSQL
Release Notes_.

You can also view information about support dates for engine versions by using
the AWS CLI or the RDS API. For more information, see [Viewing support dates for engine versions in Amazon RDS Extended Support](extended-support-viewing-support-dates.md "extended-support-viewing-support-dates.md").

## Amazon RDS Extended Support version naming

Amazon RDS will release new minor versions with fixes and CVE patches
for engines on RDS Extended Support. For more information, see [Amazon RDS Extended Support versions for RDS for MySQL](MySQL.Concepts.md#mysql-extended-support-releases "MySQL.Concepts.md#mysql-extended-support-releases") and [Amazon RDS Extended Support updates for RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-extendedsupport.md "../PostgreSQLReleaseNotes/postgresql-extendedsupport.md") in the _Amazon RDS for PostgreSQL
Release Notes_.

The names of these minor releases will be in the form _major.minor-RDS.YYYYMMDD.patch.YYYYMMDD_, for
example, 5.7.44-RDS.20240208.R2.20240210 (for RDS for MySQL) or
11.22-RDS.20240208.R2.20240210 (for RDS for PostgreSQL).

**major**

For MySQL, the major version number is both the integer and the first
fractional part of the version number, for example, 8.0. A major version
upgrade increases the major part of the version number. For example, an
upgrade from 5.7.44 to 8.0.33 is a major version upgrade, where
_5.7_ and _8.0_ are the major version numbers.

For PostgreSQL, the major version number is the integer, for example, 11.

**minor-RDS.YYYYMMDD**

For MySQL, the minor version number is the third part of the version
number, for example, the 44-RDS.20240208 in
5.7.44-RDS.20240208.

For PostgeSQL, the minor version number is the second part of version
number, for example, the 22-RDS.20240208in
11.22-RDS.20240208.

The date is when Amazon RDS created the Amazon RDS minor version.

**patch**

The patch version is what follows the date when Amazon RDS created the
Amazon RDS minor version, for example, the R2 in
5.7.44-RDS.20240208.R2 or
11.22-RDS.20240208.R2.

An Amazon RDS patch version includes important bug fixes added to an Amazon RDS
minor version after its release.

**YYYYMMDD**

The date is when Amazon RDS created the patch version, for example, the
20240210 in 5.7.44-RDS.20240208.R2.20240210 or
11.22-RDS.20240208.R2.20240210.

An Amazon RDS dated version is a security patch that includes important
security fixes added to a minor version after its release. It doesn't
include any fixes that might change an engine's behavior.
