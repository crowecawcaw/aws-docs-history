

# Manage user permissions for Amazon GameLift Servers FleetIQ
<a name="gsg-iam-permissions-users"></a>

Create additional users or extend Amazon GameLift Servers FleetIQ access permissions to existing users as needed. Users who work with Amazon GameLift Servers FleetIQ game server groups and the related Amazon EC2 and Auto Scaling services must have permissions to access these services.

As a best practice ([ Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)), apply least-privilege permissions for all users. You can set permissions for individual users or user groups and limit user access by service, action, or resource. 

Use the following instructions to set user permissions based on how you manage the users in your AWS account. If you use IAM users, as a best practice always attach permissions to roles or user groups, not individual users.
+ [Permissions syntax for users](gsg-iam-permissions-users-policy.md)
+ [Additional permissions syntax for use with CloudFormation](gsg-iam-permissions-users-policycfn.md)

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.