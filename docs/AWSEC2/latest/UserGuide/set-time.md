# Precision clock and time synchronization on your EC2 instance

A consistent and accurate time reference on your Amazon EC2 instance is crucial for many server
tasks and processes. Time stamps in system logs play an essential role in identifying when
issues occurred and the chronological order of events. When you use the AWS CLI or an AWS
SDK to make requests from your instance, these tools sign requests on your behalf. If your
instance's date and time settings are inaccurate, it can result in a discrepancy between the
date in the signature and the date of the request, leading to AWS rejecting your
requests.

To address this important aspect, Amazon offers the Amazon Time Sync Service, which is accessible from all
EC2 instances and used by various AWS services. The service uses a fleet of
satellite-connected and atomic reference clocks in each AWS Region to deliver accurate and
current time readings of the Coordinated Universal Time (UTC) global standard.

For the best performance, we recommend using the [local
Amazon Time Sync Service](configure-ec2-ntp.md "configure-ec2-ntp.md") on your EC2 instances. For a backup to the local Amazon Time Sync Service on your instances,
or to connect resources outside of Amazon EC2 to the Amazon Time Sync Service, you can use the [public Amazon Time Sync Service](configure-time-sync.md "configure-time-sync.md") located at `time.aws.com`. The public Amazon Time Sync Service, like
the local Amazon Time Sync Service, automatically smears any leap seconds that are added to UTC. The public
Amazon Time Sync Service is supported globally by our fleet of satellite-connected and atomic reference clocks
in each AWS Region.

## Hardware packet timestamping

You can enable hardware packet timestamping on your instance to add a 64-bit
nanosecond-precision timestamp to every incoming network packet. Because hardware packet
timestamping occurs at the hardware level—before the packet reaches the kernel,
socket, or application layer—you bypass any delays added by software
timestamping. The underlying reference clock for hardware timestamping is the Amazon Time Sync Service
[PTP hardware clock](configure-ec2-ntp.md#connect-to-the-ptp-hardware-clock "configure-ec2-ntp.md#connect-to-the-ptp-hardware-clock").

###### Benefits

Hardware packet timestamping provides the following benefits:

- Improves event ordering, which can also be used to determine the actual
  order in which packets arrive at your EC2 instance, ensuring fair packet
  processing.
- Measures one-way network latency.
- Increases distributed transaction speed with higher precision and accuracy
  compared to most on-premises solutions.

###### Prerequisites and configuration

To enable hardware packet timestamping, your instance must meet the following
prerequisites:

- Must be a Linux instance.
- Meet the [requirements to
  support the PTP hardware clock](configure-ec2-ntp.md#ptp-hardware-clock-requirements "configure-ec2-ntp.md#ptp-hardware-clock-requirements").

For the configuration instructions, see [Hardware Packet Timestamping](https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#hardware-packet-timestamping "https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#hardware-packet-timestamping") on the **Linux kernel driver for
Elastic Network Adapter (ENA) family** page on _GitHub_.

## Leap seconds

Leap seconds, introduced in 1972, are occasional one-second adjustments to UTC time to
factor in irregularities in the earth’s rotation in order to accommodate differences
between International Atomic Time (TAI) and solar time (Ut1). To manage leap seconds on
behalf of customers, we designed leap second smearing within the Amazon Time Sync Service. For more
information, see [Look Before You
Leap – The Coming Leap Second and AWS](https://aws.amazon.com/blogs/aws/look-before-you-leap-the-coming-leap-second-and-aws/ "https://aws.amazon.com/blogs/aws/look-before-you-leap-the-coming-leap-second-and-aws/").

Leap seconds are going away, and we are in full support of the decision made at the
[27th General Conference
on Weights and Measures to abandon leap seconds by or before 2035](https://www.bipm.org/en/cgpm-2022/resolution-4 "https://www.bipm.org/en/cgpm-2022/resolution-4").

To support this transition, we still plan on smearing time during a leap second event
when accessing the Amazon Time Sync Service over the local NTP connection or our public NTP pools (`time.aws.com`). The
PTP hardware clock, however, does not provide a smeared time option. In the event of a
leap second, the PTP hardware clock will add the leap second following UTC standards.
Leap-smeared and leap second time sources are the same in most cases. But because they
differ during a leap second event, we do not recommend using both smeared and
non-smeared time sources in your time client configuration during a leap second
event.

 

###### Topics

- [Set the time reference on your EC2 instance to use
  the local Amazon Time Sync Service](configure-ec2-ntp.md "configure-ec2-ntp.md")
- [Set the time reference on your EC2 instance or any
  internet-connected device to use the public Amazon Time Sync Service](configure-time-sync.md "configure-time-sync.md")
- [Compare timestamps for your Linux
  instances](compare-timestamps-with-clockbound.md "compare-timestamps-with-clockbound.md")
- [Change the time zone of your
  instance](change-time-zone-of-instance.md "change-time-zone-of-instance.md")

 

###### Related resources

- AWS Compute Blog: [It’s About Time: Microsecond-Accurate Clocks on Amazon EC2 Instances](https://aws.amazon.com/blogs/compute/its-about-time-microsecond-accurate-clocks-on-amazon-ec2-instances/ "https://aws.amazon.com/blogs/compute/its-about-time-microsecond-accurate-clocks-on-amazon-ec2-instances/")
- AWS Cloud Operations & Migrations Blog: [Manage Amazon EC2 instance clock accuracy using Amazon Time Sync Service and Amazon CloudWatch – Part
  1](https://aws.amazon.com/blogs/mt/manage-amazon-ec2-instance-clock-accuracy-using-amazon-time-sync-service-and-amazon-cloudwatch-part-1/ "https://aws.amazon.com/blogs/mt/manage-amazon-ec2-instance-clock-accuracy-using-amazon-time-sync-service-and-amazon-cloudwatch-part-1/")
- (Linux) [https://chrony-project.org/](https://chrony-project.org/ "https://chrony-project.org/")
