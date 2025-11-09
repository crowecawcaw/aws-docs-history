# Anomaly detection

Amazon Managed Service for Prometheus provides anomaly detection capabilities that use machine learning algorithms to
automatically identify unusual patterns in your metric data. This feature helps you
proactively detect potential issues, reduce alert fatigue, and improve your monitoring
effectiveness by focusing on truly anomalous behavior rather than static thresholds.

Anomaly detection in Amazon Managed Service for Prometheus uses the Random Cut Forest (RCF) algorithm, which analyzes
your time series data to establish normal behavior patterns and identify deviations from
those patterns. The algorithm adapts to seasonal trends, handles missing data gracefully,
and provides confidence scores for detected anomalies.

## How anomaly detection works

Amazon Managed Service for Prometheus anomaly detection uses machine learning to identify unusual patterns in metrics
data without manual threshold configuration. The system learns normal behavior patterns
and seasonal variations, reducing false positives and enabling early issue detection. It
continuously adapts to application changes, making it suitable for dynamic cloud
environments.

Anomaly detection monitors application performance metrics like response times and
error rates, tracks infrastructure health through CPU and memory usage, detects unusual
user behavior, identifies capacity planning needs through traffic analysis, and monitors
business metrics for unexpected changes. It works best with predictable patterns,
seasonal variations, or gradual growth trends.

The Random Cut Forest (RCF) algorithm is used to analyze time series data. RCF creates
decision trees that partition data space and identifies isolated points far from normal
distribution. The algorithm learns from incoming data to build a dynamic model of normal
behavior for each metric.

When enabled, it analyzes historical data to establish baseline patterns and seasonal
trends, then generates predictions for expected values and identifies deviations. The
algorithm produces four key outputs:

- _upper_band_ - The upper boundary of expected normal
  values
- _lower_band_ - The lower boundary of expected normal
  values
- _score_ - A numerical anomaly score indicating how unusual
  the data point is
- _value_ - The actual observed metric value

## Getting started with anomaly

detection

To begin using anomaly detection with your Prometheus metrics, you need sufficient
historical data for the algorithm to learn normal patterns. We recommend having at least
14 days of consistent metric data before enabling anomaly detection for optimal
results.

You can preview how anomaly detection will work with your metrics using the
`PreviewAnomalyDetector` API. Use `PreviewAnomalyDetector` to
test the algorithm against your historical data and evaluate its effectiveness before
implementing it in production monitoring. For more information, see [PreviewAnomalyDetector API](anomaly-detection-api.md "anomaly-detection-api.md").

When implementing anomaly detection, consider these best practices:

- **Start with stable metrics** – Begin with
  metrics that have consistent patterns and avoid highly volatile or sparse data
  initially.
- **Use aggregated data** – Apply anomaly
  detection to aggregated metrics (such as averages or sums) rather than raw,
  high-cardinality data for better performance and accuracy.
- **Tune sensitivity** – Adjust the
  algorithm parameters based on your specific use case and tolerance for false
  positives versus missed anomalies.
- **Monitor algorithm performance** –
  Regularly review detected anomalies to ensure the algorithm continues to provide
  valuable insights as your system evolves.
