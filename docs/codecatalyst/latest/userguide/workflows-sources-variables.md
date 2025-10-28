Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'BranchName' and 'CommitId'

variables

The CodeCatalyst source produces
and sets `BranchName` and `CommitId` variables when your workflow
runs. These are known as _predefined variables_. See the following
table for information about these variables.

For information about referencing these variables in a workflow, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

| Key        | Value                                                                                                                                                                                                                                                                                                                                                                             |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CommitId   | The commit ID representing the state of the repository at the time the workflow run started. Example: `example3819261db00a3ab59468c8b` See also: [Example: Referencing the "CommitId" predefined variable](workflows-predefined-examples.md#workflows-working-with-variables-ex-refer-action "workflows-predefined-examples.md#workflows-working-with-variables-ex-refer-action") |
| BranchName | The name of the branch against which the workflow run started. Examples: `main`, `feature/branch`, `test-LiJuan` See also: [Example: Referencing the "BranchName" predefined variable](workflows-predefined-examples.md#workflows-working-with-variables-ex-branch "workflows-predefined-examples.md#workflows-working-with-variables-ex-branch")                                 |
