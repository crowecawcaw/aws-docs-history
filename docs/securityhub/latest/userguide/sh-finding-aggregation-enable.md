# Enabling cross-Region aggregation

You must enable cross-Region aggregation from the AWS Region that you want to designate as the home Region.

To enable cross-Region aggregation, you create a Security Hub resource called a finding aggregator. The finding aggregator resource specifies your home Region and linked Regions (if any).

You can't use an AWS Region that is disabled by default as your home Region.
For a list of Regions that are disabled by default, see Enabling a Region in the AWS General Reference.

When you enable cross-Region aggregation, you choose to specify one or more linked Regions if you wish.
Enabling cross-Region aggregation does not enable Security Hub in that region. To enable Security Hub in a region refer to Creating a policy as the delegated administrator to manage member accounts in the Security Hub user guide.

###### To enable cross-Region aggregation (console)

1. From the administrator account or in a standalone account open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home")
2. Using the AWS Region selector, sign in to the Region that you want to use as the aggregation Region.
3. In the Security Hub navigation menu, choose **Settings** and then **General**.
4. In the Cross-Region aggregation section choose **Configure**.
5. By default, the home Region is set to **No aggregation Region**.
6. Under **Home Region**, select the option to designate the current Region as the home Region.
7. Optionally, for **Linked Regions**, select the Regions to aggregate data from.
8. Choose **Save**.
