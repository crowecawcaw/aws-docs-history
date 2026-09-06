

# Permissions for AWS services in key policies
<a name="key-policy-services"></a>

Many AWS services use AWS KMS keys to protect the resources they manage. When a service uses [AWS owned keys](concepts.md#aws-owned-key) or [AWS managed keys](concepts.md#aws-managed-key), the service establishes and maintains the key policies for these KMS keys. 

However, when you use a [customer managed key](concepts.md#customer-mgn-key) with an AWS service, you set and maintain the key policy. That key policy must allow the service the minimum permissions that it requires to protect the resource on your behalf. We recommend that you follow the principle of least privilege: give the service only the permissions that it requires. You can do this effectively by learning which permissions the service needs and using [AWS global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) and [AWS KMS condition keys](policy-conditions.md) to refine the permissions. 

To find the permissions that the service requires on a customer managed key, see the encryption documentation for the service. The following list includes links to some services documentation:
+ **AWS CloudTrail** permissions - [Configure AWS KMS key policies for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-kms-key-policy-for-cloudtrail.html#create-kms-key-policy-for-cloudtrail-decrypt)
+ **Amazon Elastic Block Store** permissions - [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#ebs-encryption-permissions) and [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EBSEncryption.html#ebs-encryption-permissions)
+ **AWS Lambda** permissions - [Data encryption at rest for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-encryption-at-rest.html)
+ **Amazon Q** permissions - [Data encryption for Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-encryption.html)
+ **Amazon Relational Database Service** permissions - [AWS KMS key management](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.Keys.html)
+ **AWS Secrets Manager** permissions - [Authorizing use of the KMS key](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html#security-encryption-authz)
+ **Amazon Simple Queue Service** permissions - [Amazon SQS Key management](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-key-management.html)