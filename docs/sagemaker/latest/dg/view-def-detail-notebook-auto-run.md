# View notebook job definitions

###### Note

If you scheduled your notebook job with the SageMaker Python SDK, skip this section. Only
notebook jobs created in Studio or local JupyterLab environments create job
definitions. Therefore, if you created your notebook job with the SageMaker Python SDK, you
won’t see job definitions in the Notebook Jobs dashboard. You can, however, view your
notebook jobs as described in [View notebook jobs](view-notebook-jobs.md "view-notebook-jobs.md").

When you create a job definition, you create a schedule for a job. The
**Notebook Job Definitions** tab lists these schedules, as well as
information about specific notebook job definitions. For example, you might create a job
definition that runs a specific notebook every minute. Once this job definition is active,
you see a new job every minute in the **Notebook Jobs** tab. The following
page gives information about the **Notebook Job Definitions** tab, as well
as how to view a notebook job definition.

The **Notebook Job Definitions** tab displays a dashboard with all your
job definitions and includes the input notebook, the creation time, the schedule, and the
status for each job definition. The value in the **Status** column is one
of the following values:

- **Paused**: You paused the job definition. Studio does not
  initiate any jobs until you resume the definition.
- **Active**: The schedule is on and Studio can run the notebook
  according to the schedule you specified.
  In addition, the **Actions** column provides shortcuts to help you
  perform the following tasks directly in the interface:

- Pause: Pauses the job definition. Studio won’t create any jobs until you resume
  the definition.
- Delete: Removes the job definition from the **Notebook Job
  Definitions** tab.
- Resume: Continues a paused job definition so that it can start jobs.
  If you created a job definition but it doesn’t initiate jobs, see [Job definition doesn’t create
  jobs](notebook-auto-run-troubleshoot.md#notebook-auto-run-troubleshoot-no-jobs "notebook-auto-run-troubleshoot.md#notebook-auto-run-troubleshoot-no-jobs") in the [Troubleshooting guide](notebook-auto-run-troubleshoot.md "notebook-auto-run-troubleshoot.md").

## View a single job definition

If you select a job definition name in the **Notebook Job
Definitions** tab, you see the **Job Definition** page where
you can view specific details for a job definition. Use this page to confirm the settings
you specified when you created the job definition. If you don’t see any jobs created from
your job definition, see [Job definition doesn’t create
jobs](notebook-auto-run-troubleshoot.md#notebook-auto-run-troubleshoot-no-jobs "notebook-auto-run-troubleshoot.md#notebook-auto-run-troubleshoot-no-jobs") in the [Troubleshooting guide](notebook-auto-run-troubleshoot.md "notebook-auto-run-troubleshoot.md").

This page also contains a section listing the jobs that run from this job definition.
Viewing your jobs in the **Job Definition** page may be a more productive
way to help you organize your jobs instead of viewing jobs in the **Notebook
Jobs** tab, which combines all jobs from all your job definitions.

In addition, this page provides shortcuts for the following actions:

- **Pause/Resume**: Pause your job definition, or resume a paused
  definition. Note that if a job is currently running for this definition, Studio
  does not stop it.
- **Run**: Run a single on-demand job from this job definition.
  This option also lets you specify different input parameters to your notebook before
  starting the job.
- **Edit Job Definition**: Change the schedule of your job
  definition. You can select a different time interval, or you can opt for a custom
  schedule using cron syntax.
- **Delete Job Definition**: Remove the job definition from the
  **Notebook Job Definitions** tab. Note that if a job is currently
  running for this definition, Studio does not stop it.
