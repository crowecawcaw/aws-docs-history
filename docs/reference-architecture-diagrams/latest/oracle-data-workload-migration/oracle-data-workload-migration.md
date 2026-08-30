# Oracle Data Workload Migration to AWS Cloud

Publication date: **2020 ([Diagram history](#odwm-diagram-history "#odwm-diagram-history"))**

With this architecture, you can migrate Oracle and non-Oracle workloads from on-premises to AWS. You migrate online transaction processing (OLTP) data to [Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.md") for operational reporting. You migrate online analytical processing (OLAP) data to Snowflake Data Warehouse for historical reporting.

## Oracle Data Workload Migration to AWS Cloud

![Architecture diagram for Oracle data workload migration to AWS with Amazon Aurora, AWS Database Migration Service, AWS Glue, and Amazon S3.](images/oracle-data-workload-migration-to-aws-ra.png)

The following steps describe the architecture:

1. Oracle and non-Oracle backend systems regularly load transactional data into an Oracle Enterprise Data Warehouse.
2. [AWS Schema Conversion Tool](../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md "../../../SchemaConversionTool/latest/userguide/CHAP_Welcome.md") extracts Oracle data definition language (DDL) scripts and schema from all Oracle database tables. It publishes the DDL scripts to Amazon Aurora and sends the schema to Snowflake Data Warehouse.
3. [AWS Database Migration Service](../../../dms/latest/userguide/Welcome.md "../../../dms/latest/userguide/Welcome.md") (AWS DMS) extracts OLAP and OLTP data from all Oracle tables. AWS DMS stores OLAP data in [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") in CSV format. AWS DMS loads OLTP data directly into tables created in Amazon Aurora.
4. Legacy systems load data into an Amazon S3 bucket. [AWS Glue](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") transforms data from the Amazon S3 bucket and loads it into Amazon Aurora.
5. AWS Glue transforms data from Amazon Aurora and stores the transformed data in an Amazon S3 bucket. Snowflake Data Warehouse loads transformed data from the Amazon S3 bucket into OLAP tables.
6. Cloud-based extract-transform-load (ETL) platforms extract data from non-migrated data warehouse systems. These platforms load the data into Snowflake Data Warehouse.
7. [Amazon Quick Sight](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md") receives data for analysis and reporting. Tableau and cloud business intelligence (BI) tools also receive the data.
8. Cloud-based and on-premises BI tools can query OLAP data directly from Snowflake for historical reporting. These tools can also query OLTP data directly from Amazon Aurora for operational reporting.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date            |
| ------------------- | ----------------------------------------------- | --------------- |
| Initial publication | Reference architecture diagram first published. | January 1, 2020 |

###### RSS subscription

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.
