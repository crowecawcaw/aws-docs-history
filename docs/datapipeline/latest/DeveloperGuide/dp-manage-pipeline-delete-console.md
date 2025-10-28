AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Deleting Your Pipeline

When you no longer require a pipeline, such as a pipeline created during application
testing, you should delete it to remove it from active use. Deleting a pipeline puts it
into a deleting state. When the pipeline is in the deleted state, its pipeline
definition and run history are gone. Therefore, you can no longer perform operations on
the pipeline, including describing it.

###### Important

You can't restore a pipeline after you delete it, so be sure that you won't need
the pipeline in the future before you delete it.

###### To delete a pipeline using the AWS CLI

To delete a pipeline, use the [delete-pipeline](../../../cli/latest/reference/datapipeline/delete-pipeline.md "../../../cli/latest/reference/datapipeline/delete-pipeline.md")
command. The following command deletes the specified pipeline.

```
`aws datapipeline delete-pipeline --pipeline-id `df-00627471SOVYZEXAMPLE``
```
