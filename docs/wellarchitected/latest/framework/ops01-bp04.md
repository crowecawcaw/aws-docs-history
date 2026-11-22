

# OPS01-BP04 Develop distributed tracing

 Distributed tracing follows one request as it moves through the services that handle it. In a distributed system, multiple services handle each user action, so a slowdown or failure in any one of them affects the result. Tracing links each service's work into one end-to-end timeline, so you can see where time is spent or where the request fails. 

 **Desired outcome:** 
+  You can follow any request end to end across every service that handles it. 
+  You can locate the exact service and operation where latency or errors originate. 
+  Your trace data is connected across services through a shared context, not isolated per service. 
+  Your alerts fire from trace data when latency or error rates threaten the outcomes you defined. 

 **Common anti-patterns:** 
+  Only some services in the request path are instrumented, so traces break at the first uninstrumented service. 
+  Teams watch for errors but ignore gradual latency growth that degrades the experience over time. 
+  Trace context is not passed between services, leaving disconnected fragments instead of one request timeline. 
+  Tracing is added once and never revisited as new services join the request path. 

 **Benefits of establishing this best practice:** 
+  Root-cause analysis is faster because the slow or failing service is visible in the trace. 
+  Performance work targets the operations that actually consume time, not guesses. 
+  A complete request view reveals interactions between services that per-service metrics hide. 
+  Latency trends surface before they breach the targets that matter to users. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A trace records the path of one request. It consists of spans, where each span represents the work of one service or operation. A shared trace context travels with the request and links the spans across services. Metrics and logs describe one component at a time, while a trace connects them into one ordered account of that request. 

 If any service in the path does not pass the trace context, the trace breaks and everything downstream becomes disconnected from the original request. Every service in the request path must instrument consistently, or the holistic view has gaps where incidents happen. 

 Capturing every trace is expensive at scale, so most systems sample. Sampling keeps cost manageable but can discard the rare trace that explains an incident, so choose a strategy that retains failing and slow requests. Alternatively, [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html) ingests spans into Amazon CloudWatch Logs in OpenTelemetry format at a rate designed for full collection, so every transaction is searchable. 

 Degradation usually precedes failure: a service slows before it fails, so a slow but successful request is often an early warning. Gradual latency growth appears in traces, so you can act before users notice or errors appear. 

 [Amazon CloudWatch Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html) is the fastest route. Enable it on a supported runtime and it instruments services with the AWS Distro for OpenTelemetry (ADOT) SDKs automatically and propagates trace context without code changes. From the trace data, it builds an [application map](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceMap.html) and metrics for each service. Whichever OpenTelemetry SDK produces your spans, [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) receives, stores, and analyzes them, and instrumentation written against the open standard stays portable. The [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-OpenTelemetry-metrics.html) is the recommended collection path — an AWS-managed OpenTelemetry collector that accepts spans from any OpenTelemetry SDK over OTLP and forwards them to X-Ray. 

 The same model describes an AI agent. One agent run is a trace, each model invocation, tool call, or retrieval is a span, and a session groups the traces of a multi-turn conversation. For workloads instrumented with OpenTelemetry, [CloudWatch Omni](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-monitor-ai-agents.html) reads agent traces alongside application traces in one place, follows sessions, and derives the topology of the components an agent calls. For details on tracing agent reasoning, tool calls, and memory operations, see [AGENTOPS05-BP01 Establish end-to-end tracing and telemetry for agent operations](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05-bp01.html). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Instrument services and propagate trace context:** Instrument each service with [Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html) where the runtime is supported, with the [AWS Distro for OpenTelemetry (ADOT) SDKs](https://aws-otel.github.io/), or with any of the [OpenTelemetry SDKs](https://opentelemetry.io/docs/languages/), sending traces to the AWS X-Ray service. Choose the ADOT SDKs for the most integrated, AWS-supported experience, and the upstream OpenTelemetry SDKs where ADOT does not cover your language or you already operate an OpenTelemetry pipeline. Both emit the same OpenTelemetry spans. The X-Ray SDKs and daemon are in [maintenance mode](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html) and receive security fixes only, so use OpenTelemetry for new instrumentation and [migrate existing X-Ray SDK instrumentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-migration.html) as you revisit each service. 

   1.  For AI agents, the [CloudWatch Omni IDE extension](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-develop-with-the-ide-extension.html) for Visual Studio Code, Kiro, and Cursor detects a supported agent framework and language in your project and adds the required OpenTelemetry instrumentation, so [agent runs arrive as traces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-send-ai-agent-telemetry.html) before the agent reaches production. A request is only traceable if every service in its path emits spans and passes the trace context downstream. 

1.  **Collect traces with the CloudWatch agent:** Deploy the [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) as your collection point: it is an AWS-managed OpenTelemetry collector, and any OpenTelemetry SDK can [send traces to it over OTLP](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-OpenTelemetry-metrics.html) for forwarding to X-Ray. For serverless functions, add the [ADOT Lambda layer](https://aws-otel.github.io/docs/getting-started/lambda/) instead of running an agent. Standardize this collection so trace data arrives in a consistent form across services. 

1.  **Visualize the request path:** Use the Application Signals [application map](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceMap.html) to see how services connect, where latency accumulates, and which dependencies sit on a request's critical path. The [X-Ray trace map](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-servicemap.html) presents the same topology from the trace backend's console. The map is built from your trace data, so it is also a direct read on instrumentation coverage: a service missing from the map is a service missing spans. 

1.  **Analyze traces for patterns:** With [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) enabled, you can [query every span](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-search-analyze-spans.html) using the same attribute names your instrumentation emits, which turns one-off trace reads into questions you can ask of all transactions. [X-Ray insights](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-insights.html) surfaces anomalies in trace data automatically, and when a trace-derived signal degrades, [CloudWatch investigations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations.html) correlates it with related telemetry and recent changes to provide a hypothesis of the probable cause. Look at slow successful requests, not only errors. 

1.  **Alert on latency and errors:** Configure [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) on the latency and error signals derived from traces, tied to the outcomes in your monitoring plan. Where Application Signals is enabled, define [service level objectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html) on those service metrics so burn-rate alarms warn while error budget remains. Route alerts to the team that owns the affected service. 

1.  **Revisit tracing as the system changes:** Reassess coverage whenever services are added or modified, so new services in the request path are instrumented and the holistic view stays complete. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS01-BP01 Develop application telemetry](ops01-bp01.md) 
+  [OPS01-BP02 Develop user experience telemetry](ops01-bp02.md) 
+  [OPS01-BP03 Develop dependency telemetry](ops01-bp03.md) 
+  [OPS02-BP01 Develop key performance indicators](ops02-bp01.md) 

 **Related documents:** 
+  [AWS X-Ray Developer Guide](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) 
+  [Migrating from X-Ray SDK instrumentation to OpenTelemetry](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-migration.html) 
+  [Enable Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html) 
+  [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) 
+  [OpenTelemetry in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPGettingStarted.html) 
+  [Collect metrics and traces with OpenTelemetry using the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-OpenTelemetry-metrics.html) 
+  [Application Signals trace sampling rate](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application-Signals-SampleRate.html) 
+  [CloudWatch Omni: Monitor AI agents](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-monitor-ai-agents.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Observability for AI Agents and Traditional Workloads (COP335)](https://www.youtube.com/watch?v=oYpCvqZk9SQ) 

 **Related examples:** 
+  [Application Signals demo application](https://github.com/aws-observability/application-signals-demo) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 