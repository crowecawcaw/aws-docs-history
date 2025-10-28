# How AWS Control Tower works

This section describes at a high level how AWS Control Tower works. Your landing zone is a
well-architected multi-account environment for all of your AWS resources. You can use this
environment to enforce compliance regulations on all of your AWS accounts.

## Structure of an AWS Control Tower Landing Zone

The structure of a landing zone in AWS Control Tower is as follows:

- **Root** – The parent that contains all
  other OUs in your landing zone.
- **Security OU** – This OU contains the Log
  Archive and Audit accounts. These accounts often are referred to as _shared accounts_. When you launch your landing zone,
  you can choose customized names for these shared accounts, and you have the
  option to bring existing AWS accounts into AWS Control Tower for security and logging.
  However, these cannot be renamed later, and existing accounts cannot be added
  for security and logging after initial launch.
- **Sandbox OU** – The Sandbox OU is created
  when you launch your landing zone, if you enable it. This and other registered OUs
  contain the enrolled accounts that your users work with to perform their AWS
  workloads.
- **IAM Identity Center directory** – By default, this directory houses
  your IAM Identity Center users. It defines the scope of permissions for each IAM Identity Center
  user. Optionally, you can choose to self-manage your identity and access control. For more information, see [Working with AWS IAM Identity Center and AWS Control Tower](sso.md "sso.md").
- **IAM Identity Center users** – These are the identities
  that your users can assume to perform their AWS workloads in your
  landing zone.

## What happens when you set up a landing zone

When you set up a landing zone, AWS Control Tower performs the following actions in your
management account on your behalf:

- Creates two AWS Organizations organizational units (OUs): Security, and Sandbox
  (optional), contained within the organizational root structure.
- Creates or adds two shared accounts in the Security OU: the Log Archive account and
  the Audit account.
- Creates a cloud-native directory in IAM Identity Center, with preconfigured groups and
  single sign-on access, if you choose the default AWS Control Tower configuration, or it allows you to self-manage your identity provider.
- Applies all mandatory, preventive controls to enforce policies.
- Applies all mandatory, detective controls to detect configuration
  violations.
- _Preventive controls are not applied to the management account._
- Except for the management account, controls are applied to the organization
  as a whole.

###### Safely Managing Resources Within Your AWS Control Tower Landing Zone and Accounts

- When you create your landing zone, a number of AWS resources are created. To use
  AWS Control Tower, you must not modify or delete these AWS Control Tower managed resources outside of
  the supported methods described in this guide. Deleting or modifying these resources
  will cause your landing zone to enter an unknown state. For details, see [Guidance for creating and modifying AWS Control Tower
  resources](getting-started-guidance.md "getting-started-guidance.md")
- When you enable optional controls (those with _strongly
  recommended or elective_ guidance), AWS Control Tower creates AWS resources
  that it manages in your accounts. Do not modify or delete resources created by
  AWS Control Tower. Doing so can result in the controls entering an unknown state.

## How AWS Control Tower works with StackSets

AWS Control Tower uses AWS CloudFormation StackSets to set up resources in your accounts, by default. Each
stack set has StackInstances that correspond to accounts, and to AWS Regions per
account. AWS Control Tower deploys one stack set instance per account and Region.

AWS Control Tower applies updates to certain accounts and AWS Regions selectively, based on
AWS CloudFormation parameters. When updates are applied to some stack instances, other stack
instances may be left in **Outdated** status. This behavior is expected
and normal.

When a stack instance goes into **Outdated** status, it usually means
that the stack corresponding to that stack instance is not aligned with the latest
template in the stack set. The stack remains in the older template, so it might not
include the latest resources or parameters. The stack is still completely usable.

Here's a quick summary of what behavior to expect, based on AWS CloudFormation
parameters that are specified during an update:

If the stack set update includes changes to the template (that is, if the
`TemplateBody` or `TemplateURL` properties are specified), or
if the `Parameters` property is specified, AWS CloudFormation marks all stack
instances with a status of **Outdated** prior to updating the stack
instances in the specified accounts and AWS Regions. If the stack set update does not
include changes to the template or parameters, AWS CloudFormation updates the stack
instances in the specified accounts and Regions, while leaving all other stack instances
with their existing stack instance status. To update all of the stack instances
associated with a stack set, do not specify the `Accounts` or
`Regions` properties.

For more information, see [Update Your Stack
Set](../../../AWSCloudFormation/latest/UserGuide/stacksets-update.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-update.md") in the AWS CloudFormation User Guide.
