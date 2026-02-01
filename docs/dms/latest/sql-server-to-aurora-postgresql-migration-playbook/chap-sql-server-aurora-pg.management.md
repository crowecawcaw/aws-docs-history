# Database mail features

This topic provides reference information about email capabilities in Microsoft SQL Server and their counterparts in Amazon Aurora PostgreSQL. You can understand the differences in email functionality between these two database systems and learn about alternative solutions for sending emails from Aurora PostgreSQL.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                  | Key differences         |
| ------------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| One star feature compatibility | N/A                                | [SQL Server Mail](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.mail "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.mail") | Use Lambda integration. |

## SQL Server Usage

The Database Mail framework is an email client solution for sending messages directly from SQL Server. Email capabilities and APIs within the database server provide easy management of the following messages:

- Server administration messages such as alerts, logs, status reports, and process confirmations.
- Application messages such as user registration confirmation and action verifications.

###### Note

Database Mail is turned off by default.

The main features of the Database Mail framework are:

- Database Mail sends messages using the standard and secure Simple Mail Transfer Protocol (SMTP) .
- The email client engine runs asynchronously and sends messages in a separate process to minimize dependencies.
- Database Mail supports multiple SMTP Servers for redundancy.
- Full support and awareness of Windows Server Failover Cluster for high availability environments.
- Multi-profile support with multiple failover accounts in each profile.
- Enhanced security management with separate roles in the `msdb` database.
- Security is enforced for mail profiles.
- Administrators can monitor and cap attachment sizes.
- You can add attachment file types to a deny list.
- You can log Email activity to SQL Server, the Windows application event log, and a set of system tables in the `msdb` database.
- Supports full auditing capabilities with configurable retention policies.
- Supports both plain text and HTML messages.

### Architecture

Database Mail is built on top of the Microsoft SQL Server Service Broker queue management framework.

The system stored procedure `sp_send_dbmail` sends email messages. When you run this stored procedure, it inserts a row to the mail queue and records the Email message.

The queue insert operation triggers the run of the Database Mail process (`DatabaseMail.exe`). The Database Mail process then reads the Email information and sends the message to the SMTP servers.

When the SMTP servers acknowledge or reject the message, the Database Mail process inserts a status row into the status queue, including the result of the send attempt. This insert operation triggers the run of a system stored procedure that updates the status of the Email message send attempt.

Database Mail records all Email attachments in the system tables. SQL Server provides a set of system views and stored procedures for troubleshooting and administration of the Database Mail queue.

### Deprecated SQL Mail framework

The previous SQL Mail framework using `xp_sendmail` has been deprecated as of SQL Server 2008R2. For more information, see [Deprecated Database Engine Features in SQL Server 2008 R2](<https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)> "https://docs.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms143729(v=sql.105)") in the _SQL Server documentation_.

The legacy mail system has been completely replaced by the greatly enhanced DB mail framework described here. The previous system has been out of use for many years because it was prone to synchronous run issues and windows mail profile quirks.

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

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) doesn’t provide native support for sending email message from the database. For alerting purposes, use the Event Notification Subscription feature to send email notifications to operators. For more information, see [Alerting](chap-sql-server-aurora-pg.management.md "chap-sql-server-aurora-pg.management.md").

The only way to send an Email from the database is to use AWS Lambda integration. For more information, see [AWS Lambda](https://aws.amazon.com/lambda "https://aws.amazon.com/lambda").

### Examples

The following walkthrough shows how to send an Email from Aurora PostgreSQL using AWS Lambda integration.

First, configure Amazon Simple Email Service (Amazon SES). For more information, see [What is Amazon SES?](../../../ses/latest/dg/Welcome.md "../../../ses/latest/dg/Welcome.md") in the _Amazon Simple Email Service Developer Guide_.

1. In the AWS console, choose **SES**, **SMTP Settings**, and then choose **Create My SMTP Credentials**. Copy the SMTP server name, which you will use in the AWS Lambda function.
2. For **IAM User Name**, enter the SMTP user name, and then choose **Create**.
3. Save the credentials, which you will use to authenticate with the SMTP server. After you leave this page, you can’t retrieve these credentials.
4. In the AWS console, choose **SES**, **Email Addresses**, and then choose **Verify a New Email Address**. Before you send emails, verify the email address.
5. After you verify the email, create a table to store messages to be sent by the AWS Lambda function.

```
CREATE TABLE emails (title varchar(600), body varchar(600), recipients varchar(600));
```

6. In the AWS console, choose **Lambda**, and then choose **Create function**.
7. Select **Author from scratch**, enter a name for your project, and select Python 2.7 as the runtime. Make sure that you use a role with the correct permissions. Choose **Create function**.
8. Download this [GitHub project](https://github.com/alexcasalboni/awslambda-psycopg2 "https://github.com/alexcasalboni/awslambda-psycopg2").
9. In your local environment, create two files: `main.py` and `db_util.py`. Copy and paste the following content into these files. Make sure that you replace the code placeholders with values for your environment.

**main.py**

```
#!/usr/bin/python
import sys
import logging
import psycopg2

from db_util import make_conn, fetch_data
def lambda_handler(event, context):
    query_cmd = "select * from mails"
    print query_cmd

    # get a connection, if a connect can't be made an exception will be raised here
    conn = make_conn()

    result = fetch_data(conn, query_cmd)
    conn.close()

    return result
```

**db_util.py:**

```
#!/usr/bin/python
import psycopg2
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

db_host = 'YOUR_RDS_HOST'
db_port = 'YOUR_RDS_PORT'
db_name = 'YOUR_RDS_DBNAME'
db_user = 'YOUR_RDS_USER'
db_pass = 'YOUR_RDS_PASSWORD'

def sendEmail(recp, sub, message):
    # Replace sender@example.com with your "From" address.
    # This address must be verified.
    SENDER = 'PUT HERE THE VERIFIED EMAIL'
    SENDERNAME = 'Lambda'

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = recp

    # Replace smtp_username with your Amazon SES SMTP user name.
    USERNAME_SMTP = "YOUR_SMTP_USERNAME"

    # Replace smtp_password with your Amazon SES SMTP password.
    PASSWORD_SMTP = "YOUR_SMTP PASSWORD"

    # (Optional) the name of a configuration set to use for this message.
    # If you comment out this line, you also need to remove or comment out
    # the "X-SES-CONFIGURATION-SET:" header.
    CONFIGURATION_SET = "ConfigSet"

    # If you're using Amazon SES in a region other than US West (Oregon),
    # replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP
    # endpoint in the appropriate region.
    HOST = "YOUR_SMTP_SERVERNAME"
    PORT = 587

    # The subject line of the email.
    SUBJECT = sub

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Test\r\n"
        "This email was sent through the Amazon SES SMTP "
        "Interface using the Python smtplib package."
    )

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>Amazon SES SMTP Email Test</h1>""" + message + """</body>
    </html>
        """

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    msg['To'] = RECIPIENT
    # Comment or delete the next line if you aren't using a configuration set
    #msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Try to send the message.
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        #stmplib docs recommend calling ehlo() before & after starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()

    # Display an error message if something goes wrong.
    except Exception as e:
        print ("Error: ", e)
    else:
        print ("Email sent!")

def make_conn():
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print "I am unable to connect to the database"
    return conn

def fetch_data(conn, query):
    result = []
    print "Now running: %s" % (query)
    cursor = conn.cursor()
    cursor.execute(query)

    print("Number of new mails to be sent: ", cursor.rowcount)

    raw = cursor.fetchall()

    for line in raw:
        print(line[0])
        sendEmail(line[2],line[0],line[1])
        result.append(line)

    cursor.execute('delete from mails')
    cursor.execute('commit')

    return result
```

###### Note

In the body of `db_util.py`, AWS Lambda deletes the content of the mails table. 10. Place the `main.py` and `db_util.py` files inside the GitHub extracted folder and create a new archive file using the ZIP file format that includes your two new files. 11. Return to your Lambda project and change the **Code entry type** to **Upload a .ZIP file**, change the Handler to `mail.lambda_handler`, and upload the file. Choose Save. 12. To test the lambda function, choose **Test** and enter the **Event name**.

###### Note

You can trigger the AWS Lambda function by multiple options. This walkthrough demonstrates how to schedule it to run every minute. Remember, you are paying for each AWS Lambda run. 13. To create a scheduled trigger, use Amazon CloudWatch, enter all details, and choose **Add**.

###### Note

This example runs every minute, but you can use a different interval. For more information, see [Schedule expressions using rate or cron](../../../lambda/latest/dg/services-cloudwatchevents-expressions.md "../../../lambda/latest/dg/services-cloudwatchevents-expressions.md"). 14. Choose **Save**.
