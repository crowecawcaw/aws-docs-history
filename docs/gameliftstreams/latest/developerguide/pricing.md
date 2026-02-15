# Managing usage and bills for Amazon GameLift Streams

This topic covers how to monitor and manage your Amazon GameLift Streams usage, costs, and billing to optimize your streaming expenses.

Also see the Amazon GameLift Streams [Pricing page](https://aws.amazon.com/gamelift/streams/pricing/ "https://aws.amazon.com/gamelift/streams/pricing/") for the following information:

- **Cost breakdown**: Understand what AWS charges you for
  when you use Amazon GameLift Streams.
- **Amazon GameLift Streams rates**: See how much Amazon GameLift Streams costs and
  compare different options.
- **Stream capacity reservation**: Plan ahead and ensure
  that you have enough stream capacity to meet your customer demands.

## Review your Amazon GameLift Streams bills and usage

You can review your Amazon GameLift Streams bills and usage by using the AWS Billing and Cost Management tools in the AWS Console or AWS CLI.

To view your bill through the AWS Console, refer to [Viewing your bill](../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md "../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md") in the AWS Billing User Guide.

To view your bill through the AWS CLI, call [`GetCostAndUsage`](../../../aws-cost-management/latest/APIReference/API_GetCostAndUsage.md "../../../aws-cost-management/latest/APIReference/API_GetCostAndUsage.md") using the Billing and Cost Management
API. For example, use the following command to retrieve a monthly bill for Amazon GameLift Streams, and replace the dates with ones relevant to you.

###### Example: Use `GetCostAndUsage` API to view bill

```
aws ce get-cost-and-usage /
    --time-period Start=`2023-01-01`,End=`2023-01-31` /
    --granularity `MONTHLY` /
    --metrics `BlendedCost` /
    --filter `Amazon GameLift Streams-bill-filter.json`
```

where the filter, such as `Amazon GameLift Streams-bill-filter.json`, specifies the Amazon GameLift Streams service as follows:

```
{
    "Dimensions": {
        "Key": "SERVICE",
        "Values": ["Amazon Amazon GameLift Streams"]
    }
}
```

## Best practices to manage Amazon GameLift Streams costs

We strongly recommend that you use the following tools and techniques to manage your Amazon GameLift Streams costs to avoid unexpected costs.

### Create billing alerts to monitor usage

Set up billing alerts using AWS Budgets, which enables you to track your costs and usage, and respond quickly to alerts to avoid unexpected costs. You can also configure
the billing alert to trigger actions that help you stay within budget. By default, budgets
include all of your AWS services. To specify a budget for Amazon GameLift Streams only, add a
[budget filter](../../../cost-management/latest/userguide/budgets-create-filters.md "../../../cost-management/latest/userguide/budgets-create-filters.md").

For more information, see the following topics:

- [Creating a budget](../../../cost-management/latest/userguide/budgets-create.md "../../../cost-management/latest/userguide/budgets-create.md")
- [Best practices for AWS Budgets](../../../cost-management/latest/userguide/budgets-best-practices.md "../../../cost-management/latest/userguide/budgets-best-practices.md")

### Scale stream groups to zero capacity

Allocated stream capacity continues to incur costs even when they're not currently hosting stream
sessions. Scale stream groups to zero capacity when not in use to avoid unnecessary cost.
This prevents your stream group from allocating resources. When you set always-on and on-demand stream capacity to zero, all connected streams end. When you're ready, you can reuse your stream group by scaling capacity back up.

For instructions, refer to [Edit capacity](stream-groups.md#stream-groups-edit-capacity "stream-groups.md#stream-groups-edit-capacity").

###### Warning

Avoid deleting a stream group, unless you don't plan to use the stream group again. If you delete a stream group, you cannot restore the original stream group and must create a new one.

### Delete original application files

To optimize storage cost, you can delete the original application files that you uploaded to an Amazon S3 bucket. It's safe to delete the files if the application is in **Ready** status. At that point, Amazon GameLift Streams has a snapshot of the application files and no longer accesses your original files.
