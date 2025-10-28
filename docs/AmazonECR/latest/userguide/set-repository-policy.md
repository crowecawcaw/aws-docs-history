# Setting a private repository policy

statement in Amazon ECR

You can add an access policy statement to a repository in the AWS Management Console by following
the steps below. You can add multiple policy statements per repository. For example
policies, see [Private repository policy examples in Amazon ECR](repository-policy-examples.md "repository-policy-examples.md").

###### Important

Amazon ECR requires that users have permission to make calls to the
`ecr:GetAuthorizationToken` API through an IAM policy before they
can authenticate to a registry and push or pull any images from any Amazon ECR
repository. Amazon ECR provides several managed IAM policies to control user access at
varying levels. For more information, see [Amazon Elastic Container Registry Identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

###### To set a repository policy statement

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the Region that contains the repository to set
   a policy statement on.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, choose the repository to set a
   policy statement on to view the contents of the repository.
5. From the repository image list view, in the navigation pane, choose
   **Permissions**, **Edit**.

###### Note

If you don't see the **Permissions** option in the
navigation pane, ensure that you are in the repository image list
view. 6. On the **Edit permissions** page, choose **Add
statement**. 7. For **Statement name**, enter a name for the
statement. 8. For **Effect**, choose whether the policy statement will
result in an allow or an explicit deny. 9. For **Principal**, choose the scope to apply the policy
statement to. For more information, see [AWS JSON
Policy Elements: Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in the
_IAM User Guide_.

    * You can apply the statement to all authenticated AWS users by
     selecting the **Everyone (\*)** check box.
    * For **Service principal**, specify the service
     principal name (for example, `ecs.amazonaws.com`) to apply
     the statement to a specific service.
    * For **AWS Account IDs**, specify an AWS account
     number (for example, `111122223333`) to apply the
     statement to all users under a specific AWS account. Multiple accounts
     can be specified by using a comma delimited list.


    ###### Important

    The account you are granting permissions to must have the Region
     you are creating the repository policy in enabled, otherwise an
     error will occur.
    * For **IAM Entities**, select the roles or users
     under your AWS account to apply the statement to.


    ###### Note

    For more complicated repository policies that are not
     currently supported in the AWS Management Console, you can apply the policy with the [**set-repository-policy**](../../../cli/latest/reference/ecr/set-repository-policy.md "../../../cli/latest/reference/ecr/set-repository-policy.md") AWS CLI command.

10. For **Actions**, choose the scope of the Amazon ECR API operations
    that the policy statement should apply to from the list of individual API
    operations.
11. When you are finished, choose **Save** to set the
    policy.
12. Repeat the previous step for each repository policy to add.
