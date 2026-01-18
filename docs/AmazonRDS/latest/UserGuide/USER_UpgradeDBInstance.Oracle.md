# Oracle major version upgrades

To perform a major version upgrade, modify the DB instance manually. Major version
upgrades don't occur automatically.

###### Important

Make sure that you thoroughly test any upgrade to verify that your applications work
correctly before applying the upgrade to your production databases. For more
information, see [Testing an Oracle DB upgrade](USER_UpgradeDBInstance.Oracle.md "USER_UpgradeDBInstance.Oracle.md").

###### Topics

- [Supported versions for major upgrades](#USER_UpgradeDBInstance.Oracle.Major.supported-versions "#USER_UpgradeDBInstance.Oracle.Major.supported-versions")
- [Supported instance classes for major upgrades](#USER_UpgradeDBInstance.Oracle.Major.instance-classes "#USER_UpgradeDBInstance.Oracle.Major.instance-classes")
- [Gathering statistics before major upgrades](#USER_UpgradeDBInstance.Oracle.Major.gathering-stats "#USER_UpgradeDBInstance.Oracle.Major.gathering-stats")
- [Allowing
  major upgrades](#USER_UpgradeDBInstance.Oracle.Major.allowing-upgrades "#USER_UpgradeDBInstance.Oracle.Major.allowing-upgrades")

## Supported versions for major upgrades

Amazon RDS supports the following major version upgrades.

| Current version                     | Upgrade supported |
| ----------------------------------- | ----------------- |
| 19.0.0.0 using the CDB architecture | 21.0.0.0          |

A major version upgrade of Oracle Database must upgrade to a Release Update (RU) that was released in the same
month or later. Major version downgrades aren't supported for any Oracle Database versions.

## Supported instance classes for major upgrades

Your current Oracle DB instance might run on a DB instance class that isn't supported for the version
to which you are upgrading. In this case, before you upgrade, migrate the DB instance to a supported DB
instance class. For more information about the supported DB instance classes for each version and edition of
Amazon RDS for Oracle, see [DB instance classes](Concepts.md "Concepts.md").

## Gathering statistics before major upgrades

Before you perform a major version upgrade, Oracle recommends that you gather optimizer statistics on the
DB instance that you are upgrading. This action can reduce DB instance downtime during the upgrade.

To gather optimizer statistics, connect to the DB instance as the master user, and
run the `DBMS_STATS.GATHER_DICTIONARY_STATS` procedure, as in the
following example.

```
EXEC DBMS_STATS.GATHER_DICTIONARY_STATS;
```

For more information, see [GATHER_DICTIONARY_STATS Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_STATS.html?source=%3Aso%3Atw%3Aor%3Aawr%3Aodv%3A%3A#GUID-867989C7-ADFC-4464-8981-437CEA7F331E "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_STATS.html?source=%3Aso%3Atw%3Aor%3Aawr%3Aodv%3A%3A#GUID-867989C7-ADFC-4464-8981-437CEA7F331E") in the Oracle documentation.

## Allowing

major upgrades

A major engine version upgrade might be incompatible with your application. The
upgrade is irreversible. If you specify a major version for the EngineVersion
parameter that is different from the current major version, you must allow major
version upgrades.

If you upgrade a major version using the CLI command [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"), specify `--allow-major-version-upgrade`. This setting isn't
persistent, so you must specify `--allow-major-version-upgrade` whenever you perform a major
upgrade. This parameter has no impact on upgrades of minor engine versions. For more information, see [Upgrading
a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

If you upgrade a major version using the console, you don't need to choose an
option to allow the upgrade. Instead, the console displays a warning that major
upgrades are irreversible.
