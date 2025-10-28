AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Editing Your Pipeline

To change some aspect of one of your pipelines, you can update its pipeline
definition. After you change a pipeline that is running, you must re-activate the
pipeline for your changes to take effect. In addition, you can re-run one or more
pipeline components.

###### Contents

- [Limitations](#dp-edit-pipeline-limits "#dp-edit-pipeline-limits")
- [Editing a Pipeline Using the AWS CLI](#dp-edit-pipeline-aws-cli "#dp-edit-pipeline-aws-cli")

## Limitations

While the pipeline is in the `PENDING` state and is not activated, you
can't make any changes to it. After you activate a pipeline, you can edit the pipeline
with the following restrictions. The changes you make apply to new runs of the
pipeline objects after you save them and then activate the pipeline again.

- You can't remove an object
- You can't change the schedule period of an existing object
- You can't add, delete, or modify reference fields in an existing
  object
- You can't reference an existing object in an output field of a new
  object
- You can't change the scheduled start date of an object (instead, activate
  the pipeline with a specific date and time)

## Editing a Pipeline Using the AWS CLI

You can edit a pipeline using the command line tools.

First, download a copy of the current pipeline definition using the [get-pipeline-definition](../../../cli/latest/reference/datapipeline/get-pipeline-definition.md "../../../cli/latest/reference/datapipeline/get-pipeline-definition.md") command. By doing this, you can be sure that
you are modifying the most recent pipeline definition. The following example uses
prints the pipeline definition to standard output (stdout).

```
`aws datapipeline get-pipeline-definition --pipeline-id `df-00627471SOVYZEXAMPLE``
```

Save the pipeline definition to a file and edit it as needed. Update your pipeline
definition using the [put-pipeline-definition](../../../cli/latest/reference/datapipeline/put-pipeline-definition.md "../../../cli/latest/reference/datapipeline/put-pipeline-definition.md") command. The following example uploads the
updated pipeline definition file.

```
`aws datapipeline put-pipeline-definition --pipeline-id `df-00627471SOVYZEXAMPLE` --pipeline-definition `file://MyEmrPipelineDefinition.json``
```

You can retrieve the pipeline definition again using the
`get-pipeline-definition` command to ensure that the update was
successful. To activate the pipeline, use the following [activate-pipeline](../../../cli/latest/reference/datapipeline/activate-pipeline.md "../../../cli/latest/reference/datapipeline/activate-pipeline.md")
command:

```
`aws datapipeline activate-pipeline --pipeline-id `df-00627471SOVYZEXAMPLE``
```

If you prefer, you can activate the pipeline from a specific date and time, using
the `--start-timestamp` option as follows:

```
`aws datapipeline activate-pipeline --pipeline-id `df-00627471SOVYZEXAMPLE` --start-timestamp `YYYY`-`MM`-`DD`T`HH`:`MM`:`SS`Z`
```

To re-run one or more pipeline components, use the [set-status](../../../cli/latest/reference/datapipeline/set-status.md "../../../cli/latest/reference/datapipeline/set-status.md")
command.
