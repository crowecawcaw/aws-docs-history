# AWS managed policies for AWS Outposts

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

## AWS managed policy:

AWSOutpostsServiceRolePolicy

This policy is attached to a service-linked role that allows AWS Outposts to perform
actions on your behalf. For more information, see [Service-linked roles](using-service-linked-roles.md "using-service-linked-roles.md").

## AWS managed policy:

AWSOutpostsAuthorizeServerPolicy

Use this policy to grant the permissions required to authorize Outposts server hardware in your
on-premises network.

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "outposts:StartConnection",
 "outposts:GetConnection"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS Outposts updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Outposts since this service
began tracking these changes.

| Change                                                                                                                 | Description                                                                                                            | Date              |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSOutpostsAuthorizeServerPolicy](#AWSOutpostsAuthorizeServerPolicy "#AWSOutpostsAuthorizeServerPolicy") – New policy | AWS Outposts added a policy that grants permissions to authorize Outposts server hardware in your on-premises network. | January 4, 2023   |
| AWS Outposts started tracking changes                                                                                  | AWS Outposts started tracking changes for its AWS managed policies.                                                    | December 03, 2019 |
