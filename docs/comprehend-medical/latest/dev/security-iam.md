

# Identity and access management in Amazon Comprehend Medical
<a name="security-iam"></a>

Access to Comprehend Medical requires credentials that AWS can use to authenticate your requests. Those credentials must have permissions to access Comprehend Medical actions. [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) can help secure your resources by controlling who can access them. The following sections provide details on how you can use IAM with Comprehend Medical. 
+  [Authentication](#auth-med) 
+  [Access Control](#access-control-med) 

## Authentication
<a name="auth-med"></a>

You must give users permissions to interact with Amazon Comprehend Medical. For users who need full access use `ComprehendMedicalFullAccess`.

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

To use Amazon Comprehend Medical's asynchronous operations you also need a service role.

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*. 

To learn more about specifying Amazon Comprehend Medical as the service in principal, see [Role-based Permissions required for batch operations](security-iam-permissions.md#auth-role-permissions-med).

## Access Control
<a name="access-control-med"></a>

 You must have valid credentials to authenticate your requests. The credentials must have permissions to call an Amazon Comprehend Medical action. 

 The following sections describe how to manage permissions for Amazon Comprehend Medical. We recommend that you read the overview first. 
+ [Overview of managing access permissions to Amazon Comprehend Medical resources](security-iam-accesscontrol.md)
+ [Using Identity-Based policies (IAM policies) for Amazon Comprehend Medical](security-iam-permissions.md)

**Topics**
+ [Authentication](#auth-med)
+ [Access Control](#access-control-med)
+ [Overview of managing access permissions to Amazon Comprehend Medical resources](security-iam-accesscontrol.md)
+ [Using Identity-Based policies (IAM policies) for Amazon Comprehend Medical](security-iam-permissions.md)
+ [Amazon Comprehend Medical API Permissions: actions, resources, and conditions reference](security-iam-resources.md)
+ [AWS managed policies for Amazon Comprehend Medical](security-iam-awsmanpol.md)