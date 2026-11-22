

# FND03-BP01 Define observability standards and policies

 Clear observability standards and policies keep operational visibility and control across your cloud environment. This best practice focuses on defining and enforcing consistent observability requirements across both foundation components and workloads so telemetry is complete and meaningful. Teams keep flexibility in choosing monitoring tools and instrumentation libraries, and organizational standards keep telemetry consistent and available for operations. 

 **Desired outcome:** 
+  Your organization defines and enforces observability standards and policies so foundation components and workloads are instrumented consistently. 
+  Your observability approach lines up with business and operational requirements. 
+  Your observability foundation produces consistent, correlated telemetry that supports operations across the environment. 

 **Common anti-patterns:** 
+  Leaving observability to individual teams without formal standards, which produces inconsistent telemetry across the organization. 
+  Monitoring workloads while neglecting foundation components such as networking, identity, and security. 
+  Failing to assign clear ownership for telemetry quality, completeness, and availability. 
+  Leaving out documented requirements for instrumentation, data retention, or alerting. 
+  Treating observability as a deployment afterthought rather than a provisioning requirement enforced through automation. 

 **Benefits of establishing this best practice:** 
+  Foundation and workload telemetry is captured in predictable formats and locations across the organization. 
+  Foundation teams and workload owners have documented responsibilities for the telemetry they produce and consume. 
+  Required baseline telemetry helps prevent missing, incomplete, or unstructured data from going undetected. 
+  Observability practices are tied to operational and business goals rather than built in isolation. 
+  New accounts and workloads inherit observability settings automatically, which reduces manual setup. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Observability standards define the minimum telemetry that must be produced, the formats and naming conventions that enable correlation, and the ownership model. Without these standards, organizations end up with inconsistent logging formats, missing traces, and metrics that cannot be correlated across services. These inconsistencies become apparent during incident response, when investigators must reconstruct a timeline from incompatible data sources. 

 The standards must cover both foundation components and workloads because each has different ownership and lifecycle characteristics. Foundation components such as networking infrastructure, identity services, and central security controls are usually managed by foundation engineering or SRE teams. They change less often than applications, and must emit logs and metrics that give visibility into the foundational services all workloads depend on. Workloads are owned by product teams, deploy more often, and need instrumentation that captures application-specific behavior and business metrics. Standards must set baseline requirements for both categories and account for their different ownership models and change velocities. 

 Set retention for each telemetry type based on operational needs, as well as trade-offs between cost, regulations, and operational value. Troubleshooting recent incidents might need days or weeks of detailed data, whereas capacity planning might need months or years of aggregated metrics. Audit logs might have a minimum retention period set by compliance requirements. 

 Consider enforcement through automation, such as embedding standards into provisioning and deployment, which shifts enforcement from periodic manual audits to continuous automated checks. Account vending pipelines automatically configure central logging, and CI/CD pipelines verify required instrumentation. [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/), [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), and [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) together keep configuration in compliance. 

 Documentation, reference implementations, and training help workload teams understand and meet observability requirements. Update standards as operational maturity grows and new capabilities become available. Regular reviews with both foundation teams and workload owners identify coverage gaps, reduce unnecessary instrumentation burden, and keep standards current. Aim for steady improvement in telemetry coverage and quality over time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define observability standards:** Document baseline requirements for telemetry (logs, metrics, and traces) across the foundation and workloads. Define required metrics, log types, trace coverage, and data retention requirements. Use [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/) as a reference. 

1.  **Establish telemetry ownership:** Assign responsibilities for foundation-level telemetry to foundation engineering or [site reliability engineering (SRE)](https://aws.amazon.com/what-is/sre/) teams, and workload-specific telemetry to workload owners. Create a [RACI matrix](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix) to clarify responsibilities. 

1.  **Standardize telemetry formats and naming:** Define conventions for log structure, metric namespaces, dimensions, trace metadata, and tagging. Consider [OpenTelemetry](https://opentelemetry.io/) as your standard instrumentation framework so telemetry is collected and processed consistently across languages and runtimes. Amazon CloudWatch supports [native OpenTelemetry (OTel) signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html) over the OpenTelemetry Protocol (OTLP), and you can combine custom OpenTelemetry metrics with AWS vended metrics and query them using PromQL. For environments that need extra collection and processing, use the [OpenTelemetry Collector with CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPSimplesetup.html) as a central pipeline. 

1.  **Create observability policies:** Turn the standards into enforceable policies that cover both workloads and foundation components, with each policy specifying required telemetry types, formats, and destinations. Define minimum logging standards for all workloads, including required log types (application logs, access logs, and error logs), structured formats, and central destinations. Require foundation components (networking, identity, security, and infrastructure services) to send logs and metrics to the same locations. 

1.  **Define data retention policies based on operational and compliance needs:** Set retention periods for each telemetry type that balance troubleshooting value, compliance obligations, and storage cost. Document lifecycle policies that move data to lower-cost storage tiers or delete it after its retention period. Apply these using [Amazon CloudWatch Logs retention settings](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention), [Amazon S3 lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html), and equivalent retention settings for your chosen observability backends. 

1.  **Enforce standards through automation:** Shift observability enforcement from manual reviews to automated checks embedded in provisioning and deployment pipelines so telemetry gaps are caught before they reach production. Use [infrastructure as code (IaC)](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) to embed standards in account provisioning, CI/CD pipelines, and deployment tooling. Detect missing telemetry and enforce baseline configurations using [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/), [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) where applicable, and [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html), and add observability instrumentation during resource provisioning through CI/CD controls and IaC. 

1.  **Promote adoption and continuous improvement:** Treat observability standards as a living contract that evolves with the foundation, with feedback loops that surface gaps and reduce unnecessary instrumentation burden. Communicate standards through training, documentation, and onboarding guides, and review and update policies regularly as the foundation and business requirements evolve. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND03-BP02 Establish central, cross-account observability capabilities](fnd03-bp02.md) 
+  [FND03-BP03 Establish centralized event monitoring and response](fnd03-bp03.md) 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 
+  [OPS01-BP04 Develop distributed tracing](ops01-bp04.md) 

 **Related documents:** 
+  [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/) 
+  [Amazon CloudWatch native OpenTelemetry support](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html) 
+  [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/) 
+  [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) 
+  [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) 
+  [Infrastructure as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) 
+  [Operational Readiness Reviews (ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) 