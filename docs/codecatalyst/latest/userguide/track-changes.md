Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Tracking deployment status by commit

At any time in the development lifecycle, it's important to know the deployment status of
specific commits, such as bug fixes, new features, or other impactful changes. Consider the
following scenarios in which deployment status tracking capability is helpful to development
teams:

- As a developer, you've made a fix to address a bug and you want to report the
  status of its deployment across your team's deployment environments.
- As a release manager, you want to view a list of deployed commits to track and
  report their deployment status.
  CodeCatalyst provides a view you can use to determine at a glance where individual commits or
  changes have been deployed, and to which environment. This view includes:

- A list of commits.
- The status of deployments that include the commits.
- The environments in which the commits are successfully deployed.
- The status of any tests run against the commits in your CI/CD workflow.
  The following procedure details how to navigate to and use this view to track changes in
  your project.

###### Note

Tracking deployment status by commit is only supported with [CodeCatalyst repositories](source.md "source.md"). You cannot use this feature with a [GitHub repository, Bitbucket repository, or GitLab project
repository](extensions.md "extensions.md").

###### To track deployment status by commit

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose
   **Change tracking**.
4. In the two dropdown lists at the top of the main pane, choose the source
   repository and branch that contain the commits whose release status you want to
   view.
5. Choose **View changes**.

A list of commits appears.

For each commit, you can view the following:

    * Commit information such as ID, author, message, and when it was committed.
     For more information, see [Store and collaborate on code with source repositories in CodeCatalyst](source.md "source.md").
    * The status of deployments to each environment. For more information, see
     [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md").
    * Test and code coverage results. For more information, see [Testing with workflows](test-workflow-actions.md "test-workflow-actions.md").


    ###### Note

    Software Composition Analysis (SCA) results are not displayed.

6. (Optional) To view more information about the changes related to a specific
   commit, including the latest deployment and detailed code coverage and unit test
   information, choose **View details** for that commit.
