# AWS Direct Connect connection options

AWS offers customers the ability to achieve highly resilient network connections between
Amazon Virtual Private Cloud (Amazon VPC) and their on-premises infrastructure. The AWS Direct Connect Resiliency Toolkit provides a
connection wizard with multiple resiliency models. These models help you to determine, and
then place an order for the number of dedicated connections to achieve your SLA objective.
You select a resiliency model, and then the AWS Direct Connect Resiliency Toolkit guides you through the
dedicated connection ordering process. The resiliency models are designed to ensure that you
have the appropriate number of dedicated connections in multiple locations.

The following connection options are available for AWS Direct Connect.

- **Maximum Resiliency**: This model is available in the
  AWS Direct Connect Resiliency Toolkit and provides you a way to order dedicated connections to achieve an
  SLA of 99.99%. It requires you to meet all of the requirements for achieving the SLA
  that are specified in the [AWS Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/ "https://aws.amazon.com/directconnect/sla/"). For more information, see the [AWS Direct Connect Resiliency Toolkit](resiliency_toolkit.md "resiliency_toolkit.md").
- **High Resiliency**: This model is available in the AWS Direct Connect Resiliency Toolkit
  and provides you a way to order dedicated connections to achieve an SLA of 99.9%. It
  requires you to meet all of the requirements for achieving the SLA that are
  specified in the [AWS Direct Connect
  Service Level Agreement](https://aws.amazon.com/directconnect/sla/ "https://aws.amazon.com/directconnect/sla/"). For more information, see the [AWS Direct Connect Resiliency Toolkit](resiliency_toolkit.md "resiliency_toolkit.md").
- **Development and Test**: This model is available in the
  AWS Direct Connect Resiliency Toolkit and provides you a way to achieve development and test resiliency for
  non-critical workloads by using separate connections that terminate on separate
  devices in one location. For more information, see the [AWS Direct Connect Resiliency Toolkit](resiliency_toolkit.md "resiliency_toolkit.md").
- **Classic**: A Classic connection creates a connection without
  the need of the AWS Direct Connect Resiliency Toolkit. It's intended for users that have existing
  connections and want to add additional connections without using the toolkit. This
  model has a 95% SLA but does not provide resiliency or redundancy. For more
  information, see [Classic connection](classic_connection.md "classic_connection.md").

###### Topics

- [Connection prerequisites](#prerequisites "#prerequisites")
- [AWS Direct Connect Resiliency Toolkit](resiliency_toolkit.md "resiliency_toolkit.md")
- [Classic connection](classic_connection.md "classic_connection.md")

## Connection prerequisites

AWS Direct Connect supports the following port speeds over single-mode fiber: 1000BASE-LX (1310 nm)
transceiver for 1 gigabit Ethernet, a 10GBASE-LR (1310 nm) transceiver for 10 gigabit, a
100GBASE-LR4 for 100 gigabit Ethernet, or a 400GBASE-LR4 for 400 Gbps Ethernet.

You can set up an AWS Direct Connect connection using the AWS Direct Connect Resiliency Toolkit or a Classic connection in
one of the following ways:

| Model                | Bandwidth                                                                                                   | Method                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dedicated connection | 1 Gbps, 10 Gbps, 100 Gbps, and 400 Gbps                                                                     | Work with an AWS Direct Connect Partner or a network provider to connect a<br>router from your data center, office, or colocation environment to<br>an AWS Direct Connect location. The network provider does not have to be an<br>[AWS Direct Connect Partner](https://aws.amazon.com/directconnect/partners "https://aws.amazon.com/directconnect/partners") to connect you to a dedicated connection.<br>AWS Direct Connect dedicated connections support these port speeds over<br>single-mode fiber: 1 Gbps: 1000BASE-LX (1310 nm), 10 Gbps:<br>10GBASE-LR (1310 nm), 100Gbps: 100GBASE-LR4, or 400GBASE-LR4 for 400<br>Gbps Ethernet. |
| Hosted connection    | 50 Mbps, 100 Mbps, 200 Mbps, 300 Mbps, 400 Mbps, 500 Mbps, 1 Gbps, 2<br>Gbps, 5 Gbps, 10 Gbps, and 25 Gbps. | Work with a partner in the [AWS Direct Connect Partner Program](https://aws.amazon.com/directconnect/partners "https://aws.amazon.com/directconnect/partners")<br>to connect a router from your data center, office, or colocation<br>environment to an AWS Direct Connect location.<br>Only certain partners provide higher capacity connections.                                                                                                                                                                                                                                                                                          |

For connections to AWS Direct Connect with bandwidths of 1 Gbps or higher, ensure that your
network meets the following requirements:

- Your network must use single-mode fiber with a 1000BASE-LX (1310 nm) transceiver for 1 gigabit Ethernet, a 10GBASE-LR (1310 nm) transceiver for 10 gigabit, a 100GBASE-LR4 for 100 gigabit Ethernet, or a 400GBASE-LR4 for 400 Gbps Ethernet.
- Depending on the AWS Direct Connect endpoint serving your connection, on-premises device auto-negotiation might need to be enabled or disabled for any dedicated connection. If a virtual interface remains down when a Direct Connect connection is up, see [Troubleshoot layer 2 (data link) issues](ts-layer-2.md "ts-layer-2.md").
- 802.1Q VLAN encapsulation must be supported across the entire connection,
  including intermediate devices.
- Your device must support Border Gateway Protocol (BGP) and BGP MD5 authentication.
- (Optional) You can configure Bidirectional Forwarding Detection (BFD) on your
  network. Asynchronous BFD is automatically enabled for each AWS Direct Connect virtual interface. It's automatically enabled for Direct Connect virtual
  interfaces, but does not take effect until you configure it on your router. For more information, see [Enable BFD for a Direct Connect connection](https://aws.amazon.com/premiumsupport/knowledge-center/enable-bfd-direct-connect/ "https://aws.amazon.com/premiumsupport/knowledge-center/enable-bfd-direct-connect/").

Make sure you have the following information before you begin your
configuration:

- The resiliency model that you want to use if you're not creating a Classic
  connection. For AWS Direct Connect Resiliency Toolkit connection options, see the [AWS Direct Connect Resiliency Toolkit](resiliency_toolkit.md "resiliency_toolkit.md").
- The speed, location, and partner for all of your connections.

You only need the speed for one connection.
