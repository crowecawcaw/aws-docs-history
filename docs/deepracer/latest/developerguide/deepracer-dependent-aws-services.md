# AWS DeepRacer-Dependent AWS

Services

AWS DeepRacer uses the following AWS services to manage required resources:

Amazon Simple Storage Service

To store trained model artifacts in an Amazon S3 bucket.

AWS Lambda

To create and run the reward functions.

AWS CloudFormation

To create training jobs for AWS DeepRacer models.

SageMaker AI

To train the AWS DeepRacer models.

The dependent AWS Lambda, AWS CloudFormation, and SageMaker AI in turn use other AWS services
including Amazon CloudWatch and Amazon CloudWatch Logs.

The following table shows AWS services used by AWS DeepRacer, directly or indirectly.

| AWS Services that AWS DeepRacer uses directly or indirectly                                         | AWS service principal                                                                                                                                                                                                                                                                                                                            | Comments |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| [`application-autoscaling`](https://aws.amazon.com/ecr/ "https://aws.amazon.com/ecr/")              | • Indirectly called by SageMaker AI to automatically scale its<br>operations.                                                                                                                                                                                                                                                                    |
| [`cloudformation`](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") | • Directly called by AWS DeepRacer to create account resources.                                                                                                                                                                                                                                                                                  |
| [`cloudwatch`](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")             | • Directly called by AWS DeepRacer to log its operations.<br>• Indirectly called by SageMaker AI to log its operations.                                                                                                                                                                                                                          |
| [`ec2`](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")                                  | • Indirectly called by AWS CloudFormation and SageMaker AI to create and run<br>training jobs.                                                                                                                                                                                                                                                   |
| `kinesisvideo`                                                                                      | • Directly called by AWS DeepRacer to view cached training<br>streams.                                                                                                                                                                                                                                                                           |
| [`lambda`](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")                         | • Directly called by AWS DeepRacer to create and run the reward<br>functions.                                                                                                                                                                                                                                                                    |
| [`logs`](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")                   | • Directly called by AWS DeepRacer to log its operations.<br>• Indirectly called by AWS Lambda to log its operations.                                                                                                                                                                                                                            |
| [`s3`](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")                                     | • Indirectly called by SageMaker AI to perform SageMaker AI-specific storage<br>operations.<br>• Directly called by AWS DeepRacer to create, list, and delete<br>buckets that have names starting with "`deepracer`."<br>Also called to download objects from the buckets, upload objects<br>to the buckets, or delete objects from the buckets. |
| [`sagemaker`](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/")                | • Directly called by AWS DeepRacer to train reinforcement learning models.                                                                                                                                                                                                                                                                       |

To use AWS DeepRacer to call these services, you must have appropriate IAM roles
with required policies attached to them. Learn the details about these
policies and roles in [Required IAM roles
for AWS DeepRacer to call dependent AWS Services](deepracer-understand-required-permissions-and-iam-roles.md "deepracer-understand-required-permissions-and-iam-roles.md").
