# Using

workflows in Amazon SageMaker Unified Studio

With a Amazon SageMaker Unified Studio workflow, you can set up and run a series of tasks in Amazon SageMaker Unified Studio.
Amazon SageMaker Unified Studio workflows use Apache Airflow to model data processing procedures and orchestrate your
Amazon SageMaker Unified Studio code artifacts. Go to the **Workflows** page of a project in
Amazon SageMaker Unified Studio to create workflows in Python code, run them, and review logs.

###### Note

Workflows are available in Amazon SageMaker Unified Studio projects created with the **All capabilities** project profile.

To use workflows in Amazon SageMaker Unified Studio, you must provision an instance of at least 4GB memory and 4vCPUs.

There are two compute spaces that you can use for workflows in your project:

- **Local space**. Only you can view and edit the workflows in your local space.
- **Shared environment**. Everyone in the project sees and accesses the files in the shared environment.
  Each workflow that you create starts in your local space as a file. To share your workflows with other users, commit the file defining your workflow and sync the workflow with a shared environment.
