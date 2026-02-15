# Database mail features

This topic provides reference information about migrating the Database Mail feature from Microsoft SQL Server 2019 to Amazon Aurora MySQL. You can understand the key differences in email functionality between these two database systems and learn about alternative approaches for sending emails from Aurora MySQL.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                       | Key differences                                                                                                                                                                                                                                                         |
| ------------------------------ | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| One star feature compatibility | No automation                      | [SQL Server Database Mail](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.mail "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.mail") | Use AWS Lambda integration. For more information, see [Invoking a Lambda function from an Amazon Aurora MySQL DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md"). |

## SQL Server Usage

The Database Mail framework is an email client solution for sending messages directly from SQL Server. Email capabilities and APIs within the database server provide easy management of the following messages:

- Server administration messages such as alerts, logs, status reports, and process confirmations.
- Application messages such as user registration confirmation and action verifications.

###### Note

Database Mail is turned off by default.

The main features of the Database Mail framework are:

- Database Mail sends messages using the standard and secure Simple Mail Transfer Protocol (SMTP).
- The email client engine runs asynchronously and sends messages in a separate process to minimize dependencies.
- Database Mail supports multiple SMTP Servers for redundancy.
- Full support and awareness of Windows Server Failover Cluster for high availability environments.
- Multi-profile support with multiple failover accounts in each profile.
- Enhanced security management with separate roles in MSDB.
- Security is enforced for mail profiles.
- Attachment sizes are monitored and can be capped by the administrator.
- Attachment file types can be added to the deny list.
- Email activity can be logged to SQL Server, the Windows application event log, and to a set of system tables in MSDB.
- Supports full auditing capabilities with configurable retention policies.
- Supports both plain text and HTML messages.

### Architecture

Database Mail is built on top of the Microsoft SQL Server Service Broker queue management framework.

The system stored procedure `sp_send_dbmail` sends email messages. When this stored procedure runs, it inserts an row to the mail queue and records the email message.

The queue insert operation triggers the run of the Database Mail process (DatabaseMail.exe). The Database Mail process then reads the email information and sends the message to the SMTP servers.

When the SMTP servers acknowledge or reject the message, the Database Mail process inserts a status row into the status queue, including the result of the send attempt. This insert operation triggers the run of a system stored procedure that updates the status of the Email message send attempt.

Database Mail records all Email attachments in the system tables. SQL Server provides a set of system views and stored procedures for troubleshooting and administration of the Database Mail queue.

### Deprecated SQL Mail Framework

The old SQL Mail framework using `xp_sendmail` has been deprecated as of SQL Server 2008 R2. For more information, see [Deprecated Database Engine Features in SQL Server 2008 R2](<https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)> "https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)") in the _SQL Server documentation_.

The legacy mail system has been completely replaced by the greatly enhanced DB mail framework described here. The old system has been out-of-use for many years because it was prone to synchronous run issues and windows mail profile quirks.

### Syntax

```
EXECUTE sp_send_dbmail
    [[,@profile_name =] '<Profile Name>']
    [,[,@recipients =] '<Recipients>']
    [,[,@copy_recipients =] '<CC Recipients>']
    [,[,@blind_copy_recipients =] '<BCC Recipients>']
    [,[,@from_address =] '<From Address>']
    [,[,@reply_to =] '<Reply-to Address>']
    [,[,@subject =] '<Subject>']
    [,[,@body =] '<Message Body>']
    [,[,@body_format =] '<Message Body Format>']
    [,[,@importance =] '<Importance>']
    [,[,@sensitivity =] '<Sensitivity>']
    [,[,@file_attachments =] '<Attachments>']
    [,[,@query =] '<SQL Query>']
    [,[,@execute_query_database =] '<Execute Query Database>']
    [,[,@attach_query_result_as_file =] <Attach Query Result as File>]
    [,[,@query_attachment_filename =] <Query Attachment Filename>]
    [,[,@query_result_header =] <Query Result Header>]
    [,[,@query_result_width =] <Query Result Width>]
    [,[,@query_result_separator =] '<Query Result Separator>']
    [,[,@exclude_query_output =] <Exclude Query Output>]
    [,[,@append_query_error =] <Append Query Error>]
    [,[,@query_no_truncate =] <Query No Truncate>]
    [,[,@query_result_no_padding =] @<Parameter for Query Result No Padding>]
    [,[,@mailitem_id =] <Mail item id>] [,OUTPUT]
```

### Examples

Create a Database Mail account.

```
EXECUTE msdb.dbo.sysmail_add_account_sp
    @account_name = 'MailAccount1',
    @description = 'Mail account for testing DB Mail',
    @email_address = 'Address@MyDomain.com',
    @replyto_address = 'ReplyAddress@MyDomain.com',
    @display_name = 'Mailer for registration messages',
    @mailserver_name = 'smtp.MyDomain.com' ;
```

Create a Database Mail profile.

```
EXECUTE msdb.dbo.sysmail_add_profile_sp
    @profile_name = 'MailAccount1 Profile',
    @description = 'Mail Profile for testing DB Mail' ;
```

Associate the account with the profile.

```
EXECUTE msdb.dbo.sysmail_add_profileaccount_sp
    @profile_name = 'MailAccount1 Profile',
    @account_name = 'MailAccount1',
    @sequence_number =1 ;
```

Grant the profile access to the `DBMailUsers` role.

```
EXECUTE msdb.dbo.sysmail_add_principalprofile_sp
    @profile_name = 'MailAccount1 Profile',
    @principal_name = 'ApplicationUser',
    @is_default = 1 ;
```

Send a message with `sp_db_sendmail`.

```
EXEC msdb.dbo.sp_send_dbmail
    @profile_name = 'MailAccount1 Profile',
    @recipients = 'Recipient@Mydomain.com',
    @query = 'SELECT * FROM fn_WeeklySalesReport(GETDATE())',
    @subject = 'Weekly Sales Report',
    @attach_query_result_as_file = 1 ;
```

For more information, see [Database Mail](https://docs.microsoft.com/en-us/sql/relational-databases/database-mail/database-mail?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/database-mail/database-mail?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) doesn’t provide native support sending mail from the database.

For alerting purposes, use the event notification subscription feature to send email notifications to operators. For more information, see [Alerting](chap-sql-server-aurora-mysql.management.md "chap-sql-server-aurora-mysql.management.md").

For application email requirements, consider using a dedicated email framework. If the code generating email messages must be in the database, consider using a queue table. Replace all occurrences of `sp_send_dbmail` with an `INSERT` into the queue table. Design external applications to connect, read the queue, send email an message, and then update the status periodically. With this approach, messages can be populated with a query result similar to `sp_send_dbmail` with the query option.

The only way to send email from the database, is to use the AWS Lambda integration.

For more information, see [AWS Lambda](https://aws.amazon.com/lambda "https://aws.amazon.com/lambda").

### Examples

You can send emails from Aurora MySQL using AWS Lambda integration. For more information, see [Invoking a Lambda function from an Amazon Aurora MySQL DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.md").
