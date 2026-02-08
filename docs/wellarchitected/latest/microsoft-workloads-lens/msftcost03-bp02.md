# MSFTCOST03-BP02 Consolidate Microsoft SQL Server

instances

A SQL instance is part of the SQL Server Database Engine, that
provides the SQL service to clients or applications. It is common to
have SQL instances installed per server when it comes to large
production environments, to avoid resources issues and to follow
resource governance. Although, for smaller or non-critical workloads
organizations can leverage shared resources and have multiple SQL
instances installed on the same server or set of servers. This
approach will help your workload save costs on SQL licensing (less
cores running SQL) and often in compute resources as well.

**Desired outcome:** Optimize costs
and resource utilization by strategically consolidating Microsoft
SQL Server instances, particularly for smaller or non-critical
workloads. This approach aims to reduce SQL licensing expenses by
minimizing the number of cores running SQL Server, while also
potentially decreasing overall compute resource consumption. By
carefully assessing workload requirements and identifying
consolidation opportunities, organizations can achieve significant
cost savings without compromising performance for mission-critical
applications.

**Common anti-patterns:**

- Over-isolation: Deploying separate SQL Server instances for
  every application or workload, regardless of size or
  criticality, leading to unnecessary licensing costs and
  underutilized resources.
- Indiscriminate consolidation: Merging SQL Server instances
  without proper assessment of workload characteristics, resource
  requirements, and potential conflicts, resulting in performance
  degradation and operational issues for critical applications.

**Benefits of establishing this best
practice:**

- Reduced Licensing Costs: By consolidating multiple SQL Server
  instances, particularly those running on less than 4 vCPUs,
  organizations can significantly reduce licensing expenses since
  SQL Server requires licensing for a minimum of 4 vCPUs per
  instance regardless of actual usage.
- Optimized Resource Utilization: Consolidation enables more
  efficient use of compute resources by sharing infrastructure
  across multiple workloads, reducing the total number of servers
  required and decreasing overall infrastructure costs.
- Simplified Management Overhead: Fewer SQL Server instances mean
  reduced administrative effort for maintenance, patching, backup
  management, and monitoring, leading to operational efficiency
  and lower management costs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement SQL Server instance consolidation, assess workload
patterns and resource requirements to identify compatible
instances for merging, prioritizing non-critical workloads and
especially targeting instances with less than 4 vCPUs since SQL
Server requires licensing for a minimum of 4 vCPUs regardless of
actual usage. Use AWS migration tools for consolidation, implement
resource governance for effective management, and maintain regular
performance monitoring to ensure optimal efficiency while reducing
licensing costs.

### Implementation steps

1. Conduct a comprehensive assessment of existing SQL Server
   instances, identifying workloads using less than 4 vCPUs and
   evaluating resource usage patterns, performance
   requirements, and compatibility.
2. Create a consolidation plan that groups compatible
   workloads, prioritizing non-critical applications and
   instances that can share resources without performance
   impact.
3. Implement database migrations between instances as needed,
   leveraging AWS Database Migration Service to facilitate the
   process.
4. Establish monitoring and review processes to track
   performance metrics, resource utilization, and cost savings
   of the consolidated environment.

## Resources

**Related documents:**

- [Consolidate
  instances](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/consolidate-instances.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/consolidate-instances.md")

**Related tools:**

- [AWS Database Migration Service](https://aws.amazon.com/dms/ "https://aws.amazon.com/dms/")
