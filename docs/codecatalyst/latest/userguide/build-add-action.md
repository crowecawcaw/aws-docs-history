Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding the build action

Use the following procedure to add a build action to your CodeCatalyst workflow.

Visual

###### To add a build action using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
3. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
4. Choose **Edit**.
5. Choose **Visual**.
6. Choose **Actions**.
7. In **Actions**, choose **Build**.
8. In the **Inputs** and **Configuration** tabs,
   complete the fields according to your needs. For a description of each field, see the
   [Build and test actions YAML](build-action-ref.md "build-action-ref.md"). This reference
   provides detailed information on each field (and corresponding YAML property value) as
   it appears in both the YAML and visual editors.
9. (Optional) Choose **Validate** to validate the workflow's YAML
   code before committing.
10. Choose **Commit**, enter a commit message, and choose
    **Commit** again.

YAML

###### To add a build action using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
3. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
4. Choose **Edit**.
5. Choose **YAML**.
6. Choose **Actions**.
7. In **Actions**, choose **Build**.
8. Modify the properties in the YAML code according to your needs. An explanation of
   each available property is provided in the [Build and test actions YAML](build-action-ref.md "build-action-ref.md").
9. (Optional) Choose **Validate** to validate the workflow's YAML
   code before committing.
10. Choose **Commit**, enter a commit message, and choose
    **Commit** again.

## Build action definition

The build action is defined as a set of YAML properties inside your workflow definition
file. For information on these properties, see [Build and test actions YAML](build-action-ref.md "build-action-ref.md") in the [Workflow YAML definition](workflow-reference.md "workflow-reference.md").
