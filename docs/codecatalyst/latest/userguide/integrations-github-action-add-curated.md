Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Adding a curated GitHub Action

A _curated GitHub Action_ is a GitHub Action that is made available in
the CodeCatalyst console, and serves as an example of how to use a GitHub Action inside a CodeCatalyst
workflow.

Curated GitHub Actions are wrapped in the CodeCatalyst-authored [GitHub Actions action](integrations-github-action-add.md "integrations-github-action-add.md"),
identified by the `aws/github-actions-runner@v1` identifier. For example, here's
what the curated GitHub Action, [TruffleHog OSS](https://github.com/marketplace/actions/trufflehog-oss "https://github.com/marketplace/actions/trufflehog-oss"), looks
like:

```
Actions:
  TruffleHogOSS_e8:
    Identifier: aws/github-actions-runner@v1
    Inputs:
      Sources:
        - WorkflowSource # This specifies that the action requires this Workflow as a source
    Configuration:
      Steps:
        - uses: trufflesecurity/trufflehog@v3.16.0
          with:
            path: ' ' # Required; description: Repository path
            base: ' ' # Required; description: Start scanning from here (usually main branch).
            head: ' ' # Optional; description: Scan commits until here (usually dev branch).
            extra_args: ' ' # Optional; description: Extra args to be passed to the trufflehog cli.
```

In the previous code, the CodeCatalyst **GitHub Actions** action (identified by
`aws/github-actions-runner@v1`) wraps the TruffleHog OSS action (identified by
`trufflesecurity/trufflehog@v3.16.0`), making it work in a CodeCatalyst workflow.

To configure this action, you would replace the empty strings under `with:` with
your own values. For example:

```
Actions:
  TruffleHogOSS_e8:
    Identifier: aws/github-actions-runner@v1
    Inputs:
      Sources:
        - WorkflowSource # This specifies that the action requires this Workflow as a source
    Configuration:
      Steps:
        - uses: trufflesecurity/trufflehog@v3.16.0
          with:
            path: ./
            base: main # Required; description: Start scanning from here (usually main branch).
            head: HEAD # Optional; description: Scan commits until here (usually dev branch).
            extra_args: '‐‐debug ‐‐only-verified' # Optional; description: Extra args to be passed to the trufflehog cli.
```

To add a curated GitHub Action to a workflow, use the following procedure. For general
information about using GitHub Actions in a CodeCatalyst workflow, see [Integrating with GitHub Actions](integrations-github-actions.md "integrations-github-actions.md").

###### Note

If you don't see your GitHub Action among the list of curated actions, you can still add
it to your workflow using the **GitHub Actions** action. For more
information, see [Adding the 'GitHub Actions' action](integrations-github-action-add.md "integrations-github-action-add.md").

Visual

###### To add a curated GitHub action using the visual editor

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
9. Browse or search for a GitHub Action, and do one of the
   following:
   - Choose the plus sign (**+**) to add the action to the
     workflow diagram and open its configuration pane.

   Or
   - Choose the name of the GitHub Action. The action details dialog box
     appears. On this dialog box:
     - (Optional) Choose **View source** to [view the action's source
       code](workflows-view-source.md#workflows-view-source.title "workflows-view-source.md#workflows-view-source.title").
     - Choose **Add to workflow** to add the action to the
       workflow diagram and open its configuration pane.

10. In the **Inputs**, **Configuration**, and
    **Outputs** tabs, complete the fields according to your needs. For
    a description of each field, see the ['GitHub Actions' action YAML](github-action-ref.md "github-action-ref.md"). This reference provides detailed information about
    each field (and corresponding YAML property value) available to the **GitHub
    Actions** action, as it appears in both the YAML and visual editors.

For information about the configuration options available to the curated GitHub
Action, see its documentation. 11. (Optional) Choose **Validate** to validate the workflow's YAML
code before committing. 12. Choose **Commit**, enter a commit message, and choose
**Commit** again.

YAML

###### To add a curated GitHub action using the YAML editor

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
9. Browse or search for a GitHub Action, and do one of the
   following:
   - Choose the plus sign (**+**) to add the action to the
     workflow diagram and open its configuration pane.

   Or
   - Choose the name of the GitHub Action. The action details dialog box
     appears. On this dialog box:
     - (Optional) Choose **View source** to [view the action's source
       code](workflows-view-source.md#workflows-view-source.title "workflows-view-source.md#workflows-view-source.title").
     - Choose **Add to workflow** to add the action to the
       workflow diagram and open its configuration pane.

10. Modify the properties in the YAML code according to your needs. An explanation of
    each property available to the **GitHub Actions** action is provided
    in the ['GitHub Actions' action YAML](github-action-ref.md "github-action-ref.md").

For information about the configuration options available to the curated GitHub
Action, see its documentation. 11. (Optional) Choose **Validate** to validate the workflow's YAML
code before committing. 12. Choose **Commit**, enter a commit message, and choose
**Commit** again.
