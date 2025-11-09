# Improve network performance between EC2 instances with ENA

Express

ENA Express is powered by AWS Scalable Reliable Datagram (SRD) technology.
SRD is a high performance network transport protocol that uses dynamic routing
to increase throughput and minimize tail latency. With ENA Express, you can communicate between two EC2 instances in
the same Availability Zone.

###### Benefits of ENA Express

- Increases the maximum bandwidth a single flow can use from 5 Gbps up to 25 Gbps
  within the Availability Zone, up to the aggregate instance limit.
- Reduces tail latency of network traffic between EC2 instances, especially during
  periods of high network load.
- Detects and avoids congested network paths.
- Handles some tasks directly in the network layer, such as packet reordering on the
  receiving end, and most retransmits that are needed. This frees up the application
  layer for other work.

###### Note

- If your application sends or receives a high volume of packets per second, and
  needs to optimize for latency most of the time, especially during periods when
  there is no congestion on the network, [Enhanced networking](enhanced-networking.md "enhanced-networking.md") might be a better fit for your
  network.
- ENA Express traffic can't be sent in a Local Zone.
  After you've enabled ENA Express for the network interface attachment on an instance, the
  sending instance initiates communication with the receiving instance, and SRD detects if ENA
  Express is operating on both the sending instance and the receiving instance. If ENA Express
  is operating, the communication can use SRD transmission. If ENA Express is not operating,
  the communication falls back to standard ENA transmission.

During periods of time when network traffic is light, you might notice a slight increase
in packet latency (tens of microseconds) when the packet uses ENA Express. During those
times, applications that prioritize specific network performance characteristics can benefit
from ENA Express as follows:

- Processes can benefit from increased maximum single flow bandwidth from 5 Gbps up
  to 25 Gbps within the same Availability Zone, up to the aggregate instance limit.
  For example, if a specific instance type supports up to 12.5 Gbps, the single flow
  bandwidth is also limited to 12.5 Gbps.
- Longer running processes should experience reduced tail latency during periods of
  network congestion.
- Processes can benefit from a smoother and more standard distribution for network
  response times.

###### Topics

- [How ENA Express works](#ena-express-how-it-works "#ena-express-how-it-works")
- [Supported instance types for ENA
  Express](#ena-express-supported-instance-types "#ena-express-supported-instance-types")
- [Prerequisites for Linux instances](#ena-express-prereq-linux "#ena-express-prereq-linux")
- [Tune performance for ENA Express settings on Linux
  instances](#ena-express-tune "#ena-express-tune")
- [Review ENA Express settings for your EC2
  instance](ena-express-list-view.md "ena-express-list-view.md")
- [Configure ENA Express settings for your EC2
  instance](ena-express-configure.md "ena-express-configure.md")

## How ENA Express works

ENA Express is powered by AWS Scalable Reliable Datagram (SRD) technology. It distributes packets for each network flow across
different AWS network paths, and dynamically adjusts distribution when it detects
signs of congestion. It also manages packet reordering on the receiving end.

To ensure that ENA Express can manage network traffic as intended, sending and
receiving instances and the communication between them must meet all of the following
requirements:

- Both sending and receiving instance types are supported. See the
  [Supported instance types for ENA
  Express](#ena-express-supported-instance-types "#ena-express-supported-instance-types")
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

- The sending and receiving instances must run in the same Availability Zone.
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
technology provides. For more information about ENA Express metrics, see [Metrics for ENA
Express](monitoring-network-performance-ena.md#network-performance-metrics-ena-express "monitoring-network-performance-ena.md#network-performance-metrics-ena-express").

## Supported instance types for ENA

Express

The following instance types support ENA Express.

General purpose

| Instance type     | Architecture |
| ----------------- | ------------ |
| `m6a.12xlarge`    | x86_64       |
| `m6a.16xlarge`    | x86_64       |
| `m6a.24xlarge`    | x86_64       |
| `m6a.32xlarge`    | x86_64       |
| `m6a.48xlarge`    | x86_64       |
| `m6a.metal`       | x86_64       |
| `m6i.8xlarge`     | x86_64       |
| `m6i.12xlarge`    | x86_64       |
| `m6i.16xlarge`    | x86_64       |
| `m6i.24xlarge`    | x86_64       |
| `m6i.32xlarge`    | x86_64       |
| `m6i.metal`       | x86_64       |
| `m6id.8xlarge`    | x86_64       |
| `m6id.12xlarge`   | x86_64       |
| `m6id.16xlarge`   | x86_64       |
| `m6id.24xlarge`   | x86_64       |
| `m6id.32xlarge`   | x86_64       |
| `m6id.metal`      | x86_64       |
| `m6idn.8xlarge`   | x86_64       |
| `m6idn.12xlarge`  | x86_64       |
| `m6idn.16xlarge`  | x86_64       |
| `m6idn.24xlarge`  | x86_64       |
| `m6idn.32xlarge`  | x86_64       |
| `m6idn.metal`     | x86_64       |
| `m6in.8xlarge`    | x86_64       |
| `m6in.12xlarge`   | x86_64       |
| `m6in.16xlarge`   | x86_64       |
| `m6in.24xlarge`   | x86_64       |
| `m6in.32xlarge`   | x86_64       |
| `m6in.metal`      | x86_64       |
| `m7a.12xlarge`    | x86_64       |
| `m7a.16xlarge`    | x86_64       |
| `m7a.24xlarge`    | x86_64       |
| `m7a.32xlarge`    | x86_64       |
| `m7a.48xlarge`    | x86_64       |
| `m7a.metal-48xl`  | x86_64       |
| `m7g.12xlarge`    | arm64        |
| `m7g.16xlarge`    | arm64        |
| `m7g.metal`       | arm64        |
| `m7gd.12xlarge`   | arm64        |
| `m7gd.16xlarge`   | arm64        |
| `m7gd.metal`      | arm64        |
| `m7i.12xlarge`    | x86_64       |
| `m7i.16xlarge`    | x86_64       |
| `m7i.24xlarge`    | x86_64       |
| `m7i.48xlarge`    | x86_64       |
| `m7i.metal-24xl`  | x86_64       |
| `m7i.metal-48xl`  | x86_64       |
| `m8a.16xlarge`    | x86_64       |
| `m8a.24xlarge`    | x86_64       |
| `m8a.48xlarge`    | x86_64       |
| `m8a.metal-24xl`  | x86_64       |
| `m8a.metal-48xl`  | x86_64       |
| `m8g.12xlarge`    | arm64        |
| `m8g.16xlarge`    | arm64        |
| `m8g.24xlarge`    | arm64        |
| `m8g.48xlarge`    | arm64        |
| `m8g.metal-24xl`  | arm64        |
| `m8g.metal-48xl`  | arm64        |
| `m8gd.12xlarge`   | arm64        |
| `m8gd.16xlarge`   | arm64        |
| `m8gd.24xlarge`   | arm64        |
| `m8gd.48xlarge`   | arm64        |
| `m8gd.metal-24xl` | arm64        |
| `m8gd.metal-48xl` | arm64        |
| `m8i.24xlarge`    | x86_64       |
| `m8i.32xlarge`    | x86_64       |
| `m8i.48xlarge`    | x86_64       |
| `m8i.96xlarge`    | x86_64       |
| `m8i.metal-48xl`  | x86_64       |
| `m8i.metal-96xl`  | x86_64       |

Compute optimized

| Instance type     | Architecture |
| ----------------- | ------------ |
| `c6a.12xlarge`    | x86_64       |
| `c6a.16xlarge`    | x86_64       |
| `c6a.24xlarge`    | x86_64       |
| `c6a.32xlarge`    | x86_64       |
| `c6a.48xlarge`    | x86_64       |
| `c6a.metal`       | x86_64       |
| `c6gn.4xlarge`    | arm64        |
| `c6gn.8xlarge`    | arm64        |
| `c6gn.12xlarge`   | arm64        |
| `c6gn.16xlarge`   | arm64        |
| `c6i.8xlarge`     | x86_64       |
| `c6i.12xlarge`    | x86_64       |
| `c6i.16xlarge`    | x86_64       |
| `c6i.24xlarge`    | x86_64       |
| `c6i.32xlarge`    | x86_64       |
| `c6i.metal`       | x86_64       |
| `c6id.8xlarge`    | x86_64       |
| `c6id.12xlarge`   | x86_64       |
| `c6id.16xlarge`   | x86_64       |
| `c6id.24xlarge`   | x86_64       |
| `c6id.32xlarge`   | x86_64       |
| `c6id.metal`      | x86_64       |
| `c6in.8xlarge`    | x86_64       |
| `c6in.12xlarge`   | x86_64       |
| `c6in.16xlarge`   | x86_64       |
| `c6in.24xlarge`   | x86_64       |
| `c6in.32xlarge`   | x86_64       |
| `c6in.metal`      | x86_64       |
| `c7a.12xlarge`    | x86_64       |
| `c7a.16xlarge`    | x86_64       |
| `c7a.24xlarge`    | x86_64       |
| `c7a.32xlarge`    | x86_64       |
| `c7a.48xlarge`    | x86_64       |
| `c7a.metal-48xl`  | x86_64       |
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
| `c7i.12xlarge`    | x86_64       |
| `c7i.16xlarge`    | x86_64       |
| `c7i.24xlarge`    | x86_64       |
| `c7i.48xlarge`    | x86_64       |
| `c7i.metal-24xl`  | x86_64       |
| `c7i.metal-48xl`  | x86_64       |
| `c8g.12xlarge`    | arm64        |
| `c8g.16xlarge`    | arm64        |
| `c8g.24xlarge`    | arm64        |
| `c8g.48xlarge`    | arm64        |
| `c8g.metal-24xl`  | arm64        |
| `c8g.metal-48xl`  | arm64        |
| `c8gd.12xlarge`   | arm64        |
| `c8gd.16xlarge`   | arm64        |
| `c8gd.24xlarge`   | arm64        |
| `c8gd.48xlarge`   | arm64        |
| `c8gd.metal-24xl` | arm64        |
| `c8gd.metal-48xl` | arm64        |
| `c8gn.8xlarge`    | arm64        |
| `c8gn.12xlarge`   | arm64        |
| `c8gn.16xlarge`   | arm64        |
| `c8gn.24xlarge`   | arm64        |
| `c8gn.48xlarge`   | arm64        |
| `c8gn.metal-24xl` | arm64        |
| `c8gn.metal-48xl` | arm64        |
| `c8i.24xlarge`    | x86_64       |
| `c8i.32xlarge`    | x86_64       |
| `c8i.48xlarge`    | x86_64       |
| `c8i.96xlarge`    | x86_64       |
| `c8i.metal-48xl`  | x86_64       |
| `c8i.metal-96xl`  | x86_64       |

Memory optimized

| Instance type          | Architecture |
| ---------------------- | ------------ |
| `r6a.12xlarge`         | x86_64       |
| `r6a.16xlarge`         | x86_64       |
| `r6a.24xlarge`         | x86_64       |
| `r6a.32xlarge`         | x86_64       |
| `r6a.48xlarge`         | x86_64       |
| `r6a.metal`            | x86_64       |
| `r6i.8xlarge`          | x86_64       |
| `r6i.12xlarge`         | x86_64       |
| `r6i.16xlarge`         | x86_64       |
| `r6i.24xlarge`         | x86_64       |
| `r6i.32xlarge`         | x86_64       |
| `r6i.metal`            | x86_64       |
| `r6id.8xlarge`         | x86_64       |
| `r6id.12xlarge`        | x86_64       |
| `r6id.16xlarge`        | x86_64       |
| `r6id.24xlarge`        | x86_64       |
| `r6id.32xlarge`        | x86_64       |
| `r6id.metal`           | x86_64       |
| `r6idn.8xlarge`        | x86_64       |
| `r6idn.12xlarge`       | x86_64       |
| `r6idn.16xlarge`       | x86_64       |
| `r6idn.24xlarge`       | x86_64       |
| `r6idn.32xlarge`       | x86_64       |
| `r6idn.metal`          | x86_64       |
| `r6in.8xlarge`         | x86_64       |
| `r6in.12xlarge`        | x86_64       |
| `r6in.16xlarge`        | x86_64       |
| `r6in.24xlarge`        | x86_64       |
| `r6in.32xlarge`        | x86_64       |
| `r6in.metal`           | x86_64       |
| `r7a.12xlarge`         | x86_64       |
| `r7a.16xlarge`         | x86_64       |
| `r7a.24xlarge`         | x86_64       |
| `r7a.32xlarge`         | x86_64       |
| `r7a.48xlarge`         | x86_64       |
| `r7a.metal-48xl`       | x86_64       |
| `r7g.12xlarge`         | arm64        |
| `r7g.16xlarge`         | arm64        |
| `r7g.metal`            | arm64        |
| `r7gd.12xlarge`        | arm64        |
| `r7gd.16xlarge`        | arm64        |
| `r7gd.metal`           | arm64        |
| `r7i.12xlarge`         | x86_64       |
| `r7i.16xlarge`         | x86_64       |
| `r7i.24xlarge`         | x86_64       |
| `r7i.48xlarge`         | x86_64       |
| `r7i.metal-24xl`       | x86_64       |
| `r7i.metal-48xl`       | x86_64       |
| `r7iz.8xlarge`         | x86_64       |
| `r7iz.12xlarge`        | x86_64       |
| `r7iz.16xlarge`        | x86_64       |
| `r7iz.32xlarge`        | x86_64       |
| `r7iz.metal-16xl`      | x86_64       |
| `r7iz.metal-32xl`      | x86_64       |
| `r8a.16xlarge`         | x86_64       |
| `r8a.24xlarge`         | x86_64       |
| `r8a.48xlarge`         | x86_64       |
| `r8a.metal-24xl`       | x86_64       |
| `r8a.metal-48xl`       | x86_64       |
| `r8g.12xlarge`         | arm64        |
| `r8g.16xlarge`         | arm64        |
| `r8g.24xlarge`         | arm64        |
| `r8g.48xlarge`         | arm64        |
| `r8g.metal-24xl`       | arm64        |
| `r8g.metal-48xl`       | arm64        |
| `r8gb.8xlarge`         | arm64        |
| `r8gb.12xlarge`        | arm64        |
| `r8gb.16xlarge`        | arm64        |
| `r8gb.24xlarge`        | arm64        |
| `r8gb.metal-24xl`      | arm64        |
| `r8gd.12xlarge`        | arm64        |
| `r8gd.16xlarge`        | arm64        |
| `r8gd.24xlarge`        | arm64        |
| `r8gd.48xlarge`        | arm64        |
| `r8gd.metal-24xl`      | arm64        |
| `r8gd.metal-48xl`      | arm64        |
| `r8gn.8xlarge`         | arm64        |
| `r8gn.12xlarge`        | arm64        |
| `r8gn.16xlarge`        | arm64        |
| `r8gn.24xlarge`        | arm64        |
| `r8gn.48xlarge`        | arm64        |
| `r8gn.metal-24xl`      | arm64        |
| `r8gn.metal-48xl`      | arm64        |
| `r8i.24xlarge`         | x86_64       |
| `r8i.32xlarge`         | x86_64       |
| `r8i.48xlarge`         | x86_64       |
| `r8i.96xlarge`         | x86_64       |
| `r8i.metal-48xl`       | x86_64       |
| `r8i.metal-96xl`       | x86_64       |
| `u7i-6tb.112xlarge`    | x86_64       |
| `u7i-8tb.112xlarge`    | x86_64       |
| `u7i-12tb.224xlarge`   | x86_64       |
| `u7in-16tb.224xlarge`  | x86_64       |
| `u7in-24tb.224xlarge`  | x86_64       |
| `u7in-32tb.224xlarge`  | x86_64       |
| `u7inh-32tb.480xlarge` | x86_64       |
| `x2idn.16xlarge`       | x86_64       |
| `x2idn.24xlarge`       | x86_64       |
| `x2idn.32xlarge`       | x86_64       |
| `x2idn.metal`          | x86_64       |
| `x2iedn.8xlarge`       | x86_64       |
| `x2iedn.16xlarge`      | x86_64       |
| `x2iedn.24xlarge`      | x86_64       |
| `x2iedn.32xlarge`      | x86_64       |
| `x2iedn.metal`         | x86_64       |
| `x8g.12xlarge`         | arm64        |
| `x8g.16xlarge`         | arm64        |
| `x8g.24xlarge`         | arm64        |
| `x8g.48xlarge`         | arm64        |
| `x8g.metal-24xl`       | arm64        |
| `x8g.metal-48xl`       | arm64        |

Accelerated computing

| Instance type      | Architecture |
| ------------------ | ------------ |
| `g6.48xlarge`      | x86_64       |
| `g6e.12xlarge`     | x86_64       |
| `g6e.24xlarge`     | x86_64       |
| `g6e.48xlarge`     | x86_64       |
| `p5.48xlarge`      | x86_64       |
| `p5e.48xlarge`     | x86_64       |
| `p5en.48xlarge`    | x86_64       |
| `p6-b200.48xlarge` | x86_64       |

Storage optimized

| Instance type     | Architecture |
| ----------------- | ------------ |
| `i4g.4xlarge`     | arm64        |
| `i4g.8xlarge`     | arm64        |
| `i4g.16xlarge`    | arm64        |
| `i4i.8xlarge`     | x86_64       |
| `i4i.12xlarge`    | x86_64       |
| `i4i.16xlarge`    | x86_64       |
| `i4i.24xlarge`    | x86_64       |
| `i4i.32xlarge`    | x86_64       |
| `i4i.metal`       | x86_64       |
| `i7i.12xlarge`    | x86_64       |
| `i7i.16xlarge`    | x86_64       |
| `i7i.24xlarge`    | x86_64       |
| `i7i.48xlarge`    | x86_64       |
| `i7i.metal-24xl`  | x86_64       |
| `i7i.metal-48xl`  | x86_64       |
| `i7ie.12xlarge`   | x86_64       |
| `i7ie.18xlarge`   | x86_64       |
| `i7ie.24xlarge`   | x86_64       |
| `i7ie.48xlarge`   | x86_64       |
| `i7ie.metal-24xl` | x86_64       |
| `i7ie.metal-48xl` | x86_64       |
| `i8g.12xlarge`    | arm64        |
| `i8g.16xlarge`    | arm64        |
| `i8g.24xlarge`    | arm64        |
| `i8g.48xlarge`    | arm64        |
| `i8g.metal-24xl`  | arm64        |
| `i8ge.12xlarge`   | arm64        |
| `i8ge.18xlarge`   | arm64        |
| `i8ge.24xlarge`   | arm64        |
| `i8ge.48xlarge`   | arm64        |
| `i8ge.metal-24xl` | arm64        |
| `i8ge.metal-48xl` | arm64        |
| `im4gn.4xlarge`   | arm64        |
| `im4gn.8xlarge`   | arm64        |
| `im4gn.16xlarge`  | arm64        |

## Prerequisites for Linux instances

To ensure that ENA Express can operate effectively, update the settings for your Linux
instance as follows.

- If your instance uses jumbo frames, run the following command to set your
  maximum transmission unit (MTU) to `8900`.

```
`[ec2-user ~]$` sudo ip link set dev `eth0` mtu `8900`
```

- Increase the receiver (Rx) ring size, as follows:

```
`[ec2-user ~]$` ethtool -G `device` rx 8192
```

- To maximize ENA Express bandwidth, configure your TCP queue limits as
  follows:
  1.  Set the TCP small queue limit to 1MB or higher. This increases the
      amount of data that's queued for transmission on a socket.

  ```
  sudo sh -c 'echo `1048576` > /proc/sys/net/ipv4/tcp_limit_output_bytes'
  ```

  2.  Disable byte queue limits on the eth device if they're enabled for
      your Linux distribution. This increases data queued for transmission for
      the device queue.

  ```
  sudo sh -c 'for txq in /sys/class/net/`eth0`/queues/tx-*; do echo max > ${txq}/byte_queue_limits/limit_min; done'
  ```

  ###### Note

  The ENA driver for the Amazon Linux distribution disables byte queue
  limits by default.

## Tune performance for ENA Express settings on Linux

instances

To check your Linux instance configuration for optimal ENA Express performance, you
can run the following script that's available on the Amazon GitHub repository:

[https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express-settings.sh](https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express-settings.sh "https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express-settings.sh")

The script runs a series of tests and suggests both recommended and required
configuration changes.
