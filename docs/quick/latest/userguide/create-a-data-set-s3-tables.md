

# Creating a dataset using Amazon S3 Tables
<a name="create-a-data-set-s3-tables"></a>

You can use Amazon S3 Tables as a data source to create datasets in Quick Sight. Amazon S3 Tables stores data as Apache Iceberg tables, enabling you to query your data lake directly from Quick Sight without setting up an intermediate query layer.

You can use Amazon S3 Tables datasets in the following query modes:
+ **Direct Query** – Query your Amazon S3 Tables data directly without importing it.
+ **SPICE** – Import your Amazon S3 Tables data into SPICE for faster performance.

## Configuring Amazon S3 Tables resource permissions (admin)
<a name="s3-tables-admin-setup"></a>

Before authors can create datasets from Amazon S3 Tables, an admin must configure resource permissions.

**To configure Amazon S3 Tables resource permissions**

1. Log in as an admin user.

1. Choose the people icon in the top right, and then choose **Manage QuickSuite** to open the admin page.

1. Choose the **AWS Resources** card to open the resource permissions page.

1. Choose **Use QuickSuite-managed role (default)** so that Quick manages the related IAM role and permissions for you.

1. Select **Amazon S3 Tables**. All available S3 table buckets in your current Region are displayed.

1. Select the S3 table buckets that you want to allow authors to use, and then choose **Finish**.

1. Choose **Save**.

After you save, a new IAM role named `aws-quicksight-s3-tables-role-v0` is created with permissions to read the selected S3 table buckets.

## Creating a data source for an Amazon S3 table bucket
<a name="s3-tables-create-data-source"></a>

**To create an Amazon S3 Tables data source**

1. From the left navigation pane, choose **Data**, and then choose the **Data sources** tab.

1. Choose **Create data source**.

1. Choose the **Amazon S3 Tables** card.

1. Enter the ARN of the S3 table bucket and a name for the data source, and then choose **Create data source**.

After a few seconds, the data source appears in your data sources list.

## Creating a dataset from an Amazon S3 Tables data source
<a name="s3-tables-create-dataset"></a>

**To create a dataset using Amazon S3 Tables**

1. From the left navigation pane, choose **Data**, and then choose the **Datasets** tab.

1. Choose **Create dataset**.

1. Select the Amazon S3 Tables data source that you want to use.

1. Select the namespace of the S3 table that you want to use, and then select the table.

1. Choose **Direct Query** or **SPICE** mode based on your use case.

1. Choose **Edit/Preview data** to transform your data in the same way you would for other data sources. After all transformations are defined, choose **Save and publish** to save the dataset.

**Note**  
Amazon S3 Tables datasets support a maximum of 2 billion rows.

For information about supported AWS Regions, see [Supported AWS Regions](https://docs.aws.amazon.com/quicksuite/latest/userguide/regions.html).