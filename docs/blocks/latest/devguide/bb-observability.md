

# Observability
<a name="bb-observability"></a>

This section covers Blocks for monitoring, logging, and tracing.

## Choosing an observability Block
<a name="_choosing_an_observability_block"></a>


| Block | Best for | Avoid when | 
| --- | --- | --- | 
|  `Metrics`  | Custom application metrics with dimensions for filtering and aggregation | You only need request-level tracing (use Tracer) | 
|  `Logger`  | Structured JSON logging with correlation IDs and log levels | You need numeric aggregation or alerting (use Metrics) | 
|  `Tracer`  | Distributed tracing across services, latency analysis, dependency mapping | You only need simple log output (use Logger) | 
|  `Dashboard`  | Real-time operational views combining metrics, logs, and alarms | You don’t have Metrics or Logger blocks yet (add those first) | 

## Metrics
<a name="bb-metrics"></a>

Custom application metrics. Emit named metric data points with dimensions for filtering and aggregation. Supports child emitters with merged dimensions for scoped metric contexts. Uses CloudWatch Embedded Metric Format for zero-latency metric emission.

Locally, Metrics writes to the console. On AWS, metrics flow to Amazon CloudWatch. Best for tracking business KPIs, API latencies, error rates, and custom application counters.

For more information, see [bb-metrics on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-metrics).

## Logger
<a name="bb-logger"></a>

Structured JSON logging with levels, contextual metadata, and correlation IDs. Supports debug, info, warn, and error levels. Attach arbitrary metadata to log entries for filtering and analysis.

Locally, Logger writes to the console. On AWS, structured JSON flows to CloudWatch Logs with automatic correlation to API Gateway request IDs. Best for application logging with searchable structured data.

For more information, see [bb-logger on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-logger).

## Tracer
<a name="bb-tracer"></a>

Distributed request tracing. Wrap operations in traced segments to visualize request flow across your application. Add searchable annotations for debugging and add metadata for detailed inspection.

Locally, Tracer is a no-op. On AWS, it integrates with AWS X-Ray for distributed tracing across Lambda, API Gateway, and downstream services. Best for debugging latency issues and understanding request paths in production.

For more information, see [bb-tracer on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-tracer).

## Dashboard
<a name="bb-dashboard"></a>

Auto-generated observability dashboard. Define your metrics and Dashboard generates a CloudWatch dashboard automatically from your Metrics definitions. No manual widget configuration needed.

Locally, Dashboard is a no-op. On AWS, it provisions a CloudWatch Dashboard with widgets for each metric you emit. Best for teams that want out-of-the-box monitoring without manual dashboard setup.

For more information, see [bb-dashboard on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-dashboard).