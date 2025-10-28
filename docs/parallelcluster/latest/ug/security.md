# Security in AWS ParallelCluster

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network
architecture that is built to meet the requirements of the most security sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")

describes this as security _of_ the
cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for protecting the
  infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use
  securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to AWS ParallelCluster, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is determined by the
  specific AWS service or services that you use. You are also responsible for several other related factors
  including the sensitivity of your data, your company’s requirements, and applicable laws and regulations.
  This documentation describes how you should apply the shared responsibility model when using AWS ParallelCluster.
  The following topics show you how to configure AWS ParallelCluster to meet your security and compliance objectives. You
  also learn how to use AWS ParallelCluster in a way that helps you to monitor and secure your AWS resources.

###### Topics

- [Security information for services used by AWS ParallelCluster](#security-seealso "#security-seealso")
- [Data protection in AWS ParallelCluster](data-protection.md "data-protection.md")
- [Identity and Access Management for AWS ParallelCluster](security-iam.md "security-iam.md")
- [Compliance validation for AWS ParallelCluster](security-compliance-validation.md "security-compliance-validation.md")
- [Enforcing a Minimum Version of TLS 1.2](security-enforcing-tls.md "security-enforcing-tls.md")
- [Configuring security groups for restricted environments](security-groups-configuration.md "security-groups-configuration.md")

## Security information for services used by AWS ParallelCluster

- [Security in Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-security.md "../../../AWSEC2/latest/UserGuide/ec2-security.md")
- [Security in
  Amazon API Gateway](../../../apigateway/latest/developerguide/security.md "../../../apigateway/latest/developerguide/security.md")
- [Security in AWS Batch](../../../batch/latest/userguide/security.md "../../../batch/latest/userguide/security.md")
- [Security in
  AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/security.md "../../../AWSCloudFormation/latest/UserGuide/security.md")
- [Security in
  Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/security.md "../../../AmazonCloudWatch/latest/monitoring/security.md")
- [Security in
  AWS CodeBuild](../../../codebuild/latest/userguide/security.md "../../../codebuild/latest/userguide/security.md")
- [Security in
  Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/security.md "../../../amazondynamodb/latest/developerguide/security.md")
- [Security in Amazon ECR](../../../AmazonECR/latest/userguide/security.md "../../../AmazonECR/latest/userguide/security.md")
- [Security in
  Amazon ECS](../../../AmazonECS/latest/developerguide/security.md "../../../AmazonECS/latest/developerguide/security.md")
- [Security in Amazon EFS](../../../efs/latest/ug/security-considerations.md "../../../efs/latest/ug/security-considerations.md")
- [Security in FSx for Lustre](../../../fsx/latest/LustreGuide/security.md "../../../fsx/latest/LustreGuide/security.md")
- [Security in AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/security.md "../../../IAM/latest/UserGuide/security.md")
- [Security in EC2 Image Builder](../../../imagebuilder/latest/userguide/image-builder-security.md "../../../imagebuilder/latest/userguide/image-builder-security.md")
- [Security in AWS Lambda](../../../lambda/latest/dg/lambda-security.md "../../../lambda/latest/dg/lambda-security.md")
- [Security in Amazon Route 53](../../../Route53/latest/DeveloperGuide/security.md "../../../Route53/latest/DeveloperGuide/security.md")
- [Security in Amazon SNS](../../../sns/latest/dg/sns-security.md "../../../sns/latest/dg/sns-security.md")
- [Security in
  Amazon SQS (For AWS ParallelCluster version 2.x.)](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-security.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-security.md")
- [Security in Amazon S3](../../../AmazonS3/latest/dev/security.md "../../../AmazonS3/latest/dev/security.md")
- [Security in Amazon VPC](../../../vpc/latest/userguide/security.md "../../../vpc/latest/userguide/security.md")
