# Schedule a query

There are two ways to schedule queries in Amazon SageMaker Unified Studio.

- You can schedule your queries directly in the editor. This way you can schedule a single
  query quickly. The following sections contain information about this method.
- You can schedule your queries using a DAG and the workflows interface. This way you can
  combine multiple elements in the same schedule. For more information about this method, see
  [Using workflows in Amazon SageMaker Unified Studio](workflow-orchestration.md "workflow-orchestration.md").

## Create a schedule for a query in Amazon SageMaker Unified Studio

You can create a schedule directly in the query editor interface in Amazon SageMaker Unified Studio. To do this,
use a project with the **All capabilities** project profile or another project
profile with scheduling enabled in the Tooling blueprint parameters. If you have created a
project that needs to be updated to enable scheduling, contact your admin.

To create a schedule in the query editor, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the query editor. You can do this by choosing **Query
   Editor** from the **Build** menu of a project.
3. After creating and saving your query, choose **Actions**, then
   **Create schedule**.

###### Note

You must have a connection selected in order to create a schedule. 4. Under **Schedule name**, enter a name for the schedule. 5. Under **Schedule status**, choose an option to determine whether the
schedule will begin running after being created.

    * Choose **Active** to activate the schedule and run the Visual ETL flow
     when the schedule indicates it should run.
    * Choose **Paused** to create a schedule that will not run the Visual
     ETL flow yet.

6. (Optional) Write a description of the schedule.
7. Choose a schedule type.
   - Choose **One-time** to run the Visual ETL flow at one specific
     time.
   - Choose **Recurring** to create a schedule that run the Visual ETL flow
     at multiple times that you choose.

8. Choose the days and times that the schedule will run.
9. Choose **Create schedule**.

You can enable project repository auto sync flag when creating or updating the project to
ensure the schedules always execute the latest Query notebook saved to repository. It is
recommended that you test the query in draft mode before saving.

## Review scheduled queries in Amazon SageMaker Unified Studio

You can review scheduled queries in the query editor in Amazon SageMaker Unified Studio. On the schedules page of
the query editor, you can pause, edit, and delete schedules. You can also view the status and
other information for a schedule and choose the name of a schedule to view runs and additional
data.

To review scheduled queries, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to your project.
3. Choose **Query Editor** from the **Build** menu.
4. Choose the Scheduled queries icon in the left navigation of the query editor.

You can then pause, edit, or delete a schedule by choosing the three-dot
**Actions** menu next to a schedule in the list.

To view information about different times the schedule has run, choose the name of the
schedule to view the **Runs** section for that schedule. You can choose the
name of a run to see querybook output and a log for that run.
