# Run a visual workflow

To run a workflow, select a workflow from the Workflows page list. Choose **Run**. You can then choose one of
the following two options:

1.  Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in using your SSO or AWS credentials.
2.  Navigate to the project that was created with the **All capabilities** project profile. To do this, use the center
    menu at the top of the landing page and choose **Browse all projects**, then choose the name of the project that you
    want to navigate to.
3.  In the **Build** menu, choose **Workflows**. This takes you to the Workflows page.
4.  Choose the name of the workflow to navigate to the workflow canvas.
5.  Expand the **Run** menu, then choose one of the following options:

        * Run with default parameters. This option starts running the workflow using the parameters already defined in the DAG file. To
         review these parameters, see the **Default parameters** tab.
        * Run with custom parameters. This option opens a window where you can change the inputs for the parameters defined in the DAG
         file. Enter the variables you want to use, and then choose **Start run** to start running the workflow.

    The workflow run then appears on the side panel. The workflow runs until it is complete or until you choose to stop it.

Running a workflow puts tasks together to orchestrate Amazon SageMaker Unified Studio artifacts. You can view multiple runs for
a workflow by navigating to the Workflows page and choosing the name of a workflow from the workflows list table.

If you want to see more runs, you can view them using the Airflow UI. Navigate to the Workflows page, choose the three dots in the
Action column for a workflow, then choose **Open Airflow UI**. This page displays charts and graphics about the workflow.

###### Note

To open the Airflow UI, your browser should allow cross-site cookie sharing. If you receive an error message, check the cookie settings
in your browser.
