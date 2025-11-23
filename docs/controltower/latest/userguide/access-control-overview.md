# Overview of managing access permissions to

your AWS Control Tower resources

Every AWS resource is owned by an AWS account, and permissions to create or gain
access to a resource are governed by permissions policies. An account administrator can
attach permissions policies to IAM identities (that is, users, groups, and roles).
Some services (such as AWS Lambda) also support attaching permissions policies to
resources.

###### Note

An _account administrator_ (or administrator) is a user with
administrator privileges. For more information, see [IAM Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

When you are responsible for granting permissions to a user or role, you must know and
track the _users and roles_ that require permissions,
the _resources_ for which each user and role requires
permissions, and the _specific actions_ that must be
allowed for operating those resources.

###### Topics

- [AWS Control Tower resources and operations](#access-control-resources "#access-control-resources")
- [About resource ownership](#access-control-owner "#access-control-owner")
- [Manage access to
  resources](access-control-manage-access-intro.md "access-control-manage-access-intro.md")
- [Specify policy
  elements: Actions, Effects, and Principals](#access-control-specify-controltower-actions "#access-control-specify-controltower-actions")
- [Specifying conditions in a policy](#specifying-conditions "#specifying-conditions")

## AWS Control Tower resources and operations

In AWS Control Tower, the primary resource is a _landing zone_. AWS Control Tower also
supports an additional resource type, _controls_, sometimes
referred to as _guardrails_. However, for AWS Control Tower,
you can manage controls only in the context of an existing landing zone. Controls can be
referred to as a _subresource_.

Resources and subresources in AWS have unique Amazon Resource Names (ARNs)
associated with them, as shown in the following example.

| Resource Type | ARN Format                                                                     |
| ------------- | ------------------------------------------------------------------------------ |
| File system   | `arn:aws:elasticfilesystem:`region`:`account-id`:file-system/`file-system-id`` |

AWS Control Tower provides a set of API operations to work with AWS Control Tower resources. For a
list of available operations, see AWS Control Tower [the AWS Control Tower API
Reference](../APIReference/API_Operations.md "../APIReference/API_Operations.md").

For more information about the CloudFormation resources in AWS Control Tower, see [the AWS CloudFormation
User Guide](../../../AWSCloudFormation/latest/UserGuide/AWS_ControlTower.md "../../../AWSCloudFormation/latest/UserGuide/AWS_ControlTower.md").

## About resource ownership

The AWS account owns the resources that are created in the account, regardless
of who created the resources. Specifically, the resource owner is the AWS account
of the [principal
entity](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md") (that is, the AWS account root user, an IAM Identity Center user, an IAM user,
or an IAM role) that authenticates the resource creation request. The following
examples illustrate how this works:

- If you use the AWS account root user credentials of your AWS account to
  set up a landing zone, your AWS account is the owner of the resource.
- If you create an IAM user in your AWS account and grant permissions to
  set up a landing zone to that user, the user can set up a landing zone as long as
  their account meets the prerequisites. However, your AWS account, to which
  the user belongs, owns the landing zone resource.
- If you create an IAM role in your AWS account with permissions to set
  up a landing zone, anyone who can assume the role can set up a landing zone. Your
  AWS account, to which the role belongs, owns the landing zone resource.

## Specify policy

elements: Actions, Effects, and Principals

You can set up and manage your landing zone through the AWS Control Tower console, or [the landing zone APIs](../APIReference/API_Operations.md "../APIReference/API_Operations.md"). To set up your landing zone, you must be an
IAM user with administrative permissions as defined in a IAM policy.

The following elements are the most basic ones you can identify in a
policy:

- **Resource** – In a policy, you use an
  Amazon Resource Name (ARN) to identify the resource to which the policy
  applies. For more information, see [AWS Control Tower resources and operations](#access-control-resources "#access-control-resources").
- **Action** – You use action keywords
  to identify resource operations that you want to allow or deny. For
  information about types of actions available to be performed, see [Actions defined by AWS Control Tower](../../../service-authorization/latest/reference/list_awscontroltower.md#awscontroltower-actions-as-permissions "../../../service-authorization/latest/reference/list_awscontroltower.md#awscontroltower-actions-as-permissions").
- **Effect** – You specify the effect
  when the user requests the specific action—this can be either allow
  or deny. If you don't explicitly grant access to (allow) a resource, access
  is implicitly denied. You can also explicitly deny access to a resource,
  which you might do to make sure that a user cannot access it, even if a
  different policy grants access.
- **Principal** – In identity-based
  policies (IAM policies), that user to which the policy is attached is the
  implicit principal. For resource-based policies, you specify the user,
  account, service, or other entity that you want to receive permissions
  (applies to resource-based policies only). AWS Control Tower doesn't support
  resource-based policies.

To learn more about IAM policy syntax and descriptions, see [AWS IAM Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")
in the _IAM User Guide_.

## Specifying conditions in a policy

When you grant permissions, you can use the IAM policy language to specify the
conditions when a policy should take effect. For example, you might want a policy to
be applied only after a specific date. For more information about specifying
conditions in a policy language, see [Condition](../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition "../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition")
in the _IAM User Guide_.

To express conditions, you can use predefined condition keys. There are no
condition keys specific to AWS Control Tower. However, there are AWS-wide condition keys
that you can use as appropriate. For a complete list of AWS-wide keys, see [Available
Keys for Conditions](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.
