# MLOE-07: Establish a lineage tracker system

Maintain a system that tracks changes for each release. These
changes include documentation, environment, model, data, code,
and infrastructure. Having this system allows you to go back and
quickly reproduce a problem on a prior release, allowing
rollbacks and reproducibility.

## Implementation plan

- **Identify artifacts needed for
  tracking** - Tracking all the artifacts used for
  a production model is an essential requirement for
  reproducing the model to meet regulatory and control
  requirements.
  [Data](../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md")
  [and
  artifacts lineage tracking](../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md") includes the list of
  artifacts needed for tracking.
- **Use SageMaker AIML Lineage
  Tracking** -
  [SageMaker AI
  ML Lineage Tracking](../../../sagemaker/latest/dg/lineage-tracking.md "../../../sagemaker/latest/dg/lineage-tracking.md") creates and stores information
  about the steps of an ML workflow from data preparation to
  model deployment. With the tracking information, you can
  reproduce the workflow steps, track model and data set
  lineage, and establish model governance and audit
  standards.
- **Use SageMaker AI Studio** -
  Use
  [SageMaker AI
  Studio](https://aws.amazon.com/sagemaker/studio/ "https://aws.amazon.com/sagemaker/studio/") to track the lineage of a SageMaker AI ML
  pipeline.
- **Use SageMaker AI Feature
  Store** –
  [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/") is a purpose-built
  repository where you can store and access features so it’s
  much easier to name, organize, and reuse them across
  teams. SageMaker AI Feature Store provides a unified store
  for features during training and real-time inference
  without the need to write additional code or create manual
  processes to keep features consistent
- **Use SageMaker AI Model
  Registry** - Use
  [SageMaker AI
  Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") to catalog models for production,
  manage model versions, and associate metadata with a
  model. Model Registry enables lineage tracking.
- **Use SageMaker AI Pipelines for model
  building** -With
  [SageMaker AI
  Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") you can track the history of your data
  within the pipeline.
  [SageMaker AI
  ML Lineage Tracking](../../../sagemaker/latest/dg/lineage-tracking.md "../../../sagemaker/latest/dg/lineage-tracking.md") lets you analyze input data,
  its source, and the outputs generated.

## Documents

- [SageMaker AI
  ML Lineage Tracking](../../../sagemaker/latest/dg/lineage-tracking.md "../../../sagemaker/latest/dg/lineage-tracking.md")
- [Data
  and artifacts lineage tracking](../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md")
- [SageMaker AI
  Model Building Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md")
- [Track
  the Lineage of a SageMaker AI ML Pipeline](../../../sagemaker/latest/dg/pipelines-lineage-tracking.md "../../../sagemaker/latest/dg/pipelines-lineage-tracking.md")
- [SageMaker AI
  Studio](../../../sagemaker/latest/dg/studio.md "../../../sagemaker/latest/dg/studio.md")
- [SageMaker AI
  Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [SageMaker AI
  Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md")

## Blogs

- [Using
  model attributes to track your training runs on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-now-comes-with-new-capabilities-for-accelerating-machine-learning-experimentation/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-now-comes-with-new-capabilities-for-accelerating-machine-learning-experimentation/")

## Examples

- [Controlling
  and auditing data exploration activities with
  SageMaker AIStudio and AWS Lake Formation](https://github.com/aws-samples/amazon-sagemaker-studio-audit "https://github.com/aws-samples/amazon-sagemaker-studio-audit")
