

# Set up your account
<a name="set-up"></a>

This section describes what you need to do to use Amazon Location Service. You must have an AWS account and have set up access to Amazon Location for users that want to use it.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## I already have an AWS account
<a name="existing-user"></a>

**Grant access to Amazon Location Service**

Your non-admin users have no permissions by default. Before they can access Amazon Location, you must grant permission by attaching an IAM policy with specific permissions. Make sure to follow the principle of least privilege when granting access to resources. 

**Note**  
For information about giving unauthenticated users access to Amazon Location Service functionality (for example, in a web-based application), see [Authenticate with Amazon Location Service](access.md).

The following example policy gives a user permission to access all Amazon Location operations. For more examples, see [Identity-based policy examples for Amazon Location Service](security-iam.md#security_iam_id-based-policy-examples).

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Action": [
        "geo:*",
        "geo-maps:*",
        "geo-places:*",
        "geo-routes:*"
      ],
      "Resource": "*",
      "Effect": "Allow"
    }
  ]
}
```

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

When creating applications that use Amazon Location Service, you may need some users to have unauthenticated access. For these use cases, see [Enabling unauthenticated access using Amazon Cognito](authenticating-using-cognito.md).