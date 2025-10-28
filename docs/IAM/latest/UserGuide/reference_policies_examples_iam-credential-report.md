# IAM: Generate and retrieve

IAM credential reports

This example shows how you might create an identity-based policy that allows users to generate and download a report that lists all IAM
users in their AWS account. The report includes the status of the users' credentials,
including passwords, access keys, MFA devices, and signing
certificates. This policy grants the permissions necessary to complete this action programmatically from the AWS API or AWS CLI.

For more information about credential reports, see [Generate credential reports for your
AWS account](id_credentials_getting-report.md "id_credentials_getting-report.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "iam:GenerateCredentialReport",
 "iam:GetCredentialReport"
 ],
 "Resource": "*"
 }
}`

```
