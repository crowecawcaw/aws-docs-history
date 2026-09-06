

# Use Quick Amazon S3 setup
<a name="CloudWatch-metric-streams-setup-Quick-S3"></a>

The **Quick S3 Setup** method works well if you want to quickly set up a stream to Amazon S3 and you don't need any formatting transformation beyond the supported JSON, OpenTelemetry 1.0.0, and OpenTelemetry 0.7.0 formats. CloudWatch will create all necessary resources including the Firehose delivery stream and the necessary IAM roles. The default format for this option is JSON, but you can change the format while you set up the stream.

Alternatively, if you want the final format to be Parquet format or Optimized Row Columnar (ORC), you should instead follow the steps in [Custom setup with Firehose](CloudWatch-metric-streams-setup-datalake.md).

## CloudWatch console
<a name="CloudWatch-metric-streams-setup-quick-S3-console"></a>

This section describes how to use the CloudWatch console to set up a metric stream Amazon S3 using Quick S3 setup.

**To set up a metric stream using Quick S3 setup**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**, **Streams**. Then choose **Create metric stream**.

1. (Optional) If you are signed in to an account that is set up as a monitoring account in CloudWatch cross-account observability, you can choose whether to include metrics from linked source accounts in this metric stream. To include metrics from source accounts, choose **Include source account metrics**.

1. Choose **Quick S3 setup**. CloudWatch will create all necessary resources including the Firehose delivery stream and the necessary IAM roles. The default format for this option is JSON, but you can change the format later in this procedure.

1. (Optional) Choose **Select existing resources** to use an existing S3 bucket or existing IAM roles instead of having CloudWatch create new ones for you.

1. (Optional) To change the output format from the default format for your scenario, choose **Change output format**. The supported formats are JSON, OpenTelemetry 1.0.0, and OpenTelemetry 0.7.0.

1. For **Metrics to be streamed**, choose either **All metrics** or **Select metrics**.

   If you choose **All metrics**, all metrics from this account will be included in the stream.

   Consider carefully whether to stream all metrics, because the more metrics that you stream the higher your metric stream charges will be.

   If you choose **Select metrics**, do one of the following:
   + To stream most metric namespaces, choose **Exclude** and select the namespaces or metrics to exclude. When you specify a namespace in **Exclude**, you can optionally select some specific metrics from that namespace to exclude. If you choose to exclude a namespace but don't then select metrics in that namespace, all metrics from that namespace are excluded.
   + To include only a few metric namespaces or metrics in the metric stream, choose **Include** and then select the namespaces or metrics to include. If you choose to include a namespace but don't then select metrics in that namespace, all metrics from that namespace are included.

1. (Optional) To stream additional statistics for some of these metrics beyond Minimum, Maximum, SampleCount, and Sum, choose **Add additional statistics**. Either choose **Add recommended metrics** to add some commonly used statistics, or manually select the namespace and metric name to stream additional statistics for. Next, select the additional statistics to stream.

   To then choose another group of metrics to stream a different set of additional statistics for, choose **Add additional statistics**. Each metric can include as many as 20 additional statistics, and as many as 100 metrics within a metric stream can include additional statistics.

   Streaming additional statistics incurs more charges. For more information, see [Statistics that can be streamed](CloudWatch-metric-streams-statistics.md).

   For definitions of the additional statistics, see [CloudWatch statistics definitions](Statistics-definitions.md).

1. (Optional) Customize the name of the new metric stream under **Metric stream name**.

1. Choose **Create metric stream**.