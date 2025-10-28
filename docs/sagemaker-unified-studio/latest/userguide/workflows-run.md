# Run a code workflow

To run a code workflow, navigate to the workflow details page by selecting a workflow from the Workflows page list. Then choose Run. You can then choose one of the following two options:

1.  Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
    using your SSO or AWS credentials.
2.  Navigate to a project that was created with the **All capabilities** project profile.
    To do this, use the center menu at the top of the landing page and choose **Browse all projects**, then choose the name of the project that you want to navigate to.
3.  In the **Build** menu, choose **Workflows**. This takes you to the Workflows page.
4.  When both local and shared environments are running and the workflow type is Saved to project:
    - To run a workflow in local environment, choose the three dots in the **Action** column for a
      workflow, choose **View local version** and then choose **Run**. This will execute
      the workflow in your local environment, limiting the execution to your individual workspace.
    - To run a workflow in shared environment, choose the name of a workflow to navigate to the workflow details page and choose **Run**.
      This will execute the workflow in that shared environment, allowing all team members to access and collaborate on the execution.

5.  When the workflow type is **Draft**, the workflow has not been saved to the project. In this state, you can
    only execute the workflow within your local environment. To run a workflow in the remote workflow environment, you must first save
    the workflow to the project. You must commit your changes to git and choose **Sync files from project** to synchronize
    the committed changes before the workflow becomes available in the shared environment.
6.  Choose the name of a workflow to navigate to the workflow details page.
7.  Expand the **Run** menu, then choose one of the following options:

        * Run with default parameters. This option starts running the workflow using the parameters already defined in the DAG file. To review these parameters, see the **Default parameters** tab.
        * Run with custom parameters. This option opens a window where you can change the inputs for the parameters defined in the DAG file. Enter the variables you want to use, and then choose **Start run** to start running the workflow.

    The workflow run then appears on the **Runs** tab of the workflow details page. The workflow runs until it is complete or until you choose to stop it.

Running a workflow puts tasks together to orchestrate Amazon SageMaker Unified Studio artifacts. You can view multiple runs for a workflow by navigating to the Workflows page and choosing the name of a workflow from the workflows list table.

If you want to see more runs, you can view them using the Airflow UI. Navigate to the Workflows page, choose the three dots in the Action column for a workflow, then choose **Open Airflow UI**. This page displays charts and graphics about the workflow.

###### Note

To open the Airflow UI, your browser should allow cross-site cookie sharing. If you receive an error message, check the cookie settings in your browser.
