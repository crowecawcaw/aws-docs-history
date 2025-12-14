# Example IAM policies for AWS Artifact in commercial AWS Regions

You can create permissions policies that grant permissions to IAM users. You can
grant users access to AWS Artifact reports and the ability to accept and download agreements
on behalf of either a single account or an organization.

The following example policies show permissions that you can assign to IAM users
based on the level of access that they need.

These policies are applicable in commercial AWS [Regions](../../../glossary/latest/reference/glos-chap.md#region "../../../glossary/latest/reference/glos-chap.md#region"). For policies applicable to AWS GovCloud (US) Regions,
see [Example IAM policies for AWS Artifact in AWS GovCloud (US) Regions](example-govcloud-iam-policies.md "example-govcloud-iam-policies.md")

- [Example policies to manage AWS reports with fine-grained permissions](#example-policy-manage-aws-reports-with-finegrained-permissions "#example-policy-manage-aws-reports-with-finegrained-permissions")
- [Example policies to manage third-party reports](#example-policy-manage-third-party-reports "#example-policy-manage-third-party-reports")
- [Example policies to manage agreements](#example-policy-manage-agreements "#example-policy-manage-agreements")
- [Example policies to integrate with AWS Organizations](#example-policy-integrate-with-organizations "#example-policy-integrate-with-organizations")
- [Example policies to manage agreements for the management account](#example-policy-agreements-master "#example-policy-agreements-master")
- [Example policies to manage organizational agreements](#example-policy-organizational-agreements "#example-policy-organizational-agreements")
- [Example policies to manage notifications](#example-policy-notifications "#example-policy-notifications")

###### Example policies to manage AWS reports through fine-grained permissions

###### Tip

You should consider using the
[AWSArtifactReportsReadOnlyAccess managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md") instead of defining your own policy.

The following policy grants permission to download all AWS reports through fine-grained permissions.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:ListReports",
 "artifact:GetReportMetadata",
 "artifact:GetReport",
 "artifact:GetTermForReport",
 "artifact:ListReportVersions"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy grants permission to download only the AWS SOC, PCI, and ISO reports through fine-grained permissions.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:ListReports"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetReportMetadata",
 "artifact:GetReport",
 "artifact:GetTermForReport",
 "artifact:ListReportVersions"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "artifact:ReportSeries": [
 "SOC",
 "PCI",
 "ISO"
 ],
 "artifact:ReportCategory": [
 "Certifications and Attestations"
 ]
 }
 }
 }
 ]
}`

```

###### Example policies to manage third-party reports

###### Tip

You should consider using the
[AWSArtifactReportsReadOnlyAccess managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md") instead of defining your own policy.

Third-party reports are denoted by the IAM resource
`report`.

The following policy grants permission to all third-party report functionality.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:ListReports",
 "artifact:GetReportMetadata",
 "artifact:GetReport",
 "artifact:GetTermForReport"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy grants permission to download third-party reports.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetReport",
 "artifact:GetTermForReport"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy grants permission to list third-party reports.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:ListReports"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy grants permission to view a third-party report's details for all versions.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetReportMetadata"
 ],
 "Resource": [
 "arn:aws:artifact:us-east-1::report/report-jRVRFP8HxUN5zpPh:*"
 ]
 }
 ]
}`

```

The following policy grants permission to view a third-party report's details for a specific version.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetReportMetadata"
 ],
 "Resource": [
 "arn:aws:artifact:us-east-1::report/report-jRVRFP8HxUN5zpPh:1"
 ]
 }
 ]
}`

```

###### Tip

You should consider using the
[AWSArtifactAgreementsReadOnlyAccess or AWSArtifactAgreementsFullAccess managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md") instead of defining your own policy.

###### Example policies to manage agreements

The following policy grants permission to download all agreements.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:ListAgreements",
 "artifact:ListCustomerAgreements"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AWSAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetAgreement",
 "artifact:AcceptNdaForAgreement",
 "artifact:GetNdaForAgreement"
 ],
 "Resource": "arn:aws:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement"
 ],
 "Resource": "arn:aws:artifact::*:customer-agreement/*"
 }
 ]
}`

```

The following policy grants permission to accept all agreements.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:ListAgreements"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "AWSAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetAgreement",
 "artifact:AcceptNdaForAgreement",
 "artifact:GetNdaForAgreement",
 "artifact:AcceptAgreement"
 ],
 "Resource": "arn:aws:artifact:::agreement/*"
 }
 ]
}`

```

The following policy grants permission to terminate all agreements.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:ListAgreements",
 "artifact:ListCustomerAgreements"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": "arn:aws:artifact::*:customer-agreement/*"
 }
 ]
}`

```

The following policy grants permissions to view and execute account level agreements.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:ListAgreements",
 "artifact:ListCustomerAgreements"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AWSAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetAgreement",
 "artifact:AcceptNdaForAgreement",
 "artifact:GetNdaForAgreement",
 "artifact:AcceptAgreement"
 ],
 "Resource": "arn:aws:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": "arn:aws:artifact::*:customer-agreement/*"
 }
 ]
}`

```

###### Example policies to integrate with AWS Organizations

The following policy grants permission to create the IAM role that AWS Artifact uses
to integrate with AWS Organizations. Your organization's management account must have these
permissions to get started with organizational agreements.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CreateServiceLinkedRoleForOrganizationsIntegration",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole",
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "artifact.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

The following policy grants permission to grant AWS Artifact the permissions to
use AWS Organizations. Your organization's management account must have these permissions
to get started with organizational agreements.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAWSServiceAccessForOrganization"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EnableServiceTrustForArtifact",
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "aws-artifact-account-sync.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

###### Example policies to manage agreements for the management account

The following policy grants permissions to manage agreements for the management account.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:ListAgreements",
 "artifact:ListCustomerAgreements"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AWSAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetAgreement",
 "artifact:AcceptNdaForAgreement",
 "artifact:GetNdaForAgreement",
 "artifact:AcceptAgreement"
 ],
 "Resource": "arn:aws:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": "arn:aws:artifact::*:customer-agreement/*"
 },
 {
 "Sid": "CreateServiceLinkedRoleForOrganizationsIntegration",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole",
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "artifact.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "EnableServiceTrust",
 "Effect": "Allow",
 "Action": [
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:DescribeOrganization"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EnableServiceTrustForArtifact",
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "aws-artifact-account-sync.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

###### Example policies to manage organizational agreements

The following policy grants permissions to manage organizational agreements. Another user
with the required permissions must set up the organizational agreements.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:ListAgreements",
 "artifact:ListCustomerAgreements"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AWSAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetAgreement",
 "artifact:AcceptNdaForAgreement",
 "artifact:GetNdaForAgreement",
 "artifact:AcceptAgreement"
 ],
 "Resource": "arn:aws:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": "arn:aws:artifact::*:customer-agreement/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy grants permissions to view organizational agreements.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:ListAgreements",
 "artifact:ListCustomerAgreements"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AWSAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetAgreement",
 "artifact:AcceptNdaForAgreement",
 "artifact:GetNdaForAgreement"
 ],
 "Resource": "arn:aws:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement"
 ],
 "Resource": "arn:aws:artifact::*:customer-agreement/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Example policies to manage notifications

The following policy grants complete permissions to use AWS Artifact notifications.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetAccountSettings",
 "artifact:PutAccountSettings",
 "notifications:AssociateChannel",
 "notifications:CreateEventRule",
 "notifications:CreateNotificationConfiguration",
 "notifications:DeleteEventRule",
 "notifications:DeleteNotificationConfiguration",
 "notifications:DisassociateChannel",
 "notifications:GetEventRule",
 "notifications:GetNotificationConfiguration",
 "notifications:ListChannels",
 "notifications:ListEventRules",
 "notifications:ListNotificationConfigurations",
 "notifications:ListNotificationHubs",
 "notifications:ListTagsForResource",
 "notifications:TagResource",
 "notifications:UntagResource",
 "notifications:UpdateEventRule",
 "notifications:UpdateNotificationConfiguration",
 "notifications-contacts:CreateEmailContact",
 "notifications-contacts:DeleteEmailContact",
 "notifications-contacts:GetEmailContact",
 "notifications-contacts:ListEmailContacts",
 "notifications-contacts:SendActivationCode"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following policy grants permission to list all configurations.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetAccountSettings",
 "notifications:ListChannels",
 "notifications:ListEventRules",
 "notifications:ListNotificationConfigurations",
 "notifications:ListNotificationHubs",
 "notifications-contacts:GetEmailContact"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following policy grants permission to create a configuration.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetAccountSettings",
 "artifact:PutAccountSettings",
 "notifications-contacts:CreateEmailContact",
 "notifications-contacts:SendActivationCode",
 "notifications:AssociateChannel",
 "notifications:CreateEventRule",
 "notifications:CreateNotificationConfiguration",
 "notifications:ListEventRules",
 "notifications:ListNotificationHubs",
 "notifications:TagResource",
 "notifications-contacts:ListEmailContacts"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following policy grants permission to edit a configuration.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:GetAccountSettings",
 "artifact:PutAccountSettings",
 "notifications:AssociateChannel",
 "notifications:DisassociateChannel",
 "notifications:GetNotificationConfiguration",
 "notifications:ListChannels",
 "notifications:ListEventRules",
 "notifications:ListTagsForResource",
 "notifications:TagResource",
 "notifications:UntagResource",
 "notifications:UpdateEventRule",
 "notifications:UpdateNotificationConfiguration",
 "notifications-contacts:GetEmailContact",
 "notifications-contacts:ListEmailContacts"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following policy grants permission to delete a configuration.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "notifications:DeleteNotificationConfiguration",
 "notifications:ListEventRules"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following policy grants permission to view details of a configuration.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "notifications:GetNotificationConfiguration",
 "notifications:ListChannels",
 "notifications:ListEventRules",
 "notifications:ListTagsForResource",
 "notifications-contacts:GetEmailContact"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following policy grants permission to register or deregister notification hubs.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "notifications:DeregisterNotificationHub",
 "notifications:RegisterNotificationHub"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
