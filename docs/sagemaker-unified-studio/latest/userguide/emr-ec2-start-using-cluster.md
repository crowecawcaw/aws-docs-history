# Using an Amazon EMR on EC2 cluster

After connecting to an Amazon EMR on EC2 cluster, you can begin using the cluster.
To get started, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the compute connection. You can
   do this by using the center menu at the top of the page and choosing
   **Browse all projects**, then choosing the name of the
   project that you want to navigate to.
3. On the **Compute** page, choose the name of the compute you want
   to initialize. This takes you to a page with details about the cluster. Make a note of the name of the compute.
4. Choose **Actions > Open JupyterLab IDE**.
5. In the first cell, choose a connection type that you want to use from the dropdown list
   of connection types. Then choose the name of the compute from the dropdown list of compute options.
6. Choose the **Run** icon.
   Your cluster is now initialized and configured to be a compute resource in your Amazon SageMaker Unified Studio project.
