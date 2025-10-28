AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Environment sharing best

practices

We recommend the following practices when sharing environments:

- Only invite read/write members you trust to your environments.
- For EC2 environments, read/write members can use the environment owner's AWS access
  credentials to make calls from the environment to AWS services. This is instead of their
  own credentials. To prevent this, the environment owner can disable AWS managed temporary credentials for the
  environment. However, this also prevents the environment owner from making calls. For more
  information, see [AWS Managed
  Temporary Credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials "security-iam.md#auth-and-access-control-temporary-managed-credentials").
- Turn on AWS CloudTrail to track activity in your environments. For more information, see
  the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- Don't use your AWS account root user to create and share environments. Use IAM
  users in the account instead. For more information, see [First-Time Access Only: Your Root User Credentials](../../../IAM/latest/UserGuide/introduction_identity-management.md#intro-identity-first-time-access "../../../IAM/latest/UserGuide/introduction_identity-management.md#intro-identity-first-time-access") and [IAM users](../../../IAM/latest/UserGuide/introduction_identity-management.md#intro-identity-users "../../../IAM/latest/UserGuide/introduction_identity-management.md#intro-identity-users") in the _IAM User Guide_.
