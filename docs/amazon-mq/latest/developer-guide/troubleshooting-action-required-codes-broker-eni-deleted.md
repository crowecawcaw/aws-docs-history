

# ActiveMQ on Amazon MQ: Deleted Elastic Network Interface alarm
<a name="troubleshooting-action-required-codes-broker-eni-deleted"></a>

ActiveMQ on Amazon MQ will raise a BROKER\_ENI\_DELETED alarm when you delete a broker’s Elastic Network Interface (ENI). When you first [create an Amazon MQ broker](getting-started-activemq.md), Amazon MQ provisions an [elastic network interface](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ElasticNetworkInterfaces.html) in the [Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Introduction.html) under your account and, thus, requires a number of [EC2 permissions](security-api-authentication-authorization.md).

You must not modify or delete this network interface. Modifying or deleting the network interface can cause a permanent loss of connection between your VPC and your broker. If you wish to delete the network interface, you must delete the broker first.