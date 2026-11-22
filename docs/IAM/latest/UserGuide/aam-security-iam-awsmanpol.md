

# AWS managed policies for account access manager

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You can't change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

Each of the following managed policies is an alternative to assembling the equivalent inline policy by hand. Instead of combining the account access manager, IAM Identity Center, Identity Store, AWS Organizations, and AWS KMS actions shown in [Identity and access management for account access manager](aam-security.md#aam-security-iam), you can attach one of these job-aligned managed policies.

## AWS managed policy: AWSAccountAccessManagerAdministrator
<a name="aam-security-iam-awsmanpol-AWSAccountAccessManagerAdministrator"></a>

This policy provides administrative access to account access manager, including setting up account access manager in the AWS organization management account, registering a delegated administrator account, and managing user entitlements. It is intended for principals who perform the job role of an account access manager administrator. It includes the IAM Identity Center, Identity Store, AWS Organizations, and AWS KMS permissions required to administer the service. AWS might update this policy to support new account access manager features.

**Permissions groupings**

This policy is grouped into statements based on the set of permissions provided.
+ **account access manager** – Create and list account access manager applications; get and delete account access manager applications; create, delete, get, and list entitlements; and tag, untag, and list tags on account access manager applications.
+ **IAM Identity Center** – Describe and list IAM Identity Center instances, applications, and Regions. Create, configure, and delete the IAM Identity Center application for account access manager. These write actions are allowed only when an AWS service makes the request on your behalf (`aws:ViaAWSService`), not when you call them directly.
+ **Identity Store** – Describe and list users, groups, and group memberships, and describe, list, and search users and groups in the IAM Identity Center directory, so that the administrator can look up the workforce identities that entitlements are assigned to, including through the user and group picker in the AWS Management Console.
+ **AWS Organizations** – Read organization, account, organizational unit, root, and delegated administrator information. The policy also allows the administrator to register and deregister the account access manager delegated administrator and to enable and disable trusted service access, each scoped to the `account-access.amazonaws.com` service principal with the `organizations:ServicePrincipal` condition.
+ **AWS KMS** – Decrypt data that is protected with a customer managed key, scoped by the `kms:ViaService` condition to the IAM Identity Center and Identity Store service runtimes. This is required for IAM Identity Center instances that use customer managed keys for encryption.
+ **IAM** – Create the `AWSServiceRoleForAccountAccessManager` service-linked role so that account access manager can perform actions on your behalf. For more information, see [Security in account access manager](aam-security.md).

To view the permissions for this policy, see [AWSAccountAccessManagerAdministrator](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAccountAccessManagerAdministrator.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSAccountAccessManagerEntitlementManager
<a name="aam-security-iam-awsmanpol-AWSAccountAccessManagerEntitlementManager"></a>

This policy provides access to manage user entitlements in account access manager, including creating, deleting, and viewing entitlements, along with the read access needed to look up identities and organization details. It is intended for a delegated administrator or an access operator who assigns and removes user access but does not administer account access manager settings. Principals with this policy *cannot* create or delete account access manager applications or modify tags; those actions are reserved for the administrator. This enforces separation of duties between day-to-day access assignment and service configuration.

**Permissions groupings**

This policy is grouped into statements based on the set of permissions provided.
+ **account access manager** – Create, delete, get, and list entitlements; get and list applications; and list tags on applications.
+ **IAM Identity Center and Identity Store** – List IAM Identity Center instances and describe, list, and search users and groups so that the operator can find the identities to assign access to, including through the console picker.
+ **AWS Organizations** – Read organization, account, organizational unit, root, and delegated administrator information.

To view the permissions for this policy, see [AWSAccountAccessManagerEntitlementManager](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAccountAccessManagerEntitlementManager.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSAccountAccessManagerReadOnlyAccess
<a name="aam-security-iam-awsmanpol-AWSAccountAccessManagerReadOnlyAccess"></a>

This policy provides read-only access to account access manager, including viewing entitlements and the related information from IAM Identity Center, Identity Store, and AWS Organizations. It is intended for auditors and other principals who need visibility into who has access to what without any ability to make changes. Principals with this policy attached *cannot* make any create, delete, or tag changes.

**Permissions groupings**

This policy is grouped into statements based on the set of permissions provided.
+ **account access manager** – Get and list applications, get and list entitlements, and list tags.
+ **IAM Identity Center and Identity Store** – Describe IAM Identity Center instances, applications, and Regions, and list instances; and describe, list, and search users and groups in the identity store.
+ **AWS KMS** – Describe keys and list aliases so that customer managed keys used by account access manager can be displayed in the console.
+ **AWS Organizations** – Read organization, account, organizational unit, root, and delegated administrator information.

To view the permissions for this policy, see [AWSAccountAccessManagerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAccountAccessManagerReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## Account access manager updates to AWS managed policies
<a name="aam-security-iam-awsmanpol-updates"></a>

For automatic alerts about changes to this page, subscribe to the RSS feed on the [IAM document history page](document-history.md).