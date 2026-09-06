

# Enabling cross-Region aggregation
<a name="finding-aggregation-enable"></a>

**Note**  
The *aggregation Region* is now called the *home Region*. Some Security Hub CSPM API operations still use the older term aggregation Region.

You must enable cross-Region aggregation from the AWS Region that you want to designate as the home Region.

To enable cross-Region aggregation, you create a Security Hub CSPM resource called a finding aggregator. The finding aggregator resource specifies your home Region and linked Regions (if any).

You can't use an AWS Region that is disabled by default as your home Region. For a list of Regions that are disabled by default, see [Enabling a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable) in the *AWS General Reference*.

When you enable cross-Region aggregation, you choose to specify one or more linked Regions if you wish. You can also choose whether to automatically link new Regions when Security Hub CSPM begins to support them and you have opted into them.

------
#### [ Security Hub CSPM console ]

**To enable cross-Region aggregation**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. Using the AWS Region selector, sign in to the Region that you want to use as the aggregation Region.

1. In the Security Hub CSPM navigation menu, choose **Settings** and then **Regions**.

1. For **Finding aggregation**, choose **Configure finding aggregation**.

   By default, the home Region is set to **No aggregation Region**.

1. Under **Aggregation Region**, select the option to designate the current Region as the home Region.

1. Optionally, for **Linked Regions**, select the Regions to aggregate data from.

1. To automatically aggregate data from new Regions in the partition as Security Hub CSPM supports them and you opt into them, select **Link future Regions**.

1. Choose **Save**.

------
#### [ Security Hub CSPM API ]

From the Region that you want to use as the home Region, use the [`CreateFindingAggregator`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateFindingAggregator.html) operation of the Security Hub CSPM API. If you use the AWS CLI, run the [create-finding-aggregator](https://docs.aws.amazon.com/cli/latest/reference/securityhub/create-finding-aggregator.html) command.

For `RegionLinkingMode`, choose one of the following options:
+ `ALL_REGIONS` – Security Hub CSPM aggregates data from all Regions. Security Hub CSPM also aggregates data from new Regions as they are supported and you opt into them.
+ `ALL_REGIONS_EXCEPT_SPECIFIED` – Security Hub CSPM aggregates data from all Regions except for Regions that you want to exclude. Security Hub CSPM also aggregates data from new Regions as they are supported and you opt into them. Use `Regions` to provide the list of Regions to exclude from aggregation.
+ `SPECIFIED_REGIONS` – Security Hub CSPM aggregates data from a selected list of Regions. Security Hub CSPM does not aggregate data automatically from new Regions. Use `Regions` to provide the list of Regions to aggregate from.
+ `NO_REGIONS` – Security Hub CSPM doesn't aggregate data because you don't select any linked Regions.

The following example configures cross-Region aggregation. The home Region is US East (N. Virginia). The linked Regions are US West (N. California) and US West (Oregon). This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securityhub create-finding-aggregator --region {{us-east-1}} --region-linking-mode {{SPECIFIED_REGIONS}} --regions {{us-west-1 us-west-2}}
```

------