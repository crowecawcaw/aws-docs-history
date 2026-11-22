

# OPS01-BP03 Develop dependency telemetry

 Every workload depends on components beyond your own code: other services of the workload, internal APIs, shared internal platforms, databases, third-party APIs, DNS, network paths, and managed cloud services. Dependency telemetry measures the health and performance of those components so you can attribute a problem to the right one, inside or outside your architecture. Without it, a failing dependency looks like a defect in whichever service alarmed first, cascading failures arrive as surprises, and you cannot predict what a change will affect. 

 **Desired outcome:** 
+  You know the health, latency, and error rates of every dependency your workload relies on, internal and external. 
+  You can distinguish a problem in your own code from a problem in a dependency, which shortens diagnosis. 
+  You receive advance notice of dependency events, such as planned maintenance or service disruptions, and act before they affect users. 
+  You see dependency health alongside your internal telemetry, giving one view of everything that affects the workload. 
+  You know which services depend on each other, so you can anticipate how a failure propagates and what a change will affect. 

 **Common anti-patterns:** 
+  Teams monitor internal metrics only and ignore the external services the workload calls. 
+  Organizations wait for a dependency to fail rather than continually tracking its health. 
+  Dependency data is spread across separate tools, producing inconsistent views of the same problem. 
+  Teams do not track the performance limits of a dependency, so they are surprised when it throttles under load. 
+  Teams document external dependencies but leave the interdependencies among their own services as tribal knowledge, so cascading failures and change impact come as surprises. 

 **Benefits of establishing this best practice:** 
+  Failures in external services are detected quickly and attributed correctly. 
+  Diagnosis is faster because operators can immediately confirm or exclude a dependency as the cause. 
+  Advance notice of provider events allows planned mitigation instead of a reactive response. 
+  Understanding dependency limits informs capacity and resilience decisions. 
+  Cascading failures are caught while they form, because telemetry on internal dependency edges shows latency and errors propagating between services. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Start by discovering what your workload depends on. Trace data reveals the services your workload calls. Where the workload is not yet instrumented for tracing, the network layer provides the same evidence: flow logs record which endpoints your compute communicates with, and DNS query logs show which names it resolves. Not all dependencies carry equal weight. A hard dependency, one your workload cannot function without, deserves closer monitoring than a soft dependency you can degrade around. Classify dependencies before you instrument, so your effort matches criticality. 

 Internal dependencies deserve the same rigor as external ones. The edges between your own services are where cascading failures form: one slow component causes timeouts upstream, retries amplify the load, and queues back up until an isolated slowdown becomes a workload-wide incident. Instrument these edges, recording timeouts, retry counts, and queue depths alongside latency and errors, so you can catch a cascade as it forms. Knowing what depends on a component tells you the blast radius of a change or a failure before you commit it. A fallback around a soft dependency only counts if telemetry confirms it engaged. Where different teams own different services, internal service level objectives serve the role that provider service level agreements serve for external dependencies. When two of your services depend on the same underlying resource, they fail together, and the graph makes this visible before an incident does. 

 For each dependency, set measurable health targets (such as acceptable latency, error rate, and availability), often expressed as a service-level objective (SLO) against the provider's service-level agreement (SLA). These targets provide a threshold for each alert and a shared reference to operators during an incident. 

 Dependency problems can sometimes look like defects in your own workload, despite the fact that they may happen elsewhere. You cannot instrument a third party's systems, so infer health from the client side: the latency, timeouts, and error responses your workload observes. Supplement this with the provider's own status and health signals. 

 Enable [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) to discover the dependencies your services call from trace data. It shows them on a map with the health of each edge, so your inventory starts from observed behavior. These traces come from [OPS01-BP04 Develop distributed tracing](ops01-bp04.md). [Amazon CloudWatch network monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Network-Monitoring-Sections.html) reports on the internet and network paths between your workload and what it depends on. [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) reports the current state of the AWS services you use and gives advance notice of planned changes. [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) traces show where in a request a dependency call slows down or fails. For database dependencies, [Amazon CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) correlates database load with the queries and calling services behind it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify dependencies:** Work with stakeholders to list the services your workload relies on, internal and external, including databases, third-party APIs, network routes to other environments, and DNS. Being comprehensive here is what makes the rest of the work effective. Start from what the workload already shows: with Application Signals enabled, the service map lists the internal and external dependencies your services actually call ([OPS01-BP04 Develop distributed tracing](ops01-bp04.md)). Where tracing is not yet in place, discover from the network layer instead: [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) record which endpoints your compute communicates with, and [Route 53 Resolver query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html) shows which names it resolves. Review the discovered inventory with stakeholders to add what telemetry cannot see, such as batch transfers or dependencies exercised only rarely. 

1.  **Define healthy and build a monitoring strategy:** For each dependency, internal or external, record its criticality, expected behavior, and any SLA or SLO. Set proactive alerts that fire on status changes or performance deviations against those targets. Define [service level objectives in Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) on the latency and availability of the services you depend on, with burn-rate alarms as the proactive signal, and set [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) on the dependency metrics your workload observes from the client side, such as timeouts and error rates. 

1.  **Monitor network paths:** Use [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) and [Network Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html) to observe global internet and network conditions. These tools help you understand and respond to degradations that affect external dependencies. [Amazon CloudWatch Network Flow Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-What-is-NetworkFlowMonitor.html) measures packet loss and latency for the network flows between your compute and its dependencies using lightweight agents, and [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) record the traffic itself for after-the-fact analysis. On Amazon EKS, [Container Network Observability](https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html) uses Network Flow Monitor to map traffic between communicating pods and from pods to AWS services and external destinations, with retransmissions and data transferred per flow. 

1.  **Track AWS service health:** Use AWS Health to see current service events and upcoming changes for the AWS services you depend on. Create [purpose-fit Health event notifications](https://docs.aws.amazon.com/health/latest/ug/) through [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html), integrate programmatically with [Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) or the [AWS Health API](https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html), and enable [organizational view](https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html) to aggregate events across accounts. 

1.  **Trace dependency calls:** Instrument the workload with [Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html), the [AWS Distro for OpenTelemetry (ADOT) SDKs](https://aws-otel.github.io/), or any of the OpenTelemetry SDKs, sending traces to [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html), so traces show where a dependency call adds latency or returns errors. This locates the failing hop inside a request rather than leaving you to guess. 

1.  **Detect emerging issues:** Use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) to investigate operational issues autonomously and surface degrading dependencies with their likely cause, so problems are flagged and worked before they become incidents. When an alarm from your monitoring strategy fires, start a [CloudWatch investigation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) to scan the related telemetry and suggest a root cause, including whether a dependency sits behind the symptom. 

1.  **Validate after changes:** Whenever a dependency changes, confirm its performance still meets your workload's requirements, applying the testing discipline of [OPS03-BP02 Test and validate any and all changes](ops03-bp02.md) to dependency changes you consume as well as changes you make. Revisit your monitoring strategy as priorities and dependencies evolve. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS01-BP01 Develop application telemetry](ops01-bp01.md) 
+  [OPS01-BP04 Develop distributed tracing](ops01-bp04.md) 
+  [OPS01-BP02 Develop user experience telemetry](ops01-bp02.md) 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 
+  [OPS03-BP02 Test and validate any and all changes](ops03-bp02.md) 

 **Related documents:** 
+  [AWS Health User Guide](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) 
+  [Amazon CloudWatch Internet Monitor User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) 
+  [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) 
+  [Amazon CloudWatch Network Flow Monitor User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-What-is-NetworkFlowMonitor.html) 
+  [Monitor Kubernetes workload traffic with Container Network Observability](https://docs.aws.amazon.com/eks/latest/userguide/network-observability.html) 
+  [Amazon CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) 
+  [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) 
+  [Service level objectives in Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) 
+  [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) 
+  [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/) 
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) 
+  [Route 53 Resolver query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Comprehensive observability with Mobile RUM and Application Map (COP364)](https://www.youtube.com/watch?v=z1qnPTUZZ9M) 
+  [Diving Deep on AWS DevOps Agent - AWS Tech Tales](https://www.youtube.com/watch?v=uFgGARWSCWk) 

 **Related examples:** 
+  [AWS Health Aware](https://github.com/aws-samples/aws-health-aware/) 
+  [Application Signals demo application](https://github.com/aws-observability/application-signals-demo) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 
+  [AWS Health](https://aws.amazon.com/premiumsupport/technology/aws-health/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 