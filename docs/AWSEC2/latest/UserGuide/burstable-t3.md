# Burstable T3 instances on Amazon EC2 Dedicated Hosts

Dedicated Hosts support burstable performance T3 instances. T3 instances provide a
cost-efficient way of using your eligible BYOL license software on dedicated hardware.
The smaller vCPU footprint of T3 instances enables you to consolidate your workloads on
fewer hosts and maximize your per-core license utilization.

T3 Dedicated Hosts are best suited for running BYOL software with low to moderate CPU
utilization. This includes eligible per-socket, per-core, or per-VM software licenses,
such as Windows Server, Windows Desktop, SQL Server, SUSE Enterprise Linux Server, Red
Hat Enterprise Linux, and Oracle Database. Examples of workloads suited for T3 Dedicated Hosts are
small and medium databases, virtual desktops, development and test environments, code
repositories, and product prototypes. T3 Dedicated Hosts are not recommended for workloads with
sustained high CPU utilization or for workloads that experience correlated CPU bursts
simultaneously.

T3 instances on Dedicated Hosts use the same credit model as T3 instances on shared tenancy
hardware. However, they support the `standard` credit mode only; they do not
support the `unlimited` credit mode. In `standard` mode, T3
instances on Dedicated Hosts _earn_, _spend_, and
_accrue_ credits in the same way as burstable instances on shared
tenancy hardware. They provide a baseline CPU performance with the ability to burst
above the baseline level. To burst above the baseline, the instance spends credits that
it has accrued in its CPU credit balance. When the accrued credits are depleted, CPU
utilization is lowered to the baseline level. For more information about
`standard` mode, see [How standard
burstable performance instances work](burstable-performance-instances-standard-mode-concepts.md#how-burstable-performance-instances-standard-works "burstable-performance-instances-standard-mode-concepts.md#how-burstable-performance-instances-standard-works").

T3 Dedicated Hosts support all of the features offered by Amazon EC2 Dedicated Hosts, including multiple
instance sizes on a single host, Host resource groups, and BYOL.

###### Supported T3 instance sizes and configurations

T3 Dedicated Hosts run general purpose burstable T3 instances that share CPU resources of the
host by providing a baseline CPU performance and the ability to burst to a higher level
when needed. This enables T3 Dedicated Hosts, which have 48 cores, to support up to a maximum of
192 instances per host. In order to efficiently utilize the host’s resources and to
provide the best instance performance, the Amazon EC2 instance placement algorithm
automatically calculates the supported number of instances and instance size
combinations that can be launched on the host.

T3 Dedicated Hosts support multiple instance types on the same host. All T3 instance sizes are
supported on Dedicated Hosts. You can run different combinations of T3 instances up to
the CPU limit of the host.

The following table lists the supported instance types, summarizes the performance of
each instance type, and indicates the maximum number of instances of each size that can
be launched.

| Instance type | vCPUs | Memory (GiB) | Baseline CPU utilization per vCPU | Network burst bandwidth (Gbps) | Amazon EBS burst bandwidth (Mbps) | Max number of instances per Dedicated Host |
| ------------- | ----- | ------------ | --------------------------------- | ------------------------------ | --------------------------------- | ------------------------------------------ |
| t3.nano       | 2     | 0.5          | 5%                                | 5                              | Up to 2,085                       | 192                                        |
| t3.micro      | 2     | 1            | 10%                               | 5                              | Up to 2,085                       | 192                                        |
| t3.small      | 2     | 2            | 20%                               | 5                              | Up to 2,085                       | 192                                        |
| t3.medium     | 2     | 4            | 20%                               | 5                              | Up to 2,085                       | 192                                        |
| t3.large      | 2     | 8            | 30%                               | 5                              | 2,780                             | 96                                         |
| t3.xlarge     | 4     | 16           | 40%                               | 5                              | 2,780                             | 48                                         |
| t3.2xlarge    | 8     | 32           | 40%                               | 5                              | 2,780                             | 24                                         |

###### Monitor CPU utilization for T3 Dedicated Hosts

You can use the `DedicatedHostCPUUtilization` Amazon CloudWatch metric to
monitor the vCPU utilization of a Dedicated Host. The metric is available in the
`EC2` namespace and `Per-Host-Metrics` dimension. For more
information, see [Dedicated Host metrics](viewing_metrics_with_cloudwatch.md#dh-metrics "viewing_metrics_with_cloudwatch.md#dh-metrics").
