

# Best Practices
<a name="pipelines-step-decorator-best"></a>

The following sections suggest best practices to follow when you use the `@step` decorator for your pipeline steps.

## Use warm pools
<a name="pipelines-step-decorator-best-warmpool"></a>

For faster pipeline step runs, use the warm pooling functionality provided for training jobs. You can turn on the warm pool functionality by providing the `keep_alive_period_in_seconds` argument to the `@step` decorator as demonstrated in the following snippet:

```
@step(
   keep_alive_period_in_seconds=900
)
```

For more information about warm pools, see [SageMaker AI Managed Warm Pools](train-warm-pools.md). 

## Structure your directory
<a name="pipelines-step-decorator-best-dir"></a>

You are advised to use code modules while using the `@step` decorator. Put the `pipeline.py` module, in which you invoke the step functions and define the pipeline, at the root of the workspace. The recommended structure is shown as follows:

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

## Secure your serialized data
<a name="pipelines-step-decorator-best-secure-data"></a>

The `@step` decorator saves function inputs and outputs to Amazon S3. By default, SageMaker AI uses the default bucket. Other projects or users in your account might share this bucket.

To keep your pipeline data safe, set `S3RootUri` in your SageMaker AI configuration file. Use a bucket that only your pipeline uses. The following example shows how to set this value:

```
SchemaVersion: '1.0'
SageMaker:
  PythonSDK:
    Modules:
      RemoteFunction:
        S3RootUri: '{{s3://amzn-s3-demo-bucket/pipeline-data}}'
```

**Important**  
Restrict write access to the `S3RootUri` path. This prevents unauthorized users from modifying your pipeline data. Apply a bucket policy so that only the SageMaker AI execution role used by your jobs can write to this path.

For more information about the configuration file, see [Configuration file](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-decorator-config.html).