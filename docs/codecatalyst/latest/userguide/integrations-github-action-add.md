Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding the 'GitHub Actions' action

A **_GitHub Actions_** action is a _CodeCatalyst action_ that
wraps a GitHub Action and makes it compatible with CodeCatalyst workflows.

For more information, see [Integrating with GitHub Actions](integrations-github-actions.md "integrations-github-actions.md").

To add the **GitHub Actions** action to a workflow, follow these
steps.

###### Tip

For a tutorial that shows you how to use the **GitHub Actions** action,
see [Tutorial: Lint code using a GitHub
Action](integrations-github-action-tutorial.md "integrations-github-action-tutorial.md").

Visual

###### To add the 'GitHub Actions' action using the visual editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **Visual**.
7. At the top-left, choose **+ Actions** to open the action
   catalog.
8. From the drop-down list, choose **GitHub**.
9. Search for the **GitHub Actions** action, and do one of the
   following:
   - Choose the plus sign (**+**) to add the action to the
     workflow diagram and open its configuration pane.

   Or
   - Choose **GitHub Actions**. The action details dialog box
     appears. On this dialog box:
     - (Optional) Choose **View source** to [view the action's source
       code](workflows-view-source.md#workflows-view-source.title "workflows-view-source.md#workflows-view-source.title").
     - Choose **Add to workflow** to add the action to the
       workflow diagram and open its configuration pane.

10. In the **Inputs** and **Configuration** tabs,
    complete the fields according to your needs. For a description of each field, see the
    ['GitHub Actions' action YAML](github-action-ref.md "github-action-ref.md"). This reference
    provides detailed information about each field (and corresponding YAML property value) as
    it appears in both the YAML and visual editors.
11. (Optional) Choose **Validate** to validate the workflow's YAML
    code before committing.
12. Choose **Commit**, enter a commit message, and choose
    **Commit** again.

YAML

###### To add the 'GitHub Actions' action using the YAML editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
5. Choose **Edit**.
6. Choose **YAML**.
7. At the top-left, choose **+ Actions** to open the action
   catalog.
8. From the drop-down list, choose **GitHub**.
9. Search for the **GitHub Actions** action, and do one of the
   following:
   - Choose the plus sign (**+**) to add the action to the
     workflow diagram and open its configuration pane.

   Or
   - Choose **GitHub Actions**. The action details dialog box
     appears. On this dialog box:
     - (Optional) Choose **View source** to [view the action's source
       code](workflows-view-source.md#workflows-view-source.title "workflows-view-source.md#workflows-view-source.title").
     - Choose **Add to workflow** to add the action to the
       workflow diagram and open its configuration pane.

10. Modify the properties in the YAML code according to your needs. An explanation of
    each available property is provided in the ['GitHub Actions' action YAML](github-action-ref.md "github-action-ref.md").
11. (Optional) Choose **Validate** to validate the workflow's YAML
    code before committing.
12. Choose **Commit**, enter a commit message, and choose
    **Commit** again.

## 'GitHub Actions' action definition

The **GitHub Actions** action is defined as a set of YAML properties inside your workflow definition file.
For information about these properties, see ['GitHub Actions' action YAML](github-action-ref.md "github-action-ref.md") in the [Workflow YAML definition](workflow-reference.md "workflow-reference.md").
