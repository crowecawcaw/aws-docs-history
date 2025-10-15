# AWS managed policies for Amazon S3

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed 
 to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because 
 they're available for all AWS customers to use. We recommend that you reduce permissions further by defining 
 [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS 
 managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is 
 most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
 existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies") in the 
 *IAM User Guide*.


## AWS managed policy:
 AmazonS3FullAccess


You can attach the `AmazonS3FullAccess` policy to your IAM identities.
 This policy grants permissions that allow full access to Amazon S3.


To view the permissions for this policy, see [AmazonS3FullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3FullAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3FullAccess$jsonEditor") in the AWS Management Console.


## AWS managed policy:
 AmazonS3ReadOnlyAccess


You can attach the `AmazonS3ReadOnlyAccess` policy to your IAM
 identities. This policy grants permissions that allow read-only access to Amazon S3.


To view the permissions for this policy, see [AmazonS3ReadOnlyAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess$jsonEditor") in the AWS Management Console.


## AWS
 managed policy: AmazonS3ObjectLambdaExecutionRolePolicy


Provides AWS Lambda functions the required permissions to send data to S3 Object Lambda when
 requests are made to an S3 Object Lambda access point. Also grants Lambda permissions to write to
 Amazon CloudWatch logs.


To view the permissions for this policy, see [AmazonS3ObjectLambdaExecutionRolePolicy](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AmazonS3ObjectLambdaExecutionRolePolicy$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AmazonS3ObjectLambdaExecutionRolePolicy$jsonEditor") in the
 AWS Management Console.


## AWS
 managed policy: S3UnlockBucketPolicy


If you incorrectly configured your bucket policy for a member account to deny all users access to your S3 bucket, you can use this AWS managed policy (`S3UnlockBucketPolicy`) to unlock the bucket. For more information on how to remove a misconfigured bucket policy that denies all principals from accessing an Amazon S3 bucket, see [Perform a privileged task on an AWS Organizations member account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user-privileged-task.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user-privileged-task.html") in the *AWS Identity and Access Management User Guide*. 


## Amazon S3 updates to AWS managed
 policies


View details about updates to AWS managed policies for Amazon S3 since this service
 began tracking these changes.




| Change | Description | Date |
| --- | --- | --- |
| Amazon S3 added
 `S3UnlockBucketPolicy` | Amazon S3 added a new AWS-managed policy called `S3UnlockBucketPolicy` to unlock a bucket and remove a misconfigured bucket policy that denies all principals from accessing an Amazon S3 bucket. | November 1, 2024 |
| Amazon S3 added
 Describe
 permissions to `AmazonS3ReadOnlyAccess` | Amazon S3 added `s3:Describe*` permissions to 
 `AmazonS3ReadOnlyAccess`. | August 11, 2023 |
| Amazon S3 added S3 Object Lambda permissions to `AmazonS3FullAccess` and
 `AmazonS3ReadOnlyAccess` | Amazon S3 updated the `AmazonS3FullAccess` and
 `AmazonS3ReadOnlyAccess` policies to include
 permissions for S3 Object Lambda. | September 27, 2021 |
| Amazon S3 added `AmazonS3ObjectLambdaExecutionRolePolicy` | Amazon S3 added a new AWS-managed policy called `AmazonS3ObjectLambdaExecutionRolePolicy` that
 provides Lambda functions permissions to interact with S3 Object Lambda and write to CloudWatch logs. | August 18, 2021 |
| Amazon S3 started tracking changes | Amazon S3 started tracking changes for its AWS managed policies. | August 18, 2021 |
