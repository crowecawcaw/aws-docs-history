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

- [Supported Db2 minor versions on
  Amazon RDS](#Db2.Concepts.VersionMgmt.Supported "#Db2.Concepts.VersionMgmt.Supported")
- [Supported Db2 major versions
  on Amazon RDS](#Db2.Concepts.VersionMgmt.ReleaseCalendar "#Db2.Concepts.VersionMgmt.ReleaseCalendar")

## Supported Db2 minor versions on

Amazon RDS

The following table shows the minor versions of Db2 11.5 that Amazon RDS currently
supports.

###### Note

Dates with only a month and a year are approximate and are updated with an exact
date when it’s known.

| Db2 engine version | IBM release date | RDS release date |
| ------------------ | ---------------- | ---------------- |
| 11.5.9.0           | 15 November 2023 | 27 November 2023 |

You can specify any currently supported Db2 version when creating a new DB instance.
You can specify the major version (such as Db2 11.5) and any supported minor version for
the specified major version. If no version is specified, Amazon RDS defaults to a supported
version, typically the most recent version. If a major version is specified but a minor
version is not, Amazon RDS defaults to a recent release of the major version that you have
specified. To see a list of supported versions, as well as defaults for newly created DB
instances, use the [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS Command Line Interface (AWS CLI) command.

For example, to list the supported engine versions for Amazon RDS for Db2, run the following
AWS CLI command. Replace `region` with your AWS Region.

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
    --filters Name=engine,Values=db2-ae,db2-se \
    --query "DBEngineVersions[].{Engine:Engine, EngineVersion:EngineVersion, DBParameterGroupFamily:DBParameterGroupFamily}" \
    --region `region`
```

For Windows:

```
aws rds describe-db-engine-versions ^
    --filters Name=engine,Values=db2-ae,db2-se ^
    --query "DBEngineVersions[].{Engine:Engine, EngineVersion:EngineVersion, DBParameterGroupFamily:DBParameterGroupFamily}" ^
    --region `region`
```

This command produces output similar to the following example:

```
[
    {
    "Engine": "db2-ae",
    "EngineVersion": "11.5.9.0.sb00000000.r1",
    "DBParameterGroupFamily": "db2-ae-11.5"
    },
    {
    "Engine": "db2-se",
    "EngineVersion": "11.5.9.0.sb00000000.r1",
    "DBParameterGroupFamily": "db2-se-11.5"
    }
]
```

The default Db2 version might vary by AWS Region. To create a DB instance with a
specific minor version, specify the minor version during DB instance creation. You can
determine the default version for an AWS Region for `db2-ae` and
`db2-se` database engines by running the`describe-db-engine-versions` command. The following example returns the
default version for `db2-ae` in US East (N. Virginia).

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
    --default-only --engine `db2-ae` \
    --query "DBEngineVersions[].{Engine:Engine, EngineVersion:EngineVersion, DBParameterGroupFamily:DBParameterGroupFamily}" \
    --region `us-east-1`
```

For Windows:

```
aws rds describe-db-engine-versions ^
    --default-only --engine `db2-ae` ^
    --query "DBEngineVersions[].{Engine:Engine, EngineVersion:EngineVersion, DBParameterGroupFamily:DBParameterGroupFamily}" ^
    --region `us-east-1`
```

This command produces output similar to the following example:

```
[
    {
    "Engine": "db2-ae",
    "EngineVersion": "11.5.9.0.sb00000000.r1",
    "DBParameterGroupFamily": "db2-ae-11.5"
    }
]
```

With Amazon RDS, you control when to upgrade your Db2 instance to a new major version
supported by Amazon RDS. You can maintain compatibility with specific Db2 versions, test new
versions with your application before deploying in production, and perform major version
upgrades at times that best fit your schedule.

When automatic minor version upgrade is enabled, Amazon RDS automatically upgrades your DB
instances to new Db2 minor versions as they are supported by Amazon RDS. This patching occurs
during your scheduled maintenance window. You can modify a DB instance to enable or
disable automatic minor version upgrades.

Except for Db2 versions 11.5.9.1 and 11.5.10.0, automatic upgrades to new Db2 minor
version includes automatic upgrades to new builds and revisions. For 11.5.9.1 and
11.5.10.0, manually upgrade minor versions.

If you opt out of automatically scheduled upgrades, you can manually upgrade to a
supported minor version release by following the same procedure as you would for a major
version update. For information, see [Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

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
