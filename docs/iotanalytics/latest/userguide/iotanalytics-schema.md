End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# File formats

AWS IoT Analytics data stores currently support JSON and Parquet file formats. The default file format
is JSON.

- [JSON (JavaScript Object
  Notation)](https://www.json.org/json-en.html "https://www.json.org/json-en.html") - A text format that supports name-value pairs and ordered
  lists of values.
- [Apache
  Parquet](https://parquet.apache.org/documentation/latest/ "https://parquet.apache.org/documentation/latest/") - A columnar storage format used to efficiently store and query
  large volumes of data.
  To configure the file format of the AWS IoT Analytics data store, you can use the
  `FileFormatConfiguration` object when you create the data store.

`fileFormatConfiguration`

Contains the configuration information of file formats. AWS IoT Analytics data stores
support JSON and Parquet.

The default file format is JSON. You can specify only one format. You can't
change the file format after you create the data store.

`jsonConfiguration`

Contains the configuration information of the JSON format.

`parquetConfiguration`

Contains the configuration information of the Parquet
format.

`schemaDefinition`

Information needed to define a schema.

`columns`

Specifies one or more columns that store
your data.

Each schema can have up to 100 columns. Each
column can have up to 100 nested types.

`name`

The name of the column.

Length constraints: 1-255 chars.

`type`

The type of data. For more information about
the supported data type, see [Common
data types](../../../glue/latest/dg/aws-glue-api-common.md "../../../glue/latest/dg/aws-glue-api-common.md") in the
_AWS Glue Developer Guide_.

Length constraints: 1-131072
characters.

AWS IoT Analytics supports all data types listed on the [Data
Types in Amazon Athena](../../../athena/latest/ug/data-types.md "../../../athena/latest/ug/data-types.md") page, except for
`DECIMAL(`precision`,
 `scale`)` -
`precision`.

## Create a data store (console)

The following procedure shows you how to create a data store that saves data in
Parquet format.

###### To create a data store

1. Sign in to the [https://console.aws.amazon.com/iotanalytics/](https://console.aws.amazon.com/iotanalytics/ "https://console.aws.amazon.com/iotanalytics/").
2. In the navigation pane, choose **Data stores**.
3. On the **Data stores** page, choose **Create data
   store**.
4. On the **Specify data store details** page, enter basic
   information about your data store.
   1. For **Data store ID**, enter a unique data store ID.
      You can't change this ID after you create it.
   2. (Optional) For **Tags**, choose **Add new
      tag** to add one or more custom tags (key-value pairs) to
      your data store. Tags can help you identify your resources that you
      create for AWS IoT Analytics.
   3. Choose **Next**.

5. On the **Configure storage type** page, specify how to store
   your data.
   1. For **Storage type**, choose **Service
      managed storage**.
   2. For **Configure how long you want to keep your processed
      data**, choose **Indefinitely**.
   3. Choose **Next**.

6. On the **Configure data format** page, define the structure
   and format of your data records.
   1. For **Classification**, choose
      **Parquet**. You can't change this format after you
      create the data store.
   2. For **Inference source**, choose **JSON
      string** for your data store.
   3. For **String**, enter your schema in JSON format,
      such as the following example.

   ```
   {
       "device_id": "0001",
       "temperature": 26,
       "humidity": 29,
       "datetime": "2018-01-26T07:06:01"
   }
   ```

   4. Choose **Infer schema**.
   5. Under **Configure Parquet schema**, confirm that the
      format matches your JSON example. If the format doesn't match, update
      the Parquet schema manually.
      - If you want your schema to show more columns, choose
        **Add new column**, enter a column name,
        and then choose the data type.

      ###### Note

      By default, you can have 100 columns for your schema. For
      more information, see [AWS IoT Analytics
      quotas](limits.md "limits.md").
      - You can change the data type for an existing column. For more
        information about the supported data types, see [Common data
        types](../../../glue/latest/dg/aws-glue-api-common.md "../../../glue/latest/dg/aws-glue-api-common.md") in the _AWS Glue Developer
        Guide_.

      ###### Note

      After you create your data store, you can't change the
      data type for an existing column.
      - To remove an existing column, choose **Remove
        column**.

   6. Choose **Next**.

7. (Optional) AWS IoT Analytics supports custom partitions in your data store so you can query on pruned data to improve latency.
   For more information about supported custom partitions, see [Custom partitions](custom-partitioning.md "custom-partitioning.md").

Choose **Next**. 8. On the **Review and create** page, review your choices, and
then choose **Create data store**.

###### Important

You can't change the data store ID, file format, or the data type for a
column after you create the data store. 9. Verify that your new data store appears on the **Data
stores** page.
