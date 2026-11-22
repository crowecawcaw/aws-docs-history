

# PERF05-BP03 Use automation to proactively remediate performance-related issues

 Configure automated investigation as the first line of incident response so analysis starts when an alert or ticket meets your incident criteria. While an engineer responds to the page, the investigation correlates telemetry and topology and returns a root cause or evidence-backed hypotheses. Deterministic automation then handles well-understood, low-risk remediation. Reserve human judgment for uncertain or high-impact actions. 

 **Desired outcome:** 
+  You start agent-assisted investigation only from alerts or tickets that meet your defined incident criteria. 
+  You link duplicate signals to active investigations, skip non-actionable events, and proceed with new incidents that require analysis. 
+  Your investigations correlate metrics, logs, traces, code changes, deployments, and service topology across the systems your team operates. 
+  You give the agent your current application design, critical user journeys, SLOs, ownership, known constraints, maintenance windows, and escalation context. 
+  Your findings and mitigation plans reach the ticketing and collaboration tools where your responders already work. 
+  You limit automated remediation to well-understood cases, keep it proportionate to the problem, and govern it with approval and rollback controls. 
+  Every automated action verifies that it resolved the issue before your workflow considers it complete. 
+  Your incident history produces proactive recommendations that reduce recurrence and improve your observability, infrastructure, governance, and code. 
+  Your reusable Skills and executable runbooks capture investigation procedures, operational practices, and remediation workflows, and you test them on a schedule. 

 **Common anti-patterns:** 
+  Teams route every alarm to the operations team without starting automated investigation or remediation. 
+  Teams route every alert to an agent without severity, user-impact, actionability, deduplication, maintenance-window, or skip criteria, producing irrelevant investigations and unnecessary agent-time charges. 
+  Teams deploy an incident agent without connecting service topology, application design, ownership, organizational context, code and deployment history, or the telemetry sources needed for cross-system correlation. 
+  Teams rely on ad hoc prompts and do not create reusable Skills for recurring investigation procedures, triage rules, tool usage, and operational practices. 
+  Teams leave ticketing and collaboration tools disconnected, forcing responders to copy investigation context by hand. 
+  Teams expose broad write-capable tools through custom integrations or MCP servers without least-privilege access, tool allowlisting, approval, and audit controls. 
+  Teams treat agent-generated hypotheses as confirmed root causes or execute mitigation plans without validation. 
+  Teams automate symptoms without addressing the underlying cause. 
+  Teams apply disruptive remediation to minor problems, such as replacing an instance for a small memory increase or failing over a database for a slow query. 
+  Teams trigger a fix in one component that creates a performance problem elsewhere, causing chain reactions. 
+  Teams remediate an issue without verifying that the action worked. 
+  Teams close incidents without reviewing history for recurring patterns and preventive improvements. 

 **Benefits of establishing this best practice:** 
+  You reduce mean time to recovery because investigation begins before the responding engineer completes manual context gathering. 
+  You control investigation volume and agent usage cost by separating alert signals from incidents that require analysis. 
+  Responders start with correlated evidence, affected dependencies, root-cause hypotheses, and mitigation options instead of an isolated alarm. 
+  You reduce user impact by acting on predictive signals for well-understood failure modes. 
+  You free operations staff to concentrate on complex issues that require judgment. 
+  You build institutional knowledge from playbooks, investigation history, and proactive recommendations. 
+  You keep automated responses proportionate and auditable, avoiding disruptive actions for minor issues. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Proactive remediation acts on a signal that predicts a problem before it occurs. A reactive automation that restarts an instance after latency has spiked still leaves users with a bad experience during the spike. A proactive workflow watches a leading indicator, such as a KPI trending toward its limit, and acts while headroom remains. Forecast-based signals require baselines and dashboards that define normal behavior before they identify a meaningful deviation. 

 Use an incident agent as the first investigation path for selected alerts and tickets. [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) starts an investigation from alarming or ticketing systems and uses a continuously updated application topology to trace dependencies. It correlates metrics, logs, traces, code changes, deployment history, and AWS Health events across the topology to identify root cause, assess blast radius, or return ranked hypotheses. 

 Define triage criteria using severity, customer impact, actionability, confidence, maintenance state, and whether an active investigation already covers the same symptom. AWS DevOps Agent triage links related events to an active investigation, skips events that match criteria defined in an [Incident Triage Skill](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-devops-agent-skills.html), or proceeds with a new investigation. Route critical and actionable signals automatically and sample or suppress low-value signals according to documented policy. Investigations are billed by agent-second, so indiscriminate routing adds cost, creates noise, and pollutes the incident history used for future recommendations. 

 Connect the agent to the systems that hold operational context. Native integrations include Amazon CloudWatch and third-party observability platforms, CI/CD and code repositories, ServiceNow, PagerDuty, and Slack. Webhooks and Amazon EventBridge connect additional incident workflows. [Custom MCP servers](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-integrations-and-knowledge-connecting-mcp-servers.html) expose proprietary telemetry, runbooks, and operational systems through structured tools. Limit investigation tools to read access, grant each Agent Space only the required tools and accounts, and record tool invocations in an audit trail. 

 Telemetry and topology don't contain all the context an investigation needs. Add workload purpose, critical user journeys, SLOs, service ownership, architecture decisions, known constraints, failure modes, maintenance windows, deployment practices, and escalation policy. Keep this context, topology, and integration credentials current. 

 Address the underlying cause. An automation that restarts a service each time memory climbs masks a leak while the defect remains. Keep the response proportionate. A database failover for a slow query, or an instance replacement for a small memory increase, causes more disruption than the original condition. 

 Bound each workflow with least-privilege permissions, idempotency, concurrency limits, cooldown periods, approval gates for high-impact actions, and an explicit rollback path. Verify success with a signal independent from the trigger. If memory pressure triggers a remediation, confirm customer-facing latency, error rate, and workload health. A lower memory reading alone doesn't prove recovery. Escalate to a person when a workflow cannot verify or safely revert its action. 

 [AWS DevOps Agent Skills](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-devops-agent-skills.html) encode recurring investigation procedures, triage and skip criteria, architectural standards, operational practices, organizational knowledge, and instructions for using native or MCP tools. Skills replace repeated one-off prompts and guide the agent's reasoning. Deterministic runbooks remain the executable layer for approved remediation. Keep agent-generated root-cause hypotheses and mitigation plans separate from execution until evidence and policy support the action. 

 [AWS DevOps Agent proactive incident prevention](https://docs.aws.amazon.com/devopsagent/latest/userguide/production-operations-proactive-incident-prevention.html) evaluates investigation history to identify recurring patterns and targeted improvements across observability, infrastructure, governance, and code. Review these recommendations on a schedule, assign owners, validate them against workload evidence, and track whether implemented changes reduce recurrence or detection and recovery time. 

 [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms initiate workflows, and [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) provides read-only AI-assisted telemetry analysis. AWS DevOps Agent performs topology-aware investigation and coordinates findings through integrated systems. [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) runs approved deterministic remediation runbooks. [Amazon CloudWatch Synthetics canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) and application health checks provide independent verification. [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) rehearses investigation and remediation with controlled failures in non-production environments. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Plan incident routing and triage:** Identify which alarm and ticket conditions represent an incident that requires investigation. Define severity, customer-impact, actionability, deduplication, maintenance-window, sampling, and skip criteria. Route critical and actionable signals automatically, link related events to active investigations, and suppress or sample low-value signals. 

1.  **Provide topology and operational context:** Configure the agent's AWS accounts, application topology, observability sources, code repositories, deployment pipelines, and AWS Health context. Add workload purpose, critical user journeys, SLOs, service ownership, architecture decisions, known constraints, maintenance windows, and escalation policy. Add only the integrations required for the workload. 

1.  **Create reusable Skills:** Encode recurring investigation procedures, Incident Triage skip rules, operational practices, organizational knowledge, and instructions for native and MCP tools in [AWS DevOps Agent Skills](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-devops-agent-skills.html). Version and review Skills when the workload, tools, ownership, or process changes. 

1.  **Identify and prioritize remediation candidates:** Use investigation history and performance telemetry to rank recurring issues by frequency, customer impact, confidence in the root cause, reversibility, and remediation blast radius. Automate the high-impact, well-understood, reversible cases first. 

1.  **Define remediation logic and controls:** Write a process that addresses the underlying cause and keeps the action proportionate. Define least-privilege permissions, idempotency, concurrency limits, cooldown periods, approval requirements, rollback criteria, and the conditions that require human escalation. 

1.  **Automate approved remediation:** Implement deterministic actions with [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html), Amazon EventBridge targets, or equivalent tooling. Keep agent-generated mitigation plans separate from execution until the plan satisfies approval and policy requirements. 

1.  **Verify the result independently:** Define customer-facing and workload-health success criteria. Use [Amazon CloudWatch Synthetics canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html), application health checks, and KPIs that are independent from the trigger. Roll back or escalate when verification fails. 

1.  **Test investigation and remediation:** Validate routing, triage, Skills, integrations, permissions, approvals, actions, verification, rollback, and escalation in a pre-production environment. Use [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to introduce controlled conditions and confirm that automation does not create a chain reaction. 

1.  **Document and train:** Record incident-routing policy, topology and context sources, investigation logic, Skills, automated runbooks, approval points, rollback, and escalation paths. Train responders to review evidence and take over when automation reaches its boundary. 

1.  **Review incident history and proactive recommendations:** Run periodic evaluations of resolved investigations. Prioritize recommendations that improve observability, capacity, deployment governance, code, and recurring failure modes. Assign owners and measure recurrence, detection time, and recovery time after implementation. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF05-BP01 Use monitoring solutions to understand the areas where performance is most critical](perf05-bp01.md) 
+  [PERF05-BP02 Evaluate your workload performance](perf05-bp02.md) 
+  [PERF05-BP05 Review metrics at regular intervals](perf05-bp05.md) 
+  [PERF01-BP04 Establish criteria for performance degradation alerts and tolerances](perf01-bp04.md) 
+  [PERF02-BP04 Scale your compute resources dynamically](perf02-bp04.md) 

 **Related documents:** 
+  [What is AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) 
+  [AWS DevOps Agent production operations](https://docs.aws.amazon.com/devopsagent/latest/userguide/working-with-devops-agent-production-operations-index.html) 
+  [Autonomous incident response](https://docs.aws.amazon.com/devopsagent/latest/userguide/production-operations-autonomous-incident-response.html) 
+  [AWS DevOps Agent Skills](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent-devops-agent-skills.html) 
+  [Integrating AWS DevOps Agent with Amazon EventBridge](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-integrations-and-knowledge-integrating-devops-agent-into-event-driven-applications-using-amazon-eventbridge-index.html) 
+  [AWS DevOps Agent pricing](https://aws.amazon.com/devops-agent/pricing/) 
+  [Configuring integrations and knowledge](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-integrations-and-knowledge.html) 
+  [Connecting to ticketing and chat](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-integrations-and-knowledge-connecting-to-ticketing-and-chat-index.html) 
+  [Connecting MCP servers](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-integrations-and-knowledge-connecting-mcp-servers.html) 
+  [Proactive incident prevention](https://docs.aws.amazon.com/devopsagent/latest/userguide/production-operations-proactive-incident-prevention.html) 
+  [Best practices for deploying AWS DevOps Agent in production](https://aws.amazon.com/blogs/devops/best-practices-for-deploying-aws-devops-agent-in-production/) 
+  [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) 
+  [CloudWatch alarm actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Move beyond reactive: Transform cloud ops with AWS DevOps Agent](https://www.youtube.com/watch?v=JajBEYle67I) 
+  [Diving Deep on AWS DevOps Agent](https://www.youtube.com/watch?v=uFgGARWSCWk) 
+  [Incident Investigation with AWS DevOps Agent](https://www.youtube.com/watch?v=PcbOQAtT13I) 
+  [AWS DevOps Agent as Your Expert Troubleshooting Peer \+ Best practices](https://www.youtube.com/watch?v=1VccSk8LDu0) 

 **Related examples:** 
+  [Automated incident lifecycle with AWS DevOps Agent](https://github.com/aws-samples/sample-automated-incident-lifecycle-with-aws-devops-agent) 
+  [EKS investigation with AWS DevOps Agent](https://github.com/aws-samples/sample-aws-genai-ops-demos/blob/main/observability/eks-investigation-devops-agent/README.md) 
+  [AWS DevOps Agent and Kiro closed-loop remediation with human review](https://github.com/aws-samples/sample-devops-kiro-integration/blob/main/README.md) 
+  [Trigger AWS DevOps Agent investigations from CloudWatch alarms](https://github.com/aws-samples/sample-aws-devops-agent-cloudwatch) 
+  [AWS DevOps Agent ACP and MCP reference implementation](https://github.com/aws-samples/sample-aws-devops-agent-acp-mcp) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 