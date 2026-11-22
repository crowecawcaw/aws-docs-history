

# PERF05-BP04 Keep your workload and services up-to-date

 Cloud providers regularly release new services, instance types, and features, and many can deliver better price-performance for what you already run. Review new releases and adopt the ones that benefit your workload. 

 **Desired outcome:** 
+  You have a defined process and owner for inventorying components and evaluating new services, features, and updates. 
+  You monitor provider announcements and account-specific lifecycle events relevant to your workload. 
+  Your documented triage rules or agents classify events and escalate only the ones that require an owner's attention. 
+  You validate candidate updates with performance tests before adopting them. 
+  You prioritize updates by their measured impact on business KPIs. 
+  You adopt beneficial changes through a documented, repeatable approach instead of ad hoc effort. 

 **Common anti-patterns:** 
+  Teams treat the current architecture as static and assume it will not change over time. 
+  Teams have no cadence to check whether updated software and packages remain compatible with the workload. 
+  Teams do not track announcements, planned lifecycle events, or service changes relevant to their workload. 
+  Teams send every provider notification to people or agents without actionability, deadline, workload-tier, environment, affected-resource, ownership, or deduplication criteria. 
+  Teams rely on a periodic planning dashboard as the real-time notification path for urgent events. 
+  Teams let an agent turn a discovered event directly into an update without owner validation and performance testing. 
+  Teams postpone optimization until a problem forces a change. 
+  Teams bundle runtime version upgrades with unrelated dependency changes, so every adopter needs a dedicated migration. 

 **Benefits of establishing this best practice:** 
+  You capture performance and efficiency gains from new capabilities soon after they are released. 
+  You resolve known issues by adopting fixes and improved features. 
+  You reduce notification noise while escalating actionable lifecycle events to the right owner. 
+  You avoid architectural stagnation by revisiting choices as the environment evolves. 
+  You reduce update risk by validating changes against KPIs before production. 
+  You make adoption predictable through a repeatable, documented process. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 AWS regularly releases new instance families, managed services, and features. Some of these releases can improve throughput, latency, or price-performance, or let you remove a workaround in your current design. Review new releases periodically, assess which apply to your workload, and adopt those worth the effort. 

 Assign an owner, choose the sources to monitor, schedule time to evaluate incoming events, and define how to escalate the ones that need action. 

 Adopting an update without checking compatibility risks a regression. A gain in one metric doesn't imply a gain in another, so compare current and candidate configurations against the same KPIs. 

 Automating image builds, patching, artifact creation, and deployment cuts both effort and variation in each update. Prioritize by business KPIs: adopt changes that improve the metrics the workload is measured on, and keep the current design when evidence shows no benefit. 

 When you roll a new runtime or platform version out across many components, change only that version and keep unrelated dependency and build changes separate. Release the version first as an opt-in default, so ordinary builds and deployments reveal compatibility problems early. Resolve the reported incompatibilities, then make it the default so components upgrade on their normal release cycle. This approach takes time and means maintaining compatibility shims during the transition. Making it the default before problems are resolved can break many consumers' builds at once. 

 Triage every provider notification before deciding whether to adopt the change. Classify events by criteria such as action required, deadline, affected resources and workload tier, environment, ownership, duplication, and maintenance state. An agent can add workload context and decide, following documented policy, whether an event reaches an owner. Apply rule-based filtering and structured queries first. Use generative AI for free-text descriptions and impact analysis. Verify AI-generated summaries and recommendations against the source event and workload data before approving an evaluation or adoption. 

 AWS publishes general changes through [What's New at AWS](https://aws.amazon.com/new/) and account-specific changes through [AWS Health planned lifecycle events](https://docs.aws.amazon.com/health/latest/ug/aws-health-planned-lifecycle-events.html). Use the [AWS Health Dashboard](https://health.console.aws.amazon.com/health) for account-specific review and [Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) or AWS Health notifications for time-sensitive routing. The [Cloud Intelligence Dashboards Health Events Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/health-events-dashboard.html) provides organization-wide historical and upcoming-event analysis for planning, but data lag makes it unsuitable for real-time notification. For conversational analysis, add the [Generative AI Assistant with CID and AWS Quick](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/generative-ai.html) or evaluate an MCP-based sample such as [Chaplin](https://github.com/aws-samples/sample-aws-health-agentic-assistant). Use these assistants for decision support, apply deterministic filters before LLM analysis, account for added service charges, and require human approval for update decisions. 

 [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) reports software and configuration inventory. [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) and [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) identify resources with configuration or generation worth evaluating. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Assign ownership and monitoring channels:** Name the owners responsible for tracking changes. Subscribe to the [What's New at AWS](https://aws.amazon.com/new/) feed for the products used by the workload and route account-specific [AWS Health events through Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) or AWS Health notifications. 

1.  **Inventory your workload:** Catalog the workload's software, architecture components, versions, owners, and business criticality. Use [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) to collect operating system, application, and instance metadata. 

1.  **Define review cadence and event triage:** Set a schedule for reviewing announcements and long-term lifecycle trends. Define real-time routing criteria for action-required events using deadline, affected resources, workload tier, environment, and owner. Use deterministic rules first. Use an agent to enrich ambiguous events and escalate according to policy, not to approve an update. 

1.  **Assess and test candidate updates:** Understand the compatibility and update path, build a proof of concept, and run performance tests comparing current and candidate configurations against the same KPIs. Adopt only the changes whose measured benefit justifies their migration risk and effort. 

1.  **Automate the update path:** Use [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) or CI/CD pipelines to rebuild AMIs, container images, and artifacts. Use [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) with [Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows.html) to schedule system updates. 

1.  **Document the process and prioritize by KPIs:** Record monitoring sources, triage and escalation rules, evaluation evidence, owners, adoption decisions, and rollback paths. Use business requirements and KPIs to prioritize updates. 

1.  **Review outcomes and improve the process:** Track missed lifecycle events, false escalations, overdue actions, agent or dashboard costs, and performance results after adoption. Adjust collection, triage, and evaluation rules using this evidence. 

1.  **Stage version rollouts:** For fleet-wide runtime or platform upgrades, release the new version as an opt-in default, resolve reported incompatibilities, then switch the default so components upgrade on their normal build or deployment cycle. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF05-BP02 Evaluate your workload performance](perf05-bp02.md) 
+  [PERF05-BP05 Review metrics at regular intervals](perf05-bp05.md) 
+  [PERF02-BP01 Select the best compute options for your workload](perf02-bp01.md) 
+  [PERF02-BP05 Use optimized hardware-based compute accelerators](perf02-bp05.md) 

 **Related documents:** 
+  [What's New with AWS](https://aws.amazon.com/new/?ref=wellarchitected) 
+  [Planned lifecycle events for AWS Health](https://docs.aws.amazon.com/health/latest/ug/aws-health-planned-lifecycle-events.html) 
+  [Monitoring events in AWS Health with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) 
+  [Cloud Intelligence Dashboards Health Events Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/health-events-dashboard.html) 
+  [Generative AI Assistant with CID and AWS Quick](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/generative-ai.html) 
+  [Build self-service AWS Health analytics with AI agents](https://aws.amazon.com/blogs/machine-learning/build-self-service-aws-health-analytics-to-find-actionable-health-insights-with-ai-agents-powered-by-amazon-bedrock/) 
+  [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) 
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) 
+  [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) 

 **Related videos:** 
+  [AWS Systems Manager Patching at Scale](https://aws.amazon.com/video/watch/5c64c6a2a17/) 
+  [Automate Patching with AWS Systems Manager](https://aws.amazon.com/video/watch/6d5ece9fe39/) 

 **Related examples:** 
+  [AWS Health Tools](https://github.com/aws/aws-health-tools) 
+  [Chaplin AWS Health Agentic Assistant](https://github.com/aws-samples/sample-aws-health-agentic-assistant) 

 **Related services:** 
+  [AWS Health Dashboard](https://health.aws.amazon.com/health/statush) 
+  [AWS Health](https://aws.amazon.com/premiumsupport/technology/aws-health/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [EC2 Image Builder](https://aws.amazon.com/image-builder/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 
+  [AWS Quick](https://aws.amazon.com/quick/) 