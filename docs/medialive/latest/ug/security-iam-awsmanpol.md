# AWS managed policies for AWS Elemental MediaLive

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

MediaLiveReadOnlyPolicy

You can attach the `MediaLiveReadOnlyPolicy` policy to your IAM
identities.

This policy provides read only access to AWS Elemental MediaLive. You can attach
`MediaLiveReadOnlyPolicy` to users, groups, and roles.

**Permissions details**

This policy includes the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSElementalMediaLiveReadOnly",
 "Effect": "Allow",
 "Action": [
 "medialive:Get*",
 "medialive:List*",
 "medialive:Describe*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## MediaLive updates to AWS managed

policies

View details about updates to AWS managed policies for MediaLive since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the MediaLive [document history](doc-history.md "doc-history.md") page.

| Change                                                                      | Description                                                                                      | Date          |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------- |
| The MediaLive managed policy **MediaLiveReadOnlyPolicy**<br>has been added. | This policy grants permission to register MediaLive Gateway Instances to<br>a MediaLive Gateway. | July 12, 2024 |
| MediaLive started tracking changes                                          | MediaLive started tracking changes for its AWS managed policies.                                 | July 12, 2024 |
