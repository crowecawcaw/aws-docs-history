# MSFTCOST03-BP03 Check if your workload is running with the

right SQL Server edition

Microsoft offers types of SQL Server editions, with a different set
of features and license cost. The Enterprise edition provides data
center capabilities with high performance, unlimited virtualization,
and several business intelligence tools. The Standard edition
provides basic data management and business intelligence for smaller
organizations and departments. The Web edition is suitable for
companies that are web hosts or web value added providers (VAPs) and
it should only be used to support public and internet accessible
webpages, websites, and web services; its license does not allow the
use for line-of-business applications. The Developer edition
includes all functionality of the Enterprise edition, but it is
intended for development purposes only. And the Express edition is a
free database that can be used for learning or for building desktop
applications. Over the release of SQL versions, Microsoft has added
more features to the Standard edition, and it is not so unusual to
see customers evaluating the downgrade from the Enterprise edition
to the Standard one.

**Desired outcome:** The workload
should run on the most cost-effective SQL Server edition that meets
its functional and performance requirements. After evaluating
feature usage, performance needs, and licensing costs across
available editions (Enterprise, Standard, Web, Developer, and
Express), the organization can confirm they are using the optimal
edition or identify opportunities to downgrade to a more
cost-effective edition without compromising workload functionality
or performance targets.

**Common anti-patterns:**

- Enterprise by Default: Automatically deploying SQL Server
  Enterprise edition for all database workloads without analyzing
  actual feature requirements, resulting in unnecessary licensing
  costs for workloads that could run effectively on Standard or
  Web editions.
- Feature Underutilization: Paying for Enterprise edition licenses
  but only using features available in lower editions, such as
  using Enterprise solely for basic OLTP workloads without
  leveraging advanced features like in-memory OLTP, partitioning,
  or advanced security features.

**Benefits of establishing this best
practice:**

- Cost Optimization: Significant cost savings through appropriate
  edition selection, particularly when downgrading from Enterprise
  to Standard edition where feasible. This can result in
  significant reduction in licensing costs while maintaining
  necessary functionality for workloads that do not require
  Enterprise-specific features.
- Resource Efficiency: Better alignment of database capabilities
  with actual workload requirements, ensuring resources are
  allocated efficiently and preventing overprovisioning of
  features that aren't being utilized. This leads to more
  streamlined database management and reduced operational
  overhead.
- Compliance and Risk Management: Appropriate edition selection
  ensures compliance with licensing terms—particularly critical
  for Web edition restrictions—while maintaining suitable feature
  sets for different environments. This reduces both compliance
  risks and potential audit findings.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Conduct a thorough assessment of your SQL Server workloads using
built-in monitoring tools to identify actual feature usage and
performance requirements. Compare these against available edition
features and costs, using AWS Prescriptive Guidance to evaluate
potential downgrades. Test thoroughly in non-production
environments before implementing any edition changes, and
establish a regular review process to ensure ongoing optimization.

### Implementation steps

1. Audit current SQL Server workloads for feature usage and
   performance requirements using proper tools or scripts.
2. Compare workload needs against features available in
   different SQL Server editions, using AWS Prescriptive
   Guidance for potential downgrade scenarios.
3. Test workload performance on proposed new editions in
   non-production environments to validate functionality and
   performance.
4. Implement edition changes in a phased approach, starting
   with non-critical workloads, and establish a regular review
   process for ongoing edition optimization.

## Resources

**Related documents:**

- [Compare
  SQL Server editions](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-editions.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-editions.md")
- [Evaluate
  downgrading Microsoft SQL Server from Enterprise edition to
  Standard edition on AWS](../../../prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/welcome.md "../../../prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/welcome.md")
