

# Updating a membership
<a name="update-membership"></a>

After you join a collaboration, you can update your membership settings. You can change your analysis logging settings, default result settings, and payment configuration.

For information about how to update a membership using the AWS SDKs, see the *[AWS Clean Rooms API Reference](https://docs.aws.amazon.com/clean-rooms/latest/apireference/Welcome.html)*.

You must already be a member of a collaboration (have an active membership) to update membership settings. The available settings depend on your member abilities in the collaboration.

**Topics**
+ [Update analysis logging settings](#update-membership-logging)
+ [Update default result settings](#update-membership-results)
+ [Update payment configuration](#update-membership-payment)

## Update analysis logging settings
<a name="update-membership-logging"></a>

You can update your analysis logging settings to turn on or turn off log storage in Amazon CloudWatch Logs.

**To update analysis logging settings**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your member AWS account.

1. In the left navigation pane, choose **Memberships**.

1. Choose the membership name.

1. On the membership detail page, choose the **Logging** tab.

1. Choose **Edit logging settings**.

1. For **Log storage in Amazon CloudWatch Logs**, choose **Turn on** or **Turn off**.

1. Choose **Save changes**.

**Note**  
After you turn on or turn off **Analysis logging**, it can take a few minutes for the changes to take effect.

## Update default result settings
<a name="update-membership-results"></a>

You can update the default results destination in Amazon S3, the result format, and the service role for your membership.

**To update default result settings**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your member AWS account.

1. In the left navigation pane, choose **Memberships**.

1. Choose the membership name.

1. On the membership detail page, choose the **Results settings** tab.

1. Choose **Edit result settings**.

1. Update the result settings as needed:

   1. For **Results destination in Amazon S3**, enter the S3 destination or choose **Browse S3** to select from a list of available S3 buckets.  
**Example**  

      For example: **s3://bucket/prefix**

   1. For **Result format**, choose either **CSV** or **PARQUET**.

   1. For **Service access**, choose either **Create and use a new service role** or **Use an existing service role**.

------
#### [ Create and use a new service role ]
      + AWS Clean Rooms creates a service role with the required policy.
      + The default **Service role name** is `cleanrooms-result-receiver-<timestamp>`
      + You must have permissions to create roles and attach policies.

------
#### [ Use an existing service role ]

      1. Choose an **Existing service role name** from the dropdown list.

         If you don't have permissions to list roles, you can enter the Amazon Resource Name (ARN) of the role that you want to use.

------
**Note**  
For more information about the required service role permissions, see [Create a service role to receive results](setting-up-roles.md#create-role-write-results).

1. Choose **Save changes**.

## Update payment configuration
<a name="update-membership-payment"></a>

You can update your payment responsibilities for the membership.

**To update payment configuration**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your member AWS account.

1. In the left navigation pane, choose **Memberships**.

1. Choose the membership name.

1. On the membership detail page, choose the **Payment configuration** tab.

1. Choose **Edit payment configuration**.

1. Update your payment responsibilities as needed:

   1. If you are the [member paying for query compute costs](glossary.md#glossary-member-paying-for-query-compute), select or clear the **I agree to pay for the query compute costs in this collaboration** checkbox to accept or decline payment responsibility.

   1. If you are the [member paying for query and job compute costs](glossary.md#glossary-member-paying-for-query-job-compute), select or clear the **I agree to pay for the compute costs in this collaboration** checkbox to accept or decline payment responsibility for both query and job compute costs.

1. Choose **Save changes**.

**Note**  
We recommend that you use AWS Budgets to configure a budget for AWS Clean Rooms and receive notifications when the maximum budget is reached. For more information about pricing, see [Pricing for AWS Clean Rooms](what-is.md#pricing).

For more information about related tasks, see the following topics:
+ [Creating a membership and joining a collaboration](create-membership.md)
+ [Editing collaborations](edit-collaboration.md)