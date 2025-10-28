# AWS managed policies for AWS End User Messaging SMS

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

## AWS managed policy: SMSVoiceServiceRolePolicy

This policy is attached to a service-linked role that allows the service to
perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

This policy allows SMSVoice to put metric data into the `AWS/SMSVoice` CloudWatch namespaces.

For details about this policy, see [SMSVoiceServiceRolePolicy](../../../aws-managed-policy/latest/reference/SMSVoiceServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/SMSVoiceServiceRolePolicy.md").

## AWS End User Messaging SMS updates to AWS managed

policies

View details about updates to AWS managed policies for AWS End User Messaging SMS since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS End User Messaging SMS Document history page.

| Change                                                                                                                                                                                          | Description                                                                                                                                                                                                                        | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| AWS End User Messaging SMS started tracking changes                                                                                                                                             | AWS End User Messaging SMS started tracking changes for its AWS managed policies.                                                                                                                                                  | November 15, 2024 |
| [SMSVoiceServiceRolePolicy](../../../aws-managed-policy/latest/reference/SMSVoiceServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/SMSVoiceServiceRolePolicy.md") - New Policy | This policy allows SMSVoice to put metric data into the `AWS/SMSVoice` CloudWatch namespaces. The service-linked role [AWSServiceRoleForSMSVoice](using-service-linked-roles.md "using-service-linked-roles.md") uses this policy. | November 15, 2024 |
