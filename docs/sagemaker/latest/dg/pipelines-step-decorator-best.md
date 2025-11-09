# Best Practices

The following sections suggest best practices to follow when you use the `@step` decorator for
your pipeline steps.

## Use warm pools

For faster pipeline step runs, use the warm pooling functionality provided for training jobs.
You can turn on the warm pool functionality by providing the `keep_alive_period_in_seconds`
argument to the `@step` decorator as
demonstrated in the following snippet:

```
@step(
   keep_alive_period_in_seconds=900
)
```

For more information about warm pools, see [SageMaker AI Managed Warm Pools](train-warm-pools.md "train-warm-pools.md").

## Structure your directory

You are advised to use code modules while using the `@step` decorator. Put the `pipeline.py` module,
in which you invoke the step functions and define the pipeline, at the root of the workspace. The recommended structure
is shown as follows:

```
.
├── config.yaml # the configuration file that define the infra settings
├── requirements.txt # dependencies
├── pipeline.py  # invoke @step-decorated functions and define the pipeline here
├── steps/
| ├── processing.py
| ├── train.py
├── data/
├── test/
```
