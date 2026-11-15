

# Building a unified catalog with Amazon DataZone
<a name="unified-catalog-datazone"></a>

Publication date: **November 20, 2024 ([Diagram history](diagram-history.md))**

The unified data catalog acts as a central repository for all your organization's data assets. This architecture shows how [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/) breaks down data silos by bringing data from various sources together and fostering improved search functionality and trust in data.

## Building a unified catalog with Amazon DataZone diagram
<a name="unified-catalog-datazone-diagram1"></a>

![Data extracted into Amazon S3, Amazon Redshift, and Aurora is cataloged by AWS Glue and published to Amazon DataZone.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/unified-catalog-datazone.png)


The following steps describe the architecture:

1. Extract data using [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/), [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/) (Amazon MSK), or [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) (AWS DMS).

1. Based on end user requirements, store the data in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), or purpose-built databases like [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) or [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/). Design data lakes to store raw structured, semi-structured, and unstructured data at low cost.

1. Crawl structured and semi-structured data from Amazon S3 using [AWS Glue Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html), which writes metadata to [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html). Perform [data quality](https://aws.amazon.com/glue/features/data-quality/) checks on catalog tables at rest using AWS Glue Data Quality. Use Java Database Connectivity (JDBC) data sources to crawl and catalog the data.

1. The Amazon DataZone domain acts as the central catalog repository hub. Use the AWS Glue Data Catalog data source to onboard existing data assets from data lakes and databases. With Amazon Redshift, automatically extract technical metadata of database tables and views to Amazon DataZone.

1. Use the [Amazon DataZone data portal](https://aws.amazon.com/datazone/features/data-discovery/) to discover, catalog, share, and govern data in a self-serve fashion.

1. Organize Amazon DataZone entities under different levels of hierarchy using [domain units](https://docs.aws.amazon.com/datazone/latest/userguide/create-domain-unit.html).

1. [Amazon DataZone data projects](https://docs.aws.amazon.com/datazone/latest/userguide/create-new-project.html) provide a collaborative space where members onboard data assets from their respective business units. [Business glossaries](https://docs.aws.amazon.com/datazone/latest/userguide/create-maintain-business-glossary.html) define business terms associated with data assets. [Metadata forms](https://docs.aws.amazon.com/datazone/latest/userguide/create-metadata-form.html) augment business context of asset metadata. [Custom assets](https://docs.aws.amazon.com/datazone/latest/userguide/create-asset-types.html) expand the catalog beyond predefined system assets.

1. Catalog unstructured data assets stored in Amazon S3 and publish them to Amazon DataZone by tagging them with relevant [custom asset types](https://docs.aws.amazon.com/datazone/latest/userguide/create-asset-types.html).

1. Every data asset onboarded to Amazon DataZone is part of Inventory. Enrich the data asset with business catalogs, data lineage, and data quality to aid discoverability.

## Further reading
<a name="unified-catalog-datazone-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)