

# Preparing first-party input data
<a name="prepare-input-data"></a>

The following steps describe how to prepare first-party data to use in a [rule-based matching workflow](creating-matching-workflow-rule-based.md), [machine learning-based matching workflow](create-matching-workflow-ml.md), or an [ID mapping workflow](create-id-mapping-workflow.md). 

## Step 1: Prepare first-party data tables
<a name="prepare-first-party-tables"></a>

Each matching workflow type has a different set of recommendations and guidelines to help ensure a success.

To prepare first-party data tables, consult the following table: 


**First-party data tables guidelines**  

| Workflow type | Required | 
| --- | --- | 
| Rule-based matching workflow with Advanced rule type |  +  A [Unique ID](glossary.md#unique-id-defn) is required.  <br />+  The Unique ID doesn't exceed 38 characters.  <br />+  (Optional) A DELETE column that specifies which records to remove from AWS Entity Resolution after the workflow has finished processing. The default value is {{false}} if the column exists without any values. Records with the DELETE column set to {{true}} will be delete. Records with the DELETE column set to {{false}} or empty will processed by AWS Entity Resolution.  <br />The schema must have a DELETE column with type `String` and no `matchKey` and `groupName`.  Look up match ID (`GetMatchID`) isn't supported because the **Advanced** rule type for the **Manual** processing cadence doesn't store any ingested data.  <br />In the following example, `S1` will be ingested and `S2` will be deleted. <pre>sourceID, name, lastName, DELETE<br />S1, name, lastname, false<br />S2, name2, lastname2, true</pre>   | 
| rule-based matching workflow with Simple rule type |  +  A [Unique ID](glossary.md#unique-id-defn) is required.  <br />+  The Unique ID doesn't exceed 38 characters.    | 
| machine learning-based matching workflow |  +  A [Unique ID](glossary.md#unique-id-defn) is required.  <br />+  The dataset contains one of the following types:   **Full Name**   **Full Address**   **Full phone**   **Email address**   **Date** – with a **Match key name** of **Date of birth**   <br />+  None of the column names use the following reserved names: "`MatchId`", "`MatchRule`", `RecordId`, `SourceId`", " and `TargetId`". <br />+  (Optional) A DELETE column that specifies which records to remove from AWS Entity Resolution after the workflow has finished processing. The default value is {{false}} if the column exists without any values. Records with the DELETE column set to {{true}} will be deleted. Records with the DELETE column set to {{false}} or empty will be processed by AWS Entity Resolution.  <br />The schema must have a DELETE column with type `String` and no `matchKey` and `groupName`. <br />In the following example, `S1` will be ingested and `S2` will be deleted. <pre>sourceID, name, lastName, DELETE<br />S1, name, lastname, false<br />S2, name2, lastname2, true</pre>   | 
| ID mapping workflow  |  +  A [Unique ID](glossary.md#unique-id-defn) is required.  <br />+  The Unique ID doesn't exceed 257 characters.  <br />+  (Optional) A DELETE column that specifies which records to remove from AWS Entity Resolution after the workflow has finished processing. The default value is {{false}} if the column exists without any values. Records with the DELETE column set to {{true}} will be delete. Records with the DELETE column set to {{false}} or empty will processed by AWS Entity Resolution.  <br />The schema must have a DELETE column with type `String` and no `matchKey` and `groupName`. <br />In the following example, `S1` will be ingested and `S2` will be deleted. <pre>sourceID, name, lastName, DELETE<br />S1, name, lastname, false<br />S2, name2, lastname2, true</pre>   | 

## Step 2: Save your input data table in a supported data format
<a name="save-input-data"></a>

If you already saved your first-party input data in a supported data format, you can skip this step. 

To use AWS Entity Resolution, the input data must be in a format that AWS Entity Resolution supports. 

AWS Entity Resolution supports the following data formats:
+ comma-separated value (CSV)
+ Parquet

## Step 3: Upload your input data table to Amazon S3
<a name="upload-to-s3"></a>

If you already have your first-party data table in Amazon S3, you can skip this step.

**Note**  
You can store the input data in Amazon S3resources in any Region in the AWS commercial partition where S3 is supported. This data can be accessed from a different Region or AWS account when running the matching workflow.

**To upload your input data table to Amazon S3**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Buckets**, and then choose a bucket to store your data table. 

1. Choose **Upload**, and then follow the prompts.

1. Choose the **Objects** tab to view the prefix where your data is stored. Make a note of the name of the folder.

   You can select the folder to view the data table.

## Step 4: Create an AWS Glue table
<a name="create-glue-table"></a>

**Note**  
If you need partitioned AWS Glue tables, skip to [Step 4: Create a partitioned AWS Glue table](#create-partitioned-glue-table).

The input data in Amazon S3 must be cataloged in AWS Glue and represented as an AWS Glue table. For more information about how to create an AWS Glue table with Amazon S3 as the input, see [Working with crawlers on the AWS Glue console](https://docs.aws.amazon.com/glue/latest/dg/console-crawlers.html) in the *AWS Glue Developer Guide.*

In this step, you set up a crawler in AWS Glue that crawls all the files in your S3 bucket and create an AWS Glue table. 

**Note**  
AWS Entity Resolution doesn't currently support Amazon S3 locations registered with AWS Lake Formation.

**To create an AWS Glue table**

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. From the navigation bar, select **Crawlers**.

1. Select your S3 bucket from the list, and then choose **Create crawler**.

1. On the **Set crawler properties** page, enter a crawler**Name**optional **Description**, and then choose **Next**.

1. Continue through the **Add crawler page**, specifying the details. 

1. On the **Choose an IAM role** page, choose **Choose an existing IAM role** and then choose **Next**.

   You can also choose **Create an IAM role** or have your administrator create the IAM role if needed.

1. For **Create a schedule for this crawler**, keep the **Frequency** default (**Run on demand**) and then choose **Next**.

1. For **Configure the crawler’s output**, enter the AWS Glue database and then choose **Next**.

1. Review all the details, and then choose **Finish**.

1. On the **Crawlers** page, select the check box next to your S3 bucket and then choose **Run crawler**.

1. After the crawler is finished running, on the AWS Glue navigation bar, choose **Databases**, and then choose your database name.

1. On the **Database** page, choose **Tables in {your database name}**.

   1. View the tables in the AWS Glue database.

   1. To view a table's schema, select a specific table.

   1. Make a note of the AWS Glue database name and AWS Glue table name.

You are now ready to create a schema mapping. For more information, see [Creating a schema mapping](create-schema-mapping.md).

## Step 4: Create a partitioned AWS Glue table
<a name="create-partitioned-glue-table"></a>

**Note**  
The AWS Glue partitioning feature in AWS Entity Resolution is only supported in ID mapping workflows. This AWS Glue partitioning feature enables you to choose specific partitions for processing with AWS Entity Resolution.  
If you don't need partitioned AWS Glue tables, you can skip this step.

A partitioned AWS Glue table automatically reflects new partitions in the AWS Glue table when you add new folders to the data structure (such as a new day folder under a month). 

When you create a partitioned AWS Glue table in AWS Entity Resolution, you can specify which partitions you want to process in an ID mapping workflow. Then, every time you run the ID mapping workflow, only the data in those partitions are processed, rather than processing all of the data in the entire AWS Glue table. This feature allows for more precise, efficient, and cost-effective data processing in AWS Entity Resolution, giving you greater control and flexibility in managing your entity resolution tasks. 

You can create a partitioned AWS Glue table for the source account in an ID mapping workflow. 

You must first catalog the input data in Amazon S3 in AWS Glue and represented it as an AWS Glue table. For more information about how to create an AWS Glue table with Amazon S3 as the input, see [Working with crawlers on the AWS Glue console](https://docs.aws.amazon.com/glue/latest/dg/console-crawlers.html) in the *AWS Glue Developer Guide.*

In this step, you set up a crawler in AWS Glue that crawls all the files in your S3 bucket and then create a partitioned AWS Glue table. 

**Note**  
AWS Entity Resolution doesn't currently support Amazon S3 locations registered with AWS Lake Formation.

**To create a partitioned AWS Glue table**

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. From the navigation bar, select **Crawlers**.

1. Select your S3 bucket from the list, and then choose **Create crawler**.

1. On the **Set crawler properties** page, enter a crawler **Name**, optional **Description**, and then choose **Next**.

1. Continue through the **Add crawler page**, specifying the details. 

1. On the **Choose an IAM role** page, choose **Choose an existing IAM role** and then choose **Next**.

   You can also choose **Create an IAM role** or have your administrator create the IAM role if needed.

1. For **Create a schedule for this crawler**, keep the **Frequency** default (**Run on demand**) and then choose **Next**.

1. For **Configure the crawler’s output**, enter the AWS Glue database and then choose **Next**.

1. Review all the details, and then choose **Finish**.

1. On the **Crawlers** page, select the check box next to your S3 bucket and then choose **Run crawler**.

1. After the crawler is finished running, on the AWS Glue navigation bar, choose **Databases**, and then choose your database name.

1. On the **Database** page, under **Tables**, choose the table to be partitioned.

1. On the **Table overview**, select the **Actions** dropdown, and then choose **Edit table**.

   1. Under **Table properties**, choose **Add**.

   1. For the new **Key**, enter **aerPushDownPredicateString**.

   1. For the new **Value**, enter **'<PartitionKey>=<PartitionValue'**.

   1. Make a note of the AWS Glue database name and AWS Glue table name.

You are now ready to: 
+ [Create a schema mapping](create-schema-mapping.md) and then [create an ID mapping workflow for one AWS account](creating-id-mapping-workflow-same-account.md).
+ [Create an ID namespace source](create-id-namespace-source.md), [create an ID namespace target](create-id-namespace-target.md), and then [create an ID mapping workflow across two AWS accounts](creating-id-mapping-workflow-two-accounts.md).