# Using Database Mail on Amazon RDS for SQL Server

You can use Database Mail to send email messages to users from your Amazon RDS on SQL Server database instance. The messages can contain
files and query results. Database Mail includes the following components:

- **Configuration and security objects** – These objects create profiles and accounts,
  and are stored in the `msdb` database.
- **Messaging objects** – These objects include the [sp_send_dbmail](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-send-dbmail-transact-sql "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-send-dbmail-transact-sql") stored procedure used to send messages, and data structures that hold information about
  messages. They're stored in the `msdb` database.
- **Logging and auditing objects** – Database Mail writes logging information to the
  `msdb` database and the Microsoft Windows application event log.
- **Database Mail executable** – `DatabaseMail.exe` reads from a queue in the
  `msdb` database and sends email messages.
  RDS supports Database Mail for all SQL Server versions on the Web, Standard, and Enterprise Editions.

## Limitations

The following limitations apply to using Database Mail on your SQL Server DB instance:

- Database Mail isn't supported for SQL Server Express Edition.
- Modifying Database Mail configuration parameters isn't supported. To see the preset (default) values, use the
  [sysmail_help_configure_sp](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-help-configure-sp-transact-sql "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-help-configure-sp-transact-sql") stored procedure.
- File attachments aren't fully supported. For more information, see [Working with file attachments](#SQLServer.DBMail.Files "#SQLServer.DBMail.Files").
- The maximum file attachment size is 1 MB.
- Database Mail requires additional configuration on Multi-AZ DB instances. For more information, see [Considerations for Multi-AZ deployments](#SQLServer.DBMail.MAZ "#SQLServer.DBMail.MAZ").
- Configuring SQL Server Agent to send email messages to predefined operators isn't supported.

## Amazon RDS stored procedures and functions for Database Mail

Microsoft provides [stored procedures](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/database-mail-stored-procedures-transact-sql "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/database-mail-stored-procedures-transact-sql") for using Database Mail, such as creating, listing, updating, and deleting accounts and profiles.
In addition, RDS provides the stored procedures and functions for Database Mail shown in the following table.

| Procedure/Function              | Description                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------- |
| rds_fn_sysmail_allitems         | Shows sent messages, including those submitted by other users.                   |
| rds_fn_sysmail_event_log        | Shows events, including those for messages submitted by other users.             |
| rds_fn_sysmail_mailattachments  | Shows attachments, including those to messages submitted by other users.         |
| rds_sysmail_control             | Starts and stops the mail queue (DatabaseMail.exe process).                      |
| rds_sysmail_delete_mailitems_sp | Deletes email messages sent by all users from the Database Mail internal tables. |

## Working with file attachments

The following file attachment extensions aren't supported in Database Mail messages from RDS on SQL Server: .ade, .adp,
.apk, .appx, .appxbundle, .bat, .bak, .cab, .chm, .cmd, .com, .cpl, .dll, .dmg, .exe, .hta, .inf1, .ins, .isp, .iso, .jar, .job,
.js, .jse, .ldf, .lib, .lnk, .mde, .mdf, .msc, .msi, .msix, .msixbundle, .msp, .mst, .nsh, .pif, .ps, .ps1, .psc1, .reg, .rgs,
.scr, .sct, .shb, .shs, .svg, .sys, .u3p, .vb, .vbe, .vbs, .vbscript, .vxd, .ws, .wsc, .wsf, and .wsh.

Database Mail uses the Microsoft Windows security context of the current user to control access to files. Users who log in
with SQL Server Authentication can't attach files using the `@file_attachments` parameter with the
`sp_send_dbmail` stored procedure. Windows doesn't allow SQL Server to provide credentials from a remote
computer to another remote computer. Therefore, Database Mail can't attach files from a network share when the command is
run from a computer other than the computer running SQL Server.

However, you can use SQL Server Agent jobs to attach files. For more information on SQL Server Agent, see [Using SQL Server Agent for Amazon RDS](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md") and [SQL Server Agent](https://docs.microsoft.com/en-us/sql/ssms/agent/sql-server-agent "https://docs.microsoft.com/en-us/sql/ssms/agent/sql-server-agent") in the Microsoft
documentation.

## Considerations for Multi-AZ deployments

When you configure Database Mail on a Multi-AZ DB instance, the configuration isn't automatically propagated to the
secondary. We recommend converting the Multi-AZ instance to a Single-AZ instance, configuring Database Mail, and then converting
the DB instance back to Multi-AZ. Then both the primary and secondary nodes have the Database Mail configuration.

If you create a read replica from your Multi-AZ instance that has Database Mail configured, the replica inherits the
configuration, but without the password to the SMTP server. Update the Database Mail account with the password.

## Removing the SMTP (port 25) restriction

By default, AWS blocks outbound traffic on SMTP (port 25) for RDS for SQL Server DB instances.
This is done to prevent spam based on the elastic network interface owner's policies.
You can remove this restriction if needed. For more information, see
[How do I remove the restriction on port 25 from my Amazon EC2 instance or Lambda function?](https://repost.aws/knowledge-center/ec2-port-25-throttle "https://repost.aws/knowledge-center/ec2-port-25-throttle").
