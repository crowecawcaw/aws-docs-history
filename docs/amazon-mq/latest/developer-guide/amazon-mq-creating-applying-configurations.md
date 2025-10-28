# Creating an Amazon MQ for ActiveMQ broker configuration

A _configuration_ contains all of the settings for your ActiveMQ broker, in XML format (similar to ActiveMQ's `activemq.xml` file). You can create a configuration before creating any brokers. You can then apply the configuration to one or more brokers. You can apply a configuration immediately or during a _maintenance window_.

The following example shows how you can create and apply an Amazon MQ broker
configuration using the AWS Management Console.

###### Important

You can only **delete**
a configuration using the `DeleteConfiguration` API.
For more information,
see [Configurations](../api-reference/configurations-configuration-id.md "../api-reference/configurations-configuration-id.md")
in the _Amazon MQ API Reference_.

## Create a New

Configuration

To create a new broker configuration, first create the new configuration.

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. On the left, expand the navigation panel and choose
   **Configurations**.

![Amazon MQ navigation panel showing Brokers and Configurations options.](images/amazon-mq-tutorials-create-configuration.png) 3. On the **Configurations** page, choose
**Create configuration**. 4. On the **Create configuration** page, in the
**Details** section, type the
**Configuration name** (for example,
`MyConfiguration`) and select a **Broker
engine** version.

###### Note

To learn more about ActiveMQ engine versions supported by Amazon MQ for ActiveMQ, see [Managing Amazon MQ for ActiveMQ engine versions](activemq-version-management.md "activemq-version-management.md"). 5. Choose **Create configuration**.

## Create a New

Configuration Revision

After you create a broker configuration, you will need to edit the configuration
using a configuration revision.

1. From the configuration list, choose
   **`MyConfiguration`**.

###### Note

The first configuration revision is always created for you when
Amazon MQ creates the configuration.

On the **`MyConfiguration`**
page, the broker engine type and version that your new configuration
revision uses (for example, **Apache ActiveMQ
5.15.16**) are displayed. 2. On the **Configuration details** tab, the configuration
revision number, description, and broker configuration in XML format are displayed.

###### Note

Editing the current configuration creates a new configuration revision.

![XML configuration snippet for ActiveMQ broker with explanatory comment.](images/amazon-mq-tutorials-edit-configuration.png) 3. Choose **Edit configuration** and make changes to the XML configuration. 4. Choose **Save**.

The **Save revision** dialog box is displayed. 5. (Optional) Type `A description of the changes in this revision`. 6. Choose **Save**.

The new revision of the configuration is saved.

###### Important

The Amazon MQ console automatically sanitizes invalid and prohibited configuration parameters according to a schema.
For more information and a full list of permitted XML parameters, see [Amazon MQ Broker Configuration Parameters](amazon-mq-broker-configuration-parameters.md "amazon-mq-broker-configuration-parameters.md").

## Apply a

Configuration Revision to Your Broker

After revising the configuration, you can apply the configuration
revision to your broker.

1. On the left, expand the navigation panel and choose
   **Brokers**.

![Amazon MQ navigation panel showing Brokers and Configurations options.](images/amazon-mq-tutorials-apply-configuration.png) 2. From the broker list, select your broker (for example, **MyBroker**) and then choose **Edit**. 3. On the **Edit `MyBroker`** page, in the
**Configuration** section, select a **Configuration**
and a **Revision** and then choose **Schedule Modifications**. 4. In the **Schedule broker modifications** section, choose whether to apply modifications
**During the next scheduled maintenance window** or **Immediately**.

###### Important

Single instance brokers are offline while being rebooted. For cluster brokers,
only one node is down at a time while the broker reboots. 5. Choose **Apply**.

Your configuration revision is applied to your
broker at the specified time.
