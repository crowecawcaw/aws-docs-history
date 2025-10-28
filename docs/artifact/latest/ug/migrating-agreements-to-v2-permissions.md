# Migrating to fine-grained permissions for AWS Artifact agreements

AWS Artifact now enables customers to use fine-grained permissions for agreements. Through these fine-grained permissions, customers have granular control on providing access to features such as viewing and accepting non-disclosure agreements, as well as accepting and terminating agreements.

To access agreements through the fine-grained permissions, you can utilize the
[AWSArtifactAgreementsReadOnlyAccess or AWSArtifactAgreementsFullAccess](security-iam-awsmanpol.md "security-iam-awsmanpol.md") managed policies or update your permissions as per the below recommendation.

###### Note

The IAM action `artifact:DownloadAgreement` was deprecated in the AWS partition on March 3, 2025 and in the AWS GovCloud (US) partition on July 1, 2025.

## Migrating to new permissions

The legacy IAM action "DownloadAgreement" has been replaced by the "GetAgreement" action to download unaccepted agreements and by the "GetCustomerAgreement" action for downloading accepted agreements. Additionally, more granular actions have been introduced to control access for viewing and accepting non-disclosure agreements (NDAs). To take advantage of these granular actions and maintain the ability to view and execute agreements, users must replace their existing policy containing legacy permissions with a policy containing fine-grained permissions.

**Migrate permissions to download agreement at account level**

Legacy Policy:

AWS

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:DownloadAgreement"
 ],
 "Resource": [
 "arn:aws:artifact::*:customer-agreement/*",
 "arn:aws:artifact:::agreement/*"
 ]
 }
 ]
}`

```

AWS GovCloud (US)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:DownloadAgreement"
 ],
 "Resource": [
 "arn:aws-us-gov:artifact::*:customer-agreement/*",
 "arn:aws-us-gov:artifact:::agreement/*"
 ]
 }
 ]
}`

```

New Policy with fine-grained permissions:

AWS

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListAgreementsActions",
 "Effect": "Allow",
 "Action": [
 "artifact:ListAgreements",
 "artifact:ListCustomerAgreements"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GetAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement",
 "artifact:GetAgreement",
 "artifact:GetNdaForAgreement",
 "artifact:AcceptNdaForAgreement"
 ],
 "Resource": [
 "arn:aws:artifact::*:customer-agreement/*",
 "arn:aws:artifact:::agreement/*"
 ]
 }
 ]
}`

```

AWS GovCloud (US)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListAgreementsActions",
 "Effect": "Allow",
 "Action": [
 "artifact:ListAgreements",
 "artifact:ListCustomerAgreements"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GetAgreementActions",
 "Effect": "Allow",
 "Action": [
 "artifact:GetCustomerAgreement",
 "artifact:GetAgreement",
 "artifact:GetNdaForAgreement",
 "artifact:AcceptNdaForAgreement"
 ],
 "Resource": [
 "arn:aws-us-gov:artifact::*:customer-agreement/*",
 "arn:aws-us-gov:artifact:::agreement/*"
 ]
 }
 ]
}`

```

**Migrate non-resource specific permissions to download, accept and terminate agreements at account level**

Legacy Policy:

AWS

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:AcceptAgreement",
 "artifact:DownloadAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": [
 "arn:aws:artifact::*:customer-agreement/*",
 "arn:aws:artifact:::agreement/*"
 ]
 }
 ]
}`

```

AWS GovCloud (US)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:AcceptAgreement",
 "artifact:DownloadAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": [
 "arn:aws-us-gov:artifact::*:customer-agreement/*",
 "arn:aws-us-gov:artifact:::agreement/*"
 ]
 }
 ]
}`

```

New Policy with fine-grained permissions:

AWS

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

AWS GovCloud (US)

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

**Migrate non-resource specific permissions to download, accept and terminate agreements at Organization level**

Legacy Policy:

AWS

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:AcceptAgreement",
 "artifact:DownloadAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": [
 "arn:aws:artifact::*:customer-agreement/*",
 "arn:aws:artifact:::agreement/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "arn:aws:iam:::role/*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam:::role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
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

AWS GovCloud (US)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:AcceptAgreement",
 "artifact:DownloadAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": [
 "arn:aws-us-gov:artifact::*:customer-agreement/*",
 "arn:aws-us-gov:artifact:::agreement/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "arn:aws-us-gov:iam:::role/*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws-us-gov:iam:::role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
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

New Policy with fine-grained permissions:

AWS

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
 "iam:CreateServiceLinkedRole"
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
 "Sid": "GetRoleToCheckForRoleExistence",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact"
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

AWS GovCloud (US)

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
 "iam:CreateServiceLinkedRole"
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
 "Sid": "GetRoleToCheckForRoleExistence",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole"
 ],
 "Resource": "arn:aws-us-gov:iam::*:role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact"
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

**Migrate resource specific permissions to download, accept and terminate agreements at account level**

Legacy Policy:

AWS

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:AcceptAgreement",
 "artifact:DownloadAgreement"
 ],
 "Resource": [
 "arn:aws:artifact:::agreement/AWS Business Associate Addendum"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "artifact:TerminateAgreement"
 ],
 "Resource": [
 "arn:aws:artifact::*:customer-agreement/*"
 ]
 }
 ]
}`

```

AWS GovCloud (US)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:AcceptAgreement",
 "artifact:DownloadAgreement"
 ],
 "Resource": [
 "arn:aws-us-gov:artifact:::agreement/AWS Business Associate Addendum"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "artifact:TerminateAgreement"
 ],
 "Resource": [
 "arn:aws-us-gov:artifact::*:customer-agreement/*"
 ]
 }
 ]
}`

```

New Policy with fine-grained permissions:

AWS

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
 "Resource": "arn:aws:artifact:::agreement/agreement-9c1kBcYznTkcpRIm"
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

AWS GovCloud (US)

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
 "Resource": "arn:aws-us-gov:artifact:::agreement/agreement-Og8HCNyYwYNp8AR1"
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

**Migrate resource specific permissions to download, accept and terminate agreements at organization level**

Legacy Policy:

AWS

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:AcceptAgreement",
 "artifact:DownloadAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": [
 "arn:aws:artifact::*:customer-agreement/*",
 "arn:aws:artifact:::agreement/AWS Organizations Business Associate Addendum"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "arn:aws:iam:::role/*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam:::role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
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

AWS GovCloud (US)

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "artifact:AcceptAgreement",
 "artifact:DownloadAgreement",
 "artifact:TerminateAgreement"
 ],
 "Resource": [
 "arn:aws-us-gov:artifact::*:customer-agreement/*",
 "arn:aws-us-gov:artifact:::agreement/AWS Organizations Business Associate Addendum"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:ListRoles",
 "Resource": "arn:aws-us-gov:iam:::role/*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws-us-gov:iam:::role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
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

New Policy with fine-grained permissions:

AWS

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
 "Resource": "arn:aws:artifact:::agreement/agreement-y03aUwMAEorHtqjv"
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
 "iam:CreateServiceLinkedRole"
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
 "Sid": "GetRoleToCheckForRoleExistence",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact"
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

AWS GovCloud (US)

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
 "Resource": "arn:aws-us-gov:artifact:::agreement/agreement-B47fK0ArVebC9XE1"
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
 "iam:CreateServiceLinkedRole"
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
 "Sid": "GetRoleToCheckForRoleExistence",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole"
 ],
 "Resource": "arn:aws-us-gov:iam::*:role/aws-service-role/artifact.amazonaws.com/AWSServiceRoleForArtifact"
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

## Legacy to Fine-grained resource mapping for Agreements

Agreement ARN's were updated for fine-grained permissions. Any previous references to legacy agreement resources should be replaced with new ARN's. Below is the Agreement ARN mapping between legacy to fine-grained resources.

AWS

| Agreement Name                                                | Artifact ARN for Legacy permissions                                                              | Artifact ARN for Fine-grained permissions                      |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ----------------- |
| AWS Business Associate Addendum                               | arn:aws:artifact:::agreement/AWS Business Associate Addendum                                     | arn:aws:artifact:::agreement/agreement-9c1kBcYznTkcpRIm        |
| AWS New Zealand Notifiable Data Breach Addendum               | arn:aws:artifact:::agreement/AWS New Zealand Notifiable Data Breach Addendum                     | arn:aws:artifact:::agreement/agreement-3YRq9rGUIu72r7Gt        |
| AWS Australian Notifiable Data Breach Addendum                | arn:aws:artifact:::agreement/AWS Australian Notifiable Data Breach Addendum                      | arn:aws:artifact:::agreement/agreement-sbLSDe8bitmAXNr9        |
| AWS SEC Rule 17a-4 Addendum                                   | arn:aws:artifact:::agreement/AWS SEC Rule 17a-4 Addendum                                         | arn:aws:artifact:::agreement/agreement-bexgr7sjvXAW4Gxu        |
| AWS SEC Rule 18a-6 Addendum                                   | arn:aws:artifact:::agreement/AWS SEC Rule 18a-6 Addendum                                         | arn:aws:artifact:::agreement/agreement-HZTdNwJuqOKLReXC        |
| AWS Organizations Business Associate Addendum                 | arn:aws:artifact:::agreement/AWS Organizations Business Associate Addendum                       | arn:aws:artifact:::agreement/agreement-y03aUwMAEorHtqjv        |
| AWS Organizations Australian Notifiable Data Breach Addendum  | arn:aws:artifact:::agreement/AWS Organizations Australian Notifiable Data Breach Addendum        | arn:aws:artifact:::agreement/agreement-YpDMFXTePE7kEg4b        |
| AWS Organizations New Zealand Notifiable Data Breach Addendum | arn:aws:artifact:::agreement/AWS Organizations New Zealand Notifiable Data Breach Addendum       | arn:aws:artifact:::agreement/agreement-uojEjr3vOnvrhV52        | AWS GovCloud (US) |
| Agreement Name                                                | Artifact ARN for Legacy permissions                                                              | Artifact ARN for Fine-grained permissions                      |
| ---                                                           | ---                                                                                              | ---                                                            |
| AWS Business Associate Addendum                               | arn:aws-us-gov:artifact:::agreement/AWS Business Associate Addendum                              | arn:aws-us-gov:artifact:::agreement/agreement-Og8HCNyYwYNp8AR1 |
| AWS Australian Notifiable Data Breach Addendum                | arn:aws-us-gov:artifact:::agreement/AWS Australian Notifiable Data Breach Addendum               | arn:aws-us-gov:artifact:::agreement/agreement-G1rBS2MGYjLiCCXy |
| AWS Organizations Business Associate Addendum                 | arn:aws-us-gov:artifact:::agreement/AWS Organizations Business Associate Addendum                | arn:aws-us-gov:artifact:::agreement/agreement-B47fK0ArVebC9XE1 |
| AWS Organizations Australian Notifiable Data Breach Addendum  | arn:aws-us-gov:artifact:::agreement/AWS Organizations Australian Notifiable Data Breach Addendum | arn:aws-us-gov:artifact:::agreement/agreement-OsnlbilP8RB73Nw5 |
