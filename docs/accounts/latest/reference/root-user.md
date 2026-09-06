

# Using the AWS account root user
<a name="root-user"></a>

Depending on how you sign up for AWS, you either have access to AWS accounts or projects. Projects contain AWS accounts and the settings for sharing with other collaborators. For more information, see [Compare sign-up options](sign-up-for-aws.md). In this section, we explain how to use the root user in an AWS account that you create using Sign up for AWS (advanced).

 When you create an AWS account, you begin with one sign-in identity called the AWS account *root user* that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*. 

To avoid using the root user for everyday tasks, learn how to [set up an administrative user in AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html). For additional root user security recommendations, see [Root user best practices for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html).

**Important**  
Anyone who has root user credentials for your AWS account has unrestricted access to all the resources in your account, including billing information.

You can [change](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-password.html), or [reset the root user password](https://docs.aws.amazon.com/IAM/latest/UserGuide/reset-root-password.html), and [create](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user_manage_add-key.html), or [delete access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user_manage_delete-key.html) (access key IDs and secret access keys) for your root user. For help signing in using your root user, see [Sign in to the AWS Management Console as the root user](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.html) in the *AWS Sign-In User Guide*.