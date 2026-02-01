# DSREL08-BP01 Maintain a map of key dependencies

Without clear dependency mapping, organizations cannot effectively
assess incident impact or meet audit requirements. They also cannot
make informed architectural decisions that protect critical business
functions and improve regulatory adherence.

**Desired outcome:** Organizations
maintain current, comprehensive dependency maps providing complete
visibility into service relationships, data flows, and critical path
dependencies. Infrastructure, applications, and third-party services
are mapped to proactively manage risks and compliance.

**Common anti-patterns:**

- Relying on spreadsheets or static documents that quickly become
  outdated, without automated discovery and updates using AWS
  tools.
- Different teams maintaining separate, incompatible dependency
  maps without centralized coordination or cross-functional
  visibility.
- Focusing only on application dependencies while ignoring
  infrastructure, network, data, and third-party services and
  APIs.
- Failing to identify and classify mission-critical paths, single
  points of failure, pre and post-recovery validation processes.

**Benefits of establishing this best
practice:**

- Rapidly identify downstream impacts, accelerate root cause
  analysis, and prioritize remediation efforts during outages
  through clear understanding of service interdependencies.
- Meet regulatory requirements while proactively identifying and
  reducing single points of failure through comprehensive system
  documentation.
- Make informed technology decisions and optimize disaster
  recovery strategies based on complete understanding of critical
  dependency chains.
- Identify cost optimization opportunities through unused
  resources while enhancing cross-team collaboration with shared
  architectural understanding.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To maintain a dependency map, start by inventorying AWS resources,
third-party services, and data flows. Use automation to track
relationships and changes. Prioritize critical workloads and
validate dependencies against compliance frameworks.

- Deploy automated discovery and mapping tools across AWS accounts and Regions
- Establish standardized tagging strategies to enable dependency
  correlation
- Create regular validation and update processes for dependency
  accuracy
- Integrate dependency maps into operational dashboards and
  incident response procedures

### Implementation steps

1. Inventory AWS resources, third-party services, and data
   flows. Gain a comprehensive understanding of your current
   infrastructure and dependencies. Confirm that you have
   documented your current infrastructure topology and
   dependencies before proceeding with changes or
   optimizations.
2. Deploy automated discovery and mapping tools across AWS accounts and Regions. Consider services like:
   - [AWS X-Ray](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") or an alternative application tracing
     service to discover runtime dependencies.
   - [AWS Systems Manager Inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md") to discover metadata
     about your managed nodes. Example metadata include EC2
     driver, agents, version, tags assigned to nodes,
     CPUModel,
     CPUCores, CPUs, and
     CPUSpeedMHz.
   - [AWS Application Discovery Service](../../../application-discovery/latest/userguide/what-is-appdiscovery.md "../../../application-discovery/latest/userguide/what-is-appdiscovery.md") to discover
     on-premises servers and databases.
   - And open-source tools like
     [Steampipe](https://steampipe.io/ "https://steampipe.io/")
     to search and build resource inventories.

3. Establish standardized tagging strategies to enable
   dependency correlation. Define and apply a consistent AWS
   tagging schema to each resource, allowing you to categorize,
   track, and manage relationships between applications and
   resources.
4. Prioritize critical workloads and validate dependencies
   against compliance frameworks. Regularly review and update
   your dependency maps to maintain adherence to regulatory
   requirements and meet your operational needs.
5. Integrate dependency maps into operational dashboards and
   incident response procedures. This allows you to quickly
   identify and mitigate risks and maintain adherence during
   incidents.

## Resources

**Related best practices:**

- [Design
  interactions in a distributed system to prevent
  failures](../reliability-pillar/design-interactions-in-a-distributed-system-to-prevent-failures.md "../reliability-pillar/design-interactions-in-a-distributed-system-to-prevent-failures.md")
- [Operational
  readiness and change management](../operational-excellence-pillar/operational-readiness.md "../operational-excellence-pillar/operational-readiness.md")

**Related documents:**

- [Disaster
  Recovery of Workloads on AWS: Recovery in the Cloud](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.md")

**Related videos:**

- [How
  AWS Application Discovery Service Maps Your IT
  Environment](https://www.youtube.com/watch?v=AasMg7BsH1o "https://www.youtube.com/watch?v=AasMg7BsH1o")
- [Establishing
  a Data Perimeter on AWS: USAA's Journey to Automated Security
  Controls](https://aws.amazon.com/awstv/watch/7bfd0425cfb/ "https://aws.amazon.com/awstv/watch/7bfd0425cfb/")
- [AWS re:Invent 2024 - How to maintain and automate compliance on
  AWS (SEC319)](https://www.youtube.com/watch?v=o93VHX4V7jY "https://www.youtube.com/watch?v=o93VHX4V7jY")
