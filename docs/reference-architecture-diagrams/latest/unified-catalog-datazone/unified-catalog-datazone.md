

# Building a Unified Catalog with Amazon DataZone
<a name="unified-catalog-datazone"></a>

Publication date: **November 20, 2024 ([Diagram history](#diagram-history))**

The unified data catalog acts as a central repository for all your organization's data assets. This architecture shows how [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html) breaks down data silos by bringing data from various sources together and fostering improved search functionality and trust in data.

## Building a Unified Catalog with Amazon DataZone
<a name="diagram1"></a>

![Architecture diagram showing a unified catalog with Amazon DataZone, AWS Glue, Amazon S3, Amazon Redshift, and Amazon Aurora.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/unified-catalog-datazone/images/unified-catalog-datazone.png)


The following steps describe the architecture:

1. Extract data using [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), Amazon Managed Streaming for Apache Kafka (Amazon MSK), or [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) (AWS DMS).

1. Based on end user requirements, store the data in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html), or purpose-built databases like [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) or [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html). Design data lakes to store raw structured, semi-structured, and unstructured data at low cost.

1. Crawl structured and semi-structured data from Amazon S3 using [AWS Glue Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html), which writes metadata to [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html). Perform [data quality](https://aws.amazon.com/glue/features/data-quality/) checks on catalog tables at rest using AWS Glue Data Quality. Use Java Database Connectivity (JDBC) data sources to crawl and catalog the data.

1. The [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/what-is-datazone.html) domain acts as the central catalog repository hub. Use the AWS Glue Data Catalog data source to onboard existing data assets from data lakes and databases. With Amazon Redshift, automatically extract technical metadata of database tables and views to Amazon DataZone.

1. Use the [Amazon DataZone data portal](https://aws.amazon.com/datazone/features/data-discovery/) to discover, catalog, share, and govern data in a self-serve fashion.

1. Organize Amazon DataZone entities under different levels of hierarchy using [domain units](https://docs.aws.amazon.com/datazone/latest/userguide/create-domain-unit.html).

1. [Amazon DataZone data projects](https://docs.aws.amazon.com/datazone/latest/userguide/create-new-project.html) provide a collaborative space where members onboard data assets from their respective business units. [Business glossaries](https://docs.aws.amazon.com/datazone/latest/userguide/create-maintain-business-glossary.html) define business terms associated with data assets. [Metadata forms](https://docs.aws.amazon.com/datazone/latest/userguide/create-metadata-form.html) augment business context of asset metadata. [Custom assets](https://docs.aws.amazon.com/datazone/latest/userguide/create-asset-types.html) expand the catalog beyond predefined system assets.

1. Catalog unstructured data assets stored in Amazon S3 and publish them to Amazon DataZone by tagging them with relevant [custom asset types](https://docs.aws.amazon.com/datazone/latest/userguide/create-asset-types.html).

1. Every data asset onboarded to Amazon DataZone is part of Inventory. Enrich the data asset with business catalogs, data lineage, and data quality to aid discoverability.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 20, 2024 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.