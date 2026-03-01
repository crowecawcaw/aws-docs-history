# Creating and configuring an Amazon MQ network of brokers

A _network of brokers_ is comprised of multiple simultaneously
active [single-instance brokers](amazon-mq-broker-architecture.md#single-broker-deployment "amazon-mq-broker-architecture.md#single-broker-deployment") or [active/standby brokers](amazon-mq-broker-architecture.md#active-standby-broker-deployment "amazon-mq-broker-architecture.md#active-standby-broker-deployment"). In this tutorial, you learn how to create a two-broker
network of brokers with a _source and sink_ topology.

For a conceptual overview and detailed configuration information, see the
following:

- [Amazon MQ network of brokers](network-of-brokers.md "network-of-brokers.md")
- [Configure Your Network of Brokers Correctly](best-practices-activemq.md#network-of-brokers-configure-correctly "best-practices-activemq.md#network-of-brokers-configure-correctly")
- `networkConnector`
- `networkConnectionStartAsync`
- [Networks of
  Brokers](http://activemq.apache.org/networks-of-brokers.html "http://activemq.apache.org/networks-of-brokers.html") in the ActiveMQ documentation
  You can use the Amazon MQ console to create an Amazon MQ network of brokers. Because you can
  start the creation of the two brokers in parallel, this process takes approximately 15
  minutes.

###### Topics

- [Prerequisites](#creating-configuring-network-of-brokers-create-brokers "#creating-configuring-network-of-brokers-create-brokers")
- [Step 1: Allow Traffic between Brokers](#creating-configuring-network-of-brokers-allow-traffic "#creating-configuring-network-of-brokers-allow-traffic")
- [Step 2: Configure Network Connectors for Your Broker](#creating-configuring-network-of-brokers-configure-network-connectors "#creating-configuring-network-of-brokers-configure-network-connectors")
- [Next Steps](#creating-configuring-network-of-brokers-test "#creating-configuring-network-of-brokers-test")

## Prerequisites

To create a network of brokers, you must have the following:

- Two or more simultaneously active brokers (named `MyBroker1`
  and `MyBroker2` in this tutorial). For more information about
  creating brokers, see [Getting started: Creating and connecting to an ActiveMQ broker](getting-started-activemq.md "getting-started-activemq.md").
- The two brokers must be in the same VPC or in peered VPCs. For more
  information about VPCs, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")
  in the _Amazon VPC User Guide_ and [What is VPC Peering?](../../../vpc/latest/peering/Welcome.md "../../../vpc/latest/peering/Welcome.md") in the
  _Amazon VPC Peering Guide_.

###### Important

If you don't have a default VPC, subnet(s), or security group, you
must create them first. For more information, see the following in the
_Amazon VPC User Guide_:

    + [Creating a Default VPC](../../../vpc/latest/userguide/default-vpc.md#create-default-vpc "../../../vpc/latest/userguide/default-vpc.md#create-default-vpc")
    + [Creating a Default Subnet](../../../vpc/latest/userguide/default-vpc.md#create-default-subnet "../../../vpc/latest/userguide/default-vpc.md#create-default-subnet")
    + [Creating a Security Group](../../../vpc/latest/userguide/VPC_SecurityGroups.md#CreatingSecurityGroups "../../../vpc/latest/userguide/VPC_SecurityGroups.md#CreatingSecurityGroups")

- Two users with identical sign-in credentials for both brokers. For
  more information about creating users, see [Creating an ActiveMQ broker user](amazon-mq-listing-managing-users.md "amazon-mq-listing-managing-users.md").

###### Note

When integrating LDAP authentication with a network of brokers, make sure that the user exists both as an ActiveMQ brokers, as well as an LDAP user.

The following example uses two [single-instance brokers](amazon-mq-broker-architecture.md#single-broker-deployment "amazon-mq-broker-architecture.md#single-broker-deployment"). However, you can create networks of brokers
using [active/standby brokers](amazon-mq-broker-architecture.md#active-standby-broker-deployment "amazon-mq-broker-architecture.md#active-standby-broker-deployment")
or a combination of broker deployment modes.

## Step 1: Allow Traffic between Brokers

After you create your brokers, you must allow traffic between them.

1. On the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/"),
   on the **MyBroker2** page, in the
   **Details** section, under **Security and
   network**, choose the name of your security group or
   ![Pencil icon indicating an edit or modification action.](images/amazon-mq-tutorials-broker-details-link.png)
   .

The **Security Groups** page of the EC2 Dashboard is
displayed. 2. From the security group list, choose your security group. 3. At the bottom of the page, choose **Inbound**, and then
choose **Edit**. 4. In the **Edit inbound rules** dialog box, add a rule for
the OpenWire endpoint.

    1. Choose **Add Rule**.
    2. For **Type**, select **Custom
     TCP**.
    3. For **Port Range**, type the OpenWire port
     (`61617`).
    4. Do one of the following:




    	* If you want to restrict access to a particular IP address,
    	 for **Source**, leave
    	 **Custom** selected, and then enter the
    	 IP address of `MyBroker1`, followed by
    	 `/32`. (This converts the IP address to a
    	 valid CIDR record). For more information see [Elastic Network
    	 Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md").


    	###### Tip

    	To retrieve the IP address of `MyBroker1`,
    	 on the [Amazon MQ
    	 console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/"), choose the name of the broker and
    	 navigate to the **Details**
    	 section.
    	* If all the brokers are private and belong to the same VPC,
    	 for **Source**, leave
    	 **Custom** selected and then type the
    	 ID of the security group you are editing.


    	###### Note

    	For public brokers, you must restrict access using IP
    	 addresses.
    5. Choose **Save**.


    Your broker can now accept inbound connections.

## Step 2: Configure Network Connectors for Your Broker

After you allow traffic between your brokers, you must configure network
connectors for one of them.

1.  Edit the configuration revision for broker `MyBroker1`.
    1. On the **MyBroker1** page, choose
       **Edit**.
    2. On the **Edit MyBroker1** page, in the
       **Configuration** section, choose
       **View**.

    The broker engine type and version that the configuration uses
    (for example, **Apache ActiveMQ 5.15.0**) are
    displayed. 3. On the **Configuration details** tab, the
    configuration revision number, description, and broker configuration
    in XML format are displayed. 4. Choose **Edit configuration**. 5. At the bottom of the configuration file, uncomment the
    `<networkConnectors>` section and include the
    following information:

        * The `name` for the network connector.
        * [The ActiveMQ Web Console username](#creating-configuring-network-of-brokers-create-brokers "#creating-configuring-network-of-brokers-create-brokers")
         that is common to both brokers.
        * Enable `duplex` connections.
        * Do one of the following:




        	+ If you are connecting the broker to a
        	 single-instance broker, use the `static:`
        	 prefix and the OpenWire endpoint `uri`
        	 for `MyBroker2`. For example:



        	```
        	<networkConnectors>
        	  <networkConnector name="`connector_1_to_2`" userName="`myCommonUser`" duplex="true"
        	    uri="static:(`ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617`)"/>
        	</networkConnectors>
        	```
        	+ If you are connecting the broker to an
        	 active/standby broker, use the
        	 `static+failover` transport and the OpenWire
        	 endpoint `uri` for both brokers with the following
        	 query parameters `?randomize=false&maxReconnectAttempts=0`.
        	 For example:



        	```
        	<networkConnectors>
        	  <networkConnector name="`connector_1_to_2`" userName="`myCommonUser`" duplex="true"
        	    uri="static:(failover:(`ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617,
        	 ssl://b-9876l5k4-32ji-109h-8gfe-7d65c4b132a1-2.mq.us-west-2.amazonaws.com:61617`)?randomize=false&amp;maxReconnectAttempts=0)"/>
        	</networkConnectors>
        	```
        ###### Note

        Don't include the sign-in credentials for the ActiveMQ
         user.

    6. Choose **Save**.
    7. In the **Save revision** dialog box, type
       `Add network of brokers connector for
MyBroker2`.
    8. Choose **Save** to save the new revision of the
       configuration.

2.  Edit `MyBroker1` to set the latest configuration revision to
    apply immediately.
    1. On the **MyBroker1** page, choose
       **Edit**.
    2. On the **Edit MyBroker1** page, in the
       **Configuration** section, choose
       **Schedule Modifications**.
    3. In the **Schedule broker modifications** section,
       choose to apply modifications
       **Immediately**.
    4. Choose **Apply**.

    `MyBroker1` is rebooted and your configuration revision
    is applied.The network of brokers is created.

## Next Steps

After you configure your network of brokers, you can test it by producing and
consuming messages.

###### Important

Make sure that you [enable inbound connections](amazon-mq-working-java-example.md#quick-start-allow-inbound-connections "amazon-mq-working-java-example.md#quick-start-allow-inbound-connections")
_from your local machine_ for broker `MyBroker1`
on port 8162 (for the ActiveMQ Web Console) and port 61617 (for the OpenWire
endpoint).

You might also need to adjust your security group(s) settings to allow the
producer and consumer to connect to the network of brokers.

1. On the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/"),
   navigate to the **Connections** section and note the
   ActiveMQ Web Console endpoint for broker `MyBroker1`.
2. Navigate to the ActiveMQ Web Console for broker
   `MyBroker1`.
3. To verify that the network bridge is connected, choose
   **Network**.

In the **Network Bridges** section, the name and the
address of `MyBroker2` are listed in the **Remote
Broker** and **Remote Address**
columns. 4. From any machine that has access to broker `MyBroker2`, create
a consumer. For example:

```
activemq consumer --brokerUrl "ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617" \
	--user commonUser \
	--password myPassword456 \
	--destination queue://MyQueue
```

The consumer connects to the OpenWire endpoint of `MyBroker2`
and begins to consume messages from queue `MyQueue`. 5. From any machine that has access to broker `MyBroker1`, create
a producer and send some messages. For example:

```
activemq producer --brokerUrl "ssl://b-9876l5k4-32ji-109h-8gfe-7d65c4b132a1-1.mq.us-east-2.amazonaws.com:61617" \
	--user commonUser \
	--password myPassword456 \
	--destination queue://MyQueue \
	--persistent true \
	--messageSize 1000 \
	--messageCount 10000
```

The producer connects to the OpenWire endpoint of `MyBroker1`
and begins to produce persistent messages to queue
`MyQueue`.
