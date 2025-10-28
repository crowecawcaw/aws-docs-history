# Using the AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

To avoid using the root user for everyday tasks, learn how to [set up an
administrative user in AWS IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md"). For additional root user security
recommendations, see [Root user best practices for
your AWS account](../../../IAM/latest/UserGuide/root-user-best-practices.md "../../../IAM/latest/UserGuide/root-user-best-practices.md").

###### Important

Anyone who has root user credentials for your AWS account has unrestricted access to
all the resources in your account, including billing information.

You can [change](../../../IAM/latest/UserGuide/root-user-password.md "../../../IAM/latest/UserGuide/root-user-password.md"), or [reset the root user password](../../../IAM/latest/UserGuide/reset-root-password.md "../../../IAM/latest/UserGuide/reset-root-password.md"),
and [create](../../../IAM/latest/UserGuide/id_root-user_manage_add-key.md "../../../IAM/latest/UserGuide/id_root-user_manage_add-key.md"), or [delete access
keys](../../../IAM/latest/UserGuide/id_root-user_manage_delete-key.md "../../../IAM/latest/UserGuide/id_root-user_manage_delete-key.md") (access key IDs and secret access keys) for your root user. For help signing
in using your root user, see [Sign in to
the AWS Management Console as the root user](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md") in the _AWS Sign-In User
Guide_.
