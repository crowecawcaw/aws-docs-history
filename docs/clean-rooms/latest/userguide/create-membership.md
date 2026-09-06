

# Creating a membership and joining a collaboration
<a name="create-membership"></a>

A *membership* is a resource that's created when a member joins a collaboration in AWS Clean Rooms. 

You can join a collaboration as a 
+ [member who can query](glossary.md#glossary-member-who-can-query)
+ [member who can run queries and jobs](glossary.md#glossary-member-who-can-run-queries-jobs)
+ [member who can receive results](glossary.md#glossary-member-who-can-receive-results) of a query or a job
+ [member paying for query compute costs](glossary.md#glossary-member-paying-for-query-compute)
+ [member paying for queries and jobs](glossary.md#glossary-member-paying-for-query-job-compute)

All members can contribute data.

For information about how to create a membership and join a collaboration using the AWS SDKs, see the *[AWS Clean Rooms API Reference](https://docs.aws.amazon.com/clean-rooms/latest/apireference/Welcome.html)*.

In this procedure, the invited member [joins the collaboration by creating a membership resource](#create-membership).

If the invited member is the member who can receive results, they specify the results destination and format. They also provide a service role ARN to write to the results destination.

If the invited member is the member who is responsible to pay for compute costs, they accept their payment responsibilities before joining the collaboration.

**To create a membership and join a collaboration**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your member AWS account.

1. In the left navigation pane, choose **Collaborations**.

1. On the **Available to join** tab, for **Collaborations available to join**, choose the **Name** of the collaboration.

1. On the collaboration details page, in the **Overview** section, view the collaboration details, including **Your member details** and a list of the other members.

   Verify that the AWS account IDs for each member of the collaboration are the ones with whom you intend to enter in to the collaboration.

1. Choose **Create membership**.

1. On the **Create membership** page, in the **Overview**, view the **Collaboration name**, **Collaboration description**, AWS account ID of the **Collaboration creator**, **Your member details**, and the AWS account ID of the member who will **Pay for queries**.

1. If the collaboration creator has chosen to enable **Analysis logging**, choose one of the following options for **Log storage in Amazon CloudWatch Logs**:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/create-membership.html)
**Note**  
After you turn on **Analysis logging**, it can take a few minutes for log storage to be set up and start receiving logs in Amazon CloudWatch Logs. During this brief period, the member who can query might run queries that don’t actually send logs.

1. If the collaboration creator enabled **Detailed monitoring** for this collaboration, choose whether you want to receive detailed observability metrics in your CloudWatch account.

   For **Detailed monitoring**:  
**Detailed monitoring options**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/create-membership.html)
**Note**  
Detailed monitoring metrics are only available to members who can run queries (analysis runners) and members who are configured as payors for the collaboration.

1. If **Your member abilities** includes **Receive results**, for **Results settings defaults**:

   1. For **Query results**, choose the **Set default settings for queries** checkbox, and then specify the **Results destination in Amazon S3** by entering the S3 destination or choose **Browse S3** to select from a list of available S3 buckets.  
**Example**  

      For example: **s3://bucket/prefix**

      1. For the **Result format**, choose either **CSV** or **PARQUET**. 

      1. (Spark only) For the **Result files**, choose either **Multiple** or **Single**.

      1. (Optional) For **Service access**, if you want to deliver queries that take up to 24 hours to your S3 destination, select the **Add a service role to support queries that take up to 24 hours to complete** check box. 

         Large queries that take up to 24 hours to complete will be delivered to your S3 destination. 

         If you don't select the check box, only queries that complete within 12 hours will be delivered to your S3 location.
**Note**  
You must either select an existing service role or have permissions to create a new one. For more information, see [Create a service role to receive results](setting-up-roles.md#create-role-write-results).

      1. Specify the **Service access** permissions by selecting either **Create and use a new service role** or **Use an existing service role**.

------
#### [ Create and use a new service role ]
         + AWS Clean Rooms creates a service role with the required policy for this table.
         + The default **Service role name** is `cleanrooms-result-receiver-<timestamp>`
         + You must have permissions to create roles and attach policies.

------
#### [ Use an existing service role ]

         1. Choose an **Existing service role name** from the dropdown list.

            The list of roles are displayed if you have permissions to list roles.

            If you don't have permissions to list roles, you can enter the Amazon Resource Name (ARN) of the role that you want to use.

         1. View the service role by choosing the **View in IAM** external link.

            If there are no existing service roles, the option to **Use an existing service role** is unavailable.

            By default, AWS Clean Rooms doesn't attempt to update the existing role policy to add necessary permissions. 

------
**Note**  
AWS Clean Rooms requires permissions to query according to the analysis rules. For more information about permissions for AWS Clean Rooms, see [AWS managed policies for AWS Clean Rooms](security-iam-awsmanpol.md).
If the role doesn’t have sufficient permissions for AWS Clean Rooms, you receive an error message stating that the role doesn't have sufficient permissions for AWS Clean Rooms. The role policy must be added before proceeding.
If you can’t modify the role policy, you receive an error message stating that AWS Clean Rooms couldn't find the policy for the service role.

   1. For **Job results**, choose the **Set default settings for jobs** checkbox, and then specify the **Results destination in Amazon S3** by entering the S3 destination or choose **Browse S3** to select from a list of available S3 buckets.  
**Example**  

      For example: **s3://bucket/prefix**

      1. Specify the **Service access** permissions by choosing an **Existing service role name** from the dropdown list.

1. If you want to enable **Tags** for the membership resource, choose **Add new tag** and then enter the **Key** and **Value** pair. 

1. If the collaboration creator has designated you as the member who will **Pay for queries** or **Pay for queries and jobs**, indicate your acceptance by selecting the **I agree to pay for the compute costs in this collaboration** checkbox.
**Note**  
You must select this checkbox to proceed.  
For more information about how pricing is calculated, see [Pricing for AWS Clean Rooms](what-is.md#pricing).

   If you are the [member paying for query compute costs](glossary.md#glossary-member-paying-for-query-compute) or the [member paying for queries and job compute costs](glossary.md#glossary-member-paying-for-query-job-compute) but not the [member who can query](glossary.md#glossary-member-who-can-query), it is recommended that you use AWS Budgets to configure a budget for AWS Clean Rooms and receive notifications once the maximum budget has been reached. For more information about setting up a budget, see [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) in the *AWS Cost Management User Guide*. For more information about setting up notifications, see [Creating an Amazon SNS topic for budget notifications](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-sns-policy.html) in the *AWS Cost Management User Guide*. If the maximum budget has been reached, you can contact the member who can run queries and jobs or [leave the collaboration](leave-collab.md). If you leave the collaboration, no more queries will be allowed to run, and therefore you will no longer be billed for query compute costs.

1. If you are sure that you want to create a membership and join the collaboration, choose **Create membership**.

You are given read access to the collaboration metadata. This includes information such as the display name and description of the collaboration, in addition to all the names and AWS account IDs of other members. 

You are now ready to: 
+ [Prepare your data table to be queried in AWS Clean Rooms](prepare-data.md). (Optional if you want to query your own event data or if you want to query identity data.)
+ [Associate the configured table to your collaboration](associate-configured-table.md) – if you want to query event data.
+ [Add an analysis rule for the configured table](add-analysis-rule.md) – if you want to query event data.
+ [Create and associate a new ID namespace](create-new-id-namespace.md) – if you want to create an ID mapping table to query identity data.

For information about how to leave a collaboration, see [Leaving a collaboration](leave-collab.md).