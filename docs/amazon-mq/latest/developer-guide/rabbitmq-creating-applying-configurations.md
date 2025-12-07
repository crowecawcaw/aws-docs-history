# Creating and applying RabbitMQ broker configurations

A _configuration_ contains all of the settings for your RabbitMQ broker in Cuttlefish format. You can create a configuration before creating any brokers. You can then apply the configuration to one or more brokers

The following examples show how you can create and apply a RabbitMQ broker configuration
using the AWS Management Console.

###### Important

You can only **delete**
a configuration using the `DeleteConfiguration` API.
For more information,
see [Configurations](../api-reference/configurations-configuration-id.md "../api-reference/configurations-configuration-id.md")
in the _Amazon MQ API Reference_.

## Create a New Configuration

To apply a configuration to your broker, you must first create the configuration.

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. On the left, expand the navigation panel and choose
   **Configurations**.

![Amazon MQ navigation panel showing Brokers and Configurations options.](/images/amazon-mq/latest/developer-guide/images/amazon-mq-tutorials-create-configuration.png) 3. On the **Configurations** page, choose **Create
configuration**. 4. On the **Create configuration** page, in the
**Details** section, type the **Configuration
name** (for example, `MyConfiguration`) and select a
**Broker engine** version.

To learn more about RabbitMQ engine versions supported by Amazon MQ for RabbitMQ, see [Managing Amazon MQ for RabbitMQ engine versions](rabbitmq-version-management.md "rabbitmq-version-management.md"). 5. Choose **Create configuration**.

## Create a New

Configuration Revision

After you create a configuration, you must edit the configuration using
a configuration revision.

1. From the configuration list, choose
   **`MyConfiguration`**.

###### Note

The first configuration revision is always created for you when Amazon MQ
creates the configuration.

On the **`MyConfiguration`**
page, the broker engine type and version that your new configuration
revision uses (for example, **RabbitMQ 3.xx.xx**) are
displayed. 2. On the **Configuration details** tab, the configuration
revision number, description, and broker configuration in Cuttlefish format are displayed.

###### Note

Editing the current configuration creates a new configuration revision. 3. Choose **Edit configuration** and make changes to the Cuttlefish configuration. 4. Choose **Save**.

The **Save revision** dialog box is displayed. 5. (Optional) Type `A description of the changes in this revision`. 6. Choose **Save**.

The new revision of the configuration is saved.

###### Important

Making changes to a configuration does _not_ apply the changes to the broker immediately.
To apply your changes, you must wait for the next maintenance window
or [reboot the broker](amazon-mq-rebooting-broker.md "amazon-mq-rebooting-broker.md").

Currently, you can't delete a configuration.

## Apply a

Configuration Revision to Your Broker

After creating the configuration revision, you can apply the configuration
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
