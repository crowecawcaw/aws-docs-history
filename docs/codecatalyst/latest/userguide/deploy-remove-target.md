Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Removing a deployment target

You can remove a deployment target such as an Amazon ECS cluster or AWS CloudFormation stack from the
**Deployment targets** page in the CodeCatalyst console.

###### Important

When you remove a deployment target, it is removed from the CodeCatalyst console, but remains
available in the AWS service that hosts it (if it still exists).

Consider removing a deployment target if the target has become stale in CodeCatalyst. Targets
might become stale if:

- You deleted the workflow that deployed to the target.
- You changed the stack or cluster that you're deploying to.
- You deleted the stack or cluster from the CloudFormation or Amazon ECS service in the AWS
  console.

###### To remove a deployment target

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Environments**.
4. Choose the name of the environment that contains the deployment target you want to
   remove. For information about environments, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md").
5. Choose the **Deployment targets** tab.
6. Choose the radio button next to the deployment target you want to remove.
7. Choose **Remove**.

The target is removed from the page.
