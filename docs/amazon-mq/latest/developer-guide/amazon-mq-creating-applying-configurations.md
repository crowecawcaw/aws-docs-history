

# Creating an Amazon MQ for ActiveMQ broker configuration
<a name="amazon-mq-creating-applying-configurations"></a>

A *configuration* contains all of the settings for your ActiveMQ broker, in XML format (similar to ActiveMQ's `activemq.xml` file). You can create a configuration before creating any brokers. You can then apply the configuration to one or more brokers. You can apply a configuration immediately or during a *maintenance window*.

The following example shows how you can create and apply an Amazon MQ broker configuration using the AWS Management Console.

**Important**  
You can only **delete** a configuration using the `DeleteConfiguration` API. For more information, see [Configurations](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/configurations-configuration-id.html) in the *Amazon MQ API Reference*.

## Create a New Configuration
<a name="creating-configuration-from-scratch-console"></a>

To create a new broker configuration, first create the new configuration.

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/).

1. On the left, expand the navigation panel and choose **Configurations**.  
![Amazon MQ navigation panel showing Brokers and Configurations options.](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/images/amazon-mq-tutorials-create-configuration.png)

1. On the **Configurations** page, choose **Create configuration**.

1. On the **Create configuration** page, in the **Details** section, type the **Configuration name** (for example, `MyConfiguration`) and select a **Broker engine** version.
**Note**  
To learn more about ActiveMQ engine versions supported by Amazon MQ for ActiveMQ, see [Managing Amazon MQ for ActiveMQ engine versions](activemq-version-management.md).

1. Choose **Create configuration**.

## Create a New Configuration Revision
<a name="creating-new-configuration-revision-console"></a>

After you create a broker configuration, you will need to edit the configuration using a configuration revision.

1. From the configuration list, choose **{{MyConfiguration}}**.
**Note**  
The first configuration revision is always created for you when Amazon MQ creates the configuration.

   On the **{{MyConfiguration}}** page, the broker engine type and version that your new configuration revision uses (for example, **Apache ActiveMQ 5.15.16**) are displayed.

1. On the **Configuration details** tab, the configuration revision number, description, and broker configuration in XML format are displayed.
**Note**  
Editing the current configuration creates a new configuration revision.  
![XML configuration snippet for ActiveMQ broker with explanatory comment.](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/images/amazon-mq-tutorials-edit-configuration.png)

1. Choose **Edit configuration** and make changes to the XML configuration.

1. Choose **Save**.

   The **Save revision** dialog box is displayed.

1. (Optional) Type `A description of the changes in this revision`.

1. Choose **Save**.

   The new revision of the configuration is saved.
**Important**  
The Amazon MQ console automatically sanitizes invalid and prohibited configuration parameters according to a schema. For more information and a full list of permitted XML parameters, see [Amazon MQ for ActiveMQ broker configurations](amazon-mq-broker-configuration-parameters.md).

## Apply a Configuration Revision to Your Broker
<a name="apply-configuration-revision-creating-console"></a>

After revising the configuration, you can apply the configuration revision to your broker.

1. On the left, expand the navigation panel and choose **Brokers**.  
![Amazon MQ navigation panel showing Brokers and Configurations options.](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/images/amazon-mq-tutorials-apply-configuration.png)

1. From the broker list, select your broker (for example, **MyBroker**) and then choose **Edit**.

1. On the **Edit {{MyBroker}}** page, in the **Configuration** section, select a **Configuration** and a **Revision** and then choose **Schedule Modifications**.

1. In the **Schedule broker modifications** section, choose whether to apply modifications **During the next scheduled maintenance window** or **Immediately**.
**Important**  
Single instance brokers are offline while being rebooted. For cluster brokers, only one node is down at a time while the broker reboots.

1. Choose **Apply**.

   Your configuration revision is applied to your broker at the specified time.