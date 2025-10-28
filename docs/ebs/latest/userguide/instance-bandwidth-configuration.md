# Configurable instance bandwidth weighting

Instance bandwidth configuration (IBC) is a feature that enables you to adjust the allocation of
network bandwidth between Amazon EBS and VPC networking for an Amazon EC2 instance. This feature can help
you optimize performance for workloads with specific bandwidth requirements. Instance bandwidth
configuration is supported on some instances only. For more information, see [Instance
bandwidth weighting configuration](../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md#config-bw-support "../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md#config-bw-support").

For EBS performance, using the `ebs-1` bandwidth weighting increases the baseline
EBS bandwidth by 25 percent while reducing the VPC networking bandwidth by the same absolute amount.
This can be beneficial for I/O-intensive workloads that require higher EBS throughput.

When planning your workload, carefully consider your I/O size and patterns. Smaller I/O sizes
are generally less affected by bandwidth limitations, while larger I/O sizes or sequential workloads
can experience more significant impacts from bandwidth changes. It's crucial to thoroughly test your
specific workload to ensure optimal performance with your chosen bandwidth weighting.

###### Considerations

- Configurable instance bandwidth is supported on select instance types. For more information,
  see [Supported instance types](../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md#config-bw-support "../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md#config-bw-support").
- Using the `ebs-1` bandwidth weighting increases EBS bandwidth up to 25 percent,
  which can improve the performance of I/O-intensive applications. However, keep in mind that VPC
  networking bandwidth will be reduced by the same absolute amount (the combined bandwidth
  specification between EBS and networking does not change).
- Changes in bandwidth weighting can significantly affect I/O performance. With the `vpc-1`
  bandwidth weighting, network bandwidth is increased, but you might experience lower than expected
  IOPS for EBS volumes. This is because you might reach the EBS bandwidth limit before the IOPS
  limit, especially with larger I/O sizes. For example, an instance type that typically supports
  240,000 IOPS with 16 KiB I/O size might achieve fewer IOPS when using `vpc-1` bandwidth
  weight due to the decreased EBS bandwidth.
- Always test your specific workload to ensure that your chosen bandwidth weighting meets your
  performance needs.
- You can configure the bandwidth weighting during instance launch or modify it for stopped
  instances. For more information see [Configure
  bandwidth weighting for your instance](../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md#config-bw-how-to "../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md#config-bw-how-to").
- You can configure instance bandwidth weighting at no additional costs.
