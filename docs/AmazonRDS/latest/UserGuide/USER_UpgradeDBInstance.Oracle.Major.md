# Oracle major version upgrades

To perform a major version upgrade, modify the DB instance manually. Major version
upgrades don't occur automatically.

###### Important

Make sure that you thoroughly test any upgrade to verify that your applications work
correctly before applying the upgrade to your production databases. For more
information, see [Testing an Oracle DB upgrade](USER_UpgradeDBInstance.Oracle.UpgradeTesting.md "USER_UpgradeDBInstance.Oracle.UpgradeTesting.md").

###### Topics

- [Supported versions for major upgrades](#USER_UpgradeDBInstance.Oracle.Major.supported-versions "#USER_UpgradeDBInstance.Oracle.Major.supported-versions")
- [Supported instance classes for major upgrades](#USER_UpgradeDBInstance.Oracle.Major.instance-classes "#USER_UpgradeDBInstance.Oracle.Major.instance-classes")
- [Gathering statistics before major upgrades](#USER_UpgradeDBInstance.Oracle.Major.gathering-stats "#USER_UpgradeDBInstance.Oracle.Major.gathering-stats")
- [Allowing major upgrades](#USER_UpgradeDBInstance.Oracle.Major.allowing-upgrades "#USER_UpgradeDBInstance.Oracle.Major.allowing-upgrades")
- [Upgrading to Oracle Database 26ai](#USER_UpgradeDBInstance.Oracle.Major.26ai "#USER_UpgradeDBInstance.Oracle.Major.26ai")

## Supported versions for major upgrades

Amazon RDS supports the following major version upgrades.

###### Note

Oracle Database 26ai is available only in Enterprise Edition.

| Current version                     | Upgrade supported  |
| ----------------------------------- | ------------------ |
| 21.0.0.0 using the CDB architecture | 26.0.0.0           |
| 19.0.0.0 using the CDB architecture | 21.0.0.0, 26.0.0.0 |

###### Note

A major version upgrade of Oracle Database must upgrade to a Release Update (RU) that was released in the same
month or later. Major version downgrades aren't supported for any Oracle Database versions.
For more information about the Oracle Database versions that Amazon RDS supports, see the [Amazon RDS for Oracle Release Notes](../OracleReleaseNotes/Welcome.md "../OracleReleaseNotes/Welcome.md").

## Supported instance classes for major upgrades

Your current Oracle DB instance might run on a DB instance class that isn't supported for the version
to which you are upgrading. In this case, before you upgrade, migrate the DB instance to a supported DB
instance class. For more information about the supported DB instance classes for each version and edition of
Amazon RDS for Oracle, see [DB instance classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

## Gathering statistics before major upgrades

Before you perform a major version upgrade, Oracle recommends that you gather optimizer statistics on the
DB instance that you are upgrading. This action can reduce DB instance downtime during the upgrade.

To gather optimizer statistics, connect to the DB instance as the master user, and
run the `DBMS_STATS.GATHER_DICTIONARY_STATS` procedure, as in the
following example.

```
EXEC DBMS_STATS.GATHER_DICTIONARY_STATS;
```

For more information, see [GATHER\_DICTIONARY\_STATS Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_STATS.html?source=%3Aso%3Atw%3Aor%3Aawr%3Aodv%3A%3A#GUID-867989C7-ADFC-4464-8981-437CEA7F331E "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_STATS.html?source=%3Aso%3Atw%3Aor%3Aawr%3Aodv%3A%3A#GUID-867989C7-ADFC-4464-8981-437CEA7F331E") in the Oracle documentation.

## Allowing major upgrades

A major engine version upgrade might be incompatible with your application. The
upgrade is irreversible. If you specify a major version for the EngineVersion
parameter that is different from the current major version, you must allow major
version upgrades.

If you upgrade a major version using the CLI command [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"), specify `--allow-major-version-upgrade`. This setting isn't
persistent, so you must specify `--allow-major-version-upgrade` whenever you perform a major
upgrade. This parameter has no impact on upgrades of minor engine versions. For more information, see [Upgrading a DB instance engine version](USER_UpgradeDBInstance.Upgrading.md "USER_UpgradeDBInstance.Upgrading.md").

If you upgrade a major version using the console, you don't need to choose an
option to allow the upgrade. Instead, the console displays a warning that major
upgrades are irreversible.

## Upgrading to Oracle Database 26ai

You can perform a major version upgrade to Oracle Database 26ai (26.0.0.0) from the following
source versions:

- Oracle Database 21c using the CDB architecture
- Oracle Database 19c using the CDB architecture

Oracle Database 26ai supports only the CDB architecture. If your DB instance runs Oracle Database 19c as a non-CDB,
first convert it to a CDB, and then upgrade it to Oracle Database 26ai. You can't change the database
architecture during an upgrade. For more information, see [Converting an RDS for Oracle non-CDB to a CDB](oracle-cdb-converting.md "oracle-cdb-converting.md").

After you convert a non-CDB to a CDB, the database uses the single-tenant
configuration. To add tenant databases (PDBs), convert the database from the
single-tenant configuration to the multi-tenant configuration. For more information, see
[Converting the single-tenant configuration to multi-tenant](oracle-single-tenant-converting.md "oracle-single-tenant-converting.md").

Before you upgrade to Oracle Database 26ai, review the following changes:

- Review the new and desupported parameters for Oracle Database 26ai. For more information,
  see [Amazon RDS parameter changes for Oracle Database 26ai (26.0.0.0)](Oracle.Concepts.database-versions.md#Oracle.Concepts.FeatureSupport.26ai.parameters "Oracle.Concepts.database-versions.md#Oracle.Concepts.FeatureSupport.26ai.parameters").
- Note the following changes to options:

  - Oracle supports only TLS 1.2 or higher for the 26ai major engine
    version. This change affects the OEM agent and SSL options and their
    option settings, specifically the allowed cipher suites and TLS versions.
    For more information, see [Oracle Management Agent for Enterprise Manager Cloud Control](Oracle.Options.OEMAgent.md "Oracle.Options.OEMAgent.md") and [Oracle Secure Sockets Layer](Appendix.Oracle.Options.SSL.md "Appendix.Oracle.Options.SSL.md").
  - Oracle Database 26ai supports only Oracle APEX version 24.1.v1 and higher. For
    more information, see [Oracle APEX](Appendix.Oracle.Options.APEX.md "Appendix.Oracle.Options.APEX.md").
  - For the NNE option, Amazon RDS has desupported older hash functions and
    cryptographic algorithms for Oracle Database 26ai. For more information, see [Oracle native network encryption](Appendix.Oracle.Options.NetworkEncryption.md "Appendix.Oracle.Options.NetworkEncryption.md").

- RDS for Oracle doesn't support the OEM Database Express and OLAP options in
  Oracle Database 26ai. Oracle desupported OEM Database Express and deprecated OLAP in
  Oracle Database 26ai. For more information, see [Oracle Enterprise Manager Database Express](Appendix.Oracle.Options.OEM_DBControl.md "Appendix.Oracle.Options.OEM_DBControl.md") and [Oracle OLAP](Oracle.Options.OLAP.md "Oracle.Options.OLAP.md").
- RDS for Oracle doesn't support the Locator option in Oracle Database 26ai. Oracle Spatial
  supersedes Oracle Locator and includes its functionality. To use Locator
  functionality in Oracle Database 26ai, use the Oracle Spatial option instead. For more
  information, see [Oracle Locator](Oracle.Options.Locator.md "Oracle.Options.Locator.md") and [Oracle Spatial](Oracle.Options.Spatial.md "Oracle.Options.Spatial.md").
