Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Stopping a workflow run

Use the following procedure to stop a workflow run that's in progress. You might want
to stop a run if it was started by accident.

When you stop a workflow run, CodeCatalyst waits for in-progress actions to complete before
it marks the run as **Stopped** in the CodeCatalyst console. Any actions that
didn't have a chance to start will not be started, and will be marked as
**Abandoned**.

###### Note

If a run is queued (that is, it has no in-progress actions), then the run is
stopped immediately.

For more information about workflow runs, see [Running a workflow](workflows-working-runs.md "workflows-working-runs.md").

###### To stop a workflow run

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Under **Workflows**, choose **Runs** and
   choose the in-progress run from the list.
5. Choose **Stop**.
