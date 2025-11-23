# Deleting cross-Region aggregation

If you don't want AWS Security Hub to aggregate data, you can delete your finding aggregator. Alternatively, you can keep your finding aggregator but not link any AWS Regions to the home Region by updating the existing aggregator to have no linked regions selected.

To change your home Region, you must delete your current finding aggregator and create a new one.

When you delete your finding aggregator, Security Hub stops aggregating data. It doesn't remove any existing aggregated data from the home Region.

###### Deleting the finding aggregator (console)

You can delete your finding aggregator from the current home Region only.

In Regions other than the home Region, the Finding aggregation panel on the Security Hub console displays a message that you must edit the configuration in the home Region. Choose this message to display a link to switch to the home Region.

###### To stop cross-Region aggregation (console)

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. Ensure that you're signed in to your current home Region.
3. In the Security Hub navigation menu, choose **Settings**, then choose **General**.
4. Under Cross-Region aggregation, choose **Edit**.
5. Under **Aggregation Region**, choose **No aggregation Region**.
6. Choose **Save**.
7. On the confirmation dialog, in the confirmation field, type `Confirm`.
8. Choose **Confirm**.
