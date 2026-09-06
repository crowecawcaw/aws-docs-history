

# Oracle Advanced Queuing and MySQL integration with Lambda
<a name="chap-oracle-aurora-mysql.special.lambda"></a>

With AWS DMS, you can seamlessly migrate data from Oracle Advanced Queuing to Aurora MySQL, and integrate with AWS Lambda for event-driven processing. Oracle Advanced Queuing provides message queuing capabilities for Oracle databases, while AWS Lambda allows running code without provisioning or managing servers.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-1.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  | N/A | Use AWS Lambda and Amazon Simple Queue Service with Aurora MySQL. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.special.lambda.oracle"></a>

The Oracle Advanced Queuing (AQ) feature enables database-integrated message queuing functionality. It is based on Oracle Streams and optimizes data functions by storing messages, allocating the messages to different service queues, and transmitting the messages using Oracle Net Services, HTTP, and HTTPS. AQ is implemented using database tables.

Oracle provides the `oracle.jdbc.aq` Java package as an interface to AQ. It contains the following items:
+ Classes:
  +  `AQDequeueOptions` — Specifies the options for the dequeue operation.
  +  `AQEnqueueOptions` — Specifies the options for the enqueue operation.
  +  `AQFactory` — A factory class for AQ, which creates components such as agent or message properties.
  +  `AQNotificationEvent` — New message notifications.
+ Interfaces:
  +  `AQAgent` — An identity of a user, producer, or consumer of a message.
  +  `AQMessage` — An enqueued or dequeued message.
  +  `AQMessageProperties` — Message properties such as:
    + Correlation
    + Sender
    + Delay
    + Expiration
    + Recipients
    + Priority
    + Ordering
+  `AQNotificationListener` — A listener interface for receiving AQ notification events.
+  `AQNotificationRegistration` — A registration to be notified when a new message is enqueued on a particular queue.

For more information, see [Introduction to Oracle Database Advanced Queuing](https://docs.oracle.com/en/database/oracle/oracle-database/19/adque/aq-introduction.html#GUID-95868022-ECDA-4685-9D0A-52ED7663C84B) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.special.lambda.mysql"></a>

 Aurora MySQL provides built-in integration with Lambda functions, which can be called from within the database and interact with Amazon Simple Notification Service (Amazon SNS). The integration with Lambda functions provides a powerful framework for using AWS services to implement custom solutions with less code.

### Examples
<a name="chap-oracle-aurora-mysql.special.lambda.mysql.examples"></a>

For examples, see [Amazon Simple Notification Service](chap-oracle-aurora-mysql.sql.mail.md).

For more information, see [Invoking a Lambda function with an Aurora MySQL native function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html#AuroraMySQL.Integrating.NativeLambda) in the *User Guide for Aurora*.