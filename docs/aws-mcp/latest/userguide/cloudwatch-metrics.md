# AWS MCP Server (Preview) CloudWatch metrics

AWS MCP Server (Preview) automatically publishes metrics to Amazon CloudWatch at no additional cost. You can use these metrics
to monitor usage patterns, track success rates, identify errors, and set up alarms for your AWS MCP Server operations.

## Metrics namespace

All AWS MCP Server (Preview) metrics are published under the `AWS-MCP` namespace in CloudWatch. Metrics are
organized by tool name, allowing you to monitor which MCP tools you use most frequently (such as
`aws___call_aws` or `aws___list_regions`) and track their success rates.

## Available metrics

The following metrics are available for AWS MCP Server (Preview). All metrics use standard resolution (1-minute granularity).

| Metric        | Description                                                                       | Unit  |
| ------------- | --------------------------------------------------------------------------------- | ----- |
| `Invocation`  | The number of times a tool was called, regardless of the response status.         | Count |
| `Success`     | The number of successful requests that returned a 200 response.                   | Count |
| `UserError`   | The number of requests that failed with a 4XX client error (excluding throttles). | Count |
| `SystemError` | The number of requests that failed with a 5XX server error.                       | Count |
| `Throttle`    | The number of requests that were throttled with a 429 response.                   | Count |

## Metric dimensions

Metrics include the following dimensions to help you filter and analyze your data:

**Tool Name**

The name of the specific MCP tool that was invoked. For example, `aws___call_aws`,
`aws___list_regions`, or `aws___retrieve_agent_sop`. For a complete list of available
tools, see [Understanding the MCP Server tools](understanding-mcp-server-tools.md "understanding-mcp-server-tools.md").

## Using metrics

You can use AWS MCP Server (Preview) metrics to:

- **Monitor usage patterns** – Track which tools you use most
  frequently to understand your interaction patterns with AWS services.
- **Identify errors** – Monitor `UserError` and `SystemError`
  metrics to quickly detect and troubleshoot issues such as permission problems or service disruptions.
- **Track success rates** – Calculate success rates by comparing `Success`
  counts to `Invocation` counts to ensure your operations are completing successfully.
- **Set up alarms** – Create CloudWatch alarms to notify you when error rates exceed
  thresholds or when usage patterns change unexpectedly.
- **Optimize costs** – Monitor invocation counts to identify inefficient usage
  patterns that might be increasing your AWS costs.

For more information about working with CloudWatch metrics, see [Using Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in the
_CloudWatch User Guide_.

## Example use cases

The following examples show how you can use AWS MCP Server (Preview) metrics:

Calculate success rate for API calls

Filter metrics by `Tool Name = aws___call_aws` and compare `Success` to
`Invocation` to calculate your API call success rate. Set up an alarm to notify you if the
success rate drops below 95%.

Detect permission issues

Monitor `UserError` metrics for specific tools. A spike in user errors often indicates
IAM permission issues or incorrect API parameters.

Track tool usage trends

Compare `Invocation` counts across different tools over time to understand which AWS
services and operations you interact with most frequently.

Monitor system health

Set up alarms for `SystemError` metrics to be notified of service disruptions or
infrastructure issues that might affect your operations.
