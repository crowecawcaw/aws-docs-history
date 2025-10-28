Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Specifying a workflow action's source

repository

Use the following instructions to specify a source repository to use with a workflow
action. On startup, the action bundles the files at the configured source repository
into an artifact, downloads the artifact to the [runtime
environment Docker image](build-images.md "build-images.md") where the action is running, and then completes its
processing using the downloaded files.

###### Note

Currently, within a workflow action, you can only specify one source repository,
which is the source repository where the workflow definition file resides (in the
`.codecatalyst/workflows/` directory or one of its
subdirectories). This source repository is represented by the label
`WorkflowSource`.

Visual

###### To specify the source repository that an action will use (visual

editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. In the workflow diagram, choose the action where you want to
   specify the source.
8. Choose **Inputs**.
9. In **Sources - optional** do the
   following:

Specify the labels that represent the source repositories that will be needed by the action.
Currently, the only supported label is `WorkflowSource`, which represents the source
repository where your workflow definition file is stored.

If you omit a source, then you must specify at least one input artifact under
``action-name`/Inputs/Artifacts`.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md "workflows-sources.md"). 10. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 11. Choose **Commit**, enter a commit message, and
choose **Commit** again.

YAML

###### To specify the source repository that an action will use (YAML

editor)

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. In an action, add code similar to the following:

```
`action-name`:
 Inputs:
   Sources:
     - WorkflowSource
```

For more information, see the description of the
`Sources` property in [Workflow YAML definition](workflow-reference.md "workflow-reference.md") for your action. 8. (Optional) Choose **Validate** to validate the
workflow's YAML code before committing. 9. Choose **Commit**, enter a commit message, and
choose **Commit** again.
