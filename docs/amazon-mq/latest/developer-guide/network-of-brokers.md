

# Amazon MQ network of brokers
<a name="network-of-brokers"></a>

Amazon MQ supports ActiveMQ's network of brokers feature.

 A network of brokers is comprised of multiple simultaneously active single-instance brokers or active/standby brokers. Creating a network of brokers can increase availability, fault tolerance, and load balancing with multiple broker instances. 

## How does a Network of Brokers work?
<a name="how-does-it-work"></a>

 A network of brokers is established by connecting one broker to another using *network connectors*. A network connector provides on-demand message from one broker to another. Network connectors are configured in the broker configuration as either *non-duplex* or *duplex* connections. For non-duplex connections, messages are forwarded only from one broker to the other. For duplex connections, messages are forwarded both ways between both brokers. 

 If the network connector is configured as duplex, messages are also forwarded from *Broker2* to *Broker1*. 

 You can use both non-duplex and duplex connections in a network of brokers. You may want to introduce a duplex connection to another broker to improve traffic, or to avoid a limit increase. Duplex connections are also useful for partial migration from on-premises to Amazon MQ managed brokers. 

The following example shows a duplex `networkConnector` entry:

```
<networkConnectors>
  <networkConnector name="connector1" duplex="true"
      uri="static:(ssl://{{broker-id}}.mq.{{region}}.amazonaws.com:61617)"/>
</networkConnectors>
```

## How Does a Network of Brokers Handle Credentials?
<a name="how-does-it-handle-credentials"></a>

For broker A to connect to broker B in a network, broker A must use valid credentials, like any other producer or consumer. Instead of providing a password in broker A's `<networkConnector>` configuration, you must first create a user on broker A with the same values as another user on broker B (these are *separate, unique* users that share the same username and password values). When you specify the `userName` attribute in the `<networkConnector>` configuration, Amazon MQ will add the password automatically at runtime.

**Important**  
Don't specify the `password` attribute for the `<networkConnector>`. We don't recommend storing plaintext passwords in broker configuration files, because this makes the passwords visible in the Amazon MQ console. For more information, see [Step 2: Configure Network Connectors for Your Broker](amazon-mq-creating-configuring-network-of-brokers.md#creating-configuring-network-of-brokers-configure-network-connectors).

## Cross region
<a name="how-to-configure-cross-region"></a>

To configure a network of brokers that spans AWS regions, deploy brokers in those regions, and configure network connectors to the endpoints of those brokers.

![Cross-region mesh topology](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/images/amazon-mq-nob-cross-region.png)


To configure a network of brokers like this example, you could add `networkConnectors` entries to the configurations of *Broker1* and *Broker4* that reference the wire-level endpoints of those brokers.

*Network connectors for Broker1:*

```
<networkConnectors>
    <networkConnector name="1_to_2" userName="myCommonUser" duplex="true"
        uri="static:(ssl://b-9876l5k4-32ji-109h-8gfe-7d65c4b132a1-2.mq.us-west-2.amazonaws.com:61617)"/>
    <networkConnector name="1_to_3" userName="myCommonUser" duplex="true"
        uri="static:(ssl://b-743c885d-2244-4c95-af67-a85017ff234e-3.mq.us-east-2.amazonaws.com:61617)"/>
    <networkConnector name="1_to_4" userName="myCommonUser" duplex="true"
        uri="static:(ssl://b-62a7fb31-d51c-466a-a873-905cd660b553-4.mq.us-east-2.amazonaws.com:61617)"/>
</networkConnectors>
```

*Network connector for Broker2:*

```
<networkConnectors>
    <networkConnector name="2_to_3" userName="myCommonUser" duplex="true"
        uri="static:(ssl://b-743c885d-2244-4c95-af67-a85017ff234e-3.mq.us-east-2.amazonaws.com:61617)"/>
</networkConnectors>
```

*Network connectors for Broker4:*

```
<networkConnectors>
    <networkConnector name="4_to_3" userName="myCommonUser" duplex="true"
        uri="static:(ssl://b-743c885d-2244-4c95-af67-a85017ff234e-3.mq.us-east-2.amazonaws.com:61617)"/>
    <networkConnector name="4_to_2" userName="myCommonUser" duplex="true"
        uri="static:(ssl://b-9876l5k4-32ji-109h-8gfe-7d65c4b132a1-2.mq.us-west-2.amazonaws.com:61617)"/>      
</networkConnectors>
```

## Dynamic Failover With Transport Connectors
<a name="transport-connectors"></a>

In addition to configuring `networkConnector` elements, you can configure your broker `transportConnector` options to enable dynamic failover, and to rebalance connections when brokers are added or removed from the network. 

```
<transportConnectors>
  <transportConnector name="openwire" updateClusterClients="true" rebalanceClusterClients="true" updateClusterClientsOnRemove="true"/>
</transportConnectors>
```

In this example both `updateClusterClients` and `rebalanceClusterClients` are set to `true`. In this case clients will be provided a list of brokers in the network, and will request them to rebalance if a new broker joins.

Available options:
+ `updateClusterClients`: Passes information to clients about changes in the network of broker topology.
+ `rebalanceClusterClients`: Causes clients to re-balance across brokers when a new broker is added to a network of brokers.
+ `updateClusterClientsOnRemove`: Updates clients with topology information when a broker leaves a network of brokers.

When `updateClusterClients` is set to true, clients can be configured to connect to a single broker in a network of brokers. 

```
failover:(ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617)
```

When a new broker connects, it will receive a list of URIs of all brokers in the network. If the connection to the broker fails, it can dynamically switch to one of the brokers provided when it connected.

For more information on failover, see [Broker-side Options for Failover](https://activemq.apache.org/failover-transport-reference.html#FailoverTransportReference-Broker-sideOptionsforFailover) in the Active MQ documentation.