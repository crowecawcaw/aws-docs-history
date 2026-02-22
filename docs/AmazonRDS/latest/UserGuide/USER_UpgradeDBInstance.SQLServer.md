# Testing an RDS for SQL Server upgrade

Before you perform a major version upgrade on your DB instance, you should thoroughly test your database, and all applications
that access the database, for compatibility with the new version. We recommend that you use the following procedure.

###### To test a major version upgrade

1. Review [Upgrade
   SQL Server](https://docs.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server "https://docs.microsoft.com/en-us/sql/database-engine/install-windows/upgrade-sql-server") in the Microsoft documentation for the new version of the database engine to see if there are
   compatibility issues that might affect your database or applications.
2. If your DB instance uses a custom option group, create a new option group compatible with the new version you are
   upgrading to. For more information, see [Option group considerations](USER_UpgradeDBInstance.SQLServer.md#USER_UpgradeDBInstance.SQLServer.OGPG.OG "USER_UpgradeDBInstance.SQLServer.md#USER_UpgradeDBInstance.SQLServer.OGPG.OG").
3. If your DB instance uses a custom parameter group, create a new parameter group compatible with the new version you
   are upgrading to. For more information, see [Parameter group considerations](USER_UpgradeDBInstance.SQLServer.md#USER_UpgradeDBInstance.SQLServer.OGPG.PG "USER_UpgradeDBInstance.SQLServer.md#USER_UpgradeDBInstance.SQLServer.OGPG.PG").
4. Create a DB snapshot of the DB instance to be upgraded. For more information, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").
5. Restore the DB snapshot to create a new test DB instance. For more information, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").
6. Modify this new test DB instance to upgrade it to the new version, by using one of the following methods:
   - [Console](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.Console "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.Console")
   - [AWS CLI](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.CLI "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.CLI")
   - [RDS API](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.API "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.Manual.API")

7. Evaluate the storage used by the upgraded instance to determine if the upgrade requires
   additional storage.
8. Run as many of your quality assurance tests against the upgraded DB instance as needed to
   ensure that your database and application work correctly with the new version.
   Implement any new tests needed to evaluate the impact of any compatibility
   issues you identified in step 1. Test all stored procedures and functions.
   Direct test versions of your applications to the upgraded DB instance.
9. If all tests pass, then perform the upgrade on your production DB instance.
   We recommend that you do not allow write operations
   to the DB instance until you confirm that
   everything is working correctly.
