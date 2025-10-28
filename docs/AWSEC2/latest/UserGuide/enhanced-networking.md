# Enhanced networking on Amazon EC2 instances

Enhanced networking uses single root I/O virtualization (SR-IOV) to provide
high-performance networking capabilities on supported instance types. SR-IOV is a method of
device virtualization that provides higher I/O performance and lower CPU utilization when
compared to traditional virtualized network interfaces. Enhanced networking provides higher
bandwidth, higher packet per second (PPS) performance, and consistently lower latency
between instances. There is no additional charge for using enhanced networking.

For information about the supported network speed for each instance type, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

You can enable enhanced networking using one of the following mechanisms:

Elastic Network Adapter (ENA)

The Elastic Network Adapter (ENA) supports network speeds of up to 100 Gbps
for supported instance types.

All [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type") use ENA for enhanced networking. In addition, the
following Xen-based instances use ENA: H1, I3, G3, `m4.16xlarge`, P2,
P3, P3dn, and R4.

For more information, see [Enable enhanced networking with ENA on your EC2 instances](enhanced-networking-ena.md "enhanced-networking-ena.md").

Intel 82599 Virtual Function (VF) interface

The Intel 82599 Virtual Function interface supports network speeds of up to 10
Gbps for supported instance types.

The following instance types use the Intel 82599 VF interface for enhanced
networking: C3, C4, D2, I2, M4 (excluding m4.16xlarge), and R3.

For more information, see [Enhanced networking with the Intel 82599 VF interface](sriov-networking.md "sriov-networking.md").

###### Contents

- [Elastic Network Adapter (ENA)](enhanced-networking-ena.md "enhanced-networking-ena.md")
- [ENA Express](ena-express.md "ena-express.md")
- [Intel 82599 VF](sriov-networking.md "sriov-networking.md")
- [Monitor network
  performance](monitoring-network-performance-ena.md "monitoring-network-performance-ena.md")
- [Improve network latency on Linux](ena-improve-network-latency-linux.md "ena-improve-network-latency-linux.md")
- [Nitro performance
  considerations](ena-nitro-perf.md "ena-nitro-perf.md")
- [Optimize network performance on Windows](enhanced-networking-os.md "enhanced-networking-os.md")
