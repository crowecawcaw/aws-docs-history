# Improve network latency for Linux based EC2 instances

Network latency is the amount of time it takes for a packet of data to travel from its
source to its destination. Applications that send data across the network depend on timely
responses to provide a positive user experience. High network latency can lead to various
issues, such as the following:

- Slow load times for web pages
- Video stream lag
- Difficulty accessing online resources
  This section outlines steps that you can take to improve the network latency on Amazon EC2
  instances that run on Linux. To achieve optimal latency, follow these steps to configure
  your instance, kernel, and ENA driver settings. For additional configuration guidance, see
  the [ENA Linux Driver Best Practices and Performance Optimization Guide](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst "https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst") on
  GitHub.

###### Note

Steps and settings may vary slightly, depending on your specific network hardware,
the AMI that you launched your instance from, and your application use case.
Before you make any changes, thoroughly test and monitor your network performance to
ensure that you're getting the desired results.

## Reduce the number of network hops for data packets

Each hop that a data packet takes as it moves from router to router increases network
latency. Typically, traffic must take multiple hops to reach your destination. There are
two ways to reduce network hops for your Amazon EC2 instances, as follows:

- **Cluster placement group** – When you specify
  a [cluster placement group](placement-strategies.md#placement-groups-cluster "placement-strategies.md#placement-groups-cluster"), Amazon EC2
  launches instances that are in close proximity to each other, physically
  within the same Availability Zone (AZ) with tighter packing. The physical proximity
  of the instances in the group allows them to take advantage of high-speed connectivity,
  resulting in low latency and high single flow throughput.
- **Dedicated Host** – A [Dedicated Host](dedicated-hosts-overview.md "dedicated-hosts-overview.md") is a physical server that's dedicated for your use. With a
  Dedicated Host, you can launch your instances to run on the same physical server.
  Communication between instances that run on the same Dedicated Host can happen without
  extra network hops.

## How Linux kernel configuration affects latency

Linux kernel configuration can increase or decrease network latency. To achieve
your latency optimization goals, it's important to fine-tune the Linux kernel
configuration according to the specific requirements of your workload.

There are many configuration options for the Linux kernel that might help decrease
network latency. The most impactful options are as follows.

- **Enable busy poll mode** – Busy poll mode
  reduces latency on the network receive path. When you enable busy poll mode, the
  socket layer code can directly poll the receive queue of a network device. The
  downside of busy polling is higher CPU usage in the host that comes from polling
  for new data in a tight loop. There are two global settings that control the number
  of microseconds to wait for packets for all interfaces.

 

`busy_read`

A low latency busy poll timeout for socket reads. This controls the number
of microseconds to wait for the socket layer to read packets on the device
queue. To enable the feature globally with the **sysctl** command,
the Linux Kernel organization recommends a value of 50 microseconds. For more
information, see [busy_read](https://www.kernel.org/doc/html/v5.19/admin-guide/sysctl/net.html?highlight=busy_read "https://www.kernel.org/doc/html/v5.19/admin-guide/sysctl/net.html?highlight=busy_read")
in the _Linux kernel user's and administrator's guide_.

```
`[ec2-user ~]$` sudo sysctl -w net.core.busy_read=`50`
```

`busy_poll`

A low latency busy poll timeout for poll and select. This controls the number
of microseconds to wait for events. The recommended value is between 50-100
microseconds, depending on the number of sockets you're polling. The more sockets
you add, the higher the number should be.

```
`[ec2-user ~]$` sudo sysctl -w net.core.busy_poll=`50`
```

- **Configure CPU power states (C-states)** – C-states
  control the sleep levels that a core may enter when it's inactive. You might want to control
  C-states to tune your system for latency versus performance. In deeper C-states, the CPU is
  essentially "asleep" and can't respond to requests until it wakes up and transitions back to
  an active state. Putting cores to sleep takes time, and although a sleeping core allows more
  headroom for another core to boost to a higher frequency, it takes time for that
  sleeping core to wake back up and perform work.

For example, if a core that's assigned to handle network packet interrupts is asleep, there
might be a delay in servicing that interrupt. You can configure the system so that it doesn't
use deeper C-states. However, while this configuration reduces the processor reaction latency,
it also reduces the headroom available to other cores for Turbo Boost.

To reduce the processor reaction latency, you can limit deeper C-states.
For more information, see [High performance and low latency by limiting deeper C-states](../../../linux/al2/ug/processor_state_control.md#c-states "../../../linux/al2/ug/processor_state_control.md#c-states") in the _Amazon Linux 2 User Guide_.

## Interrupt moderation

The ENA network driver enables communication between an instance and a network. The driver
processes network packets and passes them on to the network stack or to the Nitro card. When a
network packet comes in, the Nitro card generates an interrupt for the CPU to notify the software
of an event.

Interrupt

An interrupt is a signal that a device or application sends to the processor. The
interrupt tells the processor that an event has occurred or a condition has been met
that requires immediate attention. Interrupts can handle time-sensitive tasks such as
receiving data from a network interface, handling hardware events, or servicing requests
from other devices.

Interrupt moderation

Interrupt moderation is a technique that reduces the number of interrupts a device
generates by aggregating or delaying them. The purpose of interrupt moderation is to
improve system performance by reducing the overhead associated with handling a large
number of interrupts. Too many interrupts increase CPU usage, impacting the throughput
adversely, while too few interrupts increase the latency.

Dynamic interrupt moderation

Dynamic interrupt moderation is an enhanced form of interrupt moderation that
dynamically adjusts the interrupt rate based on the current system load and traffic
patterns. It aims to strike a balance between reducing interrupt overhead and packets
per second, or bandwidth.

###### Note

Dynamic interrupt moderation is enabled by default in some AMIs (but can be
enabled or disabled in all AMIs).

To minimize network latency, it might be necessary to disable interrupt moderation. However,
this can also increase the overhead of interrupt processing. It's important to find the
right balance between reducing latency and minimizing overhead. `ethtool`
commands can help you configure interrupt moderation. By default, `rx-usecs`
is set to `20`, and `tx-usecs` is set to `64`.

To get the current interrupt modification configuration, use the following command.

```
`[ec2-user ~]$` ethtool -c `interface` | egrep "rx-usecs:|tx-usecs:|Adaptive RX"`Adaptive RX: on TX: off
rx-usecs: 20
tx-usecs: 64`
```

To disable interrupt modification and dynamic interrupt moderation, use the following command.

```
`[ec2-user ~]$` sudo ethtool -C `interface` adaptive-rx off rx-usecs 0 tx-usecs 0
```
