

# FND04-BP05 Establish service quota management

 Service quotas (formerly service limits) control how many of each AWS resource type an account can provision. Unmanaged quotas cause failures when workloads hit a limit during a scaling event, a failover, or a large deployment. A central quota management capability gives workload teams visibility into their current consumption and a predictable path to request increases before they run out. 

 **Desired outcome:** 
+  Your foundation team has a central view of service quota consumption across all accounts in your organization. 
+  Your critical workloads have quotas sized for peak usage plus a safety margin, with monitoring that alerts before thresholds are reached. 
+  Your quota increase requests are submitted through a repeatable process with typical turnaround times understood by workload teams. 
+  Your new accounts receive baseline quota increases automatically during provisioning rather than waiting for the first failure to surface the gap. 
+  Your disaster recovery Regions have quotas sized for failover traffic, not just current resting load. 

 **Common anti-patterns:** 
+  Discovering a quota limit during an incident when a workload cannot scale or a failover cannot complete. 
+  Leaving new accounts with default quotas that are far below what production workloads need. 
+  Waiting until the week of a planned launch to request increases, then finding out the increase takes longer than the planned turnaround. 
+  Managing quotas per account in isolation, with no central view of which workloads are approaching limits. 
+  Sizing disaster recovery Region quotas only for the resting load those Regions carry, so failover fails because the target Region cannot take the traffic. 
+  Ignoring soft and hard limit differences, so requests that would have been approvable as soft-limit increases end up blocked by hard-limit constraints. 

 **Benefits of establishing this best practice:** 
+  Fewer quota-driven failures because consumption is monitored and increases are requested before limits are reached. 
+  Faster onboarding of new accounts because baseline quota increases are applied automatically during provisioning. 
+  Predictable failover capability because disaster recovery Regions have quotas sized for the traffic they will actually handle. 
+  Lower operational load on workload teams because the foundation team owns the quota request process and the monitoring tools. 
+  Clearer cost and capacity planning because central quota consumption data feeds capacity forecasts and commitment decisions. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Service quotas affect every workload, are set per account and per Region, and stay invisible until a workload hits one. Most organizations discover their quota gaps only during an incident: a scale-out that stops at the EC2 vCPU limit, a disaster recovery test that reveals the DR Region cannot hold the failover traffic, or a deployment that blocks on the maximum CloudFormation stack count. 

 A central quota management capability makes quotas a foundation-level service. The foundation team owns the tooling, baseline sizing, and request process. Workload teams consume the visibility and request increases without operating Service Quotas directly. 

 [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) provides a unified console and API for viewing quotas and requesting increases across services. With [AWS Organizations integration](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html), the foundation team can apply quota request templates to new accounts automatically, including accounts vended through [AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html). With [delegated administration for Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/), a designated account can manage quotas across the organization without holding credentials for every member account. 

 Use the [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/quota-monitor/) solution to track Service Quotas, Trusted Advisor service limits checks, and CloudWatch service metrics across an organization. It alerts when consumption approaches configured thresholds, giving workload and foundation teams time to request increases before workloads hit the limit. Set thresholds well below 100%. 70–80% is a common starting point. 

 Baseline sizing, where default account quotas are set conservatively by AWS, help avoid runaway spend in accounts that have not been secured. For production workload accounts, defaults are almost always too low. Establish a baseline quota profile per account type. Use different baselines for sandbox, development, and production, and apply the production baseline automatically when an account is marked as production. [Service Quotas templates](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) make this declarative. The foundation team defines the template once, and every new account in scope receives it. 

 Quotas in DR Regions default to low values because those Regions typically carry resting-state workloads. During a failover, the target Region absorbs production-scale traffic suddenly, and quota limits can prevent failover from succeeding. Size DR Region quotas for the failover scenario, not the resting load, and test the sizing as part of disaster recovery exercises. 

 Typical turnaround times vary by service and quota type. Some requests are automatic, some need human review, and some hard limits cannot be changed. Publish a quick reference so workload teams know which requests are fast and which need lead time. 

**Note**  
 Review the [Service Quotas documentation for each service](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) to understand which limits are adjustable before committing to an architecture that depends on exceeding a default. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Designate a delegated administrator for Service Quotas:** From the management account, [register a delegated administrator](https://docs.aws.amazon.com/servicequotas/latest/userguide/getting-started.html) for AWS Service Quotas, typically your central operations or foundation account. This account gains the ability to view and manage quotas across the organization without holding member-account credentials. 

1.  **Inventory current quota consumption:** Deploy the [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/quota-monitor/) solution to aggregate quota and usage data from all accounts and Regions. Review initial findings to identify quotas close to their limits, quotas that are likely undersized for current workload trajectories, and quotas that are irrelevant to your workloads. The first scan usually surfaces a backlog of immediate increase requests. 

1.  **Define baseline quota profiles per account type:** Create [quota request templates](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) for each account classification (sandbox, development, production, disaster recovery). Size production baselines for the workloads the account is expected to run. At a minimum, cover EC2 vCPU quotas per instance family, Lambda concurrent executions, CloudFormation stacks, VPC counts, and any service quota that is regularly requested. Size DR baselines to the expected failover load, not the resting load. 

1.  **Automate template application to new accounts:** Configure [AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) or your account provisioning pipeline to apply the appropriate quota request template based on account classification. New accounts marked as production must land with production-ready baseline quotas rather than AWS defaults. 

1.  **Configure monitoring and alerting:** Set monitoring thresholds in Quota Monitor (typically 70–80% of the current limit) and route alerts to the foundation team and to workload owners identified through account tags. Alerts must fire far enough ahead that there is time to request and receive an increase before the workload hits the limit. Integrate alerts with your existing operational tooling so that they surface where teams already work. 

1.  **Document the quota request process:** Publish a quick reference for workload teams covering how to check current quotas, how to submit increase requests (through Service Quotas or the foundation team's intake), typical turnaround times by service and quota type, which quotas are hard limits that cannot be changed, and how to escalate urgent requests. Link this into the shared documentation that workload teams already use. 

1.  **Review quotas during workload readiness:** Include a quota review as part of workload onboarding or production readiness reviews. Walk through the workload's expected peak load and verify that quotas in production accounts and DR accounts are sized for that peak plus a safety margin. For workloads undergoing significant scale changes (major launches, seasonal peaks), schedule a pre-event quota review with the foundation team.8. **Exercise quotas in disaster recovery tests:** Include quota verification in DR exercises. A DR test that exercises the failover path under production-scale traffic validates both the architecture and the quota sizing. Gaps discovered during tests are much less costly than gaps discovered during real failovers. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND04-BP02 Establish an organization view of cloud inventory and dependencies](fnd04-bp02.md) 
+  [FND03-BP02 Establish central, cross-account observability capabilities](fnd03-bp02.md) 
+  [REL01-BP03 Accommodate fixed service quotas and constraints through architecture](rel01-bp03.md) 
+  [REL01-BP04 Monitor and manage quotas](rel01-bp04.md) 

 **Related documents:** 
+  [AWS Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) 
+  [Quota request templates in AWS Organizations](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) 
+  [AWS service quotas and endpoints](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [Monitor service quotas in Amazon CloudWatch](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html) 

 **Related examples:** 
+  [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/quota-monitor/) 
+  [Automate Service Quotas increase requests using AWS Organizations](https://docs.aws.amazon.com/solutions/automating-service-quota-management-on-aws/) 

 **Related services:** 
+  [AWS Service Quotas](https://docs.aws.amazon.com/solutions/automating-service-quota-management-on-aws/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 