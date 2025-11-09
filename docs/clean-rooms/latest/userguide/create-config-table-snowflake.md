# Creating a configured table –

Snowflake data source

In this procedure, the [member](glossary.md#glossary-member "glossary.md#glossary-member") does the following tasks:

- Configures an existing Snowflake table for use in AWS Clean Rooms. (This step can be
  done before or after joining a collaboration, unless using Cryptographic Computing for Clean Rooms.)
- Names the [configured table](glossary.md#glossary-configured-table "glossary.md#glossary-configured-table") and
  chooses which columns to use in the collaboration.
  The following procedure assumes that:

- The collaboration member has already uploaded their data tables to
  Snowflake.
- (Optional) For [encrypted](glossary.md#glossary-encryption "glossary.md#glossary-encryption") data tables only, the
  collaboration member has already [prepared encrypted data tables](prepare-encrypted-data.md "prepare-encrypted-data.md")
  using the C3R encryption client.

###### To create a configured table – Snowflake data source

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Tables**.
3. In the upper right corner, choose **Configure new
   table**.
4. For **Data source**, under **Third-party clouds and
   data sources**, choose **Snowflake**.
5. Specify the **Snowflake credentials** using an existing
   secret ARN or storing a new secret for this table.

Use existing secret ARN

    1. If you have a secret ARN, enter it in the **Secret
     ARN** field.


    You can look up your secret ARN by choosing **Go
     to AWS Secrets Manager**.
    2. If you have an existing secret from another table, choose
     **Import secret ARN from existing
     table**.

###### Note

The secret ARN can be cross-account.

Store a new secret for this table

    1. Enter the following Snowflake credentials:




    	* **Snowflake username**
    	* **Snowflake warehouse**
    	* **Snowflake role**
    	* **Snowflake Privacy Enhanced Mail (PEM)
    	 private key**
    2. For encryption, do one of the following:




    	* To use the AWS managed key (default), leave the
    	 **Customize encryption settings**
    	 checkbox cleared.
    	* To use a custom AWS KMS key:




    		+ Select the **Customize encryption
    		 settings** checkbox.
    		+ For **KMS key**, enter the
    		 key ARN or choose one from the list.
    3. Enter a **Secret name** to help you find
     your credentials later.

6. For **Snowflake table and schema details**, enter the details
   manually or automatically import the details.

Enter the details manually

    1. Enter the **Snowflake account
     identifier**.


    For more information, see [Account identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier#finding-the-organization-and-account-name-for-an-account "https://docs.snowflake.com/en/user-guide/admin-account-identifier#finding-the-organization-and-account-name-for-an-account") in the Snowflake
     documentation.


    Your account identifier must be in the format used for
     Snowflake drivers. You need to replace the period (.) with a
     hyphen (-) so the identifier is formatted as
     `<orgname>-<account_name>`.
    2. Enter the **Snowflake database**.


    For more information, see [Snowflake database](https://docs.snowflake.com/en/sql-reference/snowflake-db "https://docs.snowflake.com/en/sql-reference/snowflake-db") in the Snowflake
     documentation.
    3. Enter the **Snowflake schema
     name**.
    4. Enter the **Snowflake table
     name**.


    For more information, see [Understanding Snowflake Table Structures](https://docs.snowflake.com/en/user-guide/tables-micro-partitions "https://docs.snowflake.com/en/user-guide/tables-micro-partitions") in the
     Snowflake documentation.
    5. For the **Schema**, enter the
     **Column name** and choose the
     **Data type** from the dropdown list.
    6. Choose **Add column** to add more
     columns.




    	* If you choose an **Object data
    	 type**, specify the **Object
    	 schema**.


    	###### Example object schema


    	```
    	name STRING,
    	location OBJECT(
    	    x INT,
    	    y INT,
    	    metadata OBJECT(uuid STRING)
    	),
    	history ARRAY(TEXT)
    	```
    	* If you choose an **Array data
    	 type**, specify the **Array
    	 schema**.


    	###### Example array schema


    	```
    	OBJECT(x INT, y INT)
    	```
    	* If you choose a **Map data
    	 type**, specify the **Map
    	 schema**.


    	###### Example map schema


    	```
    	STRING, OBJECT(x INT, y INT)
    	```

Automatically import the details

    1. Export your COLUMNS view from Snowflake as a CSV
     file.


    For more information about the Snowflake COLUMNS view, see
     [COLUMNS view](https://docs.snowflake.com/en/sql-reference/info-schema/columns "https://docs.snowflake.com/en/sql-reference/info-schema/columns") in the Snowflake
     documentation.
    2. Choose **Import from file** to import the
     CSV file and specify any additional information.


    The database name, schema name, table name, column names
     and data types are automatically imported.




    	* If you choose an **Object data
    	 type**, specify the **Object
    	 schema**.
    	* If you choose an **Array data
    	 type**, specify the **Array
    	 schema**.
    	* If you choose a **Map data
    	 type**, specify the **Map
    	 schema**.
    3. Enter the **Snowflake account
     identifier**.


    For more information, see [Account identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier#finding-the-organization-and-account-name-for-an-account "https://docs.snowflake.com/en/user-guide/admin-account-identifier#finding-the-organization-and-account-name-for-an-account") in the Snowflake
     documentation.

###### Note

Only S3 tables cataloged in AWS Glue can be used to retrieve the
table schema automatically. 7. For **Columns allowed in collaborations**, choose an option
based on your goal.

| Your goal                                                                            | Recommended option |
| ------------------------------------------------------------------------------------ | ------------------ |
| Allow all columns for use in AWS Clean Rooms (subject to analysis<br>rules)          | **All columns**    |
| Allow one or more columns from the \*_Specify allowed<br>columns_<br>• dropdown list | **Custom list**    |

8. For **Configured table details**,
   1. Enter a **Name** for the configured table.

   You can use the default name or rename this table. 2. Enter a **Description** of the table.

   The description helps differentiate between other configured tables
   with similar names. 3. If you want to enable **Tags** for the configured
   table resource, choose **Add new tag** and then enter
   the **Key** and **Value** pair.

9. Choose **Configure new table**.
   Now that you have created a configured table, you are ready to:

- [Add an analysis rule to the configured
  table](add-analysis-rule.md "add-analysis-rule.md")
- [Associate the configured table to a
  collaboration](associate-configured-table.md "associate-configured-table.md")
