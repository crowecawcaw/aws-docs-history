# Security for AWS DeepRacer

To use AWS DeepRacer to train and evaluate reinforcement learning, your AWS account must have appropriate
security permissions to access dependent AWS resources, including Amazon VPC to run training jobs
and an Amazon S3 bucket to store trained model artifacts.

The AWS DeepRacer console provides a way for you to have the required security settings set up
for the dependent services. This section documents the AWS services AWS DeepRacer depends as well as the
the IAM roles and policy defining the required permissions to access the dependent services.

###### Topics

- [Data protection in AWS DeepRacer](data-protection.md "data-protection.md")
- [AWS DeepRacer-Dependent AWS
  Services](deepracer-dependent-aws-services.md "deepracer-dependent-aws-services.md")
- [Required IAM roles
  for AWS DeepRacer to call dependent AWS Services](deepracer-understand-required-permissions-and-iam-roles.md "deepracer-understand-required-permissions-and-iam-roles.md")
- [AWS Identity and Access Management for AWS DeepRacer](security-iam.md "security-iam.md")
