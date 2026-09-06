

# Preparing for Oracle Database 21c end of support
<a name="USER_UpgradeDBInstance.Oracle.21c-end-of-support"></a>

Oracle Database 21c is an Innovation Release, and Oracle is ending support for it on July 31, 2027. After this date, Oracle will not release any further security patches or updates for Oracle Database 21c. Amazon RDS will deprecate the 21c major engine version in line with the Oracle support timeline.

Innovation Releases are designed for early access to new capabilities and have a shorter support lifecycle than Long Term Support Releases. Long Term Support Releases offer the highest level of stability and the longest length of error correction support. The currently available Long Term Support Releases are Oracle Database 19c and Oracle Database 26ai.

## Choosing your upgrade path
<a name="USER_UpgradeDBInstance.Oracle.21c-end-of-support.choosing-path"></a>

Your upgrade path depends on the Oracle Database edition you are currently running:
+ **Enterprise Edition (EE)** — You can perform a direct, in-place major version upgrade to Oracle Database 26ai.
+ **Standard Edition 2 (SE2)** — Oracle Database 26ai is available in Enterprise Edition only. Standard Edition 2 is not available for Oracle Database 26ai. You must choose between migrating to Oracle Database 19c (which supports SE2) or moving to Oracle Database 26ai Enterprise Edition.

## Upgrading from Oracle Database 21c Enterprise Edition
<a name="USER_UpgradeDBInstance.Oracle.21c-end-of-support.ee"></a>

If you are running Oracle Database 21c Enterprise Edition, you can upgrade directly to Oracle Database 26ai. Oracle Database 26ai is Oracle's latest Long Term Support release. It is available on Amazon RDS in Enterprise Edition.

To upgrade, modify your DB instance and select a 26.0.0.0 engine version. Amazon RDS performs the major version upgrade. Both Oracle Database 21c and Oracle Database 26ai use the multitenant (CDB) architecture, so no architecture conversion is required. Your edition and licensing model remain unchanged.

For information about new capabilities in Oracle Database 26ai, see [Oracle Database 26ai with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.database-versions.html).

For more information about upgrading, see [Upgrading the RDS for Oracle DB engine](USER_UpgradeDBInstance.Oracle.md).

## Upgrading from Oracle Database 21c Standard Edition 2
<a name="USER_UpgradeDBInstance.Oracle.21c-end-of-support.se2"></a>

Oracle Database 26ai is available in Enterprise Edition only. If you are running Oracle Database 21c Standard Edition 2, you have two options.

### Option 1: Migrate to Oracle Database 19c Standard Edition 2
<a name="USER_UpgradeDBInstance.Oracle.21c-end-of-support.se2.option1"></a>

Oracle Database 19c is a Long Term Support release that continues to support Standard Edition 2 on Amazon RDS. This option preserves your current edition, licensing model, and cost structure.

Because Oracle Database 19c is a lower major version than 21c, you cannot perform an in-place upgrade. Instead, you perform a logical migration using one of the following methods:
+ **Oracle Data Pump** — Export data from your Oracle Database 21c instance and import it into a new Oracle Database 19c SE2 instance.
+ **AWS DMS** — Use AWS DMS to migrate data with minimal downtime.

### Option 2: Move to Oracle Database 26ai Enterprise Edition
<a name="USER_UpgradeDBInstance.Oracle.21c-end-of-support.se2.option2"></a>

If your workload requires Enterprise Edition capabilities or Oracle Database 26ai features, you can upgrade to Oracle Database 26ai. This option requires the following changes:
+ An Oracle Enterprise Edition license under the Bring Your Own License (BYOL) model
+ A change in your licensing and cost profile

You can perform an in-place major version upgrade from Oracle Database 21c container databases (CDBs) by modifying your DB instance and selecting a 26.0.0.0 engine version.

For information about changing your Oracle Database edition, see [Migrating between Oracle Database editions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.Licensing.html).

## Comparing Standard Edition 2 options
<a name="USER_UpgradeDBInstance.Oracle.21c-end-of-support.comparison"></a>

The following table compares the two options if you are running Standard Edition 2.


| Consideration | Option 1: Oracle Database 19c SE2 | Option 2: Oracle Database 26ai EE | 
| --- | --- | --- | 
| Oracle edition | Standard Edition 2 (no change) | Enterprise Edition (change required) | 
| Licensing model | License Included or BYOL | BYOL only | 
| Cost impact | Comparable to current | Higher | 
| Migration method | Logical migration (Data Pump or AWS DMS) | In-place major version upgrade | 
| Oracle Database 26ai features | Not available | Available | 

## Before you begin
<a name="USER_UpgradeDBInstance.Oracle.21c-end-of-support.before-you-begin"></a>

Before you upgrade or migrate, do the following:

1. **Identify your current edition.** Confirm whether you are running Enterprise Edition or Standard Edition 2, because this determines your recommended path.

1. **Test in a non-production environment.** Restore a DB snapshot to create a test instance, and validate your application against the target version before modifying your production instance.

1. **Create a manual DB snapshot.** Take a manual snapshot of your Oracle Database 21c DB instance before you begin. This provides a recovery point if you need to roll back.

1. **Review version and edition details.** For more information about supported Oracle Database versions and editions on Amazon RDS, see [RDS for Oracle releases](Oracle.Concepts.database-versions.md).

**Important**  
If you are running Standard Edition 2 and want to evaluate whether your workload can run on Enterprise Edition, see [Comparing Oracle Database EE and SE2 features](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/compare-features.html).