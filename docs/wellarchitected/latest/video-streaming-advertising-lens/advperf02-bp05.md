# ADVPERF02-BP05 Evaluate ARM architecture for performance considerations by using AWS Graviton

To address the low latency and high throughput needs of advertising workloads, consider
adopting ARM architecture using AWS Graviton for improved performance and cost optimization.

## Implementation guidance

Migrating to AWS Graviton processors can improve performance as
a result of the following:

- **Faster processing:**
  Graviton uses 64-bit ARM Neoverse cores that are optimized
  for speed and efficiency in cloud workloads. Benchmarks show
  Graviton outperforming x86 instances for some workloads.
- **Lower latency:** The ARM
  architecture and custom memory subsystem in Graviton reduces
  latency for many operations compared to x86. This benefits
  real-time and latency-sensitive applications.
- **Improved throughput:** Graviton's support for new
  instructions like ARM Neon SIMD improves parallel processing throughput for workloads
  like video encoding and transcoding.
- **Enhanced networking:** Up
  to 25 Gbps of network bandwidth from the Nitro chip provides
  high throughput for network-intensive apps.
- **Burstable performance:** Graviton's TDP and credits system allows workloads to burst performance as needed.
- **Accelerated compression:** Hardware-based compression provided by the Nitro chip speeds up compressed workloads.
- **Caching optimizations:**
  Graviton optimizes cache utilization and memory access,
  leading to gains for memory bound workloads.

## Key AWS services

- [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")

## Resources

- [Optimizing
  for performance](../../../whitepapers/latest/aws-graviton2-for-isv/optimizing-for-performance.md "../../../whitepapers/latest/aws-graviton2-for-isv/optimizing-for-performance.md")
- [Considerations
  when transitioning workloads to AWS Graviton based Amazon EC2 instances](https://github.com/aws/aws-graviton-getting-started/blob/main/transition-guide.md "https://github.com/aws/aws-graviton-getting-started/blob/main/transition-guide.md")
- [Using
  Porting Advisor for Graviton](https://aws.amazon.com/blogs/compute/using-porting-advisor-for-graviton/ "https://aws.amazon.com/blogs/compute/using-porting-advisor-for-graviton/")
