# Create a visual workflow in IAM-based

domains

Use visual workflows to orchestrate tasks in your project. With visual workflows, you can
define a collection of tasks organized as a directed acyclic graph (DAG) that can run on a
user-defined schedule.

###### To create a visual workflow

1. Log in to Amazon SageMaker Unified Studio.
2. Navigate to the Workflows tool using the left menu, selecting
   **Workflows**.
3. Choose **Create new workflow** to open the Visual Workflows
   editor.
4. Provide a name to your workflow and choose **Save**.
5. In the Find tasks search window under Add tasks, choose a task to add to your
   workflow. The selected task appears in the canvas.
6. Configure the task by giving it a name and editing the prepopulated fields.
7. Choose the **+** symbol to add more tasks. You can drag the tasks to
   fit your workflow.
8. Complete the workflow by connecting the tasks. To connect the tasks, choose the
   **+** symbol of one task to the **+** symbol of
   another task. The arrows represent the execution order and data flow.
9. Once you've created your workflow, you can configure its settings. Choose the settings
   gear.
   1. In the Workflow settings tab you can:
      - Edit the Workflow name if the workflow has never been saved to a
        project.
      - Provide an optional description to the workflow.
      - Toggle the Run on schedule button and set the Schedule status to Active or
        Paused.
      - Choose an option from the Schedule dropdown menu to set a schedule for your
        workflow or specify a CRON expression in the Start date and time in UTC and End
        date and time in UTC fields below.

   2. Once the settings are set, choose **Apply** to save them.
   3. In the Default parameters tab, choose **Add parameter** and
      provide a name and a default value to the parameter and choose
      **Apply** to save them.
   4. In the Tags tab, choose **Add tag** to create an airflow tag to
      your workflow and provide a name to the tag, then choose **Apply** to
      save it. Airflow tags help in filtering the workflows. This step is optional.

10. Choose **Save** to save the current workflow. If there are any
    validation errors, the notifications symbol next to the settings gear will show a number
    next to it which indicates the number of errors. You must fix them before you can
    successfully run the workflow.
