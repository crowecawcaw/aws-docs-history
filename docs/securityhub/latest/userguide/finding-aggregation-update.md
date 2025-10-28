# Updating cross-Region aggregation

settings

###### Note

The _aggregation Region_ is now called the _home Region_. Some Security Hub CSPM API operations still use the older term aggregation
Region.

You can update your current cross-Region aggregation settings in AWS Security Hub CSPM by changing the linked
Regions or the current home Region. You can also change whether to
automatically aggregate data from new AWS Regions that Security Hub CSPM is supported in.

Changes to cross-Region aggregation aren't implemented for an opt-in Region until you enable the Region
in your AWS account. Regions that AWS introduced on or after to March 20, 2019 are opt-in Regions.

When you stop aggregating data from a linked Region, AWS Security Hub CSPM doesn't remove any
existing aggregated data from that Region that is accessible in the home Region.

You can't use the update procedures in this section to change the home Region. To change the
home Region, you must do the following:

1. Stop cross-Region aggregation. For instructions, see [Stopping cross-Region aggregation](finding-aggregation-stop.md "finding-aggregation-stop.md").
2. Change to the Region that you want to be the new home Region.
3. Enable cross-Region aggregation. For instructions, see [Enabling cross-Region aggregation](finding-aggregation-enable.md "finding-aggregation-enable.md").
   You must update the cross-Region aggregation configuration from the current
   home Region.

Security Hub CSPM console

###### To change the linked Regions

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in to the current aggregation Region. 2. In the Security Hub CSPM navigation menu, choose **Settings**, then
choose **Regions**. 3. For **Finding aggregation**, choose
**Edit**. 4. For **Linked Regions**, update the selected linked
Regions. 5. If needed, change whether **Link future Regions** is
selected. This setting determines whether Security Hub CSPM automatically links new
Regions as it adds support for them and you opt into them. 6. Choose **Save**.

Security Hub CSPM API
Use the [`UpdateFindingAggregator`](../../1.0/APIReference/API_UpdateFindingAggregator.md "../../1.0/APIReference/API_UpdateFindingAggregator.md") operation. If you use the AWS CLI, run the
[update-finding-aggregator](../../../cli/latest/reference/securityhub/update-finding-aggregator.md "../../../cli/latest/reference/securityhub/update-finding-aggregator.md") command. To
identify the finding aggregator, you must provide the finding aggregator
ARN. To obtain the finding aggregator ARN, use the [`ListFindingAggregators`](../../1.0/APIReference/API_ListFindingAggregators.md "../../1.0/APIReference/API_ListFindingAggregators.md") operation or [list-finding-aggregators](../../../cli/latest/reference/securityhub/list-finding-aggregators.md "../../../cli/latest/reference/securityhub/list-finding-aggregators.md") command..

If the linking mode is
`ALL_REGIONS_EXCEPT_SPECIFIED` or `SPECIFIED_REGIONS`, you
can change the list of excluded or included Regions. If you want to change the Region linking mode to
`NO_REGIONS`, you shouldn't provide a Regions list.

When you change the list of excluded or included Regions, you must provide the
full list with the updates. For example, suppose you currently aggregate findings
from US East (Ohio), and want to also aggregate findings from
US West (Oregon). You must provide a
`Regions` list that contains both US East (Ohio) and
US West (Oregon).

The following example updates cross-Region aggregation to selected Regions. The command is run from the
current home Region, which is US East (N. Virginia). The linked Regions
are US West (N. California) and US West (Oregon).
This example is formatted for Linux, macOS, or Unix,
and it uses the backslash (\) line-continuation character to improve
readability.

```
aws securityhub update-finding-aggregator --region `us-east-1` --finding-aggregator-`arn arn:aws:securityhub:us-east-1:222222222222:finding-aggregator/123e4567-e89b-12d3-a456-426652340000` --region-linking-mode SPECIFIED_REGIONS --regions `us-west-1 us-west-2`
```
