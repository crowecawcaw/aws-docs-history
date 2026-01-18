# Overview

of Oracle time zone files

An Oracle Database _time zone file_ stores the following
information:

- Offset from Coordinated Universal Time (UTC)
- Transition times for Daylight Saving Time (DST)
- Abbreviations for standard time and DST
  Oracle Database supplies multiple versions of time zone files. When you create an
  Oracle database in an on-premises environment, you choose the time zone file version.
  For more information , see [Choosing a Time Zone File](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/datetime-data-types-and-time-zone-support.html#GUID-805AB986-DE12-4FEA-AF56-5AABCD2132DF "https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/datetime-data-types-and-time-zone-support.html#GUID-805AB986-DE12-4FEA-AF56-5AABCD2132DF") in the _Oracle Database Globalization
  Support Guide_.

If the rules change for DST, Oracle publishes new time zone files. Oracle releases
these new time zone files independently of the schedule for quarterly Release Updates
(RUs) and Release Update Revisions (RURs). The time zone files reside on the database
host in the directory `$ORACLE_HOME/oracore/zoneinfo/`. The time zone file
names use the format DSTv`version`, as in DSTv35.

## How the time zone file affects data transfer

In Oracle Database, the `TIMESTAMP WITH TIME ZONE` data type stores
time stamp and time zone data. Data with the `TIMESTAMP WITH TIME ZONE`
data type uses the rules in the associated time zone file version. Thus, existing
`TIMESTAMP WITH TIME ZONE` data is affected when you update the time
zone file.

Problems can occur when you transfer data between databases that use different
versions of the time zone file. For example, if you import data from a source
database with a higher time zone file version than the target database, the database
issues the `ORA-39405` error. Previously, you had to work around this
error by using either of the following techniques:

- Create an RDS for Oracle DB instance with the desired time zone file, export data from
  your source database, and then import it into the new database.
- Use AWS DMS or logical replication to migrate your data.

## Automatic updates using the TIMEZONE_FILE_AUTOUPGRADE option

When the option group attached to your RDS for Oracle DB instance includes the
`TIMEZONE_FILE_AUTOUPGRADE` option, RDS updates your time zone files
automatically. By ensuring that your Oracle databases use the same time zone file
version, you avoid time-consuming manual techniques when you move data between
different environments. The `TIMEZONE_FILE_AUTOUPGRADE` option is
supported for both container databases (CDBs) and non-CDBs.

When you add the `TIMEZONE_FILE_AUTOUPGRADE` option to your option
group, you can choose whether to add the option immediately or during the
maintenance window. After your DB instance applies the new option, RDS checks whether it
can install a newer DSTv`version` file. The target
DSTv`version` depends on the following:

- The minor engine version that your DB instance is currently running
- The minor engine version to which you want to upgrade your DB instance

For example, your current time zone file version might be DSTv33. When RDS applies
the update to your option group, it might determine that DSTv34 is currently
available on your DB instance file system. RDS will then update your time zone file to
DSTv34 automatically.

To find the available DST versions in the supported RDS release updates, look at
the patches in [Release notes for Amazon Relational Database Service
(Amazon RDS) for Oracle](../OracleReleaseNotes/Welcome.md "../OracleReleaseNotes/Welcome.md"). For example, [version 19.0.0.0.ru-2022-10.rur-2022-10.r1](../OracleReleaseNotes/oracle-version-19-0.md#oracle-version-RU-RUR.19.0.0.0.ru-2022-10.rur-2022-10.r1 "../OracleReleaseNotes/oracle-version-19-0.md#oracle-version-RU-RUR.19.0.0.0.ru-2022-10.rur-2022-10.r1") lists
patch 34533061: RDBMS - DSTV39 UPDATE - TZDATA2022C.
