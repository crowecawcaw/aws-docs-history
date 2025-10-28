# Troubleshooting metric streams in CloudWatch

If you're not seeing metric data at your final destination, check the
following:

- Check that the metric stream is in the running state. For steps on
  how to use the CloudWatch console to do this, see
  [Metric stream
  operation and maintenance](CloudWatch-metric-streams-operation.md "CloudWatch-metric-streams-operation.md").
- Metrics published more than two days in the past are not streamed. To determine
  whether a particular metric will be streamed, graph the metric in the CloudWatch console and check how old
  the last visible datapoint is. If it is more than two days in the past, then
  it won't be picked up by metric streams.
- Check the metrics emitted by the metric stream. In the
  CloudWatch console, under **Metrics**, look at the **AWS/CloudWatch/MetricStreams** namespace for the **MetricUpdate**, **TotalMetricUpdate**, and
  **PublishErrorRate** metrics.
- If the **PublishErrorRate** metric is high,
  confirm that the destination that is used by the Firehose delivery stream exists and that the
  IAM role specified in the metric stream's configuration grants the `CloudWatch`
  service principal permissions to write to it. For more information,
  see [Trust between CloudWatch and Firehose](CloudWatch-metric-streams-trustpolicy.md "CloudWatch-metric-streams-trustpolicy.md").
- Check that the Firehose delivery stream has permission to write to the final
  destination.
- In the Firehose console, view the Firehose delivery stream that is used for the
  metric stream and check the **Monitoring** tab to see whether
  the Firehose delivery stream is receiving data.
- Confirm that you have configured your Firehose delivery stream with
  the correct details.
- Check any available logs or metrics for the final destination
  that the Firehose delivery stream writes to.
- To get more detailed information, enable CloudWatch Logs error logging on
  the Firehose delivery stream. For more information, see
  [Monitoring Amazon Data Firehose Using CloudWatch Logs](../../../firehose/latest/dev/monitoring-with-cloudwatch-logs.md "../../../firehose/latest/dev/monitoring-with-cloudwatch-logs.md").

###### Note

After a data point for a specific metric and timestamp has been sent, it won’t be sent again even if the value of the data point changes later.
