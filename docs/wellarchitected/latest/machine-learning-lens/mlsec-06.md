# MLSEC-06: Enforce data lineage

Monitor and track data origins and transformations over time.
Strictly control data access. Perform preventative controls,
auditing, and monitoring to demonstrate data lineage. Implement
integrity checks against training data to detect any unexpected
deviances caused by loss, corruption, or manipulation. Data
lineage enables visibility and helps tracing root cause of data
processing errors. 

## Implementation plan

- **Track records for any
  update** - Create and store information about the
  steps of a ML workflow from data preparation to model
  deployment using
  [Amazon SageMaker AI ML Lineage Tracker](../../../sagemaker/latest/dg/lineage-tracking.md "../../../sagemaker/latest/dg/lineage-tracking.md"). With the tracking
  information you can:
  - Reproduce the workflow steps, track model and dataset
    lineage, and establish model governance and audit
    standards.
  - Consider origin data to be the source of truth.
  - Ingest and process derived datasets and retain
    mappings throughout the process. Iterate from the end
    result back to the original data element.
  - Apply these concepts not just to data, but also the
    code, models, pipelines, and infrastructure. Validate
    that you can trace and audit any activity against
    data, pipeline actions, or machine learning models.

## Documents

- [Amazon SageMaker AI ML Lineage Tracking](../../../sagemaker/latest/dg/lineage-tracking.md "../../../sagemaker/latest/dg/lineage-tracking.md")

## Blogs

- [Using
  model attributes to track your training runs on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-now-comes-with-new-capabilities-for-accelerating-machine-learning-experimentation/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-now-comes-with-new-capabilities-for-accelerating-machine-learning-experimentation/")
