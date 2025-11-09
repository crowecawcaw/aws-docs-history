Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Exporting GitHub output parameters

You can use [GitHub output parameters](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter "https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter") in your CodeCatalyst workflows.

###### Note

Another word for _output parameter_ is _variable_.
Because GitHub uses the term _output parameter_ in its documentation,
we'll use this term too.

Use the following instructions to export a GitHub output parameter from a GitHub Action so
that it is available for use by other CodeCatalyst workflow actions.

###### To export a GitHub output parameter

1. Open a workflow and choose **Edit**. For more information, see [Creating a workflow](workflows-create-workflow.md "workflows-create-workflow.md").
2. In the **GitHub Actions** action that generates the output parameter
   that you want to export, add an `Outputs` section with an underlying
   `Variables` property that looks like this:

```
Actions:
  MyGitHubAction:
    Identifier: aws/github-actions-runner@v1
    **Outputs:
 Variables:
 - '`step-id`\_`output-name`'**

```

Replace:

    * `step-id` with value of the `id:` property in
     the GitHub action's `steps` section.
    * `output-name` with the name of the GitHub output
     parameter.

###### Example

The following example shows you how to export a GitHub output parameter called
`SELECTEDCOLOR`.

```
Actions:
  MyGitHubAction:
    Identifier: aws/github-actions-runner@v1
    **Outputs:
 Variables:
 - 'random-color-generator\_SELECTEDCOLOR'**
    Configuration:
      Steps:
        - name: Set selected color
          run: echo "SELECTEDCOLOR=green" >> $GITHUB_OUTPUT
          id: random-color-generator

```
