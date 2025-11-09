Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'BranchName' and 'CommitId'

variables

The CodeCatalyst source produces
and sets `BranchName` and `CommitId` variables when your workflow
runs. These are known as _predefined variables_. See the following
table for information about these variables.

For information about referencing these variables in a workflow, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

| Key        | Value                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CommitId   | The commit ID representing the state of the repository at the time<br>the workflow run started.<br>Example: `example3819261db00a3ab59468c8b`<br>See also: [Example:<br>Referencing the "CommitId" predefined variable](workflows-predefined-examples.md#workflows-working-with-variables-ex-refer-action "workflows-predefined-examples.md#workflows-working-with-variables-ex-refer-action") |
| BranchName | The name of the branch against which the workflow run<br>started.<br>Examples: `main`, `feature/branch`,<br>`test-LiJuan`<br>See also: [Example: Referencing<br>the "BranchName" predefined variable](workflows-predefined-examples.md#workflows-working-with-variables-ex-branch "workflows-predefined-examples.md#workflows-working-with-variables-ex-branch")                              |
