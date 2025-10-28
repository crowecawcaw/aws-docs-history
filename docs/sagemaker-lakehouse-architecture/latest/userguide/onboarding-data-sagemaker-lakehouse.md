# Onboarding data into the lakehouse architecture of Amazon SageMaker

The lakehouse architecture of Amazon SageMaker is a unified data architecture that combines data lakes and data warehouses. It's compatible with Apache Iceberg and specifically optimized for building machine learning and generative AI applications on a single copy of data.

Data onboarding into the lakehouse architecture involves the provision of direct integration pathways for
bringing existing Amazon Simple Storage Service (Amazon S3) data lakes, including Amazon S3 Tables, and Amazon Redshift data warehouses
without complex migrations. The lakehouse architecture enables unified data access by connecting external
sources such as Google BigQuery and Snowflake, allowing
organizations to query and analyze both historical warehouse data and data lakes through a
single interface.

The lakehouse architecture uses the AWS Glue Data Catalog (Data Catalog) for metadata management, providing a centralized
repository that enables data discovery across your organization. For more information, see
[Data discovery and
cataloging in AWS Glue](../../../glue/latest/dg/catalog-and-crawler.md "../../../glue/latest/dg/catalog-and-crawler.md").

After cataloging the data, you can use [AWS Lake Formation](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md") to centrally
manage data access permissions. Data lake administrators can grant fine-grained access
permissions to other IAM principals (users or roles) within the same account or across
accounts using tag-based access control (LF-Tags) and named resources methods. By using LF-Tags,
data administrators can logically organize resources based on attributes such as domain and
sensitivity level, ensuring consistent access controls across analytics and machine learning services
including Amazon Athena, Amazon EMR, AWS Glue or Amazon Redshift Spectrum.

The lakehouse architecture integrates data from the following data sources:

1. **Amazon S3 table buckets** – Created directly within Amazon SageMaker Unified Studio with built-in Apache Iceberg support. For more information, see [Working with Amazon S3 Tables in the lakehouse architecture of Amazon SageMaker](s3-tables-integration.md "s3-tables-integration.md").
2. **Amazon Redshift Managed Storage** – Accessed through federation for unified querying. For more information, see [Amazon Redshift Managed Storage for the lakehouse architecture of Amazon SageMaker](rms-integration.md "rms-integration.md").
3. **Amazon S3 data lakes** – Direct integration of existing S3-based data assets. For more information, see [Amazon S3 data lakes for the lakehouse architecture of Amazon SageMaker](s3-data-lakes.md "s3-data-lakes.md").
4. **Federated catalogs** – External data sources accessible without data duplication. For more information, see [Federated catalogs for the lakehouse architecture of Amazon SageMaker](federated-catalogs.md "federated-catalogs.md").

###### Topics

- [Data source benefits](#data-sources-benefits "#data-sources-benefits")
- [Prerequisites for onboarding data to the lakehouse architecture of Amazon SageMaker](prerequisites-s3-tables.md "prerequisites-s3-tables.md")
- [Working with Amazon S3 Tables in the lakehouse architecture of Amazon SageMaker](s3-tables-integration.md "s3-tables-integration.md")
- [Amazon Redshift Managed Storage for the lakehouse architecture of Amazon SageMaker](rms-integration.md "rms-integration.md")
- [Amazon S3 data lakes for the lakehouse architecture of Amazon SageMaker](s3-data-lakes.md "s3-data-lakes.md")
- [Federated catalogs for the lakehouse architecture of Amazon SageMaker](federated-catalogs.md "federated-catalogs.md")

## Data source benefits

Combining data from data warehouses and data lakes in the lakehouse architecture of Amazon SageMaker offers specific benefits for machine learning workloads,
from real-time feature engineering to historical model training datasets.

### Amazon S3 Tables benefits

- **Built-in Apache Iceberg support** – First cloud object store optimized for analytics workloads.
- **Performance optimization** – Features designed to continuously improve query performance and reduce storage costs for tables.
- **AWS analytics integration** – Automatic discovery and access by AWS analytics services through AWS Glue Data Catalog and AWS Lake Formation.
- **Specialized storage** – Table buckets provide Amazon S3 storage optimized for analytics workloads.

### Amazon Redshift Managed Storage benefits

- **Unified data access** – Query Amazon Redshift tables directly from your lakehouse environment using familiar SQL interfaces.
- **No data movement** – Access Amazon Redshift data in place without ETL processes or data duplication.
- **Consistent governance** – Apply unified access controls and data governance policies across data warehouse and data lake.
- **Performance optimization** – Leverage Amazon Redshift's columnar storage and query optimization for analytical workloads.

### Amazon S3 data lakes benefits

- **Scalable storage** – Store structured, semi-structured, and unstructured data at any scale while maintaining high availability, security, and query performance.
- **Multi-zone architecture** – Raw data zone for original format retention, processed data zone for cleaned data, and curated data zone for business-ready datasets.
- **Cost optimization** – Use columnar formats like Parquet or ORC and implement Amazon S3 lifecycle policies for cost-effective storage.
- **Native AWS integration** – Seamless integration with Amazon Athena, AWS Glue, Amazon EMR, SageMaker AI, and Quick Suite.

### Federated catalogs benefits

- **No data duplication** – Enable in-place querying without data movement.
- **Streamlined connectivity** – Unified interface for connecting to diverse data sources.
- **Fine-grained permissions** – Catalog, database, table, and column-level access controls.
- **Cross-source analytics** – Support for ad hoc reporting and federated queries across multiple data sources.
