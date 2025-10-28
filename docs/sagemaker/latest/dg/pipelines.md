# Pipelines

Amazon SageMaker Pipelines is a purpose-built workflow orchestration service to automate machine learning (ML) development.

Pipelines provide the following advantages over other AWS workflow offerings:

**Auto-scaling serverless infrastructure**
You don't need to manage the underlying orchestration infrastructure to run Pipelines, which
allows you to focus on core ML tasks. SageMaker AI automatically provisions, scales, and
shuts down the pipeline orchestration compute resources as your ML workload demands.

**Intuitive user experience** Pipelines can be created and managed
through your interface of choice: visual editor, SDK, APIs, or JSON. You can drag-and-drop the
various ML steps to author your pipelines in the Amazon SageMaker Studio visual interface. The following
screenshot shows the Studio visual editor for pipelines.

![Screenshot of the visual drag-and-drop interface for Pipelines in Studio.](images/pipelines/pipelines-studio-overview.png)
If you prefer managing your ML workflows programmatically, the SageMaker Python SDK offers advanced orchestration
features. For more information, see
[Amazon SageMaker Pipelines](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html")
in the SageMaker Python SDK documentation.

**AWS integrations**
Pipelines provide seamless integration with all SageMaker AI features and other AWS services to
automate data processing, model training, fine-tuning, evaluation, deployment, and monitoring jobs.
You can incorporate the SageMaker AI features in your Pipelines and navigate across them using deep links to
create, monitor, and debug your ML workflows at scale.

**Reduced costs**
With Pipelines, you only pay for the SageMaker Studio environment and the underlying jobs
that are orchestrated by Pipelines (for example, SageMaker Training, SageMaker Processing, SageMaker AI Inference, and Amazon S3 data storage).

**Auditability and lineage tracking** With Pipelines, you can track
the history of pipeline updates and executions using built-in versioning. Amazon SageMaker ML Lineage
Tracking helps you analyze the data sources and data consumers in the end-to-end ML development
lifecycle.

###### Topics

- [Pipelines overview](pipelines-overview.md "pipelines-overview.md")
- [Pipelines actions](pipelines-build.md "pipelines-build.md")
