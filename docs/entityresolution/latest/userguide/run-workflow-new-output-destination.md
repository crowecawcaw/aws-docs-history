

# Running a custom ID mapping workflow
<a name="run-workflow-new-output-destination"></a>

**Note**  
This procedure is available for [workflows within a single AWS account](creating-id-mapping-workflow-same-account.md) or [workflows that span two AWS accounts](creating-id-mapping-workflow-two-accounts.md) with incremental processing enabled.

When running an ID mapping workflow, you can specify a different Amazon S3 location for your output data than what was originally configured. You can also choose how to process your data by selecting one of three run types: **Batch** (processes all data), **Incremental** (processes only new or changed data), or **Delete only** (processes only deletion requests). 

**To run an ID mapping workflow with a new output destination**

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/).

1. In the left navigation pane, under **Workflows**, choose **ID mapping**.

1. Choose the ID mapping workflow that you want to run.

1. On the ID mapping workflow details page, choose **Run workflow**, and then choose **Run with new output destination**.

1. For **Data output destination**, configure the following.

   1. For **Run type**, select one of the following options.
      + **Batch** – Processes the entire ID mapping table. 

        Recommended for initial setup, periodic full refreshes, or when significant changes occur in both Source and Target ID namespaces.
      + **Incremental** – Processes only new, updated, or deleted records in either the Source or Target ID namespace.

        Recommended for frequent updates, daily runs, or real-time data synchronization.
      + **Delete only** – Processes only deleted records from the Target ID namespace. 

        Recommended for quickly synchronizing removals.

   1. Choose the **Amazon S3 location** for the data output.

   1. For **Encryption**, do one of the following: 
      + Keep the default encryption settings
      + Choose **Customize encryption settings**, and either enter the **AWS KMS key** ARN or choose **Create an AWS KMS key**.

      

1. To specify the **Service access** permissions, choose an option and take the recommended action.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/entityresolution/latest/userguide/run-workflow-new-output-destination.html)

1. Choose **Run**.

1. On the matching workflow details page, on the **Metrics** tab, view the following under **Last job metrics**:
   + The **Job ID**
   + The **Time completed** for the workflow job
   + The **Status** of the matching workflow job: **Queued**, **In progress**, **Completed**, **Failed** 
   + The number of **Records processed**
   + The number of **Records not processed**
   + The number of **Input records**
   + The number of **Unique match IDs generated**.
   + The number of **New mapped records**.
   + The number of **New mapped target records**.
   + The number of **New mapped source records**.
   + The number of **New mapped source records removed**.
   + The number of **New mapped target records removed**.
   + The number of **New mapped records removed**.

   Under **Job history**, you can also view the job metrics for previously run ID mapping workflow jobs.

1. After the ID mapping workflow job completes (status is **Completed**), choose **Data output**, and then choose your **Amazon S3 location** to view the results.

   After you get your CSV file, you can join the `RAMPID` with the `TRANSCODED_ID`.