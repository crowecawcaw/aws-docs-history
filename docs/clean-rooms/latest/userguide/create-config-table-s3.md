# Creating a configured table – Amazon S3 data

source

In this procedure, the [member](glossary.md#glossary-member "glossary.md#glossary-member") does the following tasks:

- Configures an existing AWS Glue table for use in AWS Clean Rooms. (This step can be
  done before or after joining a collaboration, unless using Cryptographic Computing for Clean Rooms.)

###### Note

AWS Clean Rooms supports AWS Glue tables. For more information about getting your
data in AWS Glue, see [Step 3: Upload your data table to Amazon S3](prepare-data-S3.md#upload-to-s3 "prepare-data-S3.md#upload-to-s3").

- Names the [configured table](glossary.md#glossary-configured-table "glossary.md#glossary-configured-table") and
  chooses which columns to use in the collaboration.
  The following procedure assumes that:

- The collaboration member has already [uploaded their data tables to Amazon S3](prepare-data-S3.md#upload-to-s3 "prepare-data-S3.md#upload-to-s3") and
  [created an AWS Glue table](prepare-data-S3.md#create-glue-crawler "prepare-data-S3.md#create-glue-crawler").

###### Note

If you are using the Spark analytics engine, the **Results
destination in Amazon S3** can't be within the same S3 bucket as any
data source.

- (Optional) For [encrypted](glossary.md#glossary-encryption "glossary.md#glossary-encryption") data tables only, the
  collaboration member has already [prepared encrypted data tables](prepare-encrypted-data.md "prepare-encrypted-data.md")
  using the C3R encryption client.
  You can use the statistic generation provided by AWS Glue to compute column-level
  statistics for AWS Glue Data Catalog tables. After AWS Glue generates statistics for tables in the
  Data Catalog, Amazon Redshift Spectrum automatically uses those statistics to optimize the query
  plan. For more information about computing column-level statistics using AWS Glue, see
  [Optimizing
  query performance using column statistics](../../../glue/latest/dg/column-statistics.md "../../../glue/latest/dg/column-statistics.md") in the _AWS Glue User Guide_. For more information about AWS Glue, see the _[AWS
  Glue Developer Guide](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md")_.

###### To create a configured table – Amazon S3 data source

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Tables**.
3. In the upper right corner, choose **Configure new
   table**.
4. For **Data source**, under **AWS data
   sources**, choose **Amazon S3**.
5. Under **Amazon S3 table**:
   1. Select the **Region** where the S3 table is
      hosted.

   By default, the current Region (such as N. Virginia
   us-east-1) is selected.

   ###### Warning

   When your Amazon S3 data source is in a different Region than your
   processing location, data processing may occur temporarily outside
   the source Region. Before proceeding, verify that cross-Region data
   movement complies with your data sovereignty requirements,
   regulatory compliance policies, and data governance standards.

   For more information about Regions, see [Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
   _AWS General Reference_. 2. Choose the **Database** from the dropdown
   list. 3. Choose the **Table** that you want to configure from
   the dropdown list.###### Note

To verify that this is the correct table, do either one of the
following:

    * Choose **View in AWS Glue**.
    * Turn on **View schema from AWS Glue** to view the
     schema.

###### Important

For AWS Glue tables where the data is in CSV format, the column names and
order in the Glue schema must exactly match the CSV data. If they don't
align, the allowed columns list for the configured table might not be
enforced properly. 6. For **Columns and analysis methods allowed in
collaborations**,

    1. For **Which columns do you want to allow in
     collaborations?**




    	* Choose **All columns** to allow all columns
    	 to be queried in the collaboration.
    	* Choose **Custom list** to allow one or more
    	 columns from the **Specify allowed columns**
    	 dropdown list to be queried in the collaboration.
    2. For **Allowed analysis methods**,


    	1. Choose **Direct query** to allow SQL queries
    	 to be run directly on this table
    	2. Choose **Direct job** to allow PySpark jobs
    	 to be run directly on this table.###### Example

For example, if you want to allow collaboration members to run both direct
SQL queries and PySpark jobs on all columns, then choose **All
columns**, **Direct query**, and
**Direct job**. 7. For **Configured table details**,

    1. Enter a **Name** for the configured table.


    You can use the default name or rename this table.
    2. Enter a **Description** of the table.


    The description helps differentiate between other configured tables
     with similar names.

8. If you want to enable **Tags** for the configured table
   resource, choose **Add new tag** and then enter the
   **Key** and **Value** pair.
9. Choose **Configure new table**.
   Now that you have created a configured table, you are ready to:

- [Add an analysis rule to the configured
  table](add-analysis-rule.md "add-analysis-rule.md")
- [Associate the configured table to a
  collaboration](associate-configured-table.md "associate-configured-table.md")
