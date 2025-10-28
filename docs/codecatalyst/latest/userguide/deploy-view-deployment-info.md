Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Viewing deployment information

You can view the following information about a deployment in Amazon CodeCatalyst:

- Deployment activity, including the deployment status, start time, end time, history, and
  duration of events.
- Stack name, AWS Region, last update time, and associated workflows.
- Commits and pull requests.
- Action-specific information, for example, CloudFormation events and outputs.
  You can view deployment information starting from a [workflow](workflow.md "workflow.md"), an [environment](deploy-environments.md "deploy-environments.md"), or a workflow [action](workflows-concepts.md#workflows-concepts-actions "workflows-concepts.md#workflows-concepts-actions").

###### To view deployment information starting from a workflow

- Go to the workflow run that deployed your application. For instructions, see [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md").

###### To view deployment

information starting from an environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Environments**.
4. Choose the environment where your stack was deployed, for example,
   `Production`.
5. Choose **Deployment activity** to view the deployment history of your
   stacks, the status of the deployments (for example, **SUCCEEDED** or
   **FAILED**), and other deployment-related information.
6. Choose **Deployment target** to view information about the stacks,
   clusters, or other targets deployed into the environment. You can view information such as
   the stack name, Region, provider, and identifier.

###### To view deployment information starting from an action

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. In the workflow diagram, choose the workflow action that deployed your application. For
   example, you might choose **DeployCloudFormationStack**.
6. Review the contents in the right pane for action-specific deployment information.
