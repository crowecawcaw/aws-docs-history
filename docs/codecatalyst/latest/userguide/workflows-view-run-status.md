Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Workflow run states

A workflow run can be in one of the following states:

- **Succeeded** – The workflow run was processed
  successfully.
- **Failed** – One or more actions in the workflow run
  failed.
- **In progress** – The workflow run is currently being
  processed.
- **Stopped** – A person stopped the workflow run while
  it was in progress.
- **Stopping** – The workflow run is currently being
  stopped.
- **Cancelled** – The workflow run was canceled by
  CodeCatalyst because the associated workflow was deleted or updated while the run was
  in progress.
- **Superseded** – Only occurs if you have configured
  [superseded run
  mode](workflows-configure-runs.md#workflows-configure-runs-superseded "workflows-configure-runs.md#workflows-configure-runs-superseded"). The workflow run was canceled by CodeCatalyst because a later
  workflow run superseded it.
