# MySQL on Amazon RDS versions

For MySQL, version numbers are organized as version = X.Y.Z. In Amazon RDS terminology, X.Y
denotes the major version, and Z is the minor version number. For Amazon RDS implementations, a
version change is considered major if the major version number changes—for example,
going from version 5.7 to 8.0. A version change is considered minor if only the minor
version number changes—for example, going from version 8.0.32 to 8.0.34.

###### Topics

- [Supported MySQL minor versions on
  Amazon RDS](#MySQL.Concepts.VersionMgmt.Supported "#MySQL.Concepts.VersionMgmt.Supported")
- [Supported MySQL major
  versions on Amazon RDS](#MySQL.Concepts.VersionMgmt.ReleaseCalendar "#MySQL.Concepts.VersionMgmt.ReleaseCalendar")
- [Amazon RDS Extended Support versions for
  RDS for MySQL](#mysql-extended-support-releases "#mysql-extended-support-releases")
- [Working with the
  Database Preview environment](#mysql-working-with-the-database-preview-environment "#mysql-working-with-the-database-preview-environment")
- [MySQL version 9.5 in the Database Preview environment](#mysql-preview-environment-version-9-5 "#mysql-preview-environment-version-9-5")
- [MySQL version 9.4 in the Database Preview environment](#mysql-preview-environment-version-9-4 "#mysql-preview-environment-version-9-4")
- [MySQL version 9.3 in the Database Preview environment](#mysql-preview-environment-version-9-3 "#mysql-preview-environment-version-9-3")
- [Deprecated versions for
  Amazon RDS for MySQL](#MySQL.Concepts.DeprecatedVersions "#MySQL.Concepts.DeprecatedVersions")

## Supported MySQL minor versions on

Amazon RDS

Amazon RDS currently supports the following minor versions of MySQL.

###### Note

Amazon RDS Extended Support isn't available for minor versions.

The following table shows the minor versions of MySQL 8.4 that Amazon RDS currently
supports.

| MySQL engine version | Community release date | RDS release date | RDS end of standard support date |
| -------------------- | ---------------------- | ---------------- | -------------------------------- |
| 8.4.7                | 21 October 2025        | 13 November 2025 | 30 November 2026                 |
| 8.4.6                | 22 July 2025           | 1 August 2025    | 30 September 2026                |
| 8.4.5                | 15 April 2025          | 29 April 2025    | 30 September 2026                |
| 8.4.4                | 21 January 2025        | 19 February 2025 | 31 March 2026                    |
| 8.4.3                | 15 October 2024        | 21 November 2024 | 31 March 2026                    |

The following table shows the minor versions of MySQL 8.0 that Amazon RDS currently supports.

###### Note

Minor versions can reach end of standard support before major versions do. For
example, minor version 8.0.28 reached its end of standard support date on March 28, 2024
while major version 8.0 reaches this date on July 31, 2026. RDS will support
additional 8.0.\* minor versions that the MySQL community releases between these
dates. We recommend that you upgrade to the latest available minor version as often as possible for all major versions.

| MySQL engine version | Community release date | RDS release date | RDS end of standard support date |
| -------------------- | ---------------------- | ---------------- | -------------------------------- |
| 8.0.44               | 21 October 2025        | 13 November 2025 | 31 July 2026                     |
| 8.0.43               | 22 July 2025           | 1 August 2025    | 31 July 2026                     |
| 8.0.42               | 15 April 2025          | 29 April 2025    | 31 July 2026                     |
| 8.0.41               | 21 January 2025        | 19 February 2025 | 31 March 2026                    |
| 8.0.40               | 15 October 2024        | 13 November 2024 | 31 March 2026                    |

The following table shows the minor versions of MySQL 5.7 that are available under
Amazon RDS Extended Support.

###### Note

Minor versions can reach end of Extended Support before major versions do. For
example, minor version 5.7.44-RDS.20240529 reaches its end of Extended Support date in September 2025
while major version 5.7 reaches this date on February 28, 2027. RDS will generate and release additional
5.7.44-RDS.xxyyzz minor versions between these dates. We recommend that you upgrade to
the latest available minor version as often as possible for all major versions.

| MySQL engine version  | Community release date | RDS release date  | RDS end of Extended Support date |
| --------------------- | ---------------------- | ----------------- | -------------------------------- |
| 5.7.44-RDS.20251212\* | Not applicable         | 12 December 2025  | 30 December 2026                 |
| 5.7.44-RDS.20250818\* | Not applicable         | 15 September 2025 | 30 September 2026                |
| 5.7.44-RDS.20250508\* | Not applicable         | 20 May 2025       | 30 September 2026                |
| 5.7.44-RDS.20250213\* | Not applicable         | 12 March 2025     | 30 September 2026                |
| 5.7.44-RDS.20250103\* | Not applicable         | 13 February 2025  | 31 March 2026                    |

\* MySQL Community retired major version 5.7 and won't be releasing new minor
versions. This is a minor version that Amazon RDS released with critical security patches and
bug fixes for MySQL 5.7 databases that are covered under RDS Extended Support. For more
information about these minor versions, see [Amazon RDS Extended Support versions for
RDS for MySQL](#mysql-extended-support-releases "#mysql-extended-support-releases"). For more information about RDS Extended Support,
see [Amazon RDS Extended Support with Amazon RDS](extended-support.md "extended-support.md").

You can specify any currently supported MySQL version when creating a new DB instance.
You can specify the major version (such as MySQL 5.7), and any supported minor version
for the specified major version. If no version is specified, Amazon RDS defaults to a
supported version, typically the most recent version. If a major version is specified
but a minor version is not, Amazon RDS defaults to a recent release of the major version you
have specified. To see a list of supported versions, as well as defaults for newly
created DB instances, run the [`describe-db-engine-versions`](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS CLI command.

For example, to list the supported engine versions for RDS for MySQL, run the following
CLI command:

```
aws rds describe-db-engine-versions --engine mysql --query "*[].{Engine:Engine,EngineVersion:EngineVersion}" --output text
```

The default MySQL version might vary by AWS Region. To create a DB instance with a
specific minor version, specify the minor version during DB instance creation. You can
determine the default minor version for an AWS Region by running the following AWS CLI
command:

```
aws rds describe-db-engine-versions --default-only --engine mysql --engine-version `major_engine_version` --region `region` --query "*[].{Engine:Engine,EngineVersion:EngineVersion}" --output text
```

Replace `major_engine_version` with the major engine version,
and replace `region` with the AWS Region. For example, the
following AWS CLI command returns the default MySQL minor engine version for the 5.7 major
version and the US West (Oregon) AWS Region (us-west-2):

```
aws rds describe-db-engine-versions --default-only --engine mysql --engine-version 5.7 --region us-west-2 --query "*[].{Engine:Engine,EngineVersion:EngineVersion}" --output text
```

With Amazon RDS, you control when to upgrade your MySQL instance to a new major version
supported by Amazon RDS. You can maintain compatibility with specific MySQL versions, test
new versions with your application before deploying in production, and perform major
version upgrades at times that best fit your schedule.

When automatic minor version upgrade is enabled, your DB instance will be upgraded
automatically to new MySQL minor versions as they are supported by Amazon RDS. This patching
occurs during your scheduled maintenance window. You can modify a DB instance to enable
or disable automatic minor version upgrades.

If you opt out of automatically scheduled upgrades, you can manually upgrade to a
supported minor version release by following the same procedure as you would for a major
version update. For information, see [Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

Amazon RDS currently supports the following upgrades for major versions of the MySQL
database engine:

- MySQL 5.7 to MySQL 8.0
- MySQL 8.0 to MySQL 8.4

Because major version upgrades involve some compatibility risk, they do not occur
automatically; you must make a request to modify the DB instance. You should thoroughly
test any upgrade before upgrading your production instances. For information about
upgrading a MySQL DB instance, see [Upgrades of the RDS for MySQL DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

You can test a DB instance against a new version before upgrading by creating a DB
snapshot of your existing DB instance, restoring from the DB snapshot to create a new DB
instance, and then initiating a version upgrade for the new DB instance. You can then
experiment safely on the upgraded clone of your DB instance before deciding whether or
not to upgrade your original DB instance.

### MySQL minor versions on

Amazon RDS

For the changes that the MySQL community made to the minor versions, see [Critical Patch Updates, Security
Alerts and Bulletins](https://www.oracle.com/security-alerts/ "https://www.oracle.com/security-alerts/") on the Oracle website. Under **Critical Patch Update**, choose the month when Oracle released the
minor version. And then choose the MySQL minor version under **Affected Products and Versions**.

###### Minor versions

- [MySQL version
  8.4.7](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.4.7 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.4.7")
- [MySQL version
  8.4.6](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.4.6 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.4.6")
- [MySQL version
  8.4.5](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.4.5 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.4.5")
- [MySQL version
  8.4.4](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.4.4 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.4.4")
- [MySQL
  version 8.0.44](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.44 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.44")
- [MySQL
  version 8.0.43](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.43 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.43")
- [MySQL
  version 8.0.42](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.42 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.42")
- [MySQL
  version 8.0.41](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.41 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.41")
- [MySQL
  version 8.0.40](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.40 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.40")
- [MySQL
  version 8.0.39](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.39 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.39")
- [MySQL
  version 8.0.37](#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.37 "#MySQL.Concepts.VersionMgmt.Supported.Minor.8.0.37")

#### MySQL version

8.4.7

MySQL version 8.4.7 is now available on Amazon RDS. This release contains fixes and
improvements added by the MySQL community and Amazon RDS.

#### MySQL version

8.4.6

MySQL version 8.4.6 is now available on Amazon RDS. This release contains fixes and
improvements added by the MySQL community and Amazon RDS.

#### MySQL version

8.4.5

MySQL version 8.4.5 is now available on Amazon RDS. This release contains fixes and
improvements added by the MySQL community and Amazon RDS.

**New features and enhancements**

- Updated the time zone information to base it on
  `tzdata2025b`.

#### MySQL version

8.4.4

MySQL version 8.4.4 is now available on Amazon RDS. This release contains fixes and
improvements added by the MySQL community and Amazon RDS.

**New features and enhancements**

- Updated the time zone information to base it on
  `tzdata2025a`.
- Fixed a bug that caused a collation error while executing the Amazon RDS
  stored procedures `mysql.rds_set_configuration` and
  `mysql.rds_kill`.

#### MySQL

version 8.0.44

MySQL version 8.0.44 is now available on Amazon RDS. This release contains fixes
and improvements added by the MySQL community and Amazon RDS.

#### MySQL

version 8.0.43

MySQL version 8.0.43 is now available on Amazon RDS. This release contains fixes
and improvements added by the MySQL community and Amazon RDS.

#### MySQL

version 8.0.42

MySQL version 8.0.42 is now available on Amazon RDS. This release contains fixes
and improvements added by the MySQL community and Amazon RDS.

**New features and enhancements**

- Updated the time zone information to base it on
  `tzdata2025b`.

#### MySQL

version 8.0.41

MySQL version 8.0.41 is now available on Amazon RDS. This release contains fixes
and improvements added by the MySQL community and Amazon RDS.

**New features and enhancements**

- Updated the time zone information to base it on
  `tzdata2025a`.
- Fixed a bug that caused a collation error while executing the Amazon RDS
  stored procedures `mysql.rds_set_configuration` and
  `mysql.rds_kill`.

#### MySQL

version 8.0.40

MySQL version 8.0.40 is now available on Amazon RDS. This release contains fixes
and improvements added by the MySQL community and Amazon RDS.

**New features and enhancements**

- Fixed a bug that caused character set mismatch failures during
  database upgrades.

#### MySQL

version 8.0.39

MySQL version 8.0.39 is now available on Amazon RDS. This release contains fixes
and improvements added by the MySQL community and Amazon RDS.

**New features and enhancements**

- Fixed a bug that prevented `sql_log_off` from working
  properly with the `SESSION_VARIABLES_ADMIN` privilege.
- Fixed a bug that prevented the master user from being able to grant
  the `SESSION_VARIABLE_ADMIN` privilege other database
  users.
- Fixed a bug that caused an illegal mix of collation while executing
  RDS-provided stored procedures.

#### MySQL

version 8.0.37

MySQL version 8.0.37 is now available on Amazon RDS. This release contains fixes
and improvements added by the MySQL community and Amazon RDS.

**New features and enhancements**

- Fixed a bug with executing an instant DDL statement followed by an
  UPDATE that lead to an assertion failure.

## Supported MySQL major

versions on Amazon RDS

RDS for MySQL major versions are available under standard support at least until
community end of life for the corresponding community version. You can continue running
a major version past its RDS end of standard support date for a fee. For more
information, see [Amazon RDS Extended Support with Amazon RDS](extended-support.md "extended-support.md") and
[Amazon RDS for MySQL pricing](https://aws.amazon.com/rds/mysql/pricing/ "https://aws.amazon.com/rds/mysql/pricing/").

You can use the following dates to plan your testing and upgrade cycles.

###### Note

You can also view information about support dates for major engine versions by
using the AWS CLI or the RDS API. For more
information, see [Viewing support dates for engine
versions in Amazon RDS Extended Support](extended-support-viewing-support-dates.md "extended-support-viewing-support-dates.md").

| MySQL major version | Community release date | RDS release date | Community end of life date | RDS end of standard support date | RDS start of Extended Support year 1 pricing date | RDS start of Extended Support year 3 pricing date | RDS end of Extended Support date |
| ------------------- | ---------------------- | ---------------- | -------------------------- | -------------------------------- | ------------------------------------------------- | ------------------------------------------------- | -------------------------------- |
| MySQL 8.4           | 30 April 2024          | 21 November 2024 | 30 April 2029              | 31 July 2029                     | 1 August, 2029                                    | 1 August 2031                                     | 31 July 2032                     |
| MySQL 8.0           | 19 April 2018          | 23 October 2018  | 30 April 2026              | 31 July 2026                     | 1 August 2026                                     | 1 August 2028                                     | 31 July 2029                     |
| MySQL 5.7\*         | 21 October 2015        | 22 February 2016 | 31 October 2023            | 29 February 2024                 | 1 March 2024                                      | 1 March 2026                                      | 28 February 2027                 |

\* MySQL 5.7 is now only available under RDS Extended Support. For more information, see [Amazon RDS Extended Support with Amazon RDS](extended-support.md "extended-support.md").

## Amazon RDS Extended Support versions for

RDS for MySQL

The following content lists all releases of RDS Extended Support for RDS for MySQL versions.

###### Releases

- [RDS Extended Support
  for RDS for MySQL version 5.7.44-RDS.20251212](#mysql-extended-support-releases-version-5.7.44-RDS.20251212 "#mysql-extended-support-releases-version-5.7.44-RDS.20251212")
- [RDS Extended Support
  for RDS for MySQL version 5.7.44-RDS.20250818](#mysql-extended-support-releases-version-5.7.44-RDS.20250818 "#mysql-extended-support-releases-version-5.7.44-RDS.20250818")
- [RDS Extended Support
  for RDS for MySQL version 5.7.44-RDS.20250508](#mysql-extended-support-releases-version-5.7.44-20250508 "#mysql-extended-support-releases-version-5.7.44-20250508")
- [RDS Extended Support
  for RDS for MySQL version 5.7.44-RDS.20250213](#mysql-extended-support-releases-version-5.7.44-20250213 "#mysql-extended-support-releases-version-5.7.44-20250213")
- [RDS Extended Support
  for RDS for MySQL version 5.7.44-RDS.20250103](#mysql-extended-support-releases-version-5.7.44-20250103 "#mysql-extended-support-releases-version-5.7.44-20250103")
- [RDS Extended Support
  for RDS for MySQL version 5.7.44-RDS.20240808](#mysql-extended-support-releases-version-5.7.44-20240808 "#mysql-extended-support-releases-version-5.7.44-20240808")
- [RDS Extended Support
  for RDS for MySQL version 5.7.44-RDS.20240529](#mysql-extended-support-releases-version-5.7.44-20240529 "#mysql-extended-support-releases-version-5.7.44-20240529")
- [RDS Extended Support
  for RDS for MySQL version 5.7.44-RDS.20240408](#mysql-extended-support-releases-version-5.7.44-20240408 "#mysql-extended-support-releases-version-5.7.44-20240408")

### RDS Extended Support

for RDS for MySQL version 5.7.44-RDS.20251212

RDS Extended Support for RDS for MySQL version 5.7.44-RDS.20251212 is available.

**Bugs fixed:**

- Fixed an issue with server startup when the buffer pool size exceeded the upper limit.
- Fixed read from `INFORMATION_SCHEMA.INNODB_LOCKS` that caused the server to exit abnormally.
- Fixed an issue with JUnit reporting support in MySQL Test Run (MTR).
- Fixed compilation issues when building with `-DWITH_INNODB_MEMCACHED=ON` option.
- Fixed an issue with MySQL Test Run (MTR) execution for bug 25182306.

**CVEs fixed:**

- [CVE-2025-53054](https://nvd.nist.gov/vuln/detail/CVE-2025-53054 "https://nvd.nist.gov/vuln/detail/CVE-2025-53054")
- [CVE-2025-53044](https://nvd.nist.gov/vuln/detail/CVE-2025-53044 "https://nvd.nist.gov/vuln/detail/CVE-2025-53044")
- [CVE-2025-53045](https://nvd.nist.gov/vuln/detail/CVE-2025-53045 "https://nvd.nist.gov/vuln/detail/CVE-2025-53045")
- [CVE-2025-53062](https://nvd.nist.gov/vuln/detail/CVE-2025-53062 "https://nvd.nist.gov/vuln/detail/CVE-2025-53062")
- [CVE-2025-53040](https://nvd.nist.gov/vuln/detail/CVE-2025-53040 "https://nvd.nist.gov/vuln/detail/CVE-2025-53040")
- [CVE-2025-53042](https://nvd.nist.gov/vuln/detail/CVE-2025-53042 "https://nvd.nist.gov/vuln/detail/CVE-2025-53042")
- [CVE-2025-53067](https://nvd.nist.gov/vuln/detail/CVE-2025-53067 "https://nvd.nist.gov/vuln/detail/CVE-2025-53067")

### RDS Extended Support

for RDS for MySQL version 5.7.44-RDS.20250818

RDS Extended Support for RDS for MySQL version 5.7.44-RDS.20250818 is available.

**Bugs fixed:**

- Fixed an issue where the query rewrite plugin failed when the server operated with `autocommit=OFF`.
- Fixed a permission issue that prevented Debian and Ubuntu builds from running in rootless mode.
- Fixed missing update for bug 30875669.

**CVEs fixed:**

- [CVE-2025-50082](https://nvd.nist.gov/vuln/detail/CVE-2025-50082 "https://nvd.nist.gov/vuln/detail/CVE-2025-50082")
- [CVE-2025-50083](https://nvd.nist.gov/vuln/detail/CVE-2025-50083 "https://nvd.nist.gov/vuln/detail/CVE-2025-50083")
- [CVE-2025-50079](https://nvd.nist.gov/vuln/detail/CVE-2025-50079 "https://nvd.nist.gov/vuln/detail/CVE-2025-50079")
- [CVE-2025-50084](https://nvd.nist.gov/vuln/detail/CVE-2025-50084 "https://nvd.nist.gov/vuln/detail/CVE-2025-50084")
- [CVE-2025-50087](https://nvd.nist.gov/vuln/detail/CVE-2025-50087 "https://nvd.nist.gov/vuln/detail/CVE-2025-50087")
- [CVE-2025-50091](https://nvd.nist.gov/vuln/detail/CVE-2025-50091 "https://nvd.nist.gov/vuln/detail/CVE-2025-50091")
- [CVE-2025-50101](https://nvd.nist.gov/vuln/detail/CVE-2025-50101 "https://nvd.nist.gov/vuln/detail/CVE-2025-50101")
- [CVE-2025-50102](https://nvd.nist.gov/vuln/detail/CVE-2025-50102 "https://nvd.nist.gov/vuln/detail/CVE-2025-50102")
- [CVE-2025-50098](https://nvd.nist.gov/vuln/detail/CVE-2025-50098 "https://nvd.nist.gov/vuln/detail/CVE-2025-50098")
- [CVE-2025-53023](hhttps://nvd.nist.gov/vuln/detail/CVE-2025-53023 "hhttps://nvd.nist.gov/vuln/detail/CVE-2025-53023")
- [CVE-2025-50081](https://nvd.nist.gov/vuln/detail/CVE-2025-50081 "https://nvd.nist.gov/vuln/detail/CVE-2025-50081")
- [CVE-2025-50085](https://nvd.nist.gov/vuln/detail/CVE-2025-50085 "https://nvd.nist.gov/vuln/detail/CVE-2025-50085")
- [CVE-2025-50077](https://nvd.nist.gov/vuln/detail/CVE-2025-50077 "https://nvd.nist.gov/vuln/detail/CVE-2025-50077")
- [CVE-2025-50088](https://nvd.nist.gov/vuln/detail/CVE-2025-50088 "https://nvd.nist.gov/vuln/detail/CVE-2025-50088")
- [CVE-2025-50092](https://nvd.nist.gov/vuln/detail/CVE-2025-50092 "https://nvd.nist.gov/vuln/detail/CVE-2025-50092")
- [CVE-2025-50099](https://nvd.nist.gov/vuln/detail/CVE-2025-50099 "https://nvd.nist.gov/vuln/detail/CVE-2025-50099")
- [CVE-2025-50096](https://nvd.nist.gov/vuln/detail/CVE-2025-50096 "https://nvd.nist.gov/vuln/detail/CVE-2025-50096")

### RDS Extended Support

for RDS for MySQL version 5.7.44-RDS.20250508

RDS Extended Support for RDS for MySQL version 5.7.44-RDS.20250508 is available.

**Bugs fixed:**

- Fixed virtual index unstable after rollback when `index_id` is greater than max `uint32`.
- Fixed Tests fails with memory issue.
- Fixed `<COMMAND_CLASS>` is empty for `<NAME>Execute</NAME>`.
- Fixed Compile MySQL with GCC 14 [noclose 5.7].

**CVEs fixed:**

- [CVE-2025-30682](https://nvd.nist.gov/vuln/detail/CVE-2025-30682 "https://nvd.nist.gov/vuln/detail/CVE-2025-30682")
- [CVE-2025-30687](https://nvd.nist.gov/vuln/detail/CVE-2025-30687 "https://nvd.nist.gov/vuln/detail/CVE-2025-30687")
- [CVE-2025-30688](https://nvd.nist.gov/vuln/detail/CVE-2025-30688 "https://nvd.nist.gov/vuln/detail/CVE-2025-30688")
- [CVE-2025-21581](https://nvd.nist.gov/vuln/detail/CVE-2025-21581 "https://nvd.nist.gov/vuln/detail/CVE-2025-21581")
- [CVE-2025-21585](https://nvd.nist.gov/vuln/detail/CVE-2025-21585 "https://nvd.nist.gov/vuln/detail/CVE-2025-21585")
- [CVE-2025-30689](https://nvd.nist.gov/vuln/detail/CVE-2025-30689 "https://nvd.nist.gov/vuln/detail/CVE-2025-30689")
- [CVE-2025-30722](https://nvd.nist.gov/vuln/detail/CVE-2025-30722 "https://nvd.nist.gov/vuln/detail/CVE-2025-30722")
- [CVE-2025-21577](https://nvd.nist.gov/vuln/detail/CVE-2025-21577 "https://nvd.nist.gov/vuln/detail/CVE-2025-21577")
- [CVE-2025-30693](https://nvd.nist.gov/vuln/detail/CVE-2025-30693 "https://nvd.nist.gov/vuln/detail/CVE-2025-30693")
- [CVE-2025-30695](https://nvd.nist.gov/vuln/detail/CVE-2025-30695 "https://nvd.nist.gov/vuln/detail/CVE-2025-30695")
- [CVE-2025-30703](https://nvd.nist.gov/vuln/detail/CVE-2025-30703 "https://nvd.nist.gov/vuln/detail/CVE-2025-30703")

### RDS Extended Support

for RDS for MySQL version 5.7.44-RDS.20250213

RDS Extended Support for RDS for MySQL version 5.7.44-RDS.20250213 is available.

**Bugs fixed:**

- Fixed InnoDB failing assertion `result != FTS_INVALID`.
- Fixed crashing and widespread corruption of spatial indexes after `ALTER
TABLE` operation rebuilds InnoDB table using the `INPLACE`
  algorithm.
- Fixed `ON DELETE CASCADE` with generated column crashes in
  `innobase_get_computed_value`.
- Fixed assertion failure in `row_MySQL_pad_col`.
- Fixed an issue where online DDL causes the following error: `ERROR 1712
(HY000): Index PRIMARY is corrupted`.
- Fixed crashes at `Item_rollup_sum_switcher::current_arg`.
- Fixed an issue where the database cache is not flushed on `DROP
USER`.
- Fixed buffer overrun in `my_print_help`.
- Fixed an InnoDB issue where `FULLTEXT` index limits
  `FTS_DOC_ID` to max unsigned 32-bit value.

**CVEs fixed:**

- [CVE-2025-21497](https://nvd.nist.gov/vuln/detail/CVE-2025-21497 "https://nvd.nist.gov/vuln/detail/CVE-2025-21497")
- [CVE-2025-21555](https://nvd.nist.gov/vuln/detail/CVE-2025-21555 "https://nvd.nist.gov/vuln/detail/CVE-2025-21555")
- [CVE-2025-21559](https://nvd.nist.gov/vuln/detail/CVE-2025-21559 "https://nvd.nist.gov/vuln/detail/CVE-2025-21559")
- [CVE-2025-21490](https://nvd.nist.gov/vuln/detail/CVE-2025-21490 "https://nvd.nist.gov/vuln/detail/CVE-2025-21490")
- [CVE-2025-21491](https://nvd.nist.gov/vuln/detail/CVE-2025-21491 "https://nvd.nist.gov/vuln/detail/CVE-2025-21491")
- [CVE-2025-21500](https://nvd.nist.gov/vuln/detail/CVE-2025-21500 "https://nvd.nist.gov/vuln/detail/CVE-2025-21500")
- [CVE-2025-21501](https://nvd.nist.gov/vuln/detail/CVE-2025-21501 "https://nvd.nist.gov/vuln/detail/CVE-2025-21501")
- [CVE-2025-21540](https://nvd.nist.gov/vuln/detail/CVE-2025-21540 "https://nvd.nist.gov/vuln/detail/CVE-2025-21540")
- [CVE-2025-21543](https://nvd.nist.gov/vuln/detail/CVE-2025-21543 "https://nvd.nist.gov/vuln/detail/CVE-2025-21543")
- [CVE-2025-21520](https://nvd.nist.gov/vuln/detail/CVE-2025-21520 "https://nvd.nist.gov/vuln/detail/CVE-2025-21520")

### RDS Extended Support

for RDS for MySQL version 5.7.44-RDS.20250103

RDS Extended Support for RDS for MySQL version 5.7.44-RDS.20250103 is available.

**Bugs fixed:**

- Fixed FTS clean-up issue when dropping and adding a `FULLTEXT`
  index in the same transaction.
- Optimized the memory allocation timing in the MySQL client to prevent any
  potential leaks.
- Fixed the truncation of results at 34 bytes when using the `UNION`
  operator.
- Fixed potential out-of-bounds access due to `ulong bitmask` in the
  authorization code.

**CVEs fixed:**

- [CVE-2024-21230](https://nvd.nist.gov/vuln/detail/CVE-2024-21230 "https://nvd.nist.gov/vuln/detail/CVE-2024-21230")
- [CVE-2024-21201](https://nvd.nist.gov/vuln/detail/CVE-2024-21201 "https://nvd.nist.gov/vuln/detail/CVE-2024-21201")
- [CVE-2024-21241](https://nvd.nist.gov/vuln/detail/CVE-2024-21241 "https://nvd.nist.gov/vuln/detail/CVE-2024-21241")
- [CVE-2024-21203](https://nvd.nist.gov/vuln/detail/CVE-2024-21203 "https://nvd.nist.gov/vuln/detail/CVE-2024-21203")

### RDS Extended Support

for RDS for MySQL version 5.7.44-RDS.20240808

RDS Extended Support for RDS for MySQL version 5.7.44-RDS.20240808 is available.

**Bugs fixed:**

- Fixed assertion failure related to dictionary column index.
- Fixed issue with the `is_binlog_cache_empty()` function.
- Fixed `heap-use-after-free` errors in `sql/item.cc`
  files.
- Fixed several spatial index issues by disabling them for
  `index-only` reads.
- Fixed instrumentation issue with the `LOCK_ORDER:
CONNECTION_CONTROL` plugin.
- Fixed threads getting stuck with the `CONNECTION_CONTROL`
  plugin.
- Fixed `PSI_THREAD_INFO` not updating for `PREPARED
STATEMENTS`.
- Fixed double processing of FTS index words with
  `innodb_optimize_fulltext_only`.

**CVEs fixed:**

- [CVE-2024-21177](https://nvd.nist.gov/vuln/detail/CVE-2024-21177 "https://nvd.nist.gov/vuln/detail/CVE-2024-21177")

### RDS Extended Support

for RDS for MySQL version 5.7.44-RDS.20240529

RDS Extended Support for RDS for MySQL version 5.7.44-RDS.20240529 is available.

**Bugs fixed:**

- Fixed `field.cc` assertion failure by implementing
  `fix_after_pullout`.
- Fixed a null pointer failure when returning metadata to the client for certain
  SQL queries. These queries contained dynamic parameters and subqueries in
  `SELECT` clauses.
- Fixed incorrect results when using `GROUP BY` for loose index
  scans, or scans of noncontiguous ranges of an index.
- Fixed loss of GTID information on MySQL crash during persistence.
- Fixed a race condition that could cause an InnoDB transaction to hang
  indefinitely.
- Fixed a race condition in Group Replication's certification information
  cleanup.
- Fixed backward index scan issue with concurrent page operations.
- Fixed an inconsistent full-text search (FTS) state issue in concurrent
  scenarios.
- Fixed assertion issue with change buffer on deleting tables.
- Unified behavior for calling `deinit` function across all plugin
  types.

**CVEs fixed:**

- [CVE-2024-20963](https://nvd.nist.gov/vuln/detail/CVE-2024-20963 "https://nvd.nist.gov/vuln/detail/CVE-2024-20963")
- [CVE-2024-20993](https://nvd.nist.gov/vuln/detail/CVE-2024-20993 "https://nvd.nist.gov/vuln/detail/CVE-2024-20993")
- [CVE-2024-20998](https://nvd.nist.gov/vuln/detail/CVE-2024-20998 "https://nvd.nist.gov/vuln/detail/CVE-2024-20998")
- [CVE-2024-21009](https://nvd.nist.gov/vuln/detail/CVE-2024-21009 "https://nvd.nist.gov/vuln/detail/CVE-2024-21009")
- [CVE-2024-21054](https://nvd.nist.gov/vuln/detail/CVE-2024-21054 "https://nvd.nist.gov/vuln/detail/CVE-2024-21054")
- [CVE-2024-21055](https://nvd.nist.gov/vuln/detail/CVE-2024-21055 "https://nvd.nist.gov/vuln/detail/CVE-2024-21055")
- [CVE-2024-21057](https://nvd.nist.gov/vuln/detail/CVE-2024-21057 "https://nvd.nist.gov/vuln/detail/CVE-2024-21057")
- [CVE-2024-21062](https://nvd.nist.gov/vuln/detail/CVE-2024-21062 "https://nvd.nist.gov/vuln/detail/CVE-2024-21062")
- [CVE-2024-21008](https://nvd.nist.gov/vuln/detail/CVE-2024-21008 "https://nvd.nist.gov/vuln/detail/CVE-2024-21008")
- [CVE-2024-21013](https://nvd.nist.gov/vuln/detail/CVE-2024-21013 "https://nvd.nist.gov/vuln/detail/CVE-2024-21013")
- [CVE-2024-21047](https://nvd.nist.gov/vuln/detail/CVE-2024-21047 "https://nvd.nist.gov/vuln/detail/CVE-2024-21047")
- [CVE-2024-21087](https://nvd.nist.gov/vuln/detail/CVE-2024-21087 "https://nvd.nist.gov/vuln/detail/CVE-2024-21087")
- [CVE-2024-21096](https://nvd.nist.gov/vuln/detail/CVE-2024-21096 "https://nvd.nist.gov/vuln/detail/CVE-2024-21096")

### RDS Extended Support

for RDS for MySQL version 5.7.44-RDS.20240408

RDS Extended Support for RDS for MySQL version 5.7.44-RDS.20240408 is available.

This release contains patches for the following CVEs:

- [CVE-2024-20963](https://nvd.nist.gov/vuln/detail/CVE-2024-20963 "https://nvd.nist.gov/vuln/detail/CVE-2024-20963")

## Working with the

Database Preview environment

In July 2023, Oracle announced a new release model for MySQL. This model includes two
types of releases: Innovation Releases and LTS releases. Amazon RDS makes MySQL Innovation
Releases available in the RDS Preview environment. To learn more about the MySQL
Innovation releases, see [Introducing MySQL Innovation and Long-Term Support (LTS) versions](https://blogs.oracle.com/mysql/post/introducing-mysql-innovation-and-longterm-support-lts-versions "https://blogs.oracle.com/mysql/post/introducing-mysql-innovation-and-longterm-support-lts-versions").

RDS for MySQL DB instances in the Database Preview environment are functionally similar
to other RDS for MySQL DB instances. However, you can't use the Database Preview
environment for production workloads.

Preview environments have the following limitations:

- Amazon RDS deletes all DB instances 60 days after you create them, along with any
  backups and snapshots.
- You can only use General Purpose SSD and Provisioned IOPS SSD storage.
- You can't get help from Support with DB instances. Instead, you can post your questions to the AWS‐managed Q&A
  community, [AWS re:Post](https://repost.aws/tags/TAsibBK6ZeQYihN9as4S_psg/amazon-relational-database-service "https://repost.aws/tags/TAsibBK6ZeQYihN9as4S_psg/amazon-relational-database-service").
- You can't copy a snapshot of a DB instance to a production environment.

The following options are supported by the preview.

- You can create DB instances using db.m6i, db.r6i, db.m6g, db.m5, db.t3,
  db.r6g, and db.r5 DB instance classes. For more information about RDS instance
  classes, see [DB instance classes](Concepts.md "Concepts.md").
- You can use both single-AZ and multi-AZ deployments.
- You can use standard MySQL dump and load functions to export databases from or
  import databases to the Database Preview environment.

### Features not supported in the

Database Preview environment

The following features aren't available in the Database Preview
environment:

- Cross-Region snapshot copy
- Cross-Region read replicas
- RDS Proxy

### Creating a new DB

instance in the Database Preview environment

You can create a DB instance in the Database Preview environment using the
AWS Management Console, AWS CLI, or RDS API.

###### To create a DB instance in the Database Preview environment

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Dashboard** from the navigation
   pane.
3. In the **Dashboard** page, locate the
   **Database Preview Environment** section, as
   shown in the following image.

![The Database Preview Environment section with link in the Amazon RDS console.](images/preview-environment-dashboard.png)

You can navigate directly to the [Database Preview environment](https://us-east-2.console.aws.amazon.com/rds-preview/home?region=us-east-2# "https://us-east-2.console.aws.amazon.com/rds-preview/home?region=us-east-2#"). Before you can proceed,
you must acknowledge and accept the limitations.

![The Database Preview Environment Service Agreement dialog to acknowledge limitations.](images/preview-environment-console.png) 4. To create the RDS for MySQL DB instance, follow the same process that
you would for creating any Amazon RDS DB instance. For more information,
see the [Console](USER_CreateDBInstance.md#USER_CreateDBInstance.CON "USER_CreateDBInstance.md#USER_CreateDBInstance.CON") procedure in [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating").
To create a DB instance in the Database Preview environment using the
AWS CLI, use the following endpoint.

```
rds-preview.us-east-2.amazonaws.com
```

To create the RDS for MySQL DB instance, follow the same process that you
would for creating any Amazon RDS DB instance. For more information, see the
[AWS CLI](USER_CreateDBInstance.md#USER_CreateDBInstance.CLI "USER_CreateDBInstance.md#USER_CreateDBInstance.CLI") procedure in [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating").

To create a DB instance in the Database Preview environment using the RDS
API, use the following endpoint.

```
rds-preview.us-east-2.amazonaws.com
```

To create the RDS for MySQL DB instance, follow the same process that you
would for creating any Amazon RDS DB instance. For more information, see the
[RDS API](USER_CreateDBInstance.md#USER_CreateDBInstance.API "USER_CreateDBInstance.md#USER_CreateDBInstance.API") procedure in [Creating a DB instance](USER_CreateDBInstance.md#USER_CreateDBInstance.Creating "USER_CreateDBInstance.md#USER_CreateDBInstance.Creating").

## MySQL version 9.5 in the Database Preview environment

MySQL version 9.5 is now available in the Amazon RDS Database Preview environment. MySQL
version 9.5 contains several improvements that are described in [Changes in
MySQL 9.5.0](https://dev.mysql.com/doc/relnotes/mysql/9.5/en/news-9-5-0.html "https://dev.mysql.com/doc/relnotes/mysql/9.5/en/news-9-5-0.html").

For information on the Database Preview environment, see [Working with the
Database Preview environment](#mysql-working-with-the-database-preview-environment "#mysql-working-with-the-database-preview-environment"). To access the
Preview Environment from the console, select [https://console.aws.amazon.com/rds-preview/](https://console.aws.amazon.com/rds-preview/ "https://console.aws.amazon.com/rds-preview/").

## MySQL version 9.4 in the Database Preview environment

MySQL version 9.4 is now available in the Amazon RDS Database Preview environment. MySQL
version 9.4 contains several improvements that are described in [Changes in
MySQL 9.4.0](https://dev.mysql.com/doc/relnotes/mysql/9.4/en/news-9-4-0.html "https://dev.mysql.com/doc/relnotes/mysql/9.4/en/news-9-4-0.html").

For information on the Database Preview environment, see [Working with the
Database Preview environment](#mysql-working-with-the-database-preview-environment "#mysql-working-with-the-database-preview-environment"). To access the
Preview Environment from the console, select [https://console.aws.amazon.com/rds-preview/](https://console.aws.amazon.com/rds-preview/ "https://console.aws.amazon.com/rds-preview/").

## MySQL version 9.3 in the Database Preview environment

MySQL version 9.3 is now available in the Amazon RDS Database Preview environment. MySQL
version 9.3 contains several improvements that are described in [Changes in
MySQL 9.3.0](https://dev.mysql.com/doc/relnotes/mysql/9.3/en/news-9-3-0.html "https://dev.mysql.com/doc/relnotes/mysql/9.3/en/news-9-3-0.html").

For information on the Database Preview environment, see [Working with the
Database Preview environment](#mysql-working-with-the-database-preview-environment "#mysql-working-with-the-database-preview-environment"). To access the
Preview Environment from the console, select [https://console.aws.amazon.com/rds-preview/](https://console.aws.amazon.com/rds-preview/ "https://console.aws.amazon.com/rds-preview/").

## Deprecated versions for

Amazon RDS for MySQL

Amazon RDS for MySQL version 5.1, 5.5, and 5.6 are deprecated.

Amazon RDS for MySQL version 9.1 and 9.2 are deprecated in the Database Preview environment.

For information about the Amazon RDS deprecation policy for MySQL, see [Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/ "https://aws.amazon.com/rds/faqs/").
