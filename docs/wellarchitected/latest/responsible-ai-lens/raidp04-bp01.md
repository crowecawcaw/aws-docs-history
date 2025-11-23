# RAIDP04-BP01 Create a dataset registry

Create a registry to track dataset versions, metadata, and usage
across training, evaluation, and operational contexts. Store
datasets with version control, including local copies of public
benchmarks to assist builders with reproducibility as external
datasets evolve. Document the provenance, characteristics, and
intended use of each dataset version to enable others to understand
appropriate usage and limitations. Link dataset versions to specific
system training events and evaluation results to maintain
traceability between data changes and performance outcomes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Build a centralized registry system that captures essential
   metadata for each dataset including version numbers, creation
   dates, source information, and intended use cases. Start with
   a simple database or structured file system that can track
   when datasets were created, who created them, and what they're
   designed to test.
2. Create version control workflows that automatically snapshot
   datasets whenever changes are made like a version-controlled
   code repository. Test your versioning system by making small
   changes to a dataset and verifying you can retrieve both the
   current and previous versions reliably.
3. Set up local storage for copies of external benchmarks and
   public datasets you use, rather than pulling from external
   sources. Test this by comparing results from your local copy
   against the original source to catch differences that could
   affect reproducibility.
4. Build linking mechanisms that connect specific dataset
   versions to the training runs and evaluations that used them.
   Test this traceability by picking a model performance result
   and verifying you can trace back to the exact dataset version
   that produced it.

## Resources

**Related documents:**

- [Onboarding
  data in Amazon SageMaker AI Unified Studio](../../../sagemaker-unified-studio/latest/adminguide/data-onboarding.md "../../../sagemaker-unified-studio/latest/adminguide/data-onboarding.md")

- [Access
  your existing data and Resources through Amazon SageMaker AI
  Unified Studio, Part 1: AWSAWS Glue Data Catalog and Amazon Redshift](https://aws.amazon.com/blogs/big-data/access-your-existing-data-and-resources-through-amazon-sagemaker-unified-studio-part-1-aws-glue-data-catalog-and-amazon-redshift/ "https://aws.amazon.com/blogs/big-data/access-your-existing-data-and-resources-through-amazon-sagemaker-unified-studio-part-1-aws-glue-data-catalog-and-amazon-redshift/")
  - [Automate
    data lineage in Amazon SageMaker AI using AWS Glue Crawlers
    supported data sources](https://aws.amazon.com/blogs/big-data/automate-data-lineage-in-amazon-sagemaker-using-aws-glue-crawlers-supported-data-sources/ "https://aws.amazon.com/blogs/big-data/automate-data-lineage-in-amazon-sagemaker-using-aws-glue-crawlers-supported-data-sources/")
  - [ISO/IEC
    42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.5 Data provenance

**Related tools:**

- [Data
  discovery and cataloging in AWS Glue](../../../glue/latest/dg/catalog-and-crawler.md "../../../glue/latest/dg/catalog-and-crawler.md")
- [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/")
- [Amazon SageMaker AI Catalog](https://aws.amazon.com/sagemaker/catalog/ "https://aws.amazon.com/sagemaker/catalog/")
- [Accelerate
  generative AI development with Amazon SageMaker AI AI and
  MLflow](https://aws.amazon.com/sagemaker/ai/experiments/ "https://aws.amazon.com/sagemaker/ai/experiments/")
- Amazon SageMaker AI Unified Studio
