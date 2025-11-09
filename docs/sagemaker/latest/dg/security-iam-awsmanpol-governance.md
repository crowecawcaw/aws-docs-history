# AWS Managed Policies for SageMaker AI Model Governance

This AWS managed policy adds permissions required to use SageMaker AI Model Governance. The
policy is available in your AWS account and is used by execution roles created from the
SageMaker AI console.

###### Topics

- [AWS
  managed policy: AmazonSageMakerModelGovernanceUseAccess](#security-iam-awsmanpol-governance-AmazonSageMakerModelGovernanceUseAccess "#security-iam-awsmanpol-governance-AmazonSageMakerModelGovernanceUseAccess")
- [Amazon SageMaker AI updates to SageMaker AI Model Governance managed policies](#security-iam-awsmanpol-governance-updates "#security-iam-awsmanpol-governance-updates")

## AWS

managed policy: AmazonSageMakerModelGovernanceUseAccess

This AWS managed policy grants permissions needed to use all Amazon SageMaker AI Governance features. The policy is available in your AWS account.

This policy includes the following permissions.

- `s3` – Retrieve objects from Amazon S3 buckets. Retrievable objects are limited to those whose case-insensitive name contains the string `"sagemaker"`.
- `kms` – List the AWS KMS keys to use for content encryption.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSMMonitoringModelCards",
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListMonitoringAlerts",
 "sagemaker:ListMonitoringExecutions",
 "sagemaker:UpdateMonitoringAlert",
 "sagemaker:StartMonitoringSchedule",
 "sagemaker:StopMonitoringSchedule",
 "sagemaker:ListMonitoringAlertHistory",
 "sagemaker:DescribeModelPackage",
 "sagemaker:DescribeModelPackageGroup",
 "sagemaker:CreateModelCard",
 "sagemaker:DescribeModelCard",
 "sagemaker:UpdateModelCard",
 "sagemaker:DeleteModelCard",
 "sagemaker:ListModelCards",
 "sagemaker:ListModelCardVersions",
 "sagemaker:CreateModelCardExportJob",
 "sagemaker:DescribeModelCardExportJob",
 "sagemaker:ListModelCardExportJobs"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowSMTrainingModelsSearchTags",
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListTrainingJobs",
 "sagemaker:DescribeTrainingJob",
 "sagemaker:ListModels",
 "sagemaker:DescribeModel",
 "sagemaker:Search",
 "sagemaker:AddTags",
 "sagemaker:DeleteTags",
 "sagemaker:ListTags"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowKMSActions",
 "Effect": "Allow",
 "Action": [
 "kms:ListAliases"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowS3Actions",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:CreateBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::*SageMaker*",
 "arn:aws:s3:::*Sagemaker*",
 "arn:aws:s3:::*sagemaker*"
 ]
 },
 {
 "Sid": "AllowS3ListActions",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Amazon SageMaker AI updates to SageMaker AI Model Governance managed policies

View details about updates to AWS managed policies for SageMaker AI Model Governance since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the SageMaker AI [Document history page.](doc-history.md "doc-history.md")

| Policy                                                                                                                                                                                                                               | Version | Change                                                                               | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------------------------------------------------------------------------------------ | ----------------- |
| [AmazonSageMakerModelGovernanceUseAccess](#security-iam-awsmanpol-governance-AmazonSageMakerModelGovernanceUseAccess "#security-iam-awsmanpol-governance-AmazonSageMakerModelGovernanceUseAccess")<br>• Update to an existing policy | 3       | Add statement IDs (`Sid`).                                                           | June 4, 2024      |
| AmazonSageMakerModelGovernanceUseAccess<br>• Update to an existing policy                                                                                                                                                            | 2       | Add `sagemaker:DescribeModelPackage` and<br>`DescribeModelPackageGroup` permissions. | July 17, 2023     |
| AmazonSageMakerModelGovernanceUseAccess<br>• New policy                                                                                                                                                                              | 1       | Initial policy                                                                       | November 30, 2022 |
