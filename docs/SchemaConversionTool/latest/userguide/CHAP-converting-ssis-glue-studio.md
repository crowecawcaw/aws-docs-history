# Converting SSIS pacakges to AWS Glue Studio with AWS Schema Conversion Tool

You can use AWS SCT to convert Microsoft SQL Server Integration Services (SSIS) packages to
AWS Glue Studio.

An _SSIS package_ includes the necessary components, such as
the connection manager, tasks, control flow, data flow, parameters, event handlers,
and variables, to run a specific extract, transform, and load (ETL) task. AWS SCT
converts SSIS packages to a format compatible with AWS Glue Studio. After you migrate your
source database to the AWS Cloud, you can run these converted AWS Glue Studio jobs to perform
ETL tasks.

To convert Microsoft SSIS packages to AWS Glue Studio, make sure that you use AWS SCT version
1.0.661 or higher.

###### Topics

- [Prerequisites](#CHAP-converting-ssis-glue-studio-prerequisites "#CHAP-converting-ssis-glue-studio-prerequisites")
- [Adding SSIS packages to your AWS SCT project](#CHAP-converting-ssis-glue-studio-create "#CHAP-converting-ssis-glue-studio-create")
- [Converting SSIS packages to AWS Glue Studio with AWS SCT](#CHAP-converting-ssis-glue-studio-convert "#CHAP-converting-ssis-glue-studio-convert")
- [Creating AWS Glue Studio jobs using the converted code](#CHAP-converting-ssis-glue-studio-jobs "#CHAP-converting-ssis-glue-studio-jobs")
- [Creating an assessment report for an SSIS package with AWS SCT](#CHAP-converting-ssis-glue-studio-assessment "#CHAP-converting-ssis-glue-studio-assessment")
- [SSIS components that AWS SCT can convert to AWS Glue Studio](#CHAP-converting-ssis-glue-studio-supported-components "#CHAP-converting-ssis-glue-studio-supported-components")

## Prerequisites

In this section, learn about the prerequisite tasks for the conversion of SSIS packages to
AWS Glue. These tasks include creating required AWS resources in your account.

You can use AWS Identity and Access Management (IAM) to define policies and roles that are needed to access resources
that AWS Glue Studio uses. For more information, see [IAM permissions for the AWS Glue Studio user](../../../glue/latest/ug/setting-up.md#getting-started-min-privs "../../../glue/latest/ug/setting-up.md#getting-started-min-privs").

After AWS SCT converts your source scripts to AWS Glue Studio, upload the converted scripts to an
Amazon S3 bucket. Make sure that you create this Amazon S3 bucket and select it in the AWS
service profile settings. For more information about creating an S3 bucket, see
[Create your first S3 bucket](../../../AmazonS3/latest/userguide/creating-bucket.md "../../../AmazonS3/latest/userguide/creating-bucket.md") in the
_Amazon Simple Storage Service User Guide_.

To make sure that AWS Glue Studio can connect to your data store, create a custom connector and a
connection. Also, store database credentials in AWS Secrets Manager.

###### To create a custom connector

1. Download the JDBC driver for your data store. For more information about JDBC drivers
   that AWS SCT uses, see [Installing JDBC drivers for AWS Schema Conversion Tool](CHAP_Installing.md "CHAP_Installing.md").
2. Upload this driver file to your Amazon S3 bucket. For more information, see
   [Upload an object to your bucket](../../../AmazonS3/latest/userguide/uploading-an-object-bucket.md "../../../AmazonS3/latest/userguide/uploading-an-object-bucket.md") in the _Amazon Simple Storage Service User Guide_.
3. Sign in to the AWS Management Console and open the AWS Glue Studio console at [https://console.aws.amazon.com/gluestudio/](https://console.aws.amazon.com/gluestudio/ "https://console.aws.amazon.com/gluestudio/").
4. Choose **Connectors**, then choose **Create custom connector**.
5. For **Connector S3 URL**, choose **Browse S3**,
   and choose the JDBC driver file that you uploaded to your Amazon S3 bucket.
6. Enter a descriptive **Name** for your connector. For example,
   enter `SQLServer`.
7. For **Connector type**, choose **JDBC**.
8. For **Class name**, enter the name of the main class for your JDBC driver.
   For SQL Server, enter `com.microsoft.sqlserver.jdbc.SQLServerDriver`.
9. For **JDBC URL base**, enter the JDBC base URL. The syntax of the JDBC
   base URL depends on your source database engine. For SQL Server, use the
   following format:
   `jdbc:sqlserver://$`<host>`:$`<port>`;databaseName=$`<dbname>`;user=$`<username>`;password=$`<password>``.

Make sure that you replace `<host>`, `<port>`,
`<dbname>`, `<username>`, and
`<password>` with your values. 10. For **URL parameter delimiter**, enter the semicolon (`;`). 11. Choose **Create connector**.

###### To store database credentials in AWS Secrets Manager

1. Sign in to the AWS Management Console and open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. On the **Choose secret type** page, do the following:
   1. For **Secret type**, choose the **Other type of secret**.
   2. For **Key/value pairs**, enter the following keys:
      `host`, `port`,
      `dbname`, `username`,
      and `password`.

   Next, enter your values for these keys.

4. On the **Configure secret** page, enter a descriptive **Secret name**.
   For example, enter `SQL_Server_secret`.
5. Choose **Next**. Then, on the **Configure rotation** page,
   choose **Next** again.
6. On the **Review** page, review your secret details, and then choose
   **Store**.

###### To create a connection for your connector

1. Sign in to the AWS Management Console and open the AWS Glue Studio console at [https://console.aws.amazon.com/gluestudio/](https://console.aws.amazon.com/gluestudio/ "https://console.aws.amazon.com/gluestudio/").
2. Choose the connector for which you want to create a connection, and then choose
   **Create connection**.
3. On the **Create connection** page, enter a descriptive **Name**
   for your connection. For example, enter `SQL-Server-connection`.
4. For **AWS Secret**, choose the secret that you created in AWS Secrets Manager.
5. Configure **Network options**, then choose **Create connection**.

Now, you can create an AWS Glue Studio job with a custom connector. For more information, see
[Creating AWS Glue Studio jobs](#CHAP-converting-ssis-glue-studio-jobs "#CHAP-converting-ssis-glue-studio-jobs").

## Adding SSIS packages to your AWS SCT project

You can add multiple SSIS packages to a single AWS SCT project.

###### To add an SSIS package to your AWS SCT project

1. Create a new project with AWS SCT or open an existing project.
   For more information, see [Starting and managing Projects in AWS SCT](CHAP_UserInterface.md "CHAP_UserInterface.md").
2. Choose **Add source** from the menu, and then choose
   **SQL Server Integration Services**.
3. For **Connection name**, enter a name for your SSIS packages. AWS SCT
   displays this name in the tree in the left panel.
4. For **SSIS packages folder**, enter the path to the folder
   with source SSIS packages.
5. Choose **Add target** from the menu, and then choose
   **AWS Glue Studio**.

To connect to AWS Glue Studio, AWS SCT uses your AWS profile. For more
information, see [Managing Profiles in the AWS Schema Conversion Tool](CHAP_UserInterface.md "CHAP_UserInterface.md"). 6. Create a mapping rule, which includes your source SSIS package
and your AWS Glue Studio target. For more information, see [Mapping data types in the AWS Schema Conversion Tool](CHAP_Mapping.md "CHAP_Mapping.md"). 7. Create AWS Glue Studio connections in the AWS Glue Studio console. For more information, see [Creating connections for connectors](../../../glue/latest/ug/connectors-chapter.md#creating-connections "../../../glue/latest/ug/connectors-chapter.md#creating-connections"). 8. Choose **Connection managers** in the left tree,
open the context (right-click) menu, and then choose
**Configure connections**.

AWS SCT displays the **Configure connections** window. 9. For each source SSIS connection, choose an AWS Glue Studio connection.

## Converting SSIS packages to AWS Glue Studio with AWS SCT

Following, find how to convert SSIS packages to AWS Glue Studio using AWS SCT.

###### To convert an SSIS package to AWS Glue Studio

1. Add your SSIS package to your AWS SCT project. For more information,
   see [Adding SSIS packages to your AWS SCT project](#CHAP-converting-ssis-glue-studio-create "#CHAP-converting-ssis-glue-studio-create").
2. In the left panel, expand the **ETL** and
   **SSIS** nodes.
3. Choose **Packages**, open the context (right-click) menu,
   and then choose **Convert package**.

AWS SCT converts your selected SSIS packages to JSON files. These JSON objects
represent a node in a directed acyclic graph (DAG). Find your converted files
in the **Package DAGs** node in the right tree. 4. Choose **Package DAGs**, open the context (right-click) menu,
and then choose **Save to Amazon S3**.

Now you can use these scripts to create jobs in the AWS Glue Studio.

## Creating AWS Glue Studio jobs using the converted code

After you convert your source SSIS packages, you can use the converted JSON files
to create AWS Glue Studio jobs.

###### To create an AWS Glue Studio job

1. Choose **Package DAGs** in the right tree, open the
   context (right-click) menu, and then choose
   **Configure AWS Glue Studio job**.
2. (Optional) Apply the extension pack that emulates SSIS functions in AWS Glue Studio.
3. The **Configure AWS Glue Studio job** window opens.

Complete the **Basic job properties** section:

    * **Name** – Enter a name of your
     AWS Glue Studio job.
    * **Script file name** – Enter a name
     of your job script.
    * **Job parameters** – Add parameters
     and enter their values.

Choose **Next**. 4. Complete the **Advanced job properties** section:

    * **IAM Role** – Choose the IAM role
     that is used for authorization to AWS Glue Studio and access data stores.
    * **Script file S3 path** – Enter the Amazon S3 path
     to your converted script.
    * **Temporary directory** – Enter the Amazon S3 path
     to a temporary directory for intermediate results. AWS Glue Studio uses this directory to
     read or write to Amazon Redshift.
    * AWS SCT automatically generates the path for Python libraries. You can
     review this path in **Generated python library path**. You can't edit this
     automatically generated path. To use additional Python libraries, enter the path in
     **User python library path**.
    * **User python library path** – Enter the paths for additional
     user Python libraries. Separate Amazon S3 paths with commas.
    * **Dependent jars path** – Enter the paths for dependent
     `*.jar` files. Separate Amazon S3 paths with
     commas.
    * **Referenced files path** – Enter the paths for additional
     files, such as configuration files, that are required by your
     script. Separate Amazon S3 paths with commas.
    * **Worker type** – Choose `G.1X` or
     `G.2X`.


    When you choose `G.1X` each worker maps to 1 DPU (4 vCPU,
     16 GB of memory, and 64 GB disk).


    When you choose `G.2X` each worker maps to 2 DPU (8 vCPU,
     32 GB of memory, and 128 GB disk).
    * **Requested number of workers** – Enter the number of
     workers that are allocated when the job runs.
    * **Max concurrency** – Enter the maximum number of concurrent runs
     that are allowed for this job. The default is 1. AWS Glue returns an error when this threshold is reached.
    * **Job timeout (minutes)** – Enter the timeout value on your ETL
     job as a safeguard against runaway jobs. The default is 2,880
     minutes (48 hours) for batch jobs. If the job exceeds this limit,
     the job run state changes to `TIMEOUT`.
    * **Delay notification threshold (minutes)** – Enter the threshold in minutes
     before AWS SCT sends a delay notification.
    * **Number of retries** – Enter the number of times
     (0–10) that AWS Glue should automatically restart the job if
     it fails. Jobs that reach the timeout limit aren't restarted.
     The default is 0.

Choose **Finish**.

AWS SCT configures your selected AWS Glue Studio jobs. 5. Find your configured jobs under **ETL jobs** in the right tree. Choose
your configured job, open the context (right-click) menu, and then choose
**Create AWS Glue Studio job**. 6. Choose **Apply status** and make sure that the
**Status** value for your job is
**Success**. 7. Open the AWS Glue Studio console, choose **Refresh**, and
choose your job. Then choose **Run**.

## Creating an assessment report for an SSIS package with AWS SCT

The _ETL migration assessment report_ provides information about
converting your SSIS packages to a format compatible with AWS Glue Studio. The assessment
report includes action items for the components of your SSIS packages. These action
items show which components AWS SCT can't automatically convert.

###### To create an ETL migration assessment report

1. Expand the **SSIS** node under **ETL**
   in the left panel.
2. Choose **Packages**, open the context (right-click) menu,
   and then choose **Create report**.
3. View the **Summary** tab. Here, AWS SCT displays the executive summary
   information from the ETL migration assessment report. It includes conversion
   results for all components of your SSIS packages.
4. (Optional) Save a local copy of the ETL migration assessment report as either a
   PDF file or a comma-separated values (CSV) file:
   - To save the ETL migration assessment report as a PDF file,
     choose **Save to PDF** at upper right.

   The PDF file contains the executive summary, action items, and
   recommendations for scripts conversion.
   - To save the ETL migration assessment report as a CSV file, choose **Save to CSV** at upper right.

   AWS SCT creates three CSV files. These files contain action items,
   recommended actions, and an estimated complexity of manual effort
   required to convert the scripts.

5. Choose the **Action items** tab. This tab contains a list
   of items that require manual conversion to AWS Glue Studio. When you choose an action item
   from the list, AWS SCT highlights the item from your source SSIS package that the
   action item applies to.

## SSIS components that AWS SCT can convert to AWS Glue Studio

You can use AWS SCT to convert SSIS data flow components and parameters to AWS Glue Studio.

Supported data flow components include the following:

- ADO NET Destination
- ADO NET Source
- Aggregate
- Character Map
- Conditional Split
- Copy Column
- Data Conversion
- Derived Column
- Lookup
- Merge
- Merge Join
- Multicast
- ODBCDestination
- ODBCSource
- OLEDBDestination
- OLEDBSource
- Row Count
- Sort
- SQL Server Destination
- Union All

AWS SCT can convert more SSIS components to AWS Glue. For more information, see
[SSIS components that AWS SCT can convert to AWS Glue](CHAP-converting-aws-glue-ssis.md#CHAP-converting-aws-glue-ssis-supported-components "CHAP-converting-aws-glue-ssis.md#CHAP-converting-aws-glue-ssis-supported-components").
