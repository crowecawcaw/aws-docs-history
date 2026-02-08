# SQL Server database migration to Amazon Aurora MySQL troubleshooting

When you work with Microsoft SQL Server as a source database and Amazon Aurora MySQL as a target database, the two most common problem areas are SQL Server change data capture (CDC) and foreign keys.

- MS-CDC: If you are using MS-CDC with SQL Server for the migration, errors that are related to permissions or errors during change data capture are common. These types of errors usually result when one of the prerequisites was not met. For example, the most common overlooked prerequisite is a full database backup.
- Foreign keys: During the full load process, AWS DMS does not load tables in any particular order, so it might load the child table data before parent table data. As a result, foreign key constraints might be violated if they are enabled. You should disable foreign keys on the Aurora MySQL target database. You can enable the foreign keys on the target after the migration is complete.
  For more tips, see the AWS DMS troubleshooting section in the [Troubleshooting migration tasks](../userguide/CHAP_Troubleshooting.md "../userguide/CHAP_Troubleshooting.md").

To troubleshoot issues specific to SQL Server, see the SQL Server troubleshooting section:

- [Troubleshooting Microsoft SQL Server Specific Issues](../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.SQLServer "../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.SQLServer")
  To troubleshoot Aurora MySQL issues, see the Aurora MySQL troubleshooting section and the MySQL troubleshooting section:

- [Troubleshooting Amazon Aurora MySQL Specific Issues](../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.Aurora "../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.Aurora")
- [Troubleshooting MySQL Specific Issues](../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL "../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL")
