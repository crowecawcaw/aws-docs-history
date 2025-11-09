End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Elastic Transcoder Metrics and Dimensions

When you create a job, Elastic Transcoder sends the following metrics and dimensions to CloudWatch every
minute. You can use the following procedures
to view the metrics for Elastic Transcoder.

###### To view metrics using the CloudWatch console

Metrics are grouped first by the service namespace, and then by the various
dimension combinations within each namespace.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. If necessary, change the region. From the navigation bar, select the region where your
   AWS resources reside. For more information, see [Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
3. In the navigation pane, choose **Metrics**.
4. In the **CloudWatch Metrics by Category** pane, under the metrics
   category for Elastic Transcoder, select a metrics category, and then in the upper pane, scroll
   down to view the full list of metrics.

###### To view metrics using the AWS CLI

- At a command prompt, use the following command:

```
`aws cloudwatch list-metrics --namespace "`AWS/ElasticTranscoder`"`

```

CloudWatch displays the following metrics for Elastic Transcoder:

## Elastic Transcoder Dimensions and Metrics

The metrics and dimensions that Elastic Transcoder sends to Amazon CloudWatch are listed below.

### Elastic Transcoder Metrics

The `AWS/ElasticTranscoder` namespace includes the following metrics.

| Metric                | Description                                                                                                                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Billed HD Output`    | The number of billable seconds of HD output for a pipeline.<br>Valid Dimensions: PipelineId<br>Unit: Seconds                                                                             |
| `Billed SD Output`    | The number of billable seconds of SD output for a pipeline.<br>Valid Dimensions: PipelineId<br>Unit: Seconds                                                                             |
| `Billed Audio Output` | The number of billable seconds of audio output for a pipeline.<br>Valid Dimensions: PipelineId<br>Unit: Seconds                                                                          |
| `Jobs Completed`      | The number of jobs completed by this pipeline.<br>Valid Dimensions: PipelineId<br>Unit: Count                                                                                            |
| `Jobs Errored`        | The number of jobs that failed because of invalid inputs, such as a request to<br>transcode a file that is not in the given input bucket.<br>Valid Dimensions: PipelineId<br>Unit: Count |
| `Outputs per Job`     | The number of outputs Elastic Transcoder created for a job.<br>Valid Dimensions: PipelineId<br>Unit: Count                                                                               |
| `Standby Time`        | The number of seconds before Elastic Transcoder started transcoding a job.<br>Valid Dimensions: PipelineId<br>Unit: Seconds                                                              |
| `Errors`              | The number of errors caused by invalid operation parameters, such as a request for a job status that<br>does not include the job ID.<br>Valid Dimensions: Operation<br>Unit: Count       |
| `Throttles`           | The number of times that Elastic Transcoder automatically throttled an operation.<br>Valid Dimensions: Operation<br>Unit: Count                                                          |

### Dimensions for Elastic Transcoder Metrics

Elastic Transcoder metrics use the
Elastic Transcoder namespace and provide metrics for the following
dimension(s):

| Dimension    | Description                                                                                           |
| ------------ | ----------------------------------------------------------------------------------------------------- |
| `PipelineId` | The ID of a pipeline. This dimension filters the data you request for an Elastic Transcoder pipeline. |
| `Operation`  | This dimension filters the data you request for the APIs that Elastic Transcoder provides.            |
