# Stopping cross-Region aggregation

###### Note

The _aggregation Region_ is now called the _home Region_. Some Security Hub CSPM API operations still use the older term aggregation
Region.

If you don't want AWS Security Hub CSPM to aggregate data, you can delete your finding aggregator. Alternatively, you can
keep your finding aggregator but not link any AWS Regions to the home Region by updating the existing aggregator
to the `NO_REGIONS` linking mode.

To change your home Region, you must delete your current finding aggregator and create a new one.

When you delete your finding aggregator, Security Hub CSPM stops aggregating data. It doesn't
remove any existing aggregated data from the home Region.

## Deleting the finding aggregator

(console)

You can delete your finding aggregator from the current home Region only.

In Regions other than the home Region, the **Finding
aggregation** panel on the Security Hub CSPM console displays a message that you must edit the
configuration in the home Region. Choose this message to display a link to
switch to the home Region.

Security Hub CSPM console

###### To stop cross-Region aggregation (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. Ensure that you're signed in to your current home Region.
3. In the Security Hub CSPM navigation menu, choose **Settings**, then
   choose **Regions**.
4. Under **Finding aggregation**, choose
   **Edit**.
5. Under **Aggregation Region**, choose **No
   aggregation Region**.
6. Choose **Save**.
7. On the confirmation dialog, in the confirmation field, type
   `Confirm`.
8. Choose **Confirm**.

Security Hub CSPM API
Use the [`DeleteFindingAggregator`](../../1.0/APIReference/API_DeleteFindingAggregator.md "../../1.0/APIReference/API_DeleteFindingAggregator.md") operation of the Security Hub CSPM API.
If you're using the AWS CLI, run the
[`delete-finding-aggregator`](../../../cli/latest/reference/securityhub/delete-finding-aggregator.md "../../../cli/latest/reference/securityhub/delete-finding-aggregator.md") command.

To identify
the finding aggregator to delete, provide the finding aggregator ARN. To
obtain the finding aggregator ARN, use the [`ListFindingAggregators`](../../1.0/APIReference/API_ListFindingAggregators.md "../../1.0/APIReference/API_ListFindingAggregators.md") operation or [`list-finding-aggregators`](../../../cli/latest/reference/securityhub/list-finding-aggregators.md "../../../cli/latest/reference/securityhub/list-finding-aggregators.md") command.

The following example deletes the finding aggregator. The command is run from the
current home Region, which is US East (N. Virginia).
This example is formatted for Linux, macOS, or Unix,
and it uses the backslash (\) line-continuation character to improve
readability.

```
`$``aws securityhub delete-finding-aggregator `arn:aws:securityhub:us-east-1:222222222222:finding-aggregator/123e4567-e89b-12d3-a456-426652340000` --region `us-east-1``
```
