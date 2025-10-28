# Turn on step caching

To turn on step caching, you must add a `CacheConfig` property to the step
definition. `CacheConfig` properties use the following format in the pipeline
definition file:

```
{
    "CacheConfig": {
        "Enabled": false,
        "ExpireAfter": "<time>"
    }
}
```

The `Enabled` field indicates whether caching is turned on for the particular
step. You can set the field to `true`, which tells SageMaker AI to try to find a previous
run of the step with the same attributes. Or, you can set the field to `false`,
which tells SageMaker AI to run the step every time the pipeline runs. `ExpireAfter` is a
string in [ISO 8601
duration](https://en.wikipedia.org/wiki/ISO_8601#Durations "https://en.wikipedia.org/wiki/ISO_8601#Durations") format that defines the timeout period. The `ExpireAfter` duration can be a
year, month, week, day, hour, or minute value. Each value consists of a number followed by a
letter indicating the unit of duration. For example:

- "30d" = 30 days
- "5y" = 5 years
- "T16m" = 16 minutes
- "30dT5h" = 30 days and 5 hours.
  The following discussion describes the procedure to turn on caching for new or
  pre-existing pipelines using the Amazon SageMaker Python SDK.

**Turn on caching for new pipelines**

For new pipelines, initialize a `CacheConfig` instance with
`enable_caching=True` and provide it as an input to your pipeline step. The
following example turns on caching with a 1-hour timeout period for a training step:

```
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.workflow.steps import CacheConfig

cache_config = CacheConfig(enable_caching=True, expire_after="PT1H")
estimator = Estimator(..., sagemaker_session=PipelineSession())

step_train = TrainingStep(
    name="TrainAbaloneModel",
    step_args=estimator.fit(inputs=inputs),
    cache_config=cache_config
)
```

**Turn on caching for pre-existing pipelines**

To turn on caching for pre-existing, already-defined pipelines, turn on the
`enable_caching` property for the step, and set `expire_after` to a
timeout value. Lastly, update the pipeline with `pipeline.upsert()` or
`pipeline.update()`. Once you run it again, the following code example turns on
caching with a 1-hour timeout period for a training step:

```
from sagemaker.workflow.pipeline_context import PipelineSession
from sagemaker.workflow.steps import CacheConfig
from sagemaker.workflow.pipeline import Pipeline

cache_config = CacheConfig(enable_caching=True, expire_after="PT1H")
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

# additional step for existing pipelines
pipeline.update()
# or, call upsert() to update the pipeline
# pipeline.upsert()
```

Alternatively, update the cache config after you have already defined the (pre-existing)
pipeline, allowing one continuous code run. The following code sample demonstrates this
method:

```
# turn on caching with timeout period of one hour
pipeline.steps[0].cache_config.enable_caching = True
pipeline.steps[0].cache_config.expire_after = "PT1H"

# additional step for existing pipelines
pipeline.update()
# or, call upsert() to update the pipeline
# pipeline.upsert()
```

For more detailed code examples and a discussion about how Python SDK parameters affect
caching, see [Caching Configuration](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#caching-configuration "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#caching-configuration") in the Amazon SageMaker Python SDK documentation.
