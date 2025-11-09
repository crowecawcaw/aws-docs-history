Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Viewing the deployment logs

You can view logs related to specific deploy actions to troubleshoot problems in
Amazon CodeCatalyst.

You can view logs starting from a [workflow](workflow.md "workflow.md"), or an [environment](deploy-environments.md "deploy-environments.md").

###### To view the logs of a deploy action starting from a workflow

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Runs**.
6. Choose the workflow run that deployed your application.
7. In the workflow diagram, choose the action whose logs you want to view.
8. Choose the **Logs** tab and expand the sections to reveal the log
   messages.
9. To view more logs, choose the **Summary** tab, and then choose
   **View in CloudFormation** (if it's available) to view more logs there. You
   may need to sign in to AWS.

###### To view the logs of a deploy action starting from an environment

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Environments**.
4. Choose the environment into which your application was deployed.
5. In **Deployment activity**, find the **Workflow Run
   ID** column, and choose the workflow run that deployed your stack.
6. In the workflow diagram, choose the action whose logs you want to view.
7. Choose the **Logs** tab and expand the sections to reveal the log
   messages.
8. To view more logs, choose the **Summary** tab, and then choose
   **View in CloudFormation** (if it's available) to view more logs there. You
   may need to sign in to AWS.
