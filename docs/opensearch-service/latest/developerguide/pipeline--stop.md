# Stopping an Amazon OpenSearch Ingestion pipeline

To use an OpenSearch Ingestion pipeline or perform administration, you always begin with an
active pipeline, then stop the pipeline, and then start the pipeline again. While your
pipeline is stopped, you're not charged for Ingestion OCU hours.

###### To stop a pipeline

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines "https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines"). You'll be on the Pipelines page.
2. Choose a pipeline. You can perform the stop operation from this page, or navigate to the
   details page for the pipeline that you want to stop.
3. For **Actions**, choose **Stop pipeline**.

If a pipeline can't be stopped and started, the **Stop pipeline** action
isn't available.
To stop a pipeline using the AWS CLI, call the [stop-pipeline](../../../cli/latest/reference/osis/stop-pipeline.md "../../../cli/latest/reference/osis/stop-pipeline.md") command
with the following parameters:

- `--pipeline-name` – the name of the pipeline.

###### Example

```
aws osis stop-pipeline --pipeline-name `my-pipeline`
```

To stop a pipeline using the OpenSearch Ingestion API, call the [StopPipeline](../APIReference/API_osis_StopPipeline.md "../APIReference/API_osis_StopPipeline.md") operation with the following parameter:

- `PipelineName` – the name of the pipeline.
