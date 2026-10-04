

# Managed Spot Training in Amazon SageMaker AI
<a name="model-managed-spot-training"></a>

Amazon SageMaker AI makes it easy to train machine learning models using managed Amazon EC2 Spot instances. Managed spot training can optimize the cost of training models up to 90% over on-demand instances. SageMaker AI manages the Spot interruptions on your behalf. 

Managed Spot Training uses Amazon EC2 Spot instance to run training jobs instead of on-demand instances. You can specify which training jobs use spot instances and a stopping condition that specifies how long SageMaker AI waits for a job to run using Amazon EC2 Spot instances. Metrics and logs generated during training runs are available in CloudWatch. 

Amazon SageMaker AI automatic model tuning, also known as hyperparameter tuning, can use managed spot training. For more information on automatic model tuning, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md).

Spot instances can be interrupted, causing jobs to take longer to start or finish. You can configure your managed spot training job to use checkpoints. SageMaker AI copies checkpoint data from a local path to Amazon S3. When the job is restarted, SageMaker AI copies the data from Amazon S3 back into the local path. The training job can then resume from the last checkpoint instead of restarting. For more information about checkpointing, see [Checkpoints in Amazon SageMaker AI](model-checkpoints.md).

**Note**  
Unless your training job will complete quickly, we recommend you use checkpointing with managed spot training. SageMaker AI built-in algorithms and marketplace algorithms that do not checkpoint are currently limited to a `MaxWaitTimeInSeconds` of 3600 seconds (60 minutes). 

To use managed spot training, create a training job. Set `EnableManagedSpotTraining` to `True` and specify the `MaxWaitTimeInSeconds`. `MaxWaitTimeInSeconds` must be larger than `MaxRuntimeInSeconds`. For more information about creating a training job, see [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html). 

You can calculate the savings from using managed spot training using the formula `(1 - (BillableTimeInSeconds / TrainingTimeInSeconds)) * 100`. For example, if `BillableTimeInSeconds` is 100 and `TrainingTimeInSeconds` is 500, this means that your training job ran for 500 seconds, but you were billed for only 100 seconds. Your savings is (1 - (100 / 500)) \* 100 = 80%.

`TrainingTimeInSeconds` is the compute time that was retained as productive training time. It includes the first image download and each training interval, but excludes intervals that were lost to a Spot interruption within their first hour of runtime, as well as time spent re-provisioning instances or waiting for Spot capacity after an interruption. `BillableTimeInSeconds` is the amount of time that you are billed for. For managed spot training, it is the Spot cost of those productive intervals expressed as the equivalent number of seconds at the Amazon SageMaker AI on-demand price for the instance. Because the Amazon SageMaker AI Spot price is a discount off the Amazon SageMaker AI on-demand price, `BillableTimeInSeconds` is lower than `TrainingTimeInSeconds`, and the formula gives your Spot discount relative to the Amazon SageMaker AI on-demand price.

**Note**  
The savings percentage compares the Amazon SageMaker AI Spot price to the Amazon SageMaker AI on-demand price. It is not comparable to the Amazon EC2 Spot price history shown in the Amazon EC2 console, which reflects the raw Amazon EC2 Spot market price for the underlying instance and does not include the Amazon SageMaker AI managed-service rate.
Managed spot training does not fall back to on-demand instances. When `EnableManagedSpotTraining` is set to `True`, the training job runs only on Spot capacity. If Spot capacity is unavailable, the job waits until `MaxWaitTimeInSeconds` is reached and then stops, rather than switching to on-demand instances.
The wall-clock duration of the job (`TrainingEndTime` minus `TrainingStartTime`) includes all interruptions, restarts, and Spot capacity waits, and is not the amount you are billed for. Only `BillableTimeInSeconds` is billed.

To learn how to run training jobs on Amazon SageMaker AI spot instances and how managed spot training works and reduces the billable time, see the following example notebooks:
+ [Managed Spot Training with TensorFlow](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-python-sdk/managed_spot_training_tensorflow_estimator/managed_spot_training_tensorflow_estimator.html)
+ [Managed Spot Training with PyTorch](https://github.com/aws-samples/amazon-sagemaker-managed-spot-training/blob/main/pytorch_managed_spot_training_checkpointing/pytorch_managed_spot_training_checkpointing.ipynb)
+ [Managed Spot Training with XGBoost](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_managed_spot_training.html)
+ [Managed Spot Training with MXNet](https://github.com/aws/amazon-sagemaker-examples-community/blob/215215eb25b40eadaf126d055dbb718a245d7603/training/sagemaker-debugger/mxnet-spot-training-with-sagemakerdebugger.ipynb#L41)
+ [Amazon SageMaker AI Managed Spot Training Examples GitHub repository](https://github.com/aws-samples/amazon-sagemaker-managed-spot-training)