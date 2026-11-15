

# ADVOPS02-BP06 Implement distributed tracing for automated and agent-driven advertising operations
<a name="advops02-bp06"></a>

 As advertising operations increasingly use AI agents for bid optimization, creative selection, campaign management, and brand safety monitoring, implement distributed tracing to maintain visibility into multi-step automated workflows. Distributed tracing enables rapid root cause analysis when automated decisions produce unexpected outcomes and provides an audit trail for agent-driven actions across the advertising value chain. 

 **Desired outcome:** 
+  You have distributed tracing instrumented across every automated advertising workflow, including agent-driven decisions, from the triggering event through each decision step to the final action. 
+  Your agent execution traces are correlated with business outcomes (campaign performance, bid outcomes, brand safety assessments), so operations teams can identify when automated decision changes affect business results. 
+  Your trace data supports both real-time incident response and long-term optimization of agent configurations through automated analysis pipelines that identify anomalous patterns. 

 **Common anti-patterns:** 
+  Deploying advertising agents without capturing reasoning chains, leaving automated decisions opaque. 
+  Sampling traces uniformly across successful and failed invocations, diluting signal on error paths. 
+  Storing only agent outputs without the tools invoked, iteration counts, or knowledge base queries that led to them. 
+  Relying on ephemeral trace responses from AI agent services without explicit capture and persistence logic. 
+  Treating agent traces as infrastructure telemetry only and not correlating them with campaign performance or bid outcomes. 
+  Skipping trace context propagation across agent-to-agent boundaries, losing visibility when multi-agent workflows cross organizational lines. 

 **Benefits of establishing this best practice:** 
+  Rapid root cause analysis when automated advertising workflows produce unexpected outcomes. 
+  Identify inefficient patterns such as excessive iterations, redundant tool calls, or low-relevance knowledge base retrievals. 
+  Correlation of agent behavior with business outcomes. 
+  Data-driven optimization of agent configurations and model assignments. 
+  Reduced mean time to resolution for incidents involving automated decision-making. 
+  Audit trail for agent decisions supports compliance and governance requirements for automated advertising operations. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Automated advertising workflows often span multiple services and decision points. For example, a media planning agent calls audience segmentation tools, inventory availability APIs, and pricing optimization functions before producing a campaign recommendation. Implement distributed tracing that captures each workflow from the triggering event through each decision step to the final action. Choose sampling strategies that balance observability against high-throughput advertising traffic: higher sampling for error paths, lower for successful invocations. 

 An agent trace must record why the model reached each judgment. Include what it considered, which tools it consulted, how many attempts it took, and what it retrieved. Standard service metrics like latency and error rates do not capture this reasoning. 

 Capture agent reasoning during the request. The reasoning record exists only while the response is open, and unlike infrastructure telemetry, no service retains it and no API returns it retroactively. Agent decisions also have commercial consequences. When an agent allocates budget or activates a campaign, an advertiser can question the result or an auditor can require documentation. 

 Correlate agent traces with business outcomes. An agent can meet every service metric while producing recommendations that lose money, and only comparing the reasoning record to the outcome reveals this. Iteration counts and retrieval quality are leading indicators, and rising attempt counts signal a degrading workflow. 

 Multi-agent workflows break trace continuity at their boundaries. Context propagates within a system by convention, and those conventions stop at each team's edge. When a workflow crosses into another agent or organization, the trace fragments unless you design the boundary to carry it. That fragmentation may go undiscovered for a long time. Sampling compounds the problem: a per-service sampling strategy can drop the surviving half of a cross-boundary trace, leaving an incomplete record. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Instrument workflow trace propagation:** Add trace-context propagation across every service boundary using the AWS X-Ray SDK or OpenTelemetry, with consistent trace and span identifiers so a single workflow can be followed from trigger through all downstream services. For Ad Context Protocol (AdCP, which uses MCP transport) and IAB Tech Lab Agentic RTB Framework (ARTF) inter-agent messages, carry the trace\_id as a metadata field so visibility survives when a workflow crosses organizational lines. 

1.  **Enable agent tracing and persist trace artifacts:** The mechanism depends on the runtime. For new builds on [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), observability is push-based OpenTelemetry: instrument with the ADOT SDK, enable CloudWatch Transaction Search once per account, and read OTEL spans from the aws/spans log group. There is no trace flag on the invoke call, and InvokeAgentRuntime propagates W3C traceparent headers. For existing classic Bedrock Agents (in maintenance mode and closed to new customers as of July 2026), set enableTrace at invocation time, capture TracePart objects from the InvokeAgent streaming response, buffer them per session, and write the complete trace to Amazon S3 when the stream closes. Don't rely on the ephemeral response buffer as a source of truth. 

1.  **Define trace sampling strategies appropriate for your traffic volume:** Use 100 percent sampling for error paths (all failed invocations) and 1–10 percent for successful invocations, configured per service so high-throughput services don't dominate trace storage while error paths retain full fidelity. 

1.  **Capture agent decision metadata as trace annotations:** Record model used, reasoning rationale, tools invoked, iteration count, knowledge base queries, and tokens consumed. For classic Bedrock Agents the response carries TracePart objects covering PreProcessingTrace (input validation), OrchestrationTrace (reasoning chain, action-group invocations, knowledge base lookups with relevance scores), PostProcessingTrace (response formatting), GuardrailTrace (guardrail assessments), and FailureTrace (failure reasons), plus routingClassifierTrace for multi-agent supervisor routing. Read token counts from ModelInvocationOutput.metadata.usage for per-action cost attribution. Annotations convert traces from infrastructure diagnostics into business-level decision audits. 

1.  **Build automated trace analysis pipelines:** Parse stored traces (AWS Lambda or AWS Glue) to detect high iteration counts (reasoning loops), low-relevance knowledge base results, repeated tool-call failures, and sudden token-consumption changes. Publish detection signals as Amazon CloudWatch custom metrics with agent-specific dimensions. 

1.  **Monitor guardrail intervention rates:** Track GuardrailTrace events in persisted traces and the ratio of blocked compared to allowed actions per policy. Alarm when intervention rates exceed baselines (a spike during a new creative campaign may indicate policy calibration is needed, and zero interventions may indicate misconfiguration), and include guardrail intervention metrics in the weekly yield review. 

1.  **Build correlated dashboards:** Create [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) dashboards that display agent decision-quality metrics alongside business-outcome metrics (campaign plans generated, brand-safety assessments completed, bid optimization recommendations delivered), so operators connect agent behavior changes to business results without leaving the operational view. 

1.  **Set up alarms for anomalous agent behavior:** Configure CloudWatch alarms for elevated error rates, unusual tool-invocation sequences, iteration-ceiling hits, and sudden per-invocation token-consumption changes, early signals that catch silent regressions (for example, a knowledge base update that increases tokens per answer) before they reach business outcomes. 

1.  **Conduct quarterly trace reviews:** Review agent traces with operations and ML engineering to find optimization opportunities (agents that can be simplified, tool calls that can be cached, reasoning patterns that can be streamlined) and track improvements over time. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS02-BP02 Collect and analyze detailed metrics for successful operations and ad campaigns](advops02-bp02.md) 
+  [ADVOPS02-BP04 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics](advops02-bp04.md) 

 **Related documents:** 
+  [Guidance for Advertising Agents on AWS](https://aws.amazon.com/solutions/guidance/advertising-agents-on-aws/) 
+  [Amazon Bedrock agent tracing](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html) 
+  [Ad Context Protocol (AdCP) documentation](https://docs.adcontextprotocol.org/docs/intro) 
+  [IAB Tech Lab Agentic RTB Framework (ARTF) specification](https://iabtechlab.com/agentic-rtb-framework-specification-v1-0/) 
+  [Best practices for building robust generative AI applications with Amazon Bedrock Agents, Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/) 

 **Related services:** 
+  [AWS X-Ray](https://aws.amazon.com/xray/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 