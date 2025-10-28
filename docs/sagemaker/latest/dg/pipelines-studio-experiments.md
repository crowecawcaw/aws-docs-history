# Access experiment data from a pipeline

###### Note

SageMaker Experiments is a feature provided in Studio Classic only.

When you create a pipeline and specify [pipeline_experiment_config](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.pipeline.Pipeline.pipeline_experiment_config "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.pipeline.Pipeline.pipeline_experiment_config"), Pipelines creates the following SageMaker Experiments entities
by default if they don't exist:

- An experiment for the pipeline
- A run group for every execution of the pipeline
- A run for each SageMaker AI job created in a pipeline step
  For information about how experiments are integrated with pipelines, see [Amazon SageMaker Experiments Integration](pipelines-experiments.md "pipelines-experiments.md"). For more
  information about SageMaker Experiments, see [Amazon SageMaker Experiments in Studio Classic](experiments.md "experiments.md").

You can get to the list of runs associated with a pipeline from either the pipeline
executions list or the experiments list.

**To view the runs list from the pipeline executions
list**

1. To view the pipeline executions list, follow the first five steps in the _Studio Classic_ tab of [View the details of a pipeline](pipelines-studio-list.md "pipelines-studio-list.md").
2. On the top right of the screen, choose the **Filter** icon (
   ![Funnel or filter icon representing data filtering or narrowing down options.](images/jumpstart/jumpstart-filter-icon.png)
   ).
3. Choose **Experiment**. If experiment integration wasn't deactivated
   when the pipeline was created, the experiment name is displayed in the executions list.

###### Note

Experiments integration was introduced in v2.41.0 of the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").
Pipelines created with an earlier version of the SDK aren't integrated with experiments
by default. 4. Select the experiment of your choice to view run groups and runs related to that
experiment.
**To view the runs list from the experiments list**

1. In the left sidebar of Studio Classic, choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
2. Select **Experiments** from the menu.
3. Use search bar or **Filter** icon (
   ![Funnel or filter icon representing data filtering or narrowing down options.](images/jumpstart/jumpstart-filter-icon.png)
   ) to filter the list to experiments created by a pipeline.
4. Open an experiment name and view a list of runs created by the pipeline.
