# Configuring stage rollback

You can roll back a stage to an execution that was successful in that stage. You can
preconfigure a stage for rollback on failure, or you can manually roll back a stage. The
rolled back operation will result in a new execution. The target pipeline execution chosen
for rollback is used to retrieve source revisions and variables.

The type of execution, either standard or rollback, displays in the pipeline history,
pipeline state, and pipeline execution details.

###### Topics

- [Considerations for rollbacks](#stage-rollback-considerations "#stage-rollback-considerations")
- [Roll back a stage manually](stage-rollback-manual.md "stage-rollback-manual.md")
- [Configure a stage for automatic rollback](stage-rollback-auto.md "stage-rollback-auto.md")
- [View rollback status in execution listing](stage-rollback-view-listing.md "stage-rollback-view-listing.md")
- [View rollback status details](stage-rollback-view-details.md "stage-rollback-view-details.md")

## Considerations for rollbacks

Considerations for stage rollback are as follows:

- You cannot roll back a source stage.
- The pipeline can only roll back to a previous execution if the previous
  execution was started in the current pipeline structure version.
- You cannot roll back to a target execution ID that is a rollback execution
  type.
- CodePipeline will use the variables and artifacts from the execution to which it is
  rolling back.
