# Configure data input mode using the SageMaker Python SDK

SageMaker Python SDK provides the generic [ModelTrainer class](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html") and its [variations for ML
frameworks](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/") for launching training jobs. You can specify one of the data input modes
while configuring the SageMaker AI `ModelTrainer` class or the `ModelTrainer.train`
method. The following code templates show the two ways to specify input modes.

**To specify the input mode using the ModelTrainer class**

```
from sagemaker.`train` import `ModelTrainer`
from sagemaker.train.configs import InputData, OutputDataConfig, CheckpointConfig

model_trainer = ModelTrainer(
    checkpoint_config=CheckpointConfig(s3_uri='`s3://amzn-s3-demo-bucket/checkpoint-destination/`'),
    output_data_config=OutputDataConfig(s3_output_path='`s3://amzn-s3-demo-bucket/output-path/`'),
    base_job_name='`job-name`',
    training_input_mode='`File`'  # Available options: File | Pipe | FastFile
    ...
)

# Run the training job
model_trainer.train(
    input_data_config=[InputData(channel_name="training", data_source="`s3://amzn-s3-demo-bucket/my-data/train`")]
)
```

For more information, see the [sagemaker.train.ModelTrainer](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html") class in the _SageMaker Python SDK
documentation_.

**To specify the input mode through the `model_trainer.train()`
method**

```
from sagemaker.`train` import `ModelTrainer`
from sagemaker.train.configs import InputData, OutputDataConfig, CheckpointConfig
from sagemaker.core.shapes import Channel, DataSource, S3DataSource

model_trainer = ModelTrainer(
    checkpoint_config=CheckpointConfig(s3_uri='`s3://amzn-s3-demo-bucket/checkpoint-destination/`'),
    output_data_config=OutputDataConfig(s3_output_path='`s3://amzn-s3-demo-bucket/output-path/`'),
    base_job_name='`job-name`',
    ...
)

# Run the training job with per-channel input mode using Channel
model_trainer.train(
    input_data_config=[Channel(
        channel_name="training",
        data_source=DataSource(
            s3_data_source=S3DataSource(s3_data_type="S3Prefix", s3_uri="`s3://amzn-s3-demo-bucket/my-data/train`")
        ),
        input_mode="`File`",  # Per-channel override: File | Pipe | FastFile
    )]
)
```

For more information, see the [sagemaker.train.ModelTrainer.train](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html") class method and the [sagemaker.train.configs.InputData](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html "https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html") class in the _SageMaker Python SDK
documentation_.

###### Tip

To learn more about how to configure Amazon FSx for Lustre or Amazon EFS with your VPC
configuration using the SageMaker Python SDK ModelTrainers, see [Use File Systems as Training Inputs](https://sagemaker.readthedocs.io/en/stable/ "https://sagemaker.readthedocs.io/en/stable/") in the _SageMaker AI Python
SDK documentation_.

###### Tip

The data input mode integrations with Amazon S3, Amazon EFS, and FSx for Lustre are recommended ways
to optimally configure data source for the best practices. You can strategically improve
data loading performance using the SageMaker AI managed storage options and input modes, but it's
not strictly constrained. You can write your own data reading logic directly in your
training container. For example, you can set to read from a different data source, write
your own S3 data loader class, or use third-party frameworks' data loading functions within
your training script. However, you must make sure that you specify the right paths that SageMaker AI
can recognize.

###### Tip

If you use a custom training container, make sure you install the [SageMaker training toolkit](https://github.com/aws/sagemaker-training-toolkit "https://github.com/aws/sagemaker-training-toolkit") that
helps set up the environment for SageMaker training jobs. Otherwise, you must specify the
environment variables explicitly in your Dockerfile. For more information, see [Create a
container with your own algorithms and models](docker-containers-create.md "docker-containers-create.md").

For more information about how to set the data input modes using the low-level SageMaker APIs,
see [How Amazon SageMaker AI Provides Training Information](your-algorithms-training-algo-running-container.md "your-algorithms-training-algo-running-container.md"), the [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") API, and the `TrainingInputMode` in
[`AlgorithmSpecification`](../APIReference/API_AlgorithmSpecification.md "../APIReference/API_AlgorithmSpecification.md").
