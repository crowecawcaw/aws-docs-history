# Start a pipeline in CodePipeline

Each pipeline execution can be started based on a different trigger. Each pipeline
execution can have a different type of trigger, depending on how the pipeline is started.
The trigger type for each execution is shown in the execution history for a pipeline.
Trigger types can depend on the source action provider as follows:

###### Note

You cannot specify more than one trigger per source action.

- **Pipeline creation**: When a pipeline is created, a
  pipeline execution starts automatically. This is the `CreatePipeline`
  trigger type in the **Execution history**.
- **Changes on revised objects**: This category
  represents the `PutActionRevision` trigger type in the
  **Execution history**.
- **Change detection on branch and commit for a code
  push**: This category represents the `CloudWatchEvent`
  trigger type in the **Execution history**. When a change is
  detected to a source commit and branch in the source repository, your pipeline
  starts. This trigger type uses automated change detection. The source action
  providers that use this trigger type are S3 and CodeCommit. This type is also used
  for a schedule that starts your pipeline. See [Start a pipeline on a
  schedule](pipelines-trigger-source-schedule.md "pipelines-trigger-source-schedule.md").
- **Polling for source changes**: This category
  represents the `PollForSourceChanges` trigger type in the
  **Execution history**. When a change is detected to a source
  commit and branch in the source repository through polling, your pipeline starts.
  This trigger type is not recommended and should be migrated to use automated change
  detection. The source action providers that use this trigger type are S3 and
  CodeCommit.
- **Webhook events for third-party sources**: This
  category represents the `Webhook` trigger type in the **Execution
  history**. When a change is detected by a webhook event, your pipeline
  starts. This trigger type uses automated change detection. The source action
  providers that use this trigger type are connections configured for code push
  (Bitbucket Cloud, GitHub, GitHub Enterprise Server, GitLab.com, and GitLab
  self-managed).
- **WebhookV2 events for third-party sources**: This
  category represents the `WebhookV2` trigger type in the
  **Execution history**. This type is for executions that are
  triggered based on triggers defined in the pipeline definition. When a release with
  a specified Git tag is detected, your pipeline starts. You can use Git tags to mark
  a commit with a name or other identifier that helps other repository users
  understand its importance. You can also use Git tags to identify a particular commit
  in the history of a repository. This trigger type disables automated change
  detection. The source action providers that use this trigger type are connections
  configured for Git tags (Bitbucket Cloud, GitHub, GitHub Enterprise Server, and
  GitLab.com).
- **Manually starting a pipeline**: This category
  represents the `StartPipelineExecution` trigger type in the
  **Execution history**. You can use the console or the AWS CLI to
  start a pipeline manually. For information, see [Start a pipeline manually](pipelines-rerun-manually.md "pipelines-rerun-manually.md").
- **RollbackStage**: This category represents the
  `RollbackStage` trigger type in the **Execution
  history**. You can use the console or the AWS CLI to roll back a stage
  manually or automatically. For information, see [Configuring stage rollback](stage-rollback.md "stage-rollback.md").
  When you add a source action to your pipeline that uses automated change detection trigger
  types, the actions work with additional resources. Creating each source action is detailed
  in separate sections due to these additional resources for change detection. For details
  about each source provider and the change detection methods required for automated change
  detection, see [Source actions and change detection
  methods](change-detection-methods.md "change-detection-methods.md").

###### Topics

- [Start a pipeline manually](pipelines-rerun-manually.md "pipelines-rerun-manually.md")
- [Start a pipeline on a
  schedule](pipelines-trigger-source-schedule.md "pipelines-trigger-source-schedule.md")
- [Start a pipeline with a source
  revision override](pipelines-trigger-source-overrides.md "pipelines-trigger-source-overrides.md")
