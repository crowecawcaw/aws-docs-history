# Updating cross-Region aggregation

settings

You can update your current cross-Region aggregation settings in AWS Security Hub by changing the linked Regions or the current home Region.

Changes to cross-Region aggregation aren't implemented for an opt-in Region until you enable the Region in your AWS account.
Regions that AWS introduced on or after to March 20, 2019 are opt-in Regions.

When you stop aggregating data from a linked Region, AWS Security Hub doesn't remove any existing aggregated data from that Region that is accessible in the home Region.

You can't use the update procedures in this section to change the home Region. To change the home Region, you must do the following:

1. Delete the current cross-Region aggregation configuration. For instructions, see [Deleting cross-Region aggregation](sh-finding-aggregation-delete.md "sh-finding-aggregation-delete.md").
2. Change to the Region that you want to be the new home Region.
3. Enable cross-Region aggregation. For instructions, see [Deleting cross-Region aggregation](sh-finding-aggregation-delete.md "sh-finding-aggregation-delete.md").
   You must update the cross-Region aggregation configuration from the current home Region.

###### To change the linked Regions (console)

1. From the administrator account or in a standalone account open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. Sign in to the current aggregation Region.
3. In the Security Hub navigation menu, choose **Settings**, then choose **General**.
4. For Cross-Region aggregation, choose **Edit**.
5. For **Linked Regions**, update the selected linked Regions.
6. Choose **Save**.
