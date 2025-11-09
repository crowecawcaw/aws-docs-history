**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS managed policies for AWS Shield

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

## AWS managed policy: AWSShieldDRTAccessPolicy

This section explains how to use AWS managed policies for Shield.

AWS Shield uses this managed policy when you grant permission to the Shield Response Team (SRT) to act
on your behalf. This policy gives the SRT limited access to your AWS account, to assist
with DDoS attack mitigation during high-severity events. This policy allows the SRT to
manage your AWS WAF rules and Shield Advanced protections and to access your AWS WAF logs.

For information about granting permission to the SRT to operate on
your behalf, see [Granting access for the SRT](ddos-srt-access.md "ddos-srt-access.md").

For details about this policy, see [AWSShieldDRTAccessPolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy") in the IAM console.

## AWS managed policy: AWSShieldServiceRolePolicy

Shield Advanced uses this managed policy when you enable automatic application layer DDoS mitigation, to set the
permissions it needs to manage resources for your account. This
policy allows Shield Advanced to create and apply AWS WAF rules and rule groups in the web ACLs
that you've associated with your protected resources, to automatically respond to DDoS
attacks.

You can't attach AWSShieldServiceRolePolicy to your IAM entities. Shield attaches this
policy to the service-linked role `AWSServiceRoleForAWSShield` to allow Shield to perform
actions on your behalf.

Shield Advanced enables the use of this policy when you enable automatic application layer DDoS mitigation. For
more information about the use for this policy, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .

For information about the service-linked role AWSServiceRoleForAWSShield that uses this policy, see
[Using service-linked roles for
Shield Advanced](shd-using-service-linked-roles.md "shd-using-service-linked-roles.md")

For details about this policy, see [AWSShieldServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSShieldServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSShieldServiceRolePolicy") in the IAM console.

## Shield updates to AWS managed

policies

View details about updates to AWS managed policies for Shield since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Shield document history page at [Document history](doc-history.md "doc-history.md").

| Policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description of change                                                                                                                                                                                                                                                                                                                          | Date             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `AWSShieldServiceRolePolicy`<br>This policy allows Shield to access and manage AWS resources<br>in order to automatically<br>respond to application layer DDoS attacks on your behalf.<br>Details in IAM console: [AWSShieldServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSShieldServiceRolePolicy "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSShieldServiceRolePolicy")<br>The service-linked role `AWSServiceRoleForAWSShield` uses this policy. For information,<br>see [Using service-linked roles for<br>Shield Advanced](shd-using-service-linked-roles.md "shd-using-service-linked-roles.md"). | Added this policy to provide Shield Advanced with the permissions required for the<br>automatic application layer DDoS mitigation functionality.<br>For information about this feature, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") . | December 1, 2021 |
| Shield started tracking changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Shield started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                  | March 3, 2021    |
