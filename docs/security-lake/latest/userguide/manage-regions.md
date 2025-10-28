# Managing Regions in Security Lake

Amazon Security Lake can collect security logs and events across AWS Regions in which you've
enabled the service. For each Region, your data is stored in a different Amazon S3 bucket. You
can specify different data lake configurations (for example, different sources and retention
settings) for different Regions. You can also define one or more rollup Regions to
consolidate data from multiple Regions.

## Checking Region status

Security Lake can collect data across multiple AWS Regions. To track the state of your
data lake, it can be helpful to understand how each Region is currently configured.
Choose your preferred access method, and follow these steps to get the current status of
a Region.

Console

###### To check Region status

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. In the navigation pane, choose **Regions**. The
   **Regions** page appears, providing an overview
   of the Regions in which Security Lake is currently enabled.
3. Select a Region, and then choose **Edit** to see
   details for that Region.

API
To get the status of log collection in the current Region, use the [GetDataLakeSources](../APIReference/API_GetDataLakeSources.md "../APIReference/API_GetDataLakeSources.md") operation of the Security Lake API. If you're using the AWS CLI,
run the [get-data-lake-sources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-data-lake-sources.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-data-lake-sources.html") command. For the
`accounts` parameter, specify one or more AWS account IDs as a list.
If your request succeeds, Security Lake returns a snapshot for those accounts in
the current Region, including which AWS sources Security Lake is collecting data
from and the status of each source. If you don't include the `accounts` parameter, the response
includes the status of log collection for all accounts in which Security Lake is configured in the current Region.

For example, the following AWS CLI command retrieves log collection status for the specified accounts in the current Region.
This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake get-data-lake-sources \
--accounts "`123456789012`" "`111122223333`"`
```

The following AWS CLI command lists log collection status for all accounts and enabled sources in the specified Region.
This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake get-data-lake-sources \
--regions "`us-east-1`" \
--query 'dataLakeSources[].[account,sourceName]'`
```

To determine whether you've enabled Security Lake for a Region, use the [ListDataLakes](../APIReference/API_ListDataLakes.md "../APIReference/API_ListDataLakes.md") operation. If you're using the AWS CLI, run the
[list-data-lakes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-data-lakes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-data-lakes.html") command. For the `regions`
parameter, specify the Region code for the Region—for example,
`us-east-1` for the US East (N. Virginia) Region.
For a list of Region codes, see [Amazon Security Lake endpoints](../../../general/latest/gr/securitylake.md "../../../general/latest/gr/securitylake.md") in the _AWS General Reference_. The `ListDataLakes` operation
returns the data lake configuration settings for each Region that you
specify in your request. If you don't specify a Region, Security Lake returns the status and configuration settings
of your data lake in each Region in which Security Lake is available.

For example, the following AWS CLI command shows the status and configuration settings of your data lake in
the `eu-central-1` Region. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake list-data-lakes \
--regions "`us-east-1`" "`eu-central-1`"`
```

## Changing Region settings

Choose your preferred method, and follow these instructions to update settings for
your data lake in one or more AWS Regions.

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. In the navigation pane, choose
   **Regions**.
3. Select a Region, and then choose **Edit**.
4. Select the check box for **Override sources for all
   accounts in _<Region>_** to confirm that your
   selections here override previous selections for this Region.
5. For **Select storage classes**, choose
   **Add transition** to add new storage classes
   for your data.
6. For **Tags**, optionally assign or edit the tags
   for the Region. A _tag_ is a label
   that you can define and assign to certain types of AWS resources,
   including the data lake configuration for your AWS account in a
   particular Region. To learn more, see [Tagging Security Lake resources](tagging-resources.md "tagging-resources.md").
7. To turn a Region into a rollup Region, choose **Rollup
   Regions** (under **Settings**) in the
   navigation pane. Then choose **Modify**. In the
   **Select rollup Regions** section, choose
   **Add rollup Region**. Select the contributing
   Regions, and provide Security Lake with permission to replicate data
   across multiple Regions. When you finish, choose
   **Save** to save your changes.

API
To update Region settings for your data lake programmatically, use the
[UpdateDataLake](../APIReference/API_UpdateDataLake.md "../APIReference/API_UpdateDataLake.md") operation of the Security Lake API. If you're using the AWS CLI, run the
[update-data-lake](../../../cli/latest/reference/securitylake/update-data-lake.md "../../../cli/latest/reference/securitylake/update-data-lake.md") command. For the
`region` parameter, specify the Region code for the Region
that you want to change the settings for—for example,
`us-east-1` for the US East (N. Virginia) Region.
For a list of Region codes, see [Amazon Security Lake endpoints](../../../general/latest/gr/securitylake.md "../../../general/latest/gr/securitylake.md") in the _AWS General Reference_.

Use additional parameters to specify a new value for each setting that you
want to change—for example, the encryption key
(`encryptionConfiguration`) and retention settings
(`lifecycleConfiguration`).

For example, the following AWS CLI command updates the data expiration and storage class transition settings for the
`us-east-1` Region. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `update-data-lake \
--configurations '[{"region":"`us-east-1`","lifecycleConfiguration": {"expiration":{"days":`500`},"transitions":[{"days":`45`,"storageClass":"`ONEZONE_IA`"}]}}]'`
```
