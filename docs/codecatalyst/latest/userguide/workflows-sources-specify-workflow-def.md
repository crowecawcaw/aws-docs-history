Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Specifying a workflow file's

source repository

Use the following instructions to specify the CodeCatalyst source repository where you want
to store your workflow definition file. If you'd rather specify a GitHub repository,
Bitbucket repository, or GitLab project repository, see instead [Add functionality to projects with extensions in CodeCatalyst](extensions.md "extensions.md").

The source repository where your workflow definition file resides is identified by the
label, `WorkflowSource`.

###### Note

You specify the source repository where your workflow definition file resides when
you first commit your workflow definition file. After this commit, the repository
and workflow definition file are linked together permanently. The only way to change
the repository after the initial commit is to re-create the workflow in a different
repository.

###### To specify the source repository that will store the workflow definition

file

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose **Create workflow** and create the workflow. For more
   information, see [Creating a workflow](workflows-create-workflow.md "workflows-create-workflow.md").

During the workflow creation process, you can specify the CodeCatalyst
repository, branch, and folder where you want to store your workflow definition file.
