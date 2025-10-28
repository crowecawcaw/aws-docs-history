AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Cloning Your Pipeline

Cloning makes a copy of a pipeline and allows you to specify a name for the new
pipeline. You can clone a pipeline that is in any state, even if it has errors; however,
the new pipeline remains in the `PENDING` state until you manually activate
it. For the new pipeline, the clone operation uses the latest version of the original
pipeline definition rather than the active version. In the clone operation, the full
schedule from the original pipeline is not copied into the new pipeline, only the period
setting.

###### To clone a pipeline using the AWS CLI:

1. Create a new pipeline with a new name and unique ID. Note the returned pipeline ID.
2. Use the `get-pipeline-definition` CLI to get the pipeline definition of the existing pipeline to be cloned and write it to a temporary file. Note the absolute path of the file.
3. Use the `put-pipeline-definition` CLI to copy the pipeline definition from the existing pipeline to the new pipeline.
4. Use the `get-pipeline-definition` CLI to get the definition of the new pipeline to verify the pipeline definition.

```
# Create Pipeline (returns <new-pipeline-id>)
aws datapipeline create-pipeline --name my-cloned-pipeline --unique-id my-cloned-pipeline --region ap-northeast-1

#Get pipeline definition of existing pipeline
aws datapipeline get-pipeline-definition --pipeline-id <existing-pipeline-id> --region ap-northeast-1 > existing_pipeline_definition.json

# Put pipeline definition to new pipeline
aws datapipeline put-pipeline-definition --pipeline-id <new-pipeline-id> --region ap-northeast-1 --pipeline-definition file://<absolute_path_to_existing_pipeline_definition.json>

# get pipeline definition of new pipeline
aws datapipeline get-pipeline-definition --pipeline-id <new-pipeline-id> --region ap-northeast-1

```
