

# Publishing custom metrics with the embedded metric format
<a name="web-functions-emf"></a>

With the [Amazon CloudWatch embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html) (EMF), you can publish your own metrics from AWS Lambda Web Functions, such as orders placed, cache hit rate, or payment latency. Your application writes a structured JSON object to its logs, and CloudWatch extracts the metrics from it. Use custom metrics to track what your application does. The metrics that Lambda publishes describe only request outcomes and resource usage.

You can also publish custom metrics by calling the CloudWatch `PutMetricData` API directly, but we recommend EMF for Web Functions:
+ **No added request latency** – Your application doesn't call the CloudWatch API on the path that serves your HTTP response.
+ **No extra permission** – You don't need the `cloudwatch:PutMetricData` permission. EMF uses the same Amazon CloudWatch Logs permissions that the execution role already needs for logs.
+ **Centralization with your logs** – Because EMF metrics travel with your logs, the home Region has values from every Region that the endpoint serves. Metrics that you publish with `PutMetricData` appear only in the Region where you call it.

## How EMF works with Web Functions
<a name="web-functions-emf-how-it-works"></a>

EMF metrics travel from your application to CloudWatch through the following steps:

1. Your application writes an EMF-formatted JSON object, followed by a newline, directly to standard output.

1. Lambda captures it as a log event in the Region where the request ran and centralizes it into the home AWS Region, the same as any other log output. For details, see [Web Function logs in Amazon CloudWatch Logs](web-functions-logging.md).

1. CloudWatch extracts metrics from the object in the Region where the request ran, and Lambda replicates the metrics to the home Region. The metrics appear in the namespace that you specify in the object. In the home Region, the metrics include values from every Region that the endpoint serves.

Your custom metrics appear in your own namespace, not in `AWS/Lambda/Web`. That namespace is reserved for the metrics Lambda publishes.

## Publishing a custom metric
<a name="web-functions-emf-example"></a>

The following Node.js example publishes a `CheckoutLatency` metric and an `OrdersPlaced` metric under the `MyWebApp` namespace, with a `PaymentProvider` dimension. It writes the EMF object with `process.stdout.write`. Do not pass an EMF object to a `console` method. Lambda wraps `console` output in its own JSON log event, and CloudWatch does not extract metrics from the wrapped object.

```
function publishCheckoutMetrics(provider, latencyMs, orders) {
  process.stdout.write(JSON.stringify({
    _aws: {
      Timestamp: Date.now(),
      CloudWatchMetrics: [
        {
          Namespace: 'MyWebApp',
          Dimensions: [['PaymentProvider']],
          Metrics: [
            { Name: 'CheckoutLatency', Unit: 'Milliseconds' },
            { Name: 'OrdersPlaced', Unit: 'Count' }
          ]
        }
      ]
    },
    PaymentProvider: provider,
    CheckoutLatency: latencyMs,
    OrdersPlaced: orders,
    // Fields outside the metric definitions are kept as searchable log context.
    requestPath: '/checkout'
  }) + '\n');
}
```

Instead of building EMF objects yourself, you can use an EMF client library, such as [aws-embedded-metrics for Node.js](https://github.com/awslabs/aws-embedded-metrics-node) on the GitHub website. For the list of libraries, see [Creating logs in embedded metric format using the client libraries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Libraries.html) in the *Amazon CloudWatch User Guide*. Before you rely on a library, confirm that it writes EMF objects directly to standard output in a Web Function, instead of through `console` or to a CloudWatch agent.

Note the three roles that fields play in an EMF object:
+ Fields named in `Metrics` become CloudWatch metrics.
+ Fields named in `Dimensions` become metric dimensions. Keep the number of distinct dimension values low. Each combination creates a separate metric.
+ Any other field is kept in the log event as context you can query with Amazon CloudWatch Logs Insights, but does not create a metric.

Use the last property deliberately: attach high-cardinality values such as a request ID or customer ID as plain fields rather than as dimensions, so you can find the specific request in Logs Insights without multiplying your metric count.

## Billing for custom metrics
<a name="web-functions-emf-billing"></a>

EMF generates both log ingestion and custom metric charges. The log event is billed at Amazon CloudWatch Logs prices, and the extracted metrics are billed as CloudWatch custom metrics. The first centralization of a log event is free. CloudWatch extracts EMF metrics in the Region where the request ran, and Lambda replicates them to the home Region, so a request served outside the home Region produces custom metrics in both Regions.

Log volume, the number of metrics, and the number of distinct dimension combinations affect cost. Publish metrics at the granularity you will alarm on or graph, and avoid high-cardinality dimensions.

For current prices, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).