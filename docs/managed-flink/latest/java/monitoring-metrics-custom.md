Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Use custom metrics with Amazon Managed Service for Apache Flink

Managed Service for Apache Flink exposes 19 metrics to CloudWatch, including metrics for resource usage and throughput. In addition, you can
create your own metrics to track application-specific data, such as processing events or accessing external resources.

###### This topic contains the following sections:

- [How it works](#monitoring-metrics-custom-howitworks "#monitoring-metrics-custom-howitworks")
- [View examples for creating a mapping
  class](#monitoring-metrics-custom-examples "#monitoring-metrics-custom-examples")
- [View custom metrics](#monitoring-metrics-custom-examples-viewing "#monitoring-metrics-custom-examples-viewing")

## How it works

Custom metrics in Managed Service for Apache Flink use the Apache Flink metric system. Apache Flink metrics have the following attributes:

- **Type:** A metric's type describes how it measures and reports data. Available
  Apache Flink metric types
  include Count, Gauge, Histogram, and Meter. For more information about Apache Flink metric types, see
  [Metric Types](https://nightlies.apache.org/flink/flink-docs-release-1.15/monitoring/metrics.html#metric-types "https://nightlies.apache.org/flink/flink-docs-release-1.15/monitoring/metrics.html#metric-types").

###### Note

AWS CloudWatch Metrics does not support the Histogram Apache Flink metric type. CloudWatch can only display Apache Flink metrics of the
Count, Gauge, and Meter types.

- **Scope:** A metric's scope consists of its identifier and a set of key-value pairs
  that indicate how the metric will be reported to CloudWatch. A metric's identifier consists of the following:

      + A system scope, which indicates the level at which the metric is reported (e.g. Operator).
      + A user scope, that defines attributes such as user variables or the metric group names. These
       attributes are defined using
       [`MetricGroup.addGroup(key, value)`](https://ci.apache.org/projects/flink/flink-docs-master/api/java/org/apache/flink/metrics/MetricGroup.html#addGroup-java.lang.String-java.lang.String- "https://ci.apache.org/projects/flink/flink-docs-master/api/java/org/apache/flink/metrics/MetricGroup.html#addGroup-java.lang.String-java.lang.String-") or
       [`MetricGroup.addGroup(name)`](https://ci.apache.org/projects/flink/flink-docs-master/api/java/org/apache/flink/metrics/MetricGroup.html#addGroup-java.lang.String- "https://ci.apache.org/projects/flink/flink-docs-master/api/java/org/apache/flink/metrics/MetricGroup.html#addGroup-java.lang.String-").

  For more information about metric scope, see
  [Scope](https://nightlies.apache.org/flink/flink-docs-release-1.15/monitoring/metrics.html#scope "https://nightlies.apache.org/flink/flink-docs-release-1.15/monitoring/metrics.html#scope").

For more information about Apache Flink metrics, see
[Metrics](https://nightlies.apache.org/flink/flink-docs-release-1.15/monitoring/metrics.html "https://nightlies.apache.org/flink/flink-docs-release-1.15/monitoring/metrics.html")
in the [Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.15/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/").

To create a custom metric in your Managed Service for Apache Flink, you can access the Apache Flink metric system from any user function that extends
`RichFunction` by calling
[`GetMetricGroup`](https://nightlies.apache.org/flink/flink-docs-release-1.15/api/java/org/apache/flink/api/common/functions/RuntimeContext.html#getMetricGroup-- "https://nightlies.apache.org/flink/flink-docs-release-1.15/api/java/org/apache/flink/api/common/functions/RuntimeContext.html#getMetricGroup--"). This method returns a
[MetricGroup](https://nightlies.apache.org/flink/flink-docs-release-1.15/api/java/org/apache/flink/metrics/MetricGroup.html "https://nightlies.apache.org/flink/flink-docs-release-1.15/api/java/org/apache/flink/metrics/MetricGroup.html")
object you can use to create and register custom metrics. Managed Service for Apache Flink reports all metrics created with the group key `KinesisAnalytics`
to CloudWatch. Custom metrics that you define have the following characteristics:

- Your custom metric has a metric name and a group name. These names must consist of alphanumeric characters according to [Prometheus naming rules](https://prometheus.io/docs/instrumenting/writing_exporters/#naming "https://prometheus.io/docs/instrumenting/writing_exporters/#naming").
- Attributes that you define in user scope (except for the `KinesisAnalytics` metric group) are published
  as CloudWatch dimensions.
- Custom metrics are published at the `Application` level by default.
- Dimensions (Task/ Operator/ Parallelism) are added to the metric based on the application's monitoring level. You set the application's
  monitoring level using the [MonitoringConfiguration](../apiv2/API_MonitoringConfiguration.md "../apiv2/API_MonitoringConfiguration.md")
  parameter of the [CreateApplication](../apiv2/API_CreateApplication.md "../apiv2/API_CreateApplication.md") action, or the
  or [MonitoringConfigurationUpdate](../apiv2/API_MonitoringConfigurationUpdate.md "../apiv2/API_MonitoringConfigurationUpdate.md")
  parameter of the [UpdateApplication](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") action.

## View examples for creating a mapping

class

The following code examples demonstrate how to create a mapping class that creates and
increments a custom metric, and how to implement the mapping class in your application
by adding it to a `DataStream` object.

### Record count custom metric

The following code example demonstrates how to create a mapping class that creates a metric that counts records
in a data stream (the same functionality as the `numRecordsIn` metric):

```
    private static class NoOpMapperFunction extends RichMapFunction<String, String> {
        private transient int valueToExpose = 0;
        private final String customMetricName;

        public NoOpMapperFunction(final String customMetricName) {
            this.customMetricName = customMetricName;
        }

        @Override
        public void open(Configuration config) {
            getRuntimeContext().getMetricGroup()
                    .addGroup("KinesisAnalytics")
                    .addGroup("Program", "RecordCountApplication")
                    .addGroup("NoOpMapperFunction")
                    .gauge(customMetricName, (Gauge<Integer>) () -> valueToExpose);
        }

        @Override
        public String map(String value) throws Exception {
            valueToExpose++;
            return value;
        }
    }
```

In the preceding example, the `valueToExpose` variable is incremented for each record that the application processes.

After defining your mapping class, you then create an in-application stream that implements the map:

```
DataStream<String> noopMapperFunctionAfterFilter =
    kinesisProcessed.map(new NoOpMapperFunction("FilteredRecords"));
```

For the complete code for this application, see
[Record Count Custom Metric Application](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/CustomMetrics/RecordCount "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/CustomMetrics/RecordCount").

### Word count custom metric

The following code example demonstrates how to create a mapping class that creates a metric that counts words
in a data stream:

```
private static final class Tokenizer extends RichFlatMapFunction<String, Tuple2<String, Integer>> {

            private transient Counter counter;

            @Override
            public void open(Configuration config) {
                this.counter = getRuntimeContext().getMetricGroup()
                        .addGroup("KinesisAnalytics")
                        .addGroup("Service", "WordCountApplication")
                        .addGroup("Tokenizer")
                        .counter("TotalWords");
            }

            @Override
            public void flatMap(String value, Collector<Tuple2<String, Integer>>out) {
                // normalize and split the line
                String[] tokens = value.toLowerCase().split("\\W+");

                // emit the pairs
                for (String token : tokens) {
                    if (token.length() > 0) {
                        counter.inc();
                        out.collect(new Tuple2<>(token, 1));
                    }
                }
            }
        }
```

In the preceding example, the `counter` variable is incremented for each word that the application processes.

After defining your mapping class, you then create an in-application stream that implements the map:

```
// Split up the lines in pairs (2-tuples) containing: (word,1), and
// group by the tuple field "0" and sum up tuple field "1"
DataStream<Tuple2<String, Integer>> wordCountStream = input.flatMap(new Tokenizer()).keyBy(0).sum(1);

// Serialize the tuple to string format, and publish the output to kinesis sink
wordCountStream.map(tuple -> tuple.toString()).addSink(createSinkFromStaticConfig());
```

For the complete code for this application, see
[Word Count Custom Metric Application](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/CustomMetrics/WordCount "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/CustomMetrics/WordCount").

## View custom metrics

Custom metrics for your application appear in the CloudWatch Metrics console in the **AWS/KinesisAnalytics** dashboard,
under the **Application** metric group.
