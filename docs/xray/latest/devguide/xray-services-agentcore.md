

# Amazon Bedrock AgentCore and AWS X-Ray
<a name="xray-services-agentcore"></a>

Amazon Bedrock AgentCore integrates with AWS X-Ray to provide distributed tracing capabilities for your AI agents and tools. This integration allows you to track requests as they flow through your agent applications, helping you identify performance bottlenecks and troubleshoot issues.

AgentCore supports distributed tracing through X-Ray integration, allowing you to monitor the performance of your AI agents and tools. When you enable observability for your AgentCore resources, you can propagate trace context across service boundaries and gain visibility into how your agents interact with other AWS services. For more information, see [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-genesis.html). 

AgentCore supports the following X-Ray features:
+ Propagation of trace context to downstream services
+ Custom instrumentation using the AWS Distro for OpenTelemetry (ADOT) SDK

## Setting up X-Ray with AgentCore
<a name="xray-services-agentcore-settingup"></a>

To use X-Ray with AgentCore, you need to enable CloudWatch Transaction Search in your AWS account. This is a one-time setup that allows AgentCore to send trace data to X-Ray. For more information, see [Enable transaction search ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html).

For more information about setting up observability for AgentCore, see [Add observability to your Amazon Bedrock AgentCore agent or tool ](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html).

## Using trace headers with AgentCore
<a name="xray-services-agentcore-trace"></a>

AgentCore supports the X-Ray trace header format for distributed tracing. You can include the `X-Amzn-Trace-Id` header in your requests to AgentCore to maintain trace context across service boundaries.