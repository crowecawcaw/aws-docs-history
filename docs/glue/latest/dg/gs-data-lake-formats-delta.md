#

Using Delta Lake framework in AWS Glue Studio

##

Using Delta Lake framework in data sources

###

Using Delta Lake framework in Amazon S3 data sources

1. From the Source menu, choose Amazon S3.
2. If you choose Data Catalog table as the Amazon S3 source type, choose a database and table.
3. AWS Glue Studio displays the format as Delta Lake and the Amazon S3 URL.
4. Choose **Additional options** to enter a key-value pair. For example,
   a key-value pair could be: **key**: timestampAsOf and **value**: 2023-02-24 14:16:18.

![The screenshot shows the Additional options section in the Data source properties tab for an Amazon S3 data source node.](images/data_lake_formats_additional_options.png) 5. If you choose Amazon S3 location as the **Amazon S3 source type**, choose the Amazon S3 URL
by clicking **Browse Amazon S3**. 6. In **Data format**, choose Delta Lake.

###### Note

If AWS Glue Studio is unable to infer the schema from the Amazon S3 folder or file you selected,
choose **Additional options** to select a new folder or file.

In **Additional options** choose from the following options under **Schema inference**:

    * Let AWS Glue Studio automatically choose a sample file — AWS Glue Studio will choose a sample file in the
     Amazon S3 location so that the schema can be inferred. In the **Auto-sampled file** field, you can
     view the file that was automatically selected.
    * Choose a sample file from Amazon S3 — choose the Amazon S3 file to use by clicking **Browse Amazon S3**.

7. Click **Infer schema**. You can then view the output schema by clicking on the **Output schema** tab.

###

Using Delta Lake framework in Data Catalog data sources

1. From the **Source** menu, choose AWS Glue Studio Data Catalog.
2. In the **Data source properties** tab, choose a database and table.
3. AWS Glue Studio displays the format type as Delta Lake and the Amazon S3 URL.

###### Note

If your Delta Lake source is not registered as the AWS Glue Data Catalog table yet,
you have two options:

    1. Create a AWS Glue crawler for the Delta Lake data store. For more
     information, see
     [How to specify configuration options for a Delta Lake data store](crawler-configuration.md#crawler-delta-lake "crawler-configuration.md#crawler-delta-lake").
    2. Use an Amazon S3 data source to select your Delta Lake data source. See
     [Using Delta Lake framework in Amazon S3 data sources](#gs-data-lake-formats-delta-lake-s3-data-source "#gs-data-lake-formats-delta-lake-s3-data-source") .

##

Using Delta Lake formats in data targets

###

Using Delta Lake formats in Data Catalog data targets

1. From the **Target** menu, choose AWS Glue Studio Data Catalog.
2. In the **Data source properties** tab, choose a database and table.
3. AWS Glue Studio displays the format type as Delta Lake and the Amazon S3 URL.

###

Using Delta Lake formats in Amazon S3 data sources

Enter values or select from the available options to configure Delta Lake format.

- **Compression Type** — choose from one of the compression type options: Uncompressed or
  Snappy.
- **Amazon S3 Target Location** — choose the Amazon S3 target location by clicking **Browse S3**.
- **Data Catalog update options** — updating the Data Catalog is not supported for this
  format in the Glue Studio visual editor.
  - Do not update the Data Catalog: (Default) Choose this option if you don't want the job to update the
    Data Catalog, even if the schema changes or new partitions are added.
  - To update the Data Catalog after the AWS Glue job execution, run or schedule a
    AWS Glue crawler. For more information, see
    [How to specify configuration options for a Delta Lake data store](crawler-configuration.md#crawler-delta-lake "crawler-configuration.md#crawler-delta-lake").

- **Partition keys** — Choose which columns to use as partitioning keys in the output.
  To add more partition keys, choose **Add a partition key**.
- Optionally, choose **Addtional options** to enter a key-value pair. For example,
  a key-value pair could be: **key**: timestampAsOf and **value**: 2023-02-24 14:16:18.
