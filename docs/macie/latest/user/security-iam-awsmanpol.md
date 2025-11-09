# AWS managed policies for Macie

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

Amazon Macie provides several AWS managed policies: the `AmazonMacieFullAccess`
policy, the `AmazonMacieReadOnlyAccess` policy, and the
`AmazonMacieServiceRolePolicy` policy.

###### Policies and updates

- [AmazonMacieFullAccess policy](#security-iam-awsmanpol-AmazonMacieFullAccess "#security-iam-awsmanpol-AmazonMacieFullAccess")
- [AmazonMacieReadOnlyAccess policy](#security-iam-awsmanpol-AmazonMacieReadOnlyAccess "#security-iam-awsmanpol-AmazonMacieReadOnlyAccess")
- [AmazonMacieServiceRolePolicy policy](#security-iam-awsmanpol-AmazonMacieServiceRolePolicy "#security-iam-awsmanpol-AmazonMacieServiceRolePolicy")
- [Updates to AWS managed policies for Macie](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy:

AmazonMacieFullAccess

You can attach the `AmazonMacieFullAccess` policy to your IAM
entities.

This policy grants full administrative permissions that allow an IAM identity
(_principal_) to create the [Amazon Macie service-linked role](service-linked-roles.md "service-linked-roles.md") and perform all read
and write actions for Amazon Macie. The permissions include mutating functions such as create,
update, and delete. If this policy is attached to a principal, the principal can create,
retrieve, and otherwise access all Macie resources, data, and settings for their
account.

This policy must be attached to a principal before the principal can enable Macie for
their account—a principal must be allowed to create the Macie service-linked role in
order to enable Macie for their account.

**Permissions details**

This policy includes the following permissions:

- `macie2` – Allows principals to perform all read and write
  actions for Amazon Macie.
- `iam` – Allows principals to create service-linked roles. The
  `Resource` element specifies the service-linked role for Macie. The
  `Condition` element uses the `iam:AWSServiceName`
  [condition
  key](../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md") and the `StringLike`
  [condition operator](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String") to restrict permissions to the service-linked role for
  Macie.
- `pricing` – Allows principals to retrieve pricing data for their
  AWS account from AWS Billing and Cost Management. Macie uses this data to calculate and display estimated
  costs when principals create and configure sensitive data discovery jobs.

To review the permissions for this policy, see [AmazonMacieFullAccess](../../../aws-managed-policy/latest/reference/AmazonMacieFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonMacieFullAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy:

AmazonMacieReadOnlyAccess

You can attach the `AmazonMacieReadOnlyAccess` policy to your IAM
entities.

This policy grants read-only permissions that allow an IAM identity (_principal_) to perform all read actions for Amazon Macie. The
permissions don't include mutating functions such as create, update, or delete. If this
policy is attached to a principal, the principal can retrieve but not otherwise access all
Macie resources, data, and settings for their account.

**Permissions details**

This policy includes the following permissions:

`macie2` – Allows principals to perform all read actions for
Amazon Macie.

To review the permissions for this policy, see [AmazonMacieReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonMacieReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonMacieReadOnlyAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy:

AmazonMacieServiceRolePolicy

You can't attach the `AmazonMacieServiceRolePolicy` policy to your IAM
entities.

This policy is attached to a service-linked role that allows Amazon Macie to perform
actions on your behalf. For more information, see [Using service-linked roles for Macie](service-linked-roles.md "service-linked-roles.md").

To review the permissions for this policy, see [AmazonMacieServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonMacieServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonMacieServiceRolePolicy.md") in the _AWS Managed
Policy Reference Guide_.

## Updates to AWS managed policies for

Macie

The following table provides details about updates to AWS managed policies for
Amazon Macie since this service began tracking these changes. For automatic alerts about
updates to the policies, subscribe to the RSS feed on the [Macie
document history](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  | Date           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [AmazonMacieReadOnlyAccess](#security-iam-awsmanpol-AmazonMacieReadOnlyAccess "#security-iam-awsmanpol-AmazonMacieReadOnlyAccess") – Added a<br>new policy | Macie added a new policy, the `AmazonMacieReadOnlyAccess` policy. This policy<br>grants read-only permissions that allow principals to retrieve all Macie<br>resources, data, and settings for their account.                                                                                                                                                                                                                                | June 15, 2023  |
| [AmazonMacieFullAccess](#security-iam-awsmanpol-AmazonMacieFullAccess "#security-iam-awsmanpol-AmazonMacieFullAccess") – Updated an<br>existing policy     | In the `AmazonMacieFullAccess` policy, Macie updated the<br>Amazon Resource Name (ARN) of the Macie service-linked role<br>(`aws-service-role/macie.amazonaws.com/AWSServiceRoleForAmazonMacie`).                                                                                                                                                                                                                                            | June 30, 2022  |
| [AmazonMacieServiceRolePolicy](service-linked-roles.md#slr-permissions "service-linked-roles.md#slr-permissions") – Updated<br>an existing policy          | Macie removed actions and resources for Amazon Macie Classic from the<br>`AmazonMacieServiceRolePolicy` policy. Amazon Macie Classic has<br>been discontinued and is no longer available.<br>More specifically, Macie removed all AWS CloudTrail actions. Macie also removed<br>all Amazon S3 actions for the following resources:<br>`arn:aws:s3:::awsmacie-*`,<br>`arn:aws:s3:::awsmacietrail-*`, and<br>`arn:aws:s3:::*-awsmacietrail-*`. | May 20, 2022   |
| [AmazonMacieFullAccess](#security-iam-awsmanpol-AmazonMacieFullAccess "#security-iam-awsmanpol-AmazonMacieFullAccess") – Updated an<br>existing policy     | Macie added an AWS Billing and Cost Management (`pricing`) action to the<br>`AmazonMacieFullAccess` policy. This action allows principals<br>to retrieve pricing data for their account. Macie uses this data to<br>calculate and display estimated costs when principals create and configure<br>sensitive data discovery jobs.<br>Macie also removed Amazon Macie Classic (`macie`) actions from<br>the `AmazonMacieFullAccess` policy.    | March 7, 2022  |
| [AmazonMacieServiceRolePolicy](service-linked-roles.md#slr-permissions "service-linked-roles.md#slr-permissions") – Updated<br>an existing policy          | Macie added Amazon CloudWatch Logs actions to the<br>`AmazonMacieServiceRolePolicy` policy. These actions allow<br>Macie to publish log events to CloudWatch Logs for sensitive data discovery<br>jobs.                                                                                                                                                                                                                                      | April 13, 2021 |
| Macie started tracking changes                                                                                                                             | Macie started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                 | April 13, 2021 |
