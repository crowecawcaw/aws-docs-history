# Configuring data target nodes

The data target is where the job writes the transformed data.

## Overview of data target options

Your data target (also called a _data sink_) can be:

- **S3** – The job writes the data in a file in the
  Amazon S3 location you choose and in the format you specify.

If you configure partition columns for the data target, then the job writes the
dataset to Amazon S3 into directories based on the partition key.

- **AWS Glue Data Catalog** – The job uses the information associated
  with the table in the Data Catalog to write the output data to a target location.

You can create the table manually or with the crawler. You can also use
AWS CloudFormation templates to create tables in the Data Catalog.

- A connector – A connector is a piece of code that facilitates communication
  between your data store and AWS Glue. The job uses the connector and associated
  connection to write the output data to a target location. You can either subscribe to a
  connector offered in AWS Marketplace, or you can create your own custom connector. For more
  information, see [Adding connectors to AWS Glue Studio](creating-custom-connectors.md#creating-connectors "creating-custom-connectors.md#creating-connectors")

You can choose to update the Data Catalog when your job writes to an Amazon S3 data
target. Instead of requiring a crawler to update the Data Catalog when the schema or partitions
change, this option makes it easy to keep your tables up to date. This option simplifies the
process of making your data available for analytics by optionally adding new tables to the
Data Catalog, updating table partitions, and updating the schema of your tables directly from the
job.

## Editing the data target node

The data target is where the job writes the transformed data.

###### To add or configure a data target node in your job diagram

1. (Optional) If you need to add a target node, choose
   **Target** in the toolbar at the top of the visual editor,
   and then choose either **S3** or **Glue Data
   Catalog**.
   - If you choose **S3** for the target, then the job writes the
     dataset to one or more files in the Amazon S3 location you specify.
   - If you choose **AWS Glue Data Catalog** for the target, then the job
     writes to a location described by the table selected from the Data Catalog.

2. Choose a data target node in the job diagram. When you choose a node, the node
   details panel appears on the right-side of the page.
3. Choose the **Node properties** tab, and then enter the following
   information:
   - **Name**: Enter a name to associate with the node in the job
     diagram.
   - **Node type**: A value should already be selected, but you can
     change it as needed.
   - **Node parents**: The parent node is the node in the job
     diagram that provides the output data you want to write to the target location. For
     a pre-populated job diagram, the target node should already have the parent node
     selected. If there is no parent node displayed, then choose a parent node from the
     list.

   A target node has a single parent node.

4. Configure the **Data target properties** information. For more
   information, see the following sections:
   - [Using Amazon S3 for the data target](#edit-job-target-S3 "#edit-job-target-S3")
   - [Using Data Catalog tables for the data target](#edit-job-target-catalog "#edit-job-target-catalog")
   - [Using a connector for the data target](#edit-job-target-connector "#edit-job-target-connector")

5. (Optional) After configuring the data target node properties, you can view the output schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here.

### Using Amazon S3 for the data target

For all data sources except Amazon S3 and connectors, a table must exist in
the AWS Glue Data Catalog for the source type that you choose. AWS Glue Studio does not create the Data Catalog
table.

###### To configure a data target node that writes to Amazon S3

1.  Go to the visual editor for a new or saved job.
2.  Choose a data source node in the job diagram.
3.  Choose the **Data source properties** tab, and then enter the following
    information:
    - **Format**: Choose a format from the list. The available
      format types for the data results are:

          + **JSON**: JavaScript Object Notation.
          + **CSV**: Comma-separated values.
          + **Avro**: Apache Avro JSON binary.
          + **Parquet**: A custom Parquet writer type that is
           optimized for `DynamicFrames` as the data format. Instead of
           requiring a precomputed schema for the data, it computes and modifies the
           schema dynamically.
          + **ORC**: Apache Optimized Row Columnar (ORC) format.
          + **Apache Hudi**: An open-source data lake storage framework that simplifies incremental data processing and data pipeline development.
          + **Apache Iceberg**: A high-performance table format that works just like an SQL table.
          + **Delta Lake**: An open-source data lake storage framework that helps you perform ACID transactions, scale metadata handling, and unify streaming and batch data processing.
          + **XML**: Extensible Markup Language (XML).
          + **Tableau Hyper**: Tableau’s in-memory data engine technology.

      To learn more about these format options, see [Format Options for ETL Inputs and Outputs in AWS Glue](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md") in the
      _AWS Glue Developer Guide_.

    - **Compression Type**: You can choose to optionally compress
      the data using the file types `CSV`, `JSON`, or `Parquet`. The
      default is no compression, or **None**.

| File Type      | Compressions                              |
| -------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| JSON/CSV/XML   | GZIP, BZIP2, BROTLI, DEFLATE, LZ4, Snappy |
| Parquet        | Snappy, LZ4, LZO, BROTLI, GZIP            |
| ORC            | Snappy, ZLIB, Uncompressed, LZO           |
| Avro           | GZIP, BZIP2, BROTLI, DEFLATE, LZ4, Snappy |
| Delta Lake     | GZIP, BZIP2, BROTLI, DEFLATE, LZ4, Snappy |
| Apache Hudi    | GZIP, LZO, Snappy                         |
| Apache Iceberg | GZIP, LZO, Snappy                         |
| Tableau Hyper  | None                                      | <br>• **S3 Target Location**: The Amazon S3 bucket and location for the data output. You can choose the **Browse S3** button to see the Amazon S3 buckets that you have access to and choose one as the target destination. <br>• **Data catalog update options** + **Do not update the Data Catalog**: (Default) Choose this option if you don't want the job to update the Data Catalog, even if the schema changes or new partitions are added. + **Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions**: If you choose this option, the job creates the table in the Data Catalog on the first run of the job. On subsequent job runs, the job updates the Data Catalog table if the schema changes or new partitions are added. You must also select a database from the Data Catalog and enter a table name. + **Create a table in the Data Catalog and on subsequent runs, keep existing schema and add new partitions**: If you choose this option, the job creates the table in the Data Catalog on the first run of the job. On subsequent job runs, the job updates the Data Catalog table only to add new partitions. You must also select a database from the Data Catalog and enter a table name. <br>• **File Partitioning**: Choose which type of partitioning you want to save the output in. + **Autogenerate files (Recommended)**: This is the default value for the number of generated files. + **Multiple file output**: Specify the number of file outputs you want. For optimal performance, use the default auto-generated number of files value. <br>• **Partition keys**: Choose which columns to use as partitioning keys in the output. To add more partition keys, choose **Add a partition key**. File partitioning is not supported for Tableau Hyper as a target format. ### Using Data Catalog tables for the data target For all data sources except Amazon S3 and connectors, a table must exist in the AWS Glue Data Catalog for the target type that you choose. AWS Glue Studio does not create the Data Catalog table. ###### To configure the data properties for a target that uses a Data Catalog table 1. Go to the visual editor for a new or saved job. 2. Choose a data target node in the job diagram. 3. Choose the **Data target properties** tab, and then enter the following information: <br>• **Database**: Choose the database that contains the table you want to use as the target from the list. This database must already exist in the Data Catalog. <br>• **Table**: Choose the table that defines the schema of your output data from the list. This table must already exist in the Data Catalog. A table in the Data Catalog consists of the names of columns, data type definitions, partition information, and other metadata about the target dataset. Your job writes to a location described by this table in the Data Catalog. For more information about creating tables in the Data Catalog, see [Defining Tables in the Data Catalog](tables-described.md "tables-described.md") in the _AWS Glue Developer Guide_. <br>• **Data catalog update options** + **Do not change table definition**: (Default) Choose this option if you don't want the job to update the Data Catalog, even if the schema changes, or new partitions are added. + **Update schema and add new partitions**: If you choose this option, the job updates the Data Catalog table if the schema changes or new partitions are added. + **Keep existing schema and add new partitions**: If you choose this option, the job updates the Data Catalog table only to add new partitions. + **Partition keys**: Choose which columns to use as partitioning keys in the output. To add more partition keys, choose **Add a partition key**. ### Using a connector for the data target If you select a connector for the **Node type**, follow the instructions at [Authoring jobs with custom connectors](job-authoring-custom-connectors.md "job-authoring-custom-connectors.md") to finish configuring the data target properties. |
