

# Creating a collaboration for ML modeling
<a name="create-collab-ml-modeling"></a>

In this procedure, you as the [collaboration creator](glossary.md#glossary-collaboration-creator) perform the following tasks:
+ [Create a collaboration](create-collaboration.md).
+ Invite one or more [members](glossary.md#glossary-member) to the [collaboration](glossary.md#glossary-collaboration).
+ Assign abilities to members, such as the 
  + [Member who can query](glossary.md#glossary-member-who-can-query)
  + [Member who can receive results](glossary.md#glossary-member-who-can-receive-results)
  + Member who can receive output from trained models
  + Member who can output from model inference

  If the collaboration creator is also the member who can receive results, they specify the results destination and format. They also provide a service role Amazon Resource Name (ARN) to write the results to the results destination.
+ Configure which [member is responsible for paying for compute costs, model training, and model inference costs in the collaboration](glossary.md#glossary-member-paying-for-query-compute).

Before you begin, make sure that you have completed the following prerequisites: 
+ You have the name and AWS account ID for each member that you want to invite to the collaboration.
+ You have permission to share the name and AWS account ID for each member with all members of the collaboration.
**Note**  
You can’t add more members after you create the collaboration. 

For information about how to create a collaboration using the AWS SDKs, see the *[AWS Clean Rooms API Reference](https://docs.aws.amazon.com/clean-rooms/latest/apireference/Welcome.html)*.

**To create a collaboration for ML modeling**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with the AWS account that will function as the collaboration creator.

1. In the left navigation pane, choose **Collaborations**.

1. In the upper right corner, choose **Create collaboration**.

1. For **Step 1: Define collaboration**, do the following:

   1. For **Details**, enter the **Name** and **Description** of the collaboration.

      This information will be visible to collaboration members who are invited to participate in the collaboration. The **Name** and **Description** helps them understand what the collaboration is in reference to. 

   1. For **Members**:

      1. For **Member 1: You**, enter your **Member display name** as you want it to appear for the collaboration.
**Note**  
Your AWS account ID is included automatically for **Member AWS account ID**.

      1. For **Member 2**, enter the **Member display name** and **Member AWS account ID** for the member that you want to invite to the collaboration.

         The **Member display name** and **Member AWS account ID** will be visible to everyone invited to the collaboration. After you enter and save the values for these fields, you can't edit them.
**Note**  
You must inform the collaboration member that their **Member AWS account ID** and **Member display name** will be visible to all invited and active collaborators in the collaboration.

      1. If you want to add another member, choose **Add another member**. Then enter the **Member display name** and **Member AWS account ID** for each member who can contribute data that you want to invite to the collaboration.

   1. If you want to enable **Analysis logging**, select the **Enable analysis logging** checkbox, and then under **Supported log types**, choose **Logs from queries**.

   1. If you want to enable **Detailed monitoring**, select the **Enable detailed monitoring** checkbox.

      The analysis runner and configured payor can choose to enable detailed metrics when they create their membership. When enabled, detailed monitoring metrics will be published to CloudWatch for operational monitoring of collaborations, including query performance and resource utilization. These metrics will be available to the analysis runner and configured payor in their respective AWS accounts.

      For more information about CloudWatch pricing, see [CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

   1. Under **Allowed query results regions**, select one or more AWS Regions where you want to send query results.

      By default, only the current Region (such as N. Virginia us-east-1) is selected. 
**Important**  
When you enable cross-Region query results delivery, your results may be processed and stored outside the source Region.

      For more information about Regions, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *AWS General Reference*. 

   1. (Optional) Manage access to your data with **Automatic change request approval** by configuring which settings can be changed automatically without manual approvals for a change request. By default, some settings can only be changed by submitting a change request which must be approved by all members before it can take effect.
      + **Grant member abilities** – Choose the abilities that can be granted to collaboration members without manual approval. Members can always contribute data.
        + Choose abilities:
          + Contribute data *(always enabled)*
          + Receive results
        + **Auto-approve new members with these abilities** – If allowed, any members added with the abilities selected above will instantly join the collaboration. Members added with other abilities will still require manual approval to join.
      + **Abilities that can be automatically revoked** - Choose the abilities that can be revoked without manual approval. Members can always contribute data.
        + Choose abilities:
          + Contribute data *(always enabled)*
          + Receive results

      If you choose this option, you can track all collaboration configuration modifications through the **Change requests history**, located on the **Details** tab of the collaboration details page.

   1. (Optional) If you want to enable the **Cryptographic computing** capability, select the **Enable cryptographic computing** checkbox.

      1. Choose the following **Cryptographic coverage parameters**:
         + **Allow plaintext columns**

           Choose **No** if you require fully encrypted tables.

           Choose **Yes** if you want cleartext columns allowed in the encrypted table.

           To run SUM or AVG on certain columns, the columns must be in cleartext.
         + **Preserve NULL values**

           Choose **No** if you don't want to preserve NULL values. NULL values won't appear as NULL in an encrypted table.

           Choose **Yes** if you want to preserve NULL values. NULL values will appear as NULL in an encrypted table.

      1. Choose the following **Fingerprinting parameters**:
         + **Allow duplicates**

           Choose **No** if you don't want duplicate entries allowed in a fingerprint column.

           Choose **Yes** if you want duplicate entries allowed in a fingerprint column.
         + **Allow JOIN of columns with different names**

           Choose **No** if you don't want to join fingerprint columns with different names.

           Choose **Yes** if you want to join fingerprint columns with different names.

      For more information about **Cryptographic computing parameters**, see [Cryptographic computing parameters](crypto-computing-parameters.md).

      For more information about how to encrypt your data for use in AWS Clean Rooms, see [Preparing encrypted data tables with Cryptographic Computing for Clean Rooms](prepare-encrypted-data.md).
**Note**  
Verify these configurations carefully before completing the next step. After you create the collaboration, you can only edit the collaboration name, description, and whether the logs are stored in Amazon CloudWatch Logs.

   1. If you want to enable **Tags** for the collaboration resource, choose **Add new tag** and then enter the **Key** and **Value** pair.

   1. Choose **Next**.

1. For **Step 2: Specify member abilities**, 

   1. For **Analysis using queries and jobs**, under the **Supported analysis types**, leave the **Queries** checkbox selected.

   1. For **Run queries**, choose the member who will initiate the model training

   1. For **Receive results from analyses**, choose one or more members who will receive the query results.

   1. For **ML modeling using purpose-built workflows**, 

      1. For **Receive output from trained models**, choose the member who will receive trained model results, including model artifacts and metrics.

      1. For **Receive output from model inference**, choose the member who will receive the model inference results.

   1. View the member abilities under **ID resolution using AWS Entity Resolution**.

1. For **Step 3: Configure payment**, 

   1. Under **Analysis using queries**, for **Pay for queries**, do one of the following actions:
      + To have the same member pay for and run queries, select the same member you chose for **Run queries**.
      + To have a different member pay for query costs, select your member account.

   1. For **ML modeling using purpose-built workflows**, 

      1. Choose the member who will **Pay for model training**.

   1. Choose the member who will **Pay for inference job**.

   1. For **Pay for lookalike modeling**, no action is needed. The **Creator of the configured lookalike model** is the member who will pay for lookalike modeling.

   1. (Optional) Choose the member who will **Pay for Synthetic data generation**.

   1. For **ID resolution with AWS Entity Resolution**, no action is needed. The **Creator of the ID mapping table** is the member who will **Pay for ID mapping table**.

1. Choose **Next**.

1. For **Step 4: Configure membership**, under **Collaboration membership**, choose one of the following options:

------
#### [ Yes, join by creating membership now ]

   1. For **Results settings defaults**, for **Query results settings**, if you are the member who can **Receive results**, 

      1. Select the **Set default settings for queries** checkbox.

      1. For the **Results destination in Amazon S3**, enter the Amazon S3 destination or choose **Browse S3** to select an S3 bucket.

      1. For the query **Result format**, choose either **CSV** or **PARQUET**.

      1. (Spark only) For the **Result files**, choose either **Multiple** or **Single**.

      1. (Optional) If you want to deliver queries that take up to 24 hours to your S3 destination, select the **Add a service role to support queries that take up to 24 hours to complete** checkbox.

         Large queries that take up to 24 hours to complete will be delivered to your S3 destination.

         If you don't select the checkbox, only queries that complete within 12 hours will be delivered to your S3 location. 

      1. Specify the **Service access** permissions by selecting either **Create and use a new service role** or **Use an existing service role**.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/create-collab-ml-modeling.html)
**Note**  
AWS Clean Rooms requires permissions to query according to the analysis rules. For more information about permissions for AWS Clean Rooms, see [AWS managed policies for AWS Clean Rooms](security-iam-awsmanpol.md).
If the role doesn’t have sufficient permissions for AWS Clean Rooms, you receive an error message stating that the role doesn't have sufficient permissions for AWS Clean Rooms. The role policy must be added before proceeding.
If you can’t modify the role policy, you receive an error message stating that AWS Clean Rooms couldn't find the policy for the service role.

   1. For **ML configuration**, 

      1. Choose the **Create ML configuration** checkbox, and then specify the **Model output destination on Amazon S3** by entering the S3 destination or choose **Browse S3** to select from a list of available S3 buckets.

      1. Specify the **Service access** permissions by choosing to either **Create and use a new service role** or **Use an existing service role**.

      1. If the S3 bucket is encrypted, select the **The destination bucket is encrypted with a KMS key** checkbox and then enter the **AWS KMS key** or select **Create an AWS KMS key** to create a new KMS key.

   1. If you want to enable **Membership tags** for the membership resource, choose **Add new tag** and then enter the **Key** and **Value** pair. 

   1. If you are the member who is paying for **Query compute**, indicate your acceptance by selecting the **I agree to pay for the compute costs in this collaboration** checkbox.
**Note**  
You must select this checkbox to proceed.  
For more information about how pricing is calculated, see [Pricing for AWS Clean Rooms](what-is.md#pricing).

      If you are the [member paying for query compute costs](glossary.md#glossary-member-paying-for-query-compute) but not the [member who can query](glossary.md#glossary-member-who-can-run-queries-jobs), it is recommended that you use AWS Budgets to configure a budget for AWS Clean Rooms and receive notifications once the maximum budget has been reached. For more information about setting up a budget, see [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) in the *AWS Cost Management User Guide*. For more information about setting up notifications, see [Creating an Amazon SNS topic for budget notifications](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-sns-policy.html) in the *AWS Cost Management User Guide*. If the maximum budget has been reached, you can contact the member who can run queries or [leave the collaboration](leave-collab.md). If you leave the collaboration, no more queries will be allowed to run, and therefore you will no longer be billed for query compute costs.

   1. Choose **Next**.

   Both the collaboration and your membership are created. 

   Your status in the collaboration is active.

------
#### [ No, I will create a membership later ]

   1. Choose **Next**.

      Only the collaboration is created. 

      Your status in the collaboration is inactive.

------

1. For **Step 5: Review and create**, do the following:

   1. Review the selections that you made for the previous steps and edit if necessary. 

   1. Choose one of the options.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/create-collab-ml-modeling.html)