

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Prerequisites for setting up AWS Audit Manager
<a name="setup-prerequisites"></a>



Before you can use AWS Audit Manager, you must make sure that you have properly set up your AWS account and user permissions. 

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Add the required permissions to access and enable Audit Manager](#attach-IAM)
+ [Next steps](#setup-prerequisites-next-steps)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Add the required permissions to access and enable Audit Manager
<a name="attach-IAM"></a>

You must give users the required permissions to enable Audit Manager. For users who need full access to Audit Manager, use the [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) managed policy. This is an AWS managed policy that’s available in your AWS account, and it’s the recommended policy for Audit Manager administrators. 

**Tip**  
As a security best practice, we recommend that you get started with AWS managed policies and then move toward least-privilege permissions. AWS managed policies grant permissions for many common use cases. However, keep in mind that because AWS managed policies are available for use by all AWS customers, they might not grant least-privilege permissions for your specific use cases. As a result, we recommend that you reduce permissions further by defining [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *AWS Identity and Access Management User Guide.*

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

## Next steps
<a name="setup-prerequisites-next-steps"></a>

Now that you've set up your AWS account and granted the required permissions, you're ready to enable Audit Manager. For step-by-step instructions, see [Enabling AWS Audit Manager](setup-audit-manager.md).