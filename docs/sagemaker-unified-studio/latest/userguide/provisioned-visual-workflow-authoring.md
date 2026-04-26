# Using visual workflows in Amazon SageMaker Unified Studio

With Amazon SageMaker Unified Studio visual workflows, you can create and orchestrate data processing workflows using an intuitive drag-and-drop
interface without writing code. Visual workflows enable you to connect notebooks, queries, and data processing jobs in a graphical
format, and create and manage schedules.

- [Create a visual workflow in Amazon SageMaker Unified Studio](#provisioned-using-visual-workflows "#provisioned-using-visual-workflows")
- [View visual workflow details](#provisioned-view-visual-workflow-details "#provisioned-view-visual-workflow-details")
- [Run a visual workflow](#provisioned-run-visual-workflows "#provisioned-run-visual-workflows")
- [Edit visual workflows](#provisioned-edit-visual-workflows "#provisioned-edit-visual-workflows")
- [View visual workflows code](#provisioned-view-visual-workflows "#provisioned-view-visual-workflows")
- [Clone and Delete visual workflows](#provisioned-clone-delete-visual-workflows "#provisioned-clone-delete-visual-workflows")

## Create a visual workflow in Amazon SageMaker Unified Studio

Use visual workflows to orchestrate data processing jobs, notebooks, and querybooks in your project repositories.
With visual workflows, you can define a collection of tasks organized as a directed acyclic graph (DAG) that can run on a user-defined schedule.

### Prerequisites

- Amazon SageMaker Unified Studio project created with the **All capabilities** project profile
- Access to the **Workflows** page in your project

### Environment status

Use a shared workflow environment to share workflows with other project members. Workflow environments must
be created by project owners. To update or delete a workflow environment, you must be an owner of the project that
the workflow environment is in. After a workflow environment has been created by a project owner, any project member
can sync their files to share them in the environment.

| Environment Statuses | Status   | Shared environment |
| -------------------- | -------- | ------------------ |
| Active               | Active   |
| Missing              | Missing  |
| Loading              | Loading  |
| Creating             | Creating |
| Failed               | Failed   |

### Create a workflow

To create a workflow, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in using your SSO or AWS credentials.
2. Navigate to a project that was created with the **All capabilities** project profile. You can do this
   by choosing a project from the project selector dropdown at the top of the page.
3. In the left navigation pane, choose **Workflows**.

![Screenshot of the Workflows page in the left navigation pane](images/visual-workflows/ScreenshotVisualWorkflow1.png) 4. Choose the **Create new workflow** button or in the **Create new workflow** dropdown
menu, choose **Create in visual builder**. This takes you to the **Visual canvas workflow**.

![Screenshot of the Create new workflow button and dropdown menu](images/visual-workflows/ScreenshotVisualWorkflow2.png) 5. Provide a name to your workflow. 6. Choose a task from one of the three tabs: **Data processing job**, **Querybook**, or **Notebook**. The selected task appears in the
canvas. Configure the task by giving it a name and editing the prepopulated fields.

![Screenshot of the visual canvas with a task selected and configuration fields](images/visual-workflows/ScreenshotVisualWorkflow3.png) 7. Choose the **Add task** icon (+) to add more tasks. You can drag the tasks to fit your workflow. 8. Complete the workflow by connecting the tasks. To connect the tasks, choose the **Add task** icon (+) of one task and
connect it to the **Add task** icon (+) of another task. The arrows represent the execution order and data flow.

![Screenshot of the visual canvas showing connected workflow tasks with arrows](images/visual-workflows/ScreenshotVisualWorkflow4.png) 9. After you create your workflow, you can configure its settings. Choose the **Settings** icon.

    1. In the **Workflow settings** tab you can:




    	* Edit the Workflow name if the workflow has never been saved to a project.
    	* Provide an optional description to the workflow.
    	* Toggle the **Run on schedule** button and set the Schedule status to Active or Paused.
    	* Choose an option from the Schedule dropdown menu to set a schedule for your workflow or specify a CRON expression
    	 in the **Start date and time in UTC** and **End date and time in UTC** fields below.
    Once the settings are set, choose **Apply** to save them.
    2. In the **Default parameters** tab, choose Add parameter and provide a name and a default value to the
     parameter and choose Apply to save them.
    3. In the **Tags** tab, choose Add tag to create an airflow tag to your workflow and provide a name to the
     tag, then choose Apply to save it. Airflow tags help in filtering the workflows. This step is optional.

10. Choose **Save to project** to save the current workflow to the project. If there are any validation errors, the
    notifications symbol next to the settings gear will show a number next to it which indicates the number of errors. You must fix them
    before you can successfully save the workflow to the project.

![Screenshot of the Save to project button with validation error notifications](images/visual-workflows/ScreenshotVisualWorkflow5.png)

## View visual workflow details

After you create a visual workflow, it appears in a list on the Workflows page in Amazon SageMaker Unified Studio. On the Workflows page, you can see
each workflow you created with the name you provided. Note that it might take up to 60 seconds for the workflow to appear in the list.

To view details about workflow runs and parameters, select the name of a workflow from the list on the Workflows page in Amazon SageMaker Unified Studio.

- Choose **View Runs** to view the results of running the workflow. You can filter to show successful runs. This page
  shows information about the workflow run triggers, durations, and timeframes. There is also an **Actions** column where
  you can choose to stop a workflow if it is still running. There is a limit of 1000 rows on the **Runs** tab for a workflow.
- To view more details about a run, choose the name of a run. This takes you to the run details panel with information about the
  tasks and parameters in the workflow. You can view which tasks were successfully completed. For workflows that run Python notebooks
  and not querybooks, you can view the output in the **Notebook output** tab. This can be useful for viewing tasks in
  more detail and troubleshooting if needed.
- The **Default parameters** tab shows the default parameters outlined in the workflow code. To modify the
  parameters, navigate to the **Default parameters** tab from the **Settings** button. For more information
  about parameters, see [Params](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html") in the
  Apache Airflow documentation.
- The **Definition** tab shows the code used for the workflow.
- The **Tags** tab shows optional tags that are defined for the workflow. These are Airflow tags, not AWS tags. For more
  information, see [Add tags to DAGs and use
  it for filtering in the UI](https://airflow.apache.org/docs/apache-airflow/stable/howto/add-dag-tags.html "https://airflow.apache.org/docs/apache-airflow/stable/howto/add-dag-tags.html") in the Apache Airflow documentation.

To view details about workflow runs and parameters, select the name of a workflow from the list on the Workflows page in Amazon SageMaker Unified Studio.

## Run a visual workflow

To run a workflow, select a workflow from the Workflows page list. Choose **Run**. You can then choose one of
the following two options:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in using your SSO or AWS credentials.
2. Navigate to the project that was created with the **All capabilities** project profile. To do this,
   choose a project from the project selector dropdown at the top of the page.
3. In the left navigation pane, choose **Workflows**.
4. Choose the name of the workflow to navigate to the workflow canvas.
5. Expand the **Run** menu, then choose one of the following options:
   - Run with default parameters. This option starts running the workflow using the parameters already defined in the DAG file. To
     review these parameters, see the **Default parameters** tab.
   - Run with custom parameters. This option opens a window where you can change the inputs for the parameters defined in the DAG
     file. Enter the variables you want to use, and then choose **Start run** to start running the workflow.

The workflow run then appears on the side panel. The workflow runs until it is complete or until you choose to stop it.

Running a workflow puts tasks together to orchestrate Amazon SageMaker Unified Studio artifacts. You can view multiple runs for
a workflow by navigating to the Workflows page and choosing the name of a workflow from the workflows list table.

If you want to see more runs, you can view them using the Airflow UI. Navigate to the Workflows page, choose the three dots in the
Action column for a workflow, then choose **Open Airflow UI**. This page displays charts and graphics about the workflow.

###### Note

To open the Airflow UI, your browser should allow cross-site cookie sharing. If you receive an error message, check the cookie settings
in your browser.

## Edit visual workflows

To edit a visual workflow, modify the tasks and workflows in the canvas.

## View visual workflows code

To view a visual workflow code, navigate to the workflow details page by selecting a workflow from the Workflows page list. Then
choose the **Actions** dropdown menu and choose **View code**.

## Clone and Delete visual workflows

You can also clone and delete a visual workflow. Navigate to the workflow details page by selecting a workflow from the Workflows page
list. Then choose the **Actions** dropdown menu and:

- Choose **Clone workflow** to create a copy of your workflow.
- Choose **Delete workflow** to delete the workflow.

###### Note

Clone and delete workflow options are only available for visual workflows.
