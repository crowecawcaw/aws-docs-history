Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating a workflow

A _workflow_ is an automated procedure that describes how to build, test,
and deploy your code as part of a continuous integration and continuous delivery (CI/CD) system.
A workflow defines a series of steps, or _actions_, to take during a workflow
run. A workflow also defines the events, or _triggers_, that cause the
workflow to start. To set up a workflow, you create a _workflow definition
file_ using the CodeCatalyst console's
[visual
or YAML editor](flows.md#workflow.editors "flows.md#workflow.editors").

###### Tip

For a quick look at how you might use workflows in a project, [create a project with a blueprint](projects-create.md#projects-create-console-template "projects-create.md#projects-create-console-template"). Each blueprint deploys a functioning workflow
that you can review, run, and experiment with.

Use the following procedure to create a workflow in CodeCatalyst. The workflow will be stored as
a YAML file in a `~/.codecatalyst/workflows/` folder in the chosen
source repository. Optionally, you can store the workflow in a subfolder of
`~/.codecatalyst/workflows/` by prefacing the workflow file name
with a folder name when you commit it. For more information, see the following
instructions.

For more information about workflows, see [Build, test, and deploy with workflows](workflow.md "workflow.md").

Visual

###### To create a workflow using the visual

editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose **Create workflow**.

The **Create workflow** dialog box appears. 5. In the **Source repository** field, choose a source
repository where the workflow definition file will reside. If no source
repository exists, [create
one](source-repositories-create.md "source-repositories-create.md"). 6. In the **Branch** field, choose a branch where the
workflow definition file will reside. 7. Choose **Create**.

Amazon CodeCatalyst saves the repository and branch information in memory, but
the workflow is not yet committed. 8. Choose **Visual**. 9. Build the workflow:

    1. (Optional) In the workflow diagram, choose the
     **Source** and
     **Triggers** box. A
     **Triggers** pane appears. Choose
     **Add trigger** to add a trigger. For more
     information, see [Adding triggers to workflows](workflows-add-trigger-add.md "workflows-add-trigger-add.md").
    2. Choose **+ Actions** (top-left). The
     **Actions** catalog appears.
    3. Choose the plus sign (**+**) inside an action
     to add it to the workflow. Use the pane on the right to
     configure the action. For more information, see [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md").
    4. (Optional) Choose **Workflow properties**
     (top-right). A **Workflow properties** pane
     appears. Configure the workflow name run mode, and compute. For
     more information, see [Configuring the queuing behavior of runs](workflows-configure-runs.md "workflows-configure-runs.md") and [Configuring compute and runtime images](workflows-working-compute.md "workflows-working-compute.md").

10. (Optional) Choose **Validate** to validate the
    workflow's YAML code before committing.
11. Choose **Commit**, and on the **Commit
    workflow** dialog box, do the following:
    1.  For **Workflow file name**, leave the default
        name or enter your own. The file will be stored in a
        `~/.codecatalyst/workflows/` folder in
        the chosen source repository and branch. You can preface the
        file name with a folder or subfolder. Examples:
        - Specifying `my-workflow` (no
          folder) stores the file as
          `~/.codecatalyst/workflows/my-workflow.yaml`
        - Specifying
          `folder/subfolder/my-workflow`
          stores the file as
          `~/.codecatalyst/workflows/folder/subfolder/my-workflow.yaml`

    2.  For **Commit message**, leave the default
        message or enter your own.
    3.  For **Repository** and
        **Branch**, choose the source repository
        and branch for the workflow definition file. These fields should
        be set to the repository and branch that you specified earlier
        in the **Create workflow** dialog box. You can
        change the repository and branch now, if you'd like.

    ###### Note

    After committing your workflow definition file, it cannot
    be associated with another repository or branch, so make
    sure to choose them carefully. 4. Choose **Commit** to commit the workflow
    definition file.

YAML

###### To create a workflow using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose **Create workflow**.

The **Create workflow** dialog box appears. 5. In the **Source repository** field, choose a source
repository where the workflow definition file will reside. If no source
repository exists, [create
one](source-repositories-create.md "source-repositories-create.md"). 6. In the **Branch** field, choose a branch where the
workflow definition file will reside. 7. Choose **Create**.

Amazon CodeCatalyst saves the repository and branch information in memory, but
the workflow is not yet committed. 8. Choose **YAML**. 9. Build the workflow:

    1. (Optional) Add a trigger to the YAML code. For more
     information, see [Adding triggers to workflows](workflows-add-trigger-add.md "workflows-add-trigger-add.md").
    2. Choose **+ Actions** (top-left). The
     **Actions** catalog appears.
    3. Choose the plus sign (**+**) inside an action
     to add it to the workflow. Use the pane on the right to
     configure the action. For more information, see [Adding an action to a workflow](workflows-add-action.md "workflows-add-action.md").
    4. (Optional) Choose **Workflow properties**
     (top-right). A **Workflow properties** pane
     appears. Configure the workflow name, run mode, and compute. For
     more information, see [Configuring the queuing behavior of runs](workflows-configure-runs.md "workflows-configure-runs.md") and [Configuring compute and runtime images](workflows-working-compute.md "workflows-working-compute.md").

10. (Optional) Choose **Validate** to validate the
    workflow's YAML code before committing.
11. Choose **Commit**, and on the **Commit
    workflow** dialog box, do the following:
    1.  For **Workflow file name**, leave the default
        name or enter your own. The file will be stored in a
        `~/.codecatalyst/workflows/` folder in
        the chosen source repository and branch. You can preface the
        file name with a folder or subfolder. Examples:
        - Specifying `my-workflow` (no
          folder) stores the file as
          `~/.codecatalyst/workflows/my-workflow.yaml`
        - Specifying
          `folder/subfolder/my-workflow`
          stores the file as
          `~/.codecatalyst/workflows/folder/subfolder/my-workflow.yaml`

    2.  For **Commit message**, leave the default
        message or enter your own.
    3.  For **Repository** and
        **Branch**, choose the source repository
        and branch for the workflow definition file. These fields should
        be set to the repository and branch that you specified earlier
        in the **Create workflow** dialog box. You can
        change the repository and branch now, if you'd like.

    ###### Note

    After committing your workflow definition file, it cannot
    be associated with another repository or branch, so make
    sure to choose them carefully. 4. Choose **Commit** to commit the workflow
    definition file.
