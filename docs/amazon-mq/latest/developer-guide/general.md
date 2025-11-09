# Troubleshooting: General Amazon MQ

Use the information in this section to help you diagnose common issues you might encounter when working
with Amazon MQ brokers, such as issues connecting to your broker, and broker reboots.

###### Contents

- [I can't connect to my broker web console or endpoints.](general.md#issues-connecting-to-console-or-endpoint "general.md#issues-connecting-to-console-or-endpoint")
- [My broker is running, and I can verify connectivity using telnet,
  but my clients are unable to connect and are returning SSL exceptions.](general.md#issues-ssl-certificate-exception "general.md#issues-ssl-certificate-exception")
- [I created a broker but broker creation failed.](general.md#issues-creating-a-broker "general.md#issues-creating-a-broker")
- [My broker restarted and I'm not sure why.](general.md#w194aac39b9c13 "general.md#w194aac39b9c13")

## I can't connect to my broker web console or endpoints.

If you're experiencing issues connecting to your broker using the web console or wire-level endpoints,
we recommend the following steps.

1. Check whether you're attempting to connect to your broker from behind a firewall. You might need to configure the firewall to allow access to your broker.
2. Check whether you're trying to connect to your broker using a [FIPS](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/") endpoint.
   Amazon MQ only supports FIPS endpoints when using API operations, and not for wire-level connections to the broker instance itself.
3. Check if the **Public Accessibility** option for your broker is set to **Yes**.
   If this is set to **No**, check your subnet's network [Access Control List (ACL)](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") rules.
   If you've created custom network ACLs, you might need to change the network ACL rules to provide access to your broker. For more information on Amazon VPC networking, see
   [Enabling internet access](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#vpc-igw-internet-access "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#vpc-igw-internet-access")
   in the _Amazon VPC User Guide_
4. Check your broker's Security Group rules. Make sure that you are allowing connections to the following ports:

###### Note

The following ports are grouped according to engine types because ActiveMQ on Amazon MQ and RabbitMQ on Amazon MQ use different ports for connections.

###### ActiveMQ on Amazon MQ

    * Web console – Port `8162`
    * OpenWire – Port `61617`
    * AMQP – Port `5671`
    * STOMP – Port `61614`
    * MQTT – Port `8883`
    * WSS – Port `61619`

###### RabbitMQ on Amazon MQ

    * Web console and management API – Port  `443` and `15671`
    * AMQP – Port `5671`

5. Run the following network connectivity tests for your broker engine type.

###### Note

For brokers without public accessibility, run the tests from an Amazon EC2 instance within
the same Amazon VPC as your Amazon MQ broker and evaluate the responses.

ActiveMQ on Amazon MQ

###### To test your ActiveMQ on Amazon MQ broker's network connectivity

    1. Open a new terminal or command line window.
    2. Run the following `nslookup` command to query your broker DNS record. For
     [active/standby](amazon-mq-broker-architecture.md#active-standby-broker-deployment "amazon-mq-broker-architecture.md#active-standby-broker-deployment") deployments, test both the active and standby endpoints. The active/standby endpoints are identified
     with a suffix, `-1` or `-2` added to the unique broker ID. Replace the endpoint with your information.




    ```
    `$` `nslookup `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com``
    ```

    If the query succeeds, you will see an output similar to the following.



    ```
    Non-authoritative answer:
    Server:  dns-resolver-corp-sfo-1.sfo.corp.amazon.com
    Address:  172.10.123.456

    Name:    ec2-12-345-123-45.us-west-2.compute.amazonaws.com
    Address:  12.345.123.45
    Aliases:  b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com
    ```


     The resolved IP address should match the IP addresses provided in the Amazon MQ console. This indicates that the domain name is resolving correctly on the DNS server,
     and you can move on to the next step.
    3. Run the following `telnet` command to test the network path for your broker. Replace the endpoint with your information.
     Replace `port` with port number `8162` for the web console,
     or other wire-level ports to test additional protocols as needed.



    ###### Note


     For active/standby deployments, you will receive a `Connect failed` error message if you run `telnet` with the standby endpoint.
     This is expected, as the standby instance itself is running, but the ActiveMQ process is not running and does not have access to the broker's
     Amazon EFS storage volume. Run the command for both `-1` and `-2` endpoints to ensure you test both the active and the standby instances.




    ```
    `$` `telnet `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com` `port``
    ```

    For the active instance, you will see an output similar to the following.



    ```
    Connected to b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com.
    Escape character is '^]'.
    ```
    4. Do one of the following.




    	* If the `telnet` command succeeds, check the [EstablishedConnectionsCount](activemq-logging-monitoring.md#security-logging-monitoring-cloudwatch-metrics "activemq-logging-monitoring.md#security-logging-monitoring-cloudwatch-metrics") metric and confirm that the
    	 broker has not reached the maximum [Wire-level connection limit](amazon-mq-limits.md "amazon-mq-limits.md"). You can also confirm if the limit has been reached by reviewing
    	 the broker `General` logs. If this metric is greater than zero, then there is at least one client currently connected to the broker.
    	 If the metric shows zero connections, then perform the `telnet` path test again and wait at least one minute before disconnecting, as broker metrics are published every minute.
    	* If the `telnet` command fails, check the status of your broker's [elastic network interface](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md"),
    	 and confirm that the status is `in-use`. [Create an Amazon VPC flow log](../../../vpc/latest/userguide/working-with-flow-logs.md#create-flow-log "../../../vpc/latest/userguide/working-with-flow-logs.md#create-flow-log") for each instance's network interface,
    	 and review the generated flow logs. Look for the broker's IP addresses when you ran the `telnet` command, and confirm the connection packets are `ACCEPTED`, including a return packet.
    	 For more information, and to see a flow log example, see [Flow log record examples](../../../vpc/latest/userguide/flow-logs-records-examples.md "../../../vpc/latest/userguide/flow-logs-records-examples.md") in the *Amazon VPC Developer Guide*.
    5. Run the following `curl` command to check connectivity to the ActiveMQ admin web console.




    ```
    `$` `curl https://`b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com`:8162/index.html`
    ```

    If the command succeeds, the output should be an HTML document similar to the following.



    ```
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
            <title>Apache ActiveMQ</title>
            ...

    ```

RabbitMQ on Amazon MQ

###### To test your RabbitMQ on Amazon MQ broker's network connectivity

    1. Open a new terminal or command line window.
    2. Run the following `nslookup` command to query your broker DNS record. Replace the endpoint with your information.




    ```
    `$` `nslookup `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com``
    ```

    If the query succeeds, you will see an output similar to the following.



    ```
    Non-authoritative answer:
    Server:  dns-resolver-corp-sfo-1.sfo.corp.amazon.com
    Address:  172.10.123.456

    Name:    rabbit-broker-1c23e456ca78-b9000123b4ebbab5.elb.us-west-2.amazonaws.com
    Addresses:  52.12.345.678
              52.23.234.56
              41.234.567.890
              54.123.45.678
    Aliases:  b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com
    ```
    3. Run the following `telnet` command to test the network path for your broker. Replace the endpoint with your information.
     You can replace `port` with port `443` for the web console, and `5671` to test the wire-level AMQP connection.




    ```
    `$` `telnet `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com` `port``
    ```

    If the command succeeds, you'll see an output similar to the following.



    ```
    Connected to b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com.
    Escape character is '^]'.
    ```

    ###### Note


     The telnet connection will close automatically after a few seconds.
    4. Do one of the following.




    	* If the `telnet` command succeeds, check the [ConnectionCount](rabbitmq-logging-monitoring.md#security-logging-monitoring-cloudwatch-metrics-rabbitmq "rabbitmq-logging-monitoring.md#security-logging-monitoring-cloudwatch-metrics-rabbitmq") metric and confirm that the
    	 broker has not reached the value set in the [max-connections](rabbitmq-defaults.md#rabbitmq-defaults-values "rabbitmq-defaults.md#rabbitmq-defaults-values") default policy. You can also confirm if the limit has been reached by reviewing
    	 the broker `Connection.log` log group. If this metric is greater than zero, there is at least one client currently connected to the broker.
    	 If the metric shows zero connections, then perform the `telnet` path test again. You may need to repeat this process if the connection closes before
    	 your broker has published new connection metrics to CloudWatch. Metrics are published every minute.
    	* For brokers without public accessibility, if the `telnet` command fails, check the status of your broker's [elastic network interfaces](../../../UserGuide/using-eni.md "../../../UserGuide/using-eni.md"),
    	 and confirm that the status is `in-use`. [Create an Amazon VPC flow log](../../../vpc/latest/userguide/working-with-flow-logs.md#create-flow-log "../../../vpc/latest/userguide/working-with-flow-logs.md#create-flow-log") for each network interface,
    	 and review the generated flow logs. Look for the broker's private IP addresses when you the `telnet` command was invoked, and confirm the connection packets are `ACCEPTED`, including a return packet.
    	 For more information, and to see a flow log example, see [Flow log record examples](../../../vpc/latest/userguide/flow-logs-records-examples.md "../../../vpc/latest/userguide/flow-logs-records-examples.md") in the *Amazon VPC Developer Guide*.



    	###### Note

    	This step does not apply to RabbitMQ on Amazon MQ brokers with public accessibility.
    5. Run the following `curl` command to check connectivity to the RabbitMQ admin web console.




    ```
    `$` `curl https://`b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-west-2.amazonaws.com`:443/index.html`
    ```

    If the command succeeds, the output should be an HTML document similar to the following.



    ```
    <!DOCTYPE html>
    <html>
        <head>
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <title>RabbitMQ Management</title>
            ...
    ```

## My broker is running, and I can verify connectivity using `telnet`,

but my clients are unable to connect and are returning SSL exceptions.

Your broker endpoint certificate may have been updated during the broker [maintenance window](maintaining-brokers.md "maintaining-brokers.md").
Amazon MQ broker certificates are rotated periodically to ensure continued availability and security of brokers.

We recommend using the Amazon root certificate authority (CA) in [Amazon Trust Services](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/")
to authenticate against in your clients' trust store. All Amazon MQ broker certificates are signed with this root CA.
By using an Amazon root CA, you will no longer need to download the new Amazon MQ broker certificate every time there is a certificate update on the broker.

## I created a broker but broker creation failed.

If your broker is in a `CREATION_FAILED` status, do the following.

- Check your IAM permissions. To create a broker must either use the AWS managed IAM policy `AmazonMQFullAccess` or have the correct
  set of Amazon EC2 permissions in your custom IAM policy. To learn more about the required Amazon EC2 permissions you need, see
  [IAM permissions required to create an Amazon MQ broker](security-api-authentication-authorization.md#security-permissions-required-to-create-broker "security-api-authentication-authorization.md#security-permissions-required-to-create-broker").
- Check if the subnet you are choosing for your broker is in a shared Amazon Virtual Private Cloud (VPC). To create an Amazon MQ broker in a shared
  Amazon VPC, you must create it in the account that owns the Amazon VPC.

## My broker restarted and I'm not sure why.

If your broker has restarted automatically, it may be due to one of the following reasons.

- Your broker may have restarted because of a scheduled weekly maintenance window. Periodically, Amazon MQ performs maintenance to the hardware, operating system, or the engine software of a message broker.
  The duration of the maintenance varies, but can last up to two hours, depending on the operations that are scheduled for your message broker. Brokers might restart at any point during the two hour maintenance window.
  For more information on broker maintenance windows, see [Scheduling the maintenance window for an Amazon MQ broker](maintaining-brokers.md "maintaining-brokers.md").
- Your broker instance type might not be suitable to your application workload. For example, running a production workload on a `mq.t3.micro`
  might result in the broker running out of resources. High CPU utilization, or high broker memory usage can cause a broker to unexpectedly restart.
  To see how much CPU and memory is being utilized by your broker, use the following CloudWatch metrics for your engine type.
  - ActiveMQ on Amazon MQ –
    Check `CpuUtilization` for the percentage of allocated Amazon EC2 compute units that the broker currently uses.
    Check `HeapUsage`for the percentage of the ActiveMQ JVM memory limit that the broker currently uses.
  - RabbitMQ on Amazon MQ –
    Check `SystemCpuUtilization` for the percentage of allocated Amazon EC2 compute units that the broker currently uses.
    Check `RabbitMQMemUsed` for the volume of RAM used in Bytes, and divide by `RabbitMQMemLimit` for the percentage of memory used by the RabbitMQ node.

For more information on broker instance types and how to choose the right instance type for your workload, see [Broker instance types](broker-instance-types.md "broker-instance-types.md").
