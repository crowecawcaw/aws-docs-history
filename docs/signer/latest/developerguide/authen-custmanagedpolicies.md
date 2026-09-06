

# Customer managed policies for Signer
<a name="authen-custmanagedpolicies"></a>

Customer managed policies are standalone identity-based policies that an administrator creates and can attach to multiple users, groups, or roles in your AWS account. Administrators can manage and create policies using the [AWS Management Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html), the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-cli.html), or the [IAM API](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-api.html). 

**To manage policies in the AWS Management Console**

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.