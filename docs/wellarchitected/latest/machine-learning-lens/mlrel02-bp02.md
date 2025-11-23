# MLREL02-BP02 Use a data pipeline

Automate the processing, movement, and transformation of data
between different compute and storage services. This automation
enables data processing that is fault tolerant, repeatable, and
highly available.

**Desired outcome:** You achieve
streamlined and consistent data processing workflows that
automatically handle data movement and transformations. You can
process your machine learning data with increased reliability,
repeatability, and availability, while reducing manual effort and
potential errors. Your data processing becomes more efficient and
scalable, enabling you to focus on deriving insights rather than
managing data logistics.

**Common anti-patterns:**

- Manually moving and transforming data between systems.
- Creating one-off scripts for data processing tasks.
- Inconsistent data transformation processes across teams.
- Neglecting error handling and recovery mechanisms in data
  workflows.
- Not versioning data processing code or configurations.

**Benefits of establishing this best
practice:**

- Reduces manual errors and inconsistencies in data processing.
- Increases repeatability and reliability of data transformations.
- Enables fault tolerance and automatic recovery mechanisms.
- Improves scalability of data processing workflows.
- Facilitates collaboration through standardized data processing
  patterns.
- Enhances traceability and governance of data transformations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data is the foundation of a machine learning workload, and how you
handle this data directly impacts the quality of your ML models.
Data pipelines automate and standardize the process of collecting,
cleaning, transforming, and delivering data to your ML workflows.
Without proper data pipelines, your ML initiatives can suffer from
inconsistent data quality, limited reproducibility, and
operational inefficiencies.

Creating effective data pipelines requires careful planning around
data sources, transformation logic, error handling, and monitoring
capabilities. By implementing automated data pipelines, you verify
that your data preparation follows a consistent, repeatable
process that can scale with your ML workload demands. This
approach leads to more reliable models and faster deployment
cycles.

AWS provides a comprehensive set of tools specifically designed to
build robust ML data pipelines, with Amazon SageMaker AI offering
integrated capabilities for the entire ML lifecycle. These tools
enable you to focus on deriving insights from your data rather
than managing infrastructure.

### Implementation steps

1. **Assess your data processing
   requirements**. Begin by identifying your data
   sources, required transformations, and destination systems.
   Document the flow of data from source to consumption, noting
   data quality requirements, validation rules, or business
   logic that must be applied during processing.
2. **Implement data preparation and
   wrangling processes**. Establish comprehensive data
   preparation workflows that transform raw data into ML-ready
   formats. Use a combination of AWS services and tools to:
   - Connect to data sources including
     [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"),
     [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/"),
     [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/"), and other databases using appropriate
     connectors
   - Explore and profile your data using
     [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/") with Apache Spark or
     [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/") interactive sessions to identify patterns,
     anomalies, and data quality issues
   - Transform your data using
     [AWS Glue ETL jobs](../../../glue/latest/dg/author-job.md "../../../glue/latest/dg/author-job.md"),
     [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/") clusters, or
     [SageMaker AI
     Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md") jobs with custom transformation
     scripts
   - Generate data quality reports and validation checks
     using
     [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/ "https://aws.amazon.com/glue/features/databrew/") or custom validation scripts to
     identify issues before model training
   - Create reusable data preparation workflows using
     [AWS Glue workflows](../../../glue/latest/dg/workflows_overview.md "../../../glue/latest/dg/workflows_overview.md") or
     [SageMaker AI
     Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") that verify consistency across
     different datasets and projects

3. **Build automated ML workflows with
   SageMaker AI Pipelines**. After creating your data
   preparation workflow, export it to
   [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") to automate your entire ML
   workflow. SageMaker AI Pipelines helps you:
   - Create end-to-end ML workflows that combine data
     preparation, model training, evaluation, and deployment
   - Automate pipeline execution on a schedule or
     trigger-based approach
   - Track lineage of ML artifacts for governance
   - Implement quality gates to verify that models meet
     performance criteria
   - Version control your pipelines for reproducibility

4. **Implement error handling and
   monitoring**. Configure your pipelines to handle
   errors gracefully and provide visibility into pipeline
   performance:
   - Set up retry mechanisms for transient failures
   - Create notification systems for critical pipeline
     failures
   - Implement logging throughout your pipeline steps
   - Use
     [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to monitor pipeline metrics and set up
     alerts

5. **Version and store your data
   artifacts**. Maintain traceability of your data
   processing:
   - Store processed datasets in Amazon S3 with appropriate
     versioning
   - Use
     [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/") to create reusable
     feature repositories
   - Document data transformations and their business logic
   - Implement data lineage tracking to understand data
     provenance

6. **Integrate with your existing ML
   workflow**. Connect your data pipelines to other
   components of your ML environment:
   - Feed processed data directly into model training jobs
   - Integrate with model registries and deployment pipelines
   - Establish feedback loops from model performance back to
     data preparation

7. **Scale your data processing as
   needed**. Configure your pipelines to handle
   growing data volumes:
   - Use distributed processing for large datasets with
     services like
     [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/")
   - Implement incremental processing patterns for streaming
     data
   - Configure compute resources appropriately for each
     pipeline stage

## Resources

**Related documents:**

- [Data
  transformation workloads with SageMaker AI Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md")
- [Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md")
- [Get
  started with Amazon SageMaker AI Feature Store](../../../sagemaker/latest/dg/feature-store-getting-started.md "../../../sagemaker/latest/dg/feature-store-getting-started.md")
- [Data
  preparation and cleaning](../../../prescriptive-guidance/latest/modern-data-centric-use-cases/data-preparation-cleaning.md "../../../prescriptive-guidance/latest/modern-data-centric-use-cases/data-preparation-cleaning.md")
- [Run
  secure processing jobs using PySpark in Amazon SageMaker AI
  Pipelines](https://aws.amazon.com/blogs/machine-learning/run-secure-processing-jobs-using-pyspark-in-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/run-secure-processing-jobs-using-pyspark-in-amazon-sagemaker-pipelines/")
- [Building,
  automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/")

**Related videos:**

- [AWS Glue and Amazon SageMaker AI Studio Integration](https://aws.amazon.com/awstv/watch/5d00e03ffe3/ "https://aws.amazon.com/awstv/watch/5d00e03ffe3/")
- [Build,
  automate, manage, and scale ML workflows using Amazon SageMaker AI Pipelines](https://www.youtube.com/watch?v=Hvz2GGU3Z8g "https://www.youtube.com/watch?v=Hvz2GGU3Z8g")

**Related examples:**

- [Amazon SageMaker AI Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples")
- [MLOps
  Workshop with Amazon SageMaker AI Pipelines](https://catalog.us-east-1.prod.workshops.aws/workshops/741835d3-a2bf-4cb6-81f0-d0bb4a62edca/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/741835d3-a2bf-4cb6-81f0-d0bb4a62edca/en-US")
