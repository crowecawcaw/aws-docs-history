

# Send Claude Platform traces to Amazon CloudWatch
<a name="CloudWatch-OTLP-ClaudePlatformTraces"></a>

Anthropic's Claude Platform exports OpenTelemetry traces for Claude Managed Agents sessions and Messages API requests. Send these traces to Amazon CloudWatch (CloudWatch) to see each agent turn, model call, and tool call in Transaction Search, with latency, token usage, and identifiers, alongside the rest of your stack.

You don't need to change your application code to get started. You add a destination in the Claude Console that sends traces to CloudWatch.

**Beta feature**  
OpenTelemetry export from the Claude Platform is in beta. Anthropic owns the span and field names, which can change.  
AWS supports the telemetry that you send to AWS destinations through the CloudWatch OTLP endpoints.

## How it works
<a name="CloudWatch-ClaudeTraces-HowItWorks"></a>

The Claude Platform sends traces to the CloudWatch traces OTLP endpoint (`https://xray.{{region}}.amazonaws.com/v1/traces`). A Claude Console destination authenticates with request headers over HTTPS, so you choose one of the following ways to authenticate to CloudWatch. For more information about the endpoint, see [Traces endpoint](CloudWatch-OTLPEndpoint.md#CloudWatch-TracesEndpoint).
+ **Option A: Send traces directly with a bearer token (recommended)** – The Claude Console destination sends traces straight to the CloudWatch traces endpoint, with an X-Ray API key in the `Authorization` header. You don't run any infrastructure. The API key can only write trace data, and its use is logged in AWS CloudTrail. Use this option unless one of the cases for Option B applies.
+ **Option B: Send traces through an OpenTelemetry Collector** – The Claude Console destination sends traces to an internet-facing OpenTelemetry Collector that you run. The Collector signs requests with AWS Signature Version 4 (SigV4) and forwards the traces to CloudWatch. Use this option only in the following cases:
  + Your organization's policy doesn't allow IAM users or service-specific credentials, for example because a service control policy (SCP) denies `iam:CreateServiceSpecificCredential`.
  + Your Region doesn't support bearer tokens for traces.
  + You need to process spans before they're stored, for example to redact or truncate prompts, drop attributes, sample, enrich, or send traces to more than one backend. If you only want to keep prompts and responses out of CloudWatch, choose **Metadata only** in Step 2 instead.
  + You already run a public, authenticated OTLP gateway.

  Option B doesn't remove the long-lived secret. The inbound authentication header that your Collector requires is also a long-lived secret stored in the Claude Console, and anyone who has it can write spans. You also have to patch, scale, monitor, and secure an internet-facing service. Because the Claude Platform delivers traces on a best-effort basis with limited retries, spans are dropped while the Collector is unavailable.

## Before you begin
<a name="CloudWatch-ClaudeTraces-Prereqs"></a>

Before you begin, make sure that you have the following:
+ Transaction Search is enabled in your account. For more information, see [Transaction Search](CloudWatch-Transaction-Search.md).
+ You have the Admin role in your Claude Console organization.

**Charges**  
You incur charges for the spans that you send to CloudWatch. If you use an OpenTelemetry Collector, you also incur charges for the resources that run it. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Step 1: Set up authentication
<a name="CloudWatch-ClaudeTraces-Auth"></a>

Complete Option A, unless one of the cases for Option B in [How it works](#CloudWatch-ClaudeTraces-HowItWorks) applies.

### Option A: Create an X-Ray API key
<a name="CloudWatch-ClaudeTraces-Auth-Bearer"></a>

Create an X-Ray API key (bearer token) for an IAM user. Attach the `AWSXRayAPIKeyAccess` managed policy to the user, or a policy that allows the `xray:CallWithBearerToken` and `xray:PutTraceSegments` actions. Traces need their own API key; you can't use an API key that was created for CloudWatch metrics or CloudWatch Logs.

When you create the key, the response includes a `ServiceSpecificCredentialId` and a `ServiceCredentialSecret`. The bearer token is the `ServiceCredentialSecret` value. Don't use the `ServiceSpecificCredentialId`, which causes HTTP 403 errors. Store the secret securely, because you enter it in the Claude Console in Step 2.

For the steps to create the key and the list of Regions that support bearer tokens for traces, see [Setting up bearer token authentication for traces](https://docs.aws.amazon.com/xray/latest/devguide/xray-opentelemetry-bearer-token.html) in the *X-Ray Developer Guide*.

**Long-lived credential**  
An API key is a long-lived credential. Scope the IAM user to only the permissions that it needs to send traces, and rotate the key regularly.

### Option B: Configure an OpenTelemetry Collector
<a name="CloudWatch-ClaudeTraces-Collector"></a>

The Collector must meet the following requirements:
+ Its OTLP receiver is reachable from the internet over HTTPS on port 443, with a certificate from a publicly trusted certificate authority. If needed, put a reverse proxy or load balancer with Transport Layer Security (TLS) termination in front of the Collector.
+ The receiver requires an inbound authentication header. You set the matching header in the Claude Console in Step 2. This header value is a long-lived secret. Generate a strong random value, store it in a secrets manager, and rotate it in both the Collector and the Claude Console.
+ The Collector has AWS credentials with permission to send traces, which the `CloudWatchAgentServerPolicy` or `AWSXrayWriteOnlyPolicy` managed policy grants.

Configure the Collector with an OTLP/HTTP receiver that requires inbound authentication through the `bearertokenauth` extension, the `sigv4auth` extension with the service set to `xray`, and the `otlphttp` exporter with `traces_endpoint` set to the CloudWatch traces OTLP endpoint. Replace {{region}} with your AWS Region, for example `us-west-2`.

The following example shows an OpenTelemetry Collector YAML configuration that receives OTLP/HTTP traces, requires a bearer token on inbound requests, signs the traces with SigV4, and exports them to CloudWatch. The inbound token is read from the `INBOUND_TOKEN` environment variable.

```
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
        auth:
          authenticator: bearertokenauth/inbound

exporters:
  otlphttp/traces:
    compression: gzip
    traces_endpoint: https://xray.{{region}}.amazonaws.com/v1/traces
    auth:
      authenticator: sigv4auth/traces

extensions:
  bearertokenauth/inbound:
    scheme: "Bearer"
    token: "${env:INBOUND_TOKEN}"
  sigv4auth/traces:
    region: "{{region}}"
    service: "xray"

service:
  extensions: [bearertokenauth/inbound, sigv4auth/traces]
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [otlphttp/traces]
```

For more information about building, granting permissions to, and deploying the Collector, see [Getting started](CloudWatch-OTLPGettingStarted.md) and [OpenTelemetry Collector](CloudWatch-OTLPSimplesetup.md).

## Step 2: Add a Custom destination in the Claude Console
<a name="CloudWatch-ClaudeTraces-Destination"></a>

Anthropic owns the Claude Console interface, so the following steps are a guide. Use the values for the option that you chose in Step 1.


**Destination values**  

| Setting | Option A: Bearer token | Option B: OpenTelemetry Collector | 
| --- | --- | --- | 
| OTLP endpoint URL | `https://xray.{{region}}.amazonaws.com` | Your Collector's OTLP/HTTP base URL | 
| Request header | Name: `Authorization`<br />Value: `Bearer {{ServiceCredentialSecret}}` | Name: `Authorization`<br />Value: `Bearer {{inbound-token}}`, the token that your Collector requires | 

**To add a Custom destination**

1. Open the Claude Console, sign in as an Admin, and open the OpenTelemetry settings.

1. In the OpenTelemetry settings, choose **Add destination**.

1. For **Provider**, choose **Custom**.

1. Enter the OTLP endpoint URL and the request header from the preceding table. Don't include `/v1/traces` in the URL, because the Claude Platform appends it.

   The Claude Console doesn't show saved header values again. To change a header value later, enter the full value again.

1. For the content mode, choose **Metadata only** (identifiers, timing, status, and token counts) or **Full content** (also prompts and responses).
**Full content stores prompts and responses**  
With **Full content**, prompts and responses are stored in CloudWatch in the `gen_ai.input.messages` and `gen_ai.output.messages` span attributes. Make sure that this meets your data handling requirements, and restrict access to the traces accordingly.

1. Select the workspaces that send data.

1. Save the destination.

For more information about Claude Console steps and options, see [OpenTelemetry for the Claude API on the Anthropic website](https://platform.claude.com/docs/en/manage-claude/opentelemetry).

## Step 3: Verify the integration
<a name="CloudWatch-ClaudeTraces-Verify"></a>

**To verify the integration**

1. In the Claude Console, on the destination that you created, choose the **⋯** menu, and then choose **Test**. The Claude Platform sends an `anthropic.test` span. This is the fastest way to check the connection.

   Alternatively, send a Messages API request or run a Managed Agents session.

1. In the Claude Console, confirm that the destination's **Delivery status** shows **Healthy**. This usually takes about a minute.

1. In the CloudWatch console, open Transaction Search and filter on `service.name` = `claude-platform`.

   Spans can take 1–4 minutes to become searchable after the delivery status shows **Healthy**. A parent span can appear a few minutes after its child spans.

## What the Claude Platform sends
<a name="CloudWatch-ClaudeTraces-Attributes"></a>

The Claude Platform sends traces only, not metrics or logs. The spans follow the OpenTelemetry GenAI semantic conventions, and the Claude Platform sends every span unless your trace context drops it. The Claude Platform sends spans such as the following:
+ `anthropic.messages.create` – A Messages API request. This is the server span for each `POST /v1/messages` request. It is the root span unless the caller sends a `traceparent` header.
+ `anthropic.model_request` – A model call within a request. This is an internal child span, one for each model request, and it carries the model and token usage.
+ `anthropic.test` – A test span that you send from the Claude Console.

Every span has the resource attribute `service.name` set to `claude-platform` and the instrumentation scope `com.anthropic.claude-platform`. The following table lists span attributes. Not every span includes every attribute.


| Attribute | Description | 
| --- | --- | 
| `gen_ai.provider.name` | Always `anthropic`. | 
| `anthropic.organization.id`, `anthropic.workspace.id` | The Claude Console organization and workspace that the request belongs to. | 
| `gen_ai.operation.name` | `chat` for Messages API requests (on the `anthropic.messages.create` span) and for model requests in Managed Agents sessions, `invoke_agent` for agent turns, and `execute_tool` for tool calls. | 
| `gen_ai.conversation.id` | Groups Managed Agents spans across traces into a conversation. Messages API requests do not have it. | 
| `gen_ai.agent.id`, `gen_ai.agent.name` | The agent that ran the turn (agent turns only). | 
| `gen_ai.request.model`, `gen_ai.response.model` | The requested and actual model. | 
| `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens` | Token counts. | 
| `gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions` | Message content (**Full content** mode only). | 
| `gen_ai.tool.call.arguments` | Tool input (**Full content** mode only). | 
| `anthropic.tool_result.content` | Tool output (**Full content** mode only). | 

**Span names can change**  
Anthropic owns these spans, which are in beta and can change. For more information about the spans, see [OpenTelemetry for the Claude API on the Anthropic website](https://platform.claude.com/docs/en/manage-claude/opentelemetry).

## Connect Claude traces to your application traces
<a name="CloudWatch-ClaudeTraces-Connect"></a>

If your application calls the Claude API and is instrumented with OpenTelemetry, propagate W3C trace context by sending the `traceparent` header, with the sampled flag set to keep, on each request. Claude's spans then nest under your application's spans in the same trace in Transaction Search. If the sampled flag is not set to keep, the spans might not be connected.

## Troubleshooting Claude Platform traces
<a name="CloudWatch-ClaudeTraces-Troubleshooting"></a>

Use the following guidance to resolve common problems:
+ **Delivery status** shows **Failing** with HTTP 401 or 403. If you send traces directly (Option A), confirm that the `Authorization` header is `Bearer` followed by the `ServiceCredentialSecret` value of an X-Ray API key (not the `ServiceSpecificCredentialId`, and not a CloudWatch metrics or CloudWatch Logs key), and that the key is active and its IAM user is allowed `xray:CallWithBearerToken` and `xray:PutTraceSegments`. If you use a Collector (Option B), confirm that the header in the Claude Console matches the one that your Collector expects.
+ **Delivery status** shows **Failing** with HTTP 404. The OTLP endpoint URL has the wrong path. For a Custom destination, do not include `/v1/traces`.
+ **Delivery status** shows a TLS failure (Option B). The Collector endpoint must use HTTPS on port 443 with a certificate from a publicly trusted certificate authority.
+ No spans appear in Transaction Search. Confirm that Transaction Search is enabled. If you send traces directly, confirm that your Region supports bearer tokens for traces. If you use a Collector, confirm that it is reachable and healthy, and that it has SigV4 permissions (`CloudWatchAgentServerPolicy` or `AWSXrayWriteOnlyPolicy`) to the X-Ray traces endpoint.
+ Claude spans do not nest under your application's spans. Confirm that your application sends a `traceparent` header with the sampled flag set to keep.