# AWS Marketplace Commerce Analytics Service account permissions

Use the following IAM permissions policy to enroll in the AWS Marketplace Commerce Analytics Service.

For instructions on how to enroll, follow the [onboarding guide](commerce-analytics-service.md#on-boarding-guide "commerce-analytics-service.md#on-boarding-guide").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles",
 "iam:CreateRole",
 "iam:CreatePolicy",
 "iam:AttachRolePolicy",
 "aws-marketplace-management:viewReports"
 ],
 "Resource": "*"
 }
 ]
}`

```

Use the following IAM permissions policy to allow a user to make requests to the
AWS Marketplace Commerce Analytics Service.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "marketplacecommerceanalytics:GenerateDataSet",
 "Resource": "*"
 }
 ]
}`

```

For more information about this feature, see [Accessing product and customer data with the
AWS Marketplace Commerce Analytics Service](commerce-analytics-service.md "commerce-analytics-service.md").
