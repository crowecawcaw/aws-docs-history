

# AWS policy: SageMakerStudioProjectRoleMachineLearningPolicy
<a name="security-iam-awsmanpol-SageMakerStudioProjectRoleMachineLearningPolicy"></a>

Amazon SageMaker Unified Studio creates IAM roles for projects users to perform data analytics, artificial intelligence, and machine learning actions, and uses this policy when creating these roles to define the permissions related to Amazon SageMaker.

This is the SageMaker policy for the SageMakerUnifiedStudioProjectRole role. This policy grants read and write access for Amazon SageMaker Unified Studio users to services such as Amazon SageMaker, Amazon CloudWatch, and AWS Resource Groups. The policy also gives read and write permissions to some infrastructure resources that are required to use these services such as network interfaces and AWS KMS keys.

An administrator can control certain permissions in this policy by tagging the role to which the policy is attached. The tag EnableSageMakerMLWorkloadsPermissions — when set to "true" (default), grants permissions for SageMaker ML workloads including training jobs, processing jobs, and model deployment. When not set to "true", these SageMaker ML workload permissions are not granted.

To view the permissions for this policy, see [SageMakerStudioProjectRoleMachineLearningPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SageMakerStudioProjectRoleMachineLearningPolicy.html) in the *AWS Managed Policy Reference*.