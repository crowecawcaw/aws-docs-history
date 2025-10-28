# Downgrade your SQL Server Enterprise

edition

If you determine that you can downgrade your SQL Server Enterprise edition, you can follow
this process to convert to SQL Server Standard or Developer edition. For information on how
to automate for this process, see [Downgrade SQL Server Enterprise edition using AWS Systems Manager Document to reduce
cost](https://aws.amazon.com/blogs/mt/downgrade-sql-server-enterprise-edition-using-aws-systems-manager-document-to-reduce-cost/ "https://aws.amazon.com/blogs/mt/downgrade-sql-server-enterprise-edition-using-aws-systems-manager-document-to-reduce-cost/").

###### Important

- This process will require downtime for your SQL Server instance. Your database
  will not be operational until the entire procedure has been completed
  successfully.
- Only SQL Server instances using BYOL software support in-place downgrading. For
  more information, see [Licensing options](sql-server-on-ec2-licensing.md#sql-server-on-ec2-licensing-options "sql-server-on-ec2-licensing.md#sql-server-on-ec2-licensing-options").

###### To downgrade your SQL Server Enterprise edition

1. [Create a `Full` backup](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/create-a-full-database-backup-sql-server?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/create-a-full-database-backup-sql-server?view=sql-server-ver16") of all user and system databases.
   Ensure that the backup completes successfully before continuing.
2. Note your current SQL Server minor version, service pack, cumulative updates, and
   the General Distribution Release (GDR). For more information, see [Determine which version and edition of SQL Server Database Engine is
   running](https://learn.microsoft.com/en-us/troubleshoot/sql/releases/find-my-sql-version "https://learn.microsoft.com/en-us/troubleshoot/sql/releases/find-my-sql-version") in the Microsoft documentation.
3. [Detach](https://learn.microsoft.com/en-us/sql/relational-databases/databases/detach-a-database?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/relational-databases/databases/detach-a-database?view=sql-server-ver16") all user databases.
4. [Stop the SQL Server Database Engine](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/start-stop-pause-resume-restart-sql-server-services?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/start-stop-pause-resume-restart-sql-server-services?view=sql-server-ver16") service and copy the log and system
   database data files—`master`,
   `model`, and `msdb`—to a local
   backup folder.
5. [Uninstall SQL Server](https://learn.microsoft.com/en-us/sql/sql-server/install/uninstall-an-existing-instance-of-sql-server-setup?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/sql-server/install/uninstall-an-existing-instance-of-sql-server-setup?view=sql-server-ver16") Enterprise edition including all components.
6. [Reboot](../../../AWSEC2/latest/WindowsGuide/ec2-instance-reboot.md "../../../AWSEC2/latest/WindowsGuide/ec2-instance-reboot.md") the
   instance.
7. [Install SQL Server](https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver16") Standard or Developer edition according to your
   requirement.
8. Install the same service packs and cumulative updates that you had before the
   uninstall.
9. Stop the SQL Server Database Engine service.
10. Using the backups you made in step 4, restore the `master`,
    `model`, and `msdb` databases.
11. Start SQL Server service.
12. [Attach](https://learn.microsoft.com/en-us/sql/relational-databases/databases/attach-a-database?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/relational-databases/databases/attach-a-database?view=sql-server-ver16") the `mdf` and `ldf`
    user databases that were detached in step 3 to your SQL Server instance.
13. Confirm that your database is operating as expected.
