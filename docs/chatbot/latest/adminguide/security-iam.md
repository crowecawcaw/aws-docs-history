AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Identity and Access Management for Amazon Q Developer in chat applications

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use Amazon Q Developer resources. IAM is an AWS service that you can
use with no additional charge.

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshooting Amazon Q Developer in chat applications
  identity and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md"))
- **Service administrator** - determine user access and
  submit permission requests (see [How Amazon Q Developer in chat applications works with
  IAM](#security_iam_service-with-iam "#security_iam_service-with-iam"))
- **IAM administrator** - write policies to manage
  access (see [Identity-based policies for
  Amazon Q Developer in chat applications](security_iam_service-with-iam-id-based-policies.md#security_iam_id-based-policy-examples "security_iam_service-with-iam-id-based-policies.md#security_iam_id-based-policy-examples"))

## How Amazon Q Developer in chat applications works with

IAM

Before you use IAM to manage access to Amazon Q Developer, you should understand which
IAM features are available to use with Amazon Q Developer. The following subsections
introduce each IAM capability supported by Amazon Q Developer in chat applications, point you to further information about
how to use them, and describe the IAM capabilities that Amazon Q Developer in chat applications doesn't support. To get a
high-level view of how Amazon Q Developer and other AWS services work with IAM, see
[AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

For an overview of IAM and its features, see [Understanding How IAM Works](../../../IAM/latest/UserGuide/intro-structure.md "../../../IAM/latest/UserGuide/intro-structure.md") in the
_IAM User Guide_.

###### Topics

- [Identity-based policies and
  Amazon Q Developer in chat applications](#identity-based-policies-use-in-chatbot "#identity-based-policies-use-in-chatbot")
- [Resource-level permissions and
  Amazon Q Developer in chat applications](#resource-based-policies-use-in-chatbot "#resource-based-policies-use-in-chatbot")
- [Condition keys and Amazon Q Developer in chat applications](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys")
- [Using temporary
  credentials with Amazon Q Developer](#security_iam_service-with-iam-roles-tempcreds "#security_iam_service-with-iam-roles-tempcreds")
- [Service-linked
  roles](#security_iam_service-with-iam-roles-service-linked "#security_iam_service-with-iam-roles-service-linked")
- [Service roles](#security_iam_service-with-iam-roles-service "#security_iam_service-with-iam-roles-service")
- [Other policy types](#security-iam-other-policies "#security-iam-other-policies")

### Identity-based policies and

Amazon Q Developer in chat applications

Amazon Q Developer in chat applications supports the use of IAM identity-based policies for service usage and
management.

An AWS Identity and Access Management (IAM) _policy_ is a document that
defines the permissions that apply to an IAM user, group, or role. The permissions
determine what users can do in AWS. A policy typically allows access to specific
actions, and can optionally grant that the actions are allowed for specific resources,
like Amazon Simple Notification Service (Amazon SNS) notifications. Policies can also explicitly deny access.

_Identity-based policies_ are attached to an IAM
user, group, or role (identity). These policies let you specify what that AWS identity
can do (its permissions). For example, you can attach an identity policy to the IAM
user named adesai, to allow that user to perform the Amazon Q Developer in chat applications
`DescribeSlackChannels` action.

For information about, and examples of, using identity-based policies with Amazon Q Developer in chat applications, see
[Amazon Q Developer
Identity-Based Policies](security_iam_service-with-iam-id-based-policies.md "security_iam_service-with-iam-id-based-policies.md").

For more general information about how IAM identity-based policies work, see [Identity vs.
Resource](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") in the _IAM User Guide_.

### Resource-level permissions and

Amazon Q Developer in chat applications

_Resource-level permissions_ are JSON policy statements that
specify the AWS resources on which associated IAM entities can perform actions.
You define a resource-level permission in an IAM policy,
then attach the policy to a user's AWS account or to any other IAM entity. The users
then have permission to access that resource. Resource-level permissions differ from
IAM _resource-based policies_ because you attach complete
resource-based policies directly to an AWS resource.

When you customize IAM policies for users to work with the Amazon Q Developer in chat applications service, one of
your primary options for policy editing is to configure resource-based permissions
for your policies.

Amazon Q Developer in chat applications supports resource-level permissions, but not resource-based policies.

For more information about how IAM resource-level permissions work with Amazon Q Developer in chat applications, see
[IAM Resource-Level Permissions for Amazon Q Developer in chat applications](security_iam_service-with-iam-resource-based-policies.md "security_iam_service-with-iam-resource-based-policies.md").

###

Condition keys and Amazon Q Developer in chat applications

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon Q Developer doesn't define any
service-specific condition keys. It supports global condition keys. To see all actions
and resources for which Amazon Q Developer in chat applications can use global condition keys, see [Actions, Resources,
and Condition Keys for Amazon Q Developer in chat applications](../../../IAM/latest/UserGuide/list_awschatbot.md#awschatbot-policy-keys "../../../IAM/latest/UserGuide/list_awschatbot.md#awschatbot-policy-keys") in the _IAM User Guide_.
For more information about AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

### Using temporary

credentials with Amazon Q Developer

You can use temporary credentials to sign in with federation, assume an IAM role,
or assume a cross-account role. You obtain temporary security credentials by calling
AWS Security Token Service (AWS STS) API operations, such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon Q Developer supports using temporary credentials. For more information about
defining and using temporary IAM credentials, see [Temporary Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md")
in the _IAM User Guide_.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your IAM
account and are owned by the service. An IAM administrator can view, but can't edit
the permissions for service-linked roles.

### Service roles

Amazon Q Developer supports service roles.

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your IAM
account and are owned by the account. This means that an IAM administrator can change
the permissions for this role. However, doing so might prevent the service from
functioning as expected.

### Other policy types

AWS supports additional, less common policy types. These policy types can set the maximum permissions granted to you by the more common policy types.

- **AWS Organizations service control policies (SCPs)** - SCPs are JSON policies that specify the maximum permissions for an organization or
  organizational unit (OU) in AWS Organizations. AWS Organizations is a service for grouping and centrally managing multiple AWS accounts that your business owns.
  If you enable all features in an organization, then you can apply service control policies (SCPs) to any or all of your accounts. The SCP limits permissions
  for entities in member accounts, including each AWS account root user. For more information about Organizations and SCPs, see
  [How SCPs Work](../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md "../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md") in the _AWS Organizations User Guide_.
- **IAM account settings** - With IAM, you can use AWS Security Token Service (AWS STS) to create and provide trusted users with temporary security credentials that can
  control access to your AWS resources. When you activate STS endpoints for a Region, AWS STS can issue temporary credentials to users and roles in your account that make an AWS STS request.
  Those credentials can then be used in any Region that is enabled by default or is manually enabled. You must activate the Region in the account where the temporary credentials are generated.
  It does not matter whether a user is signed into the same account or a different account when they make the request.
  For more information, see [Activating and deactivating AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate")
  in the _IAM User Guide_.

###### Note

Amazon Q Developer in chat applications is a global service that requires access to all AWS Regions. If there is a policy in place that prevents access to services in certain Regions,
you must change the policy to allow global Amazon Q Developer in chat applications access.
