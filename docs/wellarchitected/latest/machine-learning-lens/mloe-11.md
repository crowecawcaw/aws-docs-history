# MLOE-11: Create tracking and version control mechanisms

Due to its exploratory and iterative nature, it’s easy to lose
track of ML model development and its evolution. You need to
experiment with multiple combinations of data, algorithms, and
parameters, all while observing the impact of incremental changes
on model accuracy. Log and track your model experiments with
configuration settings and hyperparameters. Document and version
control any data processing-related findings, processes, and
improvement to enable easier future referencing and reuse. Use a
model registry to register and version control your ML models.
Automate your model deployment with CI/CD processes. To learn more
about knowledge management, refer the best practice documented in
[OPS11-BP04](../framework/ops_evolve_ops_knowledge_management.md "../framework/ops_evolve_ops_knowledge_management.md").

## Implementation plan

- **Track your ML experiments with
  SageMaker AI Experiments** - Amazon SageMaker AI
  Experiments lets you create, manage, analyze, and compare
  your machine learning experiments. SageMaker AI Experiments
  automatically tracks the inputs, parameters, configurations,
  and results of your iterations as runs. You can assign,
  group, and organize these runs into experiments. SageMaker AI
  Experiments is integrated with Amazon SageMaker AI Studio,
  providing a visual interface to browse your active and past
  experiments, compare runs on key performance metrics, and
  identify the best performing models
- **Associate notebook instances with
  Git repositories** - To analyze data, document its
  processing, and evaluate ML models on Amazon SageMaker AI, you
  can use
  [Amazon SageMaker AI Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md"). SageMaker AI Processing can be
  used for feature engineering, data validation, model
  evaluation, and model interpretation. SageMaker AI notebook
  instances can be associated with Git repositories. This
  enables saving notebooks in a source control environment
  that persists after stopping or deleting the notebook
  instance. The notebooks hold the data processing code and
  its documentation. You can associate a default repository
  and up to three additional repositories with a notebook
  instance. The repositories can be hosted in GitHub or on any other Git server.
- **Use SageMaker AI Model
  Registry** - Catalog, manage, and deploy models
  using SageMaker AI Model Registry. Create a model group and,
  for each run of your ML pipeline, create a model version
  that you register in the model group.

## Documents

- [Amazon SageMaker AI – Process Data](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md")
- [Associate
  Git Repositories with SageMaker AI Notebook Instances](../../../sagemaker/latest/dg/nbi-git-repo.md "../../../sagemaker/latest/dg/nbi-git-repo.md")

## Blogs

- [Amazon SageMaker AI notebooks now support Git integration for
  increased persistence, collaboration, and reproducibility](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-notebooks-now-support-git-integration-for-increased-persistence-collaboration-and-reproducibility/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-notebooks-now-support-git-integration-for-increased-persistence-collaboration-and-reproducibility/")
- [Track
  your ML experiments end to end with Data Version Control and
  Amazon SageMaker AI Experiments](https://aws.amazon.com/blogs/machine-learning/track-your-ml-experiments-end-to-end-with-data-version-control-and-amazon-sagemaker-experiments/ "https://aws.amazon.com/blogs/machine-learning/track-your-ml-experiments-end-to-end-with-data-version-control-and-amazon-sagemaker-experiments/")

## Examples

- [Amazon SageMaker AI processing](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_processing.html "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_processing.html")
