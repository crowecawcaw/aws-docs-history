# Code workflows in Amazon SageMaker Unified Studio

Use workflows to orchestrate notebooks, querybooks, and more in your project repositories. With workflows, you can define a collection of tasks organized as a directed acyclic graph (DAG) that can run on a user-defined schedule.

- [Create a code workflow in Amazon SageMaker Unified Studio](#create-workflow "#create-workflow")
- [View code workflow details](#workflows-review-details "#workflows-review-details")
- [Run a code workflow](#workflows-run "#workflows-run")
- [Share a code workflow with other project members in an Amazon SageMaker Unified Studio workflow environment](#sync-workflow-environment "#sync-workflow-environment")

## Create a code workflow in Amazon SageMaker Unified Studio

### Create a code workflow

To create a code workflow, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to a project that was created with the **All capabilities** project profile.
   You can do this by choosing a project from the project selector dropdown at the top of the page.
3. In the left navigation pane, choose **Workflows**.
4. Choose **Create workflow in editor**. This takes you to the Code page
   and opens a new notebook file in the `workflows/dags` folder of the JupyterLab file navigation. The file is prepopulated with a workflow definition template.
5. Update the file as desired to create your workflow.
   1. Update `WORKFLOW_SCHEDULE` to determine when the workflow will be scheduled to run.
   2. Update `NOTEBOOK_PATH` to point to the querybook or JupyterLab notebook that you want to run.
      For example, `'src/querybook.sqlnb'`.
   3. Update `dag_id` with an ID that you can identify later.
   4. Add tags and parameters, if desired. For more information, see [Params](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html") in the Apache Airflow documentation.

When you create a workflow, you are modifying the directed acyclic graph (DAG) within the Python file. A DAG defines a collection of tasks with their dependencies and relationships to show how they should run.

A DAG consists of the following:

- A [DAG](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html") definition. The DAG ID will also be the name of the workflow.
- [Operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html") that describe how to run the DAG and the [tasks](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html") to run.
- [Operator relationships](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html") that describe the order in which to run the
  tasks.

For more information about DAGs, see [DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html# "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#") in the Apache Airflow documentation. You can configure a DAG to run on a
schedule or run it manually.

You can include multiple DAGs to create multiple workflows. When you have included the DAGs you want to use, save the file in the `workflows/dag` folder in JupyterLab.
There might be a slight delay before the workflow appears on the Workflows page.

### Sample code workflow

The following example shows a sample code workflow definition.

```
from airflow.decorators import dag
from airflow.utils.dates import days_ago
from workflows.airflow.providers.amazon.aws.operators.sagemaker_workflows \
    import NotebookOperator

###############################################################################
#
# Enter in your desired schedule as WORKFLOW_SCHEDULE.  Some options include:
#
# '@daily' (daily at midnight)
# '@hourly' (every hour, at the top of the hour)
# '30 */3 * * *' (a CRON string, run at minute 30 past every 3rd hour)
# '0 8 * * 1-5' (a CRON string, run every weekday at 8am)
#
###############################################################################

WORKFLOW_SCHEDULE = '@monthly'

###############################################################################
#
# Enter in the path to your artifacts. Example:
# 'src/example_notebook.ipynb'
#
###############################################################################

PROCESS_PATH = 'src/dataflows/airQualityToLakehouse.vetl'
QUERY_PATH = 'src/QueryBrooklynDataPutInS3.sqlnb'

default_args = {
    'owner': 'alexa',
}


@dag(
    dag_id='air-quality-process-and-query',
    default_args=default_args,
    schedule_interval=WORKFLOW_SCHEDULE,
    start_date=days_ago(2),
    is_paused_upon_creation=False,
    tags=['example-project', 'alexa'],
    catchup=False
)
def air_quality():
    def process_data():
        return NotebookOperator(
               task_id="process-data",
               input_config={'input_path': PROCESS_PATH, 'input_params': {}},
               output_config={'output_formats': ['NOTEBOOK']},
               wait_for_completion=True,
               poll_interval=5
        )

    def query_data():
        return NotebookOperator(
               task_id="query-data",
               input_config={'input_path': QUERY_PATH, 'input_params': {}},
               output_config={'output_formats': ['NOTEBOOK']},
               wait_for_completion=True,
               poll_interval=5
        )

    process_data() >> query_data()


air_quality = air_quality()
```

## View code workflow details

After you create a code workflow, you must share it with the project before it appears on the Workflows page. For more information, see [Share a code workflow with other project members in an Amazon SageMaker Unified Studio workflow environment](#sync-workflow-environment "#sync-workflow-environment"). On the Workflows page, all project members can see each shared workflow by the name defined using the DAG ID.

To view details about workflow runs and parameters, select the name of a workflow from the list on the Workflows page in Amazon SageMaker Unified Studio.

- On the **Runs** tab, you can view the results of running the workflow. You can filter to show successful runs. This page shows information about the workflow run triggers, durations, and timeframes. There is also an **Actions** column where you can choose to stop a workflow if it is still running. There is a limit of 1000 rows on the **Runs** tab for a workflow.

To view more details about a run, choose the name of a run. This takes you to the run details page, with information about the tasks and parameters in the workflow. You can view which tasks were successfully completed on the **Task log** tab. For workflows that run Python notebooks and not querybooks, you can view the output in the **Notebook output** tab. This can be useful for viewing tasks in more detail and troubleshooting if needed.

- The **Default parameters** tab shows the default parameters outlined in the workflow
  code. To modify the parameters, choose **Edit code** and edit parameters. For more
  information about parameters, see [Params](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html") in the Apache Airflow documentation.
- The **Definition** tab shows the code used for the workflow. This matches the code you wrote on the Code page. Choose **Edit code** to navigate back to the Code page and make changes.
- The **Tags** tab shows optional tags that are defined in the workflow definition file.
  These are Airflow tags, not AWS tags. For more information, see [Add tags to DAGs and use it for filtering in the UI](https://airflow.apache.org/docs/apache-airflow/stable/howto/add-dag-tags.html "https://airflow.apache.org/docs/apache-airflow/stable/howto/add-dag-tags.html") in the Apache Airflow
  documentation.

## Run a code workflow

To run a code workflow, navigate to the workflow details page by selecting a workflow from the Workflows page list. Then choose Run. You can then choose one of the following two options:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to a project that was created with the **All capabilities** project profile.
   To do this, choose a project from the project selector dropdown at the top of the page.
3. In the left navigation pane, choose **Workflows**.
4. Choose the name of a workflow to navigate to the workflow details page and choose **Run**. This will execute the workflow in the shared environment, allowing all team members to access and collaborate on the execution.
5. Choose the name of a workflow to navigate to the workflow details page.
6. Expand the **Run** menu, then choose one of the following options:
   - Run with default parameters. This option starts running the workflow using the parameters already defined in the DAG file. To review these parameters, see the **Default parameters** tab.
   - Run with custom parameters. This option opens a window where you can change the inputs for the parameters defined in the DAG file. Enter the variables you want to use, and then choose **Start run** to start running the workflow.

The workflow run then appears on the **Runs** tab of the workflow details page. The workflow runs until it is complete or until you choose to stop it.

Running a workflow puts tasks together to orchestrate Amazon SageMaker Unified Studio artifacts. You can view multiple runs for a workflow by navigating to the Workflows page and choosing the name of a workflow from the workflows list table.

If you want to see more runs, you can view them using the Airflow UI. Navigate to the Workflows page, choose the three dots in the Action column for a workflow, then choose **Open Airflow UI**. This page displays charts and graphics about the workflow.

###### Note

To open the Airflow UI, your browser should allow cross-site cookie sharing. If you receive an error message, check the cookie settings in your browser.

## Share a code workflow with other project members in an Amazon SageMaker Unified Studio workflow environment

**For Git storage:** After a workflow environment has been created by a project owner, any project member can sync their
files to share them in the environment. After you sync your files, all project members can view the workflows you have added in the workflow
environment. Files that are not synced can only be viewed by the project member that created them.

**For S3 storage:** After a workflow environment has been created by a project owner, and once you’ve saved your
workflows DAG files in JupyterLab, they are automatically synced to the project. After the files are synced, all project
members can view the workflows you have added in the workflow environment. Files that are not synced can only be viewed by the project
member that created them.

To share your workflows with other project members in a workflow environment, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to a project that was created with the **Data analytics and AI-ML model development** project profile.
   You can do this by choosing a project from the project selector dropdown at the top of the page.
3. In the left navigation pane, under **IDEs**, choose **JupyterLab**.
4. Locate the workflow you want to share in the `workflows/dags` folder.
5. Choose the **Git** icon in the left navigation.
6. Choose the **+** icon next to the files you want to commit.
7. Enter a brief summary of the commit in the **Summary** text entry field.
8. (Optional) Enter a longer description of the commit in the **Description** text entry field.
9. Choose **Commit**.
10. Choose the **Push committed changes** icon to do a git push.
11. In the left navigation pane, choose **Workflows**.
12. On the **Shared environment** tab, choose **Sync files from project**.
13. Choose **Confirm**.
