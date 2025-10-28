# Configure data input mode using the

SageMaker Python SDK

SageMaker Python SDK provides the generic [Estimator class](https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.estimator.Estimator "https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.estimator.Estimator") and its [variations for ML
frameworks](https://sagemaker.readthedocs.io/en/stable/frameworks/index.html "https://sagemaker.readthedocs.io/en/stable/frameworks/index.html") for launching training jobs. You can specify one of the data input modes
while configuring the SageMaker AI `Estimator` class or the `Estimator.fit`
method. The following code templates show the two ways to specify input modes.

**To specify the input mode using the Estimator
class**

```
from sagemaker.`estimator` import `Estimator`
from sagemaker.inputs import TrainingInput

estimator = Estimator(
    checkpoint_s3_uri='`s3://amzn-s3-demo-bucket/checkpoint-destination/`',
    output_path='`s3://amzn-s3-demo-bucket/output-path/`',
    base_job_name='`job-name`',
    input_mode='`File`'  # Available options: File | Pipe | FastFile
    ...
)

# Run the training job
estimator.fit(
    inputs=TrainingInput(s3_data="`s3://amzn-s3-demo-bucket/my-data/train`")
)
```

For more information, see the [sagemaker.estimator.Estimator](https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.estimator.Estimator "https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.estimator.Estimator") class in the _SageMaker Python SDK
documentation_.

**To specify the input mode through the `estimator.fit()`
method**

```
from sagemaker.`estimator` import `Estimator`
from sagemaker.inputs import TrainingInput

estimator = Estimator(
    checkpoint_s3_uri='`s3://amzn-s3-demo-bucket/checkpoint-destination/`',
    output_path='`s3://amzn-s3-demo-bucket/output-path/`',
    base_job_name='`job-name`',
    ...
)

# Run the training job
estimator.fit(
    inputs=TrainingInput(
        s3_data="`s3://amzn-s3-demo-bucket/my-data/train`",
        input_mode='`File`'  # Available options: File | Pipe | FastFile
    )
)
```

For more information, see the [sagemaker.estimator.Estimator.fit](https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.estimator.Estimator.fit "https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.estimator.Estimator.fit") class method and the [sagemaker.inputs.TrainingInput](https://sagemaker.readthedocs.io/en/stable/api/utility/inputs.html#sagemaker.inputs.TrainingInput "https://sagemaker.readthedocs.io/en/stable/api/utility/inputs.html#sagemaker.inputs.TrainingInput") class in the _SageMaker Python SDK
documentation_.

###### Tip

To learn more about how to configure Amazon FSx for Lustre or Amazon EFS with your VPC
configuration using the SageMaker Python SDK estimators, see [Use File Systems as Training Inputs](https://sagemaker.readthedocs.io/en/stable/overview.html?highlight=VPC#use-file-systems-as-training-inputs "https://sagemaker.readthedocs.io/en/stable/overview.html?highlight=VPC#use-file-systems-as-training-inputs") in the _SageMaker AI Python
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
see [How Amazon SageMaker AI Provides
Training Information](your-algorithms-training-algo-running-container.md "your-algorithms-training-algo-running-container.md"), the [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md") API, and the `TrainingInputMode` in
[`AlgorithmSpecification`](../APIReference/API_AlgorithmSpecification.md "../APIReference/API_AlgorithmSpecification.md").
