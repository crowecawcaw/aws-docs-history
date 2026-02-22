# Starting an Amazon OpenSearch Ingestion pipeline

You always start an OpenSearch Ingestion pipeline beginning with a pipeline that's already in the
stopped state. The pipeline keeps its configuration settings such as capacity limits,
network settings, and log publishing options.

Restarting a pipeline usually takes several minutes.

###### To start a pipeline

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines "https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines"). You'll be on the Pipelines page.
2. Choose a pipeline. You can perform the start operation from this page, or
   navigate to the details page for the pipeline that you want to start.
3. For **Actions**, choose **Start pipeline**.
   To start a pipeline by using the AWS CLI, call the [start-pipeline](../../../cli/latest/reference/osis/start-pipeline.md "../../../cli/latest/reference/osis/start-pipeline.md") command
   with the following parameters:

- `--pipeline-name` – the name of the pipeline.

###### Example

```
aws osis start-pipeline --pipeline-name `my-pipeline`
```

To start an OpenSearch Ingestion pipeline using the OpenSearch Ingestion API, call the [StartPipeline](../APIReference/API_osis_StartPipeline.md "../APIReference/API_osis_StartPipeline.md") operation with the following parameter:

- `PipelineName` – the name of the pipeline.
