# Oracle UTL_MAIL or UTL_SMTP and PostgreSQL Scheduled Lambda with Amazon SES

With AWS DMS, you can configure email notifications for migration tasks using Oracle `UTL_MAIL` or `UTL_SMTP` and PostgreSQL scheduled Lambda with Amazon Simple Email Service (Amazon SES). `UTL_MAIL` and `UTL_SMTP` are Oracle database packages that provide an interface to send emails, while scheduled Lambda with Amazon SES allows sending emails from a PostgreSQL database using AWS Lambda and Amazon SES.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences         |
| -------------------------------- | ---------------------------------- | ------------------------- | ----------------------- |
| Three star feature compatibility | No automation                      | N/A                       | Use Lambda integration. |

## Oracle UTL_MAIL usage

The Oracle `UTL_MAIL` package provides functionality for sending email messages. Unlike `UTL_SMTP`, which is more complex and provided in earlier versions of Oracle, `UTL_MAIL` supports attachments. For most cases, `UTL_MAIL` is a better choice.

**Examples**

Install the required mail packages.

```
@{ORACLE_HOME}/rdbms/admin/utlmail.sql
@{ORACLE_HOME}/rdbms/admin/prvtmail.plb
```

Set the smtp_out_server parameter.

```
ALTER SYSTEM SET smtp_out_server = 'smtp.domain.com' SCOPE=BOTH;
```

Send an email message.

```
exec utl_mail.send('Sender@mailserver.com', 'recipient@mailserver.com', NULL, NULL, 'This is the subject', 'This is the message body', NULL, 3, NULL);
```

For more information, see [UTL_MAIL](https://docs.oracle.com/database/121/ARPLS/u_mail.htm#ARPLS384 "https://docs.oracle.com/database/121/ARPLS/u_mail.htm#ARPLS384") in the _Oracle documentation_.

## Oracle UTL_SMTP usage

The Oracle `UTL_SMTP` package provides functionality for sending email messages and is useful for sending alerts about database events. Unlike `UTL_MAIL`, UTL `SMTP` is more complex and doesn’t support attachments. For most cases, `UTL_MAIL` is a better choice.

**Examples**

The following example demonstrates using `UTL_SMTP` procedures to send email messages.

Install the required scripts.

```
In oracle 12c:
@{ORACLE_HOME}/rdbms/admin/utlsmtp.sql

In oracle 11g:
@{ORACLE_HOME}/javavm/install/initjvm.sql
@{ORACLE_HOME}/rdbms/admin/initplsj.sql
```

Create and send an email message.

- `UTL_SMTP.OPEN_CONNECTION` opens a connection to the smtp server.
- `UTL_SMTP.HELO` initiates a handshake with the smtp server.
- `UTL_SMTP.MAIL` Initiates a mail transaction that obtains the senders details.
- `UTL_SMTP.RCPT` adds a recipient to the mail transaction.
- `UTL_SMTP.DATA` adds the message content.
- `UTL_SMTP.QUIT` terminates the SMTP transaction.

```
DECLARE
smtpconn utl_smtp.connection;
BEGIN
smtpconn := UTL_SMTP.OPEN_CONNECTION('smtp.mailserver.com', 25);
UTL_SMTP.HELO(smtpconn, 'smtp.mailserver.com');
UTL_SMTP.MAIL(smtpconn, 'sender@mailserver.com');
UTL_SMTP.RCPT(smtpconn, 'recipient@mailserver.com');
UTL_SMTP.DATA(smtpconn,'Message body');
UTL_SMTP.QUIT(smtpconn);
END;
/
```

For more information, see [Managing Resources with Oracle Database Resource Manager](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-resources-with-oracle-database-resource-manager.html#GUID-2BEF5482-CF97-4A85-BD90-9195E41E74EF "https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-resources-with-oracle-database-resource-manager.html#GUID-2BEF5482-CF97-4A85-BD90-9195E41E74EF") in the _Oracle documentation_.

## PostgreSQL usage

Amazon Aurora PostgreSQL doesn’t provide native support for sending email message from the database. For alerting purposes, use the Event Notification Subscription feature to send email notifications to operators.

The only way to send Email from the database is to use the AWS Lambda integration. For more information, see [AWS Lambda](https://aws.amazon.com/lambda "https://aws.amazon.com/lambda").

**Examples**

Sending an Email from Aurora PostgreSQL using Lambda integration.

First, configure [Amazon Simple Email Service (Amazon SES)](../../../ses/latest/dg/Welcome.md "../../../ses/latest/dg/Welcome.md").

In the AWS console, choose **SES**, **SMTP Settings**, and choose **Create My SMTP Credentials**. Note the SMTP server name; you will use it in the Lambda function.

Enter a name for IAM User Name (SMTP user) and choose **Create**.

Note the credentials; you will use them to authenticate with the SMTP server.

###### Note

After you leave this page, you can’t retrieve the credentials.

On the SES page, choose **Email addresses** on the left, and choose **Verify a new email address**. Before sending email, they must be verified.

The next page indicates that the email is pending verification.

After you verified the email, create a table to store messages to be sent by the Lambda fuction.

```
CREATE TABLE emails (title varchar(600), body varchar(600), recipients varchar(600));
```

To create the Lambda function, navigate to the [Lambda page](https://console.aws.amazon.com/lambda/home "https://console.aws.amazon.com/lambda/home") in the AWS Console, and choose **Create function**.

Choose **Author from scratch**, enter a name for your project, and select Python 2.7 as the runtime. Make sure that you use a role with the correct permissions. Choose **Create function**.

Download this [GitHub project](https://github.com/alexcasalboni/awslambda-psycopg2 "https://github.com/alexcasalboni/awslambda-psycopg2").

In your local environment, create two files: main.py and db_util.py. Cut and paste the following content into `main.py` and `db_util.py` respectively. Replace the placeholders in the code with values for your environment.

main.py:

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

db_util.py:

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
  SENDERNAME = 'Lambda

  # Replace recipient@example.com with a "To" address. If your account
  # is still in the sandbox, this address must be verified.
  RECIPIENT = recp

  # Replace smtp_username with your Amazon SES SMTP user name.
  USERNAME_SMTP = "YOUR_SMTP_USERNAME"

  # Replace smtp_password with your Amazon SES SMTP password.
  PASSWORD_SMTP = "YOUR_SMTP PASSWORD"

  # (Optional) the name of a configuration set to use for this message.
  # If you comment out this line, you also need to remove or comment out
  # the "X-SES-CONFIGURATION-SET:" header below.
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
      conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" %
      (db_name, db_user, db_host, db_pass))
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

In the body of db_util.py, Lambda deletes the content of the mails table.

Place the `main.py` and `db_util.py` files inside the Github extracted folder and create a new zipfile that includes your two new files.

Return to your Lambda project and change the **Code entry type** to **Upload a .ZIP file**, change the **Handler** to **mail.lambda_handler**, and upload the file. Then choose **Save**.

To test the Lambda function, choose **Test** and enter the **Event name**.

###### Note

The Lambda function can be triggered by multiple options. This walkthrough demonstrates how to schedule it to run every minute. Remember, you are paying for each Lambda execution.

To create a scheduled trigger, use Amazon CloudWatch, enter all details, and choose **Add**.

###### Note

This example runs every minute, but you can use a different interval. For more information, see [Schedule expressions using rate or cron](../../../lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.md "../../../lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.md").

Choose **Save**.
