

# Creating a data lake from an AWS CloudTrail source
<a name="getting-started-cloudtrail-tutorial"></a>

This tutorial guides you through the actions to take on the Lake Formation console to create and load your first data lake from an AWS CloudTrail source.

**High-level steps for creating a data lake**

1. Register an Amazon Simple Storage Service (Amazon S3) path as a data lake.

1. Grant Lake Formation permissions to write to the Data Catalog and to Amazon S3 locations in the data lake.

1. Create a database to organize the metadata tables in the Data Catalog.

1. Use a blueprint to create a workflow. Run the workflow to ingest data from a data source.

1. Set up your Lake Formation permissions to allow others to manage data in the Data Catalog and the data lake.

1. Set up Amazon Athena to query the data that you imported into your Amazon S3 data lake.

1. For some data store types, set up Amazon Redshift Spectrum to query the data that you imported into your Amazon S3 data lake.

**Topics**
+ [Intended audience](#cloudtrail-tut-personas)
+ [Prerequisites](#cloudtrail-tut-prereqs)
+ [Step 1: Create a data analyst user](#cloudtrail-tut-create-lf-user)
+ [Step 2: Add permissions to read AWS CloudTrail logs to the workflow role](#cloudtrail-tut-grant-cloudtrail)
+ [Step 3: Create an Amazon S3 bucket for the data lake](#cloudtrail-tut-create-bucket)
+ [Step 4: Register an Amazon S3 path](#cloudtrail-tut-register)
+ [Step 5: Grant data location permissions](#cloudtrail-tut-data-location)
+ [Step 6: Create a database in the Data Catalog](#cloudtrail-tut-create-db)
+ [Step 7: Grant data permissions](#cloudtrail-tut-data-permissions)
+ [Step 8: Use a blueprint to create a workflow](#cloudtrail-tut-create-workflow)
+ [Step 9: Run the workflow](#cloudtrail-tut-run-workflow)
+ [Step 10: Grant SELECT on the tables](#cloudtrail-tut-grant-table)
+ [Step 11: Query the data lake Using Amazon Athena](#cloudtrail-tut-query)

## Intended audience
<a name="cloudtrail-tut-personas"></a>

The following table lists the roles used in this tutorial to create a data lake.


**Intended audience**  

| Role | Description | 
| --- | --- | 
| IAM Administrator | Has the AWS managed policy: AdministratorAccess. Can create IAM roles and Amazon S3 buckets. | 
| Data lake administrator | User who can access the data catalog, create databases, and grant Lake Formation permissions to other users. Has fewer IAM permissions than the IAM administrator, but enough to administer the data lake. | 
| Data analyst | User who can run queries against the data lake. Has only enough permissions to run queries. | 
| Workflow role | Role with the required IAM policies to run a workflow. For more information, see [(Optional) Create an IAM role for workflows](initial-lf-config.md#iam-create-blueprint-role). | 

## Prerequisites
<a name="cloudtrail-tut-prereqs"></a>

Before you begin:
+ Ensure that you have completed the tasks in [Set up AWS Lake Formation](initial-lf-config.md).
+ Know the location of your CloudTrail logs.
+ Athena requires the data analyst persona to create an Amazon S3 bucket to store query results before using Athena.

Familiarity with AWS Identity and Access Management (IAM) is assumed. For information about IAM, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

## Step 1: Create a data analyst user
<a name="cloudtrail-tut-create-lf-user"></a>

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

## Step 2: Add permissions to read AWS CloudTrail logs to the workflow role
<a name="cloudtrail-tut-grant-cloudtrail"></a>

1. Attach the following inline policy to the role `LakeFormationWorkflowRole`. The policy grants permission to read your AWS CloudTrail logs. Name the policy `DatalakeGetCloudTrail`.

   To create the `LakeFormationWorkflowRole` role, see [(Optional) Create an IAM role for workflows](initial-lf-config.md#iam-create-blueprint-role).
**Important**  
Replace {{<your-s3-cloudtrail-bucket>}} with the Amazon S3 location of your CloudTrail data.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "s3:GetObject",
               "Resource": ["arn:aws:s3:::{{<your-s3-cloudtrail-bucket>}}/*"]
           }
       ]
   }
   ```

------

1. Verify that there are three policies attached to the role.

## Step 3: Create an Amazon S3 bucket for the data lake
<a name="cloudtrail-tut-create-bucket"></a>

Create the Amazon S3 bucket that is to be the root location of your data lake.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/) and sign in as a user with administrative access.

1. Choose **Create bucket**, and go through the wizard to create a bucket named `{{<yourName>}}-datalake-cloudtrail`, where {{<yourName>}} is your first initial and last name. For example: `jdoe-datalake-cloudtrail`.

   For detailed instructions on creating an Amazon S3 bucket, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html).

## Step 4: Register an Amazon S3 path
<a name="cloudtrail-tut-register"></a>

Register an Amazon S3 path as the root location of your data lake.

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/). Sign in as the data lake administrator.

1. In the navigation pane, under **Register and ingest**, choose **Data lake locations**.

1. Choose **Register location** and then **Browse**. 

1. Select the `{{<yourName>}}-datalake-cloudtrail` bucket that you created previously, accept the default IAM role `AWSServiceRoleForLakeFormationDataAccess`, and then choose **Register location**.

   For more information about registering locations, see [Adding an Amazon S3 location to your data lake](register-data-lake.md).

## Step 5: Grant data location permissions
<a name="cloudtrail-tut-data-location"></a>

Principals must have *data location permissions* on a data lake location to create Data Catalog tables or databases that point to that location. You must grant data location permissions to the IAM role for workflows so that the workflow can write to the data ingestion destination.

1. In the navigation pane, under **Permissions**, choose **Data locations**.

1. Choose **Grant**, and in the **Grant permissions** dialog box, make these selections:

   1. For **IAM user and roles**, choose `LakeFormationWorkflowRole`.

   1. For **Storage locations**, choose your `{{<yourName>}}-datalake-cloudtrail` bucket.

1. Choose **Grant**.

For more information about data location permissions, see [Underlying data access control](access-control-underlying-data.md#data-location-permissions).

## Step 6: Create a database in the Data Catalog
<a name="cloudtrail-tut-create-db"></a>

Metadata tables in the Lake Formation Data Catalog are stored within a database.

1. In the navigation pane, under **Data catalog**, choose **Databases**.

1. Choose **Create database**, and under **Database details**, enter the name `lakeformation_cloudtrail`.

1. Leave the other fields blank, and choose **Create database**.

## Step 7: Grant data permissions
<a name="cloudtrail-tut-data-permissions"></a>

You must grant permissions to create metadata tables in the Data Catalog. Because the workflow will run with the role `LakeFormationWorkflowRole`, you must grant these permissions to the role.

1. In the Lake Formation console, in the navigation pane, under **Data catalog**, choose **Databases**. 

1. Choose the `lakeformation_cloudtrail` database, then, from the **Actions** drop-down list, choose **Grant** under the heading Permissions.

1. In the **Grant data permissions** dialog box, make these selections:

   1. Under **Principals**, for **IAM user and roles**, choose `LakeFormationWorkflowRole`.

   1. Under **LF-Tags or catalog resources**, choose **Named Data Catalog resources**.

   1. For **Databases**, you should see that the `lakeformation_cloudtrail` database is already added.

   1. Under **Database permissions**, select **Create table**, **Alter**, and **Drop**, and clear **Super** if it is selected.

1. Choose **Grant**.

For more information about granting Lake Formation permissions, see [Managing Lake Formation permissions](managing-permissions.md).

## Step 8: Use a blueprint to create a workflow
<a name="cloudtrail-tut-create-workflow"></a>

In order to read the CloudTrail logs, understand their structure, create the appropriate tables in the Data Catalog, we need to set up a workflow that consists of a AWS Glue crawlers, jobs, triggers, and workflows. Lake Formation's blueprints simplifies this process. 

The workflow generates the jobs, crawlers, and triggers that discover and ingest data into your data lake. You create a workflow based on one of the predefined Lake Formation blueprints.

1. In the Lake Formation console, in the navigation pane, choose **Blueprints** under **Ingestion**, and then choose **Use blueprint**.

1. On the **Use a blueprint** page, under **Blueprint type**, choose **AWS CloudTrail**.

1. Under **Import source**, choose a CloudTrail source and start date.

1. Under **Import target**, specify these parameters:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-cloudtrail-tutorial.html)

1. For import frequency, choose **Run on demand**.

1. Under **Import options**, specify these parameters:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-cloudtrail-tutorial.html)

1. Choose **Create**, and wait for the console to report that the workflow was successfully created.
**Tip**  
Did you get the following error message?  
`User: arn:aws:iam::{{<account-id>}}:user/{{<datalake_administrator_user>}} is not authorized to perform: iam:PassRole on resource:arn:aws:iam::{{<account-id>}}:role/LakeFormationWorkflowRole...`  
If so, check that you replaced {{<account-id>}} in the inline policy for the data lake administrator user with a valid AWS account number.

## Step 9: Run the workflow
<a name="cloudtrail-tut-run-workflow"></a>

Because you specified that the workflow is run-on-demand, you must manually start the workflow.
+ On the **Blueprints** page, select the workflow `lakeformationcloudtrailtest`, and on the **Actions** menu, choose **Start**.

  As the workflow runs, you can view its progress in the **Last run status** column. Choose the refresh button occasionally.

  The status goes from **RUNNING**, to **Discovering**, to **Importing**, to **COMPLETED**. 

  When the workflow completes:
  + The Data Catalog will have new metadata tables.
  + Your CloudTrail logs will be ingested into the data lake.

  If the workflow fails, do the following:

  1. Select the workflow, and on the **Actions** menu, choose **View graph**.

     The workflow opens in the AWS Glue console.

  1. Ensure that the workflow is selected, and choose the **History** tab.

  1. Under **History**, select the most recent run and choose **View run details**.

  1. Select a failed job or crawler in the dynamic (runtime) graph, and review the error message. Failed nodes are either red or yellow.

## Step 10: Grant SELECT on the tables
<a name="cloudtrail-tut-grant-table"></a>

You must grant the `SELECT` permission on the new Data Catalog tables so that the data analyst can query the data that the tables point to.

**Note**  
A workflow automatically grants the `SELECT` permission on the tables that it creates to the user who ran it. Because the data lake administrator ran this workflow, you must grant `SELECT` to the data analyst.

1. In the Lake Formation console, in the navigation pane, under **Data catalog**, choose **Databases**. 

1. Choose the `lakeformation_cloudtrail` database, then, from the **Actions** drop-down list, choose **Grant** under the heading Permissions.

1. In the **Grant data permissions** dialog box, make these selections:

   1. Under **Principals**, for **IAM user and roles**, choose `datalake_user`.

   1. Under **LF-Tags or catalog resources**, choose **Named data catalog resources**.

   1. For **Databases**, the `lakeformation_cloudtrail` database should already be selected.

   1. For **Tables**, choose `cloudtrailtest-cloudtrail`.

   1. Under **Table and column permissions**, choose **Select**.

1. Choose **Grant**.

**The next step is performed as the data analyst.**

## Step 11: Query the data lake Using Amazon Athena
<a name="cloudtrail-tut-query"></a>

Use the Amazon Athena console to query the CloudTrail data in your data lake.

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home) and sign in as the data analyst, user `datalake_user`.

1. If necessary, choose **Get Started** to continue to the Athena query editor.

1. For **Data source**, choose **AwsDataCatalog**.

1. For **Database**, choose `lakeformation_cloudtrail`.

   The **Tables** list populates.

1. On the overflow menu (3 dots arranged horizontally) beside the table `cloudtrailtest-cloudtrail`, choose **Preview table**, then choose **Run**.

   The query runs and displays 10 rows of data.

   If you have not used Athena before, you must first configure an Amazon S3 location in the Athena console for storing the query results. The `datalake_user` must have the necessary permissions to access the Amazon S3 bucket that you choose.

**Note**  
Now that you have completed the tutorial, grant data permissions and data location permissions to the principals in your organization.