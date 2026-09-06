

# Oracle UTL\_MAIL or UTL\_SMTP and Amazon Simple Notification Service
<a name="chap-oracle-aurora-mysql.sql.mail"></a>

With AWS DMS, you can migrate email functionality from Oracle databases to Amazon Simple Notification Service (Amazon SNS). Oracle `UTL_MAIL` and `UTL_SMTP` packages provide database email capabilities, which AWS Database Migration Service can help you transition to the fully managed Amazon SNS service. The following sections detail the process of replicating Oracle `UTL_MAIL/UTL_SMTP` functionality using Amazon SNS with AWS DMS.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  | N/A | Use Lambda integration. | 

## Oracle UTL\_MAIL usage
<a name="chap-oracle-aurora-mysql.sql.mail.oracle"></a>

The Oracle `UTL_MAIL` package provides functionality for sending email messages. Unlike `UTL_SMTP`, which is more complex and provided in earlier versions of Oracle, `UTL_MAIL` supports attachments. For most cases, `UTL_MAIL` is a better choice.

### Examples
<a name="chap-oracle-aurora-mysql.sql.mail.oracle.examples"></a>

Install the required mail packages.

```
@{ORACLE_HOME}/rdbms/admin/utlmail.sql
@{ORACLE_HOME}/rdbms/admin/prvtmail.plb
```

Set the `smtp_out_server` parameter.

```
ALTER SYSTEM SET smtp_out_server = 'smtp.domain.com' SCOPE=BOTH;
```

Send an email message.

```
exec utl_mail.send('Sender@mailserver.com', 'recipient@mailserver.com', NULL, NULL, 'This is the subject', 'This is the message body', NULL, 3, NULL);
```

For more information, see [UTL\_MAIL](https://docs.oracle.com/database/121/ARPLS/u_mail.htm#ARPLS384) in the *Oracle documentation*.

## Oracle UTL\_SMTP usage
<a name="chap-oracle-aurora-mysql.sql.mail.orasmtp"></a>

The Oracle `UTL_SMTP` package provides functionality for sending email messages and is useful for sending alerts about database events. Unlike `UTL_MAIL`, UTL `SMTP` is more complex and doesn’t support attachments. For most cases, `UTL_MAIL` is a better choice.

### Examples
<a name="chap-oracle-aurora-mysql.sql.mail.orasmtp.examples"></a>

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
+  `UTL_SMTP.OPEN_CONNECTION` opens a connection to the smtp server.
+  `UTL_SMTP.HELO` initiates a handshake with the smtp server.
+  `UTL_SMTP.MAIL` Initiates a mail transaction that obtains the senders details.
+  `UTL_SMTP.RCPT` adds a recipient to the mail transaction.
+  `UTL_SMTP.DATA` adds the message content.
+  `UTL_SMTP.QUIT` terminates the SMTP transaction.

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

For more information, see [Managing Resources with Oracle Database Resource Manager](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-resources-with-oracle-database-resource-manager.html#GUID-2BEF5482-CF97-4A85-BD90-9195E41E74EF) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.mail.mysql"></a>

Aurora MySQL does not support direct configuration of engine alerts. Use the Event Notifications Infrastructure to collect history logs or receive event notifications in near real-time.

The Amazon Relational Database Service (Amazon RDS) uses the Amazon Simple Notification Service (Amazon SNS) to provide notifications for events. Amazon SNS can send notifications in any form supported by the region including email, text messages, or calls to HTTP endpoints for response automation.

Events are grouped into categories. You can only subscribe to event categories, not individual events. SNS sends notifications when any event in a category occurs.

You can subscribe to alerts for database instances, database clusters, database snapshots, database cluster snapshots, database security groups, and database parameter groups. For example, a subscription to the Backup category for a specific database instance sends notifications when backup-related events occur on that instance. A subscription to the Configuration Change category for a database security group sends notifications when the security group changes.

**Note**  
For Amazon Aurora, some events occur at the cluster rather than instance level. You will not receive those events if you subscribe to an Aurora DB instance.

Amazon SNS sends event notifications to the address specified when the subscription was created. Typically, administrators create several subscriptions. For example, one subscription to receive logging events and another to receive only critical events for a production environment requiring immediate responses.

You can disable notifications without deleting a subscription by setting the Enabled radio button to No in the Amazon RDS console. Alternatively, use the AWS Command Line Interface (CLI) or Amazon RDS API to change the Enabled setting.

Subscriptions are identified by the Amazon Resource Name (ARN) of an Amazon SNS topic. The Amazon RDS console creates ARNs when subscriptions are created. When using the CLI or API, you must create the ARN using the Amazon SNS console or the Amazon SNS API.

### Examples
<a name="chap-oracle-aurora-mysql.sql.mail.mysql.examples"></a>

The following walkthrough demonstrates how to create an Event Notification Subscription:

1. Sign in to the AWS Management Console and choose **RDS**.

1. Choose **Events**. If you have not previously subscribed to events, the screen displays zero events.

1. Choose **Event subscriptions**, and then choose **Create event subscription**.

1. For **Name**, enter the name of the subscription.

1. For **Target**, choose **ARN** or **New email topic**. For email subscriptions, enter values for **Topic name** and **With these recipients**.

1. Choose the event source and then choose specific event categories to be monitored from the drop-down menu.

1. Choose **Create**.

1. On the Amazon RDS dashboard, choose **Recent events**.

For more information, see [Working with Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html) in the *Amazon Relational Database Service User Guide*.

For application email requirements, consider using a dedicated email framework. If the code generating email messages must reside in the database, consider using a queue table. Replace all occurrences of `UTL_SMTP` and `UTL_MAIL` with an `INSERT` into the queue table. Design external applications to connect, read the queue, send an email message, and then update the status periodically. With this approach, messages can be populated with a query result similar to `UTL_SMTP` and `UTL_MAIL` with the query option.

The only way to send email from the database is to use AWS Lambda integration. For more information about AWS Lambda, see [AWS Lambda](https://aws.amazon.com/lambda).

For an example of sending an email message from Aurora MySQL using AWS Lambda integration, see [Invoking a Lambda Function from an Amazon Aurora MySQL DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html).