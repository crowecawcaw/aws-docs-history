# Using an AWS SCT extension pack to

emulate SQL Server Database Mail in PostgreSQL

You can use SQL Server Database Mail to send email messages to users from
the SQL Server Database Engine or Azure SQL Managed Instance. These email messages
can contain query results or include files from any resource on your network. For
more information about SQL Server Database Mail, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/database-mail/database-mail?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/database-mail/database-mail?view=sql-server-ver15").

PostgreSQL doesn't have an equivalent for SQL Server Database Mail. To emulate the
SQL Server Database Mail features, AWS SCT creates an extension pack.
This extension pack uses AWS Lambda and Amazon Simple Email Service (Amazon SES).
AWS Lambda provides users with an interface to interact with Amazon SES email sending
service. To set up this interaction, add the Amazon Resource Name (ARN) of your
Lambda function.

For a new email account, use the following command.

```
do
$$
begin
PERFORM sysmail_add_account_sp (
    par_account_name :='your_account_name',
    par_email_address := 'your_account_email',
    par_display_name := 'your_account_display_name',
    par_mailserver_type := 'AWSLAMBDA'
    par_mailserver_name := '`ARN`'
);
end;
$$ language plpgsql;
```

To add the ARN of your Lambda function to the existing email account, use the
following command.

```
do
$$
begin
PERFORM sysmail_update_account_sp (
    par_account_name :='existind_account_name',
    par_mailserver_type := 'AWSLAMBDA'
    par_mailserver_name := '`ARN`'
);
end;
$$ language plpgsql;
```

In the preceding examples, `ARN` is the ARN
of your Lambda function.

To emulate the SQL Server Database Mail behavior in PostgreSQL, the AWS SCT
extension pack uses the following tables, views, and procedures.

## Tables that emulate SQL Server Database Mail in PostgreSQL

To emulate SQL Server Database Mail, the extension pack uses the following tables:

**sysmail_account**
Stores the information about the email accounts.

**sysmail_profile**
Stores the information about the user profiles.

**sysmail_server**
Stores the information about the email servers.

**sysmail_mailitems**
Stores the list of the email messages.

**sysmail_attachments**
Contains one row for each email attachment.

**sysmail_log**
Stores the service information about sending email messages.

**sysmail_profileaccount**
Stores the information about the user profiles and email accounts.

## Views that emulate SQL Server Database Mail in PostgreSQL

To emulate SQL Server Database Mail, AWS SCT creates the following views in
the PostgreSQL database to ensure compatibility. The extension pack doesn't use
them, but your converted code can query these views.

**sysmail_allitems**
Includes a list of all emails.

**sysmail_faileditems**
Includes a list of emails that couldn't be sent.

**sysmail_sentitems**
Includes a list of sent emails.

**sysmail_unsentitems**
Includes a list of emails that aren't sent yet.

**sysmail_mailattachments**
Includes a list of attached files.

## Procedures that emulate SQL Server Database Mail in PostgreSQL

To emulate SQL Server Database Mail, the extension pack uses the following procedures:

**sp_send_dbmail**
Sends an email to the specified recipients.

**sysmail_add_profile_sp**
Creates a new user profile.

**sysmail_add_account_sp**
Creates a new email account that stores such information
as Simple Mail Transfer Protocol (SMTP) credentials, and so on.

**sysmail_add_profileaccount_sp**
Adds an email account to the specified user profile.

**sysmail_update_profile_sp**
Changes the attributes of the user profile such as
description, name, and so on.

**sysmail_update_account_sp**
Changes the information in the existing email account.

**sysmail_update_profileaccount_sp**
Updates the email account information in the specified user profile.

**sysmail_delete_profileaccount_sp**
Removes an email account from the specified user profile.

**sysmail_delete_account_sp**
Deletes the email account.

**sysmail_delete_profile_sp**
Deletes the user profile.

**sysmail_delete_mailitems_sp**
Deletes emails from internal tables.

**sysmail_help_profile_sp**
Displays information about the user profile.

**sysmail_help_account_sp**
Displays information about the email account.

**sysmail_help_profileaccount_sp**
Displays information about email accounts associated
with the user profile.

**sysmail_dbmail_json**
An internal procedure that generates JSON requests
for AWS Lambda functions.

**sysmail_verify_profile_sp, sysmail_verify_account_sp, sysmail_verify_addressparams_sp**
Internal procedures that check settings.

**sp_get_dbmail, sp_set_dbmail, sysmail_dbmail_xml**
Deprecated internal procedures.

## Syntax for procedures that

emulate SQL Server Database Mail in PostgreSQL

The `aws_sqlserver_ext.sp_send_dbmail` procedure in the extension pack
emulates the `msdb.dbo.sp_send_dbmail` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-send-dbmail-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-send-dbmail-transact-sql?view=sql-server-ver15").

```
par_profile_name varchar = NULL::character varying,
par_recipients text = NULL::text,
par_copy_recipients text = NULL::text,
par_blind_copy_recipients text = NULL::text,
par_subject varchar = NULL::character varying,
par_body text = NULL::text,
par_body_format varchar = NULL::character varying,
par_importance varchar = 'NORMAL'::character varying,
par_sensitivity varchar = 'NORMAL'::character varying,
par_file_attachments text = NULL::text,
par_query text = NULL::text,
par_execute_query_database varchar = NULL::character varying,
par_attach_query_result_as_file smallint = 0,
par_query_attachment_filename varchar = NULL::character varying,
par_query_result_header smallint = 1,
par_query_result_width integer = 256,
par_query_result_separator VARCHAR = ' '::character varying,
par_exclude_query_output smallint = 0,
par_append_query_error smallint = 0,
par_query_no_truncate smallint = 0,
par_query_result_no_padding smallint = 0,
out par_mailitem_id integer,
par_from_address text = NULL::text,
par_reply_to text = NULL::text,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_delete_mailitems_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_delete_mailitems_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-delete-mailitems-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-delete-mailitems-sp-transact-sql?view=sql-server-ver15").

```
par_sent_before timestamp = NULL::timestamp without time zone,
par_sent_status varchar = NULL::character varying,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_add_profile_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_add_profile_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profile-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profile-sp-transact-sql?view=sql-server-ver15").

```
par_profile_name varchar,
par_description varchar = NULL::character varying,
out par_profile_id integer,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_add_account_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_add_account_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-account-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-account-sp-transact-sql?view=sql-server-ver15").

```
par_account_name varchar
par_email_address varchar
par_display_name varchar = NULL::character varying
par_replyto_address varchar = NULL::character varying
par_description varchar = NULL::character varying
par_mailserver_name varchar = NULL::character varying
par_mailserver_type varchar = 'SMTP'::bpchar
par_port integer = 25
par_username varchar = NULL::character varying
par_password varchar = NULL::character varying
par_use_default_credentials smallint = 0
par_enable_ssl smallint = 0
out par_account_id integer
out returncode integer
```

The `aws_sqlserver_ext.sysmail_add_profileaccount_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_add_profileaccount_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profileaccount-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-add-profileaccount-sp-transact-sql?view=sql-server-ver15").

```
par_profile_id integer = NULL::integer,
par_profile_name varchar = NULL::character varying,
par_account_id integer = NULL::integer,
par_account_name varchar = NULL::character varying,
par_sequence_number integer = NULL::integer,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_help_profile_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_help_profile_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-help-profile-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-help-profile-sp-transact-sql?view=sql-server-ver15").

```
par_profile_id integer = NULL::integer,
par_profile_name varchar = NULL::character varying,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_update_profile_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_update_profile_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-update-profile-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-update-profile-sp-transact-sql?view=sql-server-ver15").

```
par_profile_id integer = NULL::integer,
par_profile_name varchar = NULL::character varying,
par_description varchar = NULL::character varying,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_delete_profile_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_delete_profile_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-delete-profile-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-delete-profile-sp-transact-sql?view=sql-server-ver15").

```
par_profile_id integer = NULL::integer,
par_profile_name varchar = NULL::character varying,
par_force_delete smallint = 1,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_help_account_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_help_account_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-help-account-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-help-account-sp-transact-sql?view=sql-server-ver15").

```
par_account_id integer = NULL::integer,
par_account_name varchar = NULL::character varying,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_update_account_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_update_account_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-update-account-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-update-account-sp-transact-sql?view=sql-server-ver15").

```
par_account_id integer = NULL::integer,
par_account_name varchar = NULL::character varying,
par_email_address varchar = NULL::character varying,
par_display_name varchar = NULL::character varying,
par_replyto_address varchar = NULL::character varying,
par_description varchar = NULL::character varying,
par_mailserver_name varchar = NULL::character varying,
par_mailserver_type varchar = NULL::character varying,
par_port integer = NULL::integer,
par_username varchar = NULL::character varying,
par_password varchar = NULL::character varying,
par_use_default_credentials smallint = NULL::smallint,
par_enable_ssl smallint = NULL::smallint,
par_timeout integer = NULL::integer,
par_no_credential_change smallint = NULL::smallint,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_delete_account_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_delete_account_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-delete-account-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-delete-account-sp-transact-sql?view=sql-server-ver15").

```
par_account_id integer = NULL::integer,
par_account_name varchar = NULL::character varying,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_help_profileaccount_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_help_profileaccount_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-help-profileaccount-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-help-profileaccount-sp-transact-sql?view=sql-server-ver15").

```
par_profile_id integer = NULL::integer,
par_profile_name varchar = NULL::character varying,
par_account_id integer = NULL::integer,
par_account_name varchar = NULL::character varying,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_update_profileaccount_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_update_profileaccount_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-update-profileaccount-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-update-profileaccount-sp-transact-sql?view=sql-server-ver15").

```
par_profile_id integer = NULL::integer,
par_profile_name varchar = NULL::character varying,
par_account_id integer = NULL::integer,
par_account_name varchar = NULL::character varying,
par_sequence_number integer = NULL::integer,
out returncode integer
```

The `aws_sqlserver_ext.sysmail_delete_profileaccount_sp` procedure in the extension pack
emulates the `msdb.dbo.sysmail_delete_profileaccount_sp` procedure. For more information
about the source SQL Server Database Mail procedure, see [Microsoft technical documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-delete-profileaccount-sp-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sysmail-delete-profileaccount-sp-transact-sql?view=sql-server-ver15").

```
par_profile_id integer = NULL::integer,
par_profile_name varchar = NULL::character varying,
par_account_id integer = NULL::integer,
par_account_name varchar = NULL::character varying,
out returncode integer
```

## Examples for using procedures

that emulate SQL Server Database Mail in PostgreSQL

To send an email, use the `aws_sqlserver_ext.sp_send_dbmail` procedure
as shown following.

```
PERFORM sp_send_dbmail (
    par_profile_name := 'Administrator',
    par_recipients := 'hello@rusgl.info',
    par_subject := 'Automated Success Message',
    par_body := 'The stored procedure finished'
);
```

The following example shows how to send an email with query results.

```
PERFORM sp_send_dbmail (
    par_profile_name := 'Administrator',
    par_recipients := 'hello@rusgl.info',
    par_subject := 'Account with id = 1',
    par_query := 'SELECT COUNT(*)FROM Account WHERE id = 1'
);
```

The following example shows how to send an email with HTML code.

```
DECLARE var_tableHTML TEXT;
SET var_tableHTML := CONCAT(
    '<H1>Work Order Report</H1>',
    '<table border="1">',
    '<tr><th>Work Order ID</th><th>Product ID</th>',
    '<th>Name</th><th>Order Qty</th><th>Due Date</th>',
    '<th>Expected Revenue</th></tr>',
    '</table>'
);
PERFORM sp_send_dbmail (
    par_recipients := 'hello@rusgl.info',
    par_subject := 'Work Order List',
    par_body := var_tableHTML,
    par_body_format := 'HTML'
);
```

To delete emails, use the `aws_sqlserver_ext.sysmail_delete_mailitems_sp` procedure
as shown following.

```
DECLARE var_GETDATE datetime;
SET var_GETDATE = NOW();
PERFORM sysmail_delete_mailitems_sp (
    par_sent_before := var_GETDATE
);
```

The following example shows how to delete the oldest emails.

```
PERFORM sysmail_delete_mailitems_sp (
    par_sent_before := '31.12.2015'
);
```

The following example shows how to delete all emails that can't be
sent.

```
PERFORM sysmail_delete_mailitems_sp (
    par_sent_status := 'failed'
);
```

To create a new user profile, use
the `aws_sqlserver_ext.sysmail_add_profile_sp` procedure
as shown following.

```
PERFORM sysmail_add_profile_sp (
    profile_name := 'Administrator',
    par_description := 'administrative mail'
);
```

The following example shows how to create a new profile and save the
unique profile identifier in a variable.

```
DECLARE var_profileId INT;
SELECT par_profile_id
    FROM sysmail_add_profile_sp (
        profile_name := 'Administrator',
        par_description := ' Profile used for administrative mail.')
    INTO var_profileId;

SELECT var_profileId;
```

To create a new email account, use
the `aws_sqlserver_ext.sysmail_add_account_sp` procedure
as shown following.

```
PERFORM sysmail_add_account_sp (
    par_account_name :='Audit Account',
    par_email_address := 'dba@rusgl.info',
    par_display_name := 'Test Automated Mailer',
    par_description := 'Account for administrative e-mail.',
    par_mailserver_type := 'AWSLAMBDA'
    par_mailserver_name := 'arn:aws:lambda:us-west-2:555555555555:function:pg_v3'
);
```

To add an email account to the user profile, use
the `aws_sqlserver_ext.sysmail_add_profileaccount_sp` procedure
as shown following.

```
PERFORM sysmail_add_profileaccount_sp (
    par_account_name := 'Administrator',
    par_account_name := 'Audit Account',
    par_sequence_number := 1
);
```

## Use case examples for

emulating SQL Server Database Mail in PostgreSQL

If your source database code uses SQL Server Database Mail to send emails,
you can use the AWS SCT extension pack to convert this code to PostgreSQL.

###### To send an email from your PostgreSQL database

1. Create and configure your AWS Lambda function.
2. Apply the AWS SCT extension pack.
3. Create a user profile using the `sysmail_add_profile_sp`
   function as shown following.
4. Create an email account using the `sysmail_add_account_sp`
   function as shown following.
5. Add this email account to your user profile using
   the `sysmail_add_profileaccount_sp`
   function as shown following.

```
CREATE OR REPLACE FUNCTION aws_sqlserver_ext.
proc_dbmail_settings_msdb()
RETURNS void
AS
$BODY$
BEGIN
PERFORM aws_sqlserver_ext.sysmail_add_profile_sp(
    par_profile_name := 'Administrator',
    par_description := 'administrative mail'
);
PERFORM aws_sqlserver_ext.sysmail_add_account_sp(
    par_account_name := 'Audit Account',
    par_description := 'Account for administrative e-mail.',
    par_email_address := 'dba@rusgl.info',
    par_display_name := 'Test Automated Mailer',
    par_mailserver_type := 'AWSLAMBDA'
    par_mailserver_name := 'your_ARN'
);
PERFORM aws_sqlserver_ext.sysmail_add_profileaccount_sp(
    par_profile_name := 'Administrator',
    par_account_name := 'Audit Account',
    par_sequence_number := 1
);
END;
$BODY$
LANGUAGE plpgsql;
```

6. Send an email using the `sp_send_dbmail` function
   as shown following.

```
CREATE OR REPLACE FUNCTION aws_sqlserver_ext.
proc_dbmail_send_msdb()
RETURNS void
AS
$BODY$
BEGIN
PERFORM aws_sqlserver_ext.sp_send_dbmail(
    par_profile_name := 'Administrator',
    par_recipients := 'hello@rusgl.info',
    par_body := 'The stored procedure finished',
    par_subject := 'Automated Success Message'
);
END;
$BODY$
LANGUAGE plpgsql;
```

To view the information about all user profiles, use the
`sysmail_help_profile_sp` procedure as shown following.

```
SELECT FROM aws_sqlserver_ext.sysmail_help_profile_sp();
```

The following example displays the information about the specific user
profile.

```
select from aws_sqlserver_ext.sysmail_help_profile_sp(par_profile_id := 1);
select from aws_sqlserver_ext.sysmail_help_profile_sp(par_profile_name := 'Administrator');
```

To view the information about all email accounts, use the
`sysmail_help_account_sp` procedure as shown following.

```
select from aws_sqlserver_ext.sysmail_help_account_sp();
```

The following example displays the information about the specific email
account.

```
select from aws_sqlserver_ext.sysmail_help_account_sp(par_account_id := 1);
select from aws_sqlserver_ext.sysmail_help_account_sp(par_account_name := 'Audit Account');
```

To view the information about all email accounts that are associated with the
user profiles, use the `sysmail_help_profileaccount_sp` procedure as
shown following.

```
select from aws_sqlserver_ext.sysmail_help_profileaccount_sp();
```

The following example filters the records by identifier, profile name, or
account name.

```
select from aws_sqlserver_ext.sysmail_help_profileaccount_sp(par_profile_id := 1);
select from aws_sqlserver_ext.sysmail_help_profileaccount_sp(par_profile_id := 1, par_account_id := 1);
select from aws_sqlserver_ext.sysmail_help_profileaccount_sp(par_profile_name := 'Administrator');
select from aws_sqlserver_ext.sysmail_help_profileaccount_sp(par_account_name := 'Audit Account');
```

To change the user profile name or description, use the
`sysmail_update_profile_sp` procedure as shown following.

```
select aws_sqlserver_ext.sysmail_update_profile_sp(
    par_profile_id := 2,
    par_profile_name := 'New profile name'
);
```

To change the email account settings, use the
`ysmail_update_account_sp` procedure as shown following.

```
select from aws_sqlserver_ext.sysmail_update_account_sp (
    par_account_name := 'Audit Account',
    par_mailserver_name := 'arn:aws:lambda:region:XXXXXXXXXXXX:function:func_test',
    par_mailserver_type := 'AWSLAMBDA'
);
```
