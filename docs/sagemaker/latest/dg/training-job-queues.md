# AWS Batch support for SageMaker AI training jobs

An [AWS Batch job queue](../../../batch/latest/userguide/job_queues.md "../../../batch/latest/userguide/job_queues.md") stores and prioritizes submitted jobs before they run on compute
resources. You can submit SageMaker AI training jobs to a job queue in order to take advantage of
the serverless job scheduling and prioritization tools provided by AWS Batch.

## How it works

The following steps describe the workflow of how to use an AWS Batch job queue with
SageMaker AI training jobs. For more detailed tutorials and example notebooks, see the [Get started](#training-job-queues-get-started "#training-job-queues-get-started")
section.

- Set up AWS Batch and any necessary permissions. For more information, see
  [Setting up AWS Batch](../../../batch/latest/userguide/get-set-up-for-aws-batch.md "../../../batch/latest/userguide/get-set-up-for-aws-batch.md") in the _AWS Batch User
  Guide_.
- Create the following AWS Batch resources in the console or using the AWS CLI:
  - [Service environment](../../../batch/latest/userguide/service-environments.md "../../../batch/latest/userguide/service-environments.md") – Contains configuration parameters for
    integrating with SageMaker AI.
  - [SageMaker AI training job queue](../../../batch/latest/userguide/create-sagemaker-job-queue.md "../../../batch/latest/userguide/create-sagemaker-job-queue.md") – Integrates with SageMaker AI to submit
    training jobs.

- Configure your details and request for a SageMaker AI training job, such as your
  training container image. To submit a training job to an AWS Batch queue, you can
  use the AWS CLI, the AWS SDK for Python (Boto3), or the SageMaker AI Python
  SDK.
- Submit your training jobs to the job queue. You can use the following
  options to submit jobs:
  - Use the AWS Batch [SubmitServiceJob](../../../batch/latest/APIReference/API_SubmitServiceJob.md "../../../batch/latest/APIReference/API_SubmitServiceJob.md") API.
  - Use the [`aws_batch` module](https://github.com/aws/sagemaker-python-sdk/tree/master/src/sagemaker/aws_batch "https://github.com/aws/sagemaker-python-sdk/tree/master/src/sagemaker/aws_batch") from the SageMaker AI Python SDK.
    After creating a TrainingQueue object and a model training object
    (such as an Estimator or ModelTrainer), you can submit training jobs to
    the TrainingQueue using the `queue.submit()` method.

- After submitting jobs, view your job queue and job status with the AWS Batch
  console, the AWS Batch [DescribeServiceJob](../../../batch/latest/APIReference/API_DescribeServiceJob.md "../../../batch/latest/APIReference/API_DescribeServiceJob.md") API, or the SageMaker AI [DescribeTrainingJob](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md") API.

## Cost and availability

For detailed pricing information about training jobs, see [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker-ai/pricing/ "https://aws.amazon.com/sagemaker-ai/pricing/"). With AWS Batch, you only pay for any
AWS resources used, such as Amazon EC2 instances. For more information, see [AWS Batch
pricing](https://aws.amazon.com/batch/pricing/ "https://aws.amazon.com/batch/pricing/").

You can use AWS Batch for SageMaker AI training jobs in any AWS Region where training jobs are
available. For more information, see [Amazon SageMaker AI endpoints and quotas](../../../general/latest/gr/sagemaker.md "../../../general/latest/gr/sagemaker.md").

To ensure you have the required capacity when you need it, you can use SageMaker AI Flexible
Training Plans (FTP). These plans allow you to reserve capacity for your training jobs.
When combined with AWS Batch's queuing capabilities, you can maximize utilization
during your plan's duration. For more information, see [Reserve training plans for you training jobs or HyperPod clusters](reserve-capacity-with-training-plans.md "reserve-capacity-with-training-plans.md").

## Get started

For a tutorial on how to set up an AWS Batch job queue and submit SageMaker AI training jobs, see
[Getting started with AWS Batch on SageMaker AI](../../../batch/latest/userguide/getting-started-sagemaker.md "../../../batch/latest/userguide/getting-started-sagemaker.md") in the _AWS Batch User
Guide_.

For Jupyter notebooks that show how to use the `aws_batch` module in the
SageMaker AI Python SDK, see the [AWS Batch for SageMaker AI Training jobs notebook examples in the
amazon-sagemaker-examples GitHub repository](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20%20%20%20build_and_train_models/sm-training-queues "https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20%20%20%20build_and_train_models/sm-training-queues").
