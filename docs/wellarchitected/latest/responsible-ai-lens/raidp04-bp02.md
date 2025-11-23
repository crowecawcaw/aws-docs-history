# RAIDP04-BP02 Periodically evaluate and update datasets in the

registry

Schedule regular review cycles that assess whether existing datasets
still meet your evolving requirements and quality standards.
Increment version numbers and update associated documentation
whenever datasets change, maintaining records of what changed and
why. Assess whether dataset updates require corresponding system
retraining or evaluation re-runs to maintain validity of previous
results. Remove or archive outdated dataset versions while
preserving the ability to reproduce historical results when needed
for auditing or comparison purposes.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation considerations

1. Schedule review processes that automatically flag datasets for
   evaluation based on age, usage patterns, or changes in your
   system requirements.
2. Create change management workflows that require documenting
   the reason for a dataset modification along with version
   increments.
3. Compare new dataset versions against established quality
   metrics to catch degradation over time.
4. Design impact assessment procedures that assist you to decide
   when dataset changes require retraining your models or
   re-running evaluations.
5. Set up archival processes that move old dataset versions to
   long-term storage while keeping enough metadata to recreate
   historical results if needed.

## Resources

**Related documents:**

- [Data
  Analytics Lens : Best practice 7.2 – Monitor for data quality
  anomalies](../../../it_it/wellarchitected/latest/analytics-lens/best-practice-7.2---monitor-for-data-quality-anomalies..md "../../../it_it/wellarchitected/latest/analytics-lens/best-practice-7.2---monitor-for-data-quality-anomalies..md")
- [Generative
  AI lens: GENOPS02-BP02 Monitor foundation model metrics](../generative-ai-lens/genops02-bp02.md "../generative-ai-lens/genops02-bp02.md")
- [Data
  quality in Amazon SageMaker AI Unified Studio](../../../sagemaker-unified-studio/latest/userguide/data-quality.md "../../../sagemaker-unified-studio/latest/userguide/data-quality.md")
- [AWS Glue Data Quality](../../../glue/latest/dg/glue-data-quality.md "../../../glue/latest/dg/glue-data-quality.md")
- [Detecting
  data drift using Amazon SageMaker AI](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/ "https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.5 Data provenance

**Related tools:**

- [Amazon SageMaker AI Catalog](https://aws.amazon.com/sagemaker/catalog/ "https://aws.amazon.com/sagemaker/catalog/")
- [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality/ "https://aws.amazon.com/glue/features/data-quality/")
