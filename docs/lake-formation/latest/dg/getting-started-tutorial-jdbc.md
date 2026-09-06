

# Creating a data lake from a JDBC source in Lake Formation
<a name="getting-started-tutorial-jdbc"></a>

This tutorial guides you through the steps to take on the AWS Lake Formation console to create and load your first data lake from a JDBC source using Lake Formation. 

**Topics**
+ [Intended audience](#tut-personas)
+ [JDBC tutorial prerequisites](#tut-prereqs)
+ [Step 1: Create a data analyst user](#tut-create-lf-user)
+ [Step 2: Create a connection in AWS Glue](#tut-connection)
+ [Step 3: Create an Amazon S3 bucket for the data lake](#tut-create-bucket)
+ [Step 4: Register an Amazon S3 path](#tut-register)
+ [Step 5: Grant data location permissions](#tut-data-location)
+ [Step 6: Create a database in the Data Catalog](#tut-create-db)
+ [Step 7: Grant data permissions](#tut-grant-data-permissions)
+ [Step 8: Use a blueprint to create a workflow](#tut-create-workflow)
+ [Step 9: Run the workflow](#tut-run-workflow)
+ [Step 10: Grant SELECT on the tables](#tut-grant-select)
+ [Step 11: Query the data lake using Amazon Athena](#tut-query-athena)
+ [Step 12: Query the data in the data lake using Amazon Redshift Spectrum](#tut-query-redshift)
+ [Step 13: Grant or revoke Lake Formation permissions using Amazon Redshift Spectrum](#getting-started-tutorial-grant-revoke-redshift)

## Intended audience
<a name="tut-personas"></a>

The following table lists the roles that are used in this [AWS Lake Formation JDBC tutorial](#getting-started-tutorial-jdbc).


| Role | Description | 
| --- | --- | 
| IAM administrator | A user who can create AWS Identity and Access Management (IAM) users and roles and Amazon Simple Storage Service (Amazon S3) buckets. Has the AdministratorAccess AWS managed policy. | 
| Data lake administrator | A user who can access the Data Catalog, create databases, and grant Lake Formation permissions to other users. Has fewer IAM permissions than the IAM administrator, but enough to administer the data lake. | 
| Data analyst | A user who can run queries against the data lake. Has only enough permissions to run queries. | 
| Workflow role | A role with the required IAM policies to run a workflow. | 

For information about prerequisites for completing the tutorial, see [JDBC tutorial prerequisites](#tut-prereqs).

## JDBC tutorial prerequisites
<a name="tut-prereqs"></a>

Before you begin the [AWS Lake Formation JDBC tutorial](#getting-started-tutorial-jdbc), ensure that you've done the following:
+ Complete the tasks in [Getting started with Lake Formation](getting-started-setup.md).
+ Decide on a JDBC-accessible data store that you want to use for the tutorial.
+ Gather the information that is required to create an AWS Glue connection of type JDBC. This Data Catalog object includes the URL to the data store, login credentials, and if the data store was created in an Amazon Virtual Private Cloud (Amazon VPC), additional VPC-specific configuration information. For more information, see [ Defining Connections in the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-add-connection.html) in the *AWS Glue Developer Guide*.

The tutorial assumes that you are familiar with AWS Identity and Access Management (IAM). For information about IAM, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

To get started, proceed to [Step 1: Create a data analyst user](#tut-create-lf-user).

## Step 1: Create a data analyst user
<a name="tut-create-lf-user"></a>

In this step, you create an AWS Identity and Access Management (IAM) user to be the data analyst for your data lake in AWS Lake Formation.

This user has the minimum set of permissions to query the data lake.

1. Open the IAM console at [https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam). Sign in as a user with the `AdministratorAccess` AWS managed policy.

1. Create a user named `datalake_user` with the following settings:
   + Enable AWS Management Console access.
   + Set a password and do not require password reset.
   + Attach the `AmazonAthenaFullAccess` AWS managed policy.
   + Attach the following inline policy. Name the policy `DatalakeUserBasic`.

     ```
     {
         "Version": "2012-10-17",		 	 	 
         "Statement": [
             {
                 "Effect": "Allow",
                 "Action": [
                     "lakeformation:GetDataAccess",
                     "glue:GetTable",
                     "glue:GetTables",
                     "glue:SearchTables",
                     "glue:GetDatabase",
                     "glue:GetDatabases",
                     "glue:GetPartitions",
                     "lakeformation:GetResourceLFTags",
                     "lakeformation:ListLFTags",
                     "lakeformation:GetLFTag",
                     "lakeformation:SearchTablesByLFTags",
                     "lakeformation:SearchDatabasesByLFTags"                
                ],
                 "Resource": "*"
             }
         ]
     }
     ```

## Step 2: Create a connection in AWS Glue
<a name="tut-connection"></a>

**Note**  
Skip this step if you already have an AWS Glue connection to your JDBC data source.

AWS Lake Formation accesses JDBC data sources through an AWS Glue *connection*. A connection is a Data Catalog object that contains all the information required to connect to the data source. You can create a connection using the AWS Glue console.

**To create a connection**

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/), and sign in as a user with administrative access.

1. In the navigation pane, under **Data catalog**, choose **Connections**.

1. On the **Connectors** page, choose **Create connection**.

1. On the **Choose data source** page, choose **JDBC** as the connection type. Then choose **Next**.

1. Continue through the connection wizard and save the connection.

   For information on creating a connection, see [AWS Glue JDBC connection properties](https://docs.aws.amazon.com/glue/latest/dg/connection-properties.html#connection-properties-jdbc) in the *AWS Glue Developer Guide*.

## Step 3: Create an Amazon S3 bucket for the data lake
<a name="tut-create-bucket"></a>

In this step, you create the Amazon Simple Storage Service (Amazon S3) bucket that is to be the root location of your data lake.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/) and sign in as a user with administrative access.

1. Choose **Create bucket**, and go through the wizard to create a bucket named `{{<yourName>}}-datalake-tutorial`, where {{<yourName>}} is your first initial and last name. For example: `jdoe-datalake-tutorial`.

   For detailed instructions on creating an Amazon S3 bucket, see [How Do I Create an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html) in the *Amazon Simple Storage Service User Guide*.

## Step 4: Register an Amazon S3 path
<a name="tut-register"></a>

In this step, you register an Amazon Simple Storage Service (Amazon S3) path as the root location of your data lake.

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/). Sign in as the data lake administrator.

1. In the navigation pane, under **Administration**, choose **Data lake locations**.

1. Choose **Register location**, and then choose **Browse**. 

1. Select the `{{<yourName>}}-datalake-tutorial` bucket that you created previously, accept the default IAM role `AWSServiceRoleForLakeFormationDataAccess`, and then choose **Register location**.

   For more information about registering locations, see [Adding an Amazon S3 location to your data lake](register-data-lake.md).

## Step 5: Grant data location permissions
<a name="tut-data-location"></a>

Principals must have *data location permissions* on a data lake location to create Data Catalog tables or databases that point to that location. You must grant data location permissions to the IAM role for workflows so that the workflow can write to the data ingestion destination.

1. On the Lake Formation console, in the navigation pane, under **Permissions**, choose **Data locations**.

1. Choose **Grant**, and in the **Grant permissions** dialog box, do the following:

   1. For **IAM user and roles**, choose `LakeFormationWorkflowRole`.

   1. For **Storage locations**, choose your `{{<yourName>}}-datalake-tutorial` bucket.

1. Choose **Grant**.

For more information about data location permissions, see [Underlying data access control](access-control-underlying-data.md#data-location-permissions).

## Step 6: Create a database in the Data Catalog
<a name="tut-create-db"></a>

Metadata tables in the Lake Formation Data Catalog are stored within a database.

1. On the Lake Formation console, in the navigation pane, under **Data catalog**, choose **Databases**.

1. Choose **Create database**, and under **Database details**, enter the name `lakeformation_tutorial`.

1. Leave the other fields blank, and choose **Create database**.

## Step 7: Grant data permissions
<a name="tut-grant-data-permissions"></a>

You must grant permissions to create metadata tables in the Data Catalog. Because the workflow runs with the role `LakeFormationWorkflowRole`, you must grant these permissions to the role.

1. On the Lake Formation console, in the navigation pane, under **Permissions**, choose **Data lake permissions**.

1. Choose **Grant**, and in the **Grant data permissions** dialog box, do the following:

   1. Under **Principals**, for **IAM user and roles**, choose `LakeFormationWorkflowRole`.

   1. Under **LF-Tags or catalog resources**, choose **Named data catalog resources**.

   1. For **Databases**, choose the database that you created previously, `lakeformation_tutorial`.

   1. Under **Database permissions**, select **Create table**, **Alter**, and **Drop**, and clear **Super** if it is selected.

1. Choose **Grant**.

For more information about granting Lake Formation permissions, see [Overview of Lake Formation permissions](lf-permissions-overview.md).

## Step 8: Use a blueprint to create a workflow
<a name="tut-create-workflow"></a>

The AWS Lake Formation workflow generates the AWS Glue jobs, crawlers, and triggers that discover and ingest data into your data lake. You create a workflow based on one of the predefined Lake Formation blueprints.

1. On the Lake Formation console, in the navigation pane, choose **Blueprints**, and then choose **Use blueprint**.

1. On the **Use a blueprint** page, under **Blueprint type**, choose **Database snapshot**.

1. Under **Import source**, for **Database connection**, choose the connection that you just created, `datalake-tutorial`, or choose an existing connection for your data source.

1. For **Source data path**, enter the path from which to ingest data, in the form `{{<database>}}/{{<schema>}}/{{<table>}}`.

   You can substitute the percent (%) wildcard for schema or table. For databases that support schemas, enter {{<database>}}/{{<schema>}}/% to match all tables in {{<schema>}} within {{<database>}}. Oracle Database and MySQL don’t support schema in the path; instead, enter {{<database>}}/%. For Oracle Database, {{<database>}} is the system identifier (SID).

   For example, if an Oracle database has `orcl` as its SID, enter `orcl/%` to match all tables that the user specified in the JDCB connection has access to.
**Important**  
This field is case-sensitive.

1. Under **Import target**, specify these parameters:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-tutorial-jdbc.html)

1. For import frequency, choose **Run on demand**.

1. Under **Import options**, specify these parameters:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-tutorial-jdbc.html)

1. Choose **Create**, and wait for the console to report that the workflow was successfully created.
**Tip**  
Did you get the following error message?  
`User: arn:aws:iam::{{<account-id>}}:user/{{<datalake_administrator_user>}} is not authorized to perform: iam:PassRole on resource:arn:aws:iam::{{<account-id>}}:role/LakeFormationWorkflowRole...`  
If so, check that you replaced {{<account-id>}} in the inline policy for the data lake administrator user with a valid AWS account number.

## Step 9: Run the workflow
<a name="tut-run-workflow"></a>

Because you specified that the workflow is run-on-demand, you must manually start the workflow in AWS Lake Formation.

1. On the Lake Formation console, on the **Blueprints** page, select the workflow `lakeformationjdbctest`.

1. Choose **Actions**, and then choose **Start**.

1. As the workflow runs, view its progress in the **Last run status** column. Choose the refresh button occasionally.

   The status goes from **RUNNING**, to **Discovering**, to **Importing**, to **COMPLETED**. 

   When the workflow is complete:
   + The Data Catalog has new metadata tables.
   + Your data is ingested into the data lake.

   If the workflow fails, do the following:

   1. Select the workflow. Choose **Actions**, and then choose **View graph**.

      The workflow opens in the AWS Glue console.

   1. Select the workflow and choose the **History** tab.

   1. Select the most recent run and choose **View run details**.

   1. Select a failed job or crawler in the dynamic (runtime) graph, and review the error message. Failed nodes are either red or yellow.

## Step 10: Grant SELECT on the tables
<a name="tut-grant-select"></a>

You must grant the `SELECT` permission on the new Data Catalog tables in AWS Lake Formation so that the data analyst can query the data that the tables point to.

**Note**  
A workflow automatically grants the `SELECT` permission on the tables that it creates to the user who ran it. Because the data lake administrator ran this workflow, you must grant `SELECT` to the data analyst.

1. On the Lake Formation console, in the navigation pane, under **Permissions**, choose **Data lake permissions**.

1. Choose **Grant**, and in the **Grant data permissions** dialog box, do the following:

   1. Under **Principals**, for **IAM user and roles**, choose `datalake_user`.

   1. Under **LF-Tags or catalog resources**, choose **Named data catalog resources**.

   1. For **Databases**, choose `lakeformation_tutorial`.

      The **Tables** list populates.

   1. For **Tables**, choose one or more tables from your data source.

   1. Under **Table and column permissions**, choose **Select**.

1. Choose **Grant**.

**The next step is performed as the data analyst.** 

## Step 11: Query the data lake using Amazon Athena
<a name="tut-query-athena"></a>

Use the Amazon Athena console to query the data in your data lake.

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home), and sign in as the data analyst, user `datalake_user`.

1. If necessary, choose **Get Started** to continue to the Athena query editor.

1. For **Data source**, choose **AwsDataCatalog**.

1. For **Database**, choose `lakeformation_tutorial`.

   The **Tables** list populates.

1. In the pop-up menu beside one of the tables, choose **Preview table**.

   The query runs and displays 10 rows of data.

## Step 12: Query the data in the data lake using Amazon Redshift Spectrum
<a name="tut-query-redshift"></a>

You can set up Amazon Redshift Spectrum to query the data that you imported into your Amazon Simple Storage Service (Amazon S3) data lake. First, create an AWS Identity and Access Management (IAM) role that is used to launch the Amazon Redshift cluster and to query the Amazon S3 data. Then, grant this role the `Select` permissions on the tables that you want to query. Then, grant the user permissions to use the Amazon Redshift query editor. Finally, create an Amazon Redshift cluster and run queries.

You create the cluster as an administrator, and query the cluster as a data analyst.

For more information about Amazon Redshift Spectrum, see [Using Amazon Redshift Spectrum to Query External Data](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) in the *Amazon Redshift Database Developer Guide*.

**To set up permissions to run Amazon Redshift queries**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). Sign in as a user with the `AdministratorAccess` AWS managed policy.

1. In the navigation pane, choose **Policies**.

   If this is your first time choosing **Policies**, the **Welcome to Managed Policies** page appears. Choose **Get Started**.

1. Choose **Create policy**. 

1. Choose the **JSON** tab.

1. Paste in the following JSON policy document.

   ```
   {
       "Version": "2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "lakeformation:GetDataAccess",
                   "glue:GetTable",
                   "glue:GetTables",
                   "glue:SearchTables",
                   "glue:GetDatabase",
                   "glue:GetDatabases",
                   "glue:GetPartitions",
                   "lakeformation:GetResourceLFTags",
                   "lakeformation:ListLFTags",
                   "lakeformation:GetLFTag",
                   "lakeformation:SearchTablesByLFTags",
                   "lakeformation:SearchDatabasesByLFTags"                
              ],
               "Resource": "*"
           }
       ]
   }
   ```

1. When you are finished, choose **Review** to review the policy. The policy validator reports any syntax errors.

1. On the **Review policy** page, enter the **Name** as **RedshiftLakeFormationPolicy** for the policy that you are creating. Enter a **Description** (optional). Review the policy **Summary** to see the permissions that are granted by your policy. Then choose **Create policy** to save your work. 

1. In the navigation pane of the IAM console, choose **Roles**, and then choose **Create role**.

1. For **Select trusted entity**, choose **AWS service**.

1. Choose the Amazon Redshift service to assume this role.

1. Choose the **Redshift Customizable** use case for your service. Then choose **Next: Permissions**.

1. Search for the permissions policy that you created, `RedshiftLakeFormationPolicy`, and select the check box next to the policy name in the list.

1. Choose **Next: Tags**.

1. Choose **Next: Review**. 

1. For **Role name**, enter the name **RedshiftLakeFormationRole**. 

1. (Optional) For **Role description**, enter a description for the new role.

1. Review the role, and then choose **Create role**.

**To grant `Select` permissions on the table to be queried in the Lake Formation database**

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/). Sign in as the data lake administrator.

1. In the navigation pane, under **Permissions**, choose **Data lake permissions**, and then choose **Grant**.

1. Provide the following information:
   + For **IAM users and roles**, choose the IAM role you created, `RedshiftLakeFormationRole`. When you run the Amazon Redshift Query Editor, it uses this IAM role for permission to the data. 
   + For **Database**, choose `lakeformation_tutorial`.

     The tables list populates.
   + For **Table**, choose a table within the data source to query.
   + Choose the **Select** table permission.

1. Choose **Grant**.

**To set up Amazon Redshift Spectrum and run queries**

1. Open the Amazon Redshift console at [https://console.aws.amazon.com/redshift](https://console.aws.amazon.com/redshift). Sign in as the user `Administrator`.

1. Choose **Create cluster**.

1. On the **Create cluster** page, enter `redshift-lakeformation-demo` for the **Cluster identifier**.

1. For the **Node type**, select **dc2.large**.

1. Scroll down, and under **Database configurations**, enter or accept these parameters:
   + **Admin user name**: `awsuser`
   + **Admin user password**: `({{Choose a password}})`

1. Expand **Cluster permissions**, and for **Available IAM roles**, choose **RedshiftLakeFormationRole**. Then choose **Add IAM role**.

1. If you must use a different port than the default value of 5439, next to **Additional configurations**, turn off the **Use defaults** option. Expand the section for **Database configurations**, and enter a new **Database port** number.

1. Choose **Create cluster**.

   The **Clusters** page loads.

1. Wait until the cluster status becomes **Available**. Choose the refresh icon periodically.

1. Grant the data analyst permission to run queries against the cluster. To do so, complete the following steps.

   1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/), and sign in as the `Administrator` user.

   1. In the navigation pane, choose **Users**, and attach the following managed policies to the user `datalake_user`.
      + `AmazonRedshiftQueryEditor`
      + `AmazonRedshiftReadOnlyAccess` 

1. Sign out of the Amazon Redshift console and sign back in as user `datalake_user`.

1. In the left vertical toolbar, choose the **EDITOR** icon to open the query editor and connect to the cluster. If the **Connect to database** dialog box appears, choose the cluster name `redshift-lakeformation-demo`, and enter the database name **dev**, the user name **awsuser**, and the password that you created. Then choose **Connect to database**.
**Note**  
If you are not prompted for connection parameters and another cluster is already selected in the query editor, choose **Change Connection** to open the **Connect to database** dialog box.

1. In the ** New Query 1** text box, enter and run the following statement to map the database `lakeformation_tutorial` in Lake Formation to the Amazon Redshift schema name `redshift_jdbc`:
**Important**  
Replace {{<account-id>}} with a valid AWS account number, and {{<region>}} with a valid AWS Region name (for example, `us-east-1`).

   ```
   create external schema if not exists redshift_jdbc from DATA CATALOG database 'lakeformation_tutorial' iam_role 'arn:aws:iam::{{<account-id>}}:role/RedshiftLakeFormationRole' region '{{<region>}}';
   ```

1. In the schema list under **Select schema**, choose **redshift\_jdbc**.

   The tables list populates. The query editor shows only the tables on which you were granted Lake Formation data lake permissions.

1. On the pop-up menu next to a table name, choose **Preview data**.

   Amazon Redshift returns the first 10 rows.

   You can now run queries against the tables and columns for which you have permissions.

## Step 13: Grant or revoke Lake Formation permissions using Amazon Redshift Spectrum
<a name="getting-started-tutorial-grant-revoke-redshift"></a>

Amazon Redshift supports the ability to grant and revoke Lake Formation permissions on databases and tables using modified SQL statements. These statements are similar to the existing Amazon Redshift statements. For more information, see [GRANT](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT.html) and [REVOKE](https://docs.aws.amazon.com/redshift/latest/dg/r_REVOKE.html) in the *Amazon Redshift Database Developer Guide*. 