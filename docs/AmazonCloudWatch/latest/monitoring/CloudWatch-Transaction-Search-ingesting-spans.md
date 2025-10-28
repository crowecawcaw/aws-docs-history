# Ingesting spans for complete visibility

Recording all transaction spans provides comprehensive visibility into application issues.
It enables you to debug customer support tickets or troubleshoot rarely occurring p99 API latency spikes, which is crucial when identifying the root cause of issues in customer-facing and mission-critical applications.
You can create a cost-effective strategy to start capturing 100% of trace spans in CloudWatch by configuring the head sampling rate and then adjusting a lower span indexing rate.

## Setting up head sampling

Head sampling is a tracing technique capturing requests at the beginning of a trace, which is based on a set rate or condition.

When the head sampling rate is set to 100%, it captures the beginning of every trace without skips, guaranteeing complete visibility into all incoming requests, and that no transaction data is missed.

You can configure head sampling if you're using X-Ray or AWS Distro for OpenTelemetry SDKs or the OpenTelemetry SDK.

###### If you're using X-Ray or AWS Distro for OpenTelemetry SDKs

Navigate to your sampling rules in the console, and set the fixed sampling rate to 100%.
This guarantees all trace spans are captured and ingested into CloudWatch logs.
For more information, see [Configuring sampling rules](../../../xray/latest/devguide/xray-console-sampling.md#xray-console-config "../../../xray/latest/devguide/xray-console-sampling.md#xray-console-config")

###### If you're using the OpenTelemetry SDK

To record 100% of spans and get complete visibility, set your sampling configuration to [`always_on`](https://opentelemetry.io/docs/languages/java/sdk/#sampler "https://opentelemetry.io/docs/languages/java/sdk/#sampler").
For more information, see Language APIs & SDKs on the OpenTelemetry website.

### Features unlocked with head sampling

When you enable Transaction Search, all spans collected from your application through head sampling are ingested as structured logs in CloudWatch.
This provides you with the following features:

- The ability to search span attributes and analyze span events in a visual editor.
- The ability to visualize traces containing up to 10,000 spans.
- Total support for OpenTelemetry, which includes the ability to embed business events into spans for analysis and use span links to define connections between traces for end-to-end viewing.
- Access to application dashboards, metrics, and topology with CloudWatch Application Signals enabled for all spans sent to CloudWatch.

###### Note

Because spans are available in a log group called `aws/spans`, you can use CloudWatch Logs features with transaction spans.
For more information, see [The span log group](CloudWatch-Transaction-Search-ingesting-span-log-groups.md "CloudWatch-Transaction-Search-ingesting-span-log-groups.md").

## Setting up span indexing with trace summaries

Trace summaries can help you debug transactions and are beneficial for asynchronous processes.
You only need to index a small percentage of spans as trace summaries.

You configure span indexing when you enable Transaction Search in the console or with the API.
To enable Transaction Search, see [Getting started with Transaction Search](CloudWatch-Transaction-Search-getting-started.md "CloudWatch-Transaction-Search-getting-started.md").

### Features unlocked with trace summaries

The key features of X-Ray trace summaries include the following:

- [Trace summary search](../../../xray/latest/devguide/xray-console-traces.md#xray-console-traces-view "../../../xray/latest/devguide/xray-console-traces.md#xray-console-traces-view") – Search and find traces from trace summaries.
- [Trace summary analytics](../../../xray/latest/devguide/xray-console-analytics.md "../../../xray/latest/devguide/xray-console-analytics.md") – Interpret trace data.
- [Trace insights](../../../xray/latest/devguide/xray-console-insights.md "../../../xray/latest/devguide/xray-console-insights.md") – Analyze trace data to identify application issues.
