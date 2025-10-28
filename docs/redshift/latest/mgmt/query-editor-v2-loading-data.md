Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading data from Amazon S3

You can load Amazon S3 data into an existing or new table.

###### To load data into an existing table

The COPY command is used by query editor v2 to load data from Amazon S3. The COPY command generated and used in the query editor v2 load data wizard supports
many of the parameters available to the COPY command syntax to copy from Amazon S3.
For information about the COPY command and its options used to load data from Amazon S3, see
[COPY from Amazon Simple Storage Service](../dg/copy-parameters-data-source-s3.md "../dg/copy-parameters-data-source-s3.md") in the _Amazon Redshift Database Developer Guide_.

1. Confirm that the table is already created in the database where you want to load data.
2. Confirm that you are connected to the target database in the tree-view panel of query editor v2 before continuing.
   You can create a connection using the context menu (right-click) to the cluster or workgroup where the data will be loaded.

Choose
![Load](images/qev2-upload.png)**Load data**. 3. For **Data source**, choose **Load from S3 bucket**. 4. In **S3 URIs**, choose **Browse S3** to look for the Amazon S3 bucket that contains the data to load. 5. If the specified Amazon S3 bucket isn't in the same AWS Region as the target table, then
choose the **S3 file location** for the AWS Region where the
data is located. 6. Choose **This file is a manifest file** if the Amazon S3 file is actually a
manifest containing multiple Amazon S3 bucket URIs. 7. Choose the **File format** for the file to be uploaded. The supported data
formats are CSV, JSON, DELIMITER, FIXEDWIDTH, SHAPEFILE, AVRO, PARQUET, and
ORC. Depending on the specified file format, you can choose the respective **File options**. You can also select **Data is encrypted** if the data is encrypted and enter the Amazon Resource Name (ARN) of the KMS key
used to encrypt the data.

If you choose CSV or DELIMITER, you can also choose the **Delimiter character** and whether to
**Ignore header rows** if the specified number of rows are actually column names and not data to load. 8. Choose a compression method to compress your file. The default is no compression. 9. (Optional) The **Advanced settings** support various **Data conversion parameters** and
**Load operations**. Enter this information as needed for your file.

For more information about data conversion and data load parameters, see
[Data
conversion parameters](../dg/copy-parameters-data-conversion.md "../dg/copy-parameters-data-conversion.md") and [Data load
operations](../dg/copy-parameters-data-load.md "../dg/copy-parameters-data-load.md") in the _Amazon Redshift Database Developer Guide_. 10. Choose **Next**. 11. Choose **Load existing table**. 12. Confirm or choose the location of the **Target table** including **Cluster or workgroup**, **Database**, **Schema**,
and **Table** name where the data is loaded. 13. Choose an **IAM role** that has the required permissions to load data from Amazon S3. 14. (Optional) Choose column names to enter them in **Column mapping** to map columns in the order of the input data file. 15. Choose **Load data** to start the data load.

When the load completes, the query editor displays with the generated COPY
command that was used to load your data. The **Result** of
the COPY is shown. If successful, you can now use SQL to select data from
the loaded table. When there is an error, query the system view
STL_LOAD_ERRORS to get more details. For information about COPY command
errors, see [STL_LOAD_ERRORS](../dg/r_STL_LOAD_ERRORS.md "../dg/r_STL_LOAD_ERRORS.md")
in the _Amazon Redshift Database Developer Guide_.
When you load data into a new table, query editor v2 first creates the table in the database, then loads the data as separate actions in the same workflow.

###### To load data into a new table

The COPY command is used by query editor v2 to load data from Amazon S3. The COPY command generated and used in the query editor v2 load data wizard supports
many of the parameters available to the COPY command syntax to copy from Amazon S3.
For information about the COPY command and its options used to load data from Amazon S3, see
[COPY from Amazon Simple Storage Service](../dg/copy-parameters-data-source-s3.md "../dg/copy-parameters-data-source-s3.md") in the _Amazon Redshift Database Developer Guide_.

1. Confirm that you are connected to the target database in the tree-view panel of query editor v2 before continuing.
   You can create a connection using the context menu (right-click) to the cluster or workgroup where the data will be loaded.

Choose
![Load](images/qev2-upload.png)**Load data**. 2. For **Data source**, choose **Load from S3 bucket**. 3. In **S3 URIs**, choose **Browse S3** to look for the Amazon S3 bucket that contains the data to load. 4. If the specified Amazon S3 bucket isn't in the same AWS Region as the target table, then
choose the **S3 file location** for the AWS Region where the
data is located. 5. Choose **This file is a manifest file** if the Amazon S3 file is actually a
manifest containing multiple Amazon S3 bucket URIs. 6. Choose the **File format** for the file to be uploaded. The supported data
formats are CSV, JSON, DELIMITER, FIXEDWIDTH, SHAPEFILE, AVRO, PARQUET, and
ORC. Depending on the specified file format, you can choose the respective **File options**. You can also select **Data is encrypted** if the data is encrypted and enter the Amazon Resource Name (ARN) of the KMS key
used to encrypt the data.

If you choose CSV or DELIMITER, you can also choose the **Delimiter character** and whether to
**Ignore header rows** if the specified number of rows are actually column names and not data to load. 7. Choose a compression method to compress your file. The default is no compression. 8. (Optional) The **Advanced settings** support various **Data conversion parameters** and
**Load operations**. Enter this information as needed for your file.

For more information about data conversion and data load parameters, see
[Data
conversion parameters](../dg/copy-parameters-data-conversion.md "../dg/copy-parameters-data-conversion.md") and [Data load
operations](../dg/copy-parameters-data-load.md "../dg/copy-parameters-data-load.md") in the _Amazon Redshift Database Developer Guide_. 9. Choose **Next**. 10. Choose **Load new table**.

The table columns are inferred from the input data.
You can modify the definition of the table schema by adding columns and table details.
To revert to the query editor v2 inferred table schema, choose **Restore to defaults**. 11. Confirm or choose the location of the **Target table** including **Cluster or workgroup**, **Database**, and **Schema**
where the data is loaded.
Enter a **Table** name to be created. 12. Choose an **IAM role** that has the required permissions to load data from Amazon S3. 13. Choose **Create table** to create the table using the definition shown.

A review summary of the table definition is displayed. The table is created in
the database. To later delete the table, run a DROP TABLE SQL command. For more
information, see [DROP TABLE](../dg/r_DROP_TABLE.md "../dg/r_DROP_TABLE.md") in the
_Amazon Redshift Database Developer Guide_. 14. Choose **Load data** to start the data load.

When the load completes, the query editor displays with the generated COPY
command that was used to load your data. The **Result** of
the COPY is shown. If successful, you can now use SQL to select data from
the loaded table. When there is an error, query the system view
STL_LOAD_ERRORS to get more details. For information about COPY command
errors, see [STL_LOAD_ERRORS](../dg/r_STL_LOAD_ERRORS.md "../dg/r_STL_LOAD_ERRORS.md")
in the _Amazon Redshift Database Developer Guide_.
