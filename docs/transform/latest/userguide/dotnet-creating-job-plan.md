# Creating the AWS Transform .NET job plan

After you create your workspace, on the **Jobs** tab, select
**Create job**. Then follow the prompts from AWS Transform in the chat
pane using natural language. These are the typical steps for creating a .NET modernization
job.

1. AWS Transform will ask you which type of transformation job you would like to create. In the chat, enter _.NET modernization_.
2. AWS Transform will suggest a job name and ask you if you want to change the job
   name. If you would like to change the job name, tell AWS Transform in natural
   language, for example, _change the job name to ExampleCorpDotNet1_.
   Otherwise, in the chat, you can accept the suggested job name. After you accept the job
   name, AWS Transform notifies you in the chat window that it is creating the
   job.
3. AWS Transform creates the transformation job.

## Components of the AWS Transform .NET job plan

The AWS Transform .NET job display has 5 tabs which you select from the vertical icons
on the far left: **Tasks**, **Dashboard**,
**Approvals**, **Artifacts**, and
**Worklog**. Each tab has a left pane and a center chat pane. A right
collaboration pane may appear at times to show additional details and to request human
input.

### Tasks (Job Plan)

This tab displays your job plan in the left pane. A .NET job has 5 steps:

1. _Get resources to be transformed_: In this phase, you create a connector to your code repository using AWS CodeConnections. Depending on your repository permissions, an admin of the code repository may need to approve the connector and give AWS Transform access to the repository.
2. _Discover resources for transformation_: In this phase, AWS Transform discovers repositories in source control, and you select some or all of
   them for assessment.
3. _Assess code for transformation_: Selected repositories are assessed, and you can view assessment reports.
4. _Prepare for transformation_: In this phase, AWS Transform notifies you if any dependencies are missing from your repositories. You can upload the missing dependencies or ignore them. If you are not an admin for the repo, an admin may need to approve the final transformation plan.
5. _Transform_: In this phase, AWS Transform transforms your repo and provides you the ongoing status during the transformation until it's completed. You can review transformation reports to understand what was changed and why.

You can see the status for each step:

- Not started
- Await user input
- In Progress
- Completed

### Dashboard

The **Dashboard** tab provides a high level summary of the
transformation. It displays metrics for the number of jobs transformed, transformation
applied, and estimated time to complete the transformation. Below the dashboard is a
table of repositories and their status - In-progress, Failed, or Success.

### Approvals

Approval requests for the job are displayed and completed on this tab.

### Artifacts

Jjob-related artifacts are uploaded or downloaded from this tab.

### Worklog

AWS Transform logs its actions in the **Worklog** tab. The **Worklog** provides a detailed log of the actions AWS Transform takes, along with human input requests, and your responses to those requests.
