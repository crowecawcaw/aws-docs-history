# MSFTCOST05-BP03 Use Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP offers a file system that supports SMB
and iSCSI protocols. Useful for critical Microsoft SQL Server
environments, as ONTAP volumes can be mapped to Windows Server
instances as block storage devices using the iSCSI model, also
providing shared storage for cluster-aware applications. FSx for ONTAP has two capacity settings (HDD and SSD), data
deduplication, and cache layers. Smaller EC2 instances can leverage
the FSx solution to achieve high performance storage levels.

**Desired outcome:** By implementing
Amazon FSx for NetApp ONTAP, an organization can achieve a highly
available and performant storage solution for Microsoft workloads.
The implementation will leverage both SMB and iSCSI protocols,
enabling efficient block storage access while benefiting from
advanced features like data deduplication and multi-tiered caching.
This will result in optimized storage costs, improved performance
even with smaller EC2 instances, and reduced operational overhead
for managing Microsoft workloads.

**Common anti-patterns:**

- Running Microsoft SQL Server or other Microsoft workloads with
  directly attached EBS volumes may limit high availability and
  scalability, making failover scenarios complex and
  time-consuming. This approach also lacks the advanced storage
  management features and efficiency benefits provided by FSx for ONTAP, potentially leading to higher costs and
  operational overhead.
- Compensating for storage performance requirements by using
  oversized EC2 instances with local storage or multiple EBS
  volumes, rather than leveraging FSx for ONTAP's efficient
  storage architecture. This results in unnecessary compute costs
  and doesn't address the underlying need for enterprise-grade
  storage features like deduplication and efficient snapshots.

**Benefits of establishing this best
practice:**

- FSx for ONTAP provides high-performance storage, allowing
  even small EC2 instances to achieve excellent I/O capabilities.
- Easily scale storage capacity and performance independently of
  compute resources, adapting to changing workload demands.
- Reduce management overhead with built-in features like data
  deduplication, snapshots, and multi-protocol support.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement FSx for ONTAP for Microsoft workloads, create
an FSx file system in your VPC. Configure SVMs and volumes for
your applications, setting up SMB shares and iSCSI LUNs as needed.
Connect Windows instances to these resources using native tools.
For high availability, use Windows Server Failover Clustering with
FSx as shared storage. Migrate your data, then update backup and
recovery processes to leverage FSx features like snapshots and
replication.

### Implementation steps

1. Create FSx for ONTAP file system within your VPC,
   configuring the appropriate storage capacity and throughput
   based on workload requirements
2. Set up Storage Virtual Machines (SVMs) and configure storage
   volumes with proper protocols (SMB/iSCSI) based on your
   Microsoft application needs
3. Connect Windows Server instances to FSx storage using native
   tools (File Explorer for SMB, iSCSI Initiator for block
   storage)
4. Configure Windows Server Failover Clustering if high
   availability is required, using FSx for ONTAP as the shared
   storage
5. Migrate existing data to FSx storage and implement
   backup/recovery procedures using ONTAP's snapshot and
   replication capabilities

## Resources

**Related documents:**

- [What
  is Amazon FSx for NetApp ONTAP?](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md")
- [Provisioning
  iSCSI for Windows](../../../fsx/latest/ONTAPGuide/mount-iscsi-windows.md "../../../fsx/latest/ONTAPGuide/mount-iscsi-windows.md")
