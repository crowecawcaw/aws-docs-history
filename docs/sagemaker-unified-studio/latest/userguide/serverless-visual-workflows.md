# Using serverless visual workflows

With Amazon SageMaker Unified Studio serverless visual workflows, you can create and orchestrate tasks
using an intuitive drag-and-drop interface without writing code. Visual workflows supports over
80 tasks to help interact with multiple AWS services and automate use-cases across analytics,
compute, catalog and storage. For the full list of supported tasks, see [Supported operators](../../../mwaa/latest/mwaa-serverless-userguide/operators.md "../../../mwaa/latest/mwaa-serverless-userguide/operators.md").

- [Create a serverless visual workflow](#serverless-create-visual-workflow "#serverless-create-visual-workflow")
- [View visual workflows code](#serverless-view-visual-workflow-code "#serverless-view-visual-workflow-code")
- [Monitor your workflow](#serverless-monitor-visual-workflow "#serverless-monitor-visual-workflow")
- [Converting existing Airflow DAGs](#serverless-convert-airflow-dags "#serverless-convert-airflow-dags")

## Create a serverless visual workflow

Use visual workflows to orchestrate tasks in your project. With visual workflows, you can
define a collection of tasks organized as a directed acyclic graph (DAG) that can run on a
user-defined schedule.

###### To create a visual workflow

1. Log in to Amazon SageMaker Unified Studio.
2. In the left navigation pane, choose
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

## View visual workflows code

To view a visual workflow code, navigate to the workflow details page by selecting a
workflow from the Workflows page list. Then choose the Actions dropdown menu and choose
**View code**.

## Monitor your workflow

###### To monitor your workflow

1. From the Workflows view, choose the vertical dots to the far right of your workflow's
   name and select **View runs**.
2. In the subsequent Runs view you will see your workflow runs.
3. Choose the run to show the tasks.
4. Choose the task ID to show the task output and associated logs.

## Converting existing Airflow DAGs

You can convert existing Airflow workflows to YAML through a Python library. For more
information, see [Introducing
Amazon MWAA Serverless](https://aws.amazon.com/blogs/big-data/introducing-amazon-mwaa-serverless/ "https://aws.amazon.com/blogs/big-data/introducing-amazon-mwaa-serverless/") on the AWS Big Data Blog.
