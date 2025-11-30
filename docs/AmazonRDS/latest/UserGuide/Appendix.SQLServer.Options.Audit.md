# Adding SQL Server Audit to the DB instance options

Enabling SQL Server Audit requires two steps: enabling the option on the DB instance, and
enabling the feature inside SQL Server. The process for adding the SQL Server Audit
option to a DB instance is as follows:

1. Create a new option group, or copy or modify an existing option group.
2. Add and configure all required options.
3. Associate the option group with the DB instance.
   After you add the SQL Server Audit option, you don't need to restart your DB instance. As
   soon as the option group is active, you can create audits and store audit logs in your
   S3 bucket.

###### To add and configure SQL Server Audit on a DB instance's option group

1. Choose one of the following:
   - Use an existing option group.
   - Create a custom DB option group and use that option group. For more
     information, see
     [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create").

2. Add the **SQLSERVER_AUDIT** option to the option
   group, and configure the option settings. For more information about adding options,
   see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption").
   - For **IAM role**, if you already have an IAM role with
     the required policies, you can choose that role. To create a new IAM
     role, choose **Create a New Role**. For
     information about the required policies, see
     [Manually creating an IAM role for SQL Server Audit](Appendix.SQLServer.Options.Audit.md "Appendix.SQLServer.Options.Audit.md").
   - For **Select S3 destination**, if you already have an S3 bucket that you want to use, choose it. To create an
     S3 bucket, choose **Create a New S3 Bucket**.
   - For **Enable Compression**, leave this option chosen to
     compress audit files. Compression is enabled by default. To disable
     compression, clear **Enable Compression**.
   - For **Audit log retention**, to keep audit records on the
     DB instance, choose this option. Specify a retention time in hours. The
     maximum retention time is 35 days.

3. Apply the option group to a new or existing DB instance. Choose one of the
   following:
   - If you are creating a new DB instance, apply the option group when you launch the
     instance.
   - On an existing DB instance, apply the option group by modifying the instance and then
     attaching the new option group. For more information, see
     [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Modifying the SQL Server Audit option

After you enable the SQL Server Audit option, you can modify the settings. For information
about how to modify option settings, see [Modifying an option setting](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.ModifyOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.ModifyOption").

## Removing SQL Server Audit from the DB instance options

You can turn off the SQL Server Audit feature by disabling audits and then
deleting the option.

###### To remove auditing

1. Disable all of the audit settings inside SQL Server. To learn where
   audits are running, query the SQL Server security catalog views. For
   more information, see [Security catalog views](https://docs.microsoft.com/sql/relational-databases/system-catalog-views/security-catalog-views-transact-sql "https://docs.microsoft.com/sql/relational-databases/system-catalog-views/security-catalog-views-transact-sql") in the Microsoft SQL Server
   documentation.
2. Delete the SQL Server Audit option from the DB instance. Choose one of
   the following:
   - Delete the SQL Server Audit option from the option group that
     the DB instance uses. This change affects all DB instances that
     use the same option group. For more information, see [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption").
   - Modify the DB instance, and then choose an option group
     without the SQL Server Audit option. This change affects only
     the DB instance that you modify. You can specify the default
     (empty) option group, or a different custom option group. For
     more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

3. After you delete the SQL Server Audit option from the DB instance, you
   don't need to restart the instance. Remove unneeded audit files from
   your S3 bucket.
