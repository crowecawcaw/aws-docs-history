# Use an Algorithm to Run a Training Job

You can create use an algorithm resource to create a training job by using
the Amazon SageMaker AI console, the low-level Amazon SageMaker API, or the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

###### Topics

- [Use an Algorithm to Run a
  Training Job (Console)](#sagemaker-mkt-algo-train-console "#sagemaker-mkt-algo-train-console")
- [Use an Algorithm to Run a
  Training Job (API)](#sagemaker-mkt-algo-train-api "#sagemaker-mkt-algo-train-api")
- [Use an Algorithm to Run a
  Training Job (Amazon SageMaker Python SDK)](#sagemaker-mkt-algo-train-sdk "#sagemaker-mkt-algo-train-sdk")

## Use an Algorithm to Run a

Training Job (Console)

###### To use an algorithm to run a training job (console)

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **Algorithms**.
3. Choose an algorithm that you created from the list on the **My
   algorithms** tab or choose an algorithm that you subscribed
   to on the **AWS Marketplace subscriptions** tab.
4. Choose **Create training job**.

The algorithm you chose will automatically be selected. 5. On the **Create training job** page, provide the
following information:

    1. For **Job name**, type a name for the
     training job.
    2. For **IAM role**, choose an IAM role that
     has the required permissions to run training jobs in SageMaker AI, or
     choose **Create a new role** to allow SageMaker AI to
     create a role that has the
     `AmazonSageMakerFullAccess` managed policy
     attached. For information, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").
    3. For **Resource configuration**, provide the
     following information:


    	1. For **Instance type**, choose the
    	 instance type to use for training.
    	2. For **Instance count**, type the
    	 number of ML instances to use for the training
    	 job.
    	3. For **Additional volume per instance
    	 (GB)**, type the size of the ML storage
    	 volume that you want to provision. ML storage volumes
    	 store model artifacts and incremental states.
    	4. For **Encryption key**, if you want
    	 Amazon SageMaker AI to use an AWS Key Management Service
    	 key to encrypt data in the ML storage volume attached to
    	 the training instance, specify the key.
    	5. For **Stopping condition**, specify
    	 the maximum amount of time in seconds, minutes, hours,
    	 or days, that you want the training job to run.
    4. For **VPC**, choose a Amazon VPC that you want to
     allow your training container to access. For more information,
     see [Give SageMaker AI Training Jobs Access to Resources in Your
     Amazon VPC](train-vpc.md "train-vpc.md").
    5. For **Hyperparameters**, specify the values
     of the hyperparameters to use for the training job.
    6. For **Input data configuration**, specify the
     following values for each channel of input data to use for the
     training job. You can see what channels the algorithm you're
     using for training support, and the content type, supported
     compression type, and supported input modes for each channel,
     under **Channel specification** section of the
     **Algorithm summary** page for the
     algorithm.


    	1. For **Channel name**, type the name
    	 of the input channel.
    	2. For **Content type**, type the
    	 content type of the data that the algorithm expects for
    	 the channel.
    	3. For **Compression type**, choose the
    	 data compression type to use, if any.
    	4. For **Record wrapper**, choose
    	 `RecordIO` if the algorithm expects data
    	 in the `RecordIO` format.
    	5. For **S3 data type**, **S3
    	 data distribution type**, and **S3
    	 location**, specify the appropriate values.
    	 For information about what these values mean, see [`S3DataSource`](../APIReference/API_S3DataSource.md "../APIReference/API_S3DataSource.md").
    	6. For **Input mode**, choose
    	 **File** to download the data from
    	 to the provisioned ML storage volume, and mount the
    	 directory to a Docker volume. Choose
    	 **Pipe**To stream data directly
    	 from Amazon S3 to the container.
    	7. To add another input channel, choose **Add
    	 channel**. If you are finished adding input
    	 channels, choose **Done**.
    7. For **Output** location, specify the
     following values:


    	1. For **S3 output path**, choose the S3
    	 location where the training job stores output, such as
    	 model artifacts.


    	###### Note

    	You use the model artifacts stored at this
    	 location to create a model or model package from
    	 this training job.
    	2. For **Encryption key**, if you want
    	 SageMaker AI to use a AWS KMS key to encrypt output data at rest
    	 in the S3 location.
    8. For **Tags**, specify one or more tags to
     manage the training job. Each tag consists of a key and an
     optional value. Tag keys must be unique per resource.
    9. Choose **Create training job** to run the
     training job.

## Use an Algorithm to Run a

Training Job (API)

To use an algorithm to run a training job by using the SageMaker API, specify
either the name or the Amazon Resource Name (ARN) as the
`AlgorithmName` field of the [`AlgorithmSpecification`](../APIReference/API_AlgorithmSpecification.md "../APIReference/API_AlgorithmSpecification.md") object that you pass to [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md"). For
information about training models in SageMaker AI, see [Train a Model with Amazon SageMaker](how-it-works-training.md "how-it-works-training.md").

## Use an Algorithm to Run a

Training Job ([Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable"))

Use an algorithm that you created or subscribed to on AWS Marketplace to create a
training job, create an `AlgorithmEstimator` object and specify
either the Amazon Resource Name (ARN) or the name of the algorithm as the value
of the `algorithm_arn` argument. Then call the `fit`
method of the estimator. For example:

```
from sagemaker import AlgorithmEstimator
data_path = os.path.join(DATA_DIR, 'marketplace', 'training')

algo = AlgorithmEstimator(
algorithm_arn='arn:aws:sagemaker:us-east-2:012345678901:algorithm/my-algorithm',
        role='SageMakerRole',
        instance_count=1,
        instance_type='ml.c4.xlarge',
        sagemaker_session=sagemaker_session,
        base_job_name='test-marketplace')

train_input = algo.sagemaker_session.upload_data(
path=data_path, key_prefix='integ-test-data/marketplace/train')

algo.fit({'training': train_input})
```
