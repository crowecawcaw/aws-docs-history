# Monitor network performance for ENA

settings on your EC2 instance

The Elastic Network Adapter (ENA) driver publishes network performance metrics from the
instances where they are enabled. You can use these metrics to troubleshoot instance
performance issues, choose the right instance size for a workload, plan scaling activities
proactively, and benchmark applications to determine whether they maximize the performance
available on an instance.

Amazon EC2 defines network maximums at the instance level to ensure a high-quality networking
experience, including consistent network performance across instance sizes. AWS provides
maximums for the following for each instance:

- Bandwidth capability – Each EC2 instance has
  a maximum bandwidth for aggregate inbound and outbound traffic, based on instance
  type and size. Some instances use a network I/O credit mechanism to allocate network
  bandwidth based on average bandwidth utilization. Amazon EC2 also has maximum bandwidth
  for traffic to AWS Direct Connect and the internet. For more information, see [Amazon EC2 instance network bandwidth](ec2-instance-network-bandwidth.md "ec2-instance-network-bandwidth.md").
- Packet-per-second (PPS) performance – Each
  EC2 instance has a maximum PPS performance, based on instance type and size.
- Connections tracked – The security group
  tracks each connection established to ensure that return packets are delivered as
  expected. There is a maximum number of connections that can be tracked per instance.
  For more information, see [Amazon EC2 security group connection tracking](security-group-connection-tracking.md "security-group-connection-tracking.md")
- Link-local service access – Amazon EC2 provides a
  maximum PPS per network interface for traffic to local proxy services such as the
  Amazon DNS service, the Instance Metadata Service, and the Amazon Time Sync Service.
  When the network traffic for an instance exceeds a maximum, AWS shapes the traffic that
  exceeds the maximum by queueing and then dropping network packets. You can monitor when traffic exceeds a maximum using the network
  performance metrics. These metrics inform you, in real time, of impact to network traffic
  and possible network performance issues.

###### Contents

- [Requirements](#network-performance-metrics-requirements "#network-performance-metrics-requirements")
- [Metrics for the ENA driver](#network-performance-metrics "#network-performance-metrics")
- [View the network performance metrics
  for your instance](#view-network-performance-metrics "#view-network-performance-metrics")
- [Metrics for ENA
  Express](#network-performance-metrics-ena-express "#network-performance-metrics-ena-express")
- [Network performance metrics with the
  DPDK driver for ENA](#network-performance-metrics-dpdk "#network-performance-metrics-dpdk")
- [Metrics on instances running
  FreeBSD](#network-performance-metrics-freebsd "#network-performance-metrics-freebsd")

## Requirements

###### Linux instances

- Install ENA driver version 2.2.10 or later. To verify the installed version,
  use the **ethtool** command. In the following example, the
  version meets the minimum requirement.

```
`[ec2-user ~]$` `ethtool -i eth0 | grep version``version: 2.2.10`
```

To upgrade your ENA driver, see [Enhanced networking](enhanced-networking-ena.md "enhanced-networking-ena.md").

- To import these metrics to Amazon CloudWatch, install the CloudWatch agent. For more
  information, see [Collect network performance metrics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-network-performance.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-network-performance.md") in the
  _Amazon CloudWatch User Guide_.
- To support the `conntrack_allowance_available` metric, install ENA
  driver version 2.8.1 or later.
- To override the egress fragment PPS limit of 1024, install ENA driver version
  2.13.3 or later.

###### Windows instances

- Install ENA driver version 2.2.2 or later. To verify the installed version,
  use Device Manager as follows.

      1. Open Device Manager by running
       `devmgmt.msc`.
      2. Expand **Network Adapters**.
      3. Choose **Amazon Elastic Network Adapter**,
       **Properties**.
      4. On the **Driver** tab, locate **Driver
       Version**.

  To upgrade your ENA driver, see [Enhanced networking](enhanced-networking-ena.md "enhanced-networking-ena.md").

- To import these metrics to Amazon CloudWatch, install the CloudWatch agent. For more
  information, see [Collect advanced network metrics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-network-performance.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-network-performance.md") in the
  _Amazon CloudWatch User Guide_.

## Metrics for the ENA driver

The ENA driver delivers the following metrics to the instance in real time. They
provide the cumulative number of packets queued or dropped on each network interface
since the last driver reset.

| Metric                          | Description                                                                                                                                                                                                                                                                                                         | Supported on                                                                                                          |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `bw_in_allowance_exceeded`      | The number of packets queued or dropped because the<br>inbound aggregate bandwidth exceeded the maximum for the instance.                                                                                                                                                                                           | All instance types                                                                                                    |
| `bw_out_allowance_exceeded`     | The number of packets queued or dropped because the outbound<br>aggregate bandwidth exceeded the maximum for the instance.                                                                                                                                                                                          | All instance types                                                                                                    |
| `conntrack_allowance_exceeded`  | The number of packets dropped because connection tracking<br>exceeded the maximum for the instance and new connections could not be established. This can<br>result in packet loss for traffic to or from the instance.                                                                                             | All instance types                                                                                                    |
| `conntrack_allowance_available` | The number of tracked connections that can be established<br>by the instance before hitting the Connections Tracked allowance of that instance type.                                                                                                                                                                | [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type") only |
| `linklocal_allowance_exceeded`  | The number of packets dropped because the PPS of the traffic<br>to local proxy services exceeded the maximum for the network interface. This impacts traffic to the<br>Amazon DNS service, the Instance Metadata Service, and the Amazon Time Sync Service, but does<br>not impact traffic to custom DNS resolvers. | All instance types                                                                                                    |
| `pps_allowance_exceeded`        | The number of packets queued or dropped because the bidirectional<br>PPS exceeded the maximum for the instance. \*                                                                                                                                                                                                  | All instance types                                                                                                    |

\* Depending on the fragment proxy mode setting for ENA Linux driver v2.13.3 or
later, this limit can also include egress fragment drops that exceed 1024 PPS for the network interface. If fragment
proxy mode is enabled for the Linux driver, egress fragment drops bypass the 1024 PPS limit that usually applies
and are counted within standard PPS allowances. Fragment proxy mode is disabled by default.

## View the network performance metrics

for your instance

The procedure that you use depends on the operating system of the instance.

You can publish metrics to your favorite tools to visualize the metric data.
For example, you can publish the metrics to Amazon CloudWatch using the CloudWatch agent. The
agent enables you to select individual metrics and control publication.

You can also use the **ethtool** to retrieve the metrics for
each network interface, such as eth0, as follows.

````
`[ec2-user ~]$` `ethtool -S `eth0```bw_in_allowance_exceeded: 0
 bw_out_allowance_exceeded: 0
 pps_allowance_exceeded: 0
 conntrack_allowance_exceeded: 0
 linklocal_allowance_exceeded: 0
 conntrack_allowance_available: 136812`
````

You can view the metrics using any consumer of Windows performance counters.
The data can be parsed according to the EnaPerfCounters manifest. This is an XML
file that defines the performance counter provider and its countersets.

###### To install the manifest

If you launched the instance using an AMI that contains ENA driver 2.2.2
or later, or used the install script in the driver package for ENA driver
2.2.2, the manifest is already installed. To install the manifest manually,
use the following steps:

1. Remove the existing manifest using the following command:

```
unlodctr /m:EnaPerfCounters.man
```

2. Copy the manifest file `EnaPerfCounters.man` from
   the driver installation package to
   `%SystemRoot%\System32\drivers`.
3. Install the new manifest using the following command:

```
lodctr /m:EnaPerfCounters.man
```

###### To view metrics using Performance Monitor

1. Open Performance Monitor.
2. Press Ctrl+N to add new counters.
3. Choose **ENA Packets Shaping** from the list.
4. Select the instances to monitor and choose
   **Add**.
5. Choose **OK**.

## Metrics for ENA

Express

ENA Express is powered by AWS Scalable Reliable Datagram (SRD) technology.
SRD is a high performance network transport protocol that uses dynamic routing
to increase throughput and minimize tail latency. If you've enabled ENA Express for the network interface
attachments on both the sending instance and receiving instance, you can use ENA Express
metrics to help ensure that your instances take full advantage of the performance
improvements that SRD technology provides. For example:

- Evaluate your resources to ensure that they have sufficient capacity to
  establish more SRD connections.
- Identify where there are potential issues that prevent eligible outgoing
  packets from using SRD.
- Calculate the percentage of outgoing traffic that uses SRD for the
  instance.
- Calculate the percentage of incoming traffic that uses SRD for the
  instance.

###### Note

To produce metrics, use driver version 2.8 or higher.

To see a list of metrics for your Linux instance that's filtered for ENA Express, run
the following **ethtool** command for your network interface (shown here
as `eth0`). Take note of the value of the `ena_srd_mode`
metric.

```
`[ec2-user ~]$` `ethtool -S `eth0` | grep ena_srd``NIC statistics:
 ena_srd_mode: 1
 ena_srd_tx_pkts: 0
 ena_srd_eligible_tx_pkts: 0
 ena_srd_rx_pkts: 0
 ena_srd_resource_utilization: 0`
```

The following metrics are available for all instances that have ENA Express
enabled.

**ena_srd_mode**

Describes which ENA Express features are enabled. Values are as
follows:

- `0` = ENA Express off, UDP off
- `1` = ENA Express on, UDP off
- `2` = ENA Express off, UDP on

###### Note

This only happens when ENA Express was originally enabled, and UDP was
configured to use it. The prior value is retained for UDP traffic.

- `3` = ENA Express on, UDP on

**ena_srd_eligible_tx_pkts**

The number of network as follows:

- Both sending and receiving instance types are supported. See the
  [Supported instance types for ENA
  Express](ena-express.md#ena-express-supported-instance-types "ena-express.md#ena-express-supported-instance-types")
  table for more information.
- Both sending and receiving instances must have ENA Express configured.
- The sending and receiving instances must run in the same Availability Zone.
- The network path between the instances must not include middleware boxes. ENA Express
  doesn't currently support middleware boxes.

###### Note

The ENA Express eligibility metric covers source and destination
requirements, and the network between the two endpoints. Eligible
packets can still be disqualified after they’ve already been counted.
For example, if an eligible packet is over the maximum transmission unit
(MTU) limit, it falls back to standard ENA transmission, though the
packet is still reflected as eligible in the counter.

**ena_srd_tx_pkts**

The number of SRD packets transmitted within a given time period.

**ena_srd_rx_pkts**

The number of SRD packets received within a given time period.

**ena_srd_resource_utilization**

The percentage of the maximum allowed memory utilization for concurrent
SRD connections that the instance has consumed.

To confirm if packet transmission is using SRD, you can compare the number of eligible
packets (`ena_srd_eligible_tx_pkts` metric) to the number of SRD packets
transmitted (`ena_srd_tx_pkts` metric) during a given time period.

###### Egress traffic (outgoing packets)

To ensure that your egress traffic uses SRD as expected, compare the number of SRD
eligible packets (`ena_srd_eligible_tx_pkts`) with the number of SRD
packets sent (`ena_srd_tx_pkts`) over a given time period.

Significant differences between the number of eligible packets and the number of SRD
packets sent are often caused by resource utilization issues. When the network card
attached to the instance has used up its maximum resources, or if packets are over the
MTU limit, eligible packets are not able to transmit via SRD, and must fall back to
standard ENA transmission. Packets can also fall into this gap during live migrations or
live server updates. Additional troubleshooting is required to determine the root
cause.

###### Note

You can ignore occasional minor differences between the number of eligible packets
and the number of SRD packets. This can happen when your instance establishes a
connection to another instance for SRD traffic, for example.

To find out what percentage of your total egress traffic over a given time period uses
SRD, compare the number of SRD packets sent (`ena_srd_tx_pkts`) to the total
number of packets sent for the instance (`NetworkPacketOut`) during that
time.

###### Ingress traffic (incoming packets)

To find out what percentage of your ingress traffic uses SRD, compare the number
of SRD packets received (`ena_srd_rx_pkts`) over a given time period to
the total number of packets received for the instance (`NetworkPacketIn`)
during that time.

###### Resource utilization

Resource utilization is based on the number of concurrent SRD connections a single
instance can hold at a given time. The resource utilization metric
(`ena_srd_resource_utilization`) keeps track of your current
utilization for the instance. As utilization approaches 100%, you can expect to see
performance issues. ENA Express falls back from SRD to standard ENA transmission,
and the possibility of dropped packets increases. High resource utilization is a
sign that it’s time to scale the instance out to improve network performance.

###### Note

When the network traffic for an instance exceeds a maximum, AWS shapes the traffic that
exceeds the maximum by queueing and then dropping network packets.

###### Persistence

Egress and ingress metrics accrue while ENA Express is enabled for the instance.
Metrics stop accruing if ENA Express is deactivated, but persist as long as the
instance is still running. Metrics reset if the instance reboots or is terminated,
or if the network interface is detached from the instance.

## Network performance metrics with the

DPDK driver for ENA

The ENA driver version 2.2.0 and later supports network metrics reporting. DPDK 20.11
includes the ENA driver 2.2.0 and is the first DPDK version to support this
feature.

DPDK driver v25.03 or later supports fragment proxy mode. If fragment proxy mode is enabled
for the DPDK driver, egress fragment drops bypass the 1024 PPS limit that usually applies and
are counted within standard PPS allowances. Fragment proxy mode is disabled by default.

You can use an example application to view DPDK statistics. To start an interactive
version of the example application, run the following command.

```
./app/dpdk-testpmd -- -i
```

Within this interactive session, you can enter a command to retrieve extended
statistics for a port. The following example command retrieves the statistics for port 0.

```
show port xstats 0
```

The following is an example of an interactive session with the DPDK example
application.

```
[root@ip-192.0.2.0 build]# ./app/dpdk-testpmd -- -i
        EAL: Detected 4 lcore(s)
        EAL: Detected 1 NUMA nodes
        EAL: Multi-process socket /var/run/dpdk/rte/mp_socket
        EAL: Selected IOVA mode 'PA'
        EAL: Probing VFIO support...
        EAL:   Invalid NUMA socket, default to 0
        EAL:   Invalid NUMA socket, default to 0
        EAL: Probe PCI driver: net_ena (1d0f:ec20) device: 0000:00:06.0
(socket 0)
        EAL: No legacy callbacks, legacy socket not created
        Interactive-mode selected

        Port 0: link state change event
        testpmd: create a new mbuf pool <mb_pool_0>: n=171456,
size=2176, socket=0
        testpmd: preferred mempool ops selected: ring_mp_mc

        Warning! port-topology=paired and odd forward ports number, the
last port will pair with itself.

        Configuring Port 0 (socket 0)
        Port 0: 02:C7:17:A2:60:B1
        Checking link statuses...
        Done
        Error during enabling promiscuous mode for port 0: Operation
not supported - ignore
        testpmd> show port xstats 0
        ###### NIC extended statistics for port 0
        rx_good_packets: 0
        tx_good_packets: 0
        rx_good_bytes: 0
        tx_good_bytes: 0
        rx_missed_errors: 0
        rx_errors: 0
        tx_errors: 0
        rx_mbuf_allocation_errors: 0
        rx_q0_packets: 0
        rx_q0_bytes: 0
        rx_q0_errors: 0
        tx_q0_packets: 0
        tx_q0_bytes: 0
        wd_expired: 0
        dev_start: 1
        dev_stop: 0
        tx_drops: 0
        bw_in_allowance_exceeded: 0
        bw_out_allowance_exceeded: 0
        pps_allowance_exceeded: 0
        conntrack_allowance_exceeded: 0
        linklocal_allowance_exceeded: 0
        rx_q0_cnt: 0
        rx_q0_bytes: 0
        rx_q0_refill_partial: 0
        rx_q0_bad_csum: 0
        rx_q0_mbuf_alloc_fail: 0
        rx_q0_bad_desc_num: 0
        rx_q0_bad_req_id: 0
        tx_q0_cnt: 0
        tx_q0_bytes: 0
        tx_q0_prepare_ctx_err: 0
        tx_q0_linearize: 0
        tx_q0_linearize_failed: 0
        tx_q0_tx_poll: 0
        tx_q0_doorbells: 0
        tx_q0_bad_req_id: 0
        tx_q0_available_desc: 1023
        testpmd>
```

For more information about the example application and using it to retrieve extended
statistics. see [Testpmd
Application User Guide](https://doc.dpdk.org/guides/testpmd_app_ug/ "https://doc.dpdk.org/guides/testpmd_app_ug/") in the DPDK documentation.

## Metrics on instances running

FreeBSD

Starting with version 2.3.0, the ENA FreeBSD driver supports collecting
network performance metrics on instances running FreeBSD. To enable the
collection of FreeBSD metrics, enter the following command and set
`interval` to a value between 1 and 3600. This specifies
how often, in seconds, to collect FreeBSD metrics.

```
sysctl dev.ena.`network_interface`.eni_metrics.sample_interval=`interval`
```

For example, the following command sets the driver to collect FreeBSD
metrics on network interface 1 every 10 seconds:

```
sysctl dev.ena.1.eni_metrics.sample_interval=10
```

To turn off the collection of FreeBSD metrics, you can run the
preceding command and specify `0` as the
`interval`.

After you enable collecting FreeBSD metrics, you can retrieve the
latest set of collected metrics by running the following command.

```
sysctl dev.ena.`network_interface`.eni_metrics
```
