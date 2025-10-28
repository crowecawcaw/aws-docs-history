# Turn off step caching

A pipeline step does not rerun if you change any attributes that are not listed in [Default cache key attributes by pipeline step
type](pipelines-default-keys.md "pipelines-default-keys.md") for its step type.
However, you may decide that you want the pipeline step to rerun anyway. In this case, you
need to turn off step caching.

To turn off step caching, set the `Enabled` attribute in the step
definition’s `CacheConfig` property in the step definition to `false`,
as shown in the following code snippet:

```
{
    "CacheConfig": {
        "Enabled": false,
        "ExpireAfter": "<time>"
    }
}
```

Note that the `ExpireAfter` attribute is ignored when `Enabled` is
`false`.

To turn off caching for a pipeline step using the Amazon SageMaker Python SDK, define the pipeline
of your pipeline step, turn off the `enable_caching` property, and update the
pipeline.

Once you run it again, the following code example turns off caching for a training
step:

```
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.workflow.steps import CacheConfig
from sagemaker.workflow.pipeline import Pipeline

cache_config = CacheConfig(enable_caching=False, expire_after="PT1H")
estimator = Estimator(..., sagemaker_session=PipelineSession())

step_train = TrainingStep(
    name="TrainAbaloneModel",
    step_args=estimator.fit(inputs=inputs),
    cache_config=cache_config
)

# define pipeline
pipeline = Pipeline(
    steps=[step_train]
)

# update the pipeline
pipeline.update()
# or, call upsert() to update the pipeline
# pipeline.upsert()
```

Alternatively, turn off the `enable_caching` property after you have already
defined the pipeline, allowing one continuous code run. The following code sample
demonstrates this solution:

```
# turn off caching for the training step
pipeline.steps[0].cache_config.enable_caching = False

# update the pipeline
pipeline.update()
# or, call upsert() to update the pipeline
# pipeline.upsert()
```

For more detailed code examples and a discussion about how Python SDK parameters affect
caching, see [Caching Configuration](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#caching-configuration "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#caching-configuration") in the Amazon SageMaker Python SDK documentation.
