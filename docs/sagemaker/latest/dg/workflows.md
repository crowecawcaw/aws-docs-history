# SageMaker AI Workflows

As you scale your machine learning (ML) operations, you can use Amazon SageMaker AI fully managed
workflow services to implement continuous integration and deployment (CI/CD) practices for
your ML lifecycle. With the Pipelines SDK, you choose and integrate pipeline steps into a
unified solution that automates the model-building process from data preparation to model
deployment. For Kubernetes based architectures, you can install SageMaker AI Operators on your
Kubernetes cluster to create SageMaker AI jobs natively using the Kubernetes API and
command-line Kubernetes tools such as `kubectl`. With SageMaker AI components for Kubeflow
pipelines, you can create and monitor native SageMaker AI jobs from your Kubeflow Pipelines.
The job parameters, status, and outputs from SageMaker AI are accessible from the Kubeflow
Pipelines UI. Lastly, if you want to schedule batch jobs, you can use either the AWS Batch job queue
integration or the Jupyter notebook-based workflows service to initiate standalone or regular runs on
a schedule you define.

In summary, SageMaker AI offers the following workflow technologies:

- [Pipelines](pipelines.md "pipelines.md"): Tool for building and
  managing ML pipelines.
- [Kubernetes Orchestration](kubernetes-workflows.md "kubernetes-workflows.md"): SageMaker AI
  custom operators for your Kubernetes cluster and components for Kubeflow
  Pipelines.
- [SageMaker Notebook Jobs](notebook-auto-run.md "notebook-auto-run.md"): On demand
  or scheduled non-interactive batch runs of your Jupyter notebook.
  You can also leverage other services that integrate with SageMaker AI to build your workflow.
  Options include the following services:

- [Airflow Workflows](https://sagemaker.readthedocs.io/en/stable/workflows/airflow/index.html "https://sagemaker.readthedocs.io/en/stable/workflows/airflow/index.html"): SageMaker APIs to export configurations for creating and
  managing Airflow workflows.
- [AWS Step Functions](https://sagemaker.readthedocs.io/en/stable/workflows/step_functions/index.html "https://sagemaker.readthedocs.io/en/stable/workflows/step_functions/index.html"): Multi-step ML workflows in Python that orchestrate SageMaker AI
  infrastructure without having to provision your resources separately.
- [AWS Batch](../../../batch/latest/userguide/getting-started-sagemaker.md "../../../batch/latest/userguide/getting-started-sagemaker.md"):
  Submit SageMaker AI training jobs to an AWS Batch job queue, where you can prioritize and schedule jobs
  to run in a compute environment.
  For more information on managing SageMaker training and inference, see [Amazon SageMaker
  Python SDK Workflows](https://sagemaker.readthedocs.io/en/stable/workflows/index.html "https://sagemaker.readthedocs.io/en/stable/workflows/index.html").

###### Topics

- [Pipelines](pipelines.md "pipelines.md")
- [Kubernetes Orchestration](kubernetes-workflows.md "kubernetes-workflows.md")
- [SageMaker Notebook Jobs](notebook-auto-run.md "notebook-auto-run.md")
- [Schedule your ML workflows](workflow-scheduling.md "workflow-scheduling.md")
- [AWS Batch support for SageMaker AI training jobs](training-job-queues.md "training-job-queues.md")
