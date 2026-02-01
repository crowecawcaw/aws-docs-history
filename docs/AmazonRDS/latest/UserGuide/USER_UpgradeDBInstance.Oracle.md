# Considerations for Oracle database

upgrades

Before you upgrade your Oracle instance, review the following information.

###### Topics

- [Oracle Multitenant
  considerations](#USER_UpgradeDBInstance.Oracle.multi "#USER_UpgradeDBInstance.Oracle.multi")
- [Option group considerations](#USER_UpgradeDBInstance.Oracle.OGPG.OG "#USER_UpgradeDBInstance.Oracle.OGPG.OG")
- [Parameter group
  considerations](#USER_UpgradeDBInstance.Oracle.OGPG.PG "#USER_UpgradeDBInstance.Oracle.OGPG.PG")
- [Time zone considerations](#USER_UpgradeDBInstance.Oracle.OGPG.DST "#USER_UpgradeDBInstance.Oracle.OGPG.DST")
- [Spatial Patch Bundle (SPB)
  considerations](#USER_UpgradeDBInstance.Oracle.SPB "#USER_UpgradeDBInstance.Oracle.SPB")

## Oracle Multitenant

considerations

The following table describes the Oracle Database architectures supported in different
releases.

| Oracle Database release | RDS support status | Architecture   |
| ----------------------- | ------------------ | -------------- |
| Oracle Database 21c     | Supported          | CDB only       |
| Oracle Database 19c     | Supported          | CDB or non-CDB |

The following table describes supported and unsupported upgrade paths.

| Upgrade path   | Supported?                                                     |
| -------------- | -------------------------------------------------------------- |
| CDB to CDB     | Yes                                                            |
| Non-CDB to CDB | No, but you can convert a non-CDB to a CDB and then upgrade it |
| CDB to non-CDB | No                                                             |

For more information about Oracle Multitenant in RDS for Oracle, see [Single-tenant configuration of the
CDB architecture](Oracle.Concepts.md#Oracle.Concepts.single-tenant "Oracle.Concepts.md#Oracle.Concepts.single-tenant").

## Option group considerations

If your DB instance uses a custom option group, sometimes Amazon RDS can't automatically assign a new
option group. For example, this situation occurs when you upgrade to a new major version. In
such cases, specify a new option group when you upgrade. We recommend that you create a new
option group, and add the same options to it as in your existing custom option group.

For more information, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create") or [Copying an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy").

If your DB instance uses a custom option group that contains the `APEX` and
`APEX-DEV` options, you can sometimes reduce the upgrade time. To do this,
upgrade your version of Oracle APEX at the same time as your DB instance. For more information,
see [Upgrading the Oracle APEX
version](Appendix.Oracle.Options.APEX.md#Appendix.Oracle.Options.APEX.Upgrade "Appendix.Oracle.Options.APEX.md#Appendix.Oracle.Options.APEX.Upgrade").

## Parameter group

considerations

If your DB instance uses a custom parameter group, sometimes Amazon RDS can't automatically
assign your DB instance a new parameter group. For example, this situation occurs when you
upgrade to a new major version. In such cases, make sure to specify a new parameter group
when you upgrade. We recommend that you create a new parameter group, and configure the
parameters as in your existing custom parameter group.

For more information, see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md") or [Copying a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Time zone considerations

You can use the time zone option to change the _system time zone_ used
by your Oracle DB instance. For example, you might change the time zone of a DB instance to
be compatible with an on-premises environment, or a legacy application. The time zone option
changes the time zone at the host level. Amazon RDS for Oracle updates the system time zone
automatically throughout the year. For more information about the system time zone, see
[Oracle time zone](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md").

When you create an Oracle DB instance, the database automatically sets the
_database time zone_. The database time zone is also known as the
Daylight Saving Time (DST) time zone. The database time zone is distinct from the system
time zone.

Between Oracle Database releases, patch sets or individual patches may include new DST
versions. These patches reflect the changes in transition rules for various time zone
regions. For example, a government might change when DST takes effect. Changes to DST rules
may affect existing data of the `TIMESTAMP WITH TIME ZONE` data type.

If you upgrade an RDS for Oracle DB instance, Amazon RDS doesn't upgrade the database time zone
file automatically. To upgrade the time zone file automatically, you can include the
`TIMEZONE_FILE_AUTOUPGRADE` option in the option group associated with your
DB instance during or after the engine version upgrade. For more information, see [Oracle time zone file autoupgrade](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md").

Alternatively, to upgrade the database time zone file manually, create a new Oracle DB
instance that has the desired DST patch. However, we recommend that you upgrade the database
time zone file using the `TIMEZONE_FILE_AUTOUPGRADE` option.

After upgrading the time zone file, migrate the data from your current instance to the new
instance. You can migrate data using several techniques, including the following:

- AWS Database Migration Service
- Oracle GoldenGate
- Oracle Data Pump
- Original Export/Import (desupported for general use)

###### Note

When you migrate data using Oracle Data Pump, the utility raises the error ORA-39405
when the target time zone version is lower than the source time zone version.

For more information, see [TIMESTAMP WITH TIMEZONE restrictions](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-overview.html#GUID-9B6C92EE-860E-43DD-9728-735B17B9DA89 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-overview.html#GUID-9B6C92EE-860E-43DD-9728-735B17B9DA89") in the Oracle documentation.

## Spatial Patch Bundle (SPB)

considerations

In RDS for Oracle, release update (RU) is a minor engine version that includes security fixes,
bug fixes, and new features for Oracle Database. A Spatial Patch Bundle (SPB) is minor
engine version that also includes patches designed for the Oracle Spatial option. For
example, 19.0.0.0.ru-2025-01.spb-1.r1 is a minor engine version that contains the RU patches
in engine version 19.0.0.0.ru-2025-01.rur-2025-01.r1 plus Spatial patches.

When you upgrade your database to SPBs, consider the following:

- SPBs are supported only for Oracle Database 19c.
- Typically, an SPB is released 2–3 weeks after its corresponding quarterly
  RU.
- You can upgrade your DB instance to an SPB even if the instance doesn't use the Oracle
  Spatial option, but the Spatial patches in the engine version apply only to Oracle
  Spatial. You can create a new instance on an SPB and install the Oracle Spatial
  option later.
- If you enable automatic minor version upgrade for your DB instance, your upgrade path
  depends on whether your instance currently uses an SPB or RU. If your
  instance uses an SPB, RDS automatically upgrades your instance to the latest SPB. If
  your instance uses an RU, RDS automatically upgrades your instance to the
  latest RU.
- You can manually upgrade your DB instance from an RU to an SPB only if the SPB
  is the same engine version or higher as your current RU.
- You can manually upgrade your DB instance from an SPB to an RU only if the
  RU is a higher version.
