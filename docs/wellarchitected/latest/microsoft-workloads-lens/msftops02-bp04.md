# MSFTOPS02-BP04 Leverage managed services for your Microsoft

workload

To reduce operational overhead, implement the use of AWS managed
services to address your Microsoft workload requirements. Consider
AWS Managed Microsoft Active Directory, Amazon Relational Database Service for SQL Server, Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP, AWS Elastic Beanstalk, and others.

**Desired outcome:** Reduce
operational complexity and overhead for your Microsoft workloads by
strategically adopting AWS managed services that handle
infrastructure management, patching, backups, and scaling
automatically, allowing your team to focus on application
development and business value rather than infrastructure
maintenance.

**Common anti-patterns:**

- Managing Microsoft infrastructure components manually when
  equivalent AWS managed services are available, leading to
  increased operational overhead, higher maintenance costs, and
  potential security vulnerabilities from delayed patching.
- Choosing self-managed solutions without evaluating the total
  cost of ownership, including operational effort, expertise
  requirements, and ongoing maintenance compared to AWS managed
  service alternatives.
- Implementing managed services without proper integration
  planning, resulting in architectural complexity, security gaps,
  or performance issues that could have been avoided with better
  design considerations.

**Benefits of establishing this best
practice:**

- Significantly reduced operational overhead through AWS-managed
  infrastructure components that handle patching, backups,
  monitoring, and scaling automatically, freeing up resources for
  higher-value activities.
- Improved reliability and availability through AWS-managed
  services that provide built-in high availability, disaster
  recovery, and automated failover capabilities designed and
  tested by AWS experts.
- Enhanced security posture through managed services that include
  automatic security updates, encryption capabilities, and
  compliance features that are maintained and updated by AWS
  according to industry best practices.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing AWS managed services for Microsoft workloads requires
careful evaluation of your current architecture and identification
of components that can be replaced or enhanced with managed
alternatives. Begin by assessing your Microsoft workload
components and their operational requirements, then systematically
migrate to appropriate AWS managed services while ensuring proper
integration and security.

### Implementation steps

1. Conduct a comprehensive assessment of your current Microsoft
   workload architecture to identify components suitable for
   managed service replacement.
2. Evaluate AWS managed service options including AWS Managed Microsoft AD, Amazon RDS for SQL Server, Amazon FSx for Windows File Server, and AWS Elastic Beanstalk.
3. Develop a migration strategy that prioritizes
   high-maintenance components and considers dependencies
   between services and applications.
4. Implement pilot migrations with non-critical workloads to
   validate managed service configurations and integration
   patterns.
5. Configure managed services with appropriate security
   settings, backup policies, and monitoring to meet your
   operational requirements.
6. Establish connectivity and integration between managed
   services and existing Microsoft workload components using
   VPC networking and security groups.
7. Migrate production workloads systematically, ensuring proper
   testing and rollback procedures are in place for each
   migration phase.
8. Update operational procedures and documentation to reflect
   the new managed service architecture and reduced maintenance
   requirements.

## Resources

**Related documents:**

- [AWS Managed Services for Microsoft Workloads](https://aws.amazon.com/windows/ "https://aws.amazon.com/windows/")

**Related tools:**

- [AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md")
- [Amazon RDS for SQL Server](../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md "../../../AmazonRDS/latest/UserGuide/CHAP_SQLServer.md")
- [Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/what-is.md "../../../fsx/latest/WindowsGuide/what-is.md")
