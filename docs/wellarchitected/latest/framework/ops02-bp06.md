

# OPS02-BP06 Augment observability with AI assistants

 AI assistants now work at every stage of observability: they can instrument an application, write the queries, build the dashboards, recommend the objectives and alarms, and investigate what those alarms catch. Use them where they work the best. For example, an assistant analyzes large volumes of telemetry and correlates information across signals faster than a human can. 

 **Desired outcome:** 
+  You use AI assistance across the lifecycle, from instrumenting your workload to investigating its incidents, not only for troubleshooting. 
+  You treat everything an assistant produces as a proposal, reviewing, testing, or checking it against a baseline before it ships or drives a decision. 
+  You validate insights with the people who own the outcome, so action follows shared understanding rather than an unexamined finding. 
+  Your assistants reach telemetry through governed access, with the least privilege their task needs. 
+  You give every decision an assistant informs a named human owner. 

 **Common anti-patterns:** 
+  AI is used only when something is broken, leaving the effort of instrumenting, querying, and alarm design entirely manual. 
+  Machine findings are acted on without validation, so a plausible but wrong hypothesis drives the response. 
+  Generated instrumentation or configuration ships without review, so the team cannot explain what the workload now emits or why. 
+  Insights are never reviewed with business owners, so analysis measures the wrong dimension and effort goes to what does not matter. 
+  Agents across the organization query telemetry with broad, unaudited permissions. 
+  The team stops reading its own telemetry, and its understanding of the workload decays into whatever the assistant says. 

 **Benefits of establishing this best practice:** 
+  Time to value decreases, and the workload becomes observable and informs queries sooner. 
+  Mean time to resolution (MTTR) drops, and responders begin from a root cause hypothesis instead of from raw telemetry. 
+  Analysis stops being bounded by human reading time, which expands coverage. 
+  Validated findings produce fewer wrong turns during incidents and fewer wasted improvements between them. 
+  Common understanding with business owners keeps effort pointed at business outcomes. 
+  Assistant access to telemetry is auditable instead of accumulating over time. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md), [OPS02-BP04 Regularly analyze workload logs](ops02-bp04.md), and [OPS02-BP05 Regularly analyze workload traces](ops02-bp05.md) already use assistants to read telemetry at scale. This practice extends the same help to earlier stages: an assistant that reads telemetry can also help create it. Use an assistant where volume, correlation, or tedium exceeds what a person can do well. Assistance also has [costs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/investigations-costs.html), so explore what a feature costs before you scale its use. 

 For instrumentation, agentic development tools such as [Kiro](https://kiro.dev) write and review instrumentation code. The [Application Signals MCP server](https://github.com/awslabs/mcp/tree/main/src/cloudwatch-applicationsignals-mcp-server) provides an enablement guide an agent can follow to instrument a service, modifying the infrastructure and dependency files [OPS01-BP01 Develop application telemetry](ops01-bp01.md) prescribes. For workloads instrumented with OpenTelemetry, the [CloudWatch Omni skills](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-use-omni-skills.html) from the Agent Toolkit for AWS let your coding agent set up CloudWatch Omni instrumentation and query the resulting telemetry. Review generated instrumentation as you review any other code change. 

 The middle stages accept plain language. You can [generate and update Logs Insights queries from natural language](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Assist.html), which lowers the cost of asking one more question. You can also [summarize query results](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html) instead of reading them. Dashboards are tedious to build manually. An agent drafts them from a description of the audience and its questions, producing dashboards as code as detailed in [OPS02-BP02 Create actionable insights with dashboards](ops02-bp02.md), which are reviewable before they ships. 

 For workloads instrumented with OpenTelemetry, the [Omni agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-ask-the-omni-agent.html) built into CloudWatch Omni writes the query from your question, in SQL for logs and traces or PromQL for metrics, correlates across provided signals, and builds views and dashboards on demand. 

 Start objectives and alarms from recommendations. Use [SLO recommendations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) for the services Application Signals discovers and [alarm recommendations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html) for the AWS services beneath the workload, so coverage begins from a reviewed baseline. Set SLO targets with the business owner. 

 For troubleshooting, the analysis practices above cover the tools: CloudWatch investigations correlates telemetry and provides a hypothesis of the probable cause, AWS DevOps Agent investigates autonomously, and [MCP servers](https://github.com/awslabs/mcp) let agents anywhere query telemetry on request. In CloudWatch Omni, once the space is connected to AWS DevOps Agent, the Omni agent [delegates root cause questions to it](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-investigate-with-the-aws-devops-agent.html), and an alert offers an investigation you can choose to begin. This practice adds an access pattern where an MCP server defines what an agent can do and where. A fleet of agents queries telemetry through declared, auditable interfaces, and individual agents don't hold broad credentials. Grant those interfaces the least privilege their task needs, and know [what data an assistant reads](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/data-usage-considerations.html) when it investigates. Govern what's in the telemetry too. [Mask sensitive data in logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) at ingestion so no reader, human or machine, sees the raw values. 

 Whatever the stage, treat the output of an assistant or agent as a proposal. Validate machine findings against your baselines and service level objectives first, then with business owners and subject matter experts. They supply context that your telemetry lacks, can evaluate impacts that aren't found by your assistant, and confirm the course of action. Skipping validation can lead to failures such as measuring the wrong dimension and wasting an investigation or paying for a fix the business didn't need. A named person should own each decision that is informed by an assistant. 

 This practice is specific to AI-assisted observability. Observing AI agents themselves, such as their runs, model calls, and tool invocations, is distributed tracing, which is discussed in [OPS01-BP04 Develop distributed tracing](ops01-bp04.md). [CloudWatch Omni](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-omni.html) instruments and evaluates agents where you build them, and the [Observability and monitoring for agentic systems](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05.html) capability in the Agentic AI Lens covers agent observability in depth. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Let assistants help build the telemetry:** Use an agentic development tool such as [Kiro](https://kiro.dev) to write instrumentation, and the [Application Signals MCP server's enablement guide](https://github.com/awslabs/mcp/tree/main/src/cloudwatch-applicationsignals-mcp-server) to let an agent enable Application Signals for a service. Review generated instrumentation as code before it ships. 

1.  **Ask in plain language, and let agents build the views:** Use natural language to [generate and update Logs Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Assist.html) and [Metrics Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-query-assist.html), and [summarize query results](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html) instead of reading them. Have an agent draft the dashboards from a description of the audience and its questions, landing them as the dashboards-as-code [OPS02-BP02 Create actionable insights with dashboards](ops02-bp02.md) prescribes. Where the workload is instrumented with OpenTelemetry and monitored in CloudWatch Omni, [ask the Omni agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-ask-the-omni-agent.html), as it writes the SQL for your logs and traces or the PromQL for your metrics, and builds [views and dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-dashboards.html) on demand. Examine the generated query or view and confirm that it measures the dimension you asked about. 

1.  **Start objectives and alarms from recommendations:** Accept [SLO recommendations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) and [alarm recommendations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html) as the reviewed baseline, then set each target deliberately. Alerting strategy itself is the practice of [OPS06-BP01 Create actionable alerts](ops06-bp01.md). 

1.  **Delegate the first pass of troubleshooting:** Wire assistants into analysis and response as those practices already describe, investigations and AWS DevOps Agent per [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md), [OPS02-BP04 Regularly analyze workload logs](ops02-bp04.md), and [OPS02-BP05 Regularly analyze workload traces](ops02-bp05.md), and the composed alarm-to-ticket-to-investigation path per [OPS06-BP01 Create actionable alerts](ops06-bp01.md). In CloudWatch Omni, once the space is [connected to AWS DevOps Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-investigate-with-the-aws-devops-agent.html), you start an investigation yourself from an alert, and it begins seeded with the alert's context. 

1.  **Govern how agents reach telemetry, and what it contains:** Give agents access through [MCP servers](https://github.com/awslabs/mcp) rather than direct credentials, so what an agent can query is declared and auditable. Grant each interface the least privilege its task needs, review [what data investigations read](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/data-usage-considerations.html), and apply the [security posture the investigation service documents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html). [Mask sensitive log data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) at ingestion so sensitive data is not visible to any reader, human or machine. The [Agentic AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops04.html) covers tool integration for agents in depth. 

1.  **Validate before you act:** Check machine findings against your baselines and service level objectives, then review them with business owners and subject matter experts before they drive action: establish common understanding, identify impacts the assistant cannot see, and agree the course. Route what survives validation into the same owned actions your reviews already produce, as described in [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md). 

1.  **Keep the humans sharp:** Assign a named owner to every decision an assistant informs, and keep the team reading its own telemetry on the cadence the analysis practices define, so the assistant augments judgment that still exists. If a review would reach no decision without the assistant's narrative, treat that as a finding about the team. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS02-BP03 Regularly analyze workload metrics](ops02-bp03.md) 
+  [OPS02-BP04 Regularly analyze workload logs](ops02-bp04.md) 
+  [OPS02-BP05 Regularly analyze workload traces](ops02-bp05.md) 
+  [OPS01-BP01 Develop application telemetry](ops01-bp01.md) 
+  [OPS06-BP01 Create actionable alerts](ops06-bp01.md) 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 

 **Related documents:** 
+  [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) 
+  [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) 
+  [AWS MCP servers](https://github.com/awslabs/mcp) 
+  [Use natural language to generate and update CloudWatch Logs Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Assist.html) 
+  [SLO recommendations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) 
+  [Alarm recommendations for AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best-Practice-Alarms.html) 
+  [How CloudWatch investigations finds data for suggestions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/data-usage-considerations.html) 
+  [AWS Well-Architected Agentic AI Lens: Tool integration and management practices](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops04.html) 
+  [AWS Well-Architected Agentic AI Lens: Observability and monitoring for agentic systems](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05.html) 
+  [CloudWatch Omni](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-omni.html) 
+  [Ask the Omni agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-ask-the-omni-agent.html) 
+  [Use Omni skills from your coding agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-use-omni-skills.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Building agentic workflows for augmented observability (COP405)](https://www.youtube.com/watch?v=fLDjHr6eEIw) 
+  [AWS re:Invent 2025 - Accelerating incident response through AIOps (COP334)](https://www.youtube.com/watch?v=Ny4rrINHPe0) 

 **Related workshops:** 
+  [One Observability Workshop](https://catalog.workshops.aws/observability/en-US/intro) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 
+  [Kiro](https://kiro.dev) 