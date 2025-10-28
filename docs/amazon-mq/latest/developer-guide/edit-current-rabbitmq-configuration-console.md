# Edit a

Amazon MQ for RabbitMQ Configuration Revision

The following instructions describe how to edit a configuration revision for your broker.

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. From the broker list, select your broker (for example, **MyBroker**) and then choose **Edit**.
3. On the **`MyBroker`** page,
   choose **Edit**.
4. On the **Edit `MyBroker`**
   page, in the **Configuration** section, select a **Configuration**
   and a **Revision** and then choose **Edit**.

###### Note

Unless you select a configuration when you create a broker,
the first configuration revision is always created for you
when Amazon MQ creates the broker.

On the **`MyBroker`** page,
the broker engine type and version that the configuration uses (for
example, **RabbitMQ 3.xx.xx**) are
displayed. 5. On the **Configuration details** tab, the configuration
revision number, description, and broker configuration in Cuttlefish format are displayed.

###### Note

Editing the current configuration creates a new configuration revision. 6. Choose **Edit configuration** and make changes to the Cuttlefish configuration. 7. Choose **Save**.

The **Save revision** dialog box is displayed. 8. (Optional) Type `A description of the changes in this revision`. 9. Choose **Save**.

The new revision of the configuration is saved.

###### Important

Making changes to a configuration does _not_ apply the changes to the broker immediately.
To apply your changes, you must wait for the next maintenance window
or [reboot the broker](amazon-mq-rebooting-broker.md "amazon-mq-rebooting-broker.md").

Currently, you can't delete a configuration.
