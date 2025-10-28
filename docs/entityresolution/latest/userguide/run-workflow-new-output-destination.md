# Running a custom ID mapping

workflow

###### Note

This procedure is available for [workflows within a single
AWS account](creating-id-mapping-workflow-same-account.md "creating-id-mapping-workflow-same-account.md") or [workflows that span two
AWS accounts](creating-id-mapping-workflow-two-accounts.md "creating-id-mapping-workflow-two-accounts.md") with incremental processing enabled.

When running an ID mapping workflow, you can specify a different Amazon S3 location for your
output data than what was originally configured. You can also choose how to process your data
by selecting one of three run types: **Batch** (processes all data),
**Incremental** (processes only new or changed data), or **Delete
only** (processes only deletion requests).

###### To run an ID mapping workflow with a new output destination

1. Sign in to the AWS Management Console and open the AWS Entity Resolution console at [https://console.aws.amazon.com/entityresolution/](https://console.aws.amazon.com/entityresolution/ "https://console.aws.amazon.com/entityresolution/").
2. In the left navigation pane, under **Workflows**, choose **ID
   mapping**.
3. Choose the ID mapping workflow that you want to run.
4. On the ID mapping workflow details page, choose **Run workflow**, and
   then choose **Run with new output destination**.
5. For **Data output destination**, configure the following.
   1. For **Run type**, select one of the following options.
      - **Batch** – Processes the entire ID mapping table.

      Recommended for initial setup, periodic full refreshes, or when significant
      changes occur in both Source and Target ID namespaces.
      - **Incremental** – Processes only new, updated, or
        deleted records in either the Source or Target ID namespace.

      Recommended for frequent updates, daily runs, or real-time data
      synchronization.
      - **Delete only** – Processes only deleted records from
        the Target ID namespace.

      Recommended for quickly synchronizing removals.

   2. Choose the **Amazon S3 location** for the data output.
   3. For **Encryption**, do one of the following:
      - Keep the default encryption settings
      - Choose **Customize encryption settings**, and either enter
        the **AWS KMS key** ARN or choose **Create an AWS KMS
        key**.

6. To specify the **Service access** permissions, choose an option and
   take the recommended action.

| Option                                | Recommended action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Create and use a new service role** | <br>• AWS Entity Resolution creates a service role with the required policy for this table. <br>• The default **Service role name** is `entityresolution-id-mapping-workflow-<timestamp>`. <br>• You must have permissions to create roles and attach policies. <br>• If your input data is encrypted, choose the **This data is encrypted by a KMS key** option. Then, enter an **AWS KMS key** that is used to decrypt your data input.                                                                                                                                |
| **Use an existing service role**      | 1. Choose an **Existing service role name** from the dropdown list. The list of roles are displayed if you have permissions to list roles. If you don't have permissions to list roles, you can enter the Amazon Resource Name (ARN) of the role that you want to use. If there are no existing service roles, the option to **Use an existing service role** is unavailable. 2. View the service role by choosing the **View in IAM** external link. By default, AWS Entity Resolution doesn't attempt to update the existing role policy to add necessary permissions. | 7. Choose **Run**. 8. On the matching workflow details page, on the **Metrics** tab, view the following under **Last job metrics**: <br>• The **Job ID** <br>• The **Time completed** for the workflow job <br>• The **Status** of the matching workflow job: **Queued**, **In progress**, **Completed**, **Failed** <br>• The number of **Records processed** <br>• The number of **Records not processed** <br>• The number of **Input records** <br>• The number of **Unique match IDs generated**. <br>• The number of **New mapped records**. <br>• The number of **New mapped target records**. <br>• The number of **New mapped source records**. <br>• The number of **New mapped source records removed**. <br>• The number of **New mapped target records removed**. <br>• The number of **New mapped records removed**. Under **Job history**, you can also view the job metrics for previously run ID mapping workflow jobs. 9. After the ID mapping workflow job completes (status is **Completed**), choose **Data output**, and then choose your **Amazon S3 location** to view the results. After you get your CSV file, you can join the `RAMPID` with the `TRANSCODED_ID`. |
