# Setting a repository policy statement in Amazon ECR Public

You can add an access policy statement to a public repository in the AWS Management Console by
following these steps. You can add multiple policy statements per public repository. For
example policies, see [Public repository policy examples in Amazon ECR Public](public-repository-policy-examples.md "public-repository-policy-examples.md").

###### Important

Amazon ECR requires that users have permission to make calls to the
`ecr-public:GetAuthorizationToken` and `sts:GetServiceBearerToken` API through an IAM policy before they
can authenticate to a registry and push any images to an Amazon ECR
repository.

###### To set a repository policy statement

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories "https://console.aws.amazon.com/ecr/repositories").
2. From the navigation bar, choose the AWS Region that contains the repository
   to set a policy statement on.
3. In the navigation pane, choose **Repositories**.
4. On the **Repositories** page, select the
   **Public** tab, and then choose the repository to set a
   policy statement on.
5. In the navigation pane, choose **Permissions**,
   **Edit**.
6. On the **Edit permissions** page, choose **Add
   statement**.
7. For **Statement name**, enter a name for the
   statement.
8. For **Effect**, choose whether the policy statement results
   in an allow or an explicit deny.

###### Note

All public repositories are visible on the Amazon ECR Public Gallery. Using a repository
policy to deny access to view or pull from a public repository is not supported. 9. For **Principal**, choose the scope to apply the policy
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
     can be specified by using a comma-separated list.
    * For **IAM Entities**, select the roles or users
     under your AWS account to apply the statement to.


    ###### Note

    For more complicated repository policies that are not
     currently supported in the AWS Management Console, you can apply the policy with the [**set-repository-policy**](../../../cli/latest/reference/ecr/set-repository-policy.md "../../../cli/latest/reference/ecr/set-repository-policy.md") AWS CLI command.

10. For **Actions**, choose the scope of the Amazon ECR API operations
    that the policy statement applies to from the list of individual API
    operations.
11. When you're finished, choose **Save** to set the
    policy.
12. Repeat the previous step for each repository policy to add.
