# Create a code workflow in Amazon SageMaker Unified Studio

## Prerequisites

The files should be saved in your JupyterLab space in a folder that you can easily locate later.
You must also provision an instance of at least 4GiB memory and 4vCPU in a project created with the
**All capabilities** project profile.

###### To provision an instance for workflows

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that you want to create your workflow in.
3. Expand the **Build** menu in the top navigation, then choose **JupyterLab** to navigate to the JupyterLab IDE.
4. Choose **Configure space**
5. Under **Instance**, select an instance that has at least 4 vCPU and 4GiB. This might result in an additional cost.
6. Choose **Save and restart**. It might take a few minutes for the restart to finish.

If you want to schedule a query to run, you must first save the querybook to the project and pull it into your JupyterLab space. The steps are as follows:

###### To prepare to schedule a query

1. In a project that uses the **All capabilities** project profile, create the query you want to run and save it to the project. For more information, see [Create a query](query-create.md "query-create.md").
2. Expand the **Build** menu in the top navigation, then choose **JupyterLab** to navigate to the JupyterLab IDE.
3. Choose the **Git** icon in the left navigation.
4. Choose the **Pull latest changes** icon to do a git pull and bring the published querybook into your JupyterLab space.
5. Note the location of the file in the JupyterLab file navigation. You will need that path later so you can add it to your workflow.

## Create a code workflow

To create a code workflow, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to a project that was created with the **All capabilities** project profile.
   You can do this by using the center menu at the top of the page and choosing **Browse all projects**, then choosing the name of the project that you want to navigate to.
3. In the **Build** menu, choose **Workflows**. This takes you to the Workflows page.
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

## Sample code workflow

A sample code workflow definition can be seen here.

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
