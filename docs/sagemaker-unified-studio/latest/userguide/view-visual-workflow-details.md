# View visual workflow details

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
  To view workflow details, choose the workflow name for the environment indicated in the Type column (where Draft represents local environment
  and Saved to Project represents shared environment). For workflows in the other location, click on the three dots under the Actions column and
  choose either **View Last Saved Version** for draft workflows or **View Local Version** for workflows saved to the project.
