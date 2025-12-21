# AWS managed policies for AWS Entity Resolution

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

AWSEntityResolutionConsoleFullAccess

You can attach the `AWSEntityResolutionConsoleFullAccess` policy to your
IAM identities.

This policy grants full access to AWS Entity Resolution endpoints and resources.

This policy also allows certain read access to related AWS services like S3, AWS Glue,
Tagging, AWS KMS, Amazon EventBridge, and AWS Data Exchange so that the console can display choices and use the selected ones to
perform entity resolution actions. Additionally, this policy grants access to Amazon Connect Customer Profiles APIs to enable integration for automated match result processing. Some resources are narrowed down to contain the
service name `entityresolution`.

Because AWS Entity Resolution relies on a passed role to perform actions on related AWS
resources, this policy also grants the permissions to select and pass a desired role.

**Permissions details**

This policy includes the following permissions.

- `EntityResolutionAccess` – Allows principals full access to
  AWS Entity Resolution endpoints and resources.
- `GlueSourcesConsoleDisplay` – Grants the access to list
  AWS Glue tables as data source options and import table schema of a data source for
  user experience.
- `S3BucketsConsoleDisplay` – Grants the access to list all S3
  buckets as data source options.
- `S3SourcesConsoleDisplay` – Grants the access to display S3
  buckets as data source options.
- `TaggingConsoleDisplay` – Grants the access to read tagging
  keys and values.
- `KMSConsoleDisplay` – Grants the access to describe keys and
  list aliases in AWS Key Management Service to decrypt and encrypt data sources.
- `ListRolesToPickForPassing` – Grants the access to list all
  roles so that the user can pick the role to be passed.
- `PassRoleToEntityResolutionService` – Grants the access to
  pass a narrowed down role to the AWS Entity Resolution service.
- `ManageEventBridgeRules` – Grants the access to create,
  update, and delete the Amazon EventBridge rule for getting S3 notifications.
- `ADXReadAccess` – Grants the access to AWS Data Exchange to verify if
  the customer has an entitlement or a subscription.
- `CustomerProfilesIntegrationAccess` – Grants access to Amazon Connect
  and Amazon Connect Customer Profiles APIs to enable integration between AWS Entity Resolution
  and Amazon Connect Customer Profiles for automated match result processing.

To view the permissions for this policy, see [AWSEntityResolutionConsoleFullAccess](../../../aws-managed-policy/latest/reference/AWSEntityResolutionConsoleFullAccess.md "../../../aws-managed-policy/latest/reference/AWSEntityResolutionConsoleFullAccess.md") in the _AWS
Managed Policy Reference_.

## AWS managed policy:

AWSEntityResolutionConsoleReadOnlyAccess

You can attach `AWSEntityResolutionConsoleReadOnlyAccess` to your IAM
entities.

This policy grants read-only access to AWS Entity Resolution endpoints and resources.

**Permissions details**

This policy includes the following permissions.

- `EntityResolutionRead` – Allows principals read-only access
  to AWS Entity Resolution endpoints and resources.

To view the permissions for this policy, see [AWSEntityResolutionConsoleReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSEntityResolutionConsoleReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSEntityResolutionConsoleReadOnlyAccess.md") in the _AWS Managed Policy Reference_.

## AWS Entity Resolution updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Entity Resolution since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the AWS Entity Resolution Document history page.

| Change                                                                | Description                                                                                                                                  | Date              |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `AWSEntityResolutionConsoleFullAccess` – Update to existing policy    | Added `CustomerProfilesIntegrationAccess` to enable integration with Amazon Connect Customer Profiles for automated match result processing. | December 15, 2025 |
| `AWSEntityResolutionConsoleFullAccess` – Update to<br>existing policy | Added `ADXReadAccess` and<br>`ManageEventBridgeRules` to enable the provider services<br>option in the matching workflow.                    | October 16, 2023  |
| AWS Entity Resolution started tracking changes                        | AWS Entity Resolution started tracking changes for its AWS managed<br>policies.                                                              | August 18, 2023   |
