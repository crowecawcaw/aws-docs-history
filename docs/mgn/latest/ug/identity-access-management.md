

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Identity and access management for AWS Transform MGN
<a name="identity-access-management"></a>

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be authenticated (signed in) and authorized (have permissions) to use AWS resources. IAM enables you to create users and groups under your AWS account. You control the permissions that users have to perform tasks using AWS resources. You can use IAM for no additional charge. 

By default, users created via the IAM service don't have permissions for AWS Transform MGN resources and operations. To allow these users to manage AWS Transform MGN resources, you must create an IAM policy that explicitly grants them permissions, and attach the policy to the users or groups that require those permissions. 

When you attach a policy to a user or group of users, it allows or denies the users permission to perform the specified tasks on the specified resources. For more information, see [Policies and Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide* guide. 

## Federated identity
<a name="security_iam_authentication-federated"></a>

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A *federated identity* is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *AWS IAM Identity Center User Guide*.

 

 