# Amazon S3 data in Amazon SageMaker Unified Studio

You can bring in Amazon S3 data to your project and access it on the **Data**
page of your project in Amazon SageMaker Unified Studio.

To add S3 tables to your lakehouse in Amazon SageMaker Unified Studio, see [Amazon S3 tables integration](../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-s3-tables-integration.md "../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-s3-tables-integration.md").

To add S3 data as assets in your Amazon SageMaker Unified Studio project catalog, see [Adding Amazon S3 data](adding-existing-s3-data.md "adding-existing-s3-data.md").
In Amazon SageMaker Unified Studio, assets represent specific types of data resources such as database tables, dashboards, S3 buckets or prefixes, or machine learning models.

For S3 data in projects, SageMaker Catalog supports the creation of an asset type of **S3 Object Collection** for an Amazon S3 bucket or S3 prefix in the project.
The S3 Object Collection asset type can be curated with business context metadata by adding business names, descriptions, README, glossary terms, and metadata forms,
including mandatory metadata forms. Assets in Amazon SageMaker Unified Studio are versioned as changes are made in metadata.
