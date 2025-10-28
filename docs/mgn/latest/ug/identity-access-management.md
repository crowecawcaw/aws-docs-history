NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Identity and access management for AWS Application Migration Service

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be authenticated (signed in) and
authorized (have permissions) to use AWS resources. IAM enables you to create users and
groups under your AWS account. You control the permissions that users have to perform tasks
using AWS resources. You can use IAM for no additional charge.

By default, users created via the IAM service don't have permissions for AWS Application Migration Service (AWS MGN) resources and
operations.
To allow these users to manage AWS Application Migration Service resources, you must create an IAM policy that
explicitly grants them permissions, and attach the policy to the users or groups that
require those permissions.

When you attach a policy to a user or group of users, it allows or denies the users
permission to perform the specified tasks on the specified resources. For more information,
see [Policies and Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the
_IAM User Guide_
guide.

## Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or AWS Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity Center User Guide_.
