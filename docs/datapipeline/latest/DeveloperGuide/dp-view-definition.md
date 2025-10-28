AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Viewing Your Pipeline Definitions

Use the command line interface (CLI) to view your pipeline
definition. The CLI prints a
pipeline definition file, in JSON format. For information about the syntax and usage
of pipeline definition files, see [Pipeline definition file syntax](dp-writing-pipeline-definition.md "dp-writing-pipeline-definition.md").

When using the CLI, it's a good idea to retrieve the pipeline definition
before you submit modifications, because it's possible that another user or process
changed the pipeline definition after you last worked with it. By downloading a copy
of the current definition and using that as the basis for your modifications, you
can be sure that you are working with the most recent pipeline definition. It's also
a good idea to retrieve the pipeline definition again after you modify it, so that
you can ensure that the update was successful.

When using the CLI, you can get two different versions of your pipeline. The
`active` version is the pipeline that is currently running. The
`latest` version is a copy that's created when you edit a running
pipeline. When you upload the edited pipeline, it becomes the `active`
version and the previous `active` version is no longer available.

###### To get a pipeline definition using the AWS CLI

To get the complete pipeline definition, use the [get-pipeline-definition](../../../cli/latest/reference/datapipeline/get-pipeline-definition.md "../../../cli/latest/reference/datapipeline/get-pipeline-definition.md") command. The pipeline definition is printed
to standard output (stdout).

The following example gets the pipeline definition for the specified
pipeline.

```
`aws datapipeline get-pipeline-definition --pipeline-id `df-00627471SOVYZEXAMPLE``
```

To retrieve a specific version of a pipeline, use the `--version`
option. The following example retrieves the `active` version of the
specified pipeline.

```
`aws datapipeline get-pipeline-definition --version active --id `df-00627471SOVYZEXAMPLE``
```
