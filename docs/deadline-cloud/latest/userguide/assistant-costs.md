

# Costs
<a name="assistant-costs"></a>

The Deadline Cloud assistant incurs Amazon Bedrock usage costs in your AWS account. Costs are based on the number of input and output tokens processed during each interaction. Because the assistant uses cross-region inference, pricing is calculated based on your monitor's source Region.

For current pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

**Tip**  
The assistant displays context window usage during interactions to help you monitor token consumption.

## Tracking assistant costs
<a name="assistant-cost-tracking"></a>

Amazon Bedrock supports cost allocation by AWS Identity and Access Management (IAM) principal, which you can use to track and attribute assistant inference costs across teams, projects, or cost centers. To set up cost tracking for the assistant, tag the monitor user role with attributes that represent your organizational structure, then activate those tags for cost allocation.

To complete this procedure, you need IAM permissions to tag roles and access to the Billing console.

**To set up cost tracking for the assistant**

1. Tag the IAM role that your monitor users assume. You can add tags in the IAM console or by using the AWS CLI. The following example uses the AWS CLI:

   ```
   aws iam tag-role \
       --role-name {{YourMonitorUserRole}} \
       --tags Key=team,Value={{YourTeam}} Key=project,Value={{YourProject}}
   ```

   Choose tag keys that align with your organizational structure, such as `team`, `project`, or `cost-center`.

1. Activate the tags for cost allocation:

   1. Open the [Billing console](https://console.aws.amazon.com/costmanagement/home#/cost-allocation-tags).

   1. In the navigation pane, under **Cost Organization**, choose **Cost Allocation Tags**.

   1. Find and select your IAM principal tags, then choose **Activate**.

1. In (), filter or group by your activated IAM principal tags to view costs.

   1. Choose **Tag** as the grouping dimension.

   1. Select your tag key.

After you apply tags to your IAM roles, it can take up to 24 hours for the tag keys to appear on the cost allocation tags page. It can then take up to 24 hours for the tags to activate.

For line-item cost attribution, create a AWS Cost and Usage Report () data export and select **Include caller identity (IAM principal) allocation data**. The export includes a `line_item_iam_principal` column that records the IAM ARN for each Amazon Bedrock request, along with your IAM principal tags prefixed with `iamPrincipal/`.

For more information, see [Using IAM principal for cost allocation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/iam-principal-cost-allocation.html) in the *AWS Billing User Guide*.