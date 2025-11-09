# AWS managed policies for

Amazon SageMaker Partner AI Apps

These AWS managed policies add permissions required to use Amazon SageMaker Partner AI Apps. The policies are
available in your AWS account and are used by execution roles created from the SageMaker AI
console.

###### Topics

- [AWS
  managed policy: AmazonSageMakerPartnerAppsFullAccess](#security-iam-awsmanpol-AmazonSageMakerPartnerAppsFullAccess "#security-iam-awsmanpol-AmazonSageMakerPartnerAppsFullAccess")
- [Amazon SageMaker AI updates to
  Partner AI Apps managed policies](#security-iam-awsmanpol-partner-apps-updates "#security-iam-awsmanpol-partner-apps-updates")

## AWS

managed policy: AmazonSageMakerPartnerAppsFullAccess

Allows full administrative access to Amazon SageMaker Partner AI Apps.

**Permissions details**

This AWS managed policy includes the following permissions.

- `sagemaker` – Gives Amazon SageMaker Partner AI App users permission to access
  applications, list available applications, launch application web UIs, and
  connect using the application SDK.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonSageMakerPartnerListAppsPermission",
 "Effect": "Allow",
 "Action": "sagemaker:ListPartnerApps",
 "Resource": "*"
 },
 {
 "Sid": "AmazonSageMakerPartnerAppsPermission",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreatePartnerAppPresignedUrl",
 "sagemaker:DescribePartnerApp",
 "sagemaker:CallPartnerAppApi"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 },
 "Resource": "arn:aws:sagemaker:*:*:partner-app/*"
 }
 ]
}`

```

## Amazon SageMaker AI updates to

Partner AI Apps managed policies

View details about updates to AWS managed policies for Partner AI Apps since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the SageMaker AI [Document history
page.](doc-history.md "doc-history.md")

| Policy                                               | Version | Change         | Date             |
| ---------------------------------------------------- | ------- | -------------- | ---------------- |
| AmazonSageMakerPartnerAppsFullAccess<br>• New policy | 1       | Initial policy | January 17, 2025 |
