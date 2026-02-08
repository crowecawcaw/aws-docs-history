# Edit an Amazon MQ for ActiveMQ

configuration
revision

You may want to edit a configuration revision after applying it
to your broker. Use the following instructions to edit a configuration
revision.

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
example, **Apache ActiveMQ 5.15.8**) are
displayed. 5. On the **Configuration details** tab, the configuration
revision number, description, and broker configuration in XML format are displayed.

###### Note

Editing the current configuration creates a new configuration revision.

![XML configuration snippet for ActiveMQ broker with explanatory comment.](/images/amazon-mq/latest/developer-guide/images/amazon-mq-tutorials-edit-configuration.png) 6. Choose **Edit configuration** and make changes to the XML configuration. 7. Choose **Save**.

The **Save revision** dialog box is displayed. 8. (Optional) Type `A description of the changes in this revision`. 9. Choose **Save**.

The new revision of the configuration is saved.

###### Important

The Amazon MQ console automatically sanitizes invalid and prohibited configuration parameters according to a schema.
For more information and a full list of permitted XML parameters, see [Amazon MQ Broker Configuration Parameters](amazon-mq-broker-configuration-parameters.md "amazon-mq-broker-configuration-parameters.md").
