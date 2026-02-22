# Deleting Amazon OpenSearch Ingestion pipelines

You can delete an Amazon OpenSearch Ingestion pipeline using the AWS Management Console, the AWS CLI, or the
OpenSearch Ingestion API. You can't delete a pipeline when has a status of `Creating`
or `Updating`.

###### To delete a pipeline

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines "https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines"). You'll be on the Pipelines page.
2. Select the pipeline that you want to delete and choose
   **Actions**, **Delete**.
3. Confirm deletion and choose **Delete**.
   To delete a pipeline using the AWS CLI, send a [delete-pipeline](../../../cli/latest/reference/osis/delete-pipeline.md "../../../cli/latest/reference/osis/delete-pipeline.md")
   request:

```
aws osis delete-pipeline --pipeline-name "`my-pipeline`"
```

To delete an OpenSearch Ingestion pipeline using the OpenSearch Ingestion API, call the
[DeletePipeline](../APIReference/API_osis_DeletePipeline.md "../APIReference/API_osis_DeletePipeline.md") operation with the following parameter:

- `PipelineName` – the name of the pipeline.
