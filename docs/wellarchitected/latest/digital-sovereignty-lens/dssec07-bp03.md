# DSSEC07-BP03 Track data lineage

Organizations in highly regulated industries must implement data
lineage tracking. Data lineage provides critical transparency for
regulatory adherence, impact analysis, and data governance. It
documents the complete journey of data from source to consumption.
This capability becomes essential for demonstrating audit readiness
and maintaining trust in data-driven decision making.

**Desired outcome:** Data movement,
transformations, and dependencies are tracked automatically across
data pipelines through end-to-end lineage capabilities.
Organizations maintain visibility into data flows and possess
audit-ready documentation of data handling practices.

**Common anti-patterns:**

- Manual lineage documentation that becomes outdated quickly and
  fails to capture real-time data transformations and
  dependencies.
- Siloed lineage tracking that only covers specific tools or
  solutions without providing end-to-end visibility across the
  data landscape.
- Reactive lineage capture that attempts to reconstruct data flows
  after issues occur rather than proactively tracking lineage
  during data processing.

**Benefits of establishing this best
practice:**

- Enhanced regulatory adherence through detailed audit trails that
  demonstrate data handling practices and support regulatory
  reporting requirements.
- Improved data governance by providing visibility into data
  quality, transformation logic, and impact analysis for schema
  changes and system modifications.
- Increased data trust by enabling data consumers to understand
  data origins, transformation history, and quality measures
  before making business decisions.
- Reduced compliance costs through automated documentation and
  audit trail generation that removes manual effort and reduces
  audit preparation time.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish a data lineage tracking strategy. Implement automated
lineage capture using AWS services. Use services that integrate
with your existing data processing tools and solutions. Deploy a
centralized lineage repository that can store, query, and
visualize complex data relationships and integrate with governance
tools.

Key AWS services for data lineage implementation include Amazon
DataZone for centralized data governance and lineage
visualization, and AWS Glue for automated lineage capture from
extract, transform, load (ETL) processes.

### Implementation steps

1. **Assess current data landscape and
   lineage requirements**: Conduct an inventory of
   your data sources, processing systems, and consumption
   patterns. Identify critical data flows that require lineage
   tracking based on regulatory requirements, business
   criticality, and data sensitivity levels. Document data
   classification levels and associated lineage requirements:
   - **Highly sensitive
     data**: Full column-level lineage with
     transformation details
   - **Regulated data**:
     Table-level lineage with processing metadata
   - **Internal data**: Basic
     flow tracking with key transformation points

2. **Deploy Amazon DataZone for
   centralized data governance**: Amazon DataZone
   provides OpenLineage-compatible features that enables you to
   capture and visualize data lineage. Follow the steps
   described in the DataZone
   [documentation](../../../datazone/latest/userguide/datazone-data-lineage.md "../../../datazone/latest/userguide/datazone-data-lineage.md").
   See the resources (Related documents) section for additional
   technical measures you can apply.

## Resources

**Related best practices:**

- [SEC07-BP01
  Understand your data classification scheme](../security-pillar/sec_data_classification_identify_data.md "../security-pillar/sec_data_classification_identify_data.md")
- [SEC07-BP02
  Apply data protection controls based on data
  sensitivity](../security-pillar/sec_data_classification_define_protection.md "../security-pillar/sec_data_classification_define_protection.md")
- [SEC07-BP03
  Automate identification and classification](../security-pillar/sec_data_classification_auto_classification.md "../security-pillar/sec_data_classification_auto_classification.md")
- [SEC07-BP04
  Define scalable data lifecycle management](../security-pillar/sec_data_classification_lifecycle_management.md "../security-pillar/sec_data_classification_lifecycle_management.md")

**Related documents:**

- [Introducing
  end-to-end data lineage preview visualization in Amazon
  DataZone](https://aws.amazon.com/blogs/aws/introducing-end-to-end-data-lineage-preview-visualization-in-amazon-datazone/ "https://aws.amazon.com/blogs/aws/introducing-end-to-end-data-lineage-preview-visualization-in-amazon-datazone/")
- [Building
  end-to-end data lineage for one-time and complex queries using
  Amazon Athena, Amazon Redshift, Amazon Neptune, and dbt](https://aws.amazon.com/blogs/big-data/building-end-to-end-data-lineage-for-one-time-and-complex-queries-using-amazon-athena-amazon-redshift-amazon-neptune-and-dbt/ "https://aws.amazon.com/blogs/big-data/building-end-to-end-data-lineage-for-one-time-and-complex-queries-using-amazon-athena-amazon-redshift-amazon-neptune-and-dbt/")
- [Capture
  data lineage from dbt, Apache Airflow, and Apache Spark with
  Amazon SageMaker AI](https://aws.amazon.com/blogs/big-data/capture-data-lineage-from-dbt-apache-airflow-and-apache-spark-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/big-data/capture-data-lineage-from-dbt-apache-airflow-and-apache-spark-with-amazon-sagemaker/")
- [Announcing
  the general availability of data lineage in the next
  generation of Amazon SageMaker AI and Amazon DataZone](https://aws.amazon.com/blogs/aws/announcing-the-general-availability-of-data-lineage-in-the-next-generation-of-amazon-sagemaker-and-amazon-datazone/ "https://aws.amazon.com/blogs/aws/announcing-the-general-availability-of-data-lineage-in-the-next-generation-of-amazon-sagemaker-and-amazon-datazone/")
- [Automate
  data lineage in Amazon SageMaker AI using AWS Glue crawlers
  supported data sources](https://aws.amazon.com/blogs/big-data/automate-data-lineage-in-amazon-sagemaker-using-aws-glue-crawlers-supported-data-sources/ "https://aws.amazon.com/blogs/big-data/automate-data-lineage-in-amazon-sagemaker-using-aws-glue-crawlers-supported-data-sources/")
- [Build
  data lineage for data lakes using AWS Glue, Amazon Neptune,
  and Spline](https://aws.amazon.com/blogs/big-data/build-data-lineage-for-data-lakes-using-aws-glue-amazon-neptune-and-spline/ "https://aws.amazon.com/blogs/big-data/build-data-lineage-for-data-lakes-using-aws-glue-amazon-neptune-and-spline/")
- [Enhance
  data governance through column-level lineage in Quick Suite](https://aws.amazon.com/blogs/business-intelligence/enhance-data-governance-through-column-level-lineage-in-amazon-quicksight/ "https://aws.amazon.com/blogs/business-intelligence/enhance-data-governance-through-column-level-lineage-in-amazon-quicksight/")

**Related videos:**

- [AWS re:Invent 2024 - Empower your data journey with Amazon
  DataZone's data lineage (ANT207-NEW)](https://www.youtube.com/watch?v=p9h2JJSLq4c "https://www.youtube.com/watch?v=p9h2JJSLq4c")
- [AWS Summit Tel Aviv 2024 - Tracing Data from Streaming to Iceberg
  Lakes with OpenLineage (DEM301) - In Hebrew](https://www.youtube.com/watch?v=W4dyBnXpYRk "https://www.youtube.com/watch?v=W4dyBnXpYRk")

**Related services:**

- [Amazon
  DataZone](https://aws.amazon.com/datazone/ "https://aws.amazon.com/datazone/")
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/")
- [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/")
