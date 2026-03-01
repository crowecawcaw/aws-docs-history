# Testing an Oracle DB upgrade

Before you upgrade your DB instance to a major version, thoroughly test your database and all applications that
access the database for compatibility with the new version. We recommend that you use the following procedure.

###### To test a major version upgrade

1. Review the Oracle upgrade documentation for the new version of the database engine
   to see if there are compatibility issues
   that might affect your database or applications.
   For more information, see
   [Database Upgrade Guide](https://docs.oracle.com/database/121/UPGRD/toc.htm "https://docs.oracle.com/database/121/UPGRD/toc.htm")
   in the Oracle documentation.
2. If your DB instance uses a custom option group,
   create a new option group compatible with the new version you are upgrading to.
   For more information, see
   [Option group considerations](USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG "USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG").
3. If your DB instance uses a custom parameter group,
   create a new parameter group compatible with the new version you are upgrading to.
   For more information, see
   [Parameter group considerations](USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.PG "USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.PG").
4. Create a DB snapshot of the DB instance to be upgraded.
   For more information, see
   [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").
5. Restore the DB snapshot to create a new test DB instance.
   For more information, see
   [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").
6. Modify this new test DB instance to upgrade it to the new version,
   by using one of the following methods:
   - [Console](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.Console "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.Console")
   - [AWS CLI](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.CLI "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.CLI")
   - [RDS API](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.API "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.API")

7. Perform testing:
   - Run as many of your quality assurance tests
     against the upgraded DB instance as needed to
     ensure that your database and application
     work correctly with the new version.
   - Implement any new tests needed
     to evaluate the impact of any compatibility issues
     that you identified in step 1.
   - Test all stored procedures, functions, and triggers.
   - Direct test versions of your applications
     to the upgraded DB instance.
     Verify that the applications
     work correctly with the new version.
   - Evaluate the storage used by the upgraded instance
     to determine if the upgrade requires additional storage.
     You might need to choose a larger instance class
     to support the new version in production.
     For more information, see
     [DB instance classes](Concepts.md "Concepts.md").

8. If all tests pass, upgrade your production DB instance. We recommend that you
   confirm that the DB instance working correctly before allowing write operations
   to the DB instance.
