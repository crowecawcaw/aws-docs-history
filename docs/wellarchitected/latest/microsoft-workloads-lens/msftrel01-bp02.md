# MSFTREL01-BP02 Align your architectural design with your

availability needs and capacity demands

There are architecture recommendations regarding Microsoft
workloads, whether addressing Windows infrastructure, Active
Directory, SQL Server databases, .NET applications, or other
technologies. Review the vendor recommendations along with AWS
documentation to verify that your application is running with best
practices to improve availability and resiliency.

**Desired outcome:** A Microsoft
workload optimized for high availability and scalability and aligned
with vendor recommendations and AWS best practices. This strategy
verifies that the system meets availability targets and capacity
demands efficiently, while remaining resilient and maintainable.

**Common anti-patterns:**

- Directly migrating Microsoft workloads to AWS without
  redesigning for cloud capabilities, resulting in missed
  opportunities for improved availability and automated scaling.
- Ignoring Microsoft's recommended high-availability
  configurations (like Always On Availability Groups for SQL
  Server) in favor of simplified single-instance deployments.
- Treating AWS Regions as simple datacenter replacements rather
  than using multi-AZ and Regional resilience patterns specific to
  AWS infrastructure.

**Benefits of establishing this best
practice:**

- Increased system reliability through proven architectural
  patterns, reducing downtime and improving customer satisfaction
  while lowering operational overhead.
- Optimized cost-efficiency by properly sizing resources and
  utilizing AWS's elastic scaling capabilities, avoiding
  over-provisioning while maintaining performance.
- Enhanced disaster recovery capabilities through AWS-specific
  resilience features combined with Microsoft's high-availability
  solutions, maintaining business continuity.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Document your current Microsoft workload architecture and
availability needs, and consult AWS and Microsoft best practices
for your specific technologies.

Develop a phased migration plan incorporating these
recommendations, prioritizing critical components.

Use AWS managed services where possible and implement multi-AZ
deployments.

Regularly test resilience and conduct Well-Architected reviews to
align with best practices.

### Implementation steps

1. Evaluate SQL Server Always On Availability Groups
   configuration, Active Directory domain controller placement,
   Exchange Database Availability Groups, SharePoint farm
   topology, and .NET application dependencies. Document
   current RTO/RPO requirements and identify single points of
   failure in your Microsoft workload stack.
2. Implement SQL Server Always On across multiple Availability
   Zones using Amazon EC2 or Amazon RDS Multi-AZ, deploy Active
   Directory domain controllers in separate Availability Zones
   with AWS Managed Microsoft AD integration, establish
   Exchange DAG with cross-AZ mailbox databases, and design
   .NET applications for stateless operation with Application Load Balancer distribution. For more detail, see
   [Microsoft
   workload architecture patterns](../../../prescriptive-guidance/latest/patterns/microsoft-workloads.md "../../../prescriptive-guidance/latest/patterns/microsoft-workloads.md").
3. Replace self-managed components with Amazon RDS for SQL
   Server, AWS Managed Microsoft AD, Amazon FSx for Windows File Server, and AWS Systems Manager for Windows patch
   management. This reduces operational overhead while
   improving availability through AWS-managed infrastructure
   resilience.
4. Configure SQL Server Always On listener endpoints across
   Availability Zones, establish Active Directory site topology
   aligned with Availability Zones, implement Exchange
   transport high availability, and verify that .NET
   applications handle Availability Zone failures gracefully.
   Reference
   [Microsoft
   SQL Server on AWS best practices](../../../prescriptive-guidance/latest/sql-server-ec2-best-practices/welcome.md "../../../prescriptive-guidance/latest/sql-server-ec2-best-practices/welcome.md").
5. Test SQL Server failover scenarios, Active Directory
   replication across Availability Zones, Exchange mailbox
   database switchovers, and .NET application resilience to
   infrastructure failures. Establish automated testing
   procedures that validate both AWS infrastructure and
   Microsoft application layer availability.

## Resources

**Related documents:**

- [Design
  your workload service architecture](../reliability-pillar/design-your-workload-service-architecture.md "../reliability-pillar/design-your-workload-service-architecture.md")
