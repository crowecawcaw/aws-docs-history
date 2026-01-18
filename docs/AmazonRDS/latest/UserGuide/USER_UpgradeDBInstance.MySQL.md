# Testing an RDS for MySQL upgrade

Before you perform a major version upgrade on your DB instance, thoroughly test your
database for compatibility with the new version. In addition, thoroughly test all
applications that access the database for compatibility with the new version. We
recommend that you use the following procedure.

###### To test a major version upgrade

1. Review the upgrade documentation for the new version of the database engine to see if there
   are compatibility issues that might affect your database or applications:
   - [Changes in MySQL 5.7](http://dev.mysql.com/doc/refman/5.7/en/upgrading-from-previous-series.html "http://dev.mysql.com/doc/refman/5.7/en/upgrading-from-previous-series.html")
   - [Changes in MySQL 8.0](http://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html "http://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html")
   - [Changes in MySQL 8.4](http://dev.mysql.com/doc/refman/8.4/en/upgrading-from-previous-series.html "http://dev.mysql.com/doc/refman/8.4/en/upgrading-from-previous-series.html")

2. If your DB instance is a member of a custom DB parameter group, create a new
   DB parameter group with your existing settings that is compatible with the new
   major version. Specify the new DB parameter group when you upgrade your test
   instance, so your upgrade testing ensures that it works correctly. For more
   information about creating a DB parameter group, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
3. Create a DB snapshot of the DB instance to be upgraded.
   For more information, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").
4. Restore the DB snapshot to create a new test DB instance. For more information, see [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").
5. Modify this new test DB instance to upgrade it to the new version, using one of the methods
   detailed following. If you created a new parameter group in step 2, specify
   that parameter group.
6. Evaluate the storage used by the upgraded instance to determine if the upgrade requires
   additional storage.
7. Run as many of your quality assurance tests against the upgraded DB instance
   as needed to ensure that your database and application work correctly with the
   new version. Implement any new tests needed to evaluate the impact of any
   compatibility issues that you identified in step 1. Test all stored procedures
   and functions. Direct test versions of your applications to the upgraded DB
   instance.
8. If all tests pass, then perform the upgrade on your production DB instance. We
   recommend that you don't allow write operations to the DB instance until
   you confirm that everything is working correctly.
