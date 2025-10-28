# AWS managed policies for Amazon Comprehend Medical

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

###### Topics

- [AWS managed policy: ComprehendMedicalFullAccess](#security-iam-awsmanpol-ComprehendMedicalFullAccess "#security-iam-awsmanpol-ComprehendMedicalFullAccess")
- [Comprehend Medical updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy: ComprehendMedicalFullAccess

You can attach the `ComprehendMedicalFullAccess` policy to your IAM identities.

This policy grants administrative permission to all Comprehend Medical actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Action" : [
 "comprehendmedical:*"
 ],
 "Effect" : "Allow",
 "Resource" : "*"
 }
 ]
}`

```

## Comprehend Medical updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon Comprehend Medical since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the [Document history](comprehendmedical-releases.md "comprehendmedical-releases.md") page.

| Change                                      | Description                                                               | Date              |
| ------------------------------------------- | ------------------------------------------------------------------------- | ----------------- |
| Comprehend Medical started tracking changes | Comprehend Medical started tracking changes for its AWS managed policies. | November 27, 2018 |
