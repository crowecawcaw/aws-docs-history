

# Setting up permissions for open table storage formats in Lake Formation
<a name="otf-tutorial"></a>

AWS Lake Formation supports managing access permissions for *Open Table Formats* (OTFs) such as [Apache Iceberg](https://iceberg.apache.org/), [Apache Hudi](https://hudi.incubator.apache.org/), and [Linux foundation Delta Lake](https://delta.io/). In this tutorial, you'll learn how to create Iceberg, Hudi, and Delta Lake with symlink [manifest](https://docs.delta.io/latest/presto-integration.html) tables in the AWS Glue Data Catalog using AWS Glue, set up fine-grained permissions using Lake Formation, and query data using Amazon Athena.

**Note**  
AWS analytics services don't support all transactional table formats. For more information, see [Working with other AWS services](working-with-services.md). This tutorial manually covers creating a new database and a table in the Data Catalog using AWS Glue jobs only.

This tutorial includes an AWS CloudFormation template for quick setup. You can review and customize it to suit your needs.

**Topics**
+ [Intended audience](#tut-otf-roles)
+ [Prerequisites](#tut-otf-prereqs)
+ [Step 1: Provision your resources](#set-up-otf-resources)
+ [Step 2: Set up permissions for an Iceberg table](#set-up-iceberg-table)
+ [Step 3: Set up permissions for a Hudi table](#set-up-hudi-table)
+ [Step 4: Set up permissions for a Delta Lake table](#set-up-delta-table)
+ [Step 5: Clean up AWS resources](#otf-tut-clean-up)

## Intended audience
<a name="tut-otf-roles"></a>

This tutorial is intended for IAM administrators, data lake administrators, and business analysts. The following table lists the roles used in this tutorial for creating a governed table using Lake Formation.


| Role | Description | 
| --- | --- | 
| IAM Administrator | A user who can create IAM users and roles and Amazon S3 buckets. Has the AdministratorAccess AWS managed policy. | 
| Data lake administrator | A user who can access the Data Catalog, create databases, and grant Lake Formation permissions to other users. Has fewer IAM permissions than the IAM administrator, but enough to administer the data lake. | 
| Business analyst | A user who can run queries against the data lake. Has permissions to run queries. | 

## Prerequisites
<a name="tut-otf-prereqs"></a>

Before you start this tutorial, you must have an AWS account that you can sign in as a user with the correct permissions. For more information, see [Sign up for an AWS account](getting-started-setup.md#sign-up-for-aws).

The tutorial assumes that you are familiar with IAM roles and policies. For information about IAM, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

 You need to set up the following AWS resources to complete this tutorial:
+ Data lake administrator user
+ Lake Formation data lake settings
+ Amazon Athena engine version 3

**To create a data lake administrator**

1. Sign in to the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/) as an administrator user. You will create resources in the US East (N. Virginia) Region for this tutorial.

1. On the Lake Formation console, in the navigation pane, under **Permissions**, choose **Administrative roles and tasks**.

1. Select **Choose Administrators** under **Data lake administrators**.

1.  In the pop-up window, **Manage data lake administrators**, under **IAM users and roles**, choose **IAM admin user**.

1. Choose **Save**.

**To enable data lake settings**

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/). In the navigation pane, under **Data catalog**, choose **Settings**. Uncheck the following:
   + Use only IAM access control for new databases.
   + Use only IAM access control for new tables in new databases.

1. Under **Cross account version settings**, choose **Version 3** as the cross account version. 

1. Choose **Save**.

**To upgrade Amazon Athena engine to version 3**

1. Open Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. Select the **Workgroup** and select primary workgroup.

1. Ensure that the workgroup is at a minimum version of 3. If it is not, edit the workgroup, choose **Manual** for **Upgrade query engine**, and select version 3.

1. Choose **Save changes**.

## Step 1: Provision your resources
<a name="set-up-otf-resources"></a>

This section shows you how to set up the AWS resources using an CloudFormation template.

**To create your resources using CloudFormation template**

1. Sign into the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/) as an IAM administrator in the US East (N. Virginia) Region.

1. Choose [Launch Stack](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https://lf-public.s3.amazonaws.com/cfn/lfotfsetup.template).

1. Choose **Next** on the **Create stack** screen.

1. Enter a **Stack name**.

1. Choose **Next**.

1. On the next page, choose **Next**.

1. Review the details on the final page and select **I acknowledge that AWS CloudFormation might create IAM resources.**

1. Choose **Create**.

   The stack creation can take up to two minutes.

Launching the cloud formation stack creates the following resources:
+ lf-otf-datalake-123456789012 – Amazon S3 bucket to store data
**Note**  
The account id appended to the Amazon S3 bucket name is replaced with your account id.
+ lf-otf-tutorial-123456789012 – Amazon S3 bucket to store query results and AWS Glue job scripts
+ lficebergdb – AWS Glue Iceberg database
+ lfhudidb – AWS Glue Hudi database
+ lfdeltadb – AWS Glue Delta database
+ native-iceberg-create – AWS Glue job that creates an Iceberg table in the Data Catalog
+ native-hudi-create – AWS Glue job that creates a Hudi table in the Data Catalog
+ native-delta-create – AWS Glue job that creates a Delta table in the Data Catalog
+ LF-OTF-GlueServiceRole – IAM role that you pass to AWS Glue to run the jobs. This role has the required policies attached to access the resources like Data Catalog, Amazon S3 bucket etc.
+ LF-OTF-RegisterRole – IAM role to register the Amazon S3 location with Lake Formation. This role has `LF-Data-Lake-Storage-Policy` attached to the role.
+ lf-consumer-analystuser – IAM user to query the data using Athena
+ lf-consumer-analystuser-credentials – Password for the data analyst user stored in AWS Secrets Manager

After the stack creations is complete, navigate to the output tab and note down the values for:
+ AthenaQueryResultLocation – Amazon S3 location for Athena query output
+ BusinessAnalystUserCredentials – Password for the data analyst user

  To retrieve the password value:

  1. Choose the `lf-consumer-analystuser-credentials` value by navigating to the Secrets Manager console.

  1. In the **Secret value** section, choose **Retrieve secret value**.

  1. Note down the secret value for the password.

## Step 2: Set up permissions for an Iceberg table
<a name="set-up-iceberg-table"></a>

In this section, you'll learn how to create an Iceberg table in the AWS Glue Data Catalog, set up data permissions in AWS Lake Formation, and query data using Amazon Athena.

**To create an Iceberg table**

In this step, you’ll run an AWS Glue job that creates an Iceberg transactional table in the Data Catalog.

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/) in the US East (N. Virginia) Region as the data lake administrator user.

1. Choose **jobs** from the left navigation pane.

1. Select `native-iceberg-create`.  
![The image is a screenshot of the AWS Glue job page in the console.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/otf-glu-job-tut.png)

1. Under **Actions**, choose **Edit job**.

1. Under **Job details**, expand **Advanced properties**, and check the box next to **Use AWS Glue Data Catalog as the Hive metastore** to add the table metadata in the AWS Glue Data Catalog. This specifies AWS Glue Data Catalog as the metastore for the Data Catalog resources used in the job and enables Lake Formation permissions to be applied later on the catalog resources.

1. Choose **Save**.

1. Choose **Run**. You can view the status of the job while it is running. 

   For more information on AWS Glue jobs, see [Working with jobs on the AWS Glue console](https://docs.aws.amazon.com/glue/latest/dg/console-jobs.html) in the *AWS Glue Developer Guide*.

    This job creates an Iceberg table named `product` in the `lficebergdb` database. Verify the product table in the Lake Formation console.

**To register the data location with Lake Formation**

Next, register the Amazon S3 path as the location of your data lake.

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/) as the data lake administrator user.

1. In the navigation pane, under **Register and ingest**, choose **Data location**.

1. Choose **Register location**.

1. On the **Register location** page, enter the following:
   +  **Amazon S3 path** – Choose **Browse** and select `lf-otf-datalake-123456789012`. Choose the expand arrow next to the Amazon S3 root location to navigate to the `s3/buckets/lf-otf-datalake-123456789012/transactionaldata/native-iceberg` location. 
   + **IAM role** – Choose `LF-OTF-RegisterRole` as the IAM role.
   + Choose **Register location**.  
![The image is a screenshot of the Lake Formation Register location page in the console.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/otf-register-location-tut.png)

   For more information on registering a data location with Lake Formation, see [Adding an Amazon S3 location to your data lake](register-data-lake.md).

**To grant Lake Formation permissions on the Iceberg table**

In this step, we'll grant data lake permissions to the business analyst user.

1. Under **Data lake permissions**, choose **Grant**.

1. On the **Grant data permissions** screen, choose, **IAM users and roles**.

1. Choose `lf-consumer-analystuser` from the drop down.  
![The image is a screenshot of the Lake Formation permissions page in the console.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/otf-lf-perm-role-tut.png)

1. Choose **Named data catalog resource**.

1. For **Databases** choose `lficebergdb`.

1. For **Tables**, choose `product`.  
![The image is a screenshot of the Lake Formation permissions page in the console.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/otf-db-tbl-perm-tut.png)

1. Next, you can grant column-based access by specifying columns.

   1. Under **Table permissions**, choose **Select**.

   1. Under **Data permissions**, choose **Column-based access**, choose **Include columns**.

   1. Choose `product_name`, `price`, and `category` columns.

   1. Choose **Grant**.  
![The image is a screenshot of the Lake Formation permissions page in the console.](http://docs.aws.amazon.com/lake-formation/latest/dg/images/otf-column-perm-tut.png)

**To query the Iceberg table using Athena**

 Now you can start querying the Iceberg table you created using Athena. If it is your first time running queries in Athena, you need to configure a query result location. For more information, see [Specifying a query result location](https://docs.aws.amazon.com/athena/latest/ug/querying.html#query-results-specify-location).

1. Sign out as the data lake administrator user and sign in as `lf-consumer-analystuser` in US East (N. Virginia) Region using the password noted earlier from the CloudFormation output.

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. Choose **Settings** and select **Manage**.

1. In the **Location of query result** box, enter the path to the bucket that you created in CloudFormation outputs. Copy the value of `AthenaQueryResultLocation` (s3://lf-otf-tutorial-123456789012/athena-results/) and choose **Save**.

1. Run the following query to preview 10 records stored in the Iceberg table:

   ```
   select * from lficebergdb.product limit 10;
   ```

   For more information on querying Iceberg tables using Athena, see [Querying Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-table-data.html) in the *Amazon Athena User Guide*. 

## Step 3: Set up permissions for a Hudi table
<a name="set-up-hudi-table"></a>

In this section, you'll learn how to create a Hudi table in the AWS Glue Data Catalog, set up data permissions in AWS Lake Formation, and query data using Amazon Athena.

**To create a Hudi table**

In this step, you’ll run an AWS Glue job that creates an Hudi transactional table in the Data Catalog.

1. Sign in to the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/) in the US East (N. Virginia) Region

    as the data lake administrator user.

1. Choose **jobs** from the left navigation pane.

1. Select `native-hudi-create`.

1. Under **Actions**, choose **Edit job**.

1. Under **Job details**, expand **Advanced properties**, and check the box next to **Use AWS Glue Data Catalog as the Hive metastore** to add the table metadata in the AWS Glue Data Catalog. This specifies AWS Glue Data Catalog as the metastore for the Data Catalog resources used in the job and enables Lake Formation permissions to be applied later on the catalog resources.

1. Choose **Save**.

1. Choose **Run**. You can view the status of the job while it is running. 

   For more information on AWS Glue jobs, see [Working with jobs on the AWS Glue console](https://docs.aws.amazon.com/glue/latest/dg/console-jobs.html) in the *AWS Glue Developer Guide*.

    This job creates a Hudi(cow) table in the database:lfhudidb. Verify the `product` table in the Lake Formation console.

**To register the data location with Lake Formation**

Next, register an Amazon S3 path as the root location of your data lake.

1. Sign in to the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/) as the data lake administrator user.

1. In the navigation pane, under **Register and ingest**, choose **Data location**.

1. Choose **Register location**.

1. On the **Register location** page, enter the following:
   +  **Amazon S3 path** – Choose **Browse** and select `lf-otf-datalake-123456789012`. Choose the expand arrow next to the Amazon S3 root location to navigate to the `s3/buckets/lf-otf-datalake-123456789012/transactionaldata/native-hudi` location. 
   + **IAM role** – Choose `LF-OTF-RegisterRole` as the IAM role.
   + Choose **Register location**.

**To grant data lake permissions on the Hudi table**

In this step, we'll grant data lake permissions to the business analyst user.

1. Under **Data lake permissions**, choose **Grant**.

1. On the **Grant data permissions** screen, choose, **IAM users and roles**.

1. `lf-consumer-analystuser` from the drop down.

1. Choose **Named data catalog resource**.

1. For **Databases** choose `lfhudidb`.

1. For **Tables**, choose `product`.

1. Next, you can grant column-based access by specifying columns.

   1. Under **Table permissions**, choose **Select**.

   1. Under **Data permissions**, choose **Column-based access**, choose **Include columns**.

   1. Choose `product_name`, `price`, and `category` columns.

   1. Choose **Grant**.

**To query the Hudi table using Athena**

 Now start querying the Hudi table you created using Athena. If it is your first time running queries in Athena, you need to configure a query result location. For more information, see [Specifying a query result location](https://docs.aws.amazon.com/athena/latest/ug/querying.html#query-results-specify-location).

1. Sign out as the data lake administrator user and sign in as `lf-consumer-analystuser` in US East (N. Virginia) Region using the password noted earlier from the CloudFormation output.

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. Choose **Settings** and select **Manage**.

1. In the **Location of query result** box, enter the path to the bucket that you created in CloudFormation outputs. Copy the value of `AthenaQueryResultLocation` (s3://lf-otf-tutorial-123456789012/athena-results/) and **Save**.

1. Run the following query to preview 10 records stored in the Hudi table:

   ```
   select * from lfhudidb.product limit 10;
   ```

   For more information on querying Hudi tables, see the [Querying Hudi tables](https://docs.aws.amazon.com/athena/latest/ug/querying-hudi.html) section in the *Amazon Athena User Guide*.

## Step 4: Set up permissions for a Delta Lake table
<a name="set-up-delta-table"></a>

In this section, you'll learn how to create a Delta Lake table with symlink manifest file in the AWS Glue Data Catalog, set up data permissions in AWS Lake Formation and query data using Amazon Athena.

**To create a Delta Lake table**

In this step, you’ll run an AWS Glue job that creates a Delta Lake transactional table in the Data Catalog.

1. Sign in to the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/) in the US East (N. Virginia) Region

    as the data lake administrator user.

1. Choose **jobs** from the left navigation pane.

1. Select `native-delta-create`.

1. Under **Actions**, choose **Edit job**.

1. Under **Job details**, expand **Advanced properties**, and check the box next to **Use AWS Glue Data Catalog as the Hive metastore** to add the table metadata in the AWS Glue Data Catalog. This specifies AWS Glue Data Catalog as the metastore for the Data Catalog resources used in the job and enables Lake Formation permissions to be applied later on the catalog resources.

1. Choose **Save**.

1. Choose **Run** under **Actions**.

    This job creates a Delta Lake table named `product` in the `lfdeltadb` database. Verify the `product` table in the Lake Formation console.

**To register the data location with Lake Formation**

Next, register the Amazon S3 path as the root location of your data lake.

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/) the data lake administrator user.

1. In the navigation pane, under **Register and ingest**, choose **Data location**.

1. Choose **Register location**.

1. On the **Register location** page, enter the following:
   +  **Amazon S3 path** – Choose **Browse** and select `lf-otf-datalake-123456789012`. Choose the expand arrow next to the Amazon S3 root location to navigate to the `s3/buckets/lf-otf-datalake-123456789012/transactionaldata/native-delta` location. 
   + **IAM role** – Choose `LF-OTF-RegisterRole` as the IAM role.
   + Choose **Register location**.

**To grant data lake permissions on the Delta Lake table**

In this step, we'll grant data lake permissions to the business analyst user.

1. Under **Data lake permissions**, choose **Grant**.

1. On the **Grant data permissions** screen, choose, **IAM users and roles**.

1. `lf-consumer-analystuser` from the drop down.

1. Choose **Named data catalog resource**.

1. For **Databases** choose `lfdeltadb`.

1. For **Tables**, choose `product`.

1. Next, you can grant column-based access by specifying columns.

   1. Under **Table permissions**, choose **Select**.

   1. Under **Data permissions**, choose **Column-based access**, choose **Include columns**.

   1. Choose `product_name`, `price`, and `category` columns.

   1. Choose **Grant**.

**To query the Delta Lake table using Athena**

 Now start querying the Delta Lake table you created using Athena. If it is your first time running queries in Athena, you need to configure a query result location. For more information, see [Specifying a query result location](https://docs.aws.amazon.com/athena/latest/ug/querying.html#query-results-specify-location).

1. Log out as the data lake administrator user and login as `BusinessAnalystUser` in US East (N. Virginia) Region using the password noted earlier from the CloudFormation output.

1. Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).

1. Choose **Settings** and select **Manage**.

1. In the **Location of query result** box, enter the path to the bucket that you created in CloudFormation outputs. Copy the value of `AthenaQueryResultLocation` (s3://lf-otf-tutorial-123456789012/athena-results/) and **Save**.

1. Run the following query to preview 10 records stored in the Delta Lake table:

   ```
   select * from lfdeltadb.product limit 10;
   ```

   For more information on querying Delta Lake tables, see the [Querying Delta Lake tables](https://docs.aws.amazon.com/athena/latest/ug/delta-lake-tables.html) section in the *Amazon Athena User Guide*.

## Step 5: Clean up AWS resources
<a name="otf-tut-clean-up"></a>

**To clean up resources**

To prevent unwanted charges to your AWS account, delete the AWS resources that you used for this tutorial.

1. Sign in to the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/) as the IAM administrator.

1. [Delete the cloud formation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html). The tables you created are automatically deleted with the stack.