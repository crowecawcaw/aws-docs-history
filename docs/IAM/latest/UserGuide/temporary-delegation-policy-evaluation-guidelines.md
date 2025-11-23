# Policy evaluation guidelines

AWS will evaluate your submitted policies against a set of guidelines. The same evaluation guidelines apply to both policy templates and permission boundaries, with minor differences noted where appropriate.

For the purposes of evaluation, we separate services into distinct groups. The most important distinction is for security-sensitive services, which manage access, credentials, and keys. Policies granting access to these services need to be focused narrowly on the work being done. Security-sensitive services include the following: AWS Identity and Access Management (IAM), AWS Key Management Service (KMS), AWS Resource Access Manager (RAM), AWS IAM Identity Center, AWS Organizations, and AWS Secrets Manager.

A secondary distinction is services that can access data across account boundaries. Policies for these services must include protections to prevent unintentional cross-account access.

## Common validations

All policy statements must follow these guidelines:

- All statements must include Effect, Action (or NotAction), Resource, and Condition fields in that order
- All actions within a single statement must be listed alphabetically
- All ARNs included in the policy must follow the syntax defined in public documentation for the relevant services
- NotAction fields can only be used in Deny statements
- Actions in Allow statements must include a service code. Generic wildcards ("\*") are not allowed

## Security-sensitive service restrictions

The following restrictions apply to security-sensitive services mentioned above:

- Actions in Allow statements must be more specific than [service]:\*
- Actions in Allow statements for temporary access policy templates must not contain wildcards
- Sensitive actions, such as iam:PassRole or iam:CreateServiceLinkedRole, require additional scoping, such as specific resources or conditional checks. These actions include:
  - IAM role passing
  - IAM role modification actions
  - IAM policy modification actions
  - AWS KMS write or cryptographic operations
  - AWS RAM write or share operations
  - AWS Secrets Manager operations for retrieving or modifying secrets, or modifying resource policies

- Other actions may use a wildcard resource, such as iam:ListUsers or iam:GetPolicy
- Actions that manage credentials, such as iam:CreateAccessKey, are blocked

## IAM-specific restrictions

For IAM:

- Only limited write operations are allowed for IAM roles and policies. You can not request permissions on other IAM resources such as users, groups, and certificates.
- Policy attachment or inline policy management actions are limited to roles with a permission boundary. Permission boundaries must be partner-supplied or on a list of allowed AWS managed policies. AWS managed policies may be allowed if they do not grant highly privileged or administrative permissions. For example, AWS managed policies for specific job functions or the SecurityAudit policy may be acceptable. AWS will review each AWS managed policy on a case-by-case basis during the onboarding process.
- Policy management is only allowed for policies with a partner-specific path: arn:aws:iam::@{AccountId}:policy/partner_domain.com/[feature]\*
- Tags may only be applied during resource creation, and only for roles and policies
- iam:PassRole checks must match a specific name or path prefix

## AWS STS-specific restrictions

For AWS STS:

- sts:AssumeRole must be scoped to a specific role ARN, role ARN prefix, or limited to a set of accounts or organization ID/organizational unit

## IAM Identity Center restrictions

For AWS IAM Identity Center, the following actions are blocked:

- All actions dealing with permissions management (e.g., sso:AttachCustomerManagedPolicyReferenceToPermissionSet)
- User, group, and membership modifications for AWS Identity Store
- Tag management

## AWS Organizations restrictions

For AWS Organizations, only read actions will be allowed.

## Additional service-specific validations

- Actions that acquire secrets or credentials, such as glue:GetConnection or redshift:GetClusterCredentials, must have conditions matching either full ARNs, ARN prefixes, or tags
- For Amazon Redshift: redshift:GetClusterCredentials is only allowed on a specific database name, and redshift:GetClusterCredentialsWithIAM is only allowed on a specific workgroup name

###### Note

When managing IAM resources in the account, we recommend using a path that indicates your name, e.g., arn:aws:iam::111122223333:role/partner.com/rolename. This will help differentiate the resources associated with your integration and make discovery, audit, and analysis easier for customers.

## Cross-account access requirements

Statements that potentially allow cross-account access must include at least one of the following:

- A condition specifying the account or organization for the resource (e.g., aws:ResourceOrgId matching one or more expected values)
- A Resource field that includes a specific account (e.g., arn:aws:sqs:\*:111122223333:\*)
- A Resource field that includes a non-wildcard account and a full resource name (e.g., arn:aws:s3:::full-bucket-name)

###### Note

Cross-account access is a sensitive capability that requires clear business justification. AWS will carefully review the need for cross-account access during the onboarding process.
