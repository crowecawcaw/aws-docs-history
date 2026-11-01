

# Observability, audit logging, and tracing for your agents
<a name="observability"></a>

With Amazon Bedrock AgentCore, you can trace and audit your agents in production across three pillars: tracing and telemetry, metrics and monitoring, and audit logging.

 **Tracing and telemetry** 

With AgentCore, you can trace, debug, and monitor your agents' performance in production. AgentCore Observability provides detailed visualizations of each step in the agent workflow. You can inspect an agent’s execution path, audit intermediate outputs, and debug performance bottlenecks and failures. AgentCore emits telemetry data in a standardized OpenTelemetry (OTEL)-compatible format, so you can integrate it with your existing monitoring and observability stack.

 **Metrics and monitoring** 

AgentCore Observability gives you real-time visibility into agent operational performance through dashboards powered by Amazon CloudWatch. You can track key metrics such as session count, latency, duration, token usage, and error rates. Rich metadata tagging and filtering simplify issue investigation and quality maintenance at scale.

By default, AgentCore outputs a set of key built-in metrics for agents, gateway resources, and memory resources. For memory resources, AgentCore also outputs spans and log data if you enable it. You can also instrument your agent code to provide additional span and trace data and custom metrics and logs. See [Add observability to your Amazon Bedrock AgentCore resources](observability-configure.md) to learn more.

All of the metrics, spans, and logs output by AgentCore are stored in Amazon CloudWatch, and you can view them on the AgentCore observability page, in the CloudWatch console, or download them from CloudWatch using the AWS CLI or one of the AWS SDKs.

In addition to the raw data stored in CloudWatch Logs, for agent runtime data only, the CloudWatch console provides an observability dashboard containing trace visualizations, graphs for custom span metrics, error breakdowns, and more. To learn more about viewing your agents' observability data, see [View observability data for your Amazon Bedrock AgentCore agents](observability-view.md).

 **Audit logging** 

AgentCore records service API activity in AWS CloudTrail so you can audit who performed each API action and when. CloudTrail coverage is currently available for certain AgentCore capabilities. The AgentCore Gateway and Agent Registry capabilities each record their API activity in CloudTrail. For more information, see the following topics:
+  [Log Amazon Bedrock AgentCore Gateway API calls with CloudTrail](gateway-cloudtrail.md) 
+  [Understanding Amazon Bedrock AgentCore Gateway CloudTrail events](understanding-gateway-cloudtrail-log-entries.md) 
+  [Enable CloudTrail data event logging for Amazon Bedrock AgentCore Gateway resources](enabling-cloudtrail-data-event-logging.md) 
+  [Log Registry API calls with AWS CloudTrail](registry-cloudtrail.md) 
+  [AWS CloudTrail integration (Agent Registry)](registry-cloudtrail-integration.md) 

**Topics**
+ [Get started with AgentCore Observability](observability-get-started.md)
+ [Add observability to your Amazon Bedrock AgentCore resources](observability-configure.md)
+ [Understand observability for agentic resources in AgentCore](observability-telemetry.md)
+ [Amazon Bedrock AgentCore generated observability data](observability-service-provided.md)
+ [View observability data for your Amazon Bedrock AgentCore agents](observability-view.md)
+ [Monitor AgentCore resources across accounts](observability-cross-account.md)