

# Rebooting an Amazon MQ broker
<a name="amazon-mq-rebooting-broker"></a>

To apply a new configuration to a broker, you can reboot the broker. 

**Note**  
 If your ActiveMQ broker becomes unresponsive, you can reboot it to recover from a faulty state. 

The following example shows how you can reboot an Amazon MQ broker using the AWS Management Console.

## To Reboot an Amazon MQ Broker
<a name="rebooting-broker-console"></a>

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/).

1. From the broker list, choose the name of your broker (for example, **MyBroker**).

1. On the **{{MyBroker}}** page, choose **Actions**, **Reboot broker**.
**Important**  
Single instance brokers will be offline while being rebooted. Cluster brokers will be available, but each node is rebooted one at a time.

1. In the **Reboot broker** dialog box, choose **Reboot**.

   Rebooting a broker takes about 5 minutes. If the reboot includes instance size changes or is performed on a broker with high queue depth, the rebooting process can take longer.