# Improve network performance between EC2 instances with ENA Express

ENA Express is powered by AWS Scalable Reliable Datagram (SRD) technology.
SRD is a high performance network transport protocol that uses dynamic routing
to increase throughput and minimize tail latency. With ENA Express, you can communicate between two EC2 instances in
the same Availability Zone or across Availability Zones within the same Region.

###### Benefits of ENA Express

- Increases the maximum bandwidth a single flow can use from 5 Gbps up to 25 Gbps
  within the same Region, up to the aggregate instance limit.
- Reduces tail latency of network traffic between EC2 instances in the same
  Availability Zone, especially during periods of high network load.
- Detects and avoids congested network paths.
- Handles some tasks directly in the network layer, such as packet reordering on the
  receiving end, and most retransmits that are needed. This frees up the application
  layer for other work.

###### Note

- If your application has high packets-per-second requirements and needs to
  optimize for latency during uncongested periods, [Enhanced networking](enhanced-networking.md "enhanced-networking.md") might be a better
  fit.
- ENA Express traffic can't be sent in a Local Zone.
- ENA Express support for traffic between Availability Zones is not available
  in South America (São Paulo), Middle East (Bahrain), and
  Middle East (UAE).
  After you've enabled ENA Express for the network interface attachment on an instance, the
  sending instance initiates communication with the receiving instance, and SRD detects if ENA
  Express is operating on both the sending instance and the receiving instance. If ENA Express
  is operating, the communication can use SRD transmission. If ENA Express is not operating,
  the communication falls back to standard ENA transmission.

During periods of time when network traffic is light, you might notice a slight increase
in median packet latency (tens of microseconds) when the packet uses ENA Express. During those
times, applications that prioritize specific network performance characteristics can benefit
from ENA Express as follows:

- Processes can benefit from increased maximum single flow bandwidth from 5 Gbps up
  to 25 Gbps within the same Region, up to the aggregate instance limit.
  For example, if a specific instance type supports up to 12.5 Gbps, the single flow
  bandwidth is also limited to 12.5 Gbps.
- Longer running processes in the same Availability Zone will experience reduced
  tail latency during periods of network congestion.
- Processes can benefit from a smoother and more standard distribution for network
  response times.

###### Topics

- [How ENA Express works](#ena-express-how-it-works "#ena-express-how-it-works")
- [Supported instance types for ENA Express](#ena-express-supported-instance-types "#ena-express-supported-instance-types")
- [Tune performance for ENA Express settings on Linux instances](#ena-express-tune "#ena-express-tune")
- [Review ENA Express settings for your EC2 instance](ena-express-list-view.md "ena-express-list-view.md")
- [Configure ENA Express settings for your EC2 instance](ena-express-configure.md "ena-express-configure.md")

## How ENA Express works

ENA Express is powered by AWS Scalable Reliable Datagram (SRD) technology. It distributes packets for each network flow across
different AWS network paths, and dynamically adjusts distribution when it detects
signs of congestion. It also manages packet reordering on the receiving end.

To ensure that ENA Express can manage network traffic as intended, sending and
receiving instances and the communication between them must meet all of the following
requirements:

- Both sending and receiving instance types are supported. See the
  [Supported instance types for ENA Express](#ena-express-supported-instance-types "#ena-express-supported-instance-types")
  table for more information.
- Both sending and receiving instances must have ENA Express configured. If there are differences in the configuration, you can run into situations
  where traffic defaults to standard ENA transmission. The following scenario shows what can happen.

**Scenario: Differences in configuration**

| Instance   | ENA Express Enabled | UDP uses ENA Express |
| ---------- | ------------------- | -------------------- |
| Instance 1 | Yes                 | Yes                  |
| Instance 2 | Yes                 | No                   |

In this case, TCP traffic between the two instances can use ENA Express, as both
instances have enabled it. However, since one of the instances does not use ENA Express
for UDP traffic, communication between these two instances over UDP uses standard ENA
transmission.

- The sending and receiving instances must run in the same Region.
- The network path between the instances must not include middleware boxes. ENA Express
  doesn't currently support middleware boxes.
- (Linux instances only) To utilize full bandwidth potential, use driver version 2.2.9 or higher.
- (Linux instances only) To produce metrics, use driver version 2.8 or higher.

If any requirement is unmet, the instances use the standard TCP/UDP protocol but
without SRD to communicate.

To ensure that your instance network driver is configured for optimum performance,
review the recommended best practices for ENA drivers. These best practices apply to ENA
Express, as well. For more information, see the [ENA Linux Driver Best Practices and Performance Optimization Guide](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst "https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst") on the
GitHub website.

###### Note

Amazon EC2 refers to the relationship between an instance and a network interface
that's attached to it as an _attachment_. ENA Express settings
apply to the attachment. If the network interface is detached from the instance, the
attachment no longer exists, and the ENA Express settings that applied to it are no
longer in force. The same is true when an instance is terminated, even if the
network interface remains.

After you've enabled ENA Express for the network interface attachments on both the
sending instance and the receiving instance, you can use ENA Express metrics to help
ensure that your instances take full advantage of the performance improvements that SRD
technology provides. For more information about ENA Express metrics, see [Metrics for ENA Express](monitoring-network-performance-ena.md#network-performance-metrics-ena-express "monitoring-network-performance-ena.md#network-performance-metrics-ena-express").

## Supported instance types for ENA Express

The following instance types support ENA Express.

General purpose

| Instance type      | Architecture |
| ------------------ | ------------ |
| `m6a.12xlarge`     | x86\_64      |
| `m6a.16xlarge`     | x86\_64      |
| `m6a.24xlarge`     | x86\_64      |
| `m6a.32xlarge`     | x86\_64      |
| `m6a.48xlarge`     | x86\_64      |
| `m6a.metal`        | x86\_64      |
| `m6i.8xlarge`      | x86\_64      |
| `m6i.12xlarge`     | x86\_64      |
| `m6i.16xlarge`     | x86\_64      |
| `m6i.24xlarge`     | x86\_64      |
| `m6i.32xlarge`     | x86\_64      |
| `m6i.metal`        | x86\_64      |
| `m6id.8xlarge`     | x86\_64      |
| `m6id.12xlarge`    | x86\_64      |
| `m6id.16xlarge`    | x86\_64      |
| `m6id.24xlarge`    | x86\_64      |
| `m6id.32xlarge`    | x86\_64      |
| `m6id.metal`       | x86\_64      |
| `m6idn.8xlarge`    | x86\_64      |
| `m6idn.12xlarge`   | x86\_64      |
| `m6idn.16xlarge`   | x86\_64      |
| `m6idn.24xlarge`   | x86\_64      |
| `m6idn.32xlarge`   | x86\_64      |
| `m6idn.metal`      | x86\_64      |
| `m6in.8xlarge`     | x86\_64      |
| `m6in.12xlarge`    | x86\_64      |
| `m6in.16xlarge`    | x86\_64      |
| `m6in.24xlarge`    | x86\_64      |
| `m6in.32xlarge`    | x86\_64      |
| `m6in.metal`       | x86\_64      |
| `m7a.12xlarge`     | x86\_64      |
| `m7a.16xlarge`     | x86\_64      |
| `m7a.24xlarge`     | x86\_64      |
| `m7a.32xlarge`     | x86\_64      |
| `m7a.48xlarge`     | x86\_64      |
| `m7a.metal-48xl`   | x86\_64      |
| `m7g.12xlarge`     | arm64        |
| `m7g.16xlarge`     | arm64        |
| `m7g.metal`        | arm64        |
| `m7gd.12xlarge`    | arm64        |
| `m7gd.16xlarge`    | arm64        |
| `m7gd.metal`       | arm64        |
| `m7i.12xlarge`     | x86\_64      |
| `m7i.16xlarge`     | x86\_64      |
| `m7i.24xlarge`     | x86\_64      |
| `m7i.48xlarge`     | x86\_64      |
| `m7i.metal-24xl`   | x86\_64      |
| `m7i.metal-48xl`   | x86\_64      |
| `m8a.16xlarge`     | x86\_64      |
| `m8a.24xlarge`     | x86\_64      |
| `m8a.48xlarge`     | x86\_64      |
| `m8a.metal-24xl`   | x86\_64      |
| `m8a.metal-48xl`   | x86\_64      |
| `m8azn.12xlarge`   | x86\_64      |
| `m8azn.24xlarge`   | x86\_64      |
| `m8azn.metal-12xl` | x86\_64      |
| `m8azn.metal-24xl` | x86\_64      |
| `m8g.8xlarge`      | arm64        |
| `m8g.12xlarge`     | arm64        |
| `m8g.16xlarge`     | arm64        |
| `m8g.24xlarge`     | arm64        |
| `m8g.48xlarge`     | arm64        |
| `m8g.metal-24xl`   | arm64        |
| `m8g.metal-48xl`   | arm64        |
| `m8gb.4xlarge`     | arm64        |
| `m8gb.8xlarge`     | arm64        |
| `m8gb.12xlarge`    | arm64        |
| `m8gb.16xlarge`    | arm64        |
| `m8gb.24xlarge`    | arm64        |
| `m8gb.48xlarge`    | arm64        |
| `m8gb.metal-24xl`  | arm64        |
| `m8gb.metal-48xl`  | arm64        |
| `m8gd.8xlarge`     | arm64        |
| `m8gd.12xlarge`    | arm64        |
| `m8gd.16xlarge`    | arm64        |
| `m8gd.24xlarge`    | arm64        |
| `m8gd.48xlarge`    | arm64        |
| `m8gd.metal-24xl`  | arm64        |
| `m8gd.metal-48xl`  | arm64        |
| `m8gn.4xlarge`     | arm64        |
| `m8gn.8xlarge`     | arm64        |
| `m8gn.12xlarge`    | arm64        |
| `m8gn.16xlarge`    | arm64        |
| `m8gn.24xlarge`    | arm64        |
| `m8gn.48xlarge`    | arm64        |
| `m8gn.metal-24xl`  | arm64        |
| `m8gn.metal-48xl`  | arm64        |
| `m8i.8xlarge`      | x86\_64      |
| `m8i.12xlarge`     | x86\_64      |
| `m8i.16xlarge`     | x86\_64      |
| `m8i.24xlarge`     | x86\_64      |
| `m8i.32xlarge`     | x86\_64      |
| `m8i.48xlarge`     | x86\_64      |
| `m8i.96xlarge`     | x86\_64      |
| `m8i.metal-48xl`   | x86\_64      |
| `m8i.metal-96xl`   | x86\_64      |
| `m8id.8xlarge`     | x86\_64      |
| `m8id.12xlarge`    | x86\_64      |
| `m8id.16xlarge`    | x86\_64      |
| `m8id.24xlarge`    | x86\_64      |
| `m8id.32xlarge`    | x86\_64      |
| `m8id.48xlarge`    | x86\_64      |
| `m8id.96xlarge`    | x86\_64      |
| `m8id.metal-48xl`  | x86\_64      |
| `m8id.metal-96xl`  | x86\_64      |
| `m8in.8xlarge`     | x86\_64      |
| `m8in.12xlarge`    | x86\_64      |
| `m8in.16xlarge`    | x86\_64      |
| `m8in.24xlarge`    | x86\_64      |
| `m8in.32xlarge`    | x86\_64      |
| `m8in.48xlarge`    | x86\_64      |
| `m8in.96xlarge`    | x86\_64      |
| `m8in.metal-48xl`  | x86\_64      |
| `m8in.metal-96xl`  | x86\_64      |
| `m8idn.8xlarge`    | x86\_64      |
| `m8idn.12xlarge`   | x86\_64      |
| `m8idn.16xlarge`   | x86\_64      |
| `m8idn.24xlarge`   | x86\_64      |
| `m8idn.32xlarge`   | x86\_64      |
| `m8idn.48xlarge`   | x86\_64      |
| `m8idn.96xlarge`   | x86\_64      |
| `m8idn.metal-48xl` | x86\_64      |
| `m8idn.metal-96xl` | x86\_64      |
| `m8ib.8xlarge`     | x86\_64      |
| `m8ib.12xlarge`    | x86\_64      |
| `m8ib.16xlarge`    | x86\_64      |
| `m8ib.24xlarge`    | x86\_64      |
| `m8ib.32xlarge`    | x86\_64      |
| `m8ib.48xlarge`    | x86\_64      |
| `m8ib.96xlarge`    | x86\_64      |
| `m8ib.metal-48xl`  | x86\_64      |
| `m8ib.metal-96xl`  | x86\_64      |
| `m8idb.8xlarge`    | x86\_64      |
| `m8idb.12xlarge`   | x86\_64      |
| `m8idb.16xlarge`   | x86\_64      |
| `m8idb.24xlarge`   | x86\_64      |
| `m8idb.32xlarge`   | x86\_64      |
| `m8idb.48xlarge`   | x86\_64      |
| `m8idb.96xlarge`   | x86\_64      |
| `m8idb.metal-48xl` | x86\_64      |
| `m8idb.metal-96xl` | x86\_64      |
| `m9g.8xlarge`      | arm64        |
| `m9g.12xlarge`     | arm64        |
| `m9g.16xlarge`     | arm64        |
| `m9g.24xlarge`     | arm64        |
| `m9g.48xlarge`     | arm64        |
| `m9g.metal-48xl`   | arm64        |
| `m9gd.8xlarge`     | arm64        |
| `m9gd.12xlarge`    | arm64        |
| `m9gd.16xlarge`    | arm64        |
| `m9gd.24xlarge`    | arm64        |
| `m9gd.48xlarge`    | arm64        |
| `m9gd.metal-48xl`  | arm64        |

Compute optimized

| Instance type     | Architecture |
| ----------------- | ------------ |
| `c6a.12xlarge`    | x86\_64      |
| `c6a.16xlarge`    | x86\_64      |
| `c6a.24xlarge`    | x86\_64      |
| `c6a.32xlarge`    | x86\_64      |
| `c6a.48xlarge`    | x86\_64      |
| `c6a.metal`       | x86\_64      |
| `c6gn.4xlarge`    | arm64        |
| `c6gn.8xlarge`    | arm64        |
| `c6gn.12xlarge`   | arm64        |
| `c6gn.16xlarge`   | arm64        |
| `c6i.8xlarge`     | x86\_64      |
| `c6i.12xlarge`    | x86\_64      |
| `c6i.16xlarge`    | x86\_64      |
| `c6i.24xlarge`    | x86\_64      |
| `c6i.32xlarge`    | x86\_64      |
| `c6i.metal`       | x86\_64      |
| `c6id.8xlarge`    | x86\_64      |
| `c6id.12xlarge`   | x86\_64      |
| `c6id.16xlarge`   | x86\_64      |
| `c6id.24xlarge`   | x86\_64      |
| `c6id.32xlarge`   | x86\_64      |
| `c6id.metal`      | x86\_64      |
| `c6in.8xlarge`    | x86\_64      |
| `c6in.12xlarge`   | x86\_64      |
| `c6in.16xlarge`   | x86\_64      |
| `c6in.24xlarge`   | x86\_64      |
| `c6in.32xlarge`   | x86\_64      |
| `c6in.metal`      | x86\_64      |
| `c7a.12xlarge`    | x86\_64      |
| `c7a.16xlarge`    | x86\_64      |
| `c7a.24xlarge`    | x86\_64      |
| `c7a.32xlarge`    | x86\_64      |
| `c7a.48xlarge`    | x86\_64      |
| `c7a.metal-48xl`  | x86\_64      |
| `c7g.12xlarge`    | arm64        |
| `c7g.16xlarge`    | arm64        |
| `c7g.metal`       | arm64        |
| `c7gd.12xlarge`   | arm64        |
| `c7gd.16xlarge`   | arm64        |
| `c7gd.metal`      | arm64        |
| `c7gn.4xlarge`    | arm64        |
| `c7gn.8xlarge`    | arm64        |
| `c7gn.12xlarge`   | arm64        |
| `c7gn.16xlarge`   | arm64        |
| `c7gn.metal`      | arm64        |
| `c7i.12xlarge`    | x86\_64      |
| `c7i.16xlarge`    | x86\_64      |
| `c7i.24xlarge`    | x86\_64      |
| `c7i.48xlarge`    | x86\_64      |
| `c7i.metal-24xl`  | x86\_64      |
| `c7i.metal-48xl`  | x86\_64      |
| `c8a.16xlarge`    | x86\_64      |
| `c8a.24xlarge`    | x86\_64      |
| `c8a.48xlarge`    | x86\_64      |
| `c8a.metal-24xl`  | x86\_64      |
| `c8a.metal-48xl`  | x86\_64      |
| `c8g.8xlarge`     | arm64        |
| `c8g.12xlarge`    | arm64        |
| `c8g.16xlarge`    | arm64        |
| `c8g.24xlarge`    | arm64        |
| `c8g.48xlarge`    | arm64        |
| `c8g.metal-24xl`  | arm64        |
| `c8g.metal-48xl`  | arm64        |
| `c8gb.4xlarge`    | arm64        |
| `c8gb.8xlarge`    | arm64        |
| `c8gb.12xlarge`   | arm64        |
| `c8gb.16xlarge`   | arm64        |
| `c8gb.24xlarge`   | arm64        |
| `c8gb.48xlarge`   | arm64        |
| `c8gb.metal-24xl` | arm64        |
| `c8gb.metal-48xl` | arm64        |
| `c8gd.8xlarge`    | arm64        |
| `c8gd.12xlarge`   | arm64        |
| `c8gd.16xlarge`   | arm64        |
| `c8gd.24xlarge`   | arm64        |
| `c8gd.48xlarge`   | arm64        |
| `c8gd.metal-24xl` | arm64        |
| `c8gd.metal-48xl` | arm64        |
| `c8gn.4xlarge`    | arm64        |
| `c8gn.8xlarge`    | arm64        |
| `c8gn.12xlarge`   | arm64        |
| `c8gn.16xlarge`   | arm64        |
| `c8gn.24xlarge`   | arm64        |
| `c8gn.48xlarge`   | arm64        |
| `c8gn.metal-24xl` | arm64        |
| `c8gn.metal-48xl` | arm64        |
| `c8i.8xlarge`     | x86\_64      |
| `c8i.12xlarge`    | x86\_64      |
| `c8i.16xlarge`    | x86\_64      |
| `c8i.24xlarge`    | x86\_64      |
| `c8i.32xlarge`    | x86\_64      |
| `c8i.48xlarge`    | x86\_64      |
| `c8i.96xlarge`    | x86\_64      |
| `c8i.metal-48xl`  | x86\_64      |
| `c8i.metal-96xl`  | x86\_64      |
| `c8id.8xlarge`    | x86\_64      |
| `c8id.12xlarge`   | x86\_64      |
| `c8id.16xlarge`   | x86\_64      |
| `c8id.24xlarge`   | x86\_64      |
| `c8id.32xlarge`   | x86\_64      |
| `c8id.48xlarge`   | x86\_64      |
| `c8id.96xlarge`   | x86\_64      |
| `c8id.metal-48xl` | x86\_64      |
| `c8id.metal-96xl` | x86\_64      |
| `c8in.8xlarge`    | x86\_64      |
| `c8in.12xlarge`   | x86\_64      |
| `c8in.16xlarge`   | x86\_64      |
| `c8in.24xlarge`   | x86\_64      |
| `c8in.32xlarge`   | x86\_64      |
| `c8in.48xlarge`   | x86\_64      |
| `c8in.96xlarge`   | x86\_64      |
| `c8in.metal-48xl` | x86\_64      |
| `c8in.metal-96xl` | x86\_64      |
| `c8ib.8xlarge`    | x86\_64      |
| `c8ib.12xlarge`   | x86\_64      |
| `c8ib.16xlarge`   | x86\_64      |
| `c8ib.24xlarge`   | x86\_64      |
| `c8ib.32xlarge`   | x86\_64      |
| `c8ib.48xlarge`   | x86\_64      |
| `c8ib.96xlarge`   | x86\_64      |
| `c8ib.metal-48xl` | x86\_64      |
| `c8ib.metal-96xl` | x86\_64      |
| `c9g.8xlarge`     | arm64        |
| `c9g.12xlarge`    | arm64        |
| `c9g.16xlarge`    | arm64        |
| `c9g.24xlarge`    | arm64        |
| `c9g.48xlarge`    | arm64        |
| `c9g.metal-48xl`  | arm64        |
| `c9gd.8xlarge`    | arm64        |
| `c9gd.12xlarge`   | arm64        |
| `c9gd.16xlarge`   | arm64        |
| `c9gd.24xlarge`   | arm64        |
| `c9gd.48xlarge`   | arm64        |
| `c9gd.metal-48xl` | arm64        |

Memory optimized

| Instance type          | Architecture |
| ---------------------- | ------------ |
| `r6a.12xlarge`         | x86\_64      |
| `r6a.16xlarge`         | x86\_64      |
| `r6a.24xlarge`         | x86\_64      |
| `r6a.32xlarge`         | x86\_64      |
| `r6a.48xlarge`         | x86\_64      |
| `r6a.metal`            | x86\_64      |
| `r6i.8xlarge`          | x86\_64      |
| `r6i.12xlarge`         | x86\_64      |
| `r6i.16xlarge`         | x86\_64      |
| `r6i.24xlarge`         | x86\_64      |
| `r6i.32xlarge`         | x86\_64      |
| `r6i.metal`            | x86\_64      |
| `r6id.8xlarge`         | x86\_64      |
| `r6id.12xlarge`        | x86\_64      |
| `r6id.16xlarge`        | x86\_64      |
| `r6id.24xlarge`        | x86\_64      |
| `r6id.32xlarge`        | x86\_64      |
| `r6id.metal`           | x86\_64      |
| `r6idn.8xlarge`        | x86\_64      |
| `r6idn.12xlarge`       | x86\_64      |
| `r6idn.16xlarge`       | x86\_64      |
| `r6idn.24xlarge`       | x86\_64      |
| `r6idn.32xlarge`       | x86\_64      |
| `r6idn.metal`          | x86\_64      |
| `r6in.8xlarge`         | x86\_64      |
| `r6in.12xlarge`        | x86\_64      |
| `r6in.16xlarge`        | x86\_64      |
| `r6in.24xlarge`        | x86\_64      |
| `r6in.32xlarge`        | x86\_64      |
| `r6in.metal`           | x86\_64      |
| `r7a.12xlarge`         | x86\_64      |
| `r7a.16xlarge`         | x86\_64      |
| `r7a.24xlarge`         | x86\_64      |
| `r7a.32xlarge`         | x86\_64      |
| `r7a.48xlarge`         | x86\_64      |
| `r7a.metal-48xl`       | x86\_64      |
| `r7g.12xlarge`         | arm64        |
| `r7g.16xlarge`         | arm64        |
| `r7g.metal`            | arm64        |
| `r7gd.12xlarge`        | arm64        |
| `r7gd.16xlarge`        | arm64        |
| `r7gd.metal`           | arm64        |
| `r7i.12xlarge`         | x86\_64      |
| `r7i.16xlarge`         | x86\_64      |
| `r7i.24xlarge`         | x86\_64      |
| `r7i.48xlarge`         | x86\_64      |
| `r7i.metal-24xl`       | x86\_64      |
| `r7i.metal-48xl`       | x86\_64      |
| `r7iz.8xlarge`         | x86\_64      |
| `r7iz.12xlarge`        | x86\_64      |
| `r7iz.16xlarge`        | x86\_64      |
| `r7iz.32xlarge`        | x86\_64      |
| `r7iz.metal-16xl`      | x86\_64      |
| `r7iz.metal-32xl`      | x86\_64      |
| `r8a.16xlarge`         | x86\_64      |
| `r8a.24xlarge`         | x86\_64      |
| `r8a.48xlarge`         | x86\_64      |
| `r8a.metal-24xl`       | x86\_64      |
| `r8a.metal-48xl`       | x86\_64      |
| `r8g.8xlarge`          | arm64        |
| `r8g.12xlarge`         | arm64        |
| `r8g.16xlarge`         | arm64        |
| `r8g.24xlarge`         | arm64        |
| `r8g.48xlarge`         | arm64        |
| `r8g.metal-24xl`       | arm64        |
| `r8g.metal-48xl`       | arm64        |
| `r8gb.4xlarge`         | arm64        |
| `r8gb.8xlarge`         | arm64        |
| `r8gb.12xlarge`        | arm64        |
| `r8gb.16xlarge`        | arm64        |
| `r8gb.24xlarge`        | arm64        |
| `r8gb.48xlarge`        | arm64        |
| `r8gb.metal-24xl`      | arm64        |
| `r8gb.metal-48xl`      | arm64        |
| `r8gd.8xlarge`         | arm64        |
| `r8gd.12xlarge`        | arm64        |
| `r8gd.16xlarge`        | arm64        |
| `r8gd.24xlarge`        | arm64        |
| `r8gd.48xlarge`        | arm64        |
| `r8gd.metal-24xl`      | arm64        |
| `r8gd.metal-48xl`      | arm64        |
| `r8gn.4xlarge`         | arm64        |
| `r8gn.8xlarge`         | arm64        |
| `r8gn.12xlarge`        | arm64        |
| `r8gn.16xlarge`        | arm64        |
| `r8gn.24xlarge`        | arm64        |
| `r8gn.48xlarge`        | arm64        |
| `r8gn.metal-24xl`      | arm64        |
| `r8gn.metal-48xl`      | arm64        |
| `r8i.8xlarge`          | x86\_64      |
| `r8i.12xlarge`         | x86\_64      |
| `r8i.16xlarge`         | x86\_64      |
| `r8i.24xlarge`         | x86\_64      |
| `r8i.32xlarge`         | x86\_64      |
| `r8i.48xlarge`         | x86\_64      |
| `r8i.96xlarge`         | x86\_64      |
| `r8i.metal-48xl`       | x86\_64      |
| `r8i.metal-96xl`       | x86\_64      |
| `r8id.8xlarge`         | x86\_64      |
| `r8id.12xlarge`        | x86\_64      |
| `r8id.16xlarge`        | x86\_64      |
| `r8id.24xlarge`        | x86\_64      |
| `r8id.32xlarge`        | x86\_64      |
| `r8id.48xlarge`        | x86\_64      |
| `r8id.96xlarge`        | x86\_64      |
| `r8id.metal-48xl`      | x86\_64      |
| `r8id.metal-96xl`      | x86\_64      |
| `r8in.8xlarge`         | x86\_64      |
| `r8in.12xlarge`        | x86\_64      |
| `r8in.16xlarge`        | x86\_64      |
| `r8in.24xlarge`        | x86\_64      |
| `r8in.32xlarge`        | x86\_64      |
| `r8in.48xlarge`        | x86\_64      |
| `r8in.96xlarge`        | x86\_64      |
| `r8in.metal-48xl`      | x86\_64      |
| `r8in.metal-96xl`      | x86\_64      |
| `r8idn.8xlarge`        | x86\_64      |
| `r8idn.12xlarge`       | x86\_64      |
| `r8idn.16xlarge`       | x86\_64      |
| `r8idn.24xlarge`       | x86\_64      |
| `r8idn.32xlarge`       | x86\_64      |
| `r8idn.48xlarge`       | x86\_64      |
| `r8idn.96xlarge`       | x86\_64      |
| `r8idn.metal-48xl`     | x86\_64      |
| `r8idn.metal-96xl`     | x86\_64      |
| `r8ib.8xlarge`         | x86\_64      |
| `r8ib.12xlarge`        | x86\_64      |
| `r8ib.16xlarge`        | x86\_64      |
| `r8ib.24xlarge`        | x86\_64      |
| `r8ib.32xlarge`        | x86\_64      |
| `r8ib.48xlarge`        | x86\_64      |
| `r8ib.96xlarge`        | x86\_64      |
| `r8ib.metal-48xl`      | x86\_64      |
| `r8ib.metal-96xl`      | x86\_64      |
| `r8idb.8xlarge`        | x86\_64      |
| `r8idb.12xlarge`       | x86\_64      |
| `r8idb.16xlarge`       | x86\_64      |
| `r8idb.24xlarge`       | x86\_64      |
| `r8idb.32xlarge`       | x86\_64      |
| `r8idb.48xlarge`       | x86\_64      |
| `r8idb.96xlarge`       | x86\_64      |
| `r8idb.metal-48xl`     | x86\_64      |
| `r8idb.metal-96xl`     | x86\_64      |
| `u7i-6tb.112xlarge`    | x86\_64      |
| `u7i-8tb.112xlarge`    | x86\_64      |
| `u7i-12tb.224xlarge`   | x86\_64      |
| `u7in-16tb.224xlarge`  | x86\_64      |
| `u7in-24tb.224xlarge`  | x86\_64      |
| `u7in-32tb.224xlarge`  | x86\_64      |
| `u7inh-32tb.480xlarge` | x86\_64      |
| `x2idn.16xlarge`       | x86\_64      |
| `x2idn.24xlarge`       | x86\_64      |
| `x2idn.32xlarge`       | x86\_64      |
| `x2idn.metal`          | x86\_64      |
| `x2iedn.8xlarge`       | x86\_64      |
| `x2iedn.16xlarge`      | x86\_64      |
| `x2iedn.24xlarge`      | x86\_64      |
| `x2iedn.32xlarge`      | x86\_64      |
| `x2iedn.metal`         | x86\_64      |
| `x8g.8xlarge`          | arm64        |
| `x8g.12xlarge`         | arm64        |
| `x8g.16xlarge`         | arm64        |
| `x8g.24xlarge`         | arm64        |
| `x8g.48xlarge`         | arm64        |
| `x8g.metal-24xl`       | arm64        |
| `x8g.metal-48xl`       | arm64        |
| `x8aedz.24xlarge`      | x86\_64      |
| `x8aedz.metal-24xl`    | x86\_64      |
| `x8i.8xlarge`          | x86\_64      |
| `x8i.12xlarge`         | x86\_64      |
| `x8i.16xlarge`         | x86\_64      |
| `x8i.24xlarge`         | x86\_64      |
| `x8i.32xlarge`         | x86\_64      |
| `x8i.48xlarge`         | x86\_64      |
| `x8i.64xlarge`         | x86\_64      |
| `x8i.96xlarge`         | x86\_64      |
| `x8i.metal-48xl`       | x86\_64      |
| `x8i.metal-96xl`       | x86\_64      |

Accelerated computing

| Instance type        | Architecture |
| -------------------- | ------------ |
| `g6.48xlarge`        | x86\_64      |
| `g6e.12xlarge`       | x86\_64      |
| `g6e.24xlarge`       | x86\_64      |
| `g6e.48xlarge`       | x86\_64      |
| `g7.24xlarge`        | x86\_64      |
| `g7.48xlarge`        | x86\_64      |
| `g7e.12xlarge`       | x86\_64      |
| `g7e.24xlarge`       | x86\_64      |
| `g7e.48xlarge`       | x86\_64      |
| `p5.4xlarge`         | x86\_64      |
| `p5.48xlarge`        | x86\_64      |
| `p5e.48xlarge`       | x86\_64      |
| `p5en.48xlarge`      | x86\_64      |
| `p6-b200.48xlarge`   | x86\_64      |
| `p6-b300.48xlarge`   | x86\_64      |
| `p6e-gb200.36xlarge` | arm64        |

Storage optimized

| Instance type     | Architecture |
| ----------------- | ------------ |
| `i4g.4xlarge`     | arm64        |
| `i4g.8xlarge`     | arm64        |
| `i4g.16xlarge`    | arm64        |
| `i4i.8xlarge`     | x86\_64      |
| `i4i.12xlarge`    | x86\_64      |
| `i4i.16xlarge`    | x86\_64      |
| `i4i.24xlarge`    | x86\_64      |
| `i4i.32xlarge`    | x86\_64      |
| `i4i.metal`       | x86\_64      |
| `i7i.12xlarge`    | x86\_64      |
| `i7i.16xlarge`    | x86\_64      |
| `i7i.24xlarge`    | x86\_64      |
| `i7i.48xlarge`    | x86\_64      |
| `i7i.metal-24xl`  | x86\_64      |
| `i7i.metal-48xl`  | x86\_64      |
| `i7ie.6xlarge`    | x86\_64      |
| `i7ie.12xlarge`   | x86\_64      |
| `i7ie.18xlarge`   | x86\_64      |
| `i7ie.24xlarge`   | x86\_64      |
| `i7ie.48xlarge`   | x86\_64      |
| `i7ie.metal-24xl` | x86\_64      |
| `i7ie.metal-48xl` | x86\_64      |
| `i8g.8xlarge`     | arm64        |
| `i8g.12xlarge`    | arm64        |
| `i8g.16xlarge`    | arm64        |
| `i8g.24xlarge`    | arm64        |
| `i8g.48xlarge`    | arm64        |
| `i8g.metal-24xl`  | arm64        |
| `i8g.metal-48xl`  | arm64        |
| `i8ge.6xlarge`    | arm64        |
| `i8ge.12xlarge`   | arm64        |
| `i8ge.18xlarge`   | arm64        |
| `i8ge.24xlarge`   | arm64        |
| `i8ge.48xlarge`   | arm64        |
| `i8ge.metal-24xl` | arm64        |
| `i8ge.metal-48xl` | arm64        |
| `im4gn.4xlarge`   | arm64        |
| `im4gn.8xlarge`   | arm64        |
| `im4gn.16xlarge`  | arm64        |

## Tune performance for ENA Express settings on Linux instances

To ensure that ENA Express can operate effectively, your Linux instance must meet
several network configuration requirements.

Rather than configuring each setting manually, you can download and run the ENA
Express settings check script from the Amazon GitHub repository. The script
validates your instance against the required and recommended settings for ENA
Express, and outputs the exact commands to fix any issues it finds.

[https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express-settings.sh](https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express-settings.sh "https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express-settings.sh")

The script checks the following settings and configurations:

- **MTU size** – ENA Express
  requires a lower MTU than the default to accommodate
  additional AWS SRD headers. Newly established TCP connections automatically
  clamp the MSS to mitigate this, but UDP traffic still requires a lower
  MTU.
- **TCP output queue size limit** –
  Checks that the per-socket in-flight byte limit is sufficient to sustain
  high throughput. Environments with increased network latency require a
  higher limit.
- **Byte queue limit** –
  Confirms that the byte queue limit (BQL) is disabled on the network
  interface. BQL can restrict the amount of data queued for device-level
  transmission, which limits ENA Express performance.

###### Note

The ENA driver for the Amazon Linux distribution disables byte queue limits
by default.

- **TCP autocorking** –
  Checks whether TCP autocorking is disabled. Disabling autocorking can reduce
  latency for certain ENA Express TCP traffic patterns, such as
  request-response workloads. This might result in a
  minimal increase in packet processing overhead.
- **TX queue size and Large LLQ** –
  Verifies that the transmit queue size for the network interface is large
  enough for optimal performance. The script also checks whether the ENA
  module parameter explicitly disables the Large Low Latency Queue (Large
  LLQ) feature, as it can reduce the available TX queue depth. For more
  information about Large LLQ and its impact on TX queue size, see [Large Low Latency Queue (Large LLQ)](https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#large-low-latency-queue-large-llq "https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#large-low-latency-queue-large-llq") on GitHub.
- **RX queue size** –
  Checks that the receive ring buffer for the network interface is large
  enough to handle incoming traffic efficiently and avoid packet drops under
  load.
- **TCP and network socket buffer sizes**
  – Validates that the TCP receive and send buffer maximum sizes, as
  well as the core network socket buffer defaults and maximums, are large
  enough to sustain high throughput. These settings are important
  in environments with increased network latency, where you need larger
  buffers to use the connection.
- **TCP congestion control**
  – Verifies that the TCP congestion control configuration is optimized
  for use with ENA Express in environments with increased network
  latency.

The script also reports additional diagnostic information, including the ENA driver
version, ENA SRD statistics, interrupt moderation settings, queue configuration, and
socket buffer sizes. This information can be useful for troubleshooting ENA Express
performance issues.

To ensure that your instance network driver is configured for optimum performance,
also review the [ENA Linux Driver Best Practices and Performance Optimization Guide](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst "https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst") on
GitHub.
