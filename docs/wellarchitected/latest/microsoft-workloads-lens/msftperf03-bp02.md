# MSFTPERF03-BP02 Consider Amazon EBS io2 Block Express volumes

for high-intense I/O workloads

Amazon EBS io2 Block Express volumes are based on an updated storage
server architecture. They are designed to handle high I/O
requirements for applications running on Nitro System-based
instances. These volumes offer improved durability and lower
latency. As a result, they are suitable for resource-intensive
applications that require consistent performance, such as certain
database systems (For example, Oracle, SAP HANA, and Microsoft SQL
Server) and SAS Analytics.

**Desired outcome:** Achieve maximum
I/O performance and lowest latency for demanding Microsoft
workloads, particularly SQL Server databases and other I/O-intensive
applications, through io2 Block Express volumes that provide
consistent high-performance storage with enhanced durability and
reliability.

**Common anti-patterns:**

- Using general-purpose storage for high-performance Microsoft SQL
  Server databases without evaluating io2 Block Express benefits,
  potentially limiting application performance and user
  experience.
- Implementing io2 Block Express for workloads that don't require
  extreme I/O performance, leading to unnecessary costs without
  proportional performance benefits.
- Choosing io2 Block Express without ensuring compatibility with
  Nitro System-based instances, missing the full performance
  potential of the storage technology.

**Benefits of establishing this best
practice:**

- Maximum I/O performance through io2 Block Express architecture
  designed specifically for high-intensity workloads, enabling
  optimal performance for demanding Microsoft applications.
- Enhanced reliability and durability through improved storage
  architecture that provides consistent performance and reduced
  latency for mission-critical workloads.
- Improved application responsiveness for I/O-intensive Microsoft
  workloads including SQL Server databases, analytics
  applications, and high-performance computing scenarios.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing io2 Block Express volumes requires careful evaluation
of I/O requirements and cost considerations. Focus on workloads
that genuinely require extreme I/O performance and can justify the
additional costs through improved application performance and
business outcomes.

### Implementation steps

1. Identify Microsoft workloads with high I/O requirements that
   would benefit from io2 Block Express performance
   characteristics, particularly SQL Server databases and
   analytics applications.
2. Analyze current I/O patterns including IOPS requirements,
   throughput needs, and latency sensitivity to determine if
   io2 Block Express is appropriate.
3. Ensure compatibility with Nitro System-based instances that
   can fully utilize io2 Block Express performance
   capabilities.
4. Configure io2 Block Express volumes with appropriate IOPS
   provisioning based on workload requirements and performance
   testing results.
5. Implement performance testing in non-production environments
   to validate expected performance improvements and cost
   justification.
6. Monitor storage performance metrics including IOPS
   utilization, throughput, and latency to ensure optimal
   configuration and utilization.
7. Establish cost monitoring and optimization procedures to
   ensure io2 Block Express usage remains cost-effective for
   the performance benefits provided.
8. Document io2 Block Express configuration standards and use
   cases for consistent implementation across high-performance
   Microsoft workloads.

## Resources

**Related documents:**

- [Provisioned
  IOPS SSD (io2 Block Express) volumes](../../../ebs/latest/userguide/provisioned-iops.md#io2-block-express "../../../ebs/latest/userguide/provisioned-iops.md#io2-block-express")
- [Best
  practices for Amazon RDS for SQL Server with Amazon EBS io2
  Block Express volumes up to 64 TiB](https://aws.amazon.com/blogs/database/best-practices-for-amazon-rds-for-sql-server-with-amazon-ebs-io2-block-express-volumes-up-to-64-tib/ "https://aws.amazon.com/blogs/database/best-practices-for-amazon-rds-for-sql-server-with-amazon-ebs-io2-block-express-volumes-up-to-64-tib/")

**Related tools:**

- [io2
  Block Express considerations](../../../ebs/latest/userguide/provisioned-iops.md#io2-bx-considerations "../../../ebs/latest/userguide/provisioned-iops.md#io2-bx-considerations")
