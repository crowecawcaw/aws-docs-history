# Notebook jobs details in Amazon SageMaker Studio

SageMaker Notebook Jobs dashboards help organize the job definitions that you schedule, and
also keep track of the actual jobs that run from your job definitions. There are two important
concepts to understand when scheduling notebook jobs: _job
definitions_ and _job runs_. Job definitions are
schedules you set to run specific notebooks. For example, you can create a job definition that
runs notebook XYZ.ipynb every Wednesday. This job definition launches the actual job runs
which occur this coming Wednesday, next Wednesday, the Wednesday after that, and so on.

###### Note

The SageMaker Python SDK notebook job step does not create job definitions. However, you can
view your jobs in the Notebook Jobs dashboard. Both jobs and job definitions are available
if you schedule your job in a JupyterLab environment.

The interface provides two main tabs that help you track your existing job definitions and
job runs:

- **Notebook Jobs** tab: This tab displays a list of all your job runs
  from your on-demand jobs and job definitions. From this tab, you can directly access the
  details for a single job run. For example, you can view a single job run that occurred two
  Wednesdays ago.
- **Notebook Job Definitions** tab: This tab displays a list of all
  your job definitions. From this tab, you can directly access the details for a single job
  definition. For example, you can view the schedule you created to run XYZ.ipynb every
  Wednesday.
  For details about the **Notebook Jobs** tab, see [View notebook jobs](view-notebook-jobs.md "view-notebook-jobs.md").

For details about the **Notebook Job Definitions** tab, see [View notebook job definitions](view-def-detail-notebook-auto-run.md "view-def-detail-notebook-auto-run.md").
