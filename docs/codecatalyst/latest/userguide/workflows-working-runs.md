Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Running a workflow

A _run_ is a single iteration of a workflow. During a run, CodeCatalyst
performs the actions defined in the workflow configuration file and outputs the associated
logs, artifacts, and variables.

You can start a run manually, or you can start one automatically, through a
_workflow trigger_. An example of a workflow trigger might be a
software developer pushing a commit to your main branch.

You can also manually stop a workflow run midway through its processing if you started it
by mistake.

If multiple workflow runs are started at around the same time, you can configure how you
want these runs to be queued. You can use the default queuing behavior, where runs are
queued one after the other in the order in which they were started, or you can have a later
run supersede (or 'take over') from an earlier one to speed up your run throughout. Setting
up your workflow runs to occur in parallel, so that no run waits for any other, is also
possible.

After you've started a workflow run, either manually or automatically, you can view the
status of the run and other details. For example, you can see when it was started, who it
was started by, and whether it's still running.

###### Topics

- [Starting a workflow run manually](workflows-manually-start.md "workflows-manually-start.md")
- [Starting a workflow run automatically using
  triggers](workflows-add-trigger.md "workflows-add-trigger.md")
- [Configuring manual-only triggers](workflows-manual-only.md "workflows-manual-only.md")
- [Stopping a workflow run](workflows-stop.md "workflows-stop.md")
- [Gating a workflow run](workflows-gates.md "workflows-gates.md")
- [Requiring approvals on workflow runs](workflows-approval.md "workflows-approval.md")
- [Configuring the queuing behavior of runs](workflows-configure-runs.md "workflows-configure-runs.md")
- [Caching files between workflow runs](workflows-caching.md "workflows-caching.md")
- [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md")
