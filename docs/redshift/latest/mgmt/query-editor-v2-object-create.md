

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Creating database objects
<a name="query-editor-v2-object-create"></a>

You can create database objects, including databases, schemas, tables, and user-defined functions (UDFs). You must be connected to a cluster or workgroup and a database to create database objects.

## Creating databases
<a name="query-editor-v2-object-create-database"></a>

You can use query editor v2 to create databases in your cluster or workgroup.

**To create a database**

For information about databases, see [CREATE DATABASE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_DATABASE.html) in the *Amazon Redshift Database Developer Guide*. 

1. Choose ![Plus sign icon inside a circle, indicating an add or create action.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/qev2-add.png)**Create**, and then choose **Database**.

1. Enter a **Database name**.

1. (Optional) Select **Users and groups**, and choose a **Database user**.

1. (Optional) You can create the database from a datashare or the AWS Glue Data Catalog. For more information about AWS Glue, see [What is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) in the *AWS Glue Developer Guide*.
   + (Optional) Select **Create using a datashare**, and choose a **Select a datashare**. The list includes producer datashares that can be used to create a consumer datashare in the current cluster or workgroup.
   + (Optional) Select **Create using AWS Glue Data Catalog**, and choose a **Choose an AWS Glue database**. In **Data catalog schema**, enter the name that will be used for the schema when referencing the data in a three-part name (database.schema.table). 

1. Choose **Create database**.

   The new database displays in the tree-view panel.

   When you choose the optional step to query a database created from a datashare, connect to a Amazon Redshift database in the cluster or workgroup (for example, the default database `dev`), and use three-part notation (database.schema.table) that references the database name you created when you selected **Create using a datashare**. The datasharing database is listed in the query editor v2 editor tab, but it is not enabled for direct connection.

   When you choose the optional step to query a database created from a AWS Glue Data Catalog, connect to your Amazon Redshift database in the cluster or workgroup (for example, the default database `dev`), and use three-part notation (database.schema.table) that references the database name you created when you selected **Create using AWS Glue Data Catalog**, the schema you named in **Data catalog schema**, and the table in the AWS Glue Data Catalog. Similar to:

   ```
   SELECT * FROM {{glue-database}}.{{glue-schema}}.{{glue-table}}
   ```
**Note**  
Confirm that you are connected to the default database using the connection method **Temporary credentials using your IAM identity**, and that your IAM credentials have been granted usage privilege to the AWS Glue database.  

   ```
   GRANT USAGE ON DATABASE {{glue-database}} to "IAM:MyIAMUser"
   ```

   The AWS Glue database is listed in the query editor v2 editor tab, but it is not enabled for direct connection.

   For more information about querying an AWS Glue Data Catalog, see [Working with Lake Formation-managed datashares as a consumer](https://docs.aws.amazon.com/redshift/latest/dg/lake-formation-getting-started-consumer.html) and [Working with Lake Formation-managed datashares as a producer](https://docs.aws.amazon.com/redshift/latest/dg/lake-formation-getting-started-producer.html) in the *Amazon Redshift Database Developer Guide*.

**Example creating a database as a datashare consumer**

The following example describes a specific scenario that was used to create a database from a datashare using query editor v2. Review this scenario to learn how you can create a database from a datashare in your environment. This scenario uses two clusters, `cluster-base` (the producer cluster) and `cluster-view` (the consumer cluster).

1. Use the Amazon Redshift console to create a datashare for the table `category2` in cluster `cluster-base`. The producer datashare is named `datashare_base`.

   For information about creating datashares, see [Sharing data across clusters in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html) in the *Amazon Redshift Database Developer Guide*.

1. Use the Amazon Redshift console to accept the datashare `datashare_base` as a consumer for the table `category2` in cluster `cluster-view`.

1. View the tree-view panel in query editor v2 which shows the hierarchy of `cluster-base` as:
   + Cluster: `cluster-base`
     + Database: `dev`
       + Schema: `public`
         + Tables: `category2`

1. Choose ![Plus sign icon inside a circle, indicating an add or create action.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/qev2-add.png)**Create**, and then choose **Database**.

1. Enter `see_datashare_base` for **Database name**.

1. Select **Create using a datashare**, and choose a **Select a datashare**. Choose `datashare_base` to use as the source of the database you are creating.

   The tree-view panel in query editor v2 shows the hierarchy of `cluster-view` as:
   + Cluster: `cluster-view`
     + Database: `see_datashare_base`
       + Schema: `public`
         + Tables: `category2`

1. When you query the data, connect to the default database of the cluster `cluster-view` (typically named `dev`), but reference the datashare database `see_datashare_base` in your SQL.
**Note**  
In the query editor v2 editor view, the selected cluster is `cluster-view`. The selected database is `dev`. The database `see_datashare_base` is listed but is not enabled for direct connection. You choose the `dev` database and reference `see_datashare_base` in the SQL you run.

   ```
   SELECT * FROM "see_datashare_base"."public"."category2";
   ```

   The query retrieves data from the datashare `datashare_base` in the cluster `cluster_base`.

**Example creating a database from an AWS Glue Data Catalog**

The following example describes a specific scenario that was used to create a database from an AWS Glue Data Catalog using query editor v2. Review this scenario to learn how you can create a database from an AWS Glue Data Catalog in your environment. This scenario uses one cluster, `cluster-view` to contain the database you create.

1. Choose ![Plus sign icon inside a circle, indicating an add or create action.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/qev2-add.png)**Create**, and then choose **Database**.

1. Enter `data_catalog_database` for **Database name**.

1. Select **Create using a AWS Glue Data Catalog**, and choose **Choose an AWS Glue database**. Choose `glue_db` to use as the source of the database you are creating.

   Choose **Data catalog schema** and enter `myschema` as the schema name to use in three-part notation.

   The tree-view panel in query editor v2 shows the hierarchy of `cluster-view` as:
   + Cluster: `cluster-view`
     + Database: `data_catalog_database`
       + Schema: `myschema`
         + Tables: `category3`

1. When you query the data, connect to the default database of the cluster `cluster-view` (typically named `dev`), but reference the database `data_catalog_database` in your SQL. 
**Note**  
In the query editor v2 editor view, the selected cluster is `cluster-view`. The selected database is `dev`. The database `data_catalog_database` is listed but is not enabled for direct connection. You choose the `dev` database and reference `data_catalog_database` in the SQL you run.

   ```
   SELECT * FROM "data_catalog_database"."myschema"."category3";
   ```

   The query retrieves data that is cataloged by AWS Glue Data Catalog.

## Creating schemas
<a name="query-editor-v2-object-create-schema"></a>

You can use query editor v2 to create schemas in your cluster or workgroup.

**To create a schema**

For information about schemas, see [Schemas](https://docs.aws.amazon.com/redshift/latest/dg/r_Schemas_and_tables.html) in the *Amazon Redshift Database Developer Guide*. 

1. Choose ![Plus sign icon inside a circle, indicating an add or create action.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/qev2-add.png)**Create**, and then choose **Schema**.

1. Enter a **Schema name**.

1. Choose either **Local** or **External** as the **Schema type**.

   For more information about local schemas, see [CREATE SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_SCHEMA.html) in the *Amazon Redshift Database Developer Guide*. For more information about external schemas, see [CREATE EXTERNAL SCHEMA](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_SCHEMA.html) in the *Amazon Redshift Database Developer Guide*.

1. If you choose **External**, then you have the following choices of an external schema.
   + **Glue Data Catalog** – to create an external schema in Amazon Redshift that references tables in AWS Glue. Besides choosing the AWS Glue database, choose the IAM role associated with the cluster and the IAM role associated with the Data Catalog.
   + **PostgreSQL** – to create an external schema in Amazon Redshift that references an Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition database. Also provide the connection information to the database. For more information about federated queries, see [Querying data with federated queries](https://docs.aws.amazon.com/redshift/latest/dg/federated-overview.html) in the *Amazon Redshift Database Developer Guide*.
   + **MySQL** – to create an external schema in Amazon Redshift that references an Amazon RDS for MySQL or and Amazon Aurora MySQL-Compatible Edition database. Also provide the connection information to the database. For more information about federated queries, see [Querying data with federated queries](https://docs.aws.amazon.com/redshift/latest/dg/federated-overview.html) in the *Amazon Redshift Database Developer Guide*.

1. Choose **Create schema**.

   The new schema appears in the tree-view panel.

## Creating tables
<a name="query-editor-v2-object-create-table"></a>

You can use query editor v2 to create tables in your cluster or workgroup.

**To create a table**

You can create a table based on a comma-separated value (CSV) file that you specify or define each column of the table. For information about tables, see [Designing tables](https://docs.aws.amazon.com/redshift/latest/dg/c_designing-tables-best-practices.html) and [CREATE TABLE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_NEW.html) in the *Amazon Redshift Database Developer Guide*. 

Choose **Open query in editor** to view and edit the CREATE TABLE statement before you run the query to create the table. 

1. Choose ![Plus sign icon inside a circle, indicating an add or create action.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/qev2-add.png)**Create**, and choose **Table**.

1. Choose a schema.

1. Enter a table name.

1. Choose ![Plus sign icon representing an addition or new item action.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/add-plus.png) **Add field** to add a column. 

1. Use a CSV file as a template for the table definition:

   1. Choose **Load from CSV**.

   1. Browse to the file location.

      If you use a CSV file, be sure that the first row of the file contains the column headings.

   1. Choose the file and choose **Open**. Confirm that the column names and data types are what you intend.

1. For each column, choose the column and choose the options that you want:
   + Choose a value for **Encoding**.
   + Choose a **Default value**.
   + Turn on **Automatically increment** if you want the column values to increment. Then specify a value for **Auto increment seed** and **Auto increment step**.
   + Turn on **Not NULL** if the column should always contain a value.
   + Enter a **Size** value for the column.
   + Turn on **Primary key** if you want the column to be a primary key.
   + Turn on **Unique key** if you want the column to be a unique key.

1. (Optional) Choose **Table details** and choose any of the following options:
   + Distribution key column and style.
   + Sort key column and sort type.
   + Turn on **Backup** to include the table in snapshots.
   + Turn on **Temporary table** to create the table as a temporary table.

1. Choose **Open query in editor** to continue specifying options to define the table or choose **Create table** to create the table.

## Creating functions
<a name="query-editor-v2-object-create-function"></a>

You can use query editor v2 to create functions in your cluster or workgroup.

**To create a function**

1. Choose ![Plus sign icon inside a circle, indicating an add or create action.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/qev2-add.png)**Create**, and choose **Function**.

1. For **Type**, choose **SQL** or **Python**.

1. Choose a value for **Schema**.

1. Enter a value for **Name** for the function.

1. Enter a value for **Volatility** for the function.

1. Choose **Parameters** by their data types in the order of the input parameters.

1. For **Returns**, choose a data type.

1. Enter the **SQL program** or **Python program** code for the function.

1. Choose **Create**.

For more information about user-defined functions (UDFs), see [Creating user-defined functions](https://docs.aws.amazon.com/redshift/latest/dg/user-defined-functions.html) in the *Amazon Redshift Database Developer Guide*. 