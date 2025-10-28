# Amazon EC2 instance network bandwidth

Instance bandwidth specifications apply to both inbound and outbound traffic for the
instance. For example, if an instance specifies up to 10 Gbps of bandwidth, that means it
has up to 10 Gbps of bandwidth for inbound traffic and, simultaneously, up to 10 Gbps for
outbound traffic. The network bandwidth that's available to an EC2 instance depends on
several factors, as follows.

###### Multi-flow traffic

Bandwidth for multi-flow traffic is limited to 50% of the available bandwidth
for traffic that goes through an internet gateway or a [local gateway](../../../outposts/latest/userguide/outposts-local-gateways.md "../../../outposts/latest/userguide/outposts-local-gateways.md")
for instances with 32 or more vCPUs, or 5 Gbps, whichever is larger. For instances with
fewer than 32 vCPUs, bandwidth is limited to 5 Gbps.

###### Single-flow traffic

Bandwidth for single-flow traffic is limited to 5 Gbps when instances are
not in the same [cluster placement group](placement-strategies.md#placement-groups-cluster "placement-strategies.md#placement-groups-cluster"). To
reduce latency and increase single-flow bandwidth, try one of the following:

- Use a cluster placement group to achieve up to 10 Gbps bandwidth for instances within
  the same placement group.
- Set up multiple paths between two endpoints to achieve higher bandwidth with Multipath TCP
  (MPTCP).
- Configure ENA Express for eligible instances within the same Availability Zone to achieve
  up to 25 Gbps between those instances.

###### Note

A single-flow is considered a unique 5-tuple TCP or UDP flow. For other protocols following
the IP header, such as `GRE` or `IPsec`, the 3 tuple of source IP,
destination IP, and next protocol is used to define a flow.

## Available instance bandwidth

The available network bandwidth of an instance depends on the number of vCPUs that it
has. For example, an `m5.8xlarge` instance has 32 vCPUs and 10 Gbps network
bandwidth, and an `m5.16xlarge` instance has 64 vCPUs and 20 Gbps network
bandwidth. However, instances might not achieve this bandwidth; for example, if they
exceed network allowances at the instance level, such as packet per second or number of
tracked connections. How much of the available bandwidth the traffic can utilize depends
on the number of vCPUs and the destination. For example, an `m5.16xlarge`
instance has 64 vCPUs, so traffic to another instance in the Region can utilize the full
bandwidth available (20 Gbps). However, traffic that goes through an internet gateway
or a [local gateway](../../../outposts/latest/userguide/outposts-local-gateways.md "../../../outposts/latest/userguide/outposts-local-gateways.md") can utilize only 50% of the bandwidth available (10 Gbps).

Typically, instances with 16 vCPUs or fewer (size `4xlarge` and smaller) are
documented as having "up to" a specified bandwidth; for example, "up to 10 Gbps". These
instances have a baseline bandwidth. To meet additional demand, they can use a network
I/O credit mechanism to burst beyond their baseline bandwidth. Instances can use burst
bandwidth for a limited time, typically from 5 to 60 minutes, depending on the instance
size.

An instance receives the maximum number of network I/O credits at launch. If the instance
exhausts its network I/O credits, it returns to its baseline bandwidth. A running instance
earns network I/O credits whenever it uses less network bandwidth than its baseline bandwidth.
A stopped instance does not earn network I/O credits. Instance burst is on a best effort basis,
even when the instance has credits available, as burst bandwidth is a shared resource.

There are separate network I/O credit buckets for inbound and outbound traffic.

###### Base and burst network performance

The _Amazon EC2 Instance Types Guide_ describes the network performance for each
instance type, plus the baseline network bandwidth available for instances that can use burst
bandwidth. For more information, see the following:

- [Network specifications – General purpose](../../../ec2/latest/instancetypes/gp.md#gp_network "../../../ec2/latest/instancetypes/gp.md#gp_network")
- [Network specifications – Compute optimized](../../../ec2/latest/instancetypes/co.md#co_network "../../../ec2/latest/instancetypes/co.md#co_network")
- [Network specifications – Memory optimized](../../../ec2/latest/instancetypes/mo.md#mo_network "../../../ec2/latest/instancetypes/mo.md#mo_network")
- [Network specifications – Storage optimized](../../../ec2/latest/instancetypes/so.md#so_network "../../../ec2/latest/instancetypes/so.md#so_network")
- [Network specifications – Accelerated computing](../../../ec2/latest/instancetypes/ac.md#ac_network "../../../ec2/latest/instancetypes/ac.md#ac_network")
- [Network specifications – High-performance computing](../../../ec2/latest/instancetypes/hpc.md#hpc_network "../../../ec2/latest/instancetypes/hpc.md#hpc_network")
- [Network specifications – Previous generation](../../../ec2/latest/instancetypes/gp.md#pg_network "../../../ec2/latest/instancetypes/gp.md#pg_network")

Alternatively, you can use a command line tool to get this information. The Amazon EC2 console
does not display the baseline network bandwidth of an instance type.

AWS CLI
You can use the [describe-instance-types](../../../cli/latest/reference/ec2/describe-instance-types.md "../../../cli/latest/reference/ec2/describe-instance-types.md") command to display information about an
instance type. The following example displays network performance information for
all C5 instances.

```
aws ec2 describe-instance-types \
    --filters "Name=instance-type,Values=c5.*" \
    --query "InstanceTypes[].[InstanceType, NetworkInfo.NetworkPerformance, NetworkInfo.NetworkCards[0].BaselineBandwidthInGbps] | sort_by(@,&[2])" \
    --output table
```

The following is example output. If your output is missing the baseline bandwidth,
update to the latest version of the AWS CLI.

````
---------------------------------------------
|           DescribeInstanceTypes           | +--------------+--------------------+-------+
|  c5.large    |  Up to 10 Gigabit  |  0.75 |
|  c5.xlarge   |  Up to 10 Gigabit  |  1.25 |
|  c5.2xlarge  |  Up to 10 Gigabit  |  2.5  |
|  c5.4xlarge  |  Up to 10 Gigabit  |  5.0  |
|  c5.9xlarge  |  12 Gigabit        |  12.0 |
|  c5.12xlarge |  12 Gigabit        |  12.0 |
|  c5.18xlarge |  25 Gigabit        |  25.0 |
|  c5.24xlarge |  25 Gigabit        |  25.0 |
|  c5.metal    |  25 Gigabit        |  25.0 | +--------------+--------------------+-------+ ``` PowerShell You can use the [Get-EC2InstanceType](../../../powershell/latest/reference/items/Get-EC2InstanceType.md "../../../powershell/latest/reference/items/Get-EC2InstanceType.md") PowerShell command to display information about an instance type. The following example displays network performance information for all C5 instances. ``` Get-EC2InstanceType -Filter @{Name = "instance-type"; Values = "c5.*" } | ` Select-Object ` InstanceType, @{Name = 'NetworkPerformance'; Expression = {($_.Networkinfo.NetworkCards.NetworkPerformance)}}, @{Name = 'BaselineBandwidthInGbps'; Expression = {($_.Networkinfo.NetworkCards.BaselineBandwidthInGbps)}} | ` Format-Table -AutoSize ``` The following is example output. ``` InstanceType NetworkPerformance BaselineBandwidthInGbps ------------ ------------------ ----------------------- c5.4xlarge   Up to 10 Gigabit                      5.00 c5.xlarge    Up to 10 Gigabit                      1.25 c5.12xlarge  12 Gigabit                           12.00 c5.9xlarge   12 Gigabit                           12.00 c5.24xlarge  25 Gigabit                           25.00 c5.metal     25 Gigabit                           25.00 c5.2xlarge   Up to 10 Gigabit                      2.50 c5.large     Up to 10 Gigabit                      0.75 c5.18xlarge  25 Gigabit                           25.00 ``` ## Monitor instance bandwidth You can use CloudWatch metrics to monitor instance network bandwidth and the packets sent and received. You can use the network performance metrics provided by the Elastic Network Adapter (ENA) driver to monitor when traffic exceeds the network allowances that Amazon EC2 defines at the instance level. You can configure whether Amazon EC2 sends metric data for the instance to CloudWatch using one-minute periods or five-minute periods. It is possible that the network performance metrics would show that an allowance was exceeded and packets were dropped while the CloudWatch instance metrics do not. This can happen when the instance has a short spike in demand for network resources (known as a microburst), but the CloudWatch metrics are not granular enough to reflect these microsecond spikes. ###### Learn more <br>• [Instance metrics](viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics "viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics") <br>• [Monitor network performance](monitoring-network-performance-ena.md "monitoring-network-performance-ena.md")
````
