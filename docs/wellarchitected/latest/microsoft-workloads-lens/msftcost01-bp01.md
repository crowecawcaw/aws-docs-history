# MSFTCOST01-BP01 Run discovery tools

Migration Evaluator is a migration assessment service that helps you
create a directional business case for AWS cloud planning and
migration. The information that the AWS Migration Evaluator collects
includes server profile information (for example, OS, number of
CPUs, amount of RAM), SQL Server metadata (for example, version and
edition), utilization metrics, and network connections. AWS
Application Discovery Service helps you plan cloud migration
projects, by gathering information about your on-premises data
centers. It discovers the connections between applications and
servers to uncover unknown servers, better understand dependencies,
and establish move groups.

**Desired outcome:** Gain
comprehensive visibility into your infrastructure environment by
collecting detailed server profiles, SQL Server configurations,
utilization patterns, and application dependencies to create an
accurate business case for cloud migration and optimize resource
planning.

**Common anti-patterns:**

- Relying on manual inventory tracking and documentation, leading
  to incomplete or outdated infrastructure information and missed
  optimization opportunities.
- Making migration decisions based solely on static server
  specifications without considering actual utilization patterns
  and application dependencies.
- Planning cloud migrations in isolation without understanding the
  full scope of application relationships, resulting in overlooked
  servers and disrupted service connections.

**Benefits of establishing this best
practice:**

- Accurate cost projections and resource planning through
  automated discovery of server configurations, SQL Server
  metadata, and utilization metrics.
- Reduced migration risks by identifying hidden dependencies and
  establishing appropriate move groups based on discovered
  application connections.
- Optimized infrastructure spend by right-sizing resources based
  on actual utilization patterns rather than assumptions or
  outdated documentation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing comprehensive infrastructure discovery through tools
like AWS Migration Evaluator and AWS Application Discovery Service
is crucial for successful cloud migrations and cost optimization.
These tools automatically collect detailed information about
server configurations, SQL Server deployments, resource
utilization, and application dependencies, replacing error-prone
manual tracking methods. This automated approach not only provides
accurate data for building business cases and planning migrations
but also helps organizations avoid the common pitfalls of
oversizing resources or missing critical application connections,
ultimately leading to more successful and cost-effective cloud
deployments.

### Implementation steps

- Deploy AWS Application Discovery Agent on target servers or
  configure AWS Application Discovery Agentless Collector for
  VMware environments
- Enable data collection in AWS Migration Hub
- Monitor and analyze collected data, including server
  profiles, utilization patterns, and application dependencies
- Generate reports and recommendations for migration business
  case, infrastructure requirements, migration waves, and
  resource optimization strategies

## Resources

**Related documents:**

- [Discover
  on-premises resources using AWS Migration Hub discovery
  tools](../../../migrationhub/latest/ug/gs-new-user-discovery.md "../../../migrationhub/latest/ug/gs-new-user-discovery.md")

**Related tools:**

- [Migration
  Evaluator](https://aws.amazon.com/migration-evaluator/ "https://aws.amazon.com/migration-evaluator/")
