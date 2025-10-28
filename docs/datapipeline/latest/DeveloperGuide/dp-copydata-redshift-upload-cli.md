AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Upload and Activate the Pipeline Definition

You must upload your pipeline definition and activate your pipeline.
In the following example commands, replace `pipeline_name` with a label for your pipeline and
`pipeline_file` with the fully-qualified path for the pipeline definition `.json` file.

**AWS CLI**

To create your pipeline definition and activate your pipeline, use the following
[create-pipeline](../../../cli/latest/reference/datapipeline/create-pipeline.md "../../../cli/latest/reference/datapipeline/create-pipeline.md") command.
Note the ID of your pipeline, because you'll use this value with most CLI commands.

```
`aws datapipeline create-pipeline --name `pipeline_name` --unique-id `token``
{
    "pipelineId": "df-00627471SOVYZEXAMPLE"
}
```

To upload your pipeline definition, use the following
[put-pipeline-definition](../../../cli/latest/reference/datapipeline/put-pipeline-definition.md "../../../cli/latest/reference/datapipeline/put-pipeline-definition.md") command.

```
`aws datapipeline put-pipeline-definition --pipeline-id df-00627471SOVYZEXAMPLE --pipeline-definition file://MyEmrPipelineDefinition.json`
```

If you pipeline validates successfully, the `validationErrors` field is empty. You should review any warnings.

To activate your pipeline, use the following [activate-pipeline](../../../cli/latest/reference/datapipeline/activate-pipeline.md "../../../cli/latest/reference/datapipeline/activate-pipeline.md") command.

```
`aws datapipeline activate-pipeline --pipeline-id df-00627471SOVYZEXAMPLE`
```

You can verify that your pipeline appears in the pipeline list using the following [list-pipelines](../../../cli/latest/reference/datapipeline/list-pipelines.md "../../../cli/latest/reference/datapipeline/list-pipelines.md") command.

```
`aws datapipeline list-pipelines`
```
