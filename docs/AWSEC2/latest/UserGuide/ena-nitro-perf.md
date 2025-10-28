# Nitro system considerations for performance tuning

The Nitro System is a collection of hardware and software components built by AWS that
enable high performance, high availability, and high security.
The Nitro System provides bare metal-like capabilities that eliminate virtualization
overhead and support workloads that require full access to host hardware. For more detailed information, see [AWS Nitro System](https://aws.amazon.com/ec2/nitro/ "https://aws.amazon.com/ec2/nitro/").

All current generation EC2 instance types perform network packet processing on EC2 Nitro
Cards. This topic covers high level packet handling on the Nitro card, common aspects of
network architecture and configuration that impact packet handling performance, and what
actions you can take to achieve peak performance for your Nitro based instances.

Nitro Cards handle all input and output (I/O) interfaces, such as those needed for Virtual
Private Clouds (VPCs). For all of the components that send or receive information over the
network, the Nitro cards act as a self-contained computing device for I/O traffic that's
physically separate from the system main board on which customer workloads run.

## Network packet flow on Nitro cards

EC2 instances built on the Nitro system have hardware acceleration capabilities that
enable faster packet processing, as measured by packets per second (PPS) throughput
rates. When a Nitro card performs the initial evaluation for a new flow, it saves
information that's the same for all packets in the flow, such as security groups, access
control lists, and route table entries. When it processes additional packets for the
same flow, it can use the saved information to reduce overhead for those packets.

Your connection rate is measured by the connections per second (CPS) metric. Each new
connection requires additional processing overhead that must be factored into workload
capability estimates. It's important to consider both the CPS and PPS metrics when you
design your workloads.

###### How a connection is established

When a connection is established between a Nitro based instance and another
endpoint, the Nitro card evaluates the full flow for the first packet that's sent or
received between the two endpoints. For subsequent packets of the same flow, full
reevaluation is usually not necessary. However, there are exceptions. For more
information about the exceptions, see [Packets that don't use hardware
acceleration](#ena-nitro-perf-exceptions "#ena-nitro-perf-exceptions").

The following properties define the two endpoints and the packet flow between them.
These five properties together are known as a 5-tuple flow.

- Source IP
- Source port
- Destination IP
- Destination port
- Communication protocol

The direction of the packet flow is known as _ingress_ (inbound)
and _egress_ (outbound). The following high level descriptions
summarize end to end network packet flow.

- **Ingress** – When a Nitro card handles an
  inbound network packet, it evaluates the packet against stateful firewall rules
  and access control lists. It tracks the connection, meters it, and performs
  other actions as applicable. Then it forwards the packet to its destination on
  the host CPU.
- **Egress** – When a Nitro card handles an
  outbound network packet, it looks up the remote interface destination, evaluates
  various VPC functions, applies rate limits, and performs other actions that
  apply. Then it forwards the packet to its next hop destination on the
  network.

## Design your network for optimal

performance

To take advantage of your Nitro system's performance capabilities, you must understand
what your network processing needs are and how those needs affect the workload for your
Nitro resources. Then you can design for optimal performance for your network landscape.
Your infrastructure settings and application workload design and configuration can
impact both the packet processing and connection rates. For example, if your application
has a high rate of connection establishment, such as a DNS service, firewall, or virtual
router, it will have less opportunity to take advantage of the hardware acceleration
that only occurs after the connection is established.

You can configure application and infrastructure settings to streamline workloads and
improve network performance. However, not all packets are eligible for acceleration. The
Nitro system uses the full network flow for new connections and for packets that aren't
eligible for acceleration.

The remainder of this section will focus on application and infrastructure design
considerations to help ensure that packets flow within the accelerated path as much as
possible.

### Network design considerations for

the Nitro system

When you configure network traffic for your instance, there are many aspects to
consider that can affect PPS performance. After a flow is established, the majority
of packets that regularly come in or go out are eligible for acceleration. However,
exceptions exist to ensure that infrastructure designs and packet flows continue to
meet protocol standards.

To get the best performance from your Nitro card, you should carefully consider
the pros and cons of the following configuration details for your infrastructure and
applications.

#### Infrastructure

considerations

Your infrastructure configuration can affect your packet flow and processing
efficiency. The following list includes some important considerations.

**Network interface configuration with asymmetry**

Security groups use connection tracking to track information about
traffic that flows to and from the instance.
Asymmetric routing, where traffic comes into an instance through
one network interface and leaves through a different network interface, can reduce the peak performance
that an instance can achieve if flows are tracked. For more information about security
group connection tracking, untracked connections, and automatically
tracked connections, see [Amazon EC2 security group connection tracking](security-group-connection-tracking.md "security-group-connection-tracking.md").

**Network drivers**

Network drivers are updated and released on a regular basis. If
your drivers are out of date, that can significantly impair
performance. Keep your drivers up to date to ensure that you have
the latest patches and can take advantage of performance
improvements, such as the accelerated path feature that's only
available for the latest generation of drivers. Earlier drivers
don't support the accelerated path feature.

To take advantage of the accelerated path feature, we recommend
that you install the latest ENA driver on your instances.

Linux instances – ENA Linux
driver 2.2.9 or later. To install or update the ENA Linux driver
from the Amazon Drivers GitHub repository, see the [Driver compilation](https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#driver-compilation "https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#driver-compilation") section of the readme file.

Windows instances – ENA
Windows driver 2.0.0 or later. To install or update the ENA Windows
driver, see [Install the ENA driver on EC2 Windows instances](ena-adapter-driver-install-upgrade-win.md "ena-adapter-driver-install-upgrade-win.md").

**Distance between endpoints**

A connection between two instances in the same Availability Zone
can process more packets per second than a connection across Regions
as a result of TCP windowing at the application layer, which
determines how much data can be in flight at any given time. Long
distances between instances increase latency and decrease the number
of packets that the endpoints can process.

**Byte queue limit (BQL)**

BQL is a feature that limits the number of bytes passed to the
Nitro card to reduce queuing. BQL is disabled by default in ENA
drivers, in Amazon Linux operating systems, and in most Linux
distributions. If BQL and the fragment proxy override are both
enabled, it can result in performance limitations by restricting the
number of bytes passed to Nitro before all fragments are
processed.

#### Application design

considerations

There are aspects of application design and configuration that can affect your
processing efficiency. The following list includes some important
considerations.

**Packet size**

Larger packet sizes can increase throughput for the data that an
instance can send and receive on the network. Amazon EC2 supports jumbo
frames of 9001 bytes, however other services may enforce different
limits. Smaller packet sizes can increase the packet process rate,
but this can reduce the maximum achieved bandwidth when the number
of packets exceed PPS allowances.

If the size of a packet exceeds the Maximum Transmission Unit
(MTU) of a network hop, a router along the path might fragment it.
The resulting packet fragments are considered exceptions, and are
normally processed at the standard rate (not accelerated). This can
cause variations in your performance. However, you can override the
standard behavior for outbound fragmented packets with the fragment
proxy mode setting. For more information, see [Maximize network performance on your Nitro
system](#ena-nitro-perf-maximize "#ena-nitro-perf-maximize"). We recommended that
you evaluate your topology when you configure MTU.

**Protocol trade-offs**

Reliable protocols like TCP have more overhead than unreliable
protocols like UDP. The lower overhead and simplified network
processing for the UDP transport protocol can result in a higher PPS
rate, but at the expense of reliable packet delivery. If reliable
packet delivery isn’t critical for your application, UDP might be a
good option.

**Micro-bursting**

Micro-bursting occurs when traffic exceeds allowances during brief
periods of time rather than being evenly distributed. This typically
happens on a microsecond scale.

For example, say that you have an instance that can send up to 10
Gbps, and your application sends the full 10 Gb in half a second.
This micro-burst exceeds the allowance during the first half second
and leaves nothing for the remainder of the second. Even though you
sent 10Gb in the 1 second timeframe, allowances in the first half
second can result in packets being queued or dropped.

You can use a network scheduler such as Linux Traffic Control to
help pace your throughput and avoid causing queued or dropped
packets as a result of micro-bursting.

**Number of flows**

A single flow is limited to 5 Gbps unless it's inside of a cluster
placement group that supports up to 10 Gbps, or if it uses ENA
Express, which supports up to 25 Gbps.

Similarly, a Nitro card can process more packets across multiple
flows as opposed to using a single flow. To achieve the peak packet
processing rate per instance, we recommend at least 100 flows on
instances with 100 Gbps or higher aggregate bandwidth. As aggregate
bandwidth capabilities increase, the number of flows needed to
achieve peak processing rates also increases. Benchmarking will help
you determine what configuration you need to achieve peak rates on
your network.

**Elastic Network Adapter (ENA) queues**

ENA (Elastic Network Adapter) uses multiple receive (Rx) and
transmit (Tx) queues (ENA queues) to improve network performance and
scalability on EC2 instances. These queues efficiently manage
network traffic by load-balancing sent and received data across
available queues.

For more information, see [ENA queues](ena-queues.md "ena-queues.md").

**Feature process overhead**

Features like Traffic Mirroring and ENA Express can add more
processing overhead, which can reduce absolute packet processing
performance. You can limit feature use or disable features to
increase packet processing rates.

**Connection tracking to maintain state**

Your security groups use connection tracking to store information
about traffic to and from the instance. Connection tracking applies
rules against each individual flow of network traffic to determine
if the traffic is allowed or denied. The Nitro card uses flow
tracking to maintain state for the flow. As more security group
rules are applied, more work is required to evaluate the
flow.

###### Note

Not all network traffic flows are tracked. If a security group
rule is configured with [Untracked connections](security-group-connection-tracking.md#untracked-connections "security-group-connection-tracking.md#untracked-connections"), no additional work
is required except for connections that are automatically
tracked to ensure symmetric routing when there are multiple
valid reply paths.

#### Packets that don't use hardware

acceleration

Not all packets can take advantage of hardware acceleration. Handling these
exceptions involves some processing overhead which is necessary to ensure the
health of your network flows. Network flows must reliably meet protocol
standards, conform to changes in the VPC design, and route packets only to
allowed destinations. However, the overhead reduces your performance.

**Packet fragments**

As mentioned under **Application
considerations**, packet fragments that result from
packets that exceed network MTU are normally handled as exceptions,
and can't take advantage of hardware acceleration. However, you can
bypass egress fragment limitations with the fragment proxy mode,
depending on your driver version. For more information, see actions
you can take in the [Maximize network performance on your Nitro
system](#ena-nitro-perf-maximize "#ena-nitro-perf-maximize") section.

**Idle connections**

When a connection has no activity for a while, even if the
connection hasn't reached its timeout limit, the system can
de-prioritize it. Then, if data comes in after the connection is
de-prioritized, the system needs to handle it as an exception in
order to reconnect.

To manage your connections, you can use connection tracking
timeouts to close idle connections. You can also use TCP keepalives
to keep idle connections open. For more information, see [Idle connection tracking timeout](security-group-connection-tracking.md#connection-tracking-timeouts "security-group-connection-tracking.md#connection-tracking-timeouts").

**VPC mutation**

Updates to security groups, route tables, and access control lists
all need to be reevaluated in the processing path to ensure that
route entries and security group rules still apply as
expected.

**ICMP flows**

Internet Control Message Protocol (ICMP) is a network layer
protocol that network devices use to diagnose network communication
issues. These packets always use the full flow.

**Asymmetric L2 flows**

NitroV3 and earlier platforms do not use hardware acceleration for
traffic between two ENIs in the same subnet where one ENI is using
the default gateway router and the other is not. NitroV4 and later
platforms utilize hardware acceleration in this scenario. For better
performance on NitroV3 or earlier platforms, ensure that either the
default gateway router used matches between both ENIs, or those ENIs
are in different subnets.

## Maximize network performance on your Nitro

system

You can maximize your network performance on Nitro system by adjusting network
settings.

###### Topics

- [Considerations](#considerations "#considerations")
- [Tune PPS performance](#tuning "#tuning")
- [Configure ENA queue allocation](#max-perf-ena-queues "#max-perf-ena-queues")
- [Monitor performance on Linux instances](#monitoring "#monitoring")

### Considerations

Before you make any design decisions or adjust any network settings on your
instance, we recommend that you take the following steps to help ensure that you
have the best outcome:

1. Understand the pros and cons of the actions that you can take to improve
   performance by reviewing [Network design considerations for
   the Nitro system](#ena-nitro-perf-considerations "#ena-nitro-perf-considerations").

For more considerations and best practices for your instance configuration
on Linux, see [ENA Linux Driver Best Practices and Performance Optimization
Guide](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst "https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst") on GitHub. 2. Benchmark your workloads with peak active flow count to determine a
baseline for your application performance. With a performance baseline, you
can test variations in your settings or application design to understand
which considerations will have the most impact, especially if you plan to
scale up or scale out.

### Tune PPS performance

The following list contains actions that you can take to tune your PPS
performance, depending on your system needs.

- Reduce the physical distance between two instances. When sending and
  receiving instances are located in same Availability Zone or use cluster
  placement groups, you can reduce the number of hops a packet needs to take
  to travel from one endpoint to another.
- Use [Untracked connections](security-group-connection-tracking.md#untracked-connections "security-group-connection-tracking.md#untracked-connections").
- Use the UDP protocol for network traffic.
- For EC2 instances with aggregate bandwidth of 100 Gbps or more, distribute
  the workload over 100 or more individual flows to spread the work evenly
  across the Nitro card.
- To overcome the egress fragment PPS limit on EC2 instances, you can enable
  fragment proxy mode (depending on your driver version). This setting allows
  fragmented packets to be evaluated in the processing path, thereby
  overcoming the egress PPS limit of 1024. When loading the driver, run one of
  the following commands to enable or disable fragment proxy mode:

**Enable fragment proxy mode**

```
sudo insmod ena.ko enable_frag_bypass=1
```

**Disable fragment proxy mode**

```
sudo insmod ena.ko enable_frag_bypass=0
```

### Configure ENA queue allocation

On supported instance types, you can dynamically allocate these queues across Elastic
Network Interfaces (ENIs). Flexible ENA queue allocation optimizes resource distribution,
enabling maximum vCPU utilization. High network performance workloads typically require
multiple ENA queues. For more information, see [ENA queues](ena-queues.md "ena-queues.md").

### Monitor performance on Linux instances

You can use Ethtool metrics on Linux instances to monitor instance networking
performance indicators such as bandwidth, packet rate, and connection tracking. For
more information, see [Monitor network performance for ENA
settings on your EC2 instance](monitoring-network-performance-ena.md "monitoring-network-performance-ena.md").
