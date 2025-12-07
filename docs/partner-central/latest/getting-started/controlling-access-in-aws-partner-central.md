# Controlling access in AWS Partner Central

User access to AWS Partner Central is managed through AWS Identity and Access Management (IAM). AWS IAM is an AWS service that helps you control access to AWS resources. If you are an administrator, you control who can be authenticated (signed in) and authorized (have permissions) to use AWS Partner Central and AWS Marketplace resources. IAM is an AWS service that you can use with no additional charge.

Users are assigned to specific roles or groups that are associated with a set of managed policies. These managed policies determine which AWS Partner Central resources (i.e. Opportunities, Solutions, Fund Requests, etc.) a given user has access to, and what level of access they are allowed (i.e. read or write). AWS has published several managed policies to simplify user management for common user personas within AWS Partner Central, however organizations have the ability to create and customize managed policies to tailor access as needed. For more information, see [AWS managed policies for AWS Partner Central users](managed-policies.md "managed-policies.md").

You can modify IAM permissions whenever needed, and there's no cap on how many users can receive access rights.

###### Note

Working with AWS IAM requires specific technical knowledge and appropriate AWS account permissions. These individuals ('IAM Administrators') are required to support set up and management of these permissions. If users are not properly provisioned access in IAM, they will not be able to access features in AWS Partner Central.

The following resources provide more information about getting started and using IAM:

- [Create an administrative user](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md")
- [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_managed-using.md "../../../IAM/latest/UserGuide/access_policies_managed-using.md")
- [Attaching a policy to an IAM user group](../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md "../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md")
- [IAM Identities (users, groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md")
- [Controlling access to AWS resources using policies](../../../IAM/latest/UserGuide/access_permissions.md "../../../IAM/latest/UserGuide/access_permissions.md")
- [Actions, resources, and condition keys for AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md")

###### Topics

- [Permissions for AWS Partner Central](#permissions-for-aws-partner-central "#permissions-for-aws-partner-central")
- [Condition keys for AWS Partner Central](#condition-keys-for-aws-partner-central "#condition-keys-for-aws-partner-central")

## Permissions for AWS Partner Central

You can use the following permissions in IAM policies for AWS Partner Central. You can combine permissions into a single IAM policy to grant the permissions you want.

### ListPartnerPaths

`ListPartnerPaths` provides access to list partner paths in AWS Partner Central.

- **Action groups:** `ListOnly`, `ReadOnly`, `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### EnrollInPartnerPath

`EnrollInPartnerPath` provides access to enroll in partner paths in AWS Partner Central.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetPartnerDashboard

`GetPartnerDashboard` provides access to retrieve partner dashboard information in AWS Partner Central.

- **Action groups:** `ReadOnly`, `ReadWrite`
- **Required resources:** `arn:${Partition}:partnercentral::${Account}:catalog/${Catalog}/ReportingData/${TableId}/Dashboard/${DashboardId}`
- **Condition keys:** `partnercentral:Catalog`

### CreateBusinessPlan

`CreateBusinessPlan` provides access to create business plans in AWS Partner Central.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### PutBusinessPlan

`PutBusinessPlan` provides access to update business plans in AWS Partner Central.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### ListBusinessPlans

`ListBusinessPlans` provides access to list business plans in AWS Partner Central.

- **Action groups:** `ListOnly`, `ReadOnly`, `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetBusinessPlan

`GetBusinessPlan` provides access to retrieve business plan details in AWS Partner Central.

- **Action groups:** `ReadOnly`, `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### CreateCollaborationChannelRequest

`CreateCollaborationChannelRequest` provides access to create collaboration channel requests in AWS Partner Central.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### ListCollaborationChannels

`ListCollaborationChannels` provides access to list collaboration channels in AWS Partner Central.

- **Action groups:** `ListOnly`, `ReadOnly`, `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetCollaborationChannel

`GetCollaborationChannel` provides access to retrieve collaboration channel details in AWS Partner Central.

- **Action groups:** `ReadOnly`, `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### CreateCollaborationChannelMembers

`CreateCollaborationChannelMembers` provides access to create collaboration channel members in AWS Partner Central.

- **Action groups:** `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### SearchPartnerProfiles

`SearchPartnerProfiles` provides access to search public partner profiles in AWS Partner Central.

- **Action groups:** `ListOnly`, `ReadOnly`, `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetPartnerProfile

`GetPartnerProfile` provides access to retrieve public partner profile details in AWS Partner Central.

- **Action groups:** `ReadOnly`, `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.

### GetProgramManagementAccount

`GetProgramManagementAccount` provides access to retrieve program management account details in AWS Partner Central.

- **Action groups:** `ReadOnly`, `ReadWrite`
- **Required resources:** Does not support specifying a resource Amazon Resource Number (ARN) in the `Resource` element of an IAM policy statement. To allow access, specify `"Resource": "*"` in your policy.
- **Condition keys:** `partnercentral:Catalog`

## Condition keys for AWS Partner Central

AWS Partner Central defines the following condition keys that you can use in the `Condition` element of an IAM policy.

### partnercentral:Catalog

Filters access by a specific Catalog.

- **Type:** `String`

**Valid values:** `[AWS | Sandbox]`

### partnercentral:RelatedEntityType

Filters access by entity types for Opportunity association.

- **Type:** `String`

**Valid values:** `[Solutions | AwsProducts | AwsMarketplaceOffers]`

### partnercentral:ChannelHandshakeType

Filters access by channel handshake types.

- **Type:** `String`

**Valid values:** `[START_SERVICE_PERIOD | REVOKE_SERVICE_PERIOD | PROGRAM_MANAGEMENT_ACCOUNT]`

### partnercentral:VerificationType

Filters access by the type of verification being performed.

- **Type:** `String`

**Valid values:** `[BUSINESS_VERIFICATION | REGISTRANT_VERIFICATION]`

### partnercentral:FulfillmentTypes

Filters access by benefit fulfillment types.

- **Type:** `ArrayOfString`

**Valid values:** `[CREDITS | CASH | ACCESS]`

### partnercentral:Programs

Filters access by program.

- **Type:** `ArrayOfString`
