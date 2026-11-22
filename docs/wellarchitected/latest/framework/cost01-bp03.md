

# COST01-BP03 Track project lifecycle

 A project ends, a workload moves to production, an experiment concludes, yet the environments behind them keep running and costing money. Track the lifecycle of projects, teams, and environments so you can decommission or resize resources that no longer serve an active need. 

 **Desired outcome:** 
+  You have visibility into which projects, teams, and environments own each set of resources, and their current status. 
+  Your resources carry lifecycle metadata such as environment, criticality, cost center, and the date they were last reviewed. 
+  You resize or shut down non-production environments when they are not in active use. 
+  You have a defined process and cadence for reviewing workloads and retiring resources that are no longer needed. 
+  Your active cloud footprint reflects current business needs rather than the accumulated history of past projects. 

 **Common anti-patterns:** 
+  Keeping unused or obsolete resources running because no one is responsible for retiring them. 
+  Running development and staging environments at full capacity around the clock when they are used only during working hours. 
+  Reviewing project environments rarely or never, so waste accumulates unnoticed. 
+  Tracking resources without recording which project or lifecycle stage they belong to. 
+  Treating decommissioning as a risk to avoid rather than a routine part of the lifecycle. 

 **Benefits of establishing this best practice:** 
+  Cost falls as idle and oversized resources are found and retired. 
+  Ownership is clear, because each resource maps to a project, team, and lifecycle stage. 
+  Reviews stay proportionate, because effort follows the risk, value, and cost of each workload. 
+  Capacity adjusts as projects move between stages, matching spend to current need. 
+  Decommissioning becomes a normal operation rather than a rare, high-anxiety event. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every workload moves through stages: design and development, testing, production, ongoing support, and eventual retirement. Tracking the project lifecycle means knowing which stage each workload is currently in and reviewing whether its resources still match that stage. 

 Lifecycle tracking also surfaces resources that a newer service has made unnecessary. A workload component that looked essential when it was built can often be replaced or removed after a managed alternative ships. Once a workload reaches production, the environments that supported earlier stages can often be reduced or shut down until they are needed again. 

 Useful tracking depends on metadata. When resources carry attributes like environment, criticality, cost center, and last-reviewed date, you can tell whether a resource still earns its cost. The last-reviewed date is especially valuable: a development environment untouched for months is a signal to check whether anyone still uses it. Group resources by application with [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html) and a consistent tagging standard to track this metadata. Report each application's cost through [AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html). 

 Build an accurate inventory. [AWS Config](https://aws.amazon.com/config/) and [AWS Systems Manager](https://aws.amazon.com/systems-manager/) record which resources exist and how they are configured. Combine that data with events and metrics to see lifecycle changes. Most organizations already run project or asset management systems. Feed your cloud inventory into those systems so lifecycle events show up where teams already work. [Application Lifecycle Management (ALM)](https://aws.amazon.com/what-is/application-lifecycle-management/) applies the same discipline to software across teams, tools, and processes. 

 Assign ownership of lifecycle tracking to a central team, often a cloud center of excellence, which defines how to monitor and review workloads. Match review depth to the stakes: a revenue-critical production workload warrants close analysis, but a small internal tool does not. Judge each workload on its risk to the organization, its value or contribution, its cost, and its usage. When any of these attributes shifts, adjust the workload, from partial resizing to full decommissioning. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a lifecycle monitoring process and owner:** Assign ownership of lifecycle tracking to a central team such as the [cloud center of excellence](https://aws.amazon.com/blogs/publicsector/the-need-for-a-cloud-center-of-excellence-in-digital-transformation/). Define a structured, transparent process for monitoring workloads that emphasizes visibility and continuous improvement. 

1.  **Tag resources with lifecycle metadata:** Apply attributes such as environment, criticality, cost center, and last-reviewed date to your resources, and group them by application with [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups.html). Consistent metadata is what makes later reviews and decommissioning decisions possible. 

1.  **Build and integrate a resource inventory:** Use [AWS Config](https://aws.amazon.com/config/) and [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to maintain a detailed inventory of resources and their configuration. Feed this data into your existing project or asset management systems so lifecycle events are tracked where teams already work. 

1.  **Review workloads on a regular cadence:** Following your organizational policies, audit existing projects at a frequency that matches their risk, value, and cost. Assess each workload's risk of incident or downtime, contribution to the organization, total cost, and usage, then identify environments that can be resized or shut down. Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) or the [Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid) to track cost allocation tag coverage and how workloads change over time. 

1.  **Decommission or resize resources that no longer fit:** When a review shows a workload has changed stage or lost value, act on it: reduce capacity, move to a different service tier, or fully decommission. Record the outcome and the next review date so the lifecycle record stays current. Where an environment is still needed but not continuously, schedule it rather than reviewing it again each cycle: [Resource Scheduler](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-scheduler.html) in AWS Systems Manager Quick Setup starts and stops Amazon EC2 instances by tag on a schedule you define, across accounts and Regions, with no infrastructure to deploy. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST01-BP04 Keep up-to-date with new service releases](cost01-bp04.md) 
+  [COST02-BP01 Implement granular resource tagging for workload cost allocation](cost02-bp01.md) 
+  [COST03-BP01 Track resources over their lifetime](cost03-bp01.md) 
+  [COST03-BP02 Implement efficient resource lifecycle management](cost03-bp02.md) 

 **Related documents:** 
+  [Guidance for Tagging on AWS](https://docs.aws.amazon.com/solutions/tagging-on-aws/) 
+  [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) 
+  [What is ALM (Application Lifecycle Management)?](https://aws.amazon.com/what-is/application-lifecycle-management/) 

 **Related examples:** 
+  [Service control policy (SCP) examples](https://github.com/aws-samples/service-control-policy-examples) 

 **Related services:** 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 