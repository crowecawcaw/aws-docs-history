On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# AWS managed policies for Amazon CodeGuru Security

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your account, are
specific to CodeGuru Security.

###### Topics

- [AmazonCodeGuruSecurityFullAccess](#security-iam-awsmanpol-AmazonCodeGuruSecurityFullAccess "#security-iam-awsmanpol-AmazonCodeGuruSecurityFullAccess")
- [AmazonCodeGuruSecurityScanAccess](#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess "#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess")
- [CodeGuru Security updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AmazonCodeGuruSecurityFullAccess

You can attach the `AmazonCodeGuruSecurityFullAccess` policy to your IAM identities.

This policy grants full access to Amazon CodeGuru Security.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonCodeGuruSecurityFullAccess",
 "Effect": "Allow",
 "Action": [
 "codeguru-security:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AmazonCodeGuruSecurityScanAccess

You can attach the `AmazonCodeGuruSecurityScanAccess` policy to your IAM identities.

This policy grants permissions that allow a user to work with scans, including creating
scans, viewing scan information, and viewing scan findings.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonCodeGuruSecurityScanAccess",
 "Effect": "Allow",
 "Action": [
 "codeguru-security:CreateScan",
 "codeguru-security:CreateUploadUrl",
 "codeguru-security:GetScan",
 "codeguru-security:GetFindings"
 ],
 "Resource": "arn:aws:codeguru-security:*:*:scans/*"
 }
 ]
}`

```

## CodeGuru Security updates to AWS managed

policies

View details about updates to AWS managed policies for CodeGuru Security since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the [CodeGuru Security Document history](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                               | Description                                                                                                   | Date         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------ |
| [AmazonCodeGuruSecurityScanAccess](#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess "#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess") – New policy | CodeGuru Security added a new policy that grants permissions to create and view scans and view scan findings. | May 10, 2023 |
| [AmazonCodeGuruSecurityFullAccess](#security-iam-awsmanpol-AmazonCodeGuruSecurityFullAccess "#security-iam-awsmanpol-AmazonCodeGuruSecurityFullAccess") – New policy | CodeGuru Security added a new policy to allow full access to CodeGuru Security.                               | May 10, 2023 |
| CodeGuru Security started tracking changes                                                                                                                           | CodeGuru Security started tracking changes for its AWS managed policies.                                      | May 10, 2023 |
