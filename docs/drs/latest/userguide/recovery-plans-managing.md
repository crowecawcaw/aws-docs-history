

# Editing and deleting recovery plans
<a name="recovery-plans-managing"></a>

Use `update-recovery-plan` to change a plan's name or description, and the step commands to change its steps. Editing a plan does not affect an execution that is already running, because an execution runs against the copy of the plan that was taken when it started. Your edits apply to the next execution that you start.

Deleting a step or a plan has the following effects:
+ Deleting a step removes its servers from the plan and renumbers the remaining steps so that there are no gaps.
+ Deleting the last server step in a plan leaves the plan with no servers to recover. The plan's status becomes `INVALID` and it cannot be run until you add a server step, which returns it to `ACTIVE`. Adding a wait step does not make a plan valid.
+ Deleting a plan deletes its steps and its server assignments. You cannot delete a plan while it has an execution in progress.

Deleting a plan does not delete any recovery instances that its executions launched, and it does not affect your source servers or their replication.

**Note**  
You cannot delete a source server from AWS Elastic Disaster Recovery while it belongs to a recovery plan. Remove the server from its plans first, then delete it.