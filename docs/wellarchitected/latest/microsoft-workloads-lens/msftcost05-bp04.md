# MSFTCOST05-BP04 Use

Amazon FSx for Windows File Server

Amazon FSx for Windows File Server is a fully managed file storage service that's optimized for Microsoft
workloads. It provides an SMB file system that can be accessed by applications, including
Windows web servers and Microsoft SQL Server. FSx for Windows File Server is a scalable solution that offers
Single AZ or Multi AZ availability, automatic data deduplication, different pricing options, and
two capacity settings (HDD and SSD), being flexible to fit your Microsoft workloads. Fairly
small EC2 instances can leverage the FSx solution to achieve high performance storage levels.

**Desired outcome:** Implement Amazon FSx for Windows File Server to optimize storage
for Microsoft workloads, reducing operational overhead while enhancing scalability and
performance. This change aims to improve efficiency, simplify management, and potentially reduce
costs associated with file storage for Windows-based applications in AWS.

**Common anti-patterns:**

- Running Windows file servers on EC2 instances with attached EBS volumes, requiring
  manual management of storage capacity, backups, and Windows Server maintenance while
  incurring higher operational costs and complexity.
- Using non-Windows-optimized storage solutions for Windows workloads, resulting in
  compatibility issues, degraded performance, and the need for additional software or
  configurations to handle SMB protocol requirements.

**Benefits of establishing this best practice:**

- Eliminates the need for manual file server management, Windows patching, and backup
  administration through AWS's fully managed service.
- Provides high-performance storage with automatic capacity management and the ability to
  scale up or down based on workload demands, while supporting both Single-AZ and Multi-AZ
  deployments.
- Offers flexible storage options (HDD/SSD) and pricing models, allowing organizations to
  align costs with actual needs while eliminating the overhead of maintaining dedicated
  Windows file servers and associated licenses.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Begin by assessing your current Windows workload requirements, including storage
capacity, performance needs, and availability requirements. Choose between Single-AZ or
Multi-AZ deployment based on your reliability needs, and select the appropriate storage type
(HDD for general purpose or SSD for performance-intensive workloads). Start with a pilot
migration of a non-critical workload to validate the setup and performance. Configure your
existing Windows applications and services to connect to the FSx file system using standard
SMB protocol, and implement appropriate security groups and Active Directory integration. Once
validated, proceed with a phased migration approach for remaining workloads while monitoring
performance metrics through CloudWatch.

### Implementation steps

1. Assess workload requirements and select appropriate FSx configuration
   (Single/Multi-AZ, HDD/SSD, and storage capacity) based on performance needs and budget
   constraints.
2. Configure network security by setting up VPC security groups, ensuring proper
   routing, and establishing Active Directory integration for authentication.
3. Migrate existing file data to FSx using AWS DataSync or standard file copy tools,
   validating data integrity and permissions post-migration.
4. Update application configurations to point to the new FSx file share endpoints and
   verify connectivity, performance, and functionality across all dependent services.

## Resources

**Related documents:**

- [Amazon FSx for Windows File Server](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx.md")

**Related tools:**

- [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/")
