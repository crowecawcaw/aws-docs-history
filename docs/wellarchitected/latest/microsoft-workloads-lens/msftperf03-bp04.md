# MSFTPERF03-BP04 Consider Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP is a fully managed AWS service that
provides scalable, high-performance file storage based on the
widely-used NetApp ONTAP file system. It combines the familiar
features and capabilities of NetApp systems with the benefits of a
cloud-managed service. This service offers fast, flexible shared
file storage accessible from Linux, Windows, and macOS instances,
both in AWS and on-premises. FSx for ONTAP provides high-performance
SSD storage with very low latencies and also HDD storage. Amazon FSx for NetApp ONTAP offers robust file storage capabilities, including
support for petabyte-scale datasets in a single namespace and high
throughput of up to tens of GBps per file system.

**Desired outcome:** Achieve
enterprise-grade, high-performance file storage for Microsoft
workloads through FSx for ONTAP, providing multi-protocol
access, advanced data management features, and cost optimization
capabilities while maintaining compatibility with existing NetApp
environments and Microsoft applications.

**Common anti-patterns:**

- Using basic file storage solutions for enterprise Microsoft
  workloads without evaluating FSx for ONTAP's advanced features,
  missing opportunities for performance optimization and data
  management capabilities.
- Implementing FSx for ONTAP without leveraging its multi-protocol
  capabilities, limiting the potential for workload consolidation
  and simplified architecture.
- Choosing FSx for ONTAP configurations without considering data
  tiering and compression features, potentially missing
  significant cost optimization opportunities.

**Benefits of establishing this best
practice:**

- Superior performance and scalability through NetApp ONTAP
  technology providing high throughput, low latency, and support
  for petabyte-scale datasets in a single namespace.
- Advanced data management capabilities including automatic
  tiering, compression, deduplication, and snapshot technologies
  that optimize both performance and costs.
- Multi-protocol flexibility supporting NFS, SMB, iSCSI, and NVMe
  protocols, enabling consolidation of diverse Microsoft workload
  storage requirements on a single platform.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing Amazon FSx for NetApp ONTAP requires understanding
your enterprise storage requirements and planning for advanced
data management features. Focus on workloads that can benefit from
multi-protocol access, advanced data services, and cost
optimization through data efficiency features.

### Implementation steps

1. Assess enterprise storage requirements for Microsoft
   workloads including performance, capacity, protocol needs,
   and data management requirements.
2. Evaluate existing NetApp environments and plan migration
   strategies to leverage familiar ONTAP features in the cloud.
3. Configure FSx for ONTAP file systems with appropriate
   performance tiers, capacity planning, and multi-protocol
   access based on workload requirements.
4. Implement data efficiency features including compression,
   deduplication, and automatic tiering to optimize storage
   costs and performance.
5. Configure multi-protocol access (SMB, NFS, iSCSI) to support
   diverse Microsoft workload requirements and enable workload
   consolidation.
6. Establish backup and disaster recovery procedures using
   ONTAP's snapshot and replication capabilities for data
   protection.
7. Monitor storage performance, utilization, and cost
   optimization through CloudWatch metrics and ONTAP management
   tools.
8. Implement ongoing data management policies including
   tiering, retention, and capacity planning to maintain
   optimal performance and costs.

## Resources

**Related documents:**

- [What
  is Amazon FSx for NetApp ONTAP?](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md")
- [Managing
  storage on Windows servers with Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/managing-storage-on-windows-servers-with-amazon-fsx-for-netapp-ontap/ "https://aws.amazon.com/blogs/storage/managing-storage-on-windows-servers-with-amazon-fsx-for-netapp-ontap/")
- [Best
  practice configuration of Amazon FSx for NetApp ONTAP for
  Microsoft SQL Server workloads](https://aws.amazon.com/blogs/storage/best-practice-configuration-of-amazon-fsx-for-netapp-ontap-for-microsoft-sql-server-workloads/ "https://aws.amazon.com/blogs/storage/best-practice-configuration-of-amazon-fsx-for-netapp-ontap-for-microsoft-sql-server-workloads/")
- [AWS Guidance: Best Practices for running MSSQL workloads on FSx for ONTAP](https://repost.aws/articles/AROwbUp134QbGhtrPPEYeuog/aws-guidance-best-practices-for-running-mssql-workloads-on-fsx-for-netapp-ontap "https://repost.aws/articles/AROwbUp134QbGhtrPPEYeuog/aws-guidance-best-practices-for-running-mssql-workloads-on-fsx-for-netapp-ontap")

**Related tools:**

- [Amazon FSx for NetApp ONTAP performance](../../../fsx/latest/ONTAPGuide/performance.md "../../../fsx/latest/ONTAPGuide/performance.md")
