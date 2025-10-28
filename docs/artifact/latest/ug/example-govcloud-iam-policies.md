# Example IAM policies for AWS Artifact in AWS GovCloud (US) Regions

These policies are ONLY applicable in AWS GovCloud (US) Regions. For policies applicable to commercial AWS [Regions](../../../glossary/latest/reference/glos-chap.md#region "../../../glossary/latest/reference/glos-chap.md#region"),
see [Example IAM policies for AWS Artifact in commercial AWS Regions](example-iam-policies.md "example-iam-policies.md")

You can create permissions policies that grant permissions to IAM users. You can
grant users access to AWS Artifact reports and the ability to accept and download agreements
on behalf of either a single account or an organization.

The following example policies show permissions that you can assign to IAM users
based on the level of access that they need.

- [Example policies to manage AWS reports](#example-policy-manage-reports-govcloud "#example-policy-manage-reports-govcloud")
- [Example policies to manage agreements](#example-policy-manage-agreements-govcloud "#example-policy-manage-agreements-govcloud")
- [Example policies to integrate with AWS Organizations](#example-policy-integrate-with-organizations-govcloud "#example-policy-integrate-with-organizations-govcloud")
- [Example policies to manage agreements for the management account](#example-policy-agreements-master-govcloud "#example-policy-agreements-master-govcloud")
- [Example policies to manage organizational agreements](#example-policy-organizational-agreements-govcloud "#example-policy-organizational-agreements-govcloud")

###### Example policies to manage reports

The following policy grants permission to download all reports.

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

The following policy grants permission to download only the SOC, PCI, and ISO reports.

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
 "artifact:GetTermForReport"
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

###### Example policies to manage agreements

The following policy grants permission to download all agreements. IAM users
must also have this permission to accept agreements.

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
 "Resource": "arn:aws-us-gov:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement"
 ],
 "Resource": "arn:aws-us-gov:artifact::*:customer-agreement/*"
 }
 ]
}`

```

The following policy grants permission to accept all agreement.

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
 "Resource": "arn:aws-us-gov:artifact:::agreement/*"
 }
 ]
}`

```

The following policy grants permission to terminate all agreement.

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
 "Resource": "arn:aws-us-gov:artifact::*:customer-agreement/*"
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
 "Resource": "arn:aws-us-gov:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": "arn:aws-us-gov:artifact::*:customer-agreement/*"
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
 "Resource": "arn:aws-us-gov:iam::*:role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact",
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
 "Resource": "arn:aws-us-gov:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": "arn:aws-us-gov:artifact::*:customer-agreement/*"
 },
 {
 "Sid": "CreateServiceLinkedRoleForOrganizationsIntegration",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole",
 "iam:GetRole"
 ],
 "Resource": "arn:aws-us-gov:iam::*:role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact",
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
 "Resource": "arn:aws-us-gov:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": "arn:aws-us-gov:artifact::*:customer-agreement/*"
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
 "Resource": "arn:aws-us-gov:artifact:::agreement/*"
 },
 {
 "Sid": "CustomerAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement"
 ],
 "Resource": "arn:aws-us-gov:artifact::*:customer-agreement/*"
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
