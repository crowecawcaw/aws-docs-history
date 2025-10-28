# Creating an Amazon MQ cross-Region data replication broker

With Cross-Region data replication (CRDR), you can switch between Amazon MQ for ActiveMQ message brokers in two AWS Regions as needed.
You can designate an existing broker as a primary broker and create a replica for this broker, or create a new primary and replica broker together.
You can then promote the replica broker to the primary broker role using the Amazon MQ `Promote` API operation.
For more information about primary and replica brokers, see [Primary and replica brokers for cross-Region data replication](crdr-for-active-mq.md#crdr-primary-replica-brokers "crdr-for-active-mq.md#crdr-primary-replica-brokers").

The following instructions describe how you can create and configure a replica broker using the Amazon MQ Management Console.

###### Topics

- [Prerequisites](#create-crdr-broker-prerequisites "#create-crdr-broker-prerequisites")
- [Step 1 (Optional): Create a new primary broker](#create-new-primary-broker "#create-new-primary-broker")
- [Step 2: Create a replica of an existing broker](#create-new-replica-broker "#create-new-replica-broker")

## Prerequisites

To use the cross-Region data replication feature, you must review and comply with the following prerequisites:

- **Version**: The cross-Region data replication feature is only available
  for Amazon MQ for ActiveMQ brokers on versions 5.17.6 and above.
- **Region**: Cross-Region data replication is supported in the following regions:
  US East (Ohio), US East (N. Virginia), US West (Oregon), and US West (N. California).
- **Instance type**: Cross-Region data replication is only available for
  broker instance sizes `mq.m5.large` and above.
- **Deployment type**: Cross-Region data replication is only available
  for active/standby brokers
  with multi-availability zone deployment.
- **Broker status**: You can only create a replica broker
  for a primary broker with the broker status `Running`.

## Step 1 (Optional): Create a new primary broker

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. On the Brokers page of the Amazon MQ console, choose **Create brokers**.
3. On the **Select broker engine** page, choose **Apache ActiveMQ**.
4. On the **Select deployment and storage** page,
   in the **Deployment mode and storage type** section, do the following:
   1. For the **Deployment mode**, choose **Active/standby broker**.
      An **Active/standby broker** is comprised of two brokers in two different Availability Zones configured in a redundant pair.
      These brokers communicate synchronously with your application and with Amazon EFS. For more information, see
      [Deployment options for Amazon MQ for ActiveMQ brokers](amazon-mq-broker-architecture.md "amazon-mq-broker-architecture.md").

5. Choose **Next**.
6. On the **Configure settings** page, in the **Details** section, do the following:
   1. Enter the **Broker name**.

   ###### Important

   Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names.
   Broker names are accessible to other AWS services, including CloudWatch Logs. Broker names are not intended to be used for
   private or sensitive data. 2. Choose the **Broker instance type** (for example, **mq.m5.large**). For more information, see
   [Broker instance types](broker-instance-types.md "broker-instance-types.md").

7. In the **ActiveMQ Web Console access** section, provide a **Username**
   and **Password**. The following restrictions apply to broker usernames and passwords:
   - Your username can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ ~).
   - Your password must be at least 12 characters long, contain at least 4 unique characters and must not contain commas, colons, or equal signs (,:=).

###### Important

Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames.
Broker usernames are accessible to other AWS services, including CloudWatch Logs. Broker usernames are not intended to be used for
private or sensitive data.
The green flash bar at the top of the page confirms that Amazon MQ is creating the replica broker in the recovery Region.
You can also see the CRDR role and RPO status for your brokers. To turn off the CRDR Role and RPO Status columns,
choose the gear icon in the top right corner of the **Brokers** table.
Then, on the **Preferences** page, turn off CRDR Role or RPO Status.

## Step 2: Create a replica of an existing broker

1. On the Brokers page of the Amazon MQ console, choose **Create replica broker**.
2. On the **Choose primary broker page**, select an existing broker to use as a CRDR primary broker. Then, choose **Next**.
3. On the **Configure replica broker** page, use the drop down menu to choose the replica Region.
4. In the **ActiveMQ console user for replica broker** section, provide a **Username**
   and **Password** for the replica broker console user. The following restrictions apply to broker usernames and passwords:
   - Your username can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ ~).
   - Your password must be at least 12 characters long, contain at least 4 unique characters and must not contain commas, colons, or equal signs (,:=).

###### Important

Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames.
Broker usernames are accessible to other AWS services, including CloudWatch Logs. Broker usernames are not intended to be used for
private or sensitive data. 5. In the **Data replication user to bridge access between brokers** section, provide a **Username**
and **Password** for the user that will access both the primary and replica broker. The following restrictions apply to broker usernames and passwords:

    * Your username can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ ~).
    * Your password must be at least 12 characters long, contain at least 4 unique characters and must not contain commas, colons, or equal signs (,:=).

###### Important

Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames.
Broker usernames are accessible to other AWS services, including CloudWatch Logs. Broker usernames are not intended to be used for
private or sensitive data.

Configure any additional settings. Then, choose **Next**. 6. On the **Review and create** page, review the replica broker details. Then, choose **Create replica broker**. 7. Next, reboot the primary broker. This will also reboot the replica broker.
For instructions on rebooting your broker, see [Rebooting a Broker](amazon-mq-rebooting-broker.md "amazon-mq-rebooting-broker.md").

For more information on configuring additional settings for your ActiveMQ broker, see [Getting started: Creating and connecting to an ActiveMQ broker](getting-started-activemq.md "getting-started-activemq.md")
