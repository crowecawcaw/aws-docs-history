# Deleting Aggregators for AWS Config

You can use the AWS Config console or the AWS CLI to delete your aggregators.

Deleting Aggregators (Console)

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Navigate to the **Aggregator** page, and choose the
   aggregator name.
3. Choose **Actions** and then choose
   **Delete**.

A warning message is displayed. Deleting an aggregator results in the
loss of all aggregated data. You cannot recover this data but data in
the source account(s) is not impacted. 4. Choose **Delete** to confirm your selection.

Deleting Aggregators (AWS CLI)
Enter the following command:

```
aws configservice delete-configuration-aggregator --configuration-aggregator-name MyAggregator
```

If successful, the command executes with no additional output.
