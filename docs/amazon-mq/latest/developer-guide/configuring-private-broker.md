# Configuring a private Amazon MQ broker

A private broker does not have public accessibility and cannot be accessed from outside of your VPC.
Before configuring a private broker, view the following information about VPCs, subnets, and security groups:

- **VPCs**
  - A broker's subnet(s) and security group(s) must be in the same VPC.
  - When you are using a private broker, you may see IP addresses that you did not configure with your VPC.
    These are IP addresses from the Amazon MQ infrastructure, and they require no action.

- **Subnets**
  - If subnets are within a shared VPC, the VPC must be owned by the same account creating the broker.
  - If no subnets are provided, the default subnets in the default VPC will be used.
  - Once the broker is created, the subnets used cannot be changed.
  - For cluster and active/standby brokers, subnets must be in different Availability Zones.
  - For single instance brokers, you can specify which subnet to use and the broker will be created within the same Availability Zone.

- **Security groups**
  - If no security group is provided, the default security groups in the default VPC will be used.
  - Single-instance, cluster, and active/standby brokers require at least one security group (for example, the default security group).

  ###### Note

  Public RabbitMQ brokers do not use subnets or security groups.
  - Once the broker is created, the security group used cannot be changed. The security groups can themselves still be modified.

## Configuring a private broker in the AWS Management Console

To configure a private broker, begin [creating a new broker](getting-started-activemq.md "getting-started-activemq.md")
in the AWS Management Console.
Then, in the **Network settings** section,
to configure your broker's connectivity, do the following:

1. Choose **Private access** for your broker.
   To connect to a private broker, you can use IPv4, IPv6, or dual-stack (IPv4 and IPv6).
   For more information, see [Connecting to Amazon MQ](connect-to-amazonmq.md "connect-to-amazonmq.md").
2. Next, choose **Use the default VPC, subnet(s), and security group(s)**,
   or choose **Select existing VPC, subnet(s), and security group(s)**.
   If you do not wish to use the default or existing VPC, subnet(s), or security group(s),
   you must create a new one to connect to the private broker.

###### Note

For private broker access, the connection method will be the same as the selected IP type of the subnet.
Once the broker is created, the VPC endpoint cannot be changed
and will always have the IP type of the selected subnets.
If you want to use a new IP type, you must create a new broker.

###### Note

Amazon MQ for ActiveMQ does not use VPC endpoints. When you first create an ActiveMQ broker,
Amazon MQ provisions an elastic network interface (ENI) in the VPC.
Security groups are placed in the ENI and can be used for both public and private brokers.

## Accessing the Amazon MQ broker web console without public

accessibility

When you turn off public accessibility for your broker,
the AWS account ID that created the broker can access the private broker.
If you turn off public accessibility for your broker, you must perform the
following steps to access the broker web console.

1. Create a Linux EC2 instance in `public-vpc` (with a public
   IP, if necessary).
2. To verify that your VPC is configured correctly, establish an
   `ssh` connection to the EC2 instance and use the
   `curl` command with the URI of your broker.
3. From your machine, create an `ssh` tunnel to the EC2
   instance using the path to your private key file and the IP address of
   your public EC2 instance. For example:

```
ssh -i ~/.ssh/id_rsa -N -C -q -f -D 8080 ec2-user@203.0.113.0
```

A forward proxy server is started on your machine. 4. Install a proxy client such as [FoxyProxy](https://getfoxyproxy.org/ "https://getfoxyproxy.org/") on your machine. 5. Configure your proxy client using the following settings:

    * For proxy type, specify `SOCKS5`.
    * For IP address, DNS name, and server name, specify
     `localhost`.
    * For port, specify `8080`.
    * Remove any existing URL patterns.
    * For the URL pattern, specify
     `*.mq.*.amazonaws.com*`
    * For the connection type, specify `HTTP(S)`.

When you enable your proxy client, you can access the web
console on your machine.

###### Important

If you are using a private broker,
you may see IP addresses that you did not configure with your VPC.
These are IP addresses from the RabbitMQ on Amazon MQ infrastructure,
and they require no action.
