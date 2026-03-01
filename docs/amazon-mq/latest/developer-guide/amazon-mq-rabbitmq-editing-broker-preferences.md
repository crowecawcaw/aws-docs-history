# Editing broker preferences

You can edit your broker preferences, such as enabling or disabling CloudWatch logs using the AWS Management Console.

## Edit RabbitMQ broker options

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. From the broker list, select your broker (for example, **MyBroker**) and then choose **Edit**.
3. On the **Edit `MyBroker`** page,
   in the **Specifications** section, select a
   **Broker engine version** or a **Broker
   Instance type**.
4. In the **CloudWatch Logs** section, click the toggle button to enable or disable general logs. No other steps are required.

###### Note

    * For RabbitMQ brokers, Amazon MQ automatically uses a Service-Linked Role (SLR) to publish general logs to CloudWatch. For more information, see
     [Using service-linked roles for Amazon MQ](using-service-linked-roles.md "using-service-linked-roles.md")
    * Amazon MQ does not support audit logging for RabbitMQ brokers.

5. In the **Maintenance** section, configure your
   broker's maintenance schedule:

To upgrade the broker to new versions as AWS releases them, choose
**Enable automatic minor version upgrades**.
Automatic upgrades occur during the _maintenance window_
defined by the day of the week, the time of day (in 24-hour format), and the time zone (UTC by default). 6. Choose **Schedule modifications**.

###### Note

If you choose only **Enable automatic minor version
upgrades**, the button changes to **Save**
because no broker reboot is necessary.

Your preferences are applied to your broker at the specified time.
