# Use a form in the Athena console to add an

AWS Glue table

The following procedure shows you how to use the Athena console to add a table using the
**Create Table From S3 bucket data** form.

###### To add a table and enter schema information using a form

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the query editor, next to **Tables and views**, choose
   **Create**, and then choose **S3 bucket
   data.**
3. On the **Create Table From S3 bucket data** form, for
   **Table name**, enter a name for the table. For information
   about acceptable characters for database names, table names, and column names in
   Athena, see [Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md").
4. For **Database configuration**, choose an existing database, or
   create a new one.
5. For **Location of Input Data Set**, specify the path in Amazon S3 to
   the folder that contains the dataset that you want to process. Do not include a file
   name in the path. Athena scans all files in the folder that you specify. If your data
   is already partitioned (for example,

s3://amzn-s3-demo-bucket/logs/year=2004/month=12/day=11/), enter the base path
only (for example, s3://amzn-s3-demo-bucket/logs/). 6. For **Data Format**, choose among the following options:

    * For **Table type**, choose **Apache
     Hive**, **Apache Iceberg**, or **Delta
     Lake**. Athena uses the Apache Hive table type as the default.
     For information about querying Apache Iceberg tables in Athena, see [Query Apache Iceberg tables](querying-iceberg.md "querying-iceberg.md"). For
     information about using Delta Lake tables in Athena, see [Query Linux Foundation Delta Lake tables](delta-lake-tables.md "delta-lake-tables.md").
    * For **File format**, choose the file or log format that
     your data is in.




    	+ For the **Text File with Custom Delimiters**
    	 option, specify a **Field terminator** (that is, a
    	 column delimiter). Optionally, you can specify a
    	 **Collection terminator** that marks the end of
    	 an array type or a **Collection terminator** that
    	 marks the end of a map data type.
    * **SerDe library** – A SerDe
     (serializer-deserializer) library parses a particular data format so that
     Athena can create a table for it. For most formats, a default SerDe library
     is chosen for you. For the following formats, choose a library according to
     your requirements:




    	+ **Apache Web Logs** – Choose either the
    	 **RegexSerDe** or
    	 **GrokSerDe** library. For RegexSerDe, provide
    	 a regular expression in the **Regex definition**
    	 box. For GrokSerDe, provide a series of named regular expressions
    	 for the `input.format` SerDe property. Named regular
    	 expressions are easier to read and maintain than regular
    	 expressions. For more information, see [Query Apache logs stored in Amazon S3](querying-apache-logs.md "querying-apache-logs.md").
    	+ **CSV** – Choose
    	 **LazySimpleSerDe** if your comma-separated
    	 data does not contain values enclosed in double quotes or if it uses
    	 the `java.sql.Timestamp` format. Choose
    	 **OpenCSVSerDe** if your data includes quotes
    	 or uses the UNIX numeric format for `TIMESTAMP` (for
    	 example, `1564610311`). For more information, see [Lazy Simple SerDe for CSV, TSV, and custom-delimited
    	 files](lazy-simple-serde.md "lazy-simple-serde.md")
    	 and [Open CSV SerDe for processing CSV](csv-serde.md "csv-serde.md").
    	+ **JSON** – Choose either the
    	 **OpenX** or **Hive** JSON
    	 SerDe library. Both formats expect each JSON document to be on a
    	 single line of text and that fields not be separated by newline
    	 characters. The OpenX SerDe offers some additional properties. For
    	 more information about these properties, see [OpenX JSON SerDe](openx-json-serde.md "openx-json-serde.md").
    	 For information about the Hive SerDe, see [Hive JSON SerDe](hive-json-serde.md "hive-json-serde.md").
    For more information about using SerDe libraries in Athena, see [Choose a SerDe for your data](supported-serdes.md "supported-serdes.md").

7. For **SerDe properties**, add, edit, or remove properties and
   values according to the SerDe library that you are using and your
   requirements.
   - To add a SerDe property, choose **Add SerDe
     property**.
   - In the **Name** field, enter the name of the property.
   - In the **Value** field, enter a value for the property.
   - To remove a SerDe property, choose **Remove**.

8. For **Table properties**, choose or edit the table properties
   according to your requirements.
   - For **Write compression**, choose a compression option.
     The availability of the write compression option and of the compression
     options available depends on the data format. For more information, see
     [Use compression in Athena](compression-formats.md "compression-formats.md").
   - For **Encryption**, select **Encrypted data
     set** if the underlying data is encrypted in Amazon S3. This option
     sets the `has_encrypted_data` table property to true in the
     `CREATE TABLE` statement.

9. For **Column details**, enter the names and data types of the
   columns that you want to add to the table.
   - To add more columns one at a time, choose **Add a
     column**.
   - To quickly add more columns, choose **Bulk add columns**.
     In the text box, enter a comma separated list of columns in the format
     `column_name`
     `data_type`, `column_name`
     `data_type`[, ...], and then choose
     **Add**.

10. (Optional) For **Partition details**, add one or more column
    names and data types. Partitioning keeps related data together based on column
    values and can help reduce the amount of data scanned per query. For information
    about partitioning, see [Partition your data](partitions.md "partitions.md").
11. (Optional) For **Bucketing**, you can specify one or more columns
    that have rows that you want to group together, and then put those rows into
    multiple buckets. This allows you to query only the bucket that you want to read
    when the bucketed columns value is specified.
    - For **Buckets**, select one or more columns that have a
      large number of unique values (for example, a primary key) and that are
      frequently used to filter the data in your queries.
    - For **Number of buckets**, enter a number that permits
      files to be of optimal size. For more information, see [Top 10
      Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/ "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/") in the AWS Big Data
      Blog.
    - To specify your bucketed columns, the `CREATE TABLE` statement
      will use the following syntax:

    ```
    CLUSTERED BY (`bucketed_columns`) INTO `number_of_buckets` BUCKETS
    ```

###### Note

The **Bucketing** option is not available for the
**Iceberg** table type. 12. The **Preview table query** box shows the `CREATE
 TABLE` statement generated by the information that you entered into the
form. The preview statement cannot be edited directly. To change the statement,
modify the form fields above the preview, or [create the statement
directly](creating-tables-how-to.md#to-create-a-table-using-hive-ddl "creating-tables-how-to.md#to-create-a-table-using-hive-ddl") in the query editor instead of using the form. 13. Choose **Create table** to run the generated statement in the
query editor and create the table.
