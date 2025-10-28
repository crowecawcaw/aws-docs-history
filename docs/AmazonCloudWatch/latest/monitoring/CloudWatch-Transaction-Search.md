# Transaction Search

Transaction Search is an interactive analytics experience you can use to get complete visibility of your application transaction spans.
Spans are the fundamental units of operation in a distributed trace and represent specific actions or tasks in an application or system.
Every span records details about a particular segment of the transaction.
These details include start and end times, duration, and associated metadata, which can include business attributes like customer IDs and order IDs.
Spans are arranged in a parent-child hierarchy.
This hierarchy forms a complete trace, mapping the flow of a transaction across different components or services.

![View of the visual editor for spans](images/transactionsearch1.png)

###### Topics

- [Benefits](#w29aac28c21b9 "#w29aac28c21b9")
- [How it works](#w29aac28c21c11 "#w29aac28c21c11")
- [Pricing](#w29aac28c21c13 "#w29aac28c21c13")
- [Enable transaction search](Enable-TransactionSearch.md "Enable-TransactionSearch.md")
- [Spans](CloudWatch-Transaction-Search-ingesting-span-log-groups.md "CloudWatch-Transaction-Search-ingesting-span-log-groups.md")
- [Adding custom attributes](CloudWatch-Transaction-Search-add-custom-attributes.md "CloudWatch-Transaction-Search-add-custom-attributes.md")
- [Troubleshooting application issues](CloudWatch-Transaction-Search-troubleshooting.md "CloudWatch-Transaction-Search-troubleshooting.md")

## Benefits

The following are benefits of using Transaction Search:

###### Capture all spans

Ingest 100 percent of spans as structured logs in CloudWatch to get complete visibility.
This prevents broken traces and provides you the ability to view large traces containing up to 10,000 spans for detailed insights.

###### Index spans as trace summaries

Index a percentage of spans as trace summaries in X-Ray to unlock end to end trace search and analytics.

###### Investigate transaction issues with free form analytics

Search all span attributes in the visual editor to identify the cause of issues in application transactions.
This helps you answer questions about application performance and the impact end-users make based on their application transactions.

###### Send spans to the OpenTelemetry endpoint

Send spans to the OpenTelemetry endpoint for X-Ray traces.
These spans are stored in [the semantic convention format with W3C trace IDs](https://opentelemetry.io/docs/specs/semconv/general/trace/ "https://opentelemetry.io/docs/specs/semconv/general/trace/").

###### Note

X-Ray traces automatically convert to the semantic convention format before they're stored in a log group called `aws/spans`.
For more information, see [The span log group](CloudWatch-Transaction-Search-ingesting-span-log-groups.md "CloudWatch-Transaction-Search-ingesting-span-log-groups.md").

###### Use CloudWatch Logs with spans

Use metric filters to extract custom metrics, subscription filters to forward data, and data masking to protect personally identifiable information.

###### Troubleshoot application issues

Access application dashboards, metrics, and topology when you enable Application Signals for all spans sent to CloudWatch.

## How it works

When you enable Transaction Search, you unlock multiple capabilities, including features in Application Signals and CloudWatch Logs.

![Overview of how Transaction Search works with other services](images/howitworks.png)

If you send traces to X-Ray, you can [get started by enabling Transaction Search](CloudWatch-Transaction-Search-getting-started.md "CloudWatch-Transaction-Search-getting-started.md") in the console or with the API.
If you don't send traces to X-Ray, you can use the [CloudWatch Application Signals](CloudWatch-Application-Signals-Enable.md "CloudWatch-Application-Signals-Enable.md") that provides pre-packaged OpenTelemetry setup with
AWS Distro fro OpenTelemetry (ADOT), CloudWatch Agent, or use OpenTelemetry directly.

When you enable Transaction Search, spans sent to X-Ray are ingested in a log group called `aws/spans`.
CloudWatch uses these spans to generate a curated application performance monitoring (APM) experience in CloudWatch Application Signals.
This provides you the ability to search and analyze spans, as well as use CloudWatch Logs capabilities like outlier and pattern detection.
You can even use custom metric extraction .
CloudWatch Application Signals provides you with a unified, application-centric view of your applications, services, and dependencies.
It also helps you monitor and triage application health.

You can also explore spans using the interactive search and analytics experience in CloudWatch to answer any questions related to application performance or end-user impact with Transaction Search.
Detect the impact on end users, find transactions in context of those issues using relevant attributes, such as customer name or order number.
You can correlate transactions to business events, such as failed payments, and dive into interactions between application components to establish a root cause.
With CloudWatch, you get complete application transaction coverage with correlated insights, helping you to accelerate mean time to resolution.

## Pricing

For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
