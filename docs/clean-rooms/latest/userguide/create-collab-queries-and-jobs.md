# Creating a collaboration for queries and

jobs

In this procedure, you as the [collaboration creator](glossary.md#glossary-collaboration-creator "glossary.md#glossary-collaboration-creator") perform the
following tasks:

- [Create a
  collaboration](create-collaboration.md "create-collaboration.md").
- Invite one or more [members](glossary.md#glossary-member "glossary.md#glossary-member") to the [collaboration](glossary.md#glossary-collaboration "glossary.md#glossary-collaboration").
- Assign abilities to members, such as the [member who can run queries and
  jobs](glossary.md#glossary-member-who-can-run-queries-jobs "glossary.md#glossary-member-who-can-run-queries-jobs") and the [member who can receive
  results](glossary.md#glossary-member-who-can-receive-results "glossary.md#glossary-member-who-can-receive-results").

If the collaboration creator is also the member who can receive results, they specify
the results destination and format. They also provide a service role Amazon Resource Name
(ARN) to write the results to the results destination.

- Configure which [member is responsible for
  paying for query and job compute costs in the collaboration](glossary.md#glossary-member-paying-for-query-job-compute "glossary.md#glossary-member-paying-for-query-job-compute").
  Before you begin, make sure that you have completed the following prerequisites:

- You have the name and AWS account ID for each member that you want to invite to the
  collaboration.
- You have permission to share the name and AWS account ID for each member with all
  members of the collaboration.

###### Note

You can’t add more members after you create the collaboration.
For information about how to create a collaboration using the AWS SDKs, see the
_[AWS Clean Rooms API
Reference](../apireference/Welcome.md "../apireference/Welcome.md")_.

###### To create a collaboration for queries and jobs

1.  Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with the AWS account that will function as the
    collaboration creator.
2.  In the left navigation pane, choose **Collaborations**.
3.  In the upper right corner, choose **Create collaboration**.
4.  For **Step 1: Define collaboration**, do the following:
    1. For **Details**, enter the **Name** and
       **Description** of the collaboration.

    This information will be visible to collaboration members who are invited to
    participate in the collaboration. The **Name** and
    **Description** helps them understand what the collaboration is in
    reference to. 2. For **Analytics engine**, choose
    **Spark**.

    ###### Note

    AWS Clean Rooms will end support for the legacy Clean Rooms SQL analytics engine on
    December 17th, 2025. Before July 16, 2025, you must request a limit increase via
    AWS Customer Support to create any new Clean Rooms SQL engine-based
    collaborations. Starting July 17, 2025, the creation of new Clean Rooms SQL
    engine-based collaborations will no longer be available.

    If you want to update your collaboration from the AWS Clean Rooms SQL analytics engine to
    the Spark analytics engine, you can [edit an existing collaboration](edit-collaboration.md#change-collab-analytics-engine "edit-collaboration.md#change-collab-analytics-engine") or re-create the collaboration and select the Spark analytics engine. 3. For **Members**:

        1. For **Member 1: You**, enter your **Member display
         name** as you want it to appear for the collaboration.


        ###### Note

        Your AWS account ID is included automatically for **Member
         AWS account ID**.
        2. For **Member 2**, enter the **Member display
         name** and **Member AWS account ID** for the member
         that you want to invite to the collaboration.


        The **Member display name** and **Member
         AWS account ID** will be visible to everyone invited to the
         collaboration. After you enter and save the values for these fields, you can't
         edit them.


        ###### Note

        You must inform the collaboration member that their **Member
         AWS account ID** and **Member display name** will
         be visible to all invited and active collaborators in the collaboration.
        3. If you want to add another member, choose **Add another
         member**. Then enter the **Member display name** and
         **Member AWS account ID** for each member who can contribute
         data that you want to invite to the collaboration.

    4. If you want to enable **Analysis logging**, select the
       **Enable analysis logging** checkbox, and then choose the
       **Supported log types**.
       - If you want to receive logs generated from SQL queries, choose the
         **Logs from queries** checkbox.
       - If you want to receive logs generated from jobs using PySpark, choose the
         **Logs from jobs** checkbox.

    5. Under **Allowed query results regions**, select one or more
       AWS Regions where you want to send query results.

    By default, only the current Region (such as N. Virginia us-east-1) is
    selected.

    ###### Important

    When you enable cross-Region query results delivery, your results may be
    processed and stored outside the source Region.

    For more information about Regions, see [Regions
    and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _AWS General Reference_. 6. (Optional) To manage access to your data, for **Automatic change request
    approval**, choose one of the following options:

        * **Not allowed** – Blocks all requests. New members
         can't be added to the collaboration. This provides maximum control over
         collaboration membership.
        * **Allowed and auto approved** – Automatically approves
         all requests without review from other members. This provides flexible membership
         but less control over who joins the collaboration.


        If you choose this option, you can track all collaboration configuration
         modifications through the **Change requests history**, located on
         the **Details** tab of the collaboration details page.

    7.  (Optional) If you want to enable the **Cryptographic computing**
        capability, select the **Enable cryptographic computing**
        checkbox.
        1.  Choose the following **Cryptographic coverage
            parameters**:
            - **Allow plaintext columns**

            Choose **No** if you require fully encrypted
            tables.

            Choose **Yes** if you want cleartext
            columns allowed in the encrypted table.

            To run SUM or AVG on certain columns, the
            columns must be in cleartext.
            - **Preserve NULL values**

            Choose **No** if you don't want to preserve
            NULL values. NULL values won't appear as
            NULL in an encrypted table.

            Choose **Yes** if you want to preserve
            NULL values. NULL values will appear as
            NULL in an encrypted table.

        2.  Choose the following **Fingerprinting parameters**:

                * **Allow duplicates**


                Choose **No** if you don't want duplicate entries allowed
                 in a fingerprint column.


                Choose **Yes** if you want duplicate entries allowed in a
                 fingerprint column.
                * **Allow JOIN of columns with different
                 names**


                Choose **No** if you don't want to join
                 fingerprint columns with different names.


                Choose **Yes** if you want to join
                 fingerprint columns with different names.For more information about **Cryptographic computing

            parameters\*\*, see [Cryptographic computing parameters](crypto-computing-parameters.md "crypto-computing-parameters.md").

    For more information about how to encrypt your data for use in AWS Clean Rooms, see
    [Preparing encrypted data tables with Cryptographic Computing for Clean Rooms](prepare-encrypted-data.md "prepare-encrypted-data.md").

    ###### Note

    Verify these configurations carefully before completing the next step. After you
    create the collaboration, you can only edit the collaboration name, description, and
    whether the logs are stored in Amazon CloudWatch Logs. 8. If you want to enable **Tags** for the collaboration resource,
    choose **Add new tag** and then enter the **Key**
    and **Value** pair. 9. Choose **Next**.

5.  For **Step 2: Specify member abilities**, do the following:
    1. For **Analysis using queries and jobs**, under
       **Supported analysis types**, choose the **Jobs**
       checkbox.

    The **Queries** checkbox is selected by default.

        1. Select the member who can **Run queries and jobs** from the
         dropdown list.
        2. Select the member who can **Receive results from analyses**
         from the dropdown list.


        ###### Note

        The member who creates the PySpark analysis template must also be the member
         who receives results.

    2. If you are using Clean Rooms ML, for **ML modeling using purpose-built
       workflows**,
       1. (Optional) Select the member who can **Receive output from trained
          models** from the dropdown list.
       2. (Optional) Select the member who can **Receive output from model
          inference** from the dropdown list.

    3. View the member abilities under **ID resolution using
       AWS Entity Resolution**.
    4. Choose **Next**.

6.  For **Step 3: Configure payment**,
    1. For **Analysis using queries and jobs**, choose the member who
       will **Pay for queries and jobs**.

    You can assign the member who can **Run queries and jobs** to be
    the member who pays for the queries and jobs compute costs.

    You can assign a different member to pay for the queries and jobs compute
    costs. 2. For **ML modeling using purpose-built workflows**, the
    **Creator of the configured lookalike model** is the member who
    will **Pay for lookalike modeling**. 3. For **ID resolution with AWS Entity Resolution**, the **Creator of the ID
    mapping table** is the member who will **Pay for ID mapping
    table**. 4. Choose **Next**.

7.  For **Step 4: Configure membership**, choose one of the following
    options:

Yes, join by creating membership now

    1. For **Results settings defaults**, for **Query
     results settings**, if you are the member who can **Receive
     results**,




    	1. Choose the **Set default settings for queries**
    	 checkbox. For the **Results destination in Amazon S3**, enter
    	 the Amazon S3 destination or choose **Browse S3** to select an
    	 S3 bucket.
    	2. For the query **Result format**, choose either
    	 **CSV** or **PARQUET**.
    	3. (Spark only) For the **Result files**, choose either
    	 **Multiple** or **Single**.
    	4. (Optional) For **Service access**, if you want to
    	 deliver queries that take up to 24 hours to your S3 destination, select the
    	 **Add a service role to support queries that take up to 24 hours
    	 to complete** checkbox.


    	Large queries that take up to 24 hours to complete will be delivered to
    	 your S3 destination.


    	If you don't select the check box, only queries that complete within 12
    	 hours will be delivered to your S3 location.
    	5. Specify the **Service access** permissions by selecting
    	 either **Create and use a new service role** or
    	 **Use an existing service role**.





| If you choose to ...                                                                                             | Then ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Create and use a new service role                                                                                | <br>• AWS Clean Rooms creates a service role with the required policy for this table. <br>• The default **Service role name** is `cleanrooms-result-receiver-<timestamp>` <br>• You must have permissions to create roles and attach policies.                                                                                                                                                                                                                                                                                                                     |
| Use an existing service role                                                                                     | 1. Choose an **Existing service role name** from the dropdown list. The list of roles are displayed if you have permissions to list roles. If you don't have permissions to list roles, you can enter the Amazon Resource Name (ARN) of the role that you want to use. 2. View the service role by choosing the **View in IAM** external link. If there are no existing service roles, the option to **Use an existing service role** is unavailable. By default, AWS Clean Rooms doesn't attempt to update the existing role policy to add necessary permissions. | ###### Note <br>• AWS Clean Rooms requires permissions to query according to the analysis rules. For more information about permissions for AWS Clean Rooms, see [AWS managed policies for AWS Clean Rooms](security-iam-awsmanpol.md "security-iam-awsmanpol.md"). <br>• If the role doesn’t have sufficient permissions for AWS Clean Rooms, you receive an error message stating that the role doesn't have sufficient permissions for AWS Clean Rooms. The role policy must be added before proceeding. <br>• If you can’t modify the role policy, you receive an error message stating that AWS Clean Rooms couldn't find the policy for the service role. 2. For **Job results**, For example: `s3://bucket/prefix` 1. Choose the **Set default settings for jobs** checkbox, and then specify the **Results destination in Amazon S3** by entering the S3 destination or choose **Browse S3** to select from a list of available S3 buckets. 2. Specify the **Service access** permissions by choosing an **Existing service role name** from the dropdown list. 3. For **Logs settings**, choose one of the following options for **Log storage in Amazon CloudWatch Logs**: ###### Note The **Logs settings** section appears if you chose to enable **Query logging**. 1. Choose **Turn on** and the query logs relevant to you will be stored in your Amazon CloudWatch Logs account. Each member can receive only logs for queries that they initiated or that contain their data. The member who can receive results also receives logs for all queries run in a collaboration, even if their data isn't accessed in a query. Under **Supported log types**, choose from the log types the collaboration creator has chosen to support: Under **Supported log types**, the **Query logs** and **Job logs** checkboxes are turned on by default. ###### Note After you turn on **Analysis logging**, it can take a few minutes for log storage to be set up and start receiving logs in Amazon CloudWatch Logs. During this brief period, the member who can query might run queries that don’t actually send logs. 2. Choose **Turn off** and the query logs relevant to you won't be stored in your Amazon CloudWatch Logs account. 4. If you want to enable **Membership tags** for the membership resource, choose **Add new tag** and then enter the **Key** and **Value** pair. 5. If you are the member who is paying for **Query compute**, or **Job compute**, or both, indicate your acceptance by selecting the **I agree to pay for the compute costs in this collaboration** checkbox. ###### Note You must select this checkbox to proceed. For more information about how pricing is calculated, see [Pricing for AWS Clean Rooms](what-is.md#pricing "what-is.md#pricing"). If you are the [member paying for query compute costs](glossary.md#glossary-member-paying-for-query-compute "glossary.md#glossary-member-paying-for-query-compute") but not the [member who can query](glossary.md#glossary-member-who-can-run-queries-jobs "glossary.md#glossary-member-who-can-run-queries-jobs"), it is recommended that you use AWS Budgets to configure a budget for AWS Clean Rooms and receive notifications once the maximum budget has been reached. For more information about setting up a budget, see [Managing your costs with AWS Budgets](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md") in the _AWS Cost Management User Guide_. For more information about setting up notifications, see [Creating an Amazon SNS topic for budget notifications](../../../cost-management/latest/userguide/budgets-sns-policy.md "../../../cost-management/latest/userguide/budgets-sns-policy.md") in the _AWS Cost Management User Guide_. If the maximum budget has been reached, you can contact the member who can run queries or [leave the collaboration](leave-collab.md "leave-collab.md"). If you leave the collaboration, no more queries will be allowed to run, and therefore you will no longer be billed for query compute costs. 6. Choose **Next**. Both the collaboration and your membership are created. Your status in the collaboration is active. No, I will create a membership later 1. Choose **Next**. Only the collaboration is created. Your status in the collaboration is inactive. 8. For **Step 5: Review and create**, do the following: 1. Review the selections that you made for the previous steps and edit if necessary. 2. Choose one of the options. |
| If you have chosen to ...                                                                                        | Then choose ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Create a membership with the collaboration (**Yes, join by creating membership now**)                            | **Create collaboration and membership**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Create the collaboration, and not to create a membership at this time (**No, I will create a membership later**) | **Create collaboration**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | After your collaboration has been created successfully, you can see the collaboration details page under **Collaborations**. You are now ready to: <br>• [Prepare your data table to be analyzed in AWS Clean Rooms](prepare-data.md "prepare-data.md"). (Optional if you want to analyze your own event data or if you want to query identity data.) <br>• [Associate the configured table to your collaboration](associate-configured-table.md "associate-configured-table.md"). (Optional if you want to analyze your own event data.) <br>• [Add an analysis rule for the configured table](add-analysis-rule.md "add-analysis-rule.md"). (Optional if you want to analyze your own event data.) <br>• [Create a membership and join a collaboration](create-membership.md "create-membership.md"). (Optional if you've already created a membership.) <br>• [Invite members to join the collaboration](invite-members.md "invite-members.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
