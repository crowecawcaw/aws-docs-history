

# Pipeline version aliases

Each time you update a pipeline definition, Pipelines creates a new pipeline version with a numeric version ID. A pipeline version alias is a name, such as `prod` or `staging`, that you assign to a version. You can then start executions from the alias instead of a version ID. To promote a new version, you move the alias to it, and callers that start executions from the alias don't need to change. Pipeline version aliases are available in the SageMaker Python SDK v3.30.0 or later.

Aliases follow these rules:
+ An alias contains 1-128 letters, numbers, periods (.), hyphens (-), and underscores (\_). It can't consist of numbers only.
+ An alias is unique within a pipeline. It points to one version at a time.
+ A version can have up to 10 aliases.

## Assign aliases
<a name="pipelines-version-aliases-assign"></a>

You can assign aliases when you create a version, or add them to an existing version.
+ **When you create the pipeline** – Pass `pipeline_version_aliases` to `create()`. The aliases are assigned to version 1.
+ **When you update the pipeline definition** – Pass `pipeline_version_aliases` to `update()` or `upsert()`. The aliases are assigned to the new version that the update creates. If you pass `pipeline_version_aliases` and the update doesn't change the pipeline definition, no new version is created and the request fails with a validation error.
+ **On an existing version** – Call `update_pipeline_version()` with `aliases_to_add` and `aliases_to_remove`. An alias can't appear in both lists. Adding an alias that the version already has, or removing one that it doesn't have, has no effect.

The following example creates a pipeline whose first version has the alias `prod`, and then updates the definition to create version 2 with the alias `staging`.

```python
from sagemaker.mlops.workflow import Pipeline

pipeline = Pipeline(
    name="MyPipeline",
    parameters=[instance_type],
    steps=[step_train],
)
pipeline.create(
    role_arn=role,
    pipeline_version_aliases=["prod"],
)

# Change the definition, then create version 2 with its own alias.
pipeline.steps = [step_process, step_train]
pipeline.update(
    role_arn=role,
    pipeline_version_aliases=["staging"],
)
```

## Move an alias to another version
<a name="pipelines-version-aliases-move"></a>

Because an alias points to one version at a time, you can't add an alias that another version of the same pipeline already has. To move an alias, first remove it from its current version, and then add it to the new version. The following example promotes version 2 to `prod`.

```python
pipeline.update_pipeline_version(
    pipeline_version_id=1,
    aliases_to_remove=["prod"],
)
pipeline.update_pipeline_version(
    pipeline_version_id=2,
    aliases_to_add=["prod"],
    aliases_to_remove=["staging"],
)
```

Between the two calls, no version has the alias, so a request that uses `prod` fails with a `ResourceNotFound` error. Run the two calls back to back, and retry failed starts in callers that use the alias.

## Use an alias
<a name="pipelines-version-aliases-use"></a>

Pass `pipeline_version_alias` instead of `pipeline_version_id` to start an execution or describe a version. You can't specify both. If no version of the pipeline has the alias, the request fails with a `ResourceNotFound` error.

```python
execution = pipeline.start(
    pipeline_version_alias="prod",
    parameters={"InstanceType": "ml.m5.xlarge"},
)

version = pipeline.describe(pipeline_version_alias="prod")
print(version["PipelineVersionAliases"])
```

To list only the executions of the version that has an alias, pass `PipelineVersionAlias` to the `ListPipelineExecutions` API. The filter uses the version that has the alias when you make the request.

```python
import boto3

sm = boto3.client("sagemaker")
response = sm.list_pipeline_executions(
    PipelineName="MyPipeline",
    PipelineVersionAlias="prod",
)
```

## View aliases
<a name="pipelines-version-aliases-view"></a>

The following APIs return the aliases of a version in `PipelineVersionAliases`:
+ `DescribePipeline` and `ListPipelineVersions` return the aliases of each version.
+ `DescribePipelineExecution` and `ListPipelineExecutions` return the aliases of the version that the execution ran.

**Note**  
Execution responses show the aliases that the version has now, not the aliases it had when the execution started. If you moved `prod` after an execution ran, that execution no longer shows `prod`. To find which version an execution ran, use the `PipelineVersionId` that `DescribePipelineExecution` returns.