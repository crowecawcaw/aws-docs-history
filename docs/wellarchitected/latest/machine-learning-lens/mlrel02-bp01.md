# MLREL02-BP01 Use a data catalog

Process data across multiple data stores using data catalog
technology. An advanced data catalog service can enable ETL process
integration. This approach improves reliability and efficiency.

**Desired outcome:** You establish a
centralized system that inventories your ML data assets across the
organization. You can track, discover, and manage data
transformations, and your stakeholders can find and use appropriate
datasets. With a complete data catalog in place, you gain better
data governance, reduce duplication of effort, increase data
quality, and accelerate ML model development through streamlined
data preparation workflows.

**Common anti-patterns:**

- Maintaining separate, isolated data silos without centralized
  metadata.
- Manual tracking of data assets using spreadsheets or wiki pages.
- Failing to document data transformations and lineage.
- Rebuilding ETL processes for each new ML project.
- Relying on tribal knowledge for understanding data
  characteristics.

**Benefits of establishing this best
practice:**

- Provides centralized visibility of available data assets.
- Improves data governance.
- Reduces time spent searching for and understanding data.
- Enhances data quality through consistent transformation
  processes.
- Strengthens collaboration between data engineers and data
  scientists.
- Accelerates ML model development with faster data preparation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A data catalog is critical infrastructure for machine learning
workloads to succeed. Without proper cataloging, data scientists
spend excessive time searching for, understanding, and preparing
data rather than analyzing it or building models. A comprehensive
data catalog provides a centralized inventory of your data assets,
complete with metadata, transformation history, and usage
information.

When implementing a data catalog for ML workloads, focus on
creating a single source of truth for data discovery. The catalog
should document where data resides, what transformations have been
applied, and how it can be accessed. This reduces the time spent
on data preparation, which typically consumes 60-80% of a data
scientist's time.

For AWS environments, the AWS AWS Glue Data Catalog offers a powerful
solution as it integrates seamlessly with other AWS analytics and
machine learning services. By implementing a data catalog as part
of your ML infrastructure, you create a foundation for consistent,
reliable data processing that supports both current and future ML
initiatives.

### Implementation steps

1. **Set up AWS AWS Glue Data Catalog**. Establish the
   [AWSAWS Glue Data Catalog](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") as your central metadata
   repository. This fully managed service provides a unified
   view of your data across multiple data stores, making it
   accessible to various AWS services like
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/"),
   [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/"),
   [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/"), and
   [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/").
2. **Define your metadata
   strategy**. Determine what metadata to capture
   about each dataset, including business definitions, data
   lineage, quality metrics, and usage patterns.
   Well-documented metadata assists data scientists in quickly
   understanding if a dataset is appropriate for their modeling
   needs.
3. **Populate the data
   catalog**. Use
   [AWS Glue crawlers](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") to automatically discover schemas, data
   types, and statistics from your data sources. Crawlers can
   scan various data stores including Amazon S3, Amazon RDS,
   and other database systems. Systematically add your data
   sources to build comprehensive coverage.
4. **Implement ETL processes with AWS Glue**. Create ETL jobs that transform raw data
   into formats optimized for machine learning.
   [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/") can automatically generate Python or Scala code
   for these transformations, reducing development time and
   improving consistency across different data processing
   pipelines.
5. **Establish data lineage
   tracking**. Configure your data catalog to track
   transformations and maintain clear lineage information. With
   data lineage tracking, data scientists can understand data
   provenance, which builds trust in the datasets used for
   model training.
6. **Integrate with ML
   workflows**. Connect your AWS AWS Glue Data Catalog
   with Amazon SageMaker AI to streamline data access for model
   training. For enterprise environments, implement
   [Amazon SageMaker AI Catalog](../../../sagemaker/latest/dg/sagemaker-projects-templates-sm.md "../../../sagemaker/latest/dg/sagemaker-projects-templates-sm.md") as a central metadata hub for ML
   and data assets, enabling secure sharing and governed access
   via Amazon DataZone integration. This integration allows
   data scientists to discover and use properly prepared
   datasets directly from their modeling environments.
7. **Implement access controls and
   governance**. Configure appropriate permissions for
   your data catalog using
   [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") roles. Verify that data scientists have access to
   the metadata and datasets they need while maintaining
   security and regulatory adherence.
8. **Automate catalog
   maintenance**. Set up automated processes to keep
   your data catalog current as new data arrives and
   transformations occur. Regular updates verify that data
   scientists have access to the latest information about
   available datasets.
9. **Monitor and measure
   impact**. Track key metrics like time saved in data
   discovery, reduction in redundant data preparation work, and
   improvements in model development cycles to quantify the
   benefits of your data catalog implementation.

## Resources

**Related documents:**

- [Amazon SageMaker AI and when to use Amazon SageMaker AI vs Amazon
  DataZone](../../../datazone/latest/userguide/sagemaker-datazone.md "../../../datazone/latest/userguide/sagemaker-datazone.md")
- [The
  lakehouse architecture of Amazon SageMaker AI](https://aws.amazon.com/sagemaker/lakehouse/ "https://aws.amazon.com/sagemaker/lakehouse/")
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/")
- [Catalog
  and search](../../../whitepapers/latest/building-data-lakes/data-cataloging.md "../../../whitepapers/latest/building-data-lakes/data-cataloging.md")
- [Getting
  started with serverless ETL on AWS Glue](../../../prescriptive-guidance/latest/serverless-etl-aws-glue/metadata-management.md "../../../prescriptive-guidance/latest/serverless-etl-aws-glue/metadata-management.md")
- [Using
  crawlers to populate the Data Catalog](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md")
- [AWS modern data architecture](../../../prescriptive-guidance/latest/strategy-aws-data/aws-architecture.md "../../../prescriptive-guidance/latest/strategy-aws-data/aws-architecture.md")
- [Moving
  from development to automated ML pipelines using Amazon SageMaker AI and AWS Glue](https://aws.amazon.com/blogs/machine-learning/moving-from-notebooks-to-automated-ml-pipelines-using-amazon-sagemaker-and-aws-glue/ "https://aws.amazon.com/blogs/machine-learning/moving-from-notebooks-to-automated-ml-pipelines-using-amazon-sagemaker-and-aws-glue/")
- [How
  Genworth built a serverless ML pipeline on AWS using Amazon SageMaker AI and AWS Glue](https://aws.amazon.com/blogs/machine-learning/how-genworth-built-a-serverless-ml-pipeline-on-aws-using-amazon-sagemaker-and-aws-glue/ "https://aws.amazon.com/blogs/machine-learning/how-genworth-built-a-serverless-ml-pipeline-on-aws-using-amazon-sagemaker-and-aws-glue/")
- [How
  to build and automate a serverless data lake using AWS Glue](https://aws.amazon.com/blogs/big-data/build-and-automate-a-serverless-data-lake-using-an-aws-glue-trigger-for-the-data-catalog-and-etl-jobs/ "https://aws.amazon.com/blogs/big-data/build-and-automate-a-serverless-data-lake-using-an-aws-glue-trigger-for-the-data-catalog-and-etl-jobs/")

**Related videos:**

- [Amazon SageMaker AI Lakehouse - Unified, open, and secure data
  lakehouse](https://www.youtube.com/watch?v=wH0dZLtS88Y "https://www.youtube.com/watch?v=wH0dZLtS88Y")
- [Understanding
  Amazon S3 Tables: Architecture, performance, and
  integration](https://www.youtube.com/watch?v=e1ypMWSHgsM "https://www.youtube.com/watch?v=e1ypMWSHgsM")
- [Accelerate
  your Analytics and AI with Amazon SageMaker AI LakeHouse](https://www.youtube.com/watch?v=qZTbS0xPN-U "https://www.youtube.com/watch?v=qZTbS0xPN-U")
- [Unifying
  data governance with Immuta and AWS Lake Formation](https://www.youtube.com/watch?v=X09-n2jJZKw "https://www.youtube.com/watch?v=X09-n2jJZKw")

**Related examples:**

- [Explaining
  Credit Decisions with Amazon SageMaker AI](https://github.com/awslabs/sagemaker-explaining-credit-decisions "https://github.com/awslabs/sagemaker-explaining-credit-decisions")
- [How
  to build an end-to-end Machine Learning pipeline using AWS Glue, Amazon S3, Amazon SageMaker AI and Amazon Athena](https://github.com/aws-samples/amazon-sagemaker-predict-accessibility "https://github.com/aws-samples/amazon-sagemaker-predict-accessibility")
