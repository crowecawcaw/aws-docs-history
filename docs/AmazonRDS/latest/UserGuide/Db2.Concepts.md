# Db2 on Amazon RDS versions

For Db2, version numbers take the form of _major.minor.build.revision_, for example, 11.5.9.0.sb00000000.r1. Our version
implementation matches that of Db2.

**major**

The major version number is both the integer and the first fractional part of
the version number, for example, 11.5. A version change is considered major if
the major version number changes—for example, going from version 11.5 to
12.1.

**minor**

The minor version number is both the third and fourth parts of the version
number, for example, 9.0 in 11.5.9.0. The third part indicates the Db2 modpack,
for example, 9 in 9.0. The fourth part indicates the Db2 fixpack, for example, 0
in 9.0. A version change is considered minor if either the Db2 modpack or the
Db2 fixpack changes—for example, going from version 11.5.9.0 to 11.5.9.1,
or from 11.5.9.0 to 11.5.10.0, with exceptions to provide catalog table updates.
(Amazon RDS takes care of these exceptions.)

**build**

The build number is the fifth part of the version number, for example,
sb00000000 in 11.5.9.0.sb00000000. A build number where the number portion is
all zeroes indicates a standard build. A build number where the number portion
isn't all zeroes indicates a special build. A build number changes if there is a
security fix or special build of an existing Db2 version. A build number change
also indicates that Amazon RDS automatically applied a new minor version.

**revision**

The revision number is the sixth part of the version number, for example, r1
in 11.5.9.0.sb00000000.r1. A revision is an Amazon RDS revision to an existing Db2
release. A revision number change indicates that Amazon RDS automatically applied a
new minor version.

###### Topics

- [Upgrade management for Amazon RDS Db2 instances](Db2.Concepts.VersionMgmt.md "Db2.Concepts.VersionMgmt.md")
- [Supported Db2 major versions
  on Amazon RDS](#Db2.Concepts.VersionMgmt.ReleaseCalendar "#Db2.Concepts.VersionMgmt.ReleaseCalendar")

## Supported Db2 major versions

on Amazon RDS

RDS for Db2 major versions are available under standard support at least until
IBM end of support (base) for the corresponding IBM
version. The following table shows the dates that you can use to plan your testing and
upgrade cycles. If Amazon extends support for an RDS for Db2 version for longer than
originally stated, we plan to update this table to reflect the later date.

You can use the following dates to plan your testing and upgrade cycles.

###### Note

Dates with only a month and a year are approximate and are updated with an exact
date when it’s known.

You can view the major versions of your Db2 databases by running the [describe-db-major-engine-versions](../../../cli/latest/reference/rds/describe-db-major-engine-versions.md "../../../cli/latest/reference/rds/describe-db-major-engine-versions.md") AWS CLI command or by using the [DescribeDBMajorEngineVersions](../APIReference/API_DescribeDBMajorEngineVersions.md "../APIReference/API_DescribeDBMajorEngineVersions.md") RDS API operation.

| Db2 major version | IBM release date | RDS release date | IBM end of support (Standard and Advanced<br>Edition) | IBM end of support (extended) |
| ----------------- | ---------------- | ---------------- | ----------------------------------------------------- | ----------------------------- |
| Db2 11.5          | 27 June 2019     | 27 November 2023 | 30 April 2027                                         | 30 April 2031                 |
