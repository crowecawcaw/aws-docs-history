# MSFTPERF03-BP03 Consider Amazon FSx for Windows File Server

Amazon FSx for Windows File Server is a managed service that
provides file storage using Microsoft Windows file system
technology. It supports Windows file system features and uses the
Server Message Block (SMB) protocol for network file access, making
it compatible with various Windows-based enterprise workloads and
applications. The service offers integration with other AWS services
and performance optimized for enterprise applications, aiming to
provide low-latency file storage. FSx for Windows File Server is
designed for Windows workloads that require shared file storage,
such as File Servers, Application Server configuration stores, and
even Microsoft SQL Server databases.

**Desired outcome:** Achieve
high-performance, fully managed Windows file storage that seamlessly
integrates with Microsoft workloads, providing native Windows file
system features, SMB protocol support, and optimized performance
while reducing operational overhead through AWS-managed
infrastructure.

**Common anti-patterns:**

- Implementing self-managed Windows file servers on EC2 without
  evaluating FSx benefits, missing opportunities to reduce
  operational overhead and improve performance through managed
  services.
- Using general-purpose storage solutions for Windows workloads
  that require specific Windows file system features, potentially
  limiting functionality and performance.
- Choosing FSx configurations without proper performance analysis,
  leading to either over-provisioned resources that increase costs
  or under-provisioned storage that impacts application
  performance.

**Benefits of establishing this best
practice:**

- Reduced operational overhead through fully managed Windows file
  storage that eliminates the need to manage file server
  infrastructure, patching, and maintenance tasks.
- Enhanced performance and reliability through AWS-managed
  infrastructure optimized for Windows workloads with built-in
  high availability and backup capabilities.
- Native Windows integration providing full compatibility with
  Windows file system features, Active Directory integration, and
  SMB protocol support for seamless application integration.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing Amazon FSx for Windows File Server requires
understanding your file storage requirements and migration
planning from existing file server infrastructure. Focus on
workloads that require Windows-native file system features and can
benefit from managed service advantages.

### Implementation steps

1. Assess current Windows file storage requirements including
   capacity, performance, and feature needs for your Microsoft
   workloads.
2. Evaluate existing file server infrastructure and identify
   workloads suitable for migration to FSx for Windows File Server.
3. Choose appropriate FSx deployment options including
   Single-AZ or Multi-AZ configurations based on availability
   and performance requirements.
4. Configure FSx file systems with appropriate storage
   capacity, throughput, and IOPS settings based on workload
   analysis and performance testing.
5. Plan migration procedures for existing file shares and data,
   including user access permissions and Active Directory
   integration.
6. Implement backup and disaster recovery strategies using
   FSx's built-in backup capabilities and cross-region
   replication options.
7. Monitor file system performance and utilization using
   CloudWatch metrics to optimize configuration and identify
   scaling needs.
8. Establish operational procedures for FSx management
   including access control, monitoring, and capacity planning
   for ongoing operations.

## Resources

**Related documents:**

- [What
  is Amazon FSx for Windows File Server?](../../../fsx/latest/WindowsGuide/what-is.md "../../../fsx/latest/WindowsGuide/what-is.md")
- [Optimizing
  Amazon FSx for Windows File Server performance with new
  metrics](https://aws.amazon.com/blogs/storage/optimizing-amazon-fsx-for-windows-file-server-performance-with-new-metrics/ "https://aws.amazon.com/blogs/storage/optimizing-amazon-fsx-for-windows-file-server-performance-with-new-metrics/")

**Related tools:**

- [Amazon FSx performance](../../../fsx/latest/WindowsGuide/performance.md "../../../fsx/latest/WindowsGuide/performance.md")
