# AWS Managed Policies for Model Registry

These AWS managed policies adds permissions required to use Model Registry. The policies are
available in your AWS account and are used by execution roles created from the Amazon SageMaker AI
console.

###### Topics

- [AWS
  managed policy: AmazonSageMakerModelRegistryFullAccess](#security-iam-awsmanpol-model-registry-AmazonSageMakerModelRegistryFullAccess "#security-iam-awsmanpol-model-registry-AmazonSageMakerModelRegistryFullAccess")
- [Amazon SageMaker AI updates to Model Registry managed policies](#security-iam-awsmanpol-model-registry-updates "#security-iam-awsmanpol-model-registry-updates")

## AWS

managed policy: AmazonSageMakerModelRegistryFullAccess

This AWS managed policy grants permissions needed to use all Model Registry features inside an
Amazon SageMaker AI domain. This policy is attached to an execution role when configuring
Model Registry settings to enable Model Registry permissions.

This policy includes the following permissions.

- `ecr` – Allows principals to retrieve information,
  including metadata, about Amazon Elastic Container Registry (Amazon ECR) images.
- `iam` – Allows principals to pass the execution role
  to the Amazon SageMaker AI service.
- `resource-groups` – Allows principals to create, list,
  tag, and delete AWS Resource Groups.
- `s3` – Allows principals to retrieve objects from the
  Amazon Simple Storage Service (Amazon S3) buckets where model versions are stored. Retrievable objects are limited
  to those whose case-insensitive name contains the string `"sagemaker"`.
- `sagemaker` – Allows principals to catalog, manage, and
  deploy models using the SageMaker Model Registry.
- `kms` – Allows only the SageMaker AI service principal to add a
  grant, generate data keys, decrypt, and read AWS KMS keys, and only keys that are tagged
  for "sagemaker" use.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonSageMakerModelRegistrySageMakerReadPermission",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeAction",
 "sagemaker:DescribeInferenceRecommendationsJob",
 "sagemaker:DescribeModelPackage",
 "sagemaker:DescribeModelPackageGroup",
 "sagemaker:DescribePipeline",
 "sagemaker:DescribePipelineExecution",
 "sagemaker:ListAssociations",
 "sagemaker:ListArtifacts",
 "sagemaker:ListModelMetadata",
 "sagemaker:ListModelPackages",
 "sagemaker:Search",
 "sagemaker:GetSearchSuggestions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonSageMakerModelRegistrySageMakerWritePermission",
 "Effect": "Allow",
 "Action": [
 "sagemaker:AddTags",
 "sagemaker:CreateModel",
 "sagemaker:CreateModelPackage",
 "sagemaker:CreateModelPackageGroup",
 "sagemaker:CreateEndpoint",
 "sagemaker:CreateEndpointConfig",
 "sagemaker:CreateInferenceRecommendationsJob",
 "sagemaker:DeleteModelPackage",
 "sagemaker:DeleteModelPackageGroup",
 "sagemaker:DeleteTags",
 "sagemaker:UpdateModelPackage"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonSageMakerModelRegistryS3GetPermission",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::*SageMaker*",
 "arn:aws:s3:::*Sagemaker*",
 "arn:aws:s3:::*sagemaker*"
 ]
 },
 {
 "Sid": "AmazonSageMakerModelRegistryS3ListPermission",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonSageMakerModelRegistryECRReadPermission",
 "Effect": "Allow",
 "Action": [
 "ecr:BatchGetImage",
 "ecr:DescribeImages"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonSageMakerModelRegistryIAMPassRolePermission",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "sagemaker.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AmazonSageMakerModelRegistryTagReadPermission",
 "Effect": "Allow",
 "Action": [
 "tag:GetResources"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonSageMakerModelRegistryResourceGroupGetPermission",
 "Effect": "Allow",
 "Action": [
 "resource-groups:GetGroupQuery"
 ],
 "Resource": "arn:aws:resource-groups:*:*:group/*"
 },
 {
 "Sid": "AmazonSageMakerModelRegistryResourceGroupListPermission",
 "Effect": "Allow",
 "Action": [
 "resource-groups:ListGroupResources"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AmazonSageMakerModelRegistryResourceGroupWritePermission",
 "Effect": "Allow",
 "Action": [
 "resource-groups:CreateGroup",
 "resource-groups:Tag"
 ],
 "Resource": "arn:aws:resource-groups:*:*:group/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "sagemaker:collection"
 }
 }
 },
 {
 "Sid": "AmazonSageMakerModelRegistryResourceGroupDeletePermission",
 "Effect": "Allow",
 "Action": "resource-groups:DeleteGroup",
 "Resource": "arn:aws:resource-groups:*:*:group/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker:collection": "true"
 }
 }
 },
 {
 "Sid": "AmazonSageMakerModelRegistryResourceKMSPermission",
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:*:*:key/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/sagemaker" : "true"
 },
 "StringLike": {
 "kms:ViaService": "sagemaker.*.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Amazon SageMaker AI updates to Model Registry managed policies

View details about updates to AWS managed policies for Model Registry since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the SageMaker AI [Document history page.](doc-history.md "doc-history.md")

| Policy                                                                                                                                                                                                                                     | Version | Change                                                                                          | Date           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ----------------------------------------------------------------------------------------------- | -------------- |
| [AmazonSageMakerModelRegistryFullAccess](#security-iam-awsmanpol-model-registry-AmazonSageMakerModelRegistryFullAccess "#security-iam-awsmanpol-model-registry-AmazonSageMakerModelRegistryFullAccess") <br>• Update to an existing policy | 2       | Add `kms:CreateGrant`, `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt` permissions. | June 6, 2024   |
| AmazonSageMakerModelRegistryFullAccess - New policy                                                                                                                                                                                        | 1       | Initial policy                                                                                  | April 12, 2023 |
